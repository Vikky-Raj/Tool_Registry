"""
Bundle model - represents a collection of related tools
"""
from sqlalchemy import Column, Integer, String, Text, JSON, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

from app.config.database import Base


class Bundle(Base):
    """
    Bundle model representing a collection of related tools
    
    A bundle is a curated collection of tools grouped by purpose,
    domain, or functionality. It can be published and shared.
    """
    __tablename__ = "bundles"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Basic Information
    name = Column(String(255), unique=True, nullable=False, index=True)
    display_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    version = Column(String(50), nullable=False, default="1.0.0")
    
    # Metadata
    author = Column(String(255), nullable=True)
    category = Column(String(100), nullable=True, index=True)
    tags = Column(JSON, nullable=True)  # Array of tags
    icon_url = Column(String(500), nullable=True)
    documentation_url = Column(String(500), nullable=True)
    repository_url = Column(String(500), nullable=True)
    
    # Status and Visibility
    is_public = Column(Boolean, default=True, nullable=False)
    is_published = Column(Boolean, default=False, nullable=False)
    
    # Usage Statistics
    download_count = Column(Integer, default=0, nullable=False)
    star_count = Column(Integer, default=0, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    published_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    # bundle_tools = relationship("BundleTool", back_populates="bundle", cascade="all, delete-orphan")
    # policies = relationship("Policy", back_populates="bundle", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Bundle(id={self.id}, name='{self.name}', version='{self.version}')>"
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "display_name": self.display_name,
            "description": self.description,
            "version": self.version,
            "author": self.author,
            "category": self.category,
            "tags": self.tags,
            "icon_url": self.icon_url,
            "documentation_url": self.documentation_url,
            "repository_url": self.repository_url,
            "is_public": self.is_public,
            "is_published": self.is_published,
            "download_count": self.download_count,
            "star_count": self.star_count,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "published_at": self.published_at.isoformat() if self.published_at else None,
        }
