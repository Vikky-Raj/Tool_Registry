"""
Policy model - represents access control and usage policies
"""
from sqlalchemy import Column, Integer, String, Text, JSON, DateTime, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum

from app.config.database import Base


class PolicyType(str, enum.Enum):
    """Policy type enum"""
    ACCESS_CONTROL = "access_control"
    RATE_LIMIT = "rate_limit"
    USAGE_QUOTA = "usage_quota"
    PERMISSION = "permission"
    SECURITY = "security"


class PolicyScope(str, enum.Enum):
    """Policy scope enum"""
    GLOBAL = "global"
    BUNDLE = "bundle"
    TOOL = "tool"
    USER = "user"
    ORGANIZATION = "organization"


class Policy(Base):
    """
    Policy model representing access control and usage policies
    
    Policies define rules for:
    - Who can access tools/bundles
    - Rate limits and quotas
    - Security requirements
    - Permission levels
    """
    __tablename__ = "policies"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Basic Information
    name = Column(String(255), unique=True, nullable=False, index=True)
    display_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    
    # Policy Details
    policy_type = Column(SQLEnum(PolicyType), nullable=False, index=True)
    scope = Column(SQLEnum(PolicyScope), nullable=False, index=True)
    rules = Column(JSON, nullable=False)  # Policy rules as JSON
    
    # Foreign Keys
    bundle_id = Column(Integer, ForeignKey("bundles.id", ondelete="CASCADE"), nullable=True, index=True)
    
    # Status and Priority
    is_active = Column(Boolean, default=True, nullable=False)
    priority = Column(Integer, default=0, nullable=False)  # Higher priority policies override lower
    
    # Metadata
    tags = Column(JSON, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    effective_from = Column(DateTime(timezone=True), nullable=True)
    effective_until = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    # bundle = relationship("Bundle", back_populates="policies")
    
    def __repr__(self):
        return f"<Policy(id={self.id}, name='{self.name}', type='{self.policy_type}')>"
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "display_name": self.display_name,
            "description": self.description,
            "policy_type": self.policy_type.value if self.policy_type else None,
            "scope": self.scope.value if self.scope else None,
            "rules": self.rules,
            "bundle_id": self.bundle_id,
            "is_active": self.is_active,
            "priority": self.priority,
            "tags": self.tags,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "effective_from": self.effective_from.isoformat() if self.effective_from else None,
            "effective_until": self.effective_until.isoformat() if self.effective_until else None,
        }
