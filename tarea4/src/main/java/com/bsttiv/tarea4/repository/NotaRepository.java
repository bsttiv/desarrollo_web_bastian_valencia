package com.bsttiv.tarea4.repository;

import com.bsttiv.tarea4.model.Nota;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface NotaRepository extends JpaRepository<Nota, Long> {
    List<Nota> findByAvisoId(Long avisoId);
}
