import React from 'react'

const CaptchaForm = ({ onChange, form }) => {
    return (
        <div>
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
        </div>
    )
}

export default CaptchaForm
