# ER Diagram Requirements for ALX-AirBnB Database

## Entities
- User
- Property
- Booking
- Payment
- Review
- Message

## Relationships
- User ↔ Booking (One-to-Many)
- User ↔ Property (One-to-Many)
- User ↔ Message (One-to-Many for sender/recipient)
- Property ↔ Booking (One-to-Many)
- Booking ↔ Payment (One-to-One)
- Property ↔ Review (One-to-Many)
- User ↔ Review (One-to-Many)

## Tools Used
- Draw.io

## File
- ER Diagram image: `ERD/airbnb_erd.png`
