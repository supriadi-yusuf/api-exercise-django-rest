from rest_framework import filters

class SupriFilter(filters.BaseFilterBackend):
    #print('main filterrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    #print(dir(filters.BaseFilterBackend))
        #filter_queryset
    def filter_queryset(self, request, queryset, view):
        #print(len(queryset))
        #print(queryset)
        #raise 'test'
        print('filterrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        return queryset
        #return queryset.filter(owner=request.user)

        #get_schema_fields
    def get_schema_fields(self, view):
        #raise 'test2'
        print('filterrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr2')
        #pass
