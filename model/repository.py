from model.entity import Movie, Review


class MovieRepository:
    def insert(movie: Movie):
        pass
    
    def findByCode(code: str)->list:
        pass
    
    def findAll()-> list:
        pass

class ReviewRepository:
    def insert(review: Review):
        pass
    
    def findByCode(code: str)->list:
        pass
    
    def findAll()-> list:
        pass
    
    def update(review: Review):
        pass
    
    def delete(id: int) -> None:
        pass