import React, { useEffect } from 'react'
import TextInput from './TextInput'

const BirthForm = ({ data, onChange }) => {
    useEffect(
        () => onChange({ target: { id: "method_", value: "get_captcha" } }), [data.method_,]
    )
    return (
        <div className="container">
            <TextInput id="snd_name" title="이름" name="name" description="이름(실명)" onChange={onChange} value={data.snd_name} />
            <TextInput id="snd_birth" title="생년월일" name="birth" description="YYMMDD" onChange={onChange} value={data.snd_birth} />
            <TextInput id="snd_sex" title="주민등록번호 뒷자리 맨 앞 숫자" name="sex" description="1~4 중 하나" onChange={onChange} value={data.snd_sex} />
            <TextInput id="mobile_co" title="통신사" name="telecom" description="KTF / SKT / LGU" onChange={onChange} value={data.mobile_co} />
            <TextInput id="mobile_no" title="핸드폰 번호" name="mobile" description="하이픈('-')없이 입력" onChange={onChange} value={data.mobile_no} />
        </div>
    )
}

export default BirthForm
