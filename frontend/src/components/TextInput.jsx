import React from 'react'

const TextInput = ({ name, title, description }) => {
    return (
        <div className="textinput">
            <div className="description">{title}</div>
            <input name={name} placeholder={description || "None"} />
        </div>
    )
}

export default TextInput
