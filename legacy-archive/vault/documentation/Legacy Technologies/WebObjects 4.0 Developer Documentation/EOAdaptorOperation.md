---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOAdaptorOperation.html
archived_at: '2026-07-18T01:28:08.896076Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAdaptorContext-2.md)
[!](EOAttribute.md)

---

# EOAdaptorOperation

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

An EOAdaptorOperation object represents a primitive operation in a database server-lock, insert, update, or delete a row; or execute a stored procedure-and all the necessary information required by the operation. An EOAdaptorOperation is processed by an EOAdaptorChannel object in the method [`performAdaptorOperation`](EOAdaptorChannel.md#apple-geydmnq). You don't ordinarily create instances of EOAdaptorOperation; rather, the Framework automatically creates an EOAdaptorOperation object and sends it to an adaptor channel when your application needs the database server to perform an operation. You generally interact with EOAdaptorOperation objects only if you need to specify the order in which a set of operations are carried out (see the description for the EODatabaseContext delegate method __databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:__ ).

An EOAdaptorOperation has an entity and an operator (the type of operation the object represents). An adaptor operation's operator (AdaptorLockOperator, AdaptorInsertOperator, AdaptorUpdateOperator, AdaptorDeleteOperator, or AdaptorStoredProcedureOperator) determines additional, operator-dependent information used by the EOAdaptorOperation object. For example, only a stored procedure operation has an EOStoredProcedure object. The operator-dependent information is accessible using the methods described below.

---

## Method Types

**Constructors**

**[EOAdaptorOperation](#apple-g4ytemi)**

**Accessing the entity**

**[entity](#apple-gmzdooi)**

**Accessing the operator**

**[setAdaptorOperator](#apple-gi3deoi)

**[adaptorOperator](#apple-gi2tq)****

**Accessing the qualifier**

****[setQualifier](#apple-gi4taoi)

**[qualifier](#apple-giytooa)******

**Accessing locking attributes**

**[setAttributes](#apple-gi3dmma)

**[attributes](#apple-gizdgmi)****

**Accessing operation values**

**[setChangedValues](#apple-gi3dqny)

**[changedValues](#apple-gizdgoi)****

**Accessing a stored procedure**

**[setStoredProcedure](#apple-gmydknq)

**[storedProcedure](#apple-giydsoa)****

**Handling errors during the operation**

**[setException](#apple-gi4dqna)

**[exception](#apple-giytqoi)****

**Comparing operations**

**[compareAdaptorOperation](#apple-gi2dsmy)**

---

## Constructors

---

### EOAdaptorOperation

public `EOAdaptorOperation`()

public `EOAdaptorOperation`(Entity _entity_)

Creates and returns a new EOAdaptorOperation, with _entity_ as the entity to which the operation will be applied.

__See also:__
[`entity`](#apple-gmzdooi)

---

## Instance Methods

---

### adaptorOperator

public int `adaptorOperator`

Returns the receiver's adaptor operator. The operator indicates which of the other adaptor operation attributes are valid. For example, an adaptor operation whose operator is AdaptorInsertOperator uses `[changedValues](#apple-gizdgoi)`, but not `[attributes](#apple-gizdgmi)`, `[qualifier](#apple-giytooa)`, or `[storedProcedure](#apple-giydsoa)`.

__See also:__
[`setAdaptorOperator`](#apple-gi3deoi)

---

### attributes

public NSArray `attributes`()

Returns the array of attributes to select when locking the row. If attributes have not been assigned to the receiver, the primary key attributes are selected. Only valid for adaptor operations with the AdaptorLockOperator.

__See also:__
[`setAttributes`](#apple-gi3dmma)

---

### changedValues

public NSDictionary `changedValues`()

Returns the dictionary of values that need to be updated, inserted, or compared for locking purposes.

__See also:__
[`setChangedValues`](#apple-gi3dqny)

---

### compareAdaptorOperation

public int `compareAdaptorOperation`(EOAdaptorOperation _anAdaptorOperation_)

Orders adaptor operations alphabetically by entity name and by adaptor operator within the same entity. The adaptor operators are ordered as follows:

- AdaptorLockOperator
- AdaptorInsertOperator
- AdaptorUpdateOperator
- AdaptorDeleteOperator
- AdaptorStoredProcedureOperator

AdaptorLockOperator precedes AdaptorInsertOperator, AdaptorInsertOperator precedes AdaptorUpdateOperator, and so on.

An EODatabaseContext uses `compareAdaptorOperation:` to order adaptor operations before invoking EOAdaptorChannel's [`performAdaptorOperations`](EOAdaptorChannel.md#apple-geydomi) method.

---

### entity

public EOEntity `entity`()

Returns the entity to which the operation will be applied.

__See also:__
["Constructors"](#apple-g4ytcoi)

---

### exception

public java.lang.Throwable `exception`()

Returns the exception that was thrown when an adaptor channel attempted to process the receiver. Returns `null` if no exception was thrown or if the receiver hasn't been processed yet.

__See also:__
[`setException`](#apple-gi4dqna)

---

### qualifier

public com.apple.yellow.eocontrol.EOQualifier `qualifier`()

Returns the qualifier that identifies the specific row to which the operation applies. Not valid with adaptor operations with the operators AdaptorInsertOperator and AdaptorStoredProcedureOperator.

__See also:__
[`setStoredProcedure`](#apple-gmydknq)

---

### setAdaptorOperator

public void `setAdaptorOperator`(int _adaptorOperator_)

Sets the receiver's operator to _adaptorOperator_, which is one of the following:

- AdaptorLockOperator
- AdaptorInsertOperator
- AdaptorUpdateOperator
- AdaptorDeleteOperator
- AdaptorStoredProcedureOperator

For more information, see the discussion on adaptor operators in the class description above.

__See also:__
[`adaptorOperator`](#apple-gi2tq)

---

### setAttributes

public void `setAttributes`(NSArray _attributes_)

Sets the array of attributes to select when locking the row. The selected values are compared in memory to the corresponding snapshot values to determine if a row has changed since the application last fetched it. _attributes_ is an array of EOAttribute objects that can't be compared in a qualifier (generally BLOB types); it should not be `null` or empty. Generally, an adaptor operation's qualifier contains all the comparisons needed to verify that a row hasn't changed since the application last fetched, inserted, or updated it. In this case (if there aren't any attributes that can't be compared in a qualifier), _attributes_ should contain primary key attributes. This method is only valid for adaptor operations with the AdaptorLockOperator.

__See also:__
[`attributes`](#apple-gizdgmi), [`entity`](#apple-gmzdooi)

---

### setChangedValues

public void `setChangedValues`(NSDictionary _changedValues_)

Sets the dictionary of values that need to be updated, inserted, or compared for locking purposes. _changedValues_ is a dictionary object whose keys are attribute names and whose values are the values for those attributes. As summarized in the following table, the contents of _changedValues_ depends on the receiver's operator:

| __Operator__ | __Contents of changedValues Dictionary__ |
| AdaptorLockOperator | snapshot values used to verify that the database row hasn't changed since this application last fetched it |
| AdaptorInsertOperator | the values to insert |
| AdaptorUpdateOperator | the new values for the columns to update |
| AdaptorDeleteOperator | snapshot values (_changedValues_ is only valid for AdaptorDeleteOperation if the receiver's entity uses a stored procedure to perform delete operations.) |
| AdaptorStoredProcedureOperator | snapshot values |

```
```

__See also:__
[`changedValues`](#apple-gizdgoi)

---

### setException

public void `setException`(java.lang.Throwable _exception_)

Sets the receiver's exception to _exception_. This method is typically invoked from EOAdaptorChannel's [`performAdaptorOperations`](EOAdaptorChannel.md#apple-geydomi) method. If a database error occurs while processing an adaptor operation, the adaptor channel creates an exception and assigns it to the adaptor operation.

__See also:__
[`exception`](#apple-giytqoi)

---

### setQualifier

public void `setQualifier`(com.apple.yellow.eocontrol.EOQualifier _qualifier_)

Sets the qualifier that identifies the row to which the adaptor operation is to be applied to _qualifier_.

__See also:__
[`qualifier`](#apple-giytooa)

---

### setStoredProcedure

public void `setStoredProcedure`(EOStoredProcedure _storedProcedure_)

Sets the receiver's stored procedure to _storedProcedure_.

__See also:__
[`storedProcedure`](#apple-giydsoa)

---

### storedProcedure

public EOStoredProcedure `storedProcedure`()

Returns the receiver's stored procedure. Only valid with adaptor operations with the AdaptorStoredProcedureOperation.

__See also:__
[`setStoredProcedure`](#apple-gmydknq)

---

### 

---

[!](EOAdaptorContext-2.md)
[!](EOAttribute.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
