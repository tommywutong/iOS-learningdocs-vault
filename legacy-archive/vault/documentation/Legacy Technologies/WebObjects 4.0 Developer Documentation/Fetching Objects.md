---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/BehindSc1.html
archived_at: '2026-07-18T01:19:19.905715Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Behind%20the%20Scenes.md) [!Previous Section](Behind%20the%20Scenes.md)

# Fetching Objects

This section describes the sequence of events that occurs when objects are fetched from the database. It's broken down into the following major sections:

- ["EODisplayGroup Receives a fetch Message"](#apple-giyds)
- ["Inside EODatabaseContext"](#apple-ha2dqma)
- ["Inside EODatabaseChannel"](#apple-gyzdomy)

[Figure 47](#apple-gi3dc) provides a high-level view of what happens in Enterprise Objects Framework when you fetch an object.

!

Figure 47. What Happens During a Fetch

__Note:__  [Figure 47](#apple-gi3dc) is intended to show the flow of data, not the Enterprise Objects Framework architecture as such. For a graphical depiction of the Enterprise Objects Framework architecture, see the chapter["What Is Enterprise Objects Framework?"](What%20Is%20Enterprise%20Objects%20Framework.md#apple-gu3dcma)

The steps illustrated in [Figure 47](#apple-gi3dc) are described in detail in the following sections.

## EODisplayGroup Receives a fetch Message

A fetch most often begins with an EODisplayGroup receiving a __fetch__ message. If you've configured the display group to "fetch on load," the fetch occurs at the end of display group initialization.
When a display group receives a __fetch__ message, the following sequence of events occurs:

- The display group sends its EODataSource a __fetchObjects__ message, which for the EODatabaseDataSource subclass results in a fetch against a specific EOEntity.
- The EODatabaseDataSource constructs an EOFetchSpecification for the database data source's EOEntity (if a fetch specification doesn't already exist) and passes the specification to its EOEditingContext in an __objectsWithFetchSpecification__ message (__objectsWithFetchSpecification:__ in Objective-C).

The database data source would already have a fetch specification if you assigned one programmatically or if you assigned one in Interface Builder (or WebObjects Builder in a WebObjects application). Fetch specifications are handled differently depending on how they're configured. This discussion assumes that the fetch specification is a "regular" fetch specification-one that isn't configured to fetch raw rows, to use a custom SQL statement, or to use a stored procedure.

- The receiving editing context forwards this request, in the form of a __objectsWithFetchSpecification__ message(__objectsWithFetchSpecification:editingContext:__ in Objective-C), to its parent object store, eventually reaching the root object store (which is usually an EOObjectStoreCoordinator). An EOObjectStoreCoordinator manages one or more EODatabaseContexts or other EOCooperatingObjectStores.
- The EOObjectStoreCoordinator determines which of its EOCooperatingObjectStores should service the fetch specification and forwards the EOCooperatingObjectStore an __objectsWithFetchSpecification__ message(__objectsWithFetchSpecification:editingContext:__ in Objective-C) to ask it to actually retrieve data from the database.

__Note:__  A fetch operation is always performed with an editing context, which holds all of the objects it fetches (an editing context usually performs multiple fetches over the course of an application). Objects are kept unique within an editing context, so if an enterprise object instance already exists for a fetched row, that object is simply returned as the fetched object (possibly with updated values, as described below). Any faults created for fetched objects likewise belong to the editing context and are kept unique within it.

## Inside EODatabaseContext

When an EODatabaseContext receives a fetch request in the form of an __objectsWithFetchSpecification__ message(__objectsWithFetchSpecification:editingContext:__ in Objective-C), it fetches a number of rows from the database, transforms them into enterprise objects, and registers them as needed with the EOEditingContext that received the initial __objectsWithFetchSpecification__ message.
To do this it uses an EODatabaseChannel, whose job is specifically to fetch enterprise objects. The database channel in turn uses an EOAdaptorChannel for low-level communication with the database, along with whatever model objects-EOEntities, EOAttributes, and EORelationships-are needed to perform the fetch.
Fetching objects happens in two major steps:

- The database context uses the database channel to select the rows in the database for which objects are being fetched. To do this, it uses the EODatabaseChannel __selectObjectsWithFetchSpecification__ method(__selectObjectsWithFetchSpecification:editingContext:__ in Objective-C), passing in the fetch specification. Minimally, the fetch specification identifies the EOEntity for the objects, which in turn specifies the enterprise object class to instantiate for every object fetched. If you provided the fetch specification that's used, it can also contain a qualifier that restricts the objects to fetch to those that meet specified criteria and a sort ordering with which to sort the objects. The section["Inside EODatabaseChannel"](#apple-gyzdomy)" describes in detail how the fetch specification is handled.
- The database channel fetches each enterprise object, one at a time, as the database context repeatedly sends it the message __fetchObject__. This method uses state built up in the select step to get data for the object, create an instance if necessary, and register the new object with the editing context.

### Customizing Framework Behavior

At this stage in the fetching process, there are several ways you can customize the Framework's default behavior. To get fine-grained control over a database context, you can assign a delegate to it and implement any of the following methods.

|  EODatabaseContext Delegate Methods |  EODatabaseContext Delegate Methods |  EODatabaseContext Delegate Methods |
|  Java Method |  Objective-C Method |  Description |
|  databaseContext ShouldSelectObjects |  databaseContext: shouldSelectObjects WithFetchSpecification: databaseChannel: |  This method is invoked right before a SELECT occurs. You can return __false__ (NO) to tell the channel to skip the SELECT and return; you might want to do this to issue your own custom SQL against the adaptor. |
|  databaseContext ShouldUsePessimisticLock |  databaseContext: shouldUsePessimisticLock WithFetchSpecification: databaseChannel: |  You can use this delegate method to selectively turn off the locking of rows when you're using a pessimistic locking strategy. |
|  databaseContext DidSelectObjects |  databaseContext: didSelectObjects WithFetchSpecification: databaseChannel: |  This method is invoked immediately after a SELECT occurs. You can use it to log diagnostic information or set up internal state for the coming fetch. |
|  databaseContext ShouldFetchObjects |  databaseContext: shouldFetchObjects WithFetchSpecification: editingContext: |  You can use this method to satisfy the EOEditingContext's fetch request from a local cache. |
|  databaseContext DidFetchObjects |  databaseContext: didFetchObjects: fetchSpecification: editingContext: |  This method is invoked after an EODatabaseContext fetches objects. You can use this method to record in a local cache the results of a fetch. |

```
```


With respect to locking, note that in addition to setting an overall locking strategy, you can take advantage of EODatabaseContext's "on demand" locking feature to lock individual rows. For more information, see["Locking and Update Strategies"](Saving%20Changes.md#apple-g4ytmnq).

An EODatabaseContext also posts notifications that your objects can receive and react to.

|  EODatabaseContext Notifications |  EODatabaseContext Notifications |
|  Notification |  Description |
|  DatabaseChannelNeededNotification (EODatabaseChannelNeededNotification in Objective-C) |  This notification is broadcast whenever an EODatabaseContext is asked to perform an object store operation and it doesn't have an available EODatabaseChannel. Subscribers can create a new channel and add it to the EODatabaseContext at this time. |

```
```


## Inside EODatabaseChannel

In __fetchObject__, an EODatabaseChannel performs several tasks:

- Before anything else can be done, the EODatabaseChannel must read some data from the database. It does so by having its EOAdaptorChannel retrieve a record for the EOEntity being fetched, including the primary key, class properties, attributes used for locking, and any foreign keys used by EORelationships.
- The first thing the database channel does with the fetched record is to get an EOGlobalID for it from the EOEntity by invoking __globalIDForRow__ (__globalIDForRow:__ in Objective-C).
- The EODatabaseChannel records a snapshot for the fetched row. This step can be fairly complicated, as there may already be a snapshot recorded under the globalID. If there isn't, the EODatabase object is simply sent a __recordSnapshotForGlobalID__ message (__recordSnapshot:forGlobalID:__ in Objective-C). If there is a snapshot, however, a decision must be made on how to update the recorded snapshot. You can use the EODatabaseContext delegate method __databaseContextShouldUpdateCurrentSnapshot__ to intervene at this point(in Objective-C, __databaseContext: shouldUpdateCurrentSnapshot:newSnapshot:globalID: databaseChannel:__).

If the fetch specification is set to refresh refetched objects, an ObjectsChangedInStoreNotification (EOObjectsChangedInStoreNotification in Objective-C) is posted to invalidate (refault) any existing instances corresponding to this globalID.

- The database channel records whether the object was locked when it was selected.
- The database channel then checks with the editing context, using __objectForGlobalID__ (__objectForGlobalID:__ in Objective-C), to see whether a copy of the object already exists in that context.
- If the editing context already has an enterprise object for the global ID-and if it isn't a fault-then it's simply returned; otherwise it returns __null__ (__nil__ in Objective-C).
- If the editing context has no object or fault for the globalID, the database channel invokes the EOEntityClassDescription method __createInstanceWithEditingContext__ (__createInstanceWithEditingContext:globalID:zone:__ in Objective-C).This method finds out what the object's class should be from the EOEntity and creates an object of that class.

The __createInstanceWithEditingContext__ method provides the enterprise object class's constructor with an editing context, the entity class description, and a globalID. You'll rarely need to use this information at this point, but you might choose to if, for example, you need to extract the primary key from the globalID to do some processing on it.

Note that in Objective-C, the entity class description creates objects and initializes them with the method __initWithEditingContext:classDescription:globalID:__, if it exists (it uses __init__ otherwise). Your enterprise object class can implement __initWithEditingContext:classDescription:globalID:__ instead of simply __init__ if you need to do anything with the object's editing context, class description, or globalID at this stage in the process.

- The database channel invokes the editing context's __recordObject__ method (__recordObject:globalID:__ in Objective-C), in which the newly created object gets uniqued.
- If the editing context has a fault for the globalID, the fault is cleared and initialization proceeds just as if an empty enterprise object had been created and registered.
- To initialize the object, database channel sends the editing context an __initializeObject__ message (__initializeObject:withGlobalID:editingContext:__ in Objective-C), which is passed down the object store hierarchy. If the editing context is nested, it passes the message to its parent EOEditingContext. If the parent EOEditingContext has an object with a matching globalID, that object is used to initialize the child object. Otherwise, the message is passed down to the EODatabaseContext, which initializes the new instance from the appropriate snapshot and creates faults for its relationships. The EODatabaseContext's __initializeObject__ method sets the object's properties using the key-value coding method __takeStoredValueForKey__ (__takeStoredValue:forKey:__ in Objective-C).
- The database channel sends the enterprise object an __awakeFromFetch__ message (__awakeFromFetchInEditingContext:__ in Objective-C). Custom enterprise object classes can override this method to perform additional initialization after an object has been created from a database row and initialized from database values.

Your custom enterprise object classes can also implement the method __awakeFromInsertion__ (__awakeFromInsertionInEditingContext:__ in Objective-C), which is invoked immediately after your application creates a new object and inserts it into an EOEditingContext. This method lets you assign values to newly created enterprise objects. For more discussion of this topic, see the chapter["Designing Enterprise Objects"](Designing%20Enterprise%20Objects.md#apple-ge2daobr).

### Customizing Framework Behavior

At this stage in the fetching process, you can intervene during step 5 above by assigning a delegate to the EODatabaseContext and implementing any of the following methods.

|  Java Method |  Objective-C Method |  Description |
|  databaseContext FailedToFetchObject |  databaseContext: failedToFetchObject: globalID: |  This method is invoked when a to-one fault can't find its data in the database. This often occurs due to referential integrity problems in the database. You can use this method to intervene and take appropriate action (for example, by displaying an alert panel or initializing a fault object with new values). |
|  databaseContext ShouldLockObject WithGlobalID |  databaseContext: shouldLockObject WithGlobalID: snapshot: |  This method is invoked from lockObjectWithGlobalID:editingContext:. You can use this method to implement your own locking procedure. |
|  databaseContext ShouldRaiseException ForLockFailure |  databaseContext: shouldRaiseException ForLockFailure: |  You can use this method to suppress an exception that occurred during an EODatabaseContext's attempt to lock an object. |
|  databaseContext ShouldUpdate CurrentSnapshot |  databaseContext: shouldUpdate CurrentSnapshot: newSnapshot: globalID: databaseChannel: |  This method is invoked when an EODatabaseContext already has a snapshot for a row fetched from the database. You can use this method to compare the snapshots, possibly resolve conflicts, and instruct the EODatabaseContext to use the new snapshot instead of the existing one. |

```
```


## Flow of Data During a Fetch

The preceding sections describe what happens in Enterprise Objects Framework when you fetch objects from the database. This section describes the flow of data that occurs during a fetch.
[Figure 48](#apple-gqytg) shows how a new object gets instantiated with database data. The scenario it depicts is fetching a single, new object from the database.

!

Figure 48. Flow of Data During a Fetch

This process is described in greater detail below.
The following sequence of events occurs when an object is fetched from the database:

- A database row is fetched as raw binary data.
- The values retrieved from the database are converted from their database-specific types to instances of standard value classes:

  |  Java Class |  Objective-C Class |  Type of Data |
  |  String |  NSString |  character strings |
  |  NSGregorianDate |  NSCalendarDate |  dates and times |
  |  Number or BigDecimal (java.math) |  NSNumber or NSDecimalNumber |  numbers |
  |  NSData |  NSData |  arbitrary binary data (BLOBs) |

```
```


NULL values in the database are mapped to instances of EONullValue (EONull in Objective-C).

Additionally, you can map external data types to custom value classes defined by your application. For more discussion of this subject, see the chapter["Advanced Enterprise Object Modeling"](Advanced%20Enterprise%20Object%20Modeling.md#apple-ge2danbw).

- Once the data has been converted to objects, these objects are put in an NSDictionary. The elements of the dictionary correspond to columns (attributes) in the database table: Their names are the names of the attributes as used by the client application, and their values are the values in the database. The EOModel is used to determine the mapping from external (database) data types to internal (Objective-C) types.

The dictionary provides a snapshot of the database row, and it's later used to initialize the enterprise object. The snapshot also comes into play when changes to the object are saved to the database; for more discussion of this topic see the section["Snapshots"](#apple-gi2tm).

The EOModel, which is used to convert database data to objects, is also used when a newly allocated enterprise object is initialized. Whereas the dictionary contains an entry for each of the row's columns (those returned by sending __attributesToFetch__ to an EOEntity), the enterprise object initialized from the dictionary only contains the attributes that are defined in the EOModel as class properties.

- A new enterprise object is allocated by EOEntityClassDescription as an object of the Employee class, as determined from the EOModel.
- The enterprise object is initialized from a row snapshot, using the EOModel. Only objects that are class properties are included.

When an enterprise object is initialized, EONullValue objects (or EONull objects in Objective-C) are passed to the object as __null__ (__nil__ in Objective-C) so you don't have to write code to handle NULLs.

Also, relationship references are initialized for any relationship properties defined in the EOModel. For example, an Employee object might have a reference to the employee's department, which in database terms represents a join between the EMPLOYEE and DEPARTMENT tables. Class properties that are relationships are represented in the object graph as faults until they're accessed.

## Uniquing, Snapshots, and Faults

When you fetch objects in an Enterprise Objects Framework application, the Framework has mechanisms for ensuring that the integrity of the fetched data is maintained. To this end, the Framework implements these features:

- Uniquing

Enterprise Objects Framework maintains the mapping of each enterprise object to its corresponding database row, and uses this information to ensure that your object graph does not have two (possibly inconsistent) objects for the same database row.

- Snapshots

When objects are fetched, Enterprise Objects Framework records the state of the corresponding database row. This information is used when changes are saved back out to the database to ensure that the row data has not been changed by someone else since it was last fetched. The information is also used to only update attributes that have changed, rather than all of them.

- Faults

The objects at the destination of a fetched object's relationships are only fetched on demand; however, these objects are represented in your application by stand-in objects called _faults_ to make retrieval of the actual objects easier.

These topics are discussed in more detail in the following sections.

### Uniquing

In marrying relational databases to object-oriented programming, one of the key requirements is that a row in the database be associated with only one enterprise object in a given context in your application. Uniquing of enterprise objects limits memory usage and allows you to know with confidence that the object you're interacting with represents the true state of its associated row as it was last fetched into the object graph.
Without uniquing, you'd get a new enterprise object every time you fetch its corresponding row, whether explicitly or through resolution of relationships. This is illustrated in [Figure 49](#apple-g4zds).

!

Figure 49. Uniquing of Enterprise Objects

Uniquing occurs in the control layer, and it's based on an object's globalID. A globalID consists of an object's primary key and its associated entity. When a row is fetched to create an object in a particular EOEditingContext, its globalID is checked against the objects already in the EOEditingContext. If a match is found, the newly fetched object isn't added to the context.
A single enterprise object instance exists in one and only one EOEditingContext, but multiple copies of an object can exist in different editing contexts. In other words, object uniquing is scoped to a particular editing context.

### Snapshots

When an EODatabaseContext fetches objects from the database, it asks its EODatabase to record a _snapshot_ of the state of the corresponding database row.
A snapshot is a dictionary object recording a row's primary key, class properties, foreign keys for class property relationships, and the attributes of that object that are used for locking during an update. (Primary keys and attributes used for locking are defined in a model; see the book _Enterprise Objects Framework Tools and Techniques_.) A snapshot is recorded under the globalID of its enterprise object whenever the object is fetched or modified.
When changes to an object are saved to the database, the snapshot is compared with the corresponding database row to ensure that the row data hasn't changed since the object was last fetched. For a discussion of how this relates to the update strategy you set for your application, see the section ["Locking and Update Strategies"](Saving%20Changes.md#apple-g4ytmnq).

For more information on snapshots, see the EODatabaseContext class specification in the _Enterprise Objects Framework Reference_.

### Faults

One of the most powerful and useful features of the Framework's database level is that it automatically resolves the relationships defined in a model. It does so by delaying the actual retrieval of data-and communication with the database-until the data is needed. This delayed resolution of relationships occurs in two stages: the creation of a placeholder object for the data to be fetched, and the fetching of that data only when it's needed.
When the database level fetches an object, it examines the relationships defined in the model and creates objects representing the destinations of the fetched object's relationships. For example, if you fetch an employee object, you can ask for its manager and immediately receive an object; you don't have to get the manager's employee ID from the object you just fetched and fetch the manager yourself.
The database level doesn't immediately fetch data for the destination objects of relationships, however. Fetching is fairly expensive, and further, if the database level fetched objects related to the one explicitly asked for, it would also have to fetch the objects related to those, and so on, until all of the interrelated rows in the database had been retrieved. To avoid this waste of time and resources, the destination objects created are stand-ins, or _faults_.
Faults come in two varieties: single-object faults for to-one relationships, and array faults for to-many relationships. In Java, a single-object fault is merely a partially initialized enterprise object. It's been created with a constructor of the form:

```
public MyCustomEO (
    EOEditingContext  anEOEditingContext,
    EOClassDescription  anEOClassDescription,
    EOGlobalID  anEOGlobalID)
```


and so is already associated with a particular editing context, a class description, and a globalID. However, the object's data hasn't yet been fetched from the database. This part of the object's initialization is delayed until the object receives a message which requires it to fetch its data.
In Objective-C on the other hand, single-object faults are objects of a special class (EOFault) whose instances transform themselves into actual enterprise objects-and fetch their data-the first time they're accessed. These Objective-C faults occupies the same amount of memory as an instance of the target class (into which it's eventually transformed), and stores the information needed to retrieve the data associated with the fault (the source globalID and relationship name). A fault object thus consumes about as much memory as an empty instance of its target class.
An Objective-C fault behaves in every way possible as an instance of its target class until it receives a message it can't cover for. For example, if you fetch an Employee object and ask for its manager, you get a fault object representing another Employee object. If you send a __class__ message to this fault object, it returns the Employee class. If you send the fault object a message requesting the value of an attribute, such as __lastName__, however, it uses the EODatabaseContext that created it to retrieve its data from the database, overwrites its class identity, and invokes the target class's implementation of __lastName__.
[Figure 50](#apple-gmytkma) illustrates this process.

!

Figure 50. Resolution of a Fault Object

Array faults are treated similarly by both languages. They behave as instances of the NSMutableArray class, and are triggered to fetch their objects by any request for a member object or for the number of objects in the array (the number of objects for a to-many relationship can't be determined without actually fetching them all).
For more information on faults, see the EOFaulting interface specification (Java only), the EOFault class specification (Objective-C only), and the EOFaultHandler class specification (or both languages) in the _Enterprise Objects Framework Reference_.
Uniquing and Faults
When an EODatabaseChannel constructs a fault for a to-one relationship, it checks the globalID for the destination to see whether that object already exists in the EOEditingContext. If so, it simply uses that object to immediately resolve the relationship. This preserves the uniqueness requirement for enterprise objects, in that there's never more than one __globalID__ representing the same row in the database. Whether that __globalID__ represents an actual enterprise object or a fault doesn't matter, since the data will be fetched when it's needed.
Similarly, if an EODatabaseChannel fetches data for an object that's already been created as a fault, the EODatabaseChannel _fires_ the fault. In Java, this simply means that it finishes initializing the object with the data it's fetched. In Objective-C, this means that the database channel turns the fault into an instance of its target class, _without changing its id_, and then initializes the resulting enterprise object. In either case, the process is essentially the same whether you fetch the fault's data or whether the fault fetches the data itself upon being sent a message.

[!Table of Contents](Behind%20the%20Scenes.md) [!Next Section](How%20Changes%20are%20Distributed%20and%20Applied.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
