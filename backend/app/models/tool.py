"""
Tool model - represents an MCP tool/function
"""
from sqlalchemy import Column, Integer, String, Text, JSON, DateTime, Boolean, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum

from app.config.database import Base


class ToolStatus(str, enum.Enum):
    """Tool status enum"""
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


class Tool(Base):
    """
    Tool model representing an MCP tool/function
    
    A tool is a callable function that can be used by AI agents.
    It has input/output schemas, metadata, and can belong to bundles.
    """
    __tablename__ = "tools"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Basic Information
    name = Column(String(255), unique=True, nullable=False, index=True)
    display_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    version = Column(String(50), nullable=False, default="1.0.0")
    
    # Tool Specifications
    input_schema = Column(JSON, nullable=False)  # JSON Schema for inputs
    output_schema = Column(JSON, nullable=True)  # JSON Schema for outputs
    function_signature = Column(Text, nullable=False)  # Function signature
    
    # Metadata
    category = Column(String(100), nullable=True, index=True)
    tags = Column(JSON, nullable=True)  # Array of tags
    documentation_url = Column(String(500), nullable=True)
    
    # Status and Flags
    status = Column(SQLEnum(ToolStatus), default=ToolStatus.ACTIVE, nullable=False)
    is_public = Column(Boolean, default=True, nullable=False)
    requires_auth = Column(Boolean, default=False, nullable=False)
    
    # Usage Statistics
    usage_count = Column(Integer, default=0, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    # bundle_tools = relationship("BundleTool", back_populates="tool", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Tool(id={self.id}, name='{self.name}', version='{self.version}')>"
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "display_name": self.display_name,
            "description": self.description,
            "version": self.version,
            "input_schema": self.input_schema,
            "output_schema": self.output_schema,
            "function_signature": self.function_signature,
            "category": self.category,
            "tags": self.tags,
            "documentation_url": self.documentation_url,
            "status": self.status.value if self.status else None,
            "is_public": self.is_public,
            "requires_auth": self.requires_auth,
            "usage_count": self.usage_count,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
