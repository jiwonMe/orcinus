import React from 'react'
import TextInput from './TextInput'

const VerifyForm = () => {
    return (
        <div className="container">
            <TextInput name="answer" title="인증번호" description="문자로 발송된 인증번호 6자리" />
        </div>
    )
}

export default VerifyForm
