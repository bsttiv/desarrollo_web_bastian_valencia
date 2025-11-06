package com.bsttiv.tarea4.controller;

import com.bsttiv.tarea4.service.ListadoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.Arrays;
import java.util.stream.IntStream;

@Controller
public class ViewController {
    @Autowired
    private ListadoService listadoService;
    @GetMapping(value = {"/listado", "/listado/"})
    public String listado(Model model){
        IntStream paginas = IntStream.range(0, (int) listadoService.numeroDePaginas()+1);
        int[] paginasArr = paginas.toArray();
        model.addAttribute("paginas", paginasArr);
        model.addAttribute("actual", 0);
        return "listado";
    }
}
