# 🏠 HBnB Evolution – Technical Design Document

## 1. Introduction

### 1.1 Purpose of This Document 📄
This technical document provides a comprehensive architectural and design blueprint for the **HBnB Evolution** application, a simplified AirBnB-like platform. It serves as a reference for the implementation phases of the project by clearly describing the system structure, core business entities, and interaction flows.

### 1.2 Scope 🎯
This document includes:  
- 🏗️ A high-level architectural overview of the system  
- 📊 A detailed class diagram for the Business Logic layer  
- 🔄 Sequence diagrams illustrating API interaction flows  
- 📝 Explanatory notes explaining design decisions and data flow  

---

## 2. High-Level Architecture

### 2.1 Architectural Overview 🏛️
HBnB Evolution follows a layered architecture composed of three main layers:

**Presentation Layer 🌐**  
- Exposes RESTful APIs  
- Handles HTTP requests and responses  
- Acts as a facade to the Business Logic layer  

**Business Logic Layer ⚙️**  
- Contains domain models and core business rules  
- Validates data and enforces application constraints  

**Persistence Layer 💾**  
- Responsible for data storage and retrieval  
- Abstracts database operations from business logic  

This separation ensures maintainability, scalability, and testability.

### 2.2 High-Level Package Diagram 🗂️

``` mermaid
classDiagram
    class API {
        <<Presentation>>
    }
    class Services {
        <<Presentation>>
    }
    class HBNBFacade {
        <<Facade>>
    }
    class Repository {
        <<Persistence>>
    }
    class Database {
        <<Persistence>>
    }
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

    API --> HBNBFacade : Facade Pattern
    Services --> HBNBFacade : Facade Pattern
    HBNBFacade --> Repository : CRUD Operations
    Repository --> Database : stores data

    %% Standalone model classes
    %% (No direct relationships but included for completeness)
```

**Explanation 💡**  
- The Presentation Layer communicates only with the Business Logic layer.  
- The Business Logic layer coordinates all operations and delegates data storage to the Persistence layer.  
- The Persistence layer does not communicate directly with the Presentation layer.  

---

## 3. Business Logic Layer – Class Diagram 🏗️

### 3.1 Overview 🔹
The Business Logic layer contains the core entities:  
- 👤 **User**  
- 🏡 **Place**  
- ✍️ **Review**  
- 🛏️ **Amenity**  

Each entity:  
- Has a unique identifier  
- Tracks creation and update timestamps  
- Encapsulates business rules relevant to its domain  

### 3.2 Class Diagram 📊

``` mermaid
classDiagram
  class BaseEntity {
    +UUID id
    +datetime created_at
    +datetime updated_at
  }

  class User {
    +string first_name
    +string last_name
    +string email
    +string password
    +boolean is_admin
    +create()
    +update()
    +delete()
  }

  class Place {
    +string title
    +string description
    +float price
    +float latitude
    +float longitude
    +create()
    +update()
    +delete()
  }

  class Review {
    +int rating
    +string comment
    +create()
    +update()
    +delete()
  }

  class Amenity {
    +string name
    +string description
    +create()
    +update()
    +delete()
  }

  BaseEntity <|-- User
  BaseEntity <|-- Place
  BaseEntity <|-- Review
  BaseEntity <|-- Amenity

  User "1" o-- "many" Place : owns
  User "1" o-- "many" Review : writes
  Place "1" o-- "many" Review : has
  Place "1" o-- "many" Amenity : includes
```

### 3.3 Design Rationale 💡
- **User–Place relationship** ensures ownership of listings.  
- **Place–Review relationship** allows feedback from multiple users.  
- Many-to-many **Place–Amenity relationship** provides flexibility in property features.  
- CRUD methods are included to support API operations.  
- Timestamps support audit and traceability requirements.  

---

## 4. API Interaction Flow – Sequence Diagrams 🔄

### 4.1 User Registration 📝
**Description**  
Handles new user creation with validation and persistence.  

``` mermaid
sequenceDiagram
    actor User
    participant API as API Service
    participant BL as Business Logic
    participant DB as Database

    User->>API: Create User
    API->>BL: create_user()
    BL->>BL: Validate user data

    alt User data valid
        BL->>DB: Save user data
        DB-->>BL: User created confirmation
        BL-->>API: User create successful
        API-->>User: HTTP 201 Created
    else User data invalid
        BL-->>API: Invalid user data request
        API-->>User: HTTP 400 Bad Request
    end
```

### 4.2 Place Creation 🏡
**Description**  
Allows a user to create a new place listing.  

``` mermaid
sequenceDiagram
    actor User
    participant API as API Service
    participant BL as Business Logic
    participant DB as Database

    User->>API: Create listing request
    API->>BL: create_listing(data)
    BL->>BL: Validate listing data

    alt Listing data valid
        BL->>DB: Save listing
        DB-->>BL: Listing save confirmation
        BL-->>API: Listing create successful
        API-->>User: HTTP 201 Created
    else Listing data invalid
        BL-->>API: Invalid data error
        API-->>User: HTTP 400 Bad Request
    end
```

### 4.3 Review Submission ✍️
**Description**  
Allows users to submit reviews for places.  

``` mermaid
sequenceDiagram
    actor User
    participant API as API Service
    participant BL as Business Logic
    participant DB as Database

    User->>API: Review Submission
    API->>BL: post_review()
    BL->>BL: Validate review data

    alt Review submission valid
        BL->>DB: Save Review
        DB-->>BL: Review stored confirmation
        BL-->>API: Review posted successful
        API-->>User: HTTP 201 Created
    else Review submission invalid
        BL-->>API: Review not valid
        API-->>User: HTTP 400 Bad Request
    end
```

### 4.4 Fetching a List of Places 📋
**Description**  
Retrieves available places based on optional filters.  

``` mermaid
sequenceDiagram
    actor User
    participant API as API Service
    participant BL as Business Logic
    participant DB as Database

    User->>API: Fetch place list request
    API->>BL: getPlaces()
    BL->>DB: Query all listings
    DB-->>BL: Return list of listings
    BL-->>API: Return place list
    API-->>User: HTTP 200 OK
```

---

## 5. Conclusion ✅
This technical document defines the architecture, business entities, and interaction flows of the HBnB Evolution application. By combining UML diagrams with explanatory notes, it provides a clear and reliable reference for the implementation phases.

The layered design ensures:  
- 🧹 Clean separation of concerns  
- 🛠️ Maintainable and extensible codebase  
- 🌟 Alignment with industry best practices
