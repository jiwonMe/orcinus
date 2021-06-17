import React, { useEffect } from 'react'
import TextArea from './TextArea'
import TextInput from './TextInput'

const LetterForm = ({ onChange, data }) => {

    useEffect(
        () => onChange({ target: { id: "method_", value: "send_letter" } }), [data.method_,]
    )

    return (
        <div className="container">
            <TextInput id="sailor_name" title="받는사람" name="receiver" description="이름(실명)" onChange={onChange} />
            <TextInput id="sailor_birth" title="생년월일(받는사람)" name="receiver_birth" description="YYMMDD" onChange={onChange} />
            <TextInput id="title" title="제목" name="title" description="100자 이내" onChange={onChange} />
            <TextArea id="content" title="내용" name="content" description="내용을 입력해주세요 (1000자 이내)" onChange={onChange} />
        </div>
    )
}

export default LetterForm
