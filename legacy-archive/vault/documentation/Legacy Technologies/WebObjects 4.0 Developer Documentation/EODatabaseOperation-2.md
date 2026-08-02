---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODatabaseOperation.html
archived_at: '2026-07-18T01:28:16.295430Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODatabaseDataSource-2.md)
[!](EOEntity-2.md)

---

# EODatabaseOperation

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EODatabaseOperation.h

---

## Class Description

An EODatabaseOperation object represents an operation-insert, update, or delete-to perform on an enterprise object and all the necessary information required to perform the operation. You don't ordinarily create instances of EODatabaseOperation; rather, the Framework automatically creates an EODatabaseOperation object for each new, updated, or deleted object in an EOEditingContext. An EODatabaseContext object analyzes a set of database operations and maps each operation to one or more adaptor operations. The adaptor operations are then performed by an EOAdaptorChannel object. You generally interact with EODatabaseOperation objects only if you need to specify the order in which a set of operations are carried out (see the description for the EODatabaseContext delegate method `databaseContextWillOrderAdaptorOperationsFromDatabaseOperationsdatabaseContext:willOrderAdaptorOperationsFromDatabaseOperations:`).

An EODatabaseOperation specifies an enterprise object (called "object") on which the operation is performed, the EOGlobalID for the object, and the object's entity. In addition, the database operation has a snapshot containing the last known database values for the object and a `newRow` dictionary of new or updated values to save in the database. Finally, a database operation specifies one of the following operators (the type of operation represented by the database operation).

- EODatabaseNothingOperator
- EODatabaseInsertOperator
- EODatabaseUpdateOperator
- EODatabaseDeleteOperator

---

## Method Types

**Creating a new EODatabaseOperation**

