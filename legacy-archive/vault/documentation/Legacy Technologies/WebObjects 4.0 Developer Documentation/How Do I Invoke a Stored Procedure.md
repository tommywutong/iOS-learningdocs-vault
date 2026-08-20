---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/FAQ4.html
archived_at: '2026-07-18T01:19:47.883932Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Previous Section](How%20Do%20I%20Use%20My%20Database%20Server%27s%20Integrity-Checking%20Features.md)

# How Do I Invoke a Stored Procedure?

To invoke a stored procedure from your Enterprise Objects Framework application, you must define the stored procedure in a model and decide how to invoke it.
If your stored procedure is defined in the database at the time you create your model, you don't have to do anything to define it. When you create a new model with EOModeler, the application reads stored procedure definitions from the database's data dictionary and stores them in the model's __.eomodeld__ file. However, you can also add a stored procedure definition to an existing model. For more information, see the book _Enterprise Objects Framework Tools and Techniques_.
Depending on what a stored procedure does, you can either invoke it explicitly or specify that the Framework invoke it for common database operations.

## Invoking a Stored Procedure Automatically

You can define stored procedures to perform the following operations:

|  Operation |  Description |
|  FetchAllProcedureOperation |  Fetches all the objects for an entity. |
|  FetchWithPrimaryKeyProcedureOperation |  Fetches an object by its primary key. |
|  InsertProcedureOperation |  Inserts a new object. |
|  DeleteProcedureOperation |  Deletes an object. |
|  NextPrimaryKeyProcedureOperation |  Generates a new primary key value. |

```
```


By associating a stored procedure with an entity's operation, the Framework invokes it automatically when the operation occurs. For example, if you want to use a stored procedure to insert new Customer objects:

- Define the stored procedure in the database.
- Define the stored procedure in the model.
- Associate the stored procedure with the Customer entity's insert operation.

You can associate a stored procedure with an entity using EOModeler as described in the book _Enterprise Objects Framework Tools and Techniques_. Or you can do it programmatically using EOEntity's __setStoredProcedure__ method (__setStoredProcedure:forOperation:__ in Objective-C). For more information on the operations and on setting them programmatically, see the EOEntity class specification in the _Enterprise Objects Framework Reference_.

### Requirements for Framework-Invoked Stored Procedures

