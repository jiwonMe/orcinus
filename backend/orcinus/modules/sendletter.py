import requests
import os
import base64
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class NiceCheckplus:
    """Nice 본인인증모듈
    """

    def __init__(self, session,
                 data={
                     "mobileco": str,  # 통신사
                     "mynum1": str,  # 주민등록번호 앞 6자리
                     "mynum2": str,  # 주민등록번호 뒤 1자리
                     "username": str,  # 이름
                     "mobileno": str,  # 핸드폰 번호
                 }):
        self.session = session
        self.data = data

    # session 만들기
    def make_session(self, session=requests.Session()):
        s = session
        req = s.get(
            'https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp', verify=False)

        # 개인정보수집 및 이용에 대한 동의
        # POST
        url = '/themes/basic/sub2/4_5.jsp'
        args = {
            "check2": "Y",
            "__checkbox_check2": "Y",
        }

        ok = s.post("https://www.edunavy.mil.kr:10003" +
                    url, data=args, verify=False)
        # print(ok.text)

        # login 시도
        url = '/member/login.jsp'
        args = {
            "mode": "letter",
            "returnUrl": "https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp",
            "boardID": None,
            "category": None,
            "ipinValue": "008003"
        }

        s.post("https://www.edunavy.mil.kr:10003"+url, data=args, verify=False)
        return s

    # 캡챠 이미지 받아오기
    def get_captcha(self):

        self.data['mynum'] = self.data['mynum1']+self.data['mynum2']
        s = self.session

        url = 'https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb'
        s.post(
            url,
            data={
                "loginType": "SSN",
                "returnUrl": "https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp",
                "foreigner": "1",
                "inqRsn": "40",
                "SendInfo": "",
                "reqInfo": "2C3AECE85B04C41BC68664DC30991828A15F1C88EF6CA31A762D4216590E0F8176DFED4E96102B67E1174078F8D2D4DD686EEB9FEDB9C0BBE2F9B214413C9738EDE4F4269474E544F093E908804759E1F56B3885370321FB6A3D5F61E1F14312AC611A4B2796E6991666BA11BCC7F8C025369B4FA6505CF13520969E94FEAF5743CD545B9B88A9A27515F2150337DE5E0FFB85C46B26A85C782D382E0437F4A3",  # 실명확인 회원사 아이디
                "retUrl": "23https://www.edunavy.mil.kr:10003/siren24/ipin_popup_seed.jsp?boardID=&category=&returnUrl=https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp&ipinValue=008003&boardSeqno=",  # 실명확인 결과수신
                "verSion": "1",  # 모듈 버전 정보
                "m": "checkplusService",
                "EncodeData": "AgAFQlAzMjaCf3GYXXQeo9ujxPePqKN+nVr1K56hoXFSY+q5WqUDjBJU0Dkf4Nm6PzcO5bSYUnHHO0ZXjlvi1CyewHBHrFuPxpz/R6BoXOsvMt1SqZUxZ331dxsbAUxoeKAB5Enh7h7zVcGbCVuA+G5hWgvNNSHM8jk2PKnQUWNnw4An64OwKkq+YURhMUQAxlfJ+ucDDc+MA1L+k9hYLhnQD3bYy46ZnWy6lGOB8zP4BkPO1WBG6u24WLBapFLh/i1fa6uNj1qEHIzeGhLlPF9Q+ZGZykCcbDIDxAfz87mkrcDG+aoiUaIn80HamXwOX8uq3jDqMq1M1JVxDXzneHc86RnHnOj0Cu7hCsXaWslJapDOj0ndolRgPvDRm5QaNI1tdSavbojueez/i7WH++BvCaCoIw27Gg9olFLQ7R/sNKQUcsYF9SB6df8/UlcrHbjchC9hkGaFYuNMczYyVBVxX2FGBRya6iHUabNRxz8IC+lgC4NK79TOxZwe09oFHcSNQ1suB8H7nYLnPuU4Hz7cyeEtG0mvJm1DDw1NmWvYcvIzXadNnZxw60BBkL1N1SfHig+NWaQmFDAIqcAVnjOpJs+hzDFTdYF7IveED1PoFdFZDPWuCGXp714QCTw///OHoaDUIILWC6CObm+WPoIRKI9Jab9pPI/UYCaazJOhxMHTt/SJng==",  # 업체정보 암호화 정보
            }
        )

        s.post(url, data={
            "m": "auth_mobile_main"
        })

        s.post(url, data={
            "m": "auth_mobile01",
            "agreeOptionYn": "N",
            "mobileco": self.data['mobileco'],
            "agree1": "Y",
            "agree2": "Y",
            "agree3": "Y",
            "agree4": "Y",
        })

        res = s.post(url, data={
            "m": "auth_mobile01",
            "mobileco": self.data['mobileco'],
            "mobile_auth_type": "SMS"  # 간편인증은 "SIMPLE"
        })

        html = res.text

        soup = bs(html, 'html.parser')
        self.BDC_VCID_CAPTCHA = soup.find(
            'input', {'name': 'BDC_VCID_CAPTCHA'}).attrs['value']
        self.BDC_BackWorkaround_CAPTCHA = soup.find(
            'input', {'name': 'BDC_BackWorkaround_CAPTCHA'}).attrs['value']
        self.BDC_Hs_CAPTCHA = soup.find(
            'input', {'name': 'BDC_Hs_CAPTCHA'}).attrs['value']
        self.BDC_SP_CAPTCHA = soup.find(
            'input', {'name': 'BDC_SP_CAPTCHA'}).attrs['value']
        self.CAPTCHA_IMAGE = soup.find(
            'img', {'id': 'CAPTCHA_CaptchaImage'}).attrs['src']

        res = s.get("https://nice.checkplus.co.kr"+self.CAPTCHA_IMAGE)

        img = BytesIO(res.content)
        img = base64.b64encode(img.read())
        return img

    # 캡챠 이미지 맞는지 확인, 맞으면 자동으로 인증 문자 발송
    def check_captcha(self, answer):

        data = self.data
        s = self.session

        url = "https://nice.checkplus.co.kr/Common/checkplus.cb?m=captcha_proc"
        args = {
            "m": "auth_mobile01_proc",
            "mobileco": data['mobileco'],
            "mynum": data['mynum'],
            "username": data['username'],
            "mynum1": data['mynum1'],
            "mynum2": data['mynum2'],
            "mobileno": data['mobileno'],
            "BDC_VCID_CAPTCHA": self.BDC_VCID_CAPTCHA,
            "BDC_BackWorkaround_CAPTCHA": 1,
            "BDC_Hs_CAPTCHA": self.BDC_Hs_CAPTCHA,
            "BDC_SP_CAPTCHA": self.BDC_SP_CAPTCHA,
            "answer": answer
        }
        s.post(url, data=args)

        args["username"] = str(data['username'].encode(
            "cp949")).replace('\\x', '%')[2:-1]

        req = s.post(
            "https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb", data=args)

        html = req.text
        soup = bs(html, 'html.parser')
        self.tranid = soup.find('input', {'name': 'tranid'}).attrs['value']

    # 인증문자 확인
    def check_auth(self, answer):
        s = self.session
        # 문자 인증번호 입력 및 전송
        url = "https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb"
        args = {
            "m": "auth_mobile02_proc",
            "tranid": self.tranid,
            "authnumber": answer
        }

        req = s.post(url, data=args)
        html = req.text
        soup = bs(html, 'html.parser')
        encode_data = soup.find('input', {'name': 'EncodeData'}).attrs['value']
        print(encode_data)
        url = "https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5_1.jsp?boardID=&category=&returnUrl=https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp&ipinValue=008003&boardSeqno="

        args = {
            "EncodeData": encode_data
        }

        req = s.post(url, data=args, verify=False)  # 해군훈련소 ssl인증서가 만료된거구나..

    # 세션 반환
    def get_session(self):
        return self.session


