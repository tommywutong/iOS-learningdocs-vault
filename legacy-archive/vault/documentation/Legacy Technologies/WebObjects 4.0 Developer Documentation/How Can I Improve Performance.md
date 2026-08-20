---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/FAQ1.html
archived_at: '2026-07-18T01:19:47.619609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Previous Section](Answers%20to%20Common%20Design%20Questions.md)

# How Can I Improve Performance?

In an Enterprise Objects Framework application, every trip to the database and every object fetched is a potential drag on performance. Consequently, a large part of designing for performance entails answering these questions:

- How can I minimize my application's trips to the database?
- When I _do_ have to make trips to the database, how can I best take advantage of them?
- How can I avoid fetching objects I'll never need, while still maintaining access to objects I might need?

Enterprise Objects Framework has several built-in features for intelligently managing your application's interactions with the database. It also has hooks for fine-tuning this behavior to get the best performance for your application.

## Controlling the Number of Objects Fetched

If you define a fetch specification in your model, you can set a fetch limit for it in EOModeler. You can also define what should happen if the fetch limit is reached. For more information, see _Enterprise Objects Framework Tools and Techniques_.
If you're not using a predefined fetch specification, you set the fetch limit programmatically using EOFetchSpecification's __setFetchLimit__ method (__setFetchLimit:__ in Objective-C) passing an integer value indicating the maximum number of objects to fetch (an unsigned integer value in Objective-C). The default value is zero, indicating no fetch limit.
The EODatabaseContext will either stop fetching objects when this limit is reached or ask the EOEditingContext's message handler to ask the user whether it should continue fetching. The default behavior simply stops fetching, so if you want to prompt the user, send __setPromptsAfterFetchLimit__ (__setPromptsAfterFetchLimit:__ in Objective-C) to the fetch specification with __true__ (YES in Objective-C) as the argument. For more information on managing fetch limits, see the EOFetchSpecification class description and the EOEditingContext EOMessageHandlers interface description in the _Enterprise Objects Framework Reference_.

## Faulting

When an EODatabaseContext fetches an object, it uses the relationships defined in the model to fetch related objects. For example, if you fetch an employee object, you can access its manager directly; you don't have to get the manager's employee ID from the object you just fetched and fetch the manager yourself.
However, EODatabaseContext doesn't fetch related objects immediately, since they may never be accessed and fetching can be expensive. Instead the destination objects created are stand-ins, called _faults_, that fetch their data the first time they're accessed.
When a fault is accessed (sent a message for which it must get its data to respond), it triggers its EODatabaseContext to fetch its data and finish initializing it. This works well for limited numbers of objects. However, suppose you fetch multiple employees and then want to retrieve each employee's department. You'd have to loop over all of the employees and fetch each employee's department fault individually, resulting in numerous trips to the database.
To avoid these unnecessarily trips to the database, you can fine-tune faulting behavior for additional performance gains by using two different mechanisms: batch faulting, and prefetching relationships.

### Batch Faulting

