from rest_framework import pagination

class CustomInstancePaginator(pagination.PageNumberPagination):
    def get_data_response(self, data):
        return {'count': self.page.paginator.count,
                'data': data}