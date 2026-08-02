---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOAdaptorOperation.html
archived_at: '2026-07-15T08:11:33.405461Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOAdaptorOperation

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EODatabaseOperation.h

---

## Class Description

---

An EOAdaptorOperation object represents a primitive operation
in a database server-lock, insert, update, or delete a row; or
execute a stored procedure-and all the necessary information required
by the operation. An EOAdaptorOperation is processed by an EOAdaptorChannel
object in the method [performAdaptorOperation:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xdu).
You don't ordinarily create instances of EOAdaptorOperation; rather,
the Framework automatically creates an EOAdaptorOperation object
and sends it to an adaptor channel when your application needs the
database server to perform an operation. You generally interact
with EOAdaptorOperation objects only if you need to specify the
order in which a set of operations are carried out (see the description
for the EODatabaseContext delegate method databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:).

An EOAdaptorOperation has an entity and an operator (the type
of operation the object represents). An adaptor operation's operator
(`EOAdaptorLockOperator`, `EOAdaptorInsertOperator`, `EOAdaptorUpdateOperator`, `EOAdaptorDeleteOperator`,
or `EOAdaptorStoredProcedureOperator`)
determines additional, operator-dependent information used by the
EOAdaptorOperation object. For example, only a stored procedure
operation has an EOStoredProcedure object. The operator-dependent information
is accessible using the methods described below.

## Method Types

---

> **Creating a new EOAdaptorOperation**
> : [- initWithEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5uw42luk5uxi2cfnz2gs5dzhi)
>
> **Accessing the entity**
> : [- entity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5sw45djor4q)
>
> **Accessing the operator**
> : [- setAdaptorOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5zwk5cbmrqxa5dpojhxazlsmf2g64r2)
> : [- adaptorOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5qwiylqorxxet3qmvzgc5dpoi)
>
> **Accessing the qualifier**
> : [- setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5zwk5crovqwy2lgnfsxeoq)
> : [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5yxkylmnftgszls)
>
> **Accessing locking attributes**
> : [- setAttributes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5zwk5cbor2he2lcov2gk4z2)
> : [- attributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5qxi5dsnfrhk5dfom)
>
> **Accessing operation values**
> : [- setChangedValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5zwk5cdnbqw4z3fmrlgc3dvmvztu)
> : [- changedValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5rwqylom5swivtbnr2wk4y)
>
> **Accessing a stored procedure**
> : [- setStoredProcedure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5zwk5ctorxxezlekbzg6y3fmr2xezj2)
> : [- storedProcedure](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5zxi33smvsfa4tpmnswi5lsmu)
>
> **Handling errors during
> the operation**
> : [- setException:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5zwk5cfpbrwk4dunfxw4oq)
> : [- exception](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5sxqy3fob2gs33o)
>
> **Comparing operations**
> : [- compareAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5rw63lqmfzgkqlemfyhi33sj5ygk4tboruw63r2)

## Instance Methods

---

### adaptorOperator

`- (EOAdaptorOperator)adaptorOperator`

Returns the receiver's adaptor operator. The
operator indicates which of the other adaptor operation attributes
are valid. For example, an adaptor operation whose operator is `EOAdaptorInsertOperator` uses [changedValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5rwqylom5swivtbnr2wk4y), but
not [attributes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5qxi5dsnfrhk5dfom), [qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5yxkylmnftgszls), or [storedProcedure](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5zxi33smvsfa4tpmnswi5lsmu).

---

### attributes

`- (NSArray *)attributes`

Returns the array of attributes to select when
locking the row. If attributes have not been assigned to the receiver,
the primary key attributes are selected. Only valid for adaptor
operations with the `EOAdaptorLockOperator`.

---

### changedValues

`- (NSDictionary *)changedValues`

Returns the dictionary of values that need to
be updated, inserted, or compared for locking purposes.

---

### compareAdaptorOperation:

`- (NSComparisonResult)compareAdaptorOperation:(EOAdaptorOperation
*)operation`

Orders adaptor operations alphabetically by
entity name and by adaptor operator within the same entity. The
adaptor operators are ordered as follows:

- `EOAdaptorLockOperator`
- `EOAdaptorInsertOperator`
- `EOAdaptorUpdateOperator`
- `EOAdaptorDeleteOperator`
- `EOAdaptorStoredProcedureOperator`

