📦 Optimizador de Stock con IA — Mayoristas
Sistema en Python que simula un agente de inteligencia artificial para el monitoreo automático de inventario en distribuidores y centros de distribución mayoristas.
Detecta productos en riesgo de quiebre de stock, calcula cuándo y cuánto reponer, asigna un nivel de criticidad y genera alertas accionables listas para usar.
🎯 Motivación
En la logística mayorista, un quiebre de stock no es solo un número: es una venta perdida, un cliente insatisfecho y una cadena de suministro interrumpida.
Este proyecto nace de una necesidad real:
saber a tiempo qué productos están por debajo del stock mínimo, antes de que el problema llegue a la operación.
El objetivo es ofrecer una herramienta simple, transparente y accionable que ayude a equipos de inventario, planificación y operaciones a tomar mejores decisiones.
✨ Características principales
Carga de inventario desde archivo JSON
Cálculo automático de:
Días de cobertura de stock
Punto de reorden
Cantidad sugerida a pedir
Nivel de criticidad (Crítico / Alto / Medio / OK)
Generación de alertas prioritarias
Exportación de reportes en .txt y .csv
Logging completo de toda la actividad con fecha y hora
Código modular, legible y fácil de extender
⚙️ Cómo funciona
Carga el inventario desde data/inventario.json
Analiza cada producto y calcula:
Días de cobertura de stock
Punto de reorden (cuándo hay que volver a pedir)
Cantidad sugerida a pedir
Nivel de criticidad
Genera alertas solo para los productos que realmente están en riesgo
Guarda los reportes en:
reports/alertas_generadas.txt
reports/alertas_generadas.csv
Registra toda la actividad con logging (fecha, hora y detalle de cada paso)
🚀 Cómo ejecutarlo
Requisitos
Python 3.11 o superior
Pasos
# 1. Clonar el repositorio
git clone https://github.com/neomentes9/Optimizador-StockMayorista.git
cd Optimizador-StockMayorista

# 2. (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

# 3. Ejecutar el programa
python -m src.main
📁 Estructura del proyecto
Optimizador-StockMayorista/
├── data/
│   └── inventario.json          # Inventario de entrada
├── reports/                     # Reportes generados
│   ├── alertas_generadas.txt
│   └── alertas_generadas.csv
├── src/
│   ├── __init__.py
│   ├── analyzer.py              # Lógica de cálculo y criticidad
│   ├── loader.py                # Carga de datos
│   ├── main.py                  # Punto de entrada
│   ├── models.py                # Modelos de datos
│   └── reporter.py              # Generación de reportes
├── README.md
└── requirements.txt             # (si se agregan dependencias)
📊 Ejemplo de salida
[2026-08-05 11:45:12] INFO - Inventario cargado: 48 productos
[2026-08-05 11:45:12] INFO - Análisis completado
[2026-08-05 11:45:12] WARNING - 7 productos en riesgo detectados

Producto: Aceite Girasol 900ml
  • Stock actual: 42
  • Demanda diaria: 18
  • Días de cobertura: 2.3
  • Punto de reorden: 54
  • Cantidad sugerida: 120
  • Criticidad: CRÍTICO
🛠️ Tecnologías utilizadas
Python 3.11+
Módulos estándar (json, logging, csv, dataclasses)
Arquitectura modular y limpia (fácil de mantener y extender)
🔮 Próximas mejoras
[ ] Integración con bases de datos (SQLite / PostgreSQL)
[ ] API REST para consultar alertas en tiempo real
[ ] Dashboard web simple
[ ] Predicción de demanda con modelos de machine learning
[ ] Integración con sistemas WMS / SAP
[ ] Notificaciones por email o WhatsApp
👤 Autor
neomentes9
Proyecto orientado a la logística mayorista y a centros de distribución automatizados.
