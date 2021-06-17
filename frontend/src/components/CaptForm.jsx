import React, { useEffect } from 'react'
import TextInput from './TextInput'


const CaptForm = ({ data, image, onChange }) => {
    useEffect(
        () => onChange({ target: { id: "method_", value: "send_verifySMS" } }), [data.method_,]
    )
    return (
        <div className="container">
            <div id="captcha_image">
                <img src=
                    {"data:image/png;base64," + (image || "iVBORw0KGgoAAAANSUhEUgAAAIwAAAAoCAYAAAAsTRLGAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAUTSURBVHgB7Zs9MyxBFIZ7b/lISJCQICEhISJBQkJClSp/wA8S+gOqVIlIiEgQICEhQUKChITEradvvXPb1O7sNj0+ynmq5ro7Pf1xTr99+kyzlZWVlVdnGA3SxD+Li4vOMOqxvr7u/jjDiMAEY0RhgjGiMMEYUZhgjChMMEYUJhgjChOMEYUJxojCBGNEYYIxovg1grm4uHAHBwcuJc/Pz/76TfxIwTBJj4+PUXVubm7c1dWVS8nOzo7b3d11v4kfKZiHhwe3trYWLZrUDA8Pu76+PvebaHIlcX9/715eXlxbW5trb29vuJzowX3uVXsGkWgbeHp6ci0tLa61tTWrT7nud3Z2Ro+NtqlfNHZB+/QT9s3ztIGoobu7O2s3fy9E465Vnq/P83nb6/WRguSCwRDCNJOCMXweHR31l8q3tra8cSpnpY6Njfny6+trd3x87CeLNoDJm5iYcIODg75MWwv9dHR0uJmZmewzuQqTRrs4jbJwUjc3NzPBcH9ubi4T1vn5uTs8PPT3JVzGxfiqoe2INuiPqNfb2+tub2+zcQ8MDPjxnJ6eZveIStPT02/a0bjll9nZ2UysjBefvb7++1s3ynmOccmv+bHn20hFcsFgPM5bWlryg8bYjY0NPyk4inLEMD8/78txLpNImVYF9XE0E6E2SVj7+/vd5ORkVid0CEIiT6FfCYZnmKhQrCMjI154TBzlR0dHXlR8Pjk5cUNDQ9nz9Em7PB+KrohKpZLZTt+0gb26h9jJfbABexEK98Jx4y/qjo+P+zZ5nmdZNGG7gjp7e3uZuLFle3vb+00+TEXSHIaB44ipqaksVCIUJkDbCBPO6lJ5KJIQTRrgOJxQlLTieEQnAfETB1JPcI/JBwTQ09OThXA+I0AEI2iP+jFvQtSRbeqLSdQ95Tyyl4i0sLDwZtw8o+iKPxWl1QbthZHj7OzM+1mREFv4P3VD+1OQNMJoD2ZFhYSTjzEYyAQ3CnW0+mpBWVdX15t7RCSuonbzsHK1pXwUtR/mGXkoYxsmGsh/TDJbLcjmWvkY3N3dZRFVSCiIvdHo2AilJb21IHRiIFFISeXq6mrdemWfd+Bg8gRWPJEGJxN9wkkoAxbO/v6+j7xKohFt7BsgdRXRQorE+h6SCkargHAahkycgiMItWwrOCcmi8d5TGjRKqM/hEjuI8hpqFvNkXkYsxLw1IliESSr+CJ8Pc9vo6CcR4QLiMiKX0PbyyJpDoMoMCpcIRhKuJWBPHN5eenLuWqdvpJsAvWUOJJzQHNzs/+pEA7kHkogAQEQzZQL1ENt0gZ9Mm5Wftkw2fTFOOk3fAsE/IntjEVHCvgjFBVCoYy68jOJMclzapJvSbxxYByvmIBASD61yokuYTkTzTP56IBDtFXp9Vd7MU4m2rBd4FDK9HbAG4Wgbb1p1IM2ybVwOhd9MWYmMh8xU8IYWUCaXOzhChcD9mGrfEZ5OB58wYsEftVCY/w6bkhJhS+ylfG9JJ1j5A+XRLWDJ2CFE5GWl5ff1Ua9Oh8dd1koIhcJM3yGxVTtjKiRdt4L30sqLenF2UUOb8Sg97RRr85H+yyLIn+wgNiOFYEVRar9WqLs/OvT35KMeNhyOGBUvseJL4d4n5mci28nGF5rOfU0/sO2o4M4tkqS4K+IgvDtBPNVW8JPoKxfKMZgf3FnRGGCMaIwwRhRmGCMKEwwRhQmGCMKE4wRhQnGiMIEY0ThT3r5LaRhNMJfR6oz8CwNmo0AAAAASUVORK5CYII=")} alt="captcha placeholder" />
                <button>reload</button>
            </div>
            <TextInput title="정답" id="answer" name="answer" description="보이는 문자를 정확히 입력해주세요"
                onChange={onChange} value={data.answer} />
        </div>
    )
}

export default CaptForm
