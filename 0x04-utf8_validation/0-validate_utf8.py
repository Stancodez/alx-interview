#!/usr/bin/python3
def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0

    # Masks for the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's to determine byte size
            while mask & num:
                num_bytes += 1
                mask >>= 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # Invalid scenarios (byte count must be 2 to 4)
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Subsequent bytes must have a leading 10
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0

