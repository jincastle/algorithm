# 이 그림책 문제에서 n과 p가 주어졌을 때 p 페이지에 도달하기 위해 넘겨야 하는 최소 페이지 수를 찾아 인쇄하십시오.


def pageCount(n, p):
    # Write your code here
    page_in_book = p//2
    total_pages = n//2

    from_front = page_in_book
    from_back = total_pages - page_in_book

    return min(from_front, from_back)
