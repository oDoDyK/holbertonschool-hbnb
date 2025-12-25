# HBnB Evolution - Business Logic Layer Class Diagram

```mermaid
classDiagram
    %% =======================
    %% User Class
    %% =======================
    class User {
        +UUID id
        +String first_name
        +String last_name
        +String email
        +String password
        +Boolean is_admin
        +DateTime created_at
        +DateTime updated_at
        +register()
        +update_profile()
        +delete_account()
    }

    %% =======================
    %% Place Class
    %% =======================
    class Place {
        +UUID id
        +String title
        +String description
        +Float price
        +Float latitude
        +Float longitude
        +DateTime created_at
        +DateTime updated_at
        +add_amenity(amenity)
        +remove_amenity(amenity)
        +update_details()
        +delete_place()
    }

    %% =======================
    %% Review Class
    %% =======================
    class Review {
        +UUID id
        +UUID place_id
        +UUID user_id
        +Integer rating
        +String comment
        +DateTime created_at
        +DateTime updated_at
        +update_review()
        +delete_review()
    }

    %% =======================
    %% Amenity Class
    %% =======================
    class Amenity {
        +UUID id
        +String name
        +String description
        +DateTime created_at
        +DateTime updated_at
        +update_amenity()
        +delete_amenity()
    }

    %% =======================
    %% Relationships
    %% =======================
    User "1" -- "0..*" Place : owns
    Place "1" -- "0..*" Review : has
    User "1" -- "0..*" Review : writes
    Place "0..*" -- "0..*" Amenity : includes
