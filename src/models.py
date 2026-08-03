from dataclasses import dataclass


@dataclass
class Producto:
    sku: str
    nombre: str
    stock_actual: int
    stock_minimo: int
    consumo_diario_promedio: float
    lead_time_dias: int
    stock_seguridad: int

    @property
    def dias_cobertura(self) -> float:
        if self.consumo_diario_promedio <= 0:
            return float("inf")
        return round(self.stock_actual / self.consumo_diario_promedio, 1)

    @property
    def punto_reorden(self) -> float:
        return round((self.consumo_diario_promedio * self.lead_time_dias) + self.stock_seguridad, 1)

    @property
    def cantidad_sugerida(self) -> int:
        sugerida = self.punto_reorden - self.stock_actual
        return max(0, round(sugerida))

    @property
    def nivel_criticidad(self) -> str:
        if self.stock_actual <= self.stock_seguridad:
            return "CRÍTICO"
        elif self.stock_actual < self.punto_reorden:
            return "ALTO"
        elif self.stock_actual < self.stock_minimo:
            return "MEDIO"
        return "OK"


@dataclass
class Alerta:
    producto: Producto

    def mensaje(self) -> str:
        p = self.producto
        return (
            f"ALERTA {p.nivel_criticidad} | {p.nombre} ({p.sku})\n"
            f"Stock actual: {p.stock_actual} | Mínimo: {p.stock_minimo} | "
            f"Días de cobertura: {p.dias_cobertura}\n"
            f"Sugerencia: Pedir {p.cantidad_sugerida} unidades "
            f"(llega en {p.lead_time_dias} días)"
        )
