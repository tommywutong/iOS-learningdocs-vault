---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EODatabaseOperation.html
archived_at: '2026-07-15T08:11:31.759368Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EODatabaseOperation

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.eoaccess

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
for the EODatabaseContext delegate method [databaseContextWillOrderAdaptorOperations](EODatabaseContext.Delegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirqxiylcmfzwkq3pnz2gk6dufzcgk3dfm5qxizjpmrqxiylcmfzwkq3pnz2gk6duk5uwy3cpojsgk4sbmrqxa5dpojhxazlsmf2gs33oom)).

An EODatabaseOperation specifies an enterprise object (called
"object") on which the operation is performed, the EOGlobalID
for the object, and the object's entity. In addition, the database
operation has a snapshot containing the last known database values
for the object and a __newRow__ dictionary
of new or updated values to save in the database.

## Constants

---

EODatabaseOperation defines the following `int` constants
to identify the primitive database operation represented by an EOAdaptorOperation
object or an EODatabaseOperation object:

|  |  |
| --- | --- |
| __EOAdaptorOperation Operators__ | __EODatabaseOperation Operators__ |
| AdaptorLockOperator | DatabaseNothingOperator |
| AdaptorInsertOperator | DatabaseInsertOperator |
| AdaptorUpdateOperator | DatabaseUpdateOperator |
| AdaptorDeleteOperator | DatabaseDeleteOperator |
| AdaptorStoredProcedureOperator |  |

## Method Types

---

> **Constructors**
> : [EODatabaseOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6rkpirqxiylcmfzwkt3qmvzgc5djn5xa)
>
> **Accessing the global
> ID object**
> : [globalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6z3mn5rgc3cjiq)
>
> **Accessing the object**
> : [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc633cnjswg5a)
>
> **Accessing the entity**
> : [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6zlooruxi6i)
>
> **Accessing the operator**
> : [setDatabaseOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc643forcgc5dbmjqxgzkpobsxeylun5za)
> : [databaseOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6zdborqweyltmvhxazlsmf2g64q)
>
> **Accessing the database
> snapshot**
> : [setDBSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc643forceeu3omfyhg2dpoq)
> : [dbSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6zdcknxgc4dtnbxxi)
>
> **Accessing the row**
> : [setNewRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc643forhgk52sn53q)
> : [newRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc63tfo5jg65y)
>
> **Accessing the adaptor
> operations**
> : [addAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6ylemrawiylqorxxet3qmvzgc5djn5xa)
> : [removeAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc64tfnvxxmzkbmrqxa5dpojhxazlsmf2gs33o)
> : [adaptorOperations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6ylemfyhi33sj5ygk4tboruw63tt)
>
> **Comparing new row and
> snapshot values**
> : [rowDiffs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc64tpo5cgsztgom)
> : [rowDiffsForAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc64tpo5cgsztgondg64sbor2he2lcov2gk4y)
>
> **Working with to-many
> snapshots**
> : [recordToManySnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc64tfmnxxezcun5gwc3tzknxgc4dtnbxxi)
> : [toManySnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc65dpjvqw46ktnzqxa43in52hg)

## Constructors

---

### EODatabaseOperation

`public EODatabaseOperation(
com.apple.yellow.eocontrol.EOGlobalID aGlobalID,
Object anObject,
EOEntity anEntity)`

Creates and returns a new EODatabaseOperation
object, setting the [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc633cnjswg5a) to
which the operation will be applied to _anObject_, [globalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6z3mn5rgc3cjiq) to _aGlobalID_,
and [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6zlooruxi6i) to _anEntity_.

---

## Instance Methods

---

### adaptorOperations

`public NSArray adaptorOperations()`

Returns the EOAdaptorOperation objects that
need to be performed to carry out the operation represented by the
receiver.

__See Also:__  [addAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6ylemrawiylqorxxet3qmvzgc5djn5xa), [removeAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc64tfnvxxmzkbmrqxa5dpojhxazlsmf2gs33o)

---

### addAdaptorOperation

`public void addAdaptorOperation(EOAdaptorOperation adaptorOperation)`

Adds _adaptorOperation_ to
the receiver's list of adaptor operations. Throws an exception
if _adaptorOperation_ is null.

__See
Also:__  [adaptorOperations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6ylemfyhi33sj5ygk4tboruw63tt), [removeAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc64tfnvxxmzkbmrqxa5dpojhxazlsmf2gs33o)

---

### databaseOperator

`public int databaseOperator()`

Returns the receiver's database operator.

---

### dbSnapshot

`public NSDictionary dbSnapshot()`

