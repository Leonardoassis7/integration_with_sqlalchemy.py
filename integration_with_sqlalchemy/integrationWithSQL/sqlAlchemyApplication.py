import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column()
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.neme}, fullname={self.fullname})"


class Address(Base):
    __tablename__="address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address (id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(User.__table__)

#conexão com banco de dados
engine = create_engine("sqlite://")

#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

#depreciado sera removido futuro release
#print(engine.table_name())


#investiga o esquema de banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))

print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)



with Session(engine) as session:
    leonardo = User(
        nome='leonardo',
        fullname='roberto assis',
        address=[Address(email_address='leonardo@gmail.com')]
    )

    joao = User(
        name='joao',
        fullname='silva',
        address=[Address(email_address='joao@gamil.com'),
                 Address(email_address='joao@gamil.com.org')]
    )

    pedro = User(
        name='pedro',
        fullname='silva',)

    #enviando para o BD(persistencia de dados)
    session.add_all([leonardo, joao, pedro])

    session.commit()

stmt = select(User).where(User.name.in_(['leonardo']))
print('Recuperando usuarios ')
for user in session.scalar(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando endereço')
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print("\nrecuperation info de maneira ordernada")
for result in session.scalars(order_stmt):
    print(result)

stmt_join = select((User.fullname, Address.email_address).join_from(Address, User))
for result in session.scalars(stmt_join):
    print(result)

#print(select(User.fullname, Address.email_address).join_from(Address, User))

connection = engine.connect()
result = connection.execute(stmt_join).fetchall()
print("\nExecutando statemert a partir de connection")
for result in result:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print("\nTotal de instâncias em User")
for result in session.scalars(stmt_count):
    print(result)