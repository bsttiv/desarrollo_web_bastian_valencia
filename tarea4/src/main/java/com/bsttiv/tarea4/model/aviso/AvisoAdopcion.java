package com.bsttiv.tarea4.model.aviso;

import jakarta.persistence.*;

import java.sql.Date;


@Entity
public class AvisoAdopcion {
    private @Id
    @GeneratedValue Long id;
    @Column(name = "fecha_ingreso")
    private Date fechaIngreso;
    private String sector;
    private int cantidad;
    private int edad;
    @Column(name = "tipo")
    private TipoMascota tipo;
    @Column(name="unidad_medida")
    private UnidadMedida unidadMedida;
    @Column(name="comuna_id")
    private Long comunaId;

    public Long getId() {
        return id;
    }

    public Date getFechaIngreso() {
        return fechaIngreso;
    }

    public int getCantidad() {
        return cantidad;
    }

    public Long getComunaId() {
        return comunaId;
    }

    public String getSector() {
        return sector;
    }

    public TipoMascota getTipo() {
        return tipo;
    }

    public UnidadMedida getUnidadMedida(){
        return unidadMedida;
    }

    public int getEdad() {
        return edad;
    }
}
