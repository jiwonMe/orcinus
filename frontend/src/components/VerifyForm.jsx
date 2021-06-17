import React, { useEffect } from 'react'
import TextInput from './TextInput'

const VerifyForm = ({ onChange, data }) => {
    useEffect(
        () => onChange({ target: { id: "method_", value: "check_verifySMS" } }), [data.method_,]
    )
    return (
        <div className="container">
            <TextInput id="answer" name="answer" title="인증번호" description="문자로 발송된 인증번호 6자리" onChange={onChange} />
            만약 30초를 기다려도 문자가 도착하지 않는다면 새로고침 후 다시 시작해주세요 :(
        </div>
    )
}

export default VerifyForm
