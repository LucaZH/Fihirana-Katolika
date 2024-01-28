from utils.pagination import FihiranapPagination

url_dera = "https://katolika.org/fihirana/boky/show/4"
Pagination = FihiranapPagination(url_dera)

print(Pagination.generate_pagination_links())