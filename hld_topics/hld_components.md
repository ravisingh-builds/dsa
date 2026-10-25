1. Database
        - Postgres: Traditional database that keeps everything organised in strict little tables with clear and define rules.
        - MongoDB: store informaiton more in documents, JSON Blob
        - Redis: store simple key value pair, you can look up quickly.

        - How do you app read and write data?
        - Choose option that make those common operation fast and simple.

2. Cache
        - System short term memory
        - They are very fast but do comes up with their owne challenges
        - Mainly around keeping data fresh.
        - You need to decide 
            - how long informaiton stay valid?
            - when you kick it out of the cache?
        - Main thing to remember when you are introducing cache in your system
            - they will make your system lighting fast
            - but managing them add some additional complexities in your design that you should be aware of

3. Message Queues
        - Asynchronomous communication buffer
        - Instead of making direct call, one service can drop a message in a queue and then another service can pick it up and process it.
        - Kafka, RabbitMQ, SQS
        - you can think of it as texting instead of calling. You don't need both sides available at the same time.
        - it helps your system handle traffic spikes and keeo things running, particularly if one service were to crash, for example.
        - But the main challenge is making sure that messages actually get delivered at the first place.
        - Sometimes they get delivered once, sometimes they get delivered multiple times.
        - You will need strategies in order to handle this.

4. Load Balancer
        
5. Blob Storage
        - Your database is designed for organised, structured data like user accounts or product information.
        - It's not designed for storing large files, images or videos.
        - Trying to cram thos things into your DB is like forcing a square package into a round hole.
        - It's going to bloat your database and it's going to slow down all your queries and make backups a nightmare.
        - That's why services like Blob storage services, S3, being a popular example exists.
        - They are specifically built to handle these type of unstructured data.
        - This is typically media, large text files, etc.
        - they can host them at a much cheaper cost.
        - therefore, always keep your structured data in your database.
        - and keep your unstructed data in the blob storage.

6. Content Delivery Network: CDN
        - It's just a cache
        - It serves as global destribution system
        - You can place your content closer to user around the world.
        - Popular ones are cloudflare.
        - They can store the copies of the images and the videos an other statis files often times that you'r hosting in your Blob storage but they are going to store them closer to the user.
        - It's going to make it lot faster for the users to download these resources because they don't have to go all the way to Amercia if they'r in India.
        - They can just pull these images and files directly from a CDN server in they native country.
