package com.bsttiv.tarea4.controller;

import com.bsttiv.tarea4.model.Nota;
import com.bsttiv.tarea4.model.ResultadoNota;
import com.bsttiv.tarea4.repository.NotaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/notas")
public class NotaController {
    @Autowired
    private NotaRepository notaRepo;
    @PostMapping
    public ResultadoNota agregarNota(@RequestBody Nota nota){
        Nota res = notaRepo.save(nota);
        List<Nota> notas = notaRepo.findByAvisoId(res.getAvisoId());
        int notaActual = !notas.isEmpty() ? (notas.stream()
                .map(Nota::getNota)
                .reduce(Integer::sum)
                .orElse(0) / notas.size()) : 0;
        return new ResultadoNota("ok", "Se agrego la nota correctamente", notaActual);
    }
}
