package com.bsttiv.tarea4.repository;

import com.bsttiv.tarea4.model.Comuna;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ComunaRepository extends JpaRepository<Comuna, Long> {
}