class Sailor:
    def __init__(self, session, data={
        "name": str,  # 훈련병 이름
        "birth": str,  # 훈련병 생일
    }):
        self.session = session
        self.data = data
        self.set_sailor(session)

    def set_sailor(self, session):
        s = session
        args = {
            "method": "send",
            "name": self.data['name'],
            "birth": self.data['birth']
        }
        req = s.post(
            "https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp", data=args, verify=False)

        # print(req.text)
        html = req.text
        soup = bs(html, "html.parser")

        self.data['middle'] = soup.find(
            'input', {"name": "middle"}).attrs['value']
        self.data['small'] = soup.find(
            'input', {"name": "small"}).attrs['value']
        self.data['hunbun'] = soup.find(
            'input', {"name": "hunbun"}).attrs['value']
        self.data['type'] = soup.find('input', {"name": "type"}).attrs['value']
        self.data['num'] = soup.find('input', {"name": "num"}).attrs['value']


class PostMan:
    def send_letter(session: requests.Session, data):
        """편지 작성 및 전송

        Args:
            session (requests): 세션정보
            data (dictionary): 데이터

        Return:
            http code
        """
        data["method"] = "insert"
        session.post(
            "https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp", data=data, verify=False)

        return data


def nice_checkplus(
    session: requests.Session,
    data={
        "mobileco": str,
        "mynum1": str,
        "mynum2": str,
        "mobileno": str,
        "username": str,
    }
):
    """#### nice 본인인증

    Args:
        `session` (request.session): 세션 정보
        `data` (dictionary): POST 요청 데이터
            {
                "mobileco": 통신사 정보 ("SKT","KTF","LGU")
                "mynum1": 주민등록번호 앞 6자리
                "mynum2": 주민등록번호 뒤 첫자리
                "mobileno": 핸드폰 번호
                "username": 본인이름
            }

    Return:
        `session` (request.session): 세션 정보
    """

    data['mynum'] = data['mynum1']+data['mynum2']
    s = session

    # 본인인증 request
    url = 'https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb'
    args = {
        "loginType": "SSN",
        "returnUrl": "https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp",
        "foreigner": "1",
        "inqRsn": "40",
        "SendInfo": "",
        "reqInfo": "2C3AECE85B04C41BC68664DC30991828A15F1C88EF6CA31A762D4216590E0F8176DFED4E96102B67E1174078F8D2D4DD686EEB9FEDB9C0BBE2F9B214413C9738EDE4F4269474E544F093E908804759E1F56B3885370321FB6A3D5F61E1F14312AC611A4B2796E6991666BA11BCC7F8C025369B4FA6505CF13520969E94FEAF5743CD545B9B88A9A27515F2150337DE5E0FFB85C46B26A85C782D382E0437F4A3",  # 실명확인 회원사 아이디
        "retUrl": "23https://www.edunavy.mil.kr:10003/siren24/ipin_popup_seed.jsp?boardID=&category=&returnUrl=https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp&ipinValue=008003&boardSeqno=",  # 실명확인 결과수신
        "verSion": "1",  # 모듈 버전 정보
        "m": "checkplusService",
        "EncodeData": "AgAFQlAzMjaCf3GYXXQeo9ujxPePqKN+nVr1K56hoXFSY+q5WqUDjBJU0Dkf4Nm6PzcO5bSYUnHHO0ZXjlvi1CyewHBHrFuPxpz/R6BoXOsvMt1SqZUxZ331dxsbAUxoeKAB5Enh7h7zVcGbCVuA+G5hWgvNNSHM8jk2PKnQUWNnw4An64OwKkq+YURhMUQAxlfJ+ucDDc+MA1L+k9hYLhnQD3bYy46ZnWy6lGOB8zP4BkPO1WBG6u24WLBapFLh/i1fa6uNj1qEHIzeGhLlPF9Q+ZGZykCcbDIDxAfz87mkrcDG+aoiUaIn80HamXwOX8uq3jDqMq1M1JVxDXzneHc86RnHnOj0Cu7hCsXaWslJapDOj0ndolRgPvDRm5QaNI1tdSavbojueez/i7WH++BvCaCoIw27Gg9olFLQ7R/sNKQUcsYF9SB6df8/UlcrHbjchC9hkGaFYuNMczYyVBVxX2FGBRya6iHUabNRxz8IC+lgC4NK79TOxZwe09oFHcSNQ1suB8H7nYLnPuU4Hz7cyeEtG0mvJm1DDw1NmWvYcvIzXadNnZxw60BBkL1N1SfHig+NWaQmFDAIqcAVnjOpJs+hzDFTdYF7IveED1PoFdFZDPWuCGXp714QCTw///OHoaDUIILWC6CObm+WPoIRKI9Jab9pPI/UYCaazJOhxMHTt/SJng==",  # 업체정보 암호화 정보
    }

    ok = s.post(url, data=args)
    # print(ok.text)

    url = "https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb"
    args = {
        "m": "auth_mobile_main"
    }

    s.post(url, data=args).text

    url = "https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb"
    args = {
        "m": "auth_mobile01",
        "agreeOptionYn": "N",
        "mobileco": data['mobileco'],
        "agree1": "Y",
        "agree2": "Y",
        "agree3": "Y",
        "agree4": "Y",
    }

    res = s.post(url, data=args)
    # print(res.text)

    url = "https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb"
    args = {
        "m": "auth_mobile01",
        "mobileco": data['mobileco'],
        "mobile_auth_type": "SMS"  # 간편인증은 "SIMPLE"
    }

    res = s.post(url, data=args)
    html = res.text

    soup = bs(html, 'html.parser')
    BDC_VCID_CAPTCHA = soup.find(
        'input', {'name': 'BDC_VCID_CAPTCHA'}).attrs['value']
    BDC_BackWorkaround_CAPTCHA = soup.find(
        'input', {'name': 'BDC_BackWorkaround_CAPTCHA'}).attrs['value']
    BDC_Hs_CAPTCHA = soup.find(
        'input', {'name': 'BDC_Hs_CAPTCHA'}).attrs['value']
    BDC_SP_CAPTCHA = soup.find(
        'input', {'name': 'BDC_SP_CAPTCHA'}).attrs['value']
    CAPTCHA_IMAGE = soup.find(
        'img', {'id': 'CAPTCHA_CaptchaImage'}).attrs['src']

    res = s.get("https://nice.checkplus.co.kr"+CAPTCHA_IMAGE)
    # print(CAPTCHA_IMAGE)
    img = Image.open(BytesIO(res.content))
    img.show()

    # 보안문자: //*[@id="CAPTCHA_CaptchaImage"] -> src url에 있음

    # 보안문자 불러오기
    # t <- '//*[@id="BDC_VCID_CAPTCHA"]'에서 값 가져오기
    #url = "https://nice.checkplus.co.kr/botdetectcaptcha?get=p&c=CAPTCHA&t="+t

    url = "https://nice.checkplus.co.kr/Common/checkplus.cb?m=captcha_proc"

    answer = input()

    args = {
        "m": "auth_mobile01_proc",
        "mobileco": data['mobileco'],
        "mynum": data['mynum'],
        "username": data['username'],
        "mynum1": data['mynum1'],
        "mynum2": data['mynum2'],
        "mobileno": data['mobileno'],
        "BDC_VCID_CAPTCHA": BDC_VCID_CAPTCHA,
        "BDC_BackWorkaround_CAPTCHA": 1,
        "BDC_Hs_CAPTCHA": BDC_Hs_CAPTCHA,
        "BDC_SP_CAPTCHA": BDC_SP_CAPTCHA,
        "answer": answer
    }

    req = s.post(url, data=args)
    args = {
        "m": "auth_mobile01_proc",
        "mobileco": data['mobileco'],
        "mynum": data['mynum'],
        "username": str(data['username'].encode("cp949")).replace('\\x', '%')[2:-1],
        "mynum1": data['mynum1'],
        "mynum2": data['mynum2'],
        "mobileno": data['mobileno'],
        "BDC_VCID_CAPTCHA": BDC_VCID_CAPTCHA,
        "BDC_BackWorkaround_CAPTCHA": 1,
        "BDC_Hs_CAPTCHA": BDC_Hs_CAPTCHA,
        "BDC_SP_CAPTCHA": BDC_SP_CAPTCHA,
        "answer": answer
    }
    req = s.post(
        "https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb", data=args)
    # print(args)
    # print(req.text)

    html = req.text
    soup = bs(html, 'html.parser')
    tranid = soup.find('input', {'name': 'tranid'}).attrs['value']

    # 문자 인증번호 입력 및 전송
    url = "https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb"

    """
    m: auth_mobile02_proc
    tranid: 15326BCFIN_12100_20210526135914_1146786903
    authnumber: 111111
    """
    # print(tranid)
    authnumber = input()

    args = {
        "m": "auth_mobile02_proc",
        "tranid": tranid,
        "authnumber": authnumber
    }

    req = s.post(url, data=args)
    # print(args)
    # print(req)
    # print(req.url)
    # print(req.text)

    html = req.text
    soup = bs(html, 'html.parser')
    EncodeData = soup.find('input', {'name': 'EncodeData'}).attrs['value']

    # # 성공여부 GET
    # url = "https://nice.checkplus.co.kr/CheckPlusSafeModel/checkplus.cb?m=checkplusSerivce_resultSend"

    # req = s.get(url)
    # print(req.text)

    url = "https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5_1.jsp?boardID=&category=&returnUrl=https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp&ipinValue=008003&boardSeqno="

    args = {
        "EncodeData": EncodeData
    }

    req = s.post(url, data=args)
    # print(req.text)

    return int(200)


