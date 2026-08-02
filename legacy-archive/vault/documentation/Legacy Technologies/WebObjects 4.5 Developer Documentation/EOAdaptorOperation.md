---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOAdaptorOperation.html
archived_at: '2026-07-15T08:11:31.579378Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOAdaptorOperation

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

An EOAdaptorOperation object represents a primitive operation
in a database server-lock, insert, update, or delete a row; or
execute a stored procedure-and all the necessary information required
by the operation. An EOAdaptorOperation is processed by an EOAdaptorChannel
object in the method [performAdaptorOperation](EOAdaptorChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw4).
You don't ordinarily create instances of EOAdaptorOperation; rather,
the Framework automatically creates an EOAdaptorOperation object
and sends it to an adaptor channel when your application needs the
database server to perform an operation. You generally interact
with EOAdaptorOperation objects only if you need to specify the
order in which a set of operations are carried out (see the description
for the EODatabaseContext delegate method databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:).

An EOAdaptorOperation has an entity and an operator (the type
of operation the object represents). An adaptor operation's operator
(`AdaptorLockOperator`, `AdaptorInsertOperator`, `AdaptorUpdateOperator`, `AdaptorDeleteOperator`,
or `AdaptorStoredProcedureOperator`)
determines additional, operator-dependent information used by the
EOAdaptorOperation object. For example, only a stored procedure
operation has an EOStoredProcedure object. The operator-dependent
information is accessible using the methods described below.

## Method Types

---

> **Constructors**
> : [EOAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxukt2bmrqxa5dpojhxazlsmf2gs33o)
>
> **Accessing the entity**
> : [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwk3tunf2hs)
>
> **Accessing the operator**
> : [setAdaptorOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxgzluifsgc4dun5ze64dfojqxi33s)
> : [adaptorOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwczdbob2g64spobsxeylun5za)
>
> **Accessing the qualifier**
> : [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxgzlukf2wc3djmzuwk4q)
> : [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxc5lbnruwm2lfoi)
>
> **Accessing locking attributes**
> : [setAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxgzluif2hi4tjmj2xizlt)
> : [attributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwc5duojuwe5lumvzq)
>
> **Accessing operation values**
> : [setChangedValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxgzluinugc3thmvsfmylmovsxg)
> : [changedValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwg2dbnztwkzcwmfwhkzlt)
>
> **Accessing a stored procedure**
> : [setStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxgzlukn2g64tfmrihe33dmvshk4tf)
> : [storedProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxg5dpojswiudsn5rwkzdvojsq)
>
> **Handling errors during
> the operation**
> : [setException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxgzluiv4ggzlqoruw63q)
> : [exception](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwk6ddmvyhi2lpny)
>
> **Comparing operations**
> : [compareAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwg33nobqxezkbmrqxa5dpojhxazlsmf2gs33o)

## Constructors

---

### EOAdaptorOperation

`public EOAdaptorOperation(EOEntity entity)`

Creates and returns a new EOAdaptorOperation,
with _entity_ as the entity to which
the operation will be applied.

__See Also:__  [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwk3tunf2hs)

---

## Instance Methods

---

### adaptorOperator

`public int adaptorOperator()`

Returns the receiver's adaptor operator. The
operator indicates which of the other adaptor operation attributes
are valid. For example, an adaptor operation whose operator is `AdaptorInsertOperator` uses [changedValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwg2dbnztwkzcwmfwhkzlt), but
not [attributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxwc5duojuwe5lumvzq), [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxc5lbnruwm2lfoi), or [storedProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5ze64dfojqxi2lpnyxxg5dpojswiudsn5rwkzdvojsq).

---

### attributes

`public NSArray attributes()`

Returns the array of attributes to select when
locking the row. If attributes have not been assigned to the receiver,
the primary key attributes are selected. Only valid for adaptor
operations with the `AdaptorLockOperator`.

---

### changedValues

`public NSDictionary changedValues()`

Returns the dictionary of values that need to
be updated, inserted, or compared for locking purposes.

---

### compareAdaptorOperation

`public int compareAdaptorOperation(EOAdaptorOperation operation)`

