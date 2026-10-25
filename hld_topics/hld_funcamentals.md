1. Storage
        - Should be able to discuss various data storage models and various use cases.
        - Be prepared to explain things like how data is organised in relational database where you have normalised tables with relationships
        - Versus document storage where you have nested JSON-like structures
        - Key-value stores where you have simple look-up mechanism based on a key.
        - Do you understand ACID properties for tranactional systems in particular
        - A = Atomicity
        - C = Consistency
        - I = Isolation
        - D = Durability
        - Are you able to compare and contrast these with BASE principles for distributed databases?
        - B = Basically Available
        - S = Soft State
        - E = Eventually consistent
        - You should be able to articulate when each storage paradigm make sense based on access patterns and given the consistency requriements of your system which you probably agreed upon in non-functional requirements.

2. Scalitbitly
        - How to scale system to support more users/requests?
        - Almost always comes-up in system design interview.
        - Scale Compute: vertical scaling (more CPU and/or more RAM) vs horizontal scaling (more machines)
        - Scale Storage: 
                - Sharding/Partitioning: splitting data across multiple across multiple dBs.
                - Consistent Hashing: how to destribute data efficiently across these databases.
3. Networking
        - Layer 3, 4, and 7 are important.
        - Layer 7:
                - HTTP vs HTTPs
                - API Design: Rest vs GraphQL vs gRPC; which make sense when
                - RESTful Semantics
                - DNS Resolution
                - Websockets vs SSE: real time communication (e.g. a chat app)
        - Layer 4: important for infra style interviews.
                - TCP
                - UDP
                - Request response licecycle
        - Layer 3:
                - Load balancing
                - Firewalls, ACLs

4. Latency, Throughput & Performance
        - There is a decent chance the interview can ask to optimize the performance.
        - For example adding a cache to lower latency.

5. Fault Tolerance & Redundancy
        - Failures are inavitable in destributed systems.
        - Should be ready to discuss things like 
                - Replication strategy
                - failure detection mechanism
        - Your design should incorporate reducndancy at appropriate levels, servers, data centers, so that you can recover these failures gracefully.

6. CAP Theorem
        - Consistency, Availablity, Partition Toleracnce
                - your system can only have 2 of the 3.
                - partition toleracne is a gurantee
                - therefore, your only decision is
                        - should my system priortize availabilty or consistency.
        - You gonna talk about CAP theorem early in your interview, often times in the non-functional requriments.