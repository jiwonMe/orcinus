import React from 'react'
import BirthForm from './BirthForm'
import CaptForm from './CaptForm'
import LetterForm from './LetterForm'
import VerifyForm from './VerifyForm'

const FormContainer = () => {
    return (
        <div className="container">
            <h1>본인인증</h1>
            <div>
                <BirthForm />
                <CaptForm />
                <VerifyForm />
                <LetterForm />
                <br /><br />
            </div>
            <div className="bottom">
                <button className="submit">확인</button>
            </div>
        </div>
    )
}

export default FormContainer
