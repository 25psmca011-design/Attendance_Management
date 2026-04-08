"""Data models for Attendance Management System"""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class AttendanceStatus(Enum):
    """Enum for attendance status"""
    PRESENT = "Present"
    ABSENT = "Absent"


@dataclass
class AttendanceRecord:
    """Represents a single attendance record"""
    employee_id: str
    name: str
    date: str  # Format: YYYY-MM-DD
    status: AttendanceStatus
    check_in_time: datetime
    check_out_time: Optional[datetime] = None
    remarks: Optional[str] = None

    def __post_init__(self):
        """Validate record after initialization"""
        if not self.employee_id or not self.name:
            raise ValueError("Employee ID and name are required")
        if self.status not in AttendanceStatus:
            raise ValueError(f"Invalid status: {self.status}")

    def to_dict(self) -> dict:
        """Convert record to dictionary"""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "date": self.date,
            "status": self.status.value,
            "check_in_time": self.check_in_time.isoformat(),
            "check_out_time": self.check_out_time.isoformat() if self.check_out_time else None,
            "remarks": self.remarks
        }


@dataclass
class AttendanceSummary:
    """Summary statistics for attendance"""
    total_days: int
    present_days: int
    absent_days: int
    attendance_percentage: float