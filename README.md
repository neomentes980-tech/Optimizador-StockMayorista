# 📦 Optimizador de Stock con IA — Mayoristas

Sistema en Python que simula un agente de inteligencia artificial para el monitoreo automático de inventario en distribuidores mayoristas. Detecta productos en riesgo de quiebre de stock, calcula cuándo y cuánto reponer, y genera alertas con acciones sugeridas.

## 🎯 Motivación

Este proyecto nace de una necesidad real en la logística mayorista: saber a tiempo qué productos están por debajo del stock mínimo, antes de que se produzca un quiebre que afecte las ventas.

## ⚙️ Cómo funciona

1. Carga el inventario desde `data/inventario.json`.
2. Analiza cada producto, calculando:
   - Días de cobertura de stock.
   - Punto de reorden (cuándo hay que volver a pedir).
   - Cantidad sugerida a pedir.
   - Nivel de criticidad (Crítico / Alto / Medio / OK).
3. Genera alertas para los productos en riesgo.
4. Guarda los reportes en `reports/alertas_generadas.txt` y `reports/alertas_generadas.csv`.
5. Registra toda la actividad con fecha y hora (logging).

## 🚀 Cómo ejecutarlo

1. Cloná o descargá este repositorio.
2. Asegurate de tener Python 3.11+ instalado.
3. Abrí una terminal en la carpeta del proyecto.
4. Ejecutá el programa:

\`\`\`bash
python -m src.main
\`\`\
