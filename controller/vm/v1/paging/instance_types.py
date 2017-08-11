from rest_framework import pagination

class CustomInstanceTypesPaginator(pagination.PageNumberPagination):
    def get_data_response(self, data):
        # paginator = Paginator(data, 20)
        # try:
        #     data_res = paginator.page(page)
        # except PageNotAnInteger:
        #     data_res = paginator.page(1)
        # except EmptyPage:
        #     data_res = paginator.page(paginator.num_pages)
        # response_serializer = InstanceTypeList(data_res,many=True)
        return {'count': self.page.paginator.count,
                'data': data}