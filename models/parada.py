import uuid
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from .base import Base
from .punto import Punto
from .trayecto import Trayecto


class Parada(Base):
    __tablename__ = "paradas"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    orden: Mapped[int] = mapped_column(Integer, nullable=False)

    trayecto_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("trayecto.id"),
        nullable=False
    )
    punto_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("puntos.id"),
        nullable=False
    )

    trayecto = relationship("Trayecto", backref="paradas", lazy="joined")
    punto = relationship("Punto", lazy="joined")

    __table_args__ = (
        UniqueConstraint("trayecto_id", "orden", name="uq_trayecto_orden"),
    )

    def __repr__(self):
        return (
            f"<Parada(id={self.id}, nombre='{self.nombre}', orden={self.orden}, "
            f"trayecto_id={self.trayecto_id}, punto_id={self.punto_id})>"
        )
