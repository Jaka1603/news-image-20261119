#!/usr/bin/env python3
"""Entry point for the news-image-20261119 make.fun entry.

The artwork for this entry lives in ``image.jpg`` beside this file.
Running the program checks that the artwork obeys the competition's
mechanical limits and then copies it, untouched, to
``/output/entry.png``.  The copy is byte-for-byte, so two runs always
produce the same file; the program prints the SHA-256 of the bytes it
wrote and reads the copy back to prove the digest is right.

Only the Python standard library is used.
"""

import hashlib
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE_NAME = "image.jpg"
DEST_DIR = "/output"
DEST_NAME = "entry.png"

MAX_BYTES = 1024 * 1024          # competition ceiling: 1 MiB
MAX_SIDE = 1024                  # competition ceiling: 1024 x 1024 px

JPEG_MAGIC = b"\xff\xd8\xff"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

# JPEG markers that carry no payload and no length field.
_JPEG_STANDALONE = {0x01, 0xD8, 0xD9} | set(range(0xD0, 0xD8))
# Start-of-frame markers whose segment holds the picture dimensions.
_JPEG_SOF = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
             0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}


class Reject(Exception):
    """The artwork breaks a rule; the message says which one."""


def png_dimensions(blob):
    """Width and height from a PNG's IHDR chunk."""
    # Layout: 8-byte signature, then chunk length (4), type (4),
    # and IHDR data beginning with width and height as big-endian u32.
    if len(blob) < 24:
        raise Reject("PNG header is truncated")
    if blob[12:16] != b"IHDR":
        raise Reject("first PNG chunk is not IHDR")
    width, height = struct.unpack(">II", blob[16:24])
    return width, height


def jpeg_dimensions(blob):
    """Width and height from the first start-of-frame segment."""
    pos = 2  # skip the SOI marker (FF D8) already matched as magic
    size = len(blob)
    while pos + 1 < size:
        if blob[pos] != 0xFF:
            raise Reject("JPEG segment does not start with 0xFF")
        marker = blob[pos + 1]
        if marker in _JPEG_STANDALONE:
            pos += 2
            continue
        if pos + 4 > size:
            raise Reject("JPEG segment header is truncated")
        seg_len = struct.unpack(">H", blob[pos + 2:pos + 4])[0]
        if seg_len < 2:
            raise Reject("JPEG segment length is invalid")
        if marker in _JPEG_SOF:
            # Segment body: precision (1), height (2), width (2).
            if pos + 9 > size:
                raise Reject("JPEG frame header is truncated")
            height, width = struct.unpack(">HH", blob[pos + 5:pos + 9])
            return width, height
        pos += 2 + seg_len
    raise Reject("no start-of-frame segment found in JPEG")


def inspect(blob):
    """Validate size, format and dimensions; return a short summary."""
    if len(blob) == 0:
        raise Reject("image file is empty")
    if len(blob) > MAX_BYTES:
        raise Reject(
            "image is %d bytes, over the %d-byte limit"
            % (len(blob), MAX_BYTES))
    if blob.startswith(PNG_MAGIC):
        kind = "PNG"
        width, height = png_dimensions(blob)
    elif blob.startswith(JPEG_MAGIC):
        kind = "JPEG"
        width, height = jpeg_dimensions(blob)
    else:
        raise Reject("magic bytes are neither JPEG nor PNG")
    if width < 1 or height < 1:
        raise Reject("image dimensions are zero")
    if width > MAX_SIDE or height > MAX_SIDE:
        raise Reject(
            "image is %dx%d, over the %dx%d limit"
            % (width, height, MAX_SIDE, MAX_SIDE))
    return "%s %dx%d, %d bytes" % (kind, width, height, len(blob))


def main():
    src = os.path.join(HERE, SOURCE_NAME)
    if not os.path.isfile(src):
        print("error: %s not found next to main.py" % SOURCE_NAME,
              file=sys.stderr)
        return 1
    with open(src, "rb") as fh:
        blob = fh.read()
    try:
        summary = inspect(blob)
    except Reject as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1

    os.makedirs(DEST_DIR, exist_ok=True)
    dest = os.path.join(DEST_DIR, DEST_NAME)
    with open(dest, "wb") as fh:
        fh.write(blob)

    digest = hashlib.sha256(blob).hexdigest()

    # Read the copy back: what landed on disk must hash to the same
    # digest, otherwise something corrupted the write.
    with open(dest, "rb") as fh:
        again = hashlib.sha256(fh.read()).hexdigest()
    if again != digest:
        print("error: written file digest mismatch (%s != %s)"
              % (again, digest), file=sys.stderr)
        return 1

    print("%s: %s" % (summary, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
