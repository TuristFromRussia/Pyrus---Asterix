class CallRepository:

    def save(self, call):
        ...

    def get_by_unique_id(
        self,
        unique_id
    ):
        ...

    def update_status(
        self,
        unique_id,
        status
    ):
        ...