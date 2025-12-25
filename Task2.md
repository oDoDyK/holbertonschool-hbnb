# HBnB Evolution - Sequence Diagrams for API Calls

This section presents the sequence diagrams for four key API calls in the HBnB Evolution application, illustrating the interaction between the Presentation Layer (API, Services), Business Logic Layer (Models), and Persistence Layer (Database).

```mermaid
sequenceDiagram
participant User
participant API
participant HBNBFacade as BusinessLogic
participant Repository
participant Database

User->>API: Submit registration form
API->>BusinessLogic: Validate input & process registration
BusinessLogic->>Repository: Create new User record
Repository->>Database: Save User data
Database-->>Repository: Confirm save
Repository-->>BusinessLogic: User created
BusinessLogic-->>API: Return success response
API-->>User: Registration successful

sequenceDiagram
participant User
participant API
participant HBNBFacade as BusinessLogic
participant Repository
participant Database

User->>API: Submit new Place details
API->>BusinessLogic: Validate & process place creation
BusinessLogic->>Repository: Create Place record linked to User
Repository->>Database: Save Place data
Database-->>Repository: Confirm save
Repository-->>BusinessLogic: Place created
BusinessLogic-->>API: Return success response
API-->>User: Place creation successful


sequenceDiagram
participant User
participant API
participant HBNBFacade as BusinessLogic
participant Repository
participant Database

User->>API: Submit review for a Place
API->>BusinessLogic: Validate & process review
BusinessLogic->>Repository: Create Review linked to User & Place
Repository->>Database: Save Review data
Database-->>Repository: Confirm save
Repository-->>BusinessLogic: Review created
BusinessLogic-->>API: Return success response
API-->>User: Review submission successful


sequenceDiagram
participant User
participant API
participant HBNBFacade as BusinessLogic
participant Repository
participant Database

User->>API: Request list of Places
API->>BusinessLogic: Forward request with criteria
BusinessLogic->>Repository: Query Places
Repository->>Database: Fetch Place records
Database-->>Repository: Return Place data
Repository-->>BusinessLogic: Places retrieved
BusinessLogic-->>API: Return list of Places
API-->>User: Display list of Places



```
## Explanatory Notes

### User Registration
- **Purpose:** Allow a new user to create an account.
- **Key Steps:** 
  1. User submits form  
  2. API validates  
  3. Business Logic processes  
  4. Repository saves  
  5. Database persists  
  6. Success confirmation
- **Layer Contribution:**  
  - **Presentation Layer:** Receives request and returns response  
  - **Business Logic Layer:** Validates and applies rules  
  - **Persistence Layer:** Stores data securely

### Place Creation
- **Purpose:** Enable users to create new property listings.
- **Key Steps:** 
  1. API receives place details  
  2. Business Logic validates  
  3. Repository creates record  
  4. Database saves  
  5. Success response
- **Layer Contribution:**  
  - Ensures correct association between Place and User  
  - Handles multiple amenities if provided

### Review Submission
- **Purpose:** Allow users to leave feedback for places.
- **Key Steps:** 
  1. Submit review  
  2. Validation  
  3. Repository saves  
  4. Confirmation
- **Layer Contribution:**  
  - Maintains relationships between User and Place  
  - Enforces business rules (rating limits, comment length, etc.)

### Fetching a List of Places
- **Purpose:** Retrieve places matching user-specified criteria.
- **Key Steps:** 
  1. API request  
  2. Business Logic queries  
  3. Repository fetches  
  4. Database returns  
  5. Response to user
- **Layer Contribution:**  
  - Presentation Layer formats and displays results  
  - Business Logic applies filters and sorting  
  - Repository and Database ensure efficient data retrieval
