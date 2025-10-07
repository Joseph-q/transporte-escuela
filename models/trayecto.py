import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .punto import Punto



class Trayecto(Base):
    __tablename__ = "trayecto"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    nombre_trayecto: Mapped[str] = mapped_column(String(255), nullable=False)
    desde: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("puntos.id"),
        nullable=True
    )
    hasta: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("puntos.id"),
        nullable=True
    )
    color: Mapped[str | None] = mapped_column(String(50))

    # Relaciones opcionales (si también tienes la clase Punto)
    desde_punto = relationship("Punto", foreign_keys=[desde], lazy="joined")
    hasta_punto = relationship("Punto", foreign_keys=[hasta], lazy="joined")

    def __repr__(self):
        return (
            f"<Trayecto(id={self.id}, nombre_trayecto='{self.nombre_trayecto}', "
            f"desde={self.desde}, hasta={self.hasta}, color={self.color})>"
        )
