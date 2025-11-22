from fastapi import HTTPException, status


class BaseDAO():
    lst = None
    
    @classmethod
    def find_by_id_or_404(cls, id: int):
        for obj in cls.lst.values():
            if obj.id == id:
                return obj
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")