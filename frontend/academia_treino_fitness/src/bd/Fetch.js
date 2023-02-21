import { useContext } from "react"
import { Navigate } from "react-router-dom"
import { Context } from "../Context"

export const FetchAuthentication = (dado)=>{
    fetch('http://127.0.0.1:8000/api/academia-treino-fitness/authentication/',{
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dado)
    }).then((resp)=>resp.json()).then((data)=>{
        if(data.Authorization === 'Autenticado'){
            sessionStorage.setitem('TF_Authorization', JSON.stringify(data))
            return data.Authorization
        }else{
            return data.Authorization
        }
    }).catch((err)=>console.log(err))
}

export const FetchToken = (dado)=>{
    fetch('http://127.0.0.1:8000/api/token/',{
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dado)
    }).then((resp)=>resp.json).then((data)=>{
        sessionStorage.setItem('TF_Token', JSON.stringify(data))
    })
}

export const FetchUser = ()=>{
    fetch('http://127.0.0.1:8000/api/academia-treino-fitness/authentication/',{
        method: "GET",
        headers: {
            'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('TF_Token')).access}`
        }
    }).then((resp)=>resp.json()).then((data)=>{
        sessionStorage.setItem('TF_DataUser')
    }).catch((err)=>console.log(err))
}