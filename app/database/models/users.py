from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from app.database.session import Base


class User(Base):
    """User model for expense tracker application."""

    __tablename__ = "users"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Authentication fields
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    # Profile information
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    profile_image = Column(String(500), nullable=True)  # URL to profile image
    phone_number = Column(String(20), nullable=True)

    # User preferences and settings
    currency = Column(
        String(3), default="USD", nullable=False
    )  # Default currency for expenses

    # Account status
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    # Timestamps
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    last_login_at = Column(DateTime(timezone=True), nullable=True)

    # Additional profile information
    bio = Column(Text, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    address = Column(Text, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', username='{self.username}')>"

    @property
    def full_name(self) -> str:
        """Get the full name of the user."""
        return f"{self.first_name} {self.last_name}"
