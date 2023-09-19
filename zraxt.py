from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///pharmacy_Section.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pharmacy(Base):
    __tablename__ = 'pharmacys'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Establish a one-to-many relationship with Section
    Sections = relationship(
        'Section', back_populates='pharmacy', cascade='all, delete-orphan')


class Section(Base):
    __tablename__ = 'Sections'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Create a foreign key relationship to Pharmacy
    pharmacy_id = Column(Integer, ForeignKey('pharmacy.id'))

    # Create a reference to the Pharmacy object using the relationship
    pharmacy = relationship('Pharmacy', back_populates='Sections')


Base.metadata.create_all(engine)

# Create pharmacys and Sections
pharmacy1 = Pharmacy(name='General Pharmacy')
Section1 = Section(name='Cardiology', pharmacy=pharmacy1)
Section2 = Section(name='Pediatrics', pharmacy=pharmacy1)

pharmacy2 = Pharmacy(name='Children\'s Pharmacy')
Section3 = Section(name='Neonatology', pharmacy=pharmacy2)

session.add(pharmacy1)
session.add(Section1)
session.add(Section2)
session.add(pharmacy2)
session.add(Section3)
session.commit()

# Query the database
general_pharmacy = session.query(Pharmacy).filter_by(
    name='General Pharmacy').first()
print(f'{general_pharmacy.name} has Sections:')
for Section in general_pharmacy.Sections:
    print(f'- {Section.name}')

# Delete a pharmacy and check if linked Sections are deleted automatically
session.delete(general_pharmacy)
session.commit()

Sections_in_general_pharmacy = session.query(
    Section).filter_by(pharmacy_id=general_pharmacy.id).all()
if not Sections_in_general_pharmacy:
    print("All Sections in General Pharmacy have been deleted.")
