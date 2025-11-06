package com.bsttiv.tarea4.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;

@Entity
public class Nota {
    @JsonIgnore
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) private Long id;
    @Column(name = "aviso_id")
    private Long avisoId;
    private int nota;

    public Nota(){}

    public Nota(Long avisoId, int nota){
        this.avisoId = avisoId;
        this.nota = nota;
    }

    public int getNota() {
        return nota;
    }

    public Long getId() {
        return id;
    }

    public Long getAvisoId() {
        return avisoId;
    }

    public void setNota(int nota) {
        this.nota = nota;
    }

    public void setAvisoId(Long avisoId) {
        this.avisoId = avisoId;
    }

    public void setId(Long id) {
        this.id = id;
    }
}
