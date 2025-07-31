def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    from stats import get_num_words
    from stats import count_letters
#    print(count_letters(sys.argv[2]))
    from stats import sorting  
    words = (get_num_words(sys.argv[1]))
    to_print = (sorting(count_letters(sys.argv[1])))
    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}... 
----------- Word Count ---------- 
Found {words} total words 
--------- Character Count -------"""
)
    for key in to_print:
        print(f"{key['char']}: {key['num']}")
    print("============ BOOKBOT ============")
main()