**[- initWithGlobalID:object:entity:](#apple-gy3tkmy)**

**Accessing the global ID object**

**[- globalID](#apple-gi3tg)**

**Accessing the object**

**[- object](#apple-gi4dm)**

**Accessing the entity**

**[- entity](#apple-gi3ds)**

**Accessing the operator**

**[- setDatabaseOperator:](#apple-gmydm)

**[- databaseOperator](#apple-gi3dc)****

**Accessing the database snapshot**

**[- setDBSnapshot:](#apple-gi3dqmi)

**[- dbSnapshot](#apple-gi3dk)****

**Accessing the row**

**[- setNewRow:](#apple-gmyta)

**[- newRow](#apple-gi4dc)****

**Accessing the adaptor operations**

**[- addAdaptorOperation:](#apple-gi2to)

**[- removeAdaptorOperation:](#apple-gizdg)

**[- adaptorOperations](#apple-giztkna)******

**Comparing new row and snapshot values**

**[- rowDiffs](#apple-gi4ti)

**[- rowDiffsForAttributes:](#apple-gi4tq)****

**Working with to-many snapshots**

**[- recordToManySnapshot:relationshipName:](#apple-gy4dqni)

**[- toManySnapshots](#apple-g4ydgma)****

---

## Instance Methods

---

### adaptorOperations

- (NSArray \*)`adaptorOperations`

Returns the EOAdaptorOperation objects that need to be performed to carry out the operation represented by the receiver.

__See also:__
[- `addAdaptorOperation:`](#apple-gi2to), [- `removeAdaptorOperation:`](#apple-gizdg)

---

### addAdaptorOperation:

- (void)`addAdaptorOperation:`(EOAdaptorOperation \*)_adaptorOperation_

Adds _adaptorOperation_ to the receiver's list of adaptor operations. Raises an exception if _adaptorOperation_ is `nil`.

__See also:__
[- `adaptorOperations`](#apple-giztkna), [- `removeAdaptorOperation:`](#apple-gizdg)

---

### databaseOperator

- (EODatabaseOperator)`databaseOperator`

Returns the receiver's database operator.

__See also:__
[`setDatabaseOperator:`](#apple-gmydm)

---

### dbSnapshot

- (NSDictionary \*)`dbSnapshot`

Returns the database snapshot for the receiver's enterprise object. The snapshot contains the last known database values for the enterpriseobject. The dictionary returned from this method will be empty if the receiver's object has just been inserted into an EOEditingContext and has not yet been saved in persistent storage. For more information on EOEditingContexts, see the EOEditingContext class specification in the EOControl framework.

__See also:__
[- `setDBSnapshot:`](#apple-gi3dqmi), [- `setDatabaseOperator:`](#apple-gmydm)

---

### entity

- (EOEntity \*)`entity`

Returns the entity that corresponds to the receiver's enterprise object.

__See also:__
[- `initWithGlobalID:object:entity:`](#apple-gy3tkmy)

---

### globalID

- (EOGlobalID \*)`globalID`

Returns the EOGlobalID object that corresponds to the receiver's enterprise object.

---

### initWithGlobalID:object:entity:

- `initWithGlobalID:`(EOGlobalID \*)_globalID_ `object:`(id)_object_ `entity:`(EOEntity \*)_entity_

The designated initializer, this method initializes a new EODatabaseOperation instance. Sets the enterprise object to which the operation will be applied, the object's global ID, and the object's entity. Returns `self`.

__See also:__
[- `object`](#apple-gi4dm), [- `entity`](#apple-gi3ds)

---

### newRow

- (NSMutableDictionary \*)`newRow`

Returns a dictionary representation of the receiver's enterprise object. In addition to all the properties of the enterprise object that are stored in the database, the dictionary contains values for the non-derived attribute's of the enterprise object's entity that aren't visible in the enterprise object. For example, primary and foreign keys aren't ordinarily properties of an enterprise object but are attributes of the object's entity.

The `newRow` dictionary is initialized with the values in the receiver's snapshot. New or updated values are added to the `newRow` dictionary (replacing out-of-date values) as the Framework maps changes in the object to an operation.

__See also:__
[- `setNewRow:`](#apple-gmyta)

---

### object

- (id)`object`

Returns the receiver's enterprise object.

---

### primaryKeyDiffs

- (NSDictionary \*)`primaryKeyDiffs`

__See also:__
Returns a dictionary that contains any primary key values in [`newRow`](#apple-gi4dc) that are different from
those in the [`dbSnapshot`](#apple-gi3dk). Returns `nil` if the receiver doesn't have EODatabaseUpdateOperator
set as its database operator.[- `setDatabaseOperator:`](#apple-gmydm), [- `newRow`](#apple-gi4dc)

---

### recordToManySnapshot:relationshipName:

- (void)`recordToManySnapshot:`(NSArray \*)_globalIDs_ `relationshipName:`(NSString \*)_name_

Records the objects in _globalIDs_. _globalIDs_ is an array of the globalIDs that identify the objects at the destination of the to-many relationship named _name_; _name_ is a property of the receiver's enterprise object.

__See also:__
[- `toManySnapshots`](#apple-g4ydgma)

---

### removeAdaptorOperation:

- (void)`removeAdaptorOperation:`(EOAdaptorOperation \*)_adaptorOperation_

Removes _adaptorOperation_ from the receiver's list of adaptor operations.

__See also:__
[- `adaptorOperations`](#apple-giztkna), [- `addAdaptorOperation:`](#apple-gi2to)

---

### rowDiffs

- (NSDictionary \*)`rowDiffs`

Returns values in the receiver's [`newRow`](#apple-gi4dc) dictionary that are different than the corresponding values in its [`dbSnapshot`](#apple-gi3dk). The dictionary returned from this method contains the new values from the enterprise object.

__See also:__
[- `primaryKeyDiffs`](#apple-giytamy)

---

### rowDiffsForAttributes:

- (NSDictionary \*)`rowDiffsForAttributes:`(NSArray \*)_attributes_

For the EOAttribute objects in _attributes_, this method returns values in the receiver's [`newRow`](#apple-gi4dc) dictionary that are different than the corresponding values in its [`dbSnapshot`](#apple-gi3dk). The dictionary returned contains the new values from the enterprise object.

---

### setDatabaseOperator:

- (void)`setDatabaseOperator:`(EODatabaseOperator)_databaseOperator_

Sets the receiver's database operator. _databaseOperator_ can be one of the following:

- EODatabaseNothingOperator
- EODatabaseInsertOperator
- EODatabaseUpdateOperator
- EODatabaseDeleteOperator

__See also:__
[- `databaseOperator`](#apple-gi3dc)

---

### setDBSnapshot:

- (void)`setDBSnapshot:`(NSDictionary \*)_dbSnapshot_

Sets the snapshot for the receiver's enterprise object. If the object has just been inserted into an an EOEditingContext, it won't have a snapshot. In this case, _dbSnapshot_ should be an empty dictionary.

__See also:__
[- `dbSnapshot`](#apple-gi3dk)

---

### setNewRow:

- (void)`setNewRow:`(NSMutableDictionary \*)_newRow_

Sets the dictionary representation of the receiver's enterprise object. _newRow_ should contain values for all the properties of the enterprise object that are stored in the database and for the non-derived attribute's of the enterprise object's entity that aren't visible in the enterprise object.

__See also:__
[- `newRow`](#apple-gi4dc), [- `databaseOperator`](#apple-gi3dc)

---

### toManySnapshots

- (NSDictionary \*)`toManySnapshots`

Returns the NSDictionary containing the snapshots for the to-many relationships of the receiver's enterprise object.

__See also:__
[- `recordToManySnapshot:relationshipName:`](#apple-gy4dqni)

---

[!](EODatabaseDataSource-2.md)
[!](EOEntity-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
