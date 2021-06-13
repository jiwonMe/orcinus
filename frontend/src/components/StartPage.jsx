import React from 'react'

const StartPage = ({ onChange }) => {

    return (
        <div>
            <div>
                <button onClick={onChange}
                    name="method_"
                    value="get_captcha"
                >(1)get_captcha</button>
            </div>
            <div>
                <button onClick={onChange}
                    name="method_"
                    value="send_verifySMS"
                >(2)send_verifySMS</button>
            </div>
            <div>
                <button onClick={onChange}
                    name="method_"
                    value="check_verifySMS"
                >(3)check_verifySMS</button>
            </div>
            <div>
                <button onClick={onChange}
                    name="method_"
                    value="send_letter"
                >(4)send_letter</button>
            </div>
        </div>
    )
}

export default StartPage
