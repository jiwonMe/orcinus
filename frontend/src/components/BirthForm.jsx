import React from 'react'
import TextInput from './TextInput'

const BirthForm = () => {
    return (
        <div className="container">
            <TextInput title="이름" name="name" description="이름(실명)" />
            <TextInput title="생년월일" name="birth" description="YYMMDD" />
            <TextInput title="주민등록번호 뒷자리 맨 앞 숫자" name="sex" description="1~4 중 하나" />
            <TextInput title="통신사" name="mobile_co" description="KTF / SKT / LGU" />
            <TextInput title="핸드폰 번호" name="mobile_no" description="하이픈('-')없이 입력" />
        </div>
    )
}

export default BirthForm
