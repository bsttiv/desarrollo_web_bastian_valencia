package com.bsttiv.tarea4.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class Comuna {
    private @Id
    @GeneratedValue Long id;
    private String nombre;

    public Long getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }
}
