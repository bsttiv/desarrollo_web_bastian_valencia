package com.bsttiv.tarea4.controller;

import com.bsttiv.tarea4.model.Listado;
import com.bsttiv.tarea4.service.ListadoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/listado")
public class ListadoController {
    @Autowired
    private ListadoService listadoService;

    @GetMapping("/{pagina}")
    public List<Listado> getListado(@PathVariable("pagina") int pagina){
        return listadoService.obtenerListado(pagina);
    }

    @GetMapping(value={"","/"})
    public List<Listado> getListadoFirstPage(){
        return listadoService.obtenerListado(0);
    }
}
