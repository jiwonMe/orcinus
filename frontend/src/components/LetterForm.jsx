import React from 'react'
import TextArea from './TextArea'
import TextInput from './TextInput'

const LetterForm = () => {
    return (
        <div className="container">
            <TextInput title="받는사람" name="sailor" description="이름(실명)" />
            <TextInput title="생년월일(받는사람)" name="sailor_birth" description="YYMMDD" />
            <TextInput title="제목" name="title" description="100자 이내" />
            <TextArea title="내용" name="content" description="내용을 입력해주세요 (1000자 이내)" />
        </div>
    )
}

export default LetterForm
