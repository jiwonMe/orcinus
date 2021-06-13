import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.cache import cache

from .serializers import LetterSerializer

from .modules.sendletter import NiceCheckplus, Sailor, PostMan, nice_checkplus


class LetterView(APIView):
    def post(self, request):
        letter_serializer = LetterSerializer(data=request.data)

        if letter_serializer.is_valid():

            letter_serializer.save()

            return Response(letter_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(letter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SailorView(APIView):
    def post(self, request):
        print(request.data['mobileco'])
        return Response(request.data, status=status.HTTP_200_OK)


class Orcinus(APIView):

    data = {}
    nice_checker = None
    session = requests.Session()

    def post(self, request):

        if request.data['method_'] != "start":
            self.data = cache.get('data', self.data)
            self.nice_checker = cache.get('nice_checker', self.nice_checker)
            self.session = cache.get('session', self.session)

        self.data |= request.data

        print(self.data)

        method_ = self.data['method_']
        answer = self.data['answer']

        if method_ == "start":
            self.make_session()
            return Response({"info": "session created"}, status=status.HTTP_201_CREATED)
        elif method_ == "get_captcha":
            self.make_session()
            img = self.get_captcha()
            return Response({"info": "image",
                             "image": img}, status=status.HTTP_200_OK)
        elif method_ == "send_verifySMS":
            self.send_verifySMS(answer)
            return Response({"info": "verify SMS sent"}, status=status.HTTP_200_OK)
        elif method_ == "check_verifySMS":
            self.check_verifySMS(answer)
            return Response({"info": "checked!"}, status=status.HTTP_200_OK)
        elif method_ == "send_letter":
            self.send_letter()
            return Response({"info": "letter sent"}, status=status.HTTP_200_OK)

    def make_session(self):
        data = self.data
        self.session = requests.Session()
        self.session = NiceCheckplus.make_session(self.session)

        self.nice_checker = NiceCheckplus(self.session,
                                          {
                                              "mobileco": data['mobile_co'],
                                              "mynum1": data['snd_birth'],
                                              "mynum2": data['snd_sex'],
                                              "username": data['snd_name'],
                                              "mobileno": data['mobile_no']
                                          }
                                          )
        # """BEGIN testcode
        # """

        # img = self.nice_checker.get_captcha()
        # img.show()
        # answer = input()
        # self.nice_checker.check_captcha(answer)
        # answer = input()
        # self.nice_checker.check_auth(answer)

        # """END testcode
        # """

        cache.set_many({
            'data': self.data,
            'nice_checker': self.nice_checker,
            'session': self.session
        })

    def get_captcha(self):
        img = self.nice_checker.get_captcha()
        print(self.session.headers)
        cache.set_many({
            'data': self.data,
            'nice_checker': self.nice_checker,
            'session': self.session
        })
        # img.show()
        return img

    def send_verifySMS(self, answer):
        self.nice_checker.check_captcha(answer)
        self.session = self.nice_checker.get_session()
        cache.set_many({
            'data': self.data,
            'nice_checker': self.nice_checker,
            'session': self.session
        })

    def check_verifySMS(self, answer):
        self.nice_checker.check_auth(answer)
        cache.set_many({
            'data': self.data,
            'nice_checker': self.nice_checker,
            'session': self.session
        })

    def send_letter(self):
        self.session = self.nice_checker.get_session()
        data = self.data
        sailor = Sailor(self.session, {
            "name": data['sailor_name'],
            "birth": data['sailor_birth']
        })

        PostMan.send_letter(self.session, sailor.data | {
            "sndbirth": data['snd_birth'],
            "sndname": data['snd_name'],
            "relation": data['relation'],
            "title": data['title'],
            "content": data['content'],
        })
        cache.set_many({
            'data': self.data,
            'nice_checker': self.nice_checker,
            'session': self.session
        })