Returns the database snapshot for the receiver's
enterprise object. The snapshot contains the last known database
values for the enterpriseobject. The dictionary
returned from this method will be empty if the receiver's object
has just been inserted into an EOEditingContext and has not yet
been saved in persistent storage. For more information on EOEditingContexts,
see the EOEditingContext class specification in the EOControl framework.

__See
Also:__  [setDatabaseOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc643forcgc5dbmjqxgzkpobsxeylun5za)

---

### entity

`public EOEntity entity()`

Returns the entity that corresponds to the receiver's
enterprise object.

__See Also:__  [EODatabaseOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6rkpirqxiylcmfzwkt3qmvzgc5djn5xa)

---

### globalID

`public com.apple.yellow.eocontrol.EOGlobalID globalID()`

Returns the EOGlobalID object that corresponds
to the receiver's enterprise object.

__See
Also:__  [EODatabaseOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6rkpirqxiylcmfzwkt3qmvzgc5djn5xa)

---

### newRow

`public NSMutableDictionary newRow()`

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

`public Object object()`

Returns the receiver's enterprise object.

__See
Also:__  [EODatabaseOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6rkpirqxiylcmfzwkt3qmvzgc5djn5xa)

---

### primaryKeyDiffs

`public NSDictionary primaryKeyDiffs()`

Returns a dictionary that contains any primary
key values in [newRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc63tfo5jg65y) that
are different from those in the [dbSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6zdcknxgc4dtnbxxi). Returns null if the receiver
doesn't have EODatabaseUpdateOperator set as its database operator.

__See
Also:__  [setDatabaseOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc643forcgc5dbmjqxgzkpobsxeylun5za), [newRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc63tfo5jg65y)

---

### recordToManySnapshot

`public void recordToManySnapshot(
NSArray globalIDs,
String name)`

Records the objects in _globalIDs_. _globalIDs_ is
an array of the globalIDs that identify the objects at the destination
of the to-many relationship named _name_; _name_ is
a property of the receiver's enterprise object.

__See
Also:__  [toManySnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc65dpjvqw46ktnzqxa43in52hg)

---

### removeAdaptorOperation

`public void removeAdaptorOperation(EOAdaptorOperation adaptorOperation)`

Removes _adaptorOperation_ from
the receiver's list of adaptor operations.

__See
Also:__  [adaptorOperations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6ylemfyhi33sj5ygk4tboruw63tt), [addAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6ylemrawiylqorxxet3qmvzgc5djn5xa)

---

### rowDiffs

`public NSDictionary rowDiffs()`

Returns values in the receiver's [newRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc63tfo5jg65y) dictionary
that are different than the corresponding values in its [dbSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6zdcknxgc4dtnbxxi). The
dictionary returned from this method contains the new values from
the enterprise object.

__See Also:__  [primaryKeyDiffs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc64dsnfwwc4tzjnsxsrdjmzthg)

---

### rowDiffsForAttributes

`public NSDictionary rowDiffsForAttributes(NSArray attributes)`

For the EOAttribute objects in _attributes_,
this method returns values in the receiver's [newRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc63tfo5jg65y) dictionary that are different
than the corresponding values in its [dbSnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6zdcknxgc4dtnbxxi). The dictionary returned
contains the new values from the enterprise object.

---

### setDatabaseOperator

`public void setDatabaseOperator(int databaseOperator)`

Sets the receiver's database operator. _databaseOperator_ can
be one of the following:

- DatabaseNothingOperator
- DatabaseInsertOperator
- DatabaseUpdateOperator
- DatabaseDeleteOperator

---

### setDBSnapshot

`public void setDBSnapshot(NSDictionary dbSnapshot)`

Sets the snapshot for the receiver's enterprise
object. If the object has just been inserted into an an EOEditingContext
(EOControl), it won't have a snapshot. In this case, _dbSnapshot_ should
be an empty dictionary.

---

### setNewRow

`public void setNewRow(NSMutableDictionary newRow)`

Sets the dictionary representation of the receiver's
enterprise object. _newRow_ should
contain values for all the properties of the enterprise object that
are stored in the database and for the non-derived attribute's
of the enterprise object's entity that aren't visible in the
enterprise object.

__See Also:__  [databaseOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc6zdborqweyltmvhxazlsmf2g64q)

---

### toManySnapshots

`public NSDictionary toManySnapshots()`

Returns the NSDictionary containing the snapshots
for the to-many relationships of the receiver's enterprise object.

__See
Also:__  [recordToManySnapshot](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkt3qmvzgc5djn5xc64tfmnxxezcun5gwc3tzknxgc4dtnbxxi)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
