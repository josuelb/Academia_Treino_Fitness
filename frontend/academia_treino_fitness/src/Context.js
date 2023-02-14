import { createContext, useState } from "react";


export const Context = createContext([])

export const ContextProvider = ({children})=>{
    const [thema, setThema] = useState('ligth')
    const [login, setLogin] = useState(false)

    const settingThema = ()=>{
        if (document.body.style.background === 'white'){
            document.body.style.background = 'black'
            setThema('black')
        } else{
            document.body.style.background = 'white'
            setThema('black')
        }
    }

    const settingLogin = (valor)=>{
        setLogin(valor)
    }

    return <Context.Provider value={{thema: [thema, settingThema], login:[login, settingLogin]}}>
        {children}
    </Context.Provider>
}