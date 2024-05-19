from rest_framework.pagination import CursorPagination


class StoriesRatingPagination(CursorPagination):
    page_size = 100
    ordering = '-avg_rating'