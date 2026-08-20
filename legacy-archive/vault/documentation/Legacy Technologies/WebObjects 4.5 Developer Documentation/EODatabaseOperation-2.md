---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EODatabaseOperation.html
archived_at: '2026-07-15T08:11:33.569498Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EODatabaseOperation

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EODatabaseOperation.h

---

## Class Description

---

An EODatabaseOperation object represents an operation-insert,
update, or delete-to perform on an enterprise object and all the
necessary information required to perform the operation. You don't ordinarily
create instances of EODatabaseOperation; rather, the Framework automatically
creates an EODatabaseOperation object for each new, updated, or
deleted object in an EOEditingContext. An EODatabaseContext object
analyzes a set of database operations and maps each operation to
one or more adaptor operations. The adaptor operations are then
performed by an EOAdaptorChannel object. You generally interact
with EODatabaseOperation objects only if you need to specify the
order in which a set of operations are carried out (see the description
for the EODatabaseContext delegate method [databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2o5uwy3cpojsgk4sbmrqxa5dpojhxazlsmf2gs33oondhe33nirqxiylcmfzwkt3qmvzgc5djn5xhgoq)).

An EODatabaseOperation specifies an enterprise object (called
"object") on which the operation is performed, the EOGlobalID
for the object, and the object's entity. In addition, the database
operation has a snapshot containing the last known database values
for the object and a __newRow__ dictionary
of new or updated values to save in the database.

## Constants

---

In EODatabaseOperation.h, EOAccess defines
two enumeration types, `EOAdaptorOperator` and `EODatabaseOperator`,
to identify the primitive database operation represented by an EOAdaptorOperation
object or an EODatabaseOperation object. Their constants are:

|  |  |
| --- | --- |
| __EOAdaptorOperation Operators__ | __EODatabaseOperation Operators__ |
| EOAdaptorLockOperator | EODatabaseNothingOperator |
| EOAdaptorInsertOperator | EODatabaseInsertOperator |
| EOAdaptorUpdateOperator | EODatabaseUpdateOperator |
| EOAdaptorDeleteOperator | EODatabaseDeleteOperator |
| EOAdaptorStoredProcedureOperator |  |

## Method Types

---

> **Creating a new EODatabaseOperation**
> : [- initWithGlobalID:object:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxws3tjorlws5dii5wg6ytbnreuiotpmjvgky3uhjsw45djor4tu)
>
> **Accessing the global
> ID object**
> : [- globalID](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwo3dpmjqwyske)
>
> **Accessing the object**
> : [- object](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxw6ytkmvrxi)
>
> **Accessing the entity**
> : [- entity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwk3tunf2hs)
>
> **Accessing the operator**
> : [- setDatabaseOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxgzluirqxiylcmfzwkt3qmvzgc5dpoi5a)
> : [- databaseOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwiylumfrgc43fj5ygk4tborxxe)
>
> **Accessing the database
> snapshot**
> : [- setDBSnapshot:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxgzluirbfg3tbobzwq33uhi)
> : [- dbSnapshot](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwiystnzqxa43in52a)
>
> **Accessing the row**
> : [- setNewRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxgzlujzsxoutpo45a)
> : [- newRow](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxw4zlxkjxxo)
>
> **Accessing the adaptor
> operations**
> : [- addAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwczdeifsgc4dun5ze64dfojqxi2lpny5a)
> : [- removeAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxezlnn53gkqlemfyhi33sj5ygk4tboruw63r2)
> : [- adaptorOperations](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwczdbob2g64spobsxeylunfxw44y)
>
> **Comparing new row and
> snapshot values**
> : [- rowDiffs](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxe33xiruwmztt)
> : [- rowDiffsForAttributes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxe33xiruwmzttizxxeqluorzgsytvorsxgoq)
>
> **Working with to-many
> snapshots**
> : [- recordToManySnapshot:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxezldn5zgivdpjvqw46ktnzqxa43in52du4tfnrqxi2lpnzzwq2lqjzqw2zj2)
> : [- toManySnapshots](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxi32nmfxhsu3omfyhg2dporzq)

## Instance Methods

---

### adaptorOperations

`- (NSArray *)adaptorOperations`

Returns the EOAdaptorOperation objects that
need to be performed to carry out the operation represented by the
receiver.

__See Also:__  [- addAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwczdeifsgc4dun5ze64dfojqxi2lpny5a), [- removeAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxezlnn53gkqlemfyhi33sj5ygk4tboruw63r2)

---

### addAdaptorOperation:

`- (void)addAdaptorOperation:(EOAdaptorOperation
*)adaptorOperation`

Adds _adaptorOperation_ to
the receiver's list of adaptor operations. Raises an exception
if _adaptorOperation_ is nil.

__See
Also:__  [- adaptorOperations](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwczdbob2g64spobsxeylunfxw44y), [- removeAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxezlnn53gkqlemfyhi33sj5ygk4tboruw63r2)

---

### databaseOperator

`- (EODatabaseOperator)databaseOperator`

Returns the receiver's database operator.

---

### dbSnapshot

`- (NSDictionary *)dbSnapshot`

Returns the database snapshot for the receiver's
enterprise object. The snapshot contains the last known database
values for the enterpriseobject. The dictionary
returned from this method will be empty if the receiver's object
has just been inserted into an EOEditingContext and has not yet
been saved in persistent storage. For more information on EOEditingContexts,
see the EOEditingContext class specification in the EOControl framework.

__See
Also:__  [- setDatabaseOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxgzluirqxiylcmfzwkt3qmvzgc5dpoi5a)

