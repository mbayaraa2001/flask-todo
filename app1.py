from sqlalchemy import create_engine

engine = create_engine('sqlite:///sample.db',echo=True)

print(engine)