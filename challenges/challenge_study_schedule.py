def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    for begin, end in permanence_period:

        if not isinstance(begin, int) or not isinstance(end, int):
            return None

        if target_time in range(begin, end + 1):
            counter += 1

    return counter
