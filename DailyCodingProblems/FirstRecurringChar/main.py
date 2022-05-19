def first_recurring_character(input_str: str) -> str | None:
    """
    Given a string, find the first recurring character in it.
    If there are no recurring characters, return None.

    This solution is definetely more effecient than using sets or dicts.
    But it assumes that the input string is ASCII characters only.

    Args:
        input_str (str): _description_

    Returns:
        str | None: _description_
    """
    out_char: str = None

    char_count = [0] * 256
    for char in input_str:
        char_count[ord(char)] += 1
        if char_count[ord(char)] > 1:
            out_char = char
            break

    return out_char


def main():
    input_strings = ["abac", "aabbc", "acbbac", "plenty", "abcdef", ""]
    output_char = ["a", "a", "b", None, None, None]

    for idx, input_str in enumerate(input_strings):
        print(
            f"Input: {input_str}\tExpected Output: {output_char[idx]}\tOutput: {first_recurring_character(input_str)}"
        )


if __name__ == "__main__":
    main()
