from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'per-page'
    def get_paginated_response(self, data):
        return Response(
            {   "data":data,
                "_meta":{
                    "currentPage":self.page.number,
                    "pageCount":self.page.paginator.num_pages,
                    "perPage":self.page.paginator.per_page,
                    "totalCount":self.page.paginator.count
                }
            }
        )