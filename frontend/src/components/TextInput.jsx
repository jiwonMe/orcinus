import React from 'react'

const TextInput = ({ id, name, value, title, description, onChange }) => {
    return (
        <div className="textinput">
            <div className="description">{title}</div>
            <input id={id} name={name} placeholder={description || "None"} onChange={onChange} value={value} />
        </div>
    )
}

export default TextInput
