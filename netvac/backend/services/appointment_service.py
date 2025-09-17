from netvac.backend.models.appointment import Appointment

class AppointmentService:
    @classmethod
    def get_appointment_by_id(cls, id):
        return Appointment.get_by_id(id)

    @classmethod
    def get_all_appointments(cls):
        return Appointment.get_all()