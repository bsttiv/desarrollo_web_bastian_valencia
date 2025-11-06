package com.bsttiv.tarea4.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.servlet.resource.NoResourceFoundException;

import java.util.NoSuchElementException;

@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(NoSuchElementException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public Error handleNotFound(NoSuchElementException ex) {
        return new Error(404, "Not Found", "No se pudo encontrar el recurso solicitado");
    }

    @ExceptionHandler(NoResourceFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public Error handleNotFound(NoResourceFoundException ex){
        return new Error(404, "Not Found", "No se pudo encontrar el recurso solicitado");
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Error handleValidationErrors(MethodArgumentNotValidException ex){
        String msg = ex.getBindingResult().getFieldErrors().getFirst().getDefaultMessage();
        return new Error(400, "Bad Request", msg);
    }

    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public Error handleGenericException(Exception ex){
        System.out.println(ex.toString());
        return new Error(500, "Internal Server Error", "Ocurrio un error en el servidor");
    }
}
