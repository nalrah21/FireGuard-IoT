def avaliar_risco(temp, gas):

    motivos = []

    if temp > 50:
        motivos.append(f"Temperatura critica ({temp}°C)")
    elif temp >= 35:
        motivos.append(f"Temperatura elevada ({temp}°C)")

    if gas > 3700:
        motivos.append(f"Alta concentracao de gas ({gas})")
    elif gas >= 3300:
        motivos.append(f"Concentracao moderada de gas ({gas})")

    # STATUS
    if temp > 50 or gas > 3700:
        status = "EMERGENCIA"
    elif temp >= 35 or gas >= 3300:
        status = "ATENCAO"
    else:
        status = "SEGURO"
    
    return status, motivos


