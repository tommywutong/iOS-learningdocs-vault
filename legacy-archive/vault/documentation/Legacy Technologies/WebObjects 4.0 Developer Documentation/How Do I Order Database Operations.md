---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/FAQ5.html
archived_at: '2026-07-18T01:19:48.095651Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Previous Section](How%20Do%20I%20Invoke%20a%20Stored%20Procedure.md)

# How Do I Order Database Operations?

An Enterprise Objects Framework application typically queues up changes to many enterprise objects before saving the changes to the database. It is then the job of an EODatabaseContext to analyze an object graph to determine what has changed, translate the changes to database operations, and perform the operations using an EOAdaptorChannel.
Enterprise Objects Framework implements a default algorithm for ordering the database operations that reduces the number of scenarios in which you have to reorder adaptor operations programmatically. Enterprise Objects Framework builds an entity ordering by identifying "master" and "detail" entities as follows.

- If an entity (Employee, for example) has a to-one relationship to a second entity (Department) and the inverse relationship is a to-many, then the second entity (Department) is considered the _master_.
- If an entity has a to-one relationship to a second entity and the inverse relationship is also to-one, then the framework checks if one of the relationships propagates its primary key. The source of the "propagatesPrimaryKey" relationship is considered to be the master entity.

Before sending operations to the database, Enterprise Objects Framework orders the operations based on these master definitions. The operations will have the following order:

- Lock operations (master entities before detail entities)
- Inserts (master entities before detail entities)
- Updates (master entities before detail entities)
- Deletes (detail entities before master entities)

However, if your database uses sophisticated referential integrity, if it uses triggers, or there are referential integrity constraints that are not modeled in EORelationships, you may still need to reorder adaptor operations programmatically.
For example, if Employees have to-one relationships to their managers, then you will have to explicitly order the database operations such that a manager is inserted before that manager's direct reports are inserted. Enterprise Objects Framework can't catch this case because the relationship is self-referential.
Another example of when you might reorder database operations is when you want to use the same ordering algorithm that other non-Enterprise Objects Framework applications are using to prevent deadlock contention problems (such as can occur with Sybase servers). If a Framework application takes locks in a different order than other non-Framework applications, then you might encounter deadlock problems.
You can order database operations by implementing either or both of the following EODatabaseContext delegate methods
In Java:

- databaseContextWillOrderAdaptorOperations
- databaseContextWillPerformAdaptorOperations

In Objective-C:

- databaseContext:
  willOrderAdaptorOperationsFromDatabaseOperations:
- databaseContext:
  willPerformAdaptorOperations:
  adaptorChannel:

The "willOrder" method provides the delegate with more information from the object graph than the "willPerform" method. However, "willPerform" can be more convenient. Its second argument is an array of adaptor operations that are already prepared. The delegate only needs to rearrange them. For more information on these delegate methods, see the EODatabaseContext class specification in the _Enterprise Objects Framework Reference_.

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Next Section](How%20Are%20Enterprise%20Objects%20Cleaned%20Up.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
