import React from 'react'

const TextArea = ({ title, name, description }) => {
    return (
        <div>
            <div className="description">{title}</div>
            <textarea name={name} placeholder={description} />
        </div>
    )
}

export default TextArea
