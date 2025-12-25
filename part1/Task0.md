# HBnB Evolution - High-Level Architecture

This file shows the three layers in HBnB Evolution and the connection between them via **Facade Pattern**.

```mermaid
classDiagram
    %% =======================
    %% Presentation Layer
    %% =======================
    class API {
        <<Presentation>>
        %% Handles user requests via endpoints
    }
    class Services {
        <<Presentation>>
        %% Provides service logic for API
    }

    %% =======================
    %% Business Logic Layer
    %% =======================
    class HBNBFacade {
        <<Facade>>
        %% Unified interface to interact with models
    }

    %% =======================
    %% Persistence Layer
    %% =======================
    class Repository {
        <<Persistence>>
        %% Manages data operations for models
    }
    class Database {
        <<Persistence>>
        %% Stores application data
    }

    %% =======================
    %% Models
    %% =======================
    class User {
        <<Model>>
    }
    class Place {
        <<Model>>
    }
    class Review {
        <<Model>>
    }
    class Amenity {
        <<Model>>
    }

    %% =======================
    %% Relationships
    %% =======================
    API --> HBNBFacade : Uses Facade
    Services --> HBNBFacade : Uses Facade
    HBNBFacade --> Repository : Interacts With
    Repository --> Database : Stores Data

    %% Models connected to Repository
    Repository --> User : Manages
    Repository --> Place : Manages
    Repository --> Review : Manages
    Repository --> Amenity : Manages

```mermaid
classDiagram
    %% =======================
    %% Presentation Layer
    %% =======================
    class API {
        <<Presentation>>
        %% Handles user requests via endpoints
    }
    class Services {
        <<Presentation>>
        %% Provides service logic for API
    }

    %% =======================
    %% Business Logic Layer
    %% =======================
    class HBNBFacade {
        <<Facade>>
        %% Unified interface to interact with models
    }

    %% =======================
    %% Persistence Layer
    %% =======================
    class Repository {
        <<Persistence>>
        %% Manages data operations
    }
    class Database {
        <<Persistence>>
        %% Stores application data
    }

    %% =======================
    %% Models
    %% =======================
    class User {
        <<Model>>
    }
    class Place {
        <<Model>>
    }
    class Review {
        <<Model>>
    }
    class Amenity {
        <<Model>>
    }

    %% =======================
    %% Relationships
    %% =======================
    API --> HBNBFacade : Uses Facade
    Services --> HBNBFacade : Uses Facade
    HBNBFacade --> Repository : Interacts With
    Repository --> Database : Stores Data


```
## Explanatory Notes

### 1. Presentation Layer
**Components:** `API`, `Services`  
**Responsibilities:**  
- Handles all interactions with the end-users.  
- Exposes endpoints and service logic for users to perform operations like registering, creating places, submitting reviews, etc.  
- Does **not** directly access the database or business logic; instead, it communicates via the **Facade**.  

---

### 2. Business Logic Layer
**Components:** `HBNBFacade`  
**Responsibilities:**  
- Implements the core business logic of the application.  
- Aggregates operations on models (`User`, `Place`, `Review`, `Amenity`) and provides a **unified interface** for the Presentation Layer.  
- Ensures that rules such as associating a place with its owner, or managing amenities and reviews, are correctly enforced.  

**Role of the Facade Pattern:**  
- The **Facade** simplifies communication between the Presentation Layer and the Persistence Layer.  
- It provides a single, unified interface (`HBNBFacade`) that handles all interactions with models and delegates data operations to the Repository.  
- This prevents the Presentation Layer from dealing with multiple models or data operations directly, improving maintainability and modularity.  

---

### 3. Persistence Layer
**Components:** `Repository`, `Database`  
**Responsibilities:**  
- Responsible for storing, retrieving, updating, and deleting data.  
- `Repository` abstracts data operations for all models and provides a consistent interface for the Business Logic Layer.  
- `Database` represents the actual storage system where all entities (`User`, `Place`, `Review`, `Amenity`) are persisted.  
- Ensures data consistency, integrity, and auditability (e.g., creation/update timestamps, unique IDs).

---

### 4. Models
**Components:** `User`, `Place`, `Review`, `Amenity`  
**Responsibilities:**  
- Represent the core entities in the system.  
- Hold attributes and relationships for each entity (e.g., Place has amenities, Review is linked to a Place and User).  
- Managed indirectly through the **Repository** and **Facade**, never directly accessed by the Presentation Layer.  
