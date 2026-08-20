---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/ODBCChannel.html
archived_at: '2026-07-18T01:28:48.351704Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](ODBCAdaptor.md)
[!](ODBCContext.md)

---

# ODBCChannel

__Inherits From:__
EOAdaptorChannel : NSObject

__Inherits From:__
com.apple.yellow.odbceoadaptor

---

## Class Description

An ODBCChannel represents an independent communication channel to the database server its ODBCAdaptor is connected to. All of an ODBCChannel's operations take place within the context of transactions controlled or tracked by its ODBCContext. An ODBCContext can manage multiple ODBCChannels, and a channel is associated with only one context.

The features ODBCChannel adds to EOAdaptorChannel are methods for returning the ODBC Statement Handle (HSTMT), and for returning a dictionary-formatted result from SQLTypeInfo().

---

## Method Types

**Getting type information**

**[odbcTypeInfo](#apple-he3a)**

**Opening and closing a channel**

**[openChannel](#apple-geyda)

**[closeChannel](#apple-gq4a)

**[isOpen](#apple-ha4a)******

**Modifying rows**

**[deleteRowsDescribedByQualifier](#apple-guza)

**[insertRow](#apple-haya)****

**Fetching rows**

**[selectAttributesWithFetchSpecification](#apple-geydq)

**[fetchRow](#apple-g4za)

**[attributesToFetch](#apple-gqya)

**[cancelFetch](#apple-gq2a)

**[describeResults](#apple-gyya)

**[setAttributesToFetch](#apple-geyte)

**[isFetchInProgress](#apple-ha2a)**************

**Sending SQL to the server**

**[evaluateExpression](#apple-gy4a)**

---

## Instance Methods

---

### attributesToFetch

public com.apple.yellow.foundation.NSArray `attributesToFetch`()

Overrides the EOAdaptorChannel method `attributesToFetch` to return the set of attributes to retrieve with [`fetchRow`](#apple-g4za).

---

### cancelFetch

public void `cancelFetch`()

Overrides the EOAdaptorChannel method `cancelFetch` to clear all result sets established by the last [`selectAttributesWithFetchSpecification`](#apple-geydq) or [`evaluateExpression`](#apple-gy4a) message and terminate the current fetch, so that [`isFetchInProgress`](#apple-ha2a) returns NO.

---

### closeChannel

public void `closeChannel`()

Overrides the EOAdaptorChannel method `closeChannel` to close the channel so that it can't perform operations with the server. Any fetch in progress is canceled. This method has the side effect of closing the receiver's adaptor context's connection with the database if the receiver is its adaptor context's last open channel.

---

### deleteRowsDescribedByQualifier

public int `deleteRowsDescribedByQualifier`(com.apple.yellow.eocontrol.EOQualifier _qualifier_, com.apple.yellow.eoaccess.EOEntity _entity_)

Overrides the EOAdaptorChannel method `deleteRowsDescribedByQualifier` to delete the rows described by _qualifier_ and return the number of rows deleted. Raises an exception on failure. Some possible reasons for failure are:

- The adaptor channel isn't open
- The adaptor channel is in an invalid state (for example, it's fetching).
- An error occurs in the database server

---

### describeResults

public com.apple.yellow.foundation.NSArray `describeResults`()

Overrides the EOAdaptorChannel method `describeResults` to return an array of EOAttributes describing the properties available in the current result set, as determined by [`selectAttributesWithFetchSpecification`](#apple-geydq) or a statement evaluated by [`evaluateExpression`](#apple-gy4a). Raises an exception if an error occurs.

---

### evaluateExpression

public void `evaluateExpression`(com.apple.yellow.eoaccess.EOSQLExpression _expression_)

Overrides the EOAdaptorChannel method `evaluateExpression` to send _expression_ to the database server for evaluation, beginning a transaction first and committing it after evaluation if a transaction isn't already in progress. Raises an exception if an error occurs.

---

### fetchRow

public com.apple.yellow.foundation.NSMutableDictionary `fetchRow`()

Overrides the EOAdaptorChannel method `fetchRow` to fetch the next row from the result set of the last [`selectAttributesWithFetchSpecification`](#apple-geydq) or [`evaluateExpression`](#apple-gy4a) message sent to the receiver. Returns values for the receiver's [`attributesToFetch`](#apple-gqya). When there are no more rows in the current result set, this method returns `null`, and invokes the delegate method `adaptorChannelDidChangeResultSet` if there are more results sets. When there are no more rows or result sets, this method returns `null`, ends the fetch, and invokes `adaptorChannelDidFinishFetching`. [`isFetchInProgress`](#apple-ha2a) returns `true` until the fetch is canceled or until this method exhausts all result sets and returns `null`. Raises an exception if an error occurs.

---

### insertRow

public void `insertRow`(com.apple.yellow.foundation.NSDictionary _row_, com.apple.yellow.eoaccess.EOEntity _entity_)

Overrides the EOAdaptorChannel method `insertRow` to insert the values of _row_ into the table in the database that corresponds to _entity_. _row_ is an NSDictionary whose keys are attribute names and whose values are the values to insert. Raises an exception on failure. Some possible reasons for failure are:

- The user logged in to the database doesn't have permission to insert a new row.
- The adaptor channel is in an invalid state (for example, fetching).
- The row fails to satisfy a constraint defined in the database server.

---

### isFetchInProgress

public boolean `isFetchInProgress`()

Overrides the EOAdaptorChannel method `isFetchInProgress` to return `true` if the receiver is fetching, `false` otherwise. An adaptor channel is fetching if:

- It's been sent a successful [`selectAttributesWithFetchSpecification`](#apple-geydq) message.
- An expression sent through [`evaluateExpression`](#apple-gy4a) resulted in a select operation being performed.

An adaptor channel stops fetching when there are no more records to fetch or when it's sent a [`cancelFetch`](#apple-gq2a) message.

---

### isOpen

public boolean `isOpen`()

Overrides the EOAdaptorChannel method `isOpen` to return `true` if the channel has been opened with [`openChannel`](#apple-geyda), `false` if not.

---

### odbcTypeInfo

public com.apple.yellow.foundation.NSDictionary `odbcTypeInfo`()

Returns the result from SQLTypeInfo(), formatted in an NSDictionary ready to incorporate into a model file.

---

### openChannel

public void `openChannel`()

Overrides the EOAdaptorChannel method `openChannel` to put the channel and both its context and adaptor into a state where they are ready to perform database operations. Raises an exception if error occurs.

---

### selectAttributesWithFetchSpecification

public void `selectAttributesWithFetchSpecification`(com.apple.yellow.foundation.NSArray _attributes_, com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
boolean _flag_,
com.apple.yellow.eoaccess.EOEntity _entity_)

Overrides the EOAdaptorChannel method `selectAttributesWithFetchSpecification` to select _attributes_ in rows matching the qualifier in _fetchSpecification_ and set the receiver's attributes to fetch. The selected rows compose one or more result sets, each row of which will be returned by subsequent [`fetchRow`](#apple-g4za) messages according to _fetchSpecification_'s sort orderings. If _flag_ is `true`, the rows are locked if possible so that no other user can modify them (the lock specification in _fetchSpecification_ is ignored). Raises an exception if an error occurs. Some possible reasons for failure are:

- The adaptor channel is in an invalid state (for example, fetching).
- The database failed to lock the specified rows.

---

### setAttributesToFetch

public void `setAttributesToFetch`(com.apple.yellow.foundation.NSArray _attributes_)

Overrides the EOAdaptorChannel method `setAttributesToFetch` to change the set of _attributes_ used to describe the fetch data in the middle of a select. This method raises an exception if invoked when there is no fetch in progress.

---

### updateValuesInRowsDescribedByQualifier

public int `updateValuesInRowsDescribedByQualifier`(com.apple.yellow.foundation.NSDictionary _row_, com.apple.yellow.eocontrol.EOQualifier _qualifier_,
com.apple.yellow.eoaccess.EOEntity _entity_)

Overrides the EOAdaptorChannel method `updateValuesInRowsDescribedByQualifier` to update the rows described by _qualifier_ with the values in _values_. _values_ is an NSDictionary whose keys are attribute names and whose values are the new values for those attributes (the dictionary need only contain entries for the attributes being changed). Returns the number of updated rows. Raises an exception if an error occurs. Some possible reasons for failure are:

- The user logged in to the database doesn't have permission to update.
- The adaptor channel is in an invalid state (for example, fetching).
- The new values fail to satisfy a constraint defined in the database server.

****

---

[!](ODBCAdaptor.md)
[!](ODBCContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