Orders adaptor operations alphabetically by
entity name and by adaptor operator within the same entity. The
adaptor operators are ordered as follows:

- `AdaptorLockOperator`
- `AdaptorInsertOperator`
- `AdaptorUpdateOperator`
- `AdaptorDeleteOperator`
- `AdaptorStoredProcedureOperator`

`AdaptorLockOperator` precedes `AdaptorInsertOperator`, `AdaptorInsertOperator` precedes `AdaptorUpdateOperator`,
and so on.

An EODatabaseContext uses __compareAdaptorOperation:__ to
order adaptor operations before invoking EOAdaptorChannel's [performAdaptorOperations](EOAdaptorChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw44y) method.

---

### entity

`public EOEntity entity()`

Returns the entity to which the operation will
be applied.

---

### exception

`public Throwable exception()`

Returns the exception that was thrown when an
adaptor channel attempted to process the receiver. Returns null if
no exception was thrown or if the receiver hasn't been processed
yet.

---

### qualifier

`public com.apple.yellow.eocontrol.EOQualifier qualifier()`

Returns the qualifier that identifies the specific
row to which the operation applies. Not valid with adaptor operations
with the operators `AdaptorInsertOperator` and `AdaptorStoredProcedureOperator`.

---

### setAdaptorOperator

`public void setAdaptorOperator(int adaptorOperator)`

Sets the receiver's operator to _adaptorOperator_,
which is one of the following:

- `AdaptorLockOperator`
- `AdaptorInsertOperator`
- `AdaptorUpdateOperator`
- `AdaptorDeleteOperator`
- `AdaptorStoredProcedureOperator`

For
more information, see the discussion on adaptor operators in the
class description above.

---

### setAttributes

`public void setAttributes(NSArray attributes)`

Sets the array of attributes to select when
locking the row. The selected values are compared in memory to the
corresponding snapshot values to determine if a row has changed
since the application last fetched it. _attributes_ is
an array of EOAttribute objects that can't be compared in a qualifier
(generally BLOB types); it should not be null or empty. Generally,
an adaptor operation's qualifier contains all the comparisons
needed to verify that a row hasn't changed since the application
last fetched, inserted, or updated it. In this case (if there aren't
any attributes that can't be compared in a qualifier), attributes should
contain primary key attributes. This method is only valid for adaptor
operations with the `AdaptorLockOperator`.

---

### setChangedValues

`public void setChangedValues(NSDictionary changedValues)`

Sets the dictionary of values that need to be
updated, inserted, or compared for locking purposes. changedValues
is a dictionary object whose keys are attribute names and whose
values are the values for those attributes. As summarized in the
following table, the contents of changedValues depends on the receiver's
operator:

|  |  |
| --- | --- |
| __Operator__ | __Contents of changedValues Dictionary__ |
| `AdaptorLockOperator` | Snapshot values used to verify that the database row hasn't changed since this application last fetched it |
| `AdaptorInsertOperator` | The values to insert |
| `AdaptorUpdateOperator` | The new values for the columns to update |
| `AdaptorDeleteOperator` | Snapshot values (_changedValues_ is only valid for `AdaptorDeleteOperator` if the receiver's entity uses a stored procedure to perform delete operations.) |
| `AdaptorStoredProcedureOperator` | Snapshot values |

---

### setException

`public void setException(Throwable exception)`

Sets the receiver's exception to _exception_.
This method is typically invoked from EOAdaptorChannel's [performAdaptorOperations](EOAdaptorChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw44y) method.
If a database error occurs while processing an adaptor operation, the
adaptor channel creates an exception and assigns it to the adaptor
operation.

---

### setQualifier

`public void setQualifier(com.apple.yellow.eocontrol.EOQualifier qualifier)`

Sets the qualifier that identifies the row to
which the adaptor operation is to be applied to _qualifier_.

---

###

setStoredProcedure

`public void setStoredProcedure(EOStoredProcedure storedProcedure)`

Sets the receiver's stored procedure to _storedProcedure_.

---

### storedProcedure

`public EOStoredProcedure storedProcedure()`

Returns the receiver's stored procedure. Only
valid with adaptor operations with the `AdaptorStoredProcedureOperator`.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