def get_sailor(
    session: requests.Session,
    data={
        "name": str,
        "birth": str
    }
):
    """해군 장병 정보 확인

    Args:
        session (requests.session): 세션 정보
        data (dictionary): 훈련병 정보
        {
            "name": 훈련병 이름
            "birth": 훈련병 생년월일(YYMMDD)
        }
    Returns:
        data (dictionary): 훈련병 정보
        {
            "name": 훈련병 이름
            "birth": 훈련병 생년월일(YYMMDD)
            "middle": 중대 번호
            "small": 소대 번호
            "hunbun": 훈련병 번호
            "type": 해군 군종 구분
            "num": 훈련기수
        }
    """

    s = session

    args = {
        "method": "send",
        "name": data['name'],
        "birth": data['birth']
    }
    req = s.post(
        "https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp", data=args)

    # print(req.text)
    html = req.text
    soup = bs(html, "html.parser")

    data['middle'] = soup.find('input', {"name": "middle"}).attrs['value']
    data['small'] = soup.find('input', {"name": "small"}).attrs['value']
    data['hunbun'] = soup.find('input', {"name": "hunbun"}).attrs['value']
    data['type'] = soup.find('input', {"name": "type"}).attrs['value']
    data['num'] = soup.find('input', {"name": "num"}).attrs['value']

    return data

    # session 생성


