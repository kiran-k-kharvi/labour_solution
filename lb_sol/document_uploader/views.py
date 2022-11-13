from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from document_uploader.models import Document
from document_uploader.serializers import DocumentSerializer
from lb_sol.helpers.localize import localizable_messages


class DocumentView(ViewSet):
    queryset = Document.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = DocumentSerializer

    def list(self, request):
        user = request.user
        doc_list = self.queryset.filter(user=user).order_by('id')
        serialized_data = DocumentSerializer(instance=doc_list, many=True)
        return Response(data={"result": serialized_data.data})

    def create(self, request):
        user = request.user
        new_file = request.FILES.get('document')
        if new_file:
            Document.objects.create(user=user, document=new_file)
            return Response(status=status.HTTP_201_CREATED)
        return Response(data={"error": localizable_messages.get('no_doc_received')}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = request.user
        document = Document.objects.filter(user=user, id=pk)
        if document.exists():
            document.delete()
            return Response(data={"message": localizable_messages.get('deleted')}, status=status.HTTP_200_OK)
        return Response(data={"message": localizable_messages.get('not_found')}, status=status.HTTP_404_NOT_FOUND)
