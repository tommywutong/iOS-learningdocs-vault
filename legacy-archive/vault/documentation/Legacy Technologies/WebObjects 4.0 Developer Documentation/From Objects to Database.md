---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/WhatsEOF4.html
archived_at: '2026-07-18T01:19:52.947079Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Previous Section](From%20Objects%20to%20Interface.md)

# From Objects to Database

After your program has accumulated changes to enterprise objects, it needs to push those changes back to the database. Enterprise Objects Framework manages this process, too, analyzing the objects for changes, generating corresponding database operations, and executing those operations to synchronize the database with in-memory enterprise objects. The Framework has mechanisms for ensuring that the integrity of your data is maintained between your application and the database:

- Validation
- Referential integrity enforcement
- Automatic primary and foreign key generation
- Transaction management
- Locking

Each of these is described in the following sections.

## Validation

A good part of your application's business logic is usually validation-for example, verifying that customers don't exceed their credit limits, that return dates don't come before their corresponding check out dates, and so on. In your enterprise object classes, you implement methods that check for invalid data, and the framework automatically invokes them before saving anything to the database.

## Referential Integrity Enforcement

Enterprise Objects Framework allows you to specify rules governing the relationships between objects. You can specify whether a to-one relationship is optional or mandatory. For example, you can require that all departments have a location (mandatory), but not require that every employee have a manager (optional).
You can also specify delete rules for relationships. For example, when you delete a department object, you can specify that:

- All the employees in that department are also deleted (a cascading delete).
- All the employees in that department are updated to have no department (nullify).
- The department deletion is rejected if it has any employees (deny).

For more information on Framework's referential integrity enforcement, see the chapter ["Designing Enterprise Objects"](Designing%20Enterprise%20Objects.md#apple-ge2daobr). To learn how to define these rules in the EOModeler application, see the book _Enterprise Objects Framework Tools and Techniques_.

## Automatic Primary and Foreign Key Generation

With Enterprise Objects Framework, you don't have to maintain database artifacts such as database primary and foreign key values into your application. Database primary and foreign keys aren't usually meaningful parts of a business model; rather, they're attributes created in a relational database to express relationships between entities. For example, the primary key (MOVIE_ID) for a movie doesn't have any meaning to users. Users identify movies by their titles.
Enterprise Objects Framework keeps track of primary and foreign key data for you. You don't have to represent that information in your enterprise objects, and you don't have to worry about generating and propagating key values.
For information on eliminating database artifacts from your object model, see the chapter ["Designing Enterprise Objects"](Designing%20Enterprise%20Objects.md#apple-ge2daobr). For information on how the Framework generates primary key values, see the chapter ["Answers to Common Design Questions"](Answers%20to%20Common%20Design%20Questions.md#apple-g44tkoa).

## Transaction Management

For the most part, Enterprise Objects Framework handles transactions for you. You don't have to worry about beginning, committing, or rolling back transactions unless you want to fine-tune transaction management behavior. The Framework uses the native transaction management features of your database to group database operations that correspond to the changes that have been made to enterprise objects in memory. For more information, see the chapter ["Behind the Scenes"](Behind%20the%20Scenes.md#apple-ha2tqni).

Additionally, the Framework provides a separate in-memory transaction management feature. You can create nested contexts in which a child context's changes are folded into the parent context only upon successful completion of an in-memory operation. For more information on nested contexts, see the chapter ["Application Configurations"](Application%20Configurations.md#apple-ge2tqojy).

## Locking

The Framework offers three types of locking:

- _Pessimistic_. With this strategy, Enterprise Objects Framework uses your database server's native locking mechanism to lock rows as they're fetched into your application. If you try to fetch an object that someone else has already fetched, the operation will fail because the corresponding database row is locked. This approach prevents update conflicts by never allowing two users to look at the same object at the same time.
- _Optimistic_. With this strategy, update conflicts aren't detected until you try to save an object's changes to the database. At this point, the Framework checks the database row to see if it's changed since your object was fetched. If the row has been changed, it aborts the save operation.

Enterprise Objects Framework determines that a database row has changed since its corresponding object was fetched using a technique called _snapshotting_. When the Framework fetches an object from the database, it records a _snapshot_ of the state of the corresponding database row. When changes to an object are saved to the database, the snapshot is compared with the corresponding database row to ensure that the row data hasn't changed since the object was last fetched. For more information on snapshots, see the EODatabaseContext class specification in the _Enterprise Objects Framework Reference_.

- _On-Demand_. This approach is a mixture of the pessimistic and optimistic strategies. With on-demand locking, you lock an object after you fetch it but before you attempt to modify it. When you try to get a lock on the object, it can fail for one of two reasons: the corresponding database row has changed since you fetched the object (optimistic locking), or because someone else already has a lock on the row (pessimistic locking).

For more information on Enterprise Objects Framework's locking strategies, see the chapter ["Behind the Scenes"](Behind%20the%20Scenes.md#apple-ha2tqni).

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Next Section](Ingredients%20of%20an%20Enterprise%20Objects%20Framework%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