When Enterprise Objects Framework invokes a stored procedure for an operation, the procedure must behave in an expected way. The Framework specifies what a stored procedure's arguments, results, and return values should be. The following sections summarize the requirements for each operation:
FetchAllProcedureOperation
The FetchAllProcedureOperation (EOFetchAllProcedureOperation in Objective-C) fetches all the objects for a particular entity. A stored procedure for this operation should have no arguments and return a result set (or in the case of Oracle, a REFCURSOR argument) for all the objects in the corresponding entity.
The rows in the result set must contain values for all the columns Enterprise Objects Framework would fetch if it were not using the stored procedure, and it must return them in the same order. In other words, the stored procedure should return values for primary keys, foreign keys used in class property joins, class properties, and attributes used for locking (generally, values for all the entity's attributes). Also, the stored procedure should return the values in alphabetical order based on the names of their corresponding EOAttribute objects. For example, a Studio entity has the attributes __studioId__, __name__, and __budget__. A stored procedure that fetches all the Studio objects should return the value for a studio's budget value, then the studio's name, and then its studioId.
If an FetchAllProcedureOperation stored procedure has a return value, Enterprise Objects Framework ignores it.
FetchWithPrimaryKeyProcedureOperation
The FetchWithPrimaryKeyProcedureOperation (EOFetchWithPrimaryKeyProcedureOperation in Objective-C) fetches a single enterprise object by its primary key value. A stored procedure for this operation should take an "in" argument for each of the entity's primary key attributes. The argument names must match the names of the primary key attributes. For example, a Studio entity has one primary key attribute named "studioId". As defined in a model, the stored procedure's argument must also be named "studioId".
An FetchWithPrimaryKeyProcedureOperation stored procedure should return a result set (or in the case of Oracle, a REFCURSOR argument) containing the matching row. The row must be in the same form as those returned by an FetchAllProcedureOperation stored procedure.
If an FetchWithPrimaryKeyProcedureOperation stored procedure has a return value, Enterprise Objects Framework ignores it.
InsertProcedureOperation
The InsertProcedureOperation (EOInsertProcedureOperation in Objective-C) inserts a new enterprise object. A stored procedure for this operation should take "in" arguments for each of the corresponding entity's attributes. The argument names must match the names of the corresponding EOAttribute objects.
An InsertProcedureOperation stored procedure should not return a result set. Also, if an InsertProcedureOperation stored procedure has a return value, Enterprise Objects Framework ignores it.
DeleteProcedureOperation
The DeleteProcedureOperation (EODeleteProcedureOperation in Objective-C) deletes a single enterprise object by its primary key value. A stored procedure for this operation should take an "in" argument for each of the entity's primary key attributes. The argument names must match the names of the primary key attributes as in FetchWithPrimaryKeyProcedureOperation stored procedures.
An DeleteProcedureOperation stored procedure should not return a result set. Also, if an DeleteProcedureOperation stored procedure has a return value, Enterprise Objects Framework ignores it.
NextPrimaryKeyProcedureOperation
The NextPrimaryKeyProcedureOperation (EONextPrimaryKeyProcedureOperation in Objective-C) generates a unique primary key value for a new enterprise object. A stored procedure for this operation should take an "out" argument for each of the entity's primary key attributes. The argument names must match the names of the primary key attributes as in FetchWithPrimaryKeyProcedureOperation stored procedures.
An NextPrimaryKeyProcedureOperation stored procedure should not return a result set. Also, if an NextPrimaryKeyProcedureOperation stored procedure has a return value, Enterprise Objects Framework ignores it.

## Invoking a Stored Procedure Explicitly

Some stored procedures can't be associated with a specific database operation that Enterprise Objects Framework invokes. For example, if you've defined a stored procedure to return the sum of revenues for all the Movie objects, you'll have to invoke it explicitly. To invoke a stored procedure explicitly, you use an EOAdaptorChannel object. The following code excerpt shows how to do it:
In Java:

```
EOAdaptorChannel adChannel;      // Assume this exists.
EOStoredProcedure sumOfRevenue;
NSDictionary results;
EOModelGroup defaultGroup = EOModelGroup.defaultGroup();

sumOfRevenue =
defaultGroup.storedProcedureNamed("sumOfRevenue");
adChannel.executeStoredProcedure(sumOfRevenue, null);
results =

adChannel.returnValuesForLastStoredProcedureInvocation()
;
```


In Objective-C:

```
EOAdaptorChannel *adChannel;      // Assume this exists.
EOStoredProcedure *sumOfRevenue;
NSDictionary *results;

sumOfRevenue = [[EOModelGroup defaultGroup]
        storedProcedureNamed:@"sumOfRevenue"];
[adChannel executeStoredProcedure:sumOfRevenue
withValues:nil];
results =
        [adChannel
returnValuesForLastStoredProcedureInvocation];
```


The method __returnValuesForLastStoredProcedureInvocation__ returns stored procedure parameter and return values. The dictionary returned by this method (__results__ in this example) has entries whose keys are the names of the stored procedure's out and in-out arguments. The dictionary may also contain an entry with the key "returnValue" whose value is the return value of a stored procedure (if it has one).
Tip: If you're using Sybase, the return values dictionary always contains a "SybaseStoredProcedureReturnStatus" key whose value is the return status of the stored procedure. You don't need to declare an output parameter for this.
Tip: If you're using Oracle, you can define a stored procedure to represent a function. Add an argument named "returnValue" and use the EOAdaptorChannel method __returnValuesForLastStoredProcedureInvocation__ to get the function's result.
If you want to invoke a stored procedure that returns rows, you use __fetchRow__ (__fetchRowWithZone:__ in Objective-C) as you would if you were fetching the results of a __selectAttributes__ message (__selectAttributes:fetchSpecification:lock:entity:__ in Objective-C). For example, the following code excerpts fetch Movie objects using the __fetchMovies__ stored procedure:
In Java:

```
EOAdaptorChannel adChannel;      // Assume this exists.
EOStoredProcedure fetchMovies;
NSDictionary row;
EOModelGroup defaultGroup = EOModelGroup.defaultGroup();

fetchMovies =
defaultGroup.storedProcedureNamed("fetchMovies");
adChannel.executeStoredProcedure(fetchMovies, null);

while (adChannel.isFetchInProgress()) {
    while (row = adChannel.fetchRow()) {
        // Process theRow.
    }
}
```


In Objective-C:

```
EOAdaptorChannel *adChannel;      // Assume this exists.
EOStoredProcedure *fetchMovies;
NSDictionary *row;

fetchMovies = [[EOModelGroup defaultGroup]
        storedProcedureNamed:@"fetchMovies"];
[adChannel executeStoredProcedure:fetchMovies
withValues:nil];

while ([adChannel isFetchInProgress]) {
    while (row = [adChannel fetchRowWithZone:nil]) {
        /* Process theRow. */
    }
}
```


Neither of the previous examples uses stored procedures that have arguments. If you want to invoke a stored procedure that does, you provide the argument values to the stored procedure in the __executeStoredProcedure__ message (__executeStoredProcedure:withValues:__ in Objective-C). For example, the following code excerpts use a stored procedure to insert a row into the database:
In Java:

```
EOAdaptorChannel adChannel;  // Assume this exists.
EOStoredProcedure insert;
NSDictionary row;
EOModelGroup defaultGroup = EOModelGroup.defaultGroup();

// Assume row contains the values for the row to insert

insert = defaultGroup.storedProcedureNamed("insert");
adChannel.executeStoredProcedure(insert, row);
```


In Objective-C:

```
EOAdaptorChannel *adChannel;  // Assume this exists.
EOStoredProcedure *insert;
NSDictionary *row;

// Assume row contains the values for the row to insert.

insert = [[EOModelGroup defaultGroup]
        storedProcedureNamed:@"insertTest"];
[adChannel executeStoredProcedure:insert
withValues:row];
```


__Note:__  The EOAdaptorChannel must be open for this code to work.
For more information on invoking stored procedures explicitly, see the EOAdaptorChannel class specification in the _Enterprise Objects Framework Reference_.

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Next Section](How%20Do%20I%20Order%20Database%20Operations.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
