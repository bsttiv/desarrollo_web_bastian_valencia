package com.bsttiv.tarea4.model.aviso;

import jakarta.persistence.AttributeConverter;
import jakarta.persistence.Converter;

@Converter(autoApply = true)
public class ConverterUnidadMedida implements AttributeConverter<UnidadMedida, String> {
    @Override
    public String convertToDatabaseColumn(UnidadMedida unidadMedida){
        if (unidadMedida==null) return null;
        return unidadMedida.name().toLowerCase();
    }

    @Override
    public UnidadMedida convertToEntityAttribute(String dbValue){
        if (dbValue == null) return null;
        return UnidadMedida.valueOf(dbValue.toUpperCase());
    }
}