if __name__ == "__main__":
    # .env 파일로드
    load_dotenv(verbose=True)

    SAILOR_NAME = os.getenv("SAILOR_NAME")  # 훈련병 이름
    SAILOR_BIRTH = os.getenv("SAILOR_BIRTH")  # 훈련병 생년월일
    SND_NAME = os.getenv("SND_NAME")  # 보내는이 이름
    SND_BIRTH = os.getenv("SND_BIRTH")  # 보내는이 생년월일
    SND_SEX = os.getenv("SND_SEX")  # 보내는이 주민등록번호 뒷 첫자리
    MOBILE_NO = os.getenv("MOBILE_NO")  # 보내는이 전화번호
    MOBILE_CO = os.getenv("MOBILE_CO")  # 보내는이 통신사

    s = requests.Session()

    s = NiceCheckplus.make_session(s)

    nice_checker = NiceCheckplus(s, {
        "mobileco": MOBILE_CO,
        "mynum1": SND_BIRTH,
        "mynum2": SND_SEX,
        "username": SND_NAME,
        "mobileno": MOBILE_NO,
    })

    img = nice_checker.get_captcha()
    img.show()
    answer = input()
    nice_checker.check_captcha(answer)
    answer = input()
    nice_checker.check_auth(answer)
    s = nice_checker.get_session()

    sailor = Sailor(s, {
        "name": SAILOR_NAME,
        "birth": SAILOR_BIRTH
    })

    data = sailor.data

    print(data)

    # 재시도
    arg = {
        "m": "auth_mobile02",
    }

    # 재발송
    url = "./checkplus.cb?m=auth_mobile_authnum_resend"
    arg = {
        ""
    }

    # PostMan.send_letter(s, sailor.data | {
    #     "sndbirth": SND_BIRTH,
    #     "sndname": SND_NAME,
    #     "relation": "친구",
    #     "title": "",
    #     "content": "",
    # })
