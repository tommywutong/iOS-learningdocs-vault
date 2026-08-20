---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAdaptorChannel.html
archived_at: '2026-07-18T01:28:15.431499Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SubclassingEOAdaptor-2.md)
[!](SubclassingEOAdaptorChnnl-2.md)

---

# EOAdaptorChannel

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EOAdaptorChannel.h

---

## Class Description

EOAdaptorChannel is an abstract class that provides its concrete subclasses with a structure for performing database operations. It's associated with EOAdaptor and EOAdaptorContext, which, together with EOAdaptorChannel, form the _adaptor level_ of Enterprise Objects Framework's access layer. See the EOAdaptor class specification for more information about accessing, creating, and using adaptor level objects.

A concrete subclass of EOAdaptorChannel provides database-specific method implementations and represents an independent communication channel to the database server to which its EOAdaptor object is connected. You never interact with instances of the EOAdaptorChannel class, rather your Enterprise Objects Framework applications use instances of concrete subclasses that are written to interact with a specific database or other persistent storage system. To create an instance of a concrete EOAdaptorChannel subclass, you send a __createAdaptorChannel__  message to an instance of the corresponding EOAdaptorContext subclass. You rarely create adaptor channels yourself. They are generally created automatically by other framework objects.

You use an adaptor channel to manipulate rows (records) by selecting, fetching, inserting, deleting, and updating them. An adaptor channel also gives you access to some of the metadata on the server, such as what stored procedures exist, what tables exist, and what their basic attributes and relationships are.

All of an adaptor channel's operations take place within the context of transactions controlled or tracked by its EOAdaptorContext. An adaptor context may manage several channels (though not all can), but a channel is associated with only one context.

---

## Notifying the Adaptor Channel's Delegate

