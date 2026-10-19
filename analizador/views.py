
from django.shortcuts import render


def analizar_numero(valor, base):
    numero = int(valor, base)

    if numero < 0 or numero > 65535:
        raise ValueError("El número debe estar entre 0 y 65535.")

    binario = format(numero, "b")
    bits_significativos = len(binario)

    return {
        "decimal": numero,
        "binario": binario,
        "binario_8": binario.zfill(8),
        "binario_16": binario.zfill(16),
        "binario_24": binario.zfill(24),
        "binario_64": binario.zfill(64),
        "octal": format(numero, "o"),
        "hexadecimal": format(numero, "X"),
        "bits_significativos": bits_significativos,
        "bytes_requeridos": max(1, (bits_significativos + 7) // 8),
    }


def analizar_texto(texto):
    if len(texto) > 20:
        raise ValueError("El texto no puede superar los 20 caracteres.")

    resultado = []

    for caracter in texto:
        codigo = ord(caracter)
        bytes_utf8 = caracter.encode("utf-8")

        resultado.append({
            "caracter": caracter,
            "decimal": codigo,
            "unicode": f"U+{codigo:04X}",
            "hexadecimal": f"{codigo:X}",
            "utf8": " ".join(f"{byte:02X}" for byte in bytes_utf8),
        })

    return resultado


def inicio(request):
    contexto = {}

    if request.method == "POST":
        tipo = request.POST.get("tipo", "numero")

        if tipo == "numero":
            valor = request.POST.get("valor", "").strip()
            base_texto = request.POST.get("base", "10")

            try:
                if not valor:
                    raise ValueError("Debes introducir un número.")

                base = int(base_texto)

                if base not in (2, 8, 10, 16):
                    raise ValueError("Selecciona una base válida.")

                # Validar los caracteres permitidos antes de convertir.
                digitos = {
                    2: "01",
                    8: "01234567",
                    10: "0123456789",
                    16: "0123456789abcdefABCDEF",
                }

                if any(c not in digitos[base] for c in valor):
                    raise ValueError(
                        f"El número contiene dígitos inválidos para base {base}."
                    )

                contexto["numero"] = analizar_numero(valor, base)

            except ValueError as error:
                contexto["error_numero"] = str(error)

        elif tipo == "texto":
            texto = request.POST.get("texto", "")

            try:
                if not texto.strip():
                    raise ValueError("Debes introducir un texto.")

                contexto["texto_original"] = texto
                contexto["caracteres"] = analizar_texto(texto)

            except ValueError as error:
                contexto["error_texto"] = str(error)

    return render(request, "analizador/inicio.html", contexto)
