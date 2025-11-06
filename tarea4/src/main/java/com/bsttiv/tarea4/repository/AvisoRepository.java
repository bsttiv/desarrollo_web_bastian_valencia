package com.bsttiv.tarea4.repository;


import com.bsttiv.tarea4.model.aviso.AvisoAdopcion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AvisoRepository extends JpaRepository<AvisoAdopcion, Long> {
}
