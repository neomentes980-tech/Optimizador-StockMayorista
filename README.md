
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

```bash
python stock_ia.py
