package com.bsttiv.tarea4.model;

import java.sql.Date;

public class Listado {
    private Long id;
    private Date fechaPublicacion;
    private String sector;
    private String cantidadTipoEdad;
    private String comuna;
    private int nota;
    public Listado(Long id, Date fechaPublicacion, String sector, String cantidadTipoEdad, String comuna, int nota){
        this.id = id;
        this.fechaPublicacion = fechaPublicacion;
        this.sector = sector;
        this.cantidadTipoEdad = cantidadTipoEdad;
        this.comuna = comuna;
        this.nota = nota;
    }

    public int getNota() {
        return nota;
    }

    public String getSector() {
        return sector;
    }

    public Long getId() {
        return id;
    }

    public Date getFechaPublicacion() {
        return fechaPublicacion;
    }

    public String getCantidadTipoEdad() {
        return cantidadTipoEdad;
    }

    public String getComuna() {
        return comuna;
    }
}
