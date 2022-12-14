def get_first_start(marker_size: int) -> int:
    buffer = open("input.txt").read().strip()
    for offset in range((len(buffer) - marker_size) + 1):
        limit = offset + marker_size
        if len(set(buffer[offset:limit])) == marker_size:
            return limit
    return 0


def get_first_start_of_packet():
    packet_marker_size = 4
    return get_first_start(packet_marker_size)


print(get_first_start_of_packet())
assert get_first_start_of_packet() == 1723


def get_first_start_of_message():
    message_marker_size = 14
    return get_first_start(message_marker_size)


print(get_first_start_of_message())
assert get_first_start_of_message() == 3708
