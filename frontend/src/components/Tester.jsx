import React, { useState } from 'react'
import StartPage from './StartPage'
import CaptchaForm from './CaptchaForm'

const Tester = () => {
    const [form, setForm] = useState({
        method: '',
        answer: '',
        snd_name: '',
        snd_birth: '',
        snd_sex: '',
        mobile_co: '',
        mobile_no: '',
        sailor_name: '',
        sailor_birth: '',
        title: '',
        content: '',
        relation: ''
    });

    const [image, setImage] = useState('')

    const onChange = e => {
        const nextForm = {
            ...form,
            [e.target.name]: e.target.value
        }
        setForm(nextForm)
    }

    const orcinus = async () => {
        const res = await fetch('http://3.37.109.0:8000/api/Orcinus/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(form)
        })

        const data = await res.json()
        console.log(data)
        alert(data.info)

        if (data.image !== null) {
            setImage(data.image)
        }
    }

    const onSubmit = () => {
        alert(JSON.stringify(form))
        orcinus()
    }

    return (
        <div>
            <h1>Orcinus API Test</h1>
            <div>
                method: <br />
                <input
                    name="method"
                    value={form.method}
                    onChange={onChange}
                />
            </div>
            <StartPage onChange={onChange} />
            {
                form.method === "get_captcha" &&
                <div>
                    <CaptchaForm
                        onChange={onChange}
                        form={form}
                    />
                </div>
            }


            { image && <img src={'data:image/png;base64,' + image} alt="captcha" />}
            {
                (form.method === "send_verifySMS" ||
                    form.method === "check_verifySMS") &&
                <div>
                    answer: <br />
                    <input
                        name="answer"
                        value={form.answer}
                        onChange={onChange}
                    />
                </div>
            }
            {
                form.method === "send_letter" &&
                <div>
                    <div>
                        relation: <br />
                        <input
                            name="relation"
                            value={form.relation}
                            onChange={onChange}
                        />
                    </div>
                    <div>
                        sailor_name: <br />
                        <input
                            name="sailor_name"
                            value={form.sailor_name}
                            onChange={onChange}
                        />
                    </div>
                    <div>
                        sailor_birth: <br />
                        <input
                            name="sailor_birth"
                            value={form.sailor_birth}
                            onChange={onChange}
                        />
                    </div>
                    <div>
                        title: <br />
                        <input
                            name="title"
                            value={form.title}
                            onChange={onChange}
                        />
                    </div>
                    <div>
                        content: <br />
                        <textarea
                            name="content"
                            value={form.content}
                            onChange={onChange}
                        />
                    </div>
                </div>}
            <button onClick={onSubmit}>submit</button>
        </div >
    )
}

export default Tester
