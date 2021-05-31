from django.db import models


class Letter(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.title


class Session(models.Model):
    """`requests.Session`을 pickle을 이용해 저장

    Fields:
        `created` (DateTime): 세션 생성 시각
        `session_path` (FilePathField) : `session.pkl` 저장 장소
    """
    created = models.DateTimeField()
    session_path = models.FilePathField()

    def __str__(self) -> str:
        return self.title
