from repositories.client_repository import ClientRepository


repo = ClientRepository()

client = repo.create(
    phone="+79991112233",
    name="Иван Петров",
    company="ООО Ромашка"
)

print(client)

found = repo.get_by_phone(
    "+79991112233"
)

print(found)

print(repo.get_all())