---

### entity

`- (EOEntity *)entity`

Returns the entity that corresponds to the receiver's
enterprise object.

__See Also:__  [- initWithGlobalID:object:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxws3tjorlws5dii5wg6ytbnreuiotpmjvgky3uhjsw45djor4tu)

---

### globalID

`- (EOGlobalID *)globalID`

Returns the EOGlobalID object that corresponds
to the receiver's enterprise object.

__See
Also:__  [- initWithGlobalID:object:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxws3tjorlws5dii5wg6ytbnreuiotpmjvgky3uhjsw45djor4tu)

---

### initWithGlobalID:object:entity:

`- initWithGlobalID:(EOGlobalID
*)globalID object:(id)object
entity:(EOEntity *)entity`

The designated initializer, this method initializes
a new EODatabaseOperation instance. Sets the enterprise object to
which the operation will be applied, the object's global ID, and
the object's entity. Returns __self__.

__See
Also:__  [- object](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxw6ytkmvrxi), [- entity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwk3tunf2hs)

---

### newRow

`- (NSMutableDictionary *)newRow`

Returns a dictionary representation of the receiver's
enterprise object. In addition to all the properties of the enterprise
object that are stored in the database, the dictionary contains
values for the non-derived attribute's of the enterprise object's
entity that aren't visible in the enterprise object. For example,
primary and foreign keys aren't ordinarily properties of an enterprise
object but are attributes of the object's entity.

The __newRow__ dictionary
is initialized with the values in the receiver's snapshot. New
or updated values are added to the __newRow__ dictionary
(replacing out-of-date values) as the Framework maps changes in the
object to an operation.

---

### object

`- (id)object`

Returns the receiver's enterprise object.

__See
Also:__  [- initWithGlobalID:object:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxws3tjorlws5dii5wg6ytbnreuiotpmjvgky3uhjsw45djor4tu)

---

### primaryKeyDiffs

`- (NSDictionary *)primaryKeyDiffs`

Returns a dictionary that contains any primary
key values in [newRow](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxw4zlxkjxxo) that
are different from those in the [dbSnapshot](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwiystnzqxa43in52a). Returns nil if the receiver
doesn't have EODatabaseUpdateOperator set as its database operator.

__See
Also:__  [- setDatabaseOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxgzluirqxiylcmfzwkt3qmvzgc5dpoi5a), [- newRow](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxw4zlxkjxxo)

---

### recordToManySnapshot:relationshipName:

`- (void)recordToManySnapshot:(NSArray
*)globalIDs
relationshipName:(NSString *)name`

Records the objects in _globalIDs_. _globalIDs_ is
an array of the globalIDs that identify the objects at the destination
of the to-many relationship named _name_; _name_ is
a property of the receiver's enterprise object.

__See
Also:__  [- toManySnapshots](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxi32nmfxhsu3omfyhg2dporzq)

---

### removeAdaptorOperation:

`- (void)removeAdaptorOperation:(EOAdaptorOperation
*)adaptorOperation`

Removes _adaptorOperation_ from
the receiver's list of adaptor operations.

__See
Also:__  [- adaptorOperations](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwczdbob2g64spobsxeylunfxw44y), [- addAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwczdeifsgc4dun5ze64dfojqxi2lpny5a)

---

### rowDiffs

`- (NSDictionary *)rowDiffs`

Returns values in the receiver's [newRow](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxw4zlxkjxxo) dictionary
that are different than the corresponding values in its [dbSnapshot](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwiystnzqxa43in52a). The
dictionary returned from this method contains the new values from
the enterprise object.

__See Also:__  [- primaryKeyDiffs](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxa4tjnvqxe6klmv4ui2lgmzzq)

---

### rowDiffsForAttributes:

`- (NSDictionary *)rowDiffsForAttributes:(NSArray
*)attributes`

For the EOAttribute objects in _attributes_,
this method returns values in the receiver's [newRow](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxw4zlxkjxxo) dictionary that are different
than the corresponding values in its [dbSnapshot](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwiystnzqxa43in52a). The dictionary returned
contains the new values from the enterprise object.

---

### setDatabaseOperator:

`- (void)setDatabaseOperator:(EODatabaseOperator)databaseOperator`

Sets the receiver's database operator. _databaseOperator_ can
be one of the following:

- EODatabaseNothingOperator
- EODatabaseInsertOperator
- EODatabaseUpdateOperator
- EODatabaseDeleteOperator

---

### setDBSnapshot:

`- (void)setDBSnapshot:(NSDictionary
*)dbSnapshot`

Sets the snapshot for the receiver's enterprise
object. If the object has just been inserted into an an EOEditingContext
(EOControl), it won't have a snapshot. In this case, _dbSnapshot_ should
be an empty dictionary.

---

### setNewRow:

`- (void)setNewRow:(NSMutableDictionary
*)newRow`

Sets the dictionary representation of the receiver's
enterprise object. _newRow_ should
contain values for all the properties of the enterprise object that
are stored in the database and for the non-derived attribute's
of the enterprise object's entity that aren't visible in the
enterprise object.

__See Also:__  [- databaseOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxwiylumfrgc43fj5ygk4tborxxe)

---

### toManySnapshots

`- (NSDictionary *)toManySnapshots`

Returns the NSDictionary containing the snapshots
for the to-many relationships of the receiver's enterprise object.

__See
Also:__  [- recordToManySnapshot:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsu64dfojqxi2lpnyxxezldn5zgivdpjvqw46ktnzqxa43in52du4tfnrqxi2lpnzzwq2lqjzqw2zj2)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
