import React from 'react'

const TextArea = ({ id, title, name, description, onChange }) => {
    return (
        <div>
            <div className="description">{title}</div>
            <textarea id={id} name={name} placeholder={description} onChange={onChange} />
        </div>
    )
}

export default TextArea
