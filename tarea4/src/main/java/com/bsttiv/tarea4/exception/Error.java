package com.bsttiv.tarea4.exception;

public record Error (
    int status,
    String error,
    String message
) {}