import React, { useState } from 'react'
import FormContainer from './FormContainer'
import './main.css'

const Main = () => {

    const [data, setData] = useState({
        method_: '',
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
        relation: '친구'
    })

    const [image, setImage] = useState('')

    const onChange = e => {
        const nextData = {
            ...data,
            [e.target.id]: e.target.value
        }
        setData(nextData)
    }

    const orcinus = async () => {
        const res = await fetch('https://orcinus.jiwon.me/api/Orcinus/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(data)
        })

        const res_json = await res.json()
        console.log(res_json)
        console.log(res_json.info)

        if (data.image !== null) {
            await setImage(res_json.image)
        }
    }

    const onSubmit = () => {
        console.log(data)
        // alert(JSON.stringify(data))
        orcinus()
    }

    return (
        <div>
            <FormContainer
                data={data}
                image={image}
                method={data.method_}
                onChange={onChange}
                onSubmit={onSubmit}
            />
        </div>
    )
}

export default Main
