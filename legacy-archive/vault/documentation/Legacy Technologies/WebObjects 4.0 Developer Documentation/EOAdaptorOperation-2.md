---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAdaptorOperation.html
archived_at: '2026-07-18T01:28:15.690966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](More%20about%20EOAdaptorContext.md)
[!](EOAttribute-2.md)

---

# EOAdaptorOperation

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EODatabaseOperation.h

---

## Class Description

An EOAdaptorOperation object represents a primitive operation in a database server-lock, insert, update, or delete a row; or execute a stored procedure-and all the necessary information required by the operation. An EOAdaptorOperation is processed by an EOAdaptorChannel object in the method [`performAdaptorOperation:`](EOAdaptorChannel.md#apple-geydmnq). You don't ordinarily create instances of EOAdaptorOperation; rather, the Framework automatically creates an EOAdaptorOperation object and sends it to an adaptor channel when your application needs the database server to perform an operation. You generally interact with EOAdaptorOperation objects only if you need to specify the order in which a set of operations are carried out (see the description for the EODatabaseContext delegate method __databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:__ ).

An EOAdaptorOperation has an entity and an operator (the type of operation the object represents). An adaptor operation's operator (EOAdaptorLockOperator, EOAdaptorInsertOperator, EOAdaptorUpdateOperator, EOAdaptorDeleteOperator, or EOAdaptorStoredProcedureOperator) determines additional, operator-dependent information used by the EOAdaptorOperation object. For example, only a stored procedure operation has an EOStoredProcedure object. The operator-dependent information is accessible using the methods described below.

---

## Method Types

**Creating a new EOAdaptorOperation**

**[- initWithEntity:](#apple-gyyteni)**

**Accessing the entity**

**[- entity](#apple-gmzdooi)**

**Accessing the operator**

**[- setAdaptorOperator:](#apple-gi3deoi)

**[- adaptorOperator](#apple-gi2tq)****

**Accessing the qualifier**

**[- setStoredProcedure:](#apple-gmydknq)

**[- qualifier](#apple-giytooa)****

**Accessing locking attributes**

**[- setAttributes:](#apple-gi3dmma)

**[- attributes](#apple-gizdgmi)****

**Accessing operation values**

**[- setChangedValues:](#apple-gi3dqny)

**[- changedValues](#apple-gizdgoi)****

**Accessing a stored procedure**

**[- setStoredProcedure:](#apple-gmydknq)

**[- storedProcedure](#apple-giydsoa)****

**Handling errors during the operation**

**[- setException:](#apple-gi4dqna)

**[- exception](#apple-giytqoi)****

**Comparing operations**

**[- compareAdaptorOperation:](#apple-gi2dsmy)**

---

## Instance Methods

---

### adaptorOperator

- (EOAdaptorOperator)__adaptorOperator__

Returns the receiver's adaptor operator. The operator indicates which of the other adaptor operation attributes are valid. For example, an adaptor operation whose operator is EOAdaptorInsertOperator uses `[changedValues](#apple-gizdgoi)`, but not `[attributes](#apple-gizdgmi)`, `[qualifier](#apple-giytooa)`, or `[storedProcedure](#apple-giydsoa)`.

__See also:__
[`setAdaptorOperator:`](#apple-gi3deoi)

---

### attributes

- (NSArray \*)__attributes__

Returns the array of attributes to select when locking the row. If attributes have not been assigned to the receiver, the primary key attributes are selected. Only valid for adaptor operations with the EOAdaptorLockOperator.

__See also:__
[- `setAttributes:`](#apple-gi3dmma)

---

### changedValues

- (NSDictionary \*)__changedValues__

Returns the dictionary of values that need to be updated, inserted, or compared for locking purposes.

__See also:__
[- `setChangedValues:`](#apple-gi3dqny)

---

### compareAdaptorOperation:

- (NSComparisonResult)__compareAdaptorOperation:__ (EOAdaptorOperation \*)_operation_

Orders adaptor operations alphabetically by entity name and by adaptor operator within the same entity. The adaptor operators are ordered as follows:

- EOAdaptorLockOperator
- EOAdaptorInsertOperator
- EOAdaptorUpdateOperator
- EOAdaptorDeleteOperator
- EOAdaptorStoredProcedureOperator

EOAdaptorLockOperator precedes EOAdaptorInsertOperator, EOAdaptorInsertOperator precedes EOAdaptorUpdateOperator, and so on.

An EODatabaseContext uses `compareAdaptorOperation:` to order adaptor operations before invoking EOAdaptorChannel's [`performAdaptorOperations:`](EOAdaptorChannel.md#apple-geydomi) method.

---

### entity

- (EOEntity \*)__entity__

Returns the entity to which the operation will be applied.

__See also:__
[- `initWithEntity:`](#apple-gyyteni)

---

### exception

- (NSException \*)__exception__

Returns the exception that was raised when an adaptor channel attempted to process the receiver. Returns `nil` if no exception was raised or if the receiver hasn't been processed yet.

__See also:__
[- `setException:`](#apple-gi4dqna)

---

### qualifier

- (EOQualifier \*)__qualifier__

Returns the qualifier that identifies the specific row to which the operation applies. Not valid with adaptor operations with the operators EOAdaptorInsertOperator and EOAdaptorStoredProcedureOperator.

---

### initWithEntity:

- __initWithEntity:__ (EOEntity \*)_entity_

The designated initializer, initializes a new EOAdaptorOperation instance, and sets the entity to which the operation will be applied. Returns `self`.

__See also:__
[- `entity`](#apple-gmzdooi)

---

### setAdaptorOperator:

- (void)__setAdaptorOperator:__ (EOAdaptorOperator)_adaptorOperator_

Sets the receiver's operator to _adaptorOperator_, which is one of the following:

- EOAdaptorLockOperator
- EOAdaptorInsertOperator
- EOAdaptorUpdateOperator
- EOAdaptorDeleteOperator
- EOAdaptorStoredProcedureOperator

For more information, see the discussion on adaptor operators in the class description above.

__See also:__
[- `adaptorOperator`](#apple-gi2tq)

---

### setAttributes:

- (void)__setAttributes:__ (NSArray \*)_attributes_

Sets the array of attributes to select when locking the row. The selected values are compared in memory to the corresponding snapshot values to determine if a row has changed since the application last fetched it. _attributes_ is an array of EOAttribute objects that can't be compared in a qualifier (generally BLOB types); it should not be `nil` or empty. Generally, an adaptor operation's qualifier contains all the comparisons needed to verify that a row hasn't changed since the application last fetched, inserted, or updated it. In this case (if there aren't any attributes that can't be compared in a qualifier), _attributes_ should contain primary key attributes. This method is only valid for adaptor operations with the EOAdaptorLockOperator.

__See also:__
[- `attributes`](#apple-gizdgmi), [- `entity`](#apple-gmzdooi)

---

### setChangedValues:

- (void)__setChangedValues:__ (NSDictionary \*)_changedValues_

Sets the dictionary of values that need to be updated, inserted, or compared for locking purposes. _changedValues_ is a dictionary object whose keys are attribute names and whose values are the values for those attributes. As summarized in the following table, the contents of _changedValues_ depends on the receiver's operator:

| __Operator__ | __Contents of changedValues Dictionary__ |
| EOAdaptorLockOperator | snapshot values used to verify that the database row hasn't changed since this application last fetched it |
| EOAdaptorInsertOperator | the values to insert |
| EOAdaptorUpdateOperator | the new values for the columns to update |
| EOAdaptorDeleteOperator | snapshot values (_changedValues_ is only valid for AdaptorDeleteOperation if the receiver's entity uses a stored procedure to perform delete operations.) |
| EOAdaptorStoredProcedureOperator | snapshot values |

```
```

__See also:__
[- `changedValues`](#apple-gizdgoi)

---

### setException:

- (void)__setException:__ (NSException \*)_exception_

Sets the receiver's exception to _exception_. This method is typically invoked from EOAdaptorChannel's [`performAdaptorOperations:`](EOAdaptorChannel.md#apple-geydomi) method. If a database error occurs while processing an adaptor operation, the adaptor channel creates an exception and assigns it to the adaptor operation.

__See also:__
[- `exception`](#apple-giytqoi)

---

### setQualifier:

- (void)__setQualifier:__ (EOQualifier \*)_qualifier_

Sets the qualifier that identifies the row to which the adaptor operation is to be applied to _qualifier_.

__See also:__
[- `qualifier`](#apple-giytooa)

---

### setStoredProcedure:

- (void)`setStoredProcedure:`(EOStoredProcedure \*)_storedProcedure_

Sets the receiver's stored procedure to _storedProcedure_.

__See also:__
[- `storedProcedure`](#apple-giydsoa)

---

### storedProcedure

- (EOStoredProcedure \*)`storedProcedure`

Returns the receiver's stored procedure. Only valid with adaptor operations with the EOAdaptorStoredProcedureOperation.

__See also:__
[- `setStoredProcedure:`](#apple-gmydknq)

---

### 

---

[!](More%20about%20EOAdaptorContext.md)
[!](EOAttribute-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
