# 6 Step framework

|--------------|  |---------------|  |---------------|  |-----------|  |-------------------|  |------------|
|1.Requirements|->|2.Core Entities|->|3.API/Interface|->|4.Data Flow|->|5.High Level Design|->|6.Deep Dives|
|--------------|  |---------------|  |---------------|  |-----------|  |-------------------|  |------------|
     ^  ^                                                                         |                  |
     |  |                                                                         |                  |
     |  |_________________________________________________________________________|                  |
     |                          Primary Goal:                                                        |
     |                 Satisfy Functional Requirements                                               |
     |                                                                                               |
     |                                  Primary  Goal:                                               |       
     |                        Satisfy non-functional requirements                                    |
     |_______________________________________________________________________________________________|


# 1. Requirements

Two types -
1. Functional: feature of the system
                -  user should be able to book the ticket
2. Non-functional: quality of the system
                - booking a ticket should have low latency
                - system should be able to scale with x number of users.

## 2. Core Entities

1. It typically maps directly to the tables in your database.
2. These are just the entities that your system will persists and your API will exchange.
3. Example: a user, an event, a ticket.

### 3. API/Interface

1. Nine times out of ten these going to be REST endpoints, but there might be unique cases where GraphQL or something else makes more sense.

#### 5. High Level Design

1. From here, you headover to the white board and start drawing boxes and arrows starting with really simple, high level design.
2. Goal of the high level design is to meet the functional requriements of your system.
3. Really simple, not complex design, that allow users to say book a ticket.

##### 6. Deep Dives

1. Enhance initital high level design by deep dives.
2. Goal of the deep dive is to satisfy non-functional requirements.

*Now when I can book the ticket -
How can I make sure -
i. ticket booking system (for e.g.) is low latency?
ii. it's strongly consistent?
iii. it can scale to the scale numbers that you agreed upon with your interviewer?
-----------------------------------------------------------------------------------------------------------------------------------------------------------

# How are system design interviews evaluated?
1. Problem solving: Identify and priortize the core challenge.
                    - If you are designing ticket master, you should be focused on the booking flow not on the authentication.

2. Soltuion design: Create scalable architectures with balanced trade-offs.
                    - Did you weigh trade-offs
                    - Did you arrive at something that meets those functional requirements.

3. Technical Excellence: Demonstrate deep knowledge and expertise.
                    - This is what you will show in step 6 (deep dives), that you have technical expertise in, some, not all, but in some areas of the system.
                    - Can you go deep?
                    -  Talk about specific technology, talk about specific areas where things will break all of this.
                  
4. Communication: clearly explian complex concepts to stakeholders.




