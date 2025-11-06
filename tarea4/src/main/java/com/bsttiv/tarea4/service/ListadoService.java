package com.bsttiv.tarea4.service;

import com.bsttiv.tarea4.model.Comuna;
import com.bsttiv.tarea4.model.Listado;
import com.bsttiv.tarea4.model.Nota;
import com.bsttiv.tarea4.model.aviso.AvisoAdopcion;
import com.bsttiv.tarea4.model.aviso.UnidadMedida;
import com.bsttiv.tarea4.repository.AvisoRepository;
import com.bsttiv.tarea4.repository.ComunaRepository;
import com.bsttiv.tarea4.repository.NotaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ListadoService {
    @Autowired
    private AvisoRepository avisoRepo;
    @Autowired
    private ComunaRepository comunaRepo;
    @Autowired
    private NotaRepository notaRepo;

    public long numeroDePaginas(){
        long numeroAvisos = avisoRepo.count();
        return numeroAvisos / 6;
    }

    public List<Listado> obtenerListado(int offset){
        Pageable pageable = PageRequest.of(offset, 6);
        Page<AvisoAdopcion> avisos = avisoRepo.findAll(pageable);
        List<Listado> r = avisos.map(aviso -> {
            Comuna comuna = comunaRepo.findById(aviso.getComunaId()).orElse(new Comuna());
            List<Nota> notas = notaRepo.findByAvisoId(aviso.getId());
            String medida = aviso.getUnidadMedida() == UnidadMedida.A? "año(s)" : "mes(es)";
            String tipoAnimal = aviso.getTipo().name().toLowerCase() + "(s)";
            String cantidadTipoEdad = String.format("%d %s %d %s", aviso.getCantidad(), tipoAnimal, aviso.getEdad(), medida);
            int nota = !notas.isEmpty() ? (notas.stream()
                    .map(Nota::getNota)
                    .reduce(Integer::sum)
                    .orElse(0) / notas.size()) : 0;
            return new Listado(aviso.getId(),
                    aviso.getFechaIngreso(),
                    aviso.getSector(),
                    cantidadTipoEdad,
                    comuna.getNombre(),
                    nota);
        }).stream().collect(Collectors.toList());
        return r;
    }
}
