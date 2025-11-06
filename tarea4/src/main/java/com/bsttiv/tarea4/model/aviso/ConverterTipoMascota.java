package com.bsttiv.tarea4.model.aviso;

import jakarta.persistence.AttributeConverter;
import jakarta.persistence.Converter;

@Converter(autoApply = true)
public class ConverterTipoMascota implements AttributeConverter<TipoMascota, String> {
    @Override
    public String convertToDatabaseColumn(TipoMascota tipoMascota){
        if (tipoMascota==null) return null;
        return tipoMascota.name().toLowerCase();
    }

    @Override
    public TipoMascota convertToEntityAttribute(String dbValue){
        if (dbValue == null) return null;
        return TipoMascota.valueOf(dbValue.toUpperCase());
    }
}
