import React, { useState } from 'react'
import BirthForm from './BirthForm'
import CaptForm from './CaptForm'
import LetterForm from './LetterForm'
import VerifyForm from './VerifyForm'

const FormContainer = ({ image, data, onSubmit, onChange }) => {
    const [step, setStep] = useState(0)

    const form = [
        <BirthForm onChange={onChange} data={data} />,
        <CaptForm onChange={onChange} data={data} image={image} />,
        <VerifyForm onChange={onChange} data={data} />,
        <LetterForm onChange={onChange} data={data} />, '편지를 성공적으로 발송했습니다']

    return (
        <div className="container">
            <h1>본인인증</h1>
            <div>해당 사이트는 사용자의 정보를 서버에 일체 저장하지 않습니다.</div>
            <h2>Step {step + 1} / 4</h2>
            <div>
                {form[step]}
                <br /><br />
            </div>
            <div className="bottom">
                <button className="submit" onClick={
                    (e) => {
                        setStep(
                            () => (step < 4 ? step + 1 : 0)
                        )
                        onSubmit(e)
                        if (step === 1) {
                            onSubmit(e)
                        }
                    }
                }
                >{
                        step === 4 ? '처음으로' : '확인'
                    }</button>
            </div>
        </div>
    )
}

export default FormContainer