You can assign a delegate to an adaptor channel. The EOAdaptorChannel sends certain messages directly to the delegate, and the delegate responds to these messages on the channel's behalf. Many of the adaptor channel methods notify the channel's delegate before and after an operation is performed. Some delegate methods, such as [`adaptorChannel:shouldEvaluateExpression:`](../Protocols/EOAdaptorChannelDelegate.md#apple-geytioa), let the delegate determine whether the channel should perform an operation. Others, such as [`adaptorChannel:didEvaluateExpression:`](../Protocols/EOAdaptorChannelDelegate.md#apple-geyteny), are simply notifications that an operation has occurred. The delegate has an opportunity to respond by implementing the delegate methods. If the delegate wants to intervene, it implements `adaptorChannel:shouldEvaluateExpression:`. If it simply wants notification when a transaction has begun, it implements `adaptorChannel:didEvaluateExpression:`.

The principal attributes of the EOAdaptorChannel class are:

- Adaptor context
- Delegate

Other framework classes create EOAdaptorChannel objects, using EOAdaptorContext's [`createAdaptorChannel`](EOAdaptorContext.md#apple-gm4tamq) method, which both creates an adaptor channel and assigns its context.

The following table lists EOAdaptorChannel's more commonly-used methods:

| [openChannel](#apple-geydmmq) | Opens the channel so it can perform database operations. |
| [closeChannel](#apple-guzdemq) | Close the channel. |
| [selectAttributes:fetchSpecification:lock:entity:](#apple-geydsma) | Selects rows matching the specified qualifier. |
| [fetchRowWithZone:](#apple-gyztsni) | Fetches a row resulting from the last `selectAttributes: fetchSpecification:lock:entity:`, `executeStoredProcedure:withValues:`, or `evaluateExpression:`. |
| [insertRow:forEntity:](#apple-geydgmi) | Inserts the specified row. |
| [updateValues:inRowsDescribedByQualifier:entity:](#apple-gy3dgny) | Updates the row described by the specified qualifier. |
| [deleteRowDescribedByQualifier:entity:](#apple-guzdmna) | Deletes the row described by the specified qualifier. |
| [executeStoredProcedure:withValues:](#apple-gyztona) | Performs the specified stored procedure. |
| [evaluateExpression:](#apple-geydaoi) | Sends the specified expression to the database. |

```
```

| [- openChannel](#apple-geydmmq) | Opens the channel so it can perform database operations. |
| [- closeChannel](#apple-guzdemq) | Close the channel. |
| [- selectAttributes:fetchSpecification:lock:entity:](#apple-geydsma) | Selects rows matching the specified qualifier. |
| [- fetchRowWithZone:](#apple-gyztsni) | Fetches a row resulting from the last `select...`, `executeStoredProcedure...`, or `evaluateExpression:`. |
| [- insertRow:forEntity:](#apple-geydgmi) | Inserts the specified row. |
| [- updateValues:inRowDescribedByQualifier:entity:](#apple-geytcmi) | Updates the row described by the specified qualifier. |
| [- deleteRowDescribedByQualifier:entity:](#apple-guzdmna) | Deletes the row described by the specified qualifier. |
| [- executeStoredProcedure:withValues:](#apple-gyztona) | Performs the specified stored procedure. |
| [- evaluateExpression:](#apple-geydaoi) | Sends the specified expression to the database. |
| [- performAdaptorOperation:](#apple-geydmnq) | Performs an adaptor operation by invoking the EOAdaptorChannel method appropriate for performing the specified operation. |

```
```

For more information on subclassing EOAdaptorChannel, see ["Creating an EOAdaptorChannel Subclass"](SubclassingEOAdaptorChnnl-2.md#apple-gm2tgmy).

---

## Method Types

**Accessing the adaptor context**

**[- adaptorContext](#apple-gq3dqni)**

**Opening and closing a channel**

**[- openChannel](#apple-geydmmq)

**[- closeChannel](#apple-guzdemq)

**[- isOpen](#apple-geydkmi)******

**Creating an EOAdaptorChannel**

**[- initWithAdaptorContext:](#apple-ge2dknzs)**

**Modifying rows**

**[- insertRow:forEntity:](#apple-geydgmi)

**[- updateValues:inRowDescribedByQualifier:entity:](#apple-geytcmi)

**[- updateValues:inRowsDescribedByQualifier:entity:](#apple-gy3dgny)

**[- deleteRowDescribedByQualifier:entity:](#apple-guzdmna)

**[- deleteRowsDescribedByQualifier:entity:](#apple-guzdsna)**********

**Fetching rows**

**[- selectAttributes:fetchSpecification:lock:entity:](#apple-geydsma)

**[- describeResults](#apple-he4tk)

**[- setAttributesToFetch:](#apple-geydsny)

**[- attributesToFetch](#apple-gq3dmmq)

**[- fetchRowWithZone:](#apple-gyztsni)

**[- dictionaryWithObjects:forAttributes:zone:](#apple-ge2dioby)

**[- cancelFetch](#apple-he3do)

**[- isFetchInProgress](#apple-geydimq)****************

**Invoking stored procedures**

**[- executeStoredProcedure:withValues:](#apple-gyztona)

**[- returnValuesForLastStoredProcedureInvocation](#apple-geydqnq)****

**Assigning primary keys**

**[- primaryKeyForNewRowWithEntity:](#apple-geydqna)**

**Sending SQL to the server**

**[- evaluateExpression:](#apple-geydaoi)**

**Batch processing operations**

**[- performAdaptorOperation:](#apple-geydmnq)

**[- performAdaptorOperations:](#apple-geydomi)****

**Accessing schema information**

**[- describeTableNames](#apple-geydamq)

**[- describeStoredProcedureNames](#apple-he4ts)

**[- addStoredProceduresNamed:toModel:](#apple-he3da)

**[- describeModelWithTableNames:](#apple-guztcnq)********

**Debugging**

**[- setDebugEnabled:](#apple-geytamq)

**[- isDebugEnabled](#apple-geydgoa)****

**Accessing the delegate**

**[- delegate](#apple-he3tm)

**[- setDelegate:](#apple-geytany)****

---

## Instance Methods

---

### adaptorContext

- (EOAdaptorContext \*)__adaptorContext__

Returns the receiver's EOAdaptorContext. A subclass of EOAdaptorChannel doesn't need to override this method.

__See also:__
[- `initWithAdaptorContext:`](#apple-ge2dknzs)

---

### addStoredProceduresNamed:toModel:

- (void)__addStoredProceduresNamed:__ (NSArray \*)_storedProcedureNames_
__toModel:__ (EOModel \*)_model_

Overridden by subclasses to create EOStoredProcedure objects for the stored procedures named in _storedProcedureNames_ and then to add them to _model_. This method is used in conjunction with ____`describeStoredProcedureNames` to build a default model in EOModeler. Raises an exception if an error occurs.

---

### attributesToFetch

- (NSArray \*)__attributesToFetch__

Implemented by subclasses to return the set of attributes to retrieve when [`fetchRowWithZone:`](#apple-gyztsni) is next invoked. An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[`setAttributesToFetch:`](#apple-geydsny)

---

### cancelFetch

- (void)__cancelFetch__

Implemented by subclasses to clear all result sets established by the last `[selectAttributes:fetchSpecification:lock:entity:](#apple-geydsma)`, [`executeStoredProcedure:withValues:`](#apple-gyztona), or [`evaluateExpression:`](#apple-geydaoi) message and terminate the current fetch, so that `isFetchInProgress` returns NO.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### closeChannel

- (void)__closeChannel__

Implemented by subclasses to close the EOAdaptorChannel so that it can't perform operations with the server. Any fetch in progress is canceled. If the receiver is the last open channel in an adaptor context and if the channel's adaptor context has outstanding transactions, closing the channel has server-dependent results: some database servers roll back all outstanding transactions but others do nothing. Regardless of whether outstanding transactions are rolled back, this method has the side effect of closing the receiver's adaptor context's connection with the database if the receiver is its adaptor context's last open channel.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `cancelFetch`](#apple-he3do), [- `transactionNestingLevel`](EOAdaptorContext.md#apple-gyzto) (EOAdaptorContext)

---

### delegate

- (id)__delegate__

Returns the receiver's delegate, or `nil` if the receiver doesn't have a delegate. A subclass of EOAdaptorChannel doesn't need to override this method.

__See also:__
[`setDelegate:`](#apple-geytany)

---

### deleteRowDescribedByQualifier:entity:

- (void)__deleteRowDescribedByQualifier:__ (EOQualifier \*)_qualifier_ __entity:__ (EOEntity \*)_entity_

Deletes the row described by _qualifier_ from the database table corresponding to _entity_. Invokes `[deleteRowsDescribedByQualifier:entity:](#apple-guzdsna)` and raises an exception unless exactly one row is deleted. A subclass of EOAdaptorChannel doesn't need to override this method.

---

### deleteRowsDescribedByQualifier:entity:

- (unsigned int)__deleteRowsDescribedByQualifier:__ (EOQualifier \*)_qualifier_ __entity:__ (EOEntity \*)_entity_

Implemented by subclasses to delete the rows described by _qualifier_ from the database table corresponding to _entity_. Returns the number of rows deleted. Raises an exception on failure. Some possible reasons for failure are:

- The adaptor channel isn't open
- The adaptor channel is in an invalid state (for example, it's fetching).
- An error occurs in the database server

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `deleteRowDescribedByQualifier:entity:`](#apple-guzdmna), [- `isOpen`](#apple-geydkmi), [- `isFetchInProgress`](#apple-geydimq),
`[- transactionNestingLevel](EOAdaptorContext.md#apple-gyzto)` (EOAdaptorContext)

---

### describeModelWithTableNames:

- (EOModel \*)__describeModelWithTableNames:__ (NSArray \*)_tableNames_

Overridden by subclasses to create and return a default model containing entities for the tables specified in _tableNames_. Assigns the adaptor name and connection dictionary to the new model. This method is typically used in conjunction with `describeTableNames` and [`describeStoredProcedureNames`](#apple-he4ts).

EOAdaptorChannel's implementation does nothing. An adaptor channel subclass should override this method to create a default model from the database's metadata.

---

### describeResults

- (NSArray \*)__describeResults__

Implemented by subclasses to return an array of EOAttributes describing the properties available in the current result set, as determined by `selectAttributes:describedByQualifier:fetchOrder:lock:`, [`executeStoredProcedure:withValues:`](#apple-gyztona), or a statement evaluated by `evaluateExpression:`. Only invoke this method if a fetch is in progress as determined by [`isFetchInProgress`](#apple-geydimq).

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### describeStoredProcedureNames

- (NSArray \*)__describeStoredProcedureNames__

Overridden by subclasses to read and return an array of stored procedure names from the database. This method is used in conjunction with __addStoredProceduresNamed:toModel:__  to build a default model in EOModeler. Raises an exception if an error occurs.

---

### describeTableNames

- (NSArray \*)__describeTableNames__

Overridden by subclasses to read and return an array of table names from the database. This method in conjunction with [`describeModelWithTableNames:`](#apple-guztcnq) is used to build a default model.

EOAdaptorChannel's implementation simply returns `nil`. An adaptor channel subclass should override this method to construct an array of table names from database metadata.

---

### dictionaryWithObjects:forAttributes:zone:

- (NSMutableDictionary \*)__dictionaryWithObjects:__ (id \*)_objects___forAttributes:__ (NSArray \*)_attributes___zone:__ (NSZone \*)_zone_

Used by EOAdaptorChannel subclasses to create dictionaries that can be returned from `[fetchRowWithZone:](#apple-gyztsni)`. You don't ordinarily invoke this method unless you are writing your own concrete adaptor. If you are writing a concrete adaptor, use of this method is optional but strongly recommended because it enables performance optimizations. The objects in _objects_ are the values for the row that correspond to the EOAttribute objects in _attributes_. The dictionary representation of the row is created from _zone_.

A subclass of EOAdaptorChannel shouldn't override this method.

---

### evaluateExpression:

- (void)__evaluateExpression:__ (EOSQLExpression \*)_expression_

Implemented by subclasses to send _expression_ to the database server for evaluation, beginning a transaction first and committing it after evaluation if a transaction isn't already in progress. Raises an exception if an error occurs. An EOAdaptorChannel uses this method to send SQL expressions to the database.

If _expression_ results in a select operation being performed, you can fetch the results as you would if you had sent a [`selectAttributes:fetchSpecification:lock:entity:`](#apple-geydsma). You must use the method [`setAttributesToFetch:`](#apple-geydsny) before you begin fetching. Also, if _expression_ evaluates to multiple result sets, you must invoke `setAttributesToFetch:` before you begin fetching each subsequent set.

`evaluateExpression:` invokes the delegate methods `[adaptorChannel:shouldEvaluateExpression:](../Protocols/EOAdaptorChannelDelegate.md#apple-geytioa)` and `[adaptorChannel:didEvaluateExpression:](../Protocols/EOAdaptorChannelDelegate.md#apple-geyteny)`.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation. Note, however, that the upper layers of the Framework never invoke [`evaluateExpression:`](#apple-geydaoi) directly. Thus, adaptors for data stores that don't naturally support an expression language (for example, flat file adaptors) don't need to implement this method to work with the Framework.

__See also:__
[- `fetchRowWithZone:`](#apple-gyztsni)

---

### executeStoredProcedure:withValues:

- (void)__executeStoredProcedure:__ (EOStoredProcedure \*)_storedProcedure___withValues:__ (NSDictionary \*)_values_

Implemented by subclasses to execute _storedProcedure_. Any arguments to the stored procedure are in _values_, a dictionary whose keys are the argument names. Use [`fetchRowWithZone:`](#apple-gyztsni) to get result rows and [`returnValuesForLastStoredProcedureInvocation`](#apple-geydqnq) to get return arguments and result status, if any. Raises an exception if an error occurs.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation. Note, however, that the upper layers of the Framework never invoke [`executeStoredProcedure:withValues:`](#apple-gyztona) directly. Thus, adaptors for data stores that don't support stored procedures (for example, flat file adaptors) don't need to implement this method to work with the Framework

---

### fetchRowWithZone:

- (NSMutableDictionary \*)__fetchRowWithZone:__ (NSZone \*)_zone_

Implemented by subclasses to fetch the next row from the result set of the last [`selectAttributes:fetchSpecification:lock:entity:`](#apple-geydsma), [`executeStoredProcedure:withValues:`](#apple-gyztona), or [`evaluateExpression:`](#apple-geydaoi) message sent to the receiver. Returns values for the receiver's [`attributesToFetch`](#apple-gq3dmmq) in a dictionary whose keys are the attribute names. When there are no more rows in the current result set, this method returns `nil`, and invokes the delegate method [`adaptorChannelDidChangeResultSet:`](../Protocols/EOAdaptorChannelDelegate.md#apple-geytena) if there are more results sets. When there are no more rows or result sets, this method returns `nil`, ends the fetch, and invokes [`adaptorChannelDidFinishFetching:`](../Protocols/EOAdaptorChannelDelegate.md#apple-geytgnq). [`isFetchInProgress`](#apple-geydimq) returns YES until the fetch is canceled or until this method exhausts all result sets and returns `nil`. This method also invoke the delegate methods [`adaptorChannelWillFetchRow:`](../Protocols/EOAdaptorChannelDelegate.md#apple-geytmma) and [`adaptorChannel:didFetchRow:`](../Protocols/EOAdaptorChannelDelegate.md#apple-geytgmy). Raises an exception if an error occurs.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `setAttributesToFetch:`](#apple-geydsny)

---

### initWithAdaptorContext:

- __initWithAdaptorContext:__ (EOAdaptorContext \*)_adaptorContext_

The designated initializer for the EOAdaptorChannel class, this method is overridden by subclasses to initialize a newly allocated EOAdaptorChannel subclass and retain _adaptorContext_. Returns `self`.

You never invoke this method directly unless you are implementing a concrete adaptor context. It is invoked automatically from `[createAdaptorChannel](EOAdaptorContext.md#apple-gm4tamq)-`the EOAdaptorContext method you use to create a new adaptor channel.

A subclass of EOAdaptorChannel doesn't need to override this method, but may override it to perform additional initialization. A subclass that does override this method must incorporate the superclass's version through a message to `super`.

__See also:__
[- `adaptorContext`](#apple-gq3dqni)

---

### insertRow:forEntity:

- (void)__insertRow:__ (NSDictionary \*)_row_ __forEntity:__ (EOEntity \*)_entity_

Implemented by subclasses to insert the values of _row_ into the table in the database that corresponds to _entity_. _row_ is a dictionary whose keys are attribute names and whose values are the values to insert. Raises an exception on failure. Some possible reasons for failure are:

- The user logged in to the database doesn't have permission to insert a new row.
- The adaptor channel is in an invalid state (for example, fetching).
- The row fails to satisfy a constraint defined in the database server.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### isDebugEnabled

- (BOOL)__isDebugEnabled__

Returns YES if the adaptor channel logs evaluated SQL and other useful information to the console (or to the standard error stream), NO if not. A subclass of EOAdaptorChannel doesn't need to override this method.

__See also:__
[- `setDebugEnabled:`](#apple-geytamq), [- `setDebugEnabled:`](EOAdaptorContext.md#apple-gyzda) (EOAdaptorContext)

---

### isFetchInProgress

- (BOOL)__isFetchInProgress__

Implemented by subclasses to return YES if the receiver is fetching, NO otherwise. An adaptor channel is fetching if:

- It's been sent a successful `selectAttributes:describedByQualifier:fetchOrder:lock:` message.
- A stored procedure that returns rows has been successfully executed using [`executeStoredProcedure:withValues:`](#apple-gyztona).
- An expression sent through `evaluateExpression:` resulted in a select operation being performed.

An adaptor channel stops fetching when there are no more records to fetch or when it's sent a `cancelFetch` message.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `fetchRowWithZone:`](#apple-gyztsni)

---

### isOpen

- (BOOL)__isOpen__

Implemented by subclasses to return YES if the channel has been opened with `openChannel`, NO if not. An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `closeChannel`](#apple-guzdemq)

---

### lockRowComparingAttributes:entity:qualifier:snapshot:

- (void)`lockRowComparingAttributes:`(NSArray \*)_attributes_`entity:`(EOEntity \*)_entity_`qualifier:`(EOQualifier \*)_qualifier_`snapshot:`(NSDictionary \*)_snapshot_

Attempts to lock a row in the database by selecting it with locking on. The lock operation succeeds if a select statement generated with _qualifier_ retrieves exactly one row and the values in the row match the values in _snapshot_, a dictionary whose keys are attribute names and whose values are the values that were last fetched from the database.

`lockRowComparingAttributes:entity:qualifier:snapshot:` invokes [`selectAttributes:fetchSpecification:lock:entity:`](#apple-geydsma) with _attributes_ as the attributes to select, a fetch specification built from _qualifier_, locking on, and _entity_ as the entity. If the select returns no rows or more than one row, the method raises an EOGeneralAdaptorException. It also raises an EOGeneralAdaptorException if the values in the returned row don't match the corresponding values in _snapshot_.

The Framework uses this method whenever it needs to lock a row. When the Framework invokes it, _qualifier_ specifies the primary key of the row to be locked and attributes used for locking to be compared in the database server. If any of the values specified in _qualifier_ are different from the values in the database row, the select operation will not retrieve or lock the row. When this happens, the row to be locked has been updated in the database since it was last retrieved, and it isn't safe to update it.

Some attributes (such as BLOB types) can't be compared in the database. _attributes_ should specify any such attributes. (If the row doesn't contain any such attributes, _attributes_ can be `nil`.) If _qualifier_ generates a select statement that returns and locks a single row, this method performs an in-memory comparison between the value in the retrieved row and the value in _snapshot_ for each attribute in _attributes_. Therefore, _snapshot_ must contain an entry for each attribute in _attributes_. In addition, it must contain an entry for the row's primary key.

A subclass of EOAdaptorChannel doesnt need to override this method.

---

### openChannel

- (void)__openChannel__

Implemented by subclasses to put the channel and both its context and adaptor into a state where they are ready to perform database operations. Raises an exception if an error occurs. An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `isOpen`](#apple-geydkmi), [- `closeChannel`](#apple-guzdemq)

---

### performAdaptorOperation:

- (void)__performAdaptorOperation:__ (EOAdaptorOperation \*)_adaptorOperation_

Performs _adaptorOperation_ by invoking the adaptor channel method appropriate for performing the specified operation. For example, if the adaptor operator for _adaptorOperation_ is EOAdaptorInsertOperator, this method invokes [`insertRow:forEntity:`](#apple-geydgmi) using information in _adaptorOperation_ to supply the arguments. Raises an exception if an error occurs.

A subclass of EOAdaptorChannel doesn't need to override this method.

__See also:__
[- `performAdaptorOperations:`](#apple-geydomi)

---

### performAdaptorOperations:

- (void)__performAdaptorOperations:__ (NSArray \*)_adaptorOperations_

Performs adaptor operations by invoking [`performAdaptorOperation:`](#apple-geydmnq) with each EOAdaptorOperation object in the array _adaptorOperations_. An adaptor channel subclass may be able to override this method to take advantage of database-specific batch processing capabilities. Invokes the delegate methods [`adaptorChannel:willPerformOperations:`](../Protocols/EOAdaptorChannelDelegate.md#apple-geytmmy) and [`adaptorChannel:didPerformOperations:exception:`](../Protocols/EOAdaptorChannelDelegate.md#apple-geytgoi).

This method raises an exception if an error occurs. The exception's userInfo dictionary contains these keys:

- EOAdaptorOperationsKey
  Corresponds to the array of adaptor operations that's being executed.
- EOFailedAdaptorOperationKey
  Corresponds to the particular adaptor operation that failed.
- EOAdaptorFailureKey
  If present, offers additional information on the type of error that occurred. Currently, the only possible value for this key is EOAdaptorOptimisticLockingFailure, which indicates that an update or lock operation failed because the row found in the database did not match the snapshot taken when the row was last fetched into the application.

A subclass of EOAdaptorChannel doesn't need to override the __performAdaptorOperations:__  method.

---

### primaryKeyForNewRowWithEntity:

- (NSDictionary \*)__primaryKeyForNewRowWithEntity:__ (EOEntity \*)_entity_

Overridden by subclasses to return a primary key for a new row in the database table that corresponds to _entity_. The primary key returned from this method is a dictionary whose keys are the primary key attribute names. For example, suppose you've got a table MOVIE with primary key MOVIE_ID, and the corresponding Movie Entity's primary key attribute is `movieID`. In this scenario, the dictionary returned from [`primaryKeyForNewRowWithEntity:`](#apple-geydqna) has one entry whose key is `movieID` and whose value is the unique value to assign. If the primary key is compound (made up of more than one attribute), the dictionary should contain an entry for each primary key attribute. Note, however, that the Enterprise Objects Frameworks adaptors don't handle compound primary keys; they return `nil` from [`primaryKeyForNewRowWithEntity:`](#apple-geydqna) if the primary key is compound.

If information in _entity_ specifies an adaptor-specific means to assign a new primary key (for example, a sequence name or stored procedure), then this method returns a new primary key. Otherwise, if the key is a simple integer, the method tries to fetch a new primary key from the database using an adaptor-specific scheme. Otherwise, the method returns `nil`.

EOAdaptorChannel's implementation simply returns `nil`. See your adaptor channel's documentation for information on how it generates primary keys.

A subclass of EOAdaptorChannel must override this method. For example, to return a value generated by a sequence, you'd create the proper SQL statement (using EOSQLExpression's `expressionForString:` method) and evaluate it (using the [`evaluateExpression:`](#apple-geydaoi) method).

---

### returnValuesForLastStoredProcedureInvocation

- (NSDictionary \*)__returnValuesForLastStoredProcedureInvocation__

Implemented by subclasses to return stored procedure parameter and return values. Used in conjunction with [`executeStoredProcedure:withValues:`](#apple-gyztona). The dictionary returned by this method has entries whose keys are stored procedure parameter names and whose values are the parameter values. The dictionary also contains a special entry for the stored procedures return value with the key "returnValue". Returns an empty dictionary for stored procedures that have void return types. Returns `nil` if the stored procedure has results to fetch. In this case, you must use [`fetchRowWithZone:`](#apple-gyztsni) until there are no more results to fetch before the return value will be available.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### selectAttributes:fetchSpecification:lock:entity:

- (void)__selectAttributes:__ (NSArray \*)_attributes___fetchSpecification:__ (EOFetchSpecification \*)_fetchSpecification___lock:__ (BOOL)_flag___entity:__ (EOEntity \*)_entity_

Implemented by subclasses to select _attributes_ in rows matching the qualifier in _fetchSpecification_ and set the receiver's attributes to fetch. The selected rows compose one or more result sets, each row of which will be returned by subsequent [`fetchRowWithZone:`](#apple-gyztsni) messages according to _fetchSpecification_'s sort orderings. If _flag_ is YES, the rows are locked if possible so that no other user can modify them (the lock specification in _fetchSpecification_ is ignored). Raises an exception if an error occurs. Some possible reasons for failure are:

- The adaptor channel is in an invalid state (for example, fetching).
- The database failed to lock the specified rows.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `setAttributesToFetch:`](#apple-geydsny)

---

### setAttributesToFetch:

- (void)__setAttributesToFetch:__ (NSArray \*)_attributes_

Implemented by subclasses to specify the set of attributes used to describe fetch data from a corresponding select. _attributes_ is an array of the attributes to fetch. This method is invoked after [`evaluateExpression:`](#apple-geydaoi) but before the first call to [`fetchRowWithZone:`](#apple-gyztsni). For more information on using this method, see "Sending SQL Statements Directly to the Server" in the "WebObjects Programming Topics." Is that a good cross-reference? This method raises if invoked when there is no fetch in progress.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `attributesToFetch`](#apple-gq3dmmq), [- `selectAttributes:fetchSpecification:lock:entity:`](#apple-geydsma)

---

### setDebugEnabled:

- (void)__setDebugEnabled:__ (BOOL)_flag_

Enables debugging in the receiver and all its channels. If _flag_ is YES, enables debugging; otherwise, disables debugging. When debugging is enabled, the adaptor channel logs evaluated SQL and other useful debugging information to the console (or to the standard error stream). The information provided may vary from adaptor to adaptor and may change from release to release.

A subclass of EOAdaptorChannel doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to `super`.

__See also:__
[- `isDebugEnabled`](#apple-geydgoa), [- `setDebugEnabled:`](EOAdaptorContext.md#apple-gyzda) (EOAdaptorContext)

---

### setDelegate:

- (void)__setDelegate:__ (id)_delegate_

Sets the receiver's delegate to _delegate_, or removes its delegate if _delegate_ is `nil`. The receiver does not retain its delegate. A subclass of EOAdaptorChannel doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to `super`.

__See also:__
[- `delegate`](#apple-he3tm)

---

### updateValues:inRowDescribedByQualifier:entity:

- (void)__updateValues:__ (NSDictionary \*)_values___inRowDescribedByQualifier:__ (EOQualifier \*)_qualifier___entity:__ (EOEntity \*)_entity_

Updates the row described by _qualifier_. Invokes `[updateValues:inRowsDescribedByQualifier:entity:](#apple-gy3dgny)` and raises an exception unless exactly one row is updated.

A subclass of EOAdaptorChannel doesn't need to override this method.

---

### updateValues:inRowsDescribedByQualifier:entity:

- (unsigned int)__updateValues:__ (NSDictionary \*)_values___inRowsDescribedByQualifier:__ (EOQualifier \*)_qualifier___entity:__ (EOEntity \*)_entity_

Implemented by subclasses to update the rows described by _qualifier_ with the values in _values_. _values_ is a dictionary whose keys are attribute names and whose values are the new values for those attributes (the dictionary need only contain entries for the attributes being changed). Returns the number of updated rows. Raises an exception if an error occurs. Some possible reasons for failure are:

- The user logged in to the database doesn't have permission to update.
- The adaptor channel is in an invalid state (for example, fetching).
- The new values fail to satisfy a constraint defined in the database server.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See also:__
[- `updateValues:inRowDescribedByQualifier:entity:`](#apple-geytcmi)

---

[!](SubclassingEOAdaptor-2.md)
[!](SubclassingEOAdaptorChnnl-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
