# 📦 Optimizador de Stock con IA — Mayoristas

Sistema en Python que simula un agente de inteligencia artificial para el 
monitoreo automático de inventario en distribuidoras mayoristas. 
Detecta productos en riesgo de quiebre de stock y genera alertas 
con acciones sugeridas.

## 🎯 Motivación

Este proyecto nace de una necesidad real en la logística mayorista: 
saber a tiempo qué productos están por debajo del stock mínimo, antes 
de que se produzca un quiebre que afecte las ventas.

## ⚙️ Cómo funciona

1. Carga el inventario desde `inventario.json`
2. Analiza cada producto comparando stock actual vs. stock mínimo
3. Genera alertas para los productos en riesgo
4. Guarda un reporte en `alertas_generadas.txt`
5. Registra toda la actividad con fecha y hora (logging)

## 🚀 Cómo ejecutarlo

## 📋 Ejemplo de salida

2026-07-30 20:45:29 - INFO - Iniciando sistema de optimización de stock...
2026-07-30 20:45:29 - INFO - Inventario cargado: 5 productos.
2026-07-30 20:45:29 - WARNING - ALERTA: 'Azúcar x 1 kg' - Stock actual: 45 uds (45.0% del mínimo).
2026-07-30 20:45:29 - WARNING - ALERTA: 'Fideos Tallarín 500g' - Stock actual: 25 uds (27.8% del mínimo).
2026-07-30 20:45:29 - INFO - Reporte guardado en: alertas_generadas.txt
Se encontraron 4 producto(s) en riesgo.
## 🧱 Estructura del proyecto
├── stock_ia.py           # Lógica principal del sistema
├── inventario.json       # Base de datos de productos (editable)
└── alertas_generadas.txt # Reporte generado automáticamente
## 🛠️ Tecnologías

- Python 3.11+
- Manejo de errores (try/except)
- Dataclasses
- Logging
- JSON

## 📈 Posibles mejoras futuras

- Conexión a una base de datos real (SQLite/PostgreSQL)
- Envío de alertas por email o WhatsApp
- Dashboard web para visualizar el stock
- Predicción de demanda con machine learning

## 👤 Autor

Proyecto desarrollado como parte de mi portfolio, enfocado en 
automatización y aplicaciones prácticas de IA en logística.

