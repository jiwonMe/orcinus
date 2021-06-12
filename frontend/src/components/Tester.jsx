import React, { useState } from 'react'

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
        const res = await fetch('http://127.0.0.1:8000/api/Orcinus/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(form)
        })

        const data = await res.json()
        console.log(data)

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
            <img src={'data:image/png;base64,' + image} />
            <form>
                <div>
                    method: <br />
                    <input
                        name="method"
                        value={form.method}
                        onChange={onChange}
                    />
                </div>
                <div>
                    answer: <br />
                    <input
                        name="answer"
                        value={form.answer}
                        onChange={onChange}
                    />
                </div>
                <div>
                    relation: <br />
                    <input
                        name="relation"
                        value={form.relation}
                        onChange={onChange}
                    />
                </div>
                <div>
                    snd_name: <br />
                    <input
                        name="snd_name"
                        value={form.snd_name}
                        onChange={onChange}
                    />
                </div>
                <div>
                    snd_birth: <br />
                    <input
                        name="snd_birth"
                        value={form.snd_birth}
                        onChange={onChange}
                    />
                </div>
                <div>
                    snd_sex: <br />
                    <input
                        name="snd_sex"
                        value={form.snd_sex}
                        onChange={onChange}
                    />
                </div>
                <div>
                    mobile_co: <br />
                    <input
                        name="mobile_co"
                        value={form.mobile_co}
                        onChange={onChange}
                    />
                </div>
                <div>
                    mobile_no: <br />
                    <input
                        name="mobile_no"
                        value={form.mobile_no}
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
            </form>
            <button onClick={onSubmit}>submit</button>
        </div>
    )
}

export default Tester
