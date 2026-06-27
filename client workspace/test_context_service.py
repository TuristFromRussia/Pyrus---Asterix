from services.context_service import (
    ContextService
)

service = ContextService()

context = (
    service.get_context_by_phone(
        "+79991112233"
    )
)

print(context)