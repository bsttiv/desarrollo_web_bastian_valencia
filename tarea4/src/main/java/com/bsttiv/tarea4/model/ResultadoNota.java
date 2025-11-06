package com.bsttiv.tarea4.model;

import java.util.Optional;

public class ResultadoNota {
    private String status;
    private String msg;
    private int notaActual;
    public ResultadoNota(String status, String msg, int notaActual){
        this.status=status;
        this.msg=msg;
        this.notaActual=notaActual;
    }

    public int getNotaActual() {
        return notaActual;
    }

    public String getMsg() {
        return msg;
    }

    public String getStatus() {
        return status;
    }
}