When you access a fault, its data is fetched from the database. However, triggering one fault has no effect on other faults-it just fetches the object or array of objects for the one fault. You can take advantage of this expensive round trip to the database server by batching faults together. When you do this, triggering one fault (such as an employee's department) has the effect of fetching multiple faults. This reduces the number of fetches-the next time you access an employee's department, it's less likely to require a trip to the database.
You can configure batch faulting in a model with EOModeler. With this approach, you specify the number of faults for the same entity or relationship that should be triggered along with the first fault. For more information on setting batch faulting in an EOModel, see _Enterprise Objects Framework Tools and Techniques_.
To actually control which faults are triggered along with the first one, you can use the EODatabaseContext method __batchFetchRelationship__ (__batchFetchRelationship:forSourceObjects:editingContext:__ in Objective-C). For example, given an array of Employee objects, this method can fetch all of their departments with one round trip to the server, rather than asking the server for each of the employee's departments individually. For more information, see the EOFetchSpecification class description in the _Enterprise Objects Framework Reference_.

### Prefetching Relationships

Sometimes it's more efficient to specify _prefetching relationships_ so that related objects are fetched at the same time. For example, when fetching employees, you can define a prefetching relationship between an employee and a department to force these objects to be fetched as well, as opposed to having faults created for them. Although prefetching increases the initial fetch cost, it can improve overall performance by reducing the number of round trips made to the database server.
If you define your fetch specification in a model, you can configure its prefetching behavior in EOModeler. For more information, see _Enterprise Objects Framework Tools and Techniques_.
Alternatively, you can programmatically set prefetching relationships by sending __setPrefetchingRelationshipKeyPaths__ (__setPrefetchingRelationshipKeyPaths:__ in Objective-C) to an EOFetchSpecification object and passing an array of relationship key paths whose destinations should be fetched along with the objects specified. For more information, see the EOFetchSpecification class description in the _Enterprise Objects Framework Reference_.

## Caching an Entity's Objects

You can cache an entity's objects in memory for quick access. Caching an entity's objects allows Enterprise Objects Framework to evaluate queries in memory, thereby avoiding round trips to the database. This is most useful for read-only entities, where there is no danger of the cached data getting out of sync with database data. This technique should only be used with small tables, since it fetches the entire table into memory.
To set up object caching on an entity, you can use the Advanced Entity Inspector in EOModeler or you can do it programmatically using the EOEntity method __setCachesObjects__ (__setCachesObjects:__ in Objective-C). For more information on configuring object caching in EOModeler, see _Enterprise Objects Framework Tools and Techniques_, and for more information on object caching, see the EOEntity class specification in the _Enterprise Objects Framework Reference_.

## Creating an EOModel for Optimal Performance

The way you design your EOModel has a direct effect on how your application interacts with the database, and consequently, on performance. There are a few general guidelines you should observe:

- Avoid flattening objects whenever possible.
- Use inheritance wisely.
- Don't set BLOB attributes to be used for locking.

Each is discussed in the following sections.

### Avoid Flattening Attributes

Flattening attributes has two major drawbacks:

- The values of flattened attributes can get out of sync with the object graph (which represents the most current view of data in your application). This limitation doesn't apply if you're flattening a one-to-one relationship in order to map a class across multiple tables.
- Fetching objects that span multiple database tables requires database joins, which are expensive. If you find yourself designing an application that requires flattened attributes, you should consider whether there's a more efficient approach.

Instead of flattening attributes, you can directly traverse relationships in the object graph. For example, the following statements access the value of a __departmentName__ property belonging to the Department object to which Employee has a relationship:
In Java:

```
// Get the name of the Employee's department
employee.department().departmentName();

// Set the name of the employee's department
employee.department().setDepartmentName(newName);
```


In Objective-C:

```
// Get the name of the Employee's department
[[employee department] departmentName];

// Set the name of the employee's department
[[employee department] setDepartmentName:newName];
```


For more discussion of this subject, see the chapter ["Designing Enterprise Objects"](Designing%20Enterprise%20Objects.md#apple-ge2daobr).

### Use Inheritance Wisely

As discussed in the chapter "Designing Enterprise Objects," the way that you map an object hierarchy onto a relational database in your EOModel can have a significant effect on performance. You should observe the following guidelines:

- Avoid mapping a deep object hierarchy onto a relational database since it will probably result in multiple fetches and joins.
- Try to avoid using vertical inheritance mapping, since it's the least efficient of the possible approaches.

### Don't Use BLOB Attributes For Locking

In EOModeler the Used For Locking setting indicates whether an attribute should be checked for changes before an update is allowed. This setting applies when you're using Enterprise Object Framework's default update strategy, optimistic locking. Under optimistic locking, the state of a row is saved as a _snapshot_ when you fetch it from the database. When you perform an update, the snapshot is checked against the row to make sure the row hasn't changed. If you set Used For Locking for an attribute whose data is a BLOB type, it can increase the cost of updating the row containing the BLOB.
Ideally, you should store BLOBs in their own table away from more commonly accessed attributes.

## Updating the User Interface Display

When objects change in the EOEditingContext for an EODisplayGroup, the EODisplayGroup by default refreshes all of its EOAssociations, even if none of the EODisplayGroup's objects is in the EOEditingContext notification change list.
This "universal" refresh is sometimes necessary because EOAssociations may display derived values (through key paths or business methods) that depend on objects other than the ones being displayed. However, if you know that your user interface doesn't display derived data, you can specify that an EODisplayGroup's EOAssociation objects be refreshed only if the EODisplayGroup objects change.
There are different ways to accomplish this:

- In Interface Builder, display the Attributes view of the EODisplayGroup Inspector and uncheck "Refresh All".
- In your code, include a statement such as the following:

In Java:

```
myDisplayGroup.setUsesOptimisticRefresh(true);
```


In Objective-C:

```
[myDisplayGroup setUsesOptimisticRefresh:YES];
```


This is equivalent to unchecking "Refresh All" in Interface Builder for __myDisplayGroup__.

- Implement the EODisplayGroup delegate method __displayGroupShouldRedisplay__ (__displayGroup:shouldRedisplayForChangesInEditingContext:__ in Objective-C) to control when redisplay occurs.

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Next Section](How%20Do%20I%20Generate%20Primary%20Keys.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