`EOAdaptorLockOperator` precedes `EOAdaptorInsertOperator`, `EOAdaptorInsertOperator` precedes `EOAdaptorUpdateOperator`,
and so on.

An EODatabaseContext uses __compareAdaptorOperation:__ to
order adaptor operations before invoking EOAdaptorChannel's [performAdaptorOperations:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq) method.

---

### entity

`- (EOEntity *)entity`

Returns the entity to which the operation will
be applied.

__See Also:__  [- initWithEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5uw42luk5uxi2cfnz2gs5dzhi)

---

### exception

`- (NSException *)exception`

Returns the exception that was raised when an
adaptor channel attempted to process the receiver. Returns nil if
no exception was raised or if the receiver hasn't been processed
yet.

---

### qualifier

`- (EOQualifier *)qualifier`

Returns the qualifier that identifies the specific
row to which the operation applies. Not valid with adaptor operations
with the operators `EOAdaptorInsertOperator` and `EOAdaptorStoredProcedureOperator`.

---

### initWithEntity:

`- initWithEntity:(EOEntity
*)entity`

The designated initializer, initializes a new
EOAdaptorOperation instance, and sets the entity to which the operation
will be applied. Returns __self__.

__See
Also:__  [- entity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojhxazlsmf2gs33of5sw45djor4q)

---

### setAdaptorOperator:

`- (void)setAdaptorOperator:(EOAdaptorOperator)adaptorOperator`

Sets the receiver's operator to _adaptorOperator_,
which is one of the following:

- `EOAdaptorLockOperator`
- `EOAdaptorInsertOperator`
- `EOAdaptorUpdateOperator`
- `EOAdaptorDeleteOperator`
- `EOAdaptorStoredProcedureOperator`

For
more information, see the discussion on adaptor operators in the
class description above.

---

### setAttributes:

`- (void)setAttributes:(NSArray
*)attributes`

Sets the array of attributes to select when
locking the row. The selected values are compared in memory to the
corresponding snapshot values to determine if a row has changed
since the application last fetched it. _attributes_ is
an array of EOAttribute objects that can't be compared in a qualifier
(generally BLOB types); it should not be nil or empty. Generally,
an adaptor operation's qualifier contains all the comparisons
needed to verify that a row hasn't changed since the application
last fetched, inserted, or updated it. In this case (if there aren't
any attributes that can't be compared in a qualifier), attributes should
contain primary key attributes. This method is only valid for adaptor
operations with the `EOAdaptorLockOperator`.

---

### setChangedValues:

`- (void)setChangedValues:(NSDictionary
*)changedValues`

Sets the dictionary of values that need to be
updated, inserted, or compared for locking purposes. changedValues
is a dictionary object whose keys are attribute names and whose
values are the values for those attributes. As summarized in the
following table, the contents of changedValues depends on the receiver's
operator:

|  |  |
| --- | --- |
| __Operator__ | __Contents of changedValues Dictionary__ |
| `EOAdaptorLockOperator` | Snapshot values used to verify that the database row hasn't changed since this application last fetched it |
| `EOAdaptorInsertOperator` | The values to insert |
| `EOAdaptorUpdateOperator` | The new values for the columns to update |
| `EOAdaptorDeleteOperator` | Snapshot values (_changedValues_ is only valid for `EOAdaptorDeleteOperator` if the receiver's entity uses a stored procedure to perform delete operations.) |
| `EOAdaptorStoredProcedureOperator` | Snapshot values |

---

### setException:

`- (void)setException:(NSException
*)exception`

Sets the receiver's exception to _exception_.
This method is typically invoked from EOAdaptorChannel's [performAdaptorOperations:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq) method.
If a database error occurs while processing an adaptor operation, the
adaptor channel creates an exception and assigns it to the adaptor
operation.

---

### setQualifier:

`- (void)setQualifier:(EOQualifier
*)qualifier`

Sets the qualifier that identifies the row to
which the adaptor operation is to be applied to _qualifier_.

---

###

setStoredProcedure:

`- (void)setStoredProcedure:(EOStoredProcedure
*)storedProcedure`

Sets the receiver's stored procedure to _storedProcedure_.

---

### storedProcedure

`- (EOStoredProcedure *)storedProcedure`

Returns the receiver's stored procedure. Only
valid with adaptor operations with the `EOAdaptorStoredProcedureOperator`.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
