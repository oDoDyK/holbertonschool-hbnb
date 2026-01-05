```mermaid

classDiagram
    %% =======================
    %% Presentation Layer
    %% =======================
    class API {
        <<Presentation>>
    }

    class Services {
        <<Presentation>>
    }

    %% =======================
    %% Business Logic Layer (Facade)
    %% =======================
    class HBNBFacade {
        <<Facade>>
        %% Represents the Business Logic Layer
    }

    %% =======================
    %% Persistence Layer
    %% =======================
    class Repository {
        <<Persistence>>
    }

    %% =======================
    %% Relationships
    %% =======================
    API --> HBNBFacade : Uses Facade
    Services --> HBNBFacade : Uses Facade
    HBNBFacade --> Repository : Interacts With
