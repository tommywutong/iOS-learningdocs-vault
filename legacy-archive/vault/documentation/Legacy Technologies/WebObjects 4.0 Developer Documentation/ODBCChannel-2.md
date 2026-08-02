---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/ODBCChannel.html
archived_at: '2026-07-18T01:28:48.724904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](ODBCAdaptor-2.md)
[!](ODBCContext-2.md)

---

# ODBCChannel

__Inherits From:__
EOAdaptorChannel : NSObject

__Declared in:__
ODBCEOAdaptor/ODBCChannel.h

---

## Class Description

An ODBCChannel represents an independent communication channel to the database server its ODBCAdaptor is connected to. All of an ODBCChannel's operations take place within the context of transactions controlled or tracked by its ODBCContext. An ODBCContext can manage multiple ODBCChannels, and a channel is associated with only one context.

The features ODBCChannel adds to EOAdaptorChannel are methods for returning the ODBC Statement Handle (HSTMT), and for returning a dictionary-formatted result from SQLTypeInfo().

---

## Method Types

**Getting the HSTMT data structure**

**[- odbcStatement](#apple-gi3deoi)**

**Getting type information**

**[- odbcTypeInfo](#apple-he3a)**

**Opening and closing a channel**

**[- openChannel](#apple-geyda)

**[- closeChannel](#apple-gq4a)

**[- isOpen](#apple-ha4a)******

**Modifying rows**

**[- deleteRowsDescribedByQualifier:entity:](#apple-guza)

**[- insertRow:forEntity:](#apple-haya)****

**Getting schema information**

**[- describeModelWithTableNames:](#apple-gi2tcmy)

**[- describeTableNames](#apple-gi2teny)****

**Fetching rows**

**[- selectAttributes:fetchSpecification:lock:entity:](#apple-geydq)

**[- fetchRowWithZone:](#apple-g4za)

**[- attributesToFetch](#apple-gqya)

**[- cancelFetch](#apple-gq2a)

**[- describeResults](#apple-gyya)

**[- setAttributesToFetch:](#apple-geyte)

**[- isFetchInProgress](#apple-ha2a)**************

**Sending SQL to the server**

**[- evaluateExpression:](#apple-gy4a)**

**Assigning primary keys**

**[- primaryKeyForNewRowWithEntity:](#apple-gi3dioa)**

---

## Instance Methods

---

### attributesToFetch

- (NSArray \*)`attributesToFetch`

Overrides the EOAdaptorChannel method `attributesToFetch` to return the set of attributes to retrieve with `fetchRowWithZone:`.

---

### cancelFetch

- (void)`cancelFetch`

Overrides the EOAdaptorChannel method `cancelFetch` to clear all result sets established by the last `selectAttributes:fetchSpecification:lock:entity:` or `evaluateExpression:` message and terminate the current fetch, so that `isFetchInProgress` returns NO.

---

### closeChannel

- (void)`closeChannel`

Overrides the EOAdaptorChannel method `closeChannel` to close the channel so that it can't perform operations with the server. Any fetch in progress is canceled. This method has the side effect of closing the receiver's adaptor context's connection with the database if the receiver is its adaptor context's last open channel.

---

### deleteRowsDescribedByQualifier:entity:

- (unsigned)`deleteRowsDescribedByQualifier:`(EOQualifier \*)_qualifier_`entity:`(EOEntity \*)_entity_

Overrides the EOAdaptorChannel method `deleteRowsDescribedByQualifier:entity:` to delete the rows described by _qualifier_ and return the number of rows deleted. Raises an exception on failure. Some possible reasons for failure are:

- The adaptor channel isn't open
- The adaptor channel is in an invalid state (for example, it's fetching).
- An error occurs in the database server

---

### describeModelWithTableNames:

- (EOModel \*)`describeModelWithTableNames:`(NSArray \*)_tableNames_

Overrides the EOAdaptorChannel method `describeModelWithTableNames:` to create and return a default model containing entities for the tables specified in _tableNames_. Assigns the adaptor name and connection dictionary to the new model. This method is typically used in conjunction with `describeTableNames`. Raises an exception if an error occurs.

---

### describeResults

- (NSArray \*)`describeResults`

Overrides the EOAdaptorChannel method `describeResults` to return an array of EOAttributes describing the properties available in the current result set, as determined by `selectAttributes:fetchSpecification:lock:entity:` or a statement evaluated by `evaluateExpression:`. Raises an exception if an error occurs.

---

### describeTableNames

- (NSArray \*)`describeTableNames`

Overrides the EOAdaptorChannel method `describeTableNames` to read and return an array of table names from the database. This method is used in conjunction with `describeModelWithTableNames:` to build a default model. Raises an exception if an error occurs.

---

### evaluateExpression:

- (void)`evaluateExpression:`(EOSQLExpression \*)_expression_

Overrides the EOAdaptorChannel method `evaluateExpression:` to send _expression_ to the database server for evaluation, beginning a transaction first and committing it after evaluation if a transaction isn't already in progress. Raises an exception if an error occurs.

---

### fetchRowWithZone:

- (NSMutableDictionary \*)`fetchRowWithZone:`(NSZone \*)_zone_

Overrides the EOAdaptorChannel method `fetchRowWithZone:` to fetch the next row from the result set of the last `selectAttributes:fetchSpecification:lock:entity:` or `evaluateExpression:` message sent to the receiver. Returns values for the receiver's `attributesToFetch`. When there are no more rows in the current result set, this method returns `nil`, and invokes the delegate method `adaptorChannelDidChangeResultSet:` if there are more results sets. When there are no more rows or result sets, this method returns `nil`, ends the fetch, and invokes `adaptorChannelDidFinishFetching:`. `isFetchInProgress` returns YES until the fetch is canceled or until this method exhausts all result sets and returns `nil`. Raises an exception if an error occurs.

---

### insertRow:forEntity:

- (void)`insertRow:`(NSDictionary \*)_row_ `forEntity:`(EOEntity \*)_entity_

Overrides the EOAdaptorChannel method `insertRow:forEntity:` to insert the values of _row_ into the table in the database that corresponds to _entity_. _row_ is an NSDictionary whose keys are attribute names and whose values are the values to insert. Raises an exception on failure. Some possible reasons for failure are:

- The user logged in to the database doesn't have permission to insert a new row.
- The adaptor channel is in an invalid state (for example, fetching).
- The row fails to satisfy a constraint defined in the database server.

---

### isFetchInProgress

- (BOOL)`isFetchInProgress`

Overrides the EOAdaptorChannel method `isFetchInProgress` to return YES if the receiver is fetching, NO otherwise. An adaptor channel is fetching if:

- It's been sent a successful `selectAttributes:fetchSpecification:lock:entity:` message.
- An expression sent through `evaluateExpression:` resulted in a select operation being performed.

An adaptor channel stops fetching when there are no more records to fetch or when it's sent a `cancelFetch` message.

---

### isOpen

- (BOOL)`isOpen`

Overrides the EOAdaptorChannel method `isOpen` to return YES if the channel has been opened with `openChannel`, NO if not.

---

### odbcStatement

- (void \*)`odbcStatement`

Returns the ODBC Statement Handle HSTMT as a `void*`; you must cast the returned value to HSTMT to work with it.

---

### odbcTypeInfo

- (NSDictionary \*)`odbcTypeInfo`

Returns the result from SQLTypeInfo(), formatted in an NSDictionary ready to incorporate into a model file.

---

### openChannel

- (void)`openChannel`

Overrides the EOAdaptorChannel method `openChannel` to put the channel and both its context and adaptor into a state where they are ready to perform database operations. Raises an exception if error occurs.

---

### primaryKeyForNewRowWithEntity:

- (NSDictionary \*)`primaryKeyForNewRowWithEntity:`(EOEntity \*)_entity_

Overrides the EOAdaptorChannel method `primaryKeyForNewRowWithEntity:` to return a primary key for a new row in the database table that corresponds to _entity_. If unsuccessful, returns `nil`.

---

### selectAttributes:fetchSpecification:lock:entity:

- (void)`selectAttributes:`(NSArray \*)_attributes_`fetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_`lock:`(BOOL)_flag_`entity:`(EOEntity \*)_entity_

Overrides the EOAdaptorChannel method `selectAttributes:fetchSpecification:lock:entity:` to select _attributes_ in rows matching the qualifier in _fetchSpecification_ and set the receiver's attributes to fetch. The selected rows compose one or more result sets, each row of which will be returned by subsequent `fetchRowWithZone:` messages according to _fetchSpecification_'s sort orderings. If _flag_ is YES, the rows are locked if possible so that no other user can modify them (the lock specification in _fetchSpecification_ is ignored). Raises an exception if an error occurs. Some possible reasons for failure are:

- The adaptor channel is in an invalid state (for example, fetching).
- The database failed to lock the specified rows.

---

### setAttributesToFetch:

- (void)`setAttributesToFetch:`(NSArray \*)_attributes_

Overrides the EOAdaptorChannel method `setAttributesToFetch:` to change the set of _attributes_ used to describe the fetch data in the middle of a select. This method raises an exception if invoked when there is no fetch in progress.

---

### updateValues:inRowsDescribedByQualifier:entity:

- (unsigned)`updateValues:`(NSDictionary \*)_row_`inRowsDescribedByQualifier:`(EOQualifier \*)_qualifier_`entity:`(EOEntity \*)_entity_

Overrides the EOAdaptorChannel method `updateValues:inRowsDescribedByQualifier:entity:` to update the rows described by _qualifier_ with the values in _values_. _values_ is an NSDictionary whose keys are attribute names and whose values are the new values for those attributes (the dictionary need only contain entries for the attributes being changed). Returns the number of updated rows. Raises an exception if an error occurs. Some possible reasons for failure are:

- The user logged in to the database doesn't have permission to update.
- The adaptor channel is in an invalid state (for example, fetching).
- The new values fail to satisfy a constraint defined in the database server.

****

---

[!](ODBCAdaptor-2.md)
[!](ODBCContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
