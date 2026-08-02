---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOUtilities.html
archived_at: '2026-07-15T08:11:32.052375Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOUtilities

> __Inherits
> from:__  Object

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

[EOUtilities](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom) is a collection of convenience
methods intended to make common operations with EOF easier. [EOUtilities](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom) is an EOAccess class that
consists entirely of static methods-you never instantiate an [EOUtilities](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom) object.

Each method requires an editing context into which the objects
should be fetched; this editing context is passed as the first argument
to each method in [EOUtilities](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom).

|  |
| --- |
| The Objective-C source code for EOUtilities is available as an example. On Mac OS X Server systems, see __/System/Developer/Examples/EnterpriseObjects/Sources/EOUtilities__. On NT, see $_NEXT_ROOT___\Developer\Examples\EnterpriseObjects\Sources\EOUtilities__. |

## Method Types

---

> **Creating new objects**
> : [createAndInsertInstance](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmnzgkylumvaw4zcjnzzwk4tujfxhg5dbnzrwk)
>
> **Fetching multiple objects**
> : [objectsForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzum33sivxhi2lupfhgc3lfmq)
> : [objectsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzvo2lunbixkylmnftgszlsizxxe3lboq)
> : [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thjnsxsqlomrlgc3dvmu)
> : [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thkzqwy5lfom)
> : [objectsOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu6zsdnrqxg4y)
> : [objectsWithFetchSpecificationAndBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63sbnzsee2lomruw4z3t)
>
> **Fetching single objects**
> : [objectWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5dikf2wc3djmzuwk4sgn5zg2ylu)
> : [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2lmv4uc3tekzqwy5lf)
> : [objectMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2wmfwhkzlt)
> : [objectWithFetchSpecificationAndBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5diizsxiy3iknygky3jmzuwgylunfxw4qlomrbgs3tenfxgo4y)
> : [objectWithPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5dikbzgs3lboj4uwzlz)
> : [objectWithPrimaryKeyValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5dikbzgs3lboj4uwzlzkzqwy5lf)
>
> **Fetching raw rows**
> : [executeStoredProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsu4ylnmvsa)
> : [objectFromRawRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldordhe33nkjqxoutpo4)
> : [rawRowsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zvo2lunbixkylmnftgszlsizxxe3lboq)
> : [rawRowsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zu2ylumnugs3thjnsxsqlomrlgc3dvmu)
> : [rawRowsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zu2ylumnugs3thkzqwy5lfom)
> : [rawRowsForSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zum33skniuy)
> : [rawRowsForStoredProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zum33skn2g64tfmrihe33dmvshk4tfjzqw2zle)
>
> **Accessing the EOF stack**
> : [connectWithModelNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmnxw43tfmn2fo2lunbgw6zdfnrhgc3lfmq)
> : [databaseContextForModelNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmrqxiylcmfzwkq3pnz2gk6duizxxetlpmrswyttbnvswi)
>
> **Accessing object data**
> : [destinationKeyForSourceObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmrsxg5djnzqxi2lpnzfwk6kgn5zfg33vojrwkt3cnjswg5a)
> : [localInstanceOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpnrxwgylmjfxhg5dbnzrwkt3gj5rguzldoq)
> : [localInstancesOfObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpnrxwgylmjfxhg5dbnzrwk42pmzhwe2tfmn2hg)
> : [primaryKeyForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpobzgs3lboj4uwzlzizxxet3cnjswg5a)
>
> **Accessing model information**
> : [entityForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfdg64sdnrqxg4y)
> : [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfdg64spmjvgky3u)
> : [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfhgc3lfmq)
> : [modelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpnvxwizlmi5zg65lq)

## Instance Methods

---

### connectWithModelNamed

`public static void connectWithModelNamed(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String modelName,
NSDictionary overrides)`

Connects to the database using the connection
information in the specified model and the provided overrides dictionary.
This method facilitates per-session database logins in WebObjects
applications. Typically, you'd put a login name and password in
the overrides dictionary and otherwise use the values in the model's
connection dictionary. Throws an exception if the connection failed.

---

### __createAndInsertInstance__

`public static com.apple.yellow.eocontrol.EOEnterpriseObject createAndInsertInstance(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName)`

Creates a new enterprise object for the specified
entity, inserts it into _editingContext_,
and returns the new object.

---

### databaseContextForModelNamed

`public static EODatabaseContext databaseContextForModelNamed(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String modelName)`

Returns the database context used to service
the specified model.

---

### destinationKeyForSourceObject

`public static NSDictionary destinationKeyForSourceObject(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
com.apple.yellow.eocontrol.EOEnterpriseObject object,
String relationshipName)`

Returns the foreign key for the rows at the
destination entity of the specified relationship. As an example,
given entities Department and Employee with a relationship called
"department" joining `Department.ID` and `Employee.deptID`,
invoking this method on a Department object with ID equal to 5 returns
a dictionary with a value of 5 for the `deptID` key.

__See
Also:__  [primaryKeyForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpobzgs3lboj4uwzlzizxxet3cnjswg5a)

---

### entityForClass

`public static EOEntity entityForClass(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
Class classObject)`

Returns the entity associated with the specified
class. Throws an exception if the specified entity can't be found
or if more than one entity is associated with the class.

__See
Also:__  [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfdg64spmjvgky3u), [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfhgc3lfmq), [objectsOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu6zsdnrqxg4y)

---

### entityForObject

`public static EOEntity entityForObject(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
com.apple.yellow.eocontrol.EOEnterpriseObject object)`

Returns the entity associated with the provided
enterprise object. Throws an exception if the specified entity can't
be found.

__See Also:__  [entityForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfdg64sdnrqxg4y), [entityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfhgc3lfmq)

---

### entityNamed

`public static EOEntity entityNamed(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName)`

Returns the entity with the specified name. Throws an
exception if the specified entity can't be found.

__See
Also:__  [entityForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfdg64sdnrqxg4y), [entityForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfdg64spmjvgky3u)

---

### executeStoredProcedureNamed

`public static NSDictionary executeStoredProcedureNamed(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String storedProcedureName,
NSDictionary arguments)`

Executes the specified stored procedure with
the provided arguments. Returns the stored procedure's return
values (if any). Use only with stored procedures that don't return
results rows.

__See Also:__  [rawRowsForStoredProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zum33skn2g64tfmrihe33dmvshk4tfjzqw2zle)

---

### localInstanceOfObject

`public static com.apple.yellow.eocontrol.EOEnterpriseObject localInstanceOfObject(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
com.apple.yellow.eocontrol.EOEnterpriseObject object)`

Translates the specified enterprise object from
another editing context to the specified one.

__See
Also:__  [localInstancesOfObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpnrxwgylmjfxhg5dbnzrwk42pmzhwe2tfmn2hg)

---

### localInstancesOfObjects

`public static NSArray localInstancesOfObjects(
com.apple.yellow.eocontrol.EOEditingContext,
editingContext,
NSArray objects)`

Translates the specified enterprise objects
from another editing context to the specified one.

__See
Also:__  [localInstanceOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpnrxwgylmjfxhg5dbnzrwkt3gj5rguzldoq)

---

### modelGroup

`public static EOModelGroup modelGroup(com.apple.yellow.eocontrol.EOEditingContext editingContext)`

Returns the model group associated with the
editing context's root object store, an EOObjectStoreCoordinator.

---

### objectFromRawRow

`public static com.apple.yellow.eocontrol.EOEnterpriseObject objectFromRawRow(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
NSDictionary row)`

Fetches and returns the object corresponding
to the specified raw row (using EOEditingContext's __faultForRawRow__).
This method can only be used on raw rows that include the row's
primary key.

---

### objectMatchingKeyAndValue

`public static com.apple.yellow.eocontrol.EOEnterpriseObject objectMatchingKeyAndValue(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
String key,
Object value)`

Creates an EOKeyValueQualifier with the specified
key and value and returns matching enterprise objects. Throws an exception unless
exactly one object is retrieved.

__See Also:__  [objectMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2wmfwhkzlt), [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thjnsxsqlomrlgc3dvmu)

---

### objectMatchingValues

`public static com.apple.yellow.eocontrol.EOEnterpriseObject objectMatchingValues(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
NSDictionary values)`

Creates EOKeyValueQualifiers for each key-value
pair in the specified dictionary, ANDs these qualifiers together
into an EOAndQualifier, and returns matching enterprise objects. Throws an exception unless
exactly one object is retrieved.

__See Also:__  [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2lmv4uc3tekzqwy5lf), [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thkzqwy5lfom)

---

### objectsForEntityNamed

`public static NSArray objectsForEntityNamed(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName)`

Fetches and returns the enterprise objects associated
with the specified entity.

__See Also:__  [objectsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzvo2lunbixkylmnftgszlsizxxe3lboq), [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thjnsxsqlomrlgc3dvmu), [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thkzqwy5lfom)

---

### objectsMatchingKeyAndValue

`public static NSArray objectsMatchingKeyAndValue(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
String key,
Object value)`

Creates an EOKeyValueQualifier with the specified
key and value and returns matching enterprise objects.

__See
Also:__  [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2lmv4uc3tekzqwy5lf), [objectsForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzum33sivxhi2lupfhgc3lfmq), [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thkzqwy5lfom)

---

### objectsMatchingValues

`public static NSArray objectsMatchingValues(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
NSDictionary values)`

Creates EOKeyValueQualifiers for each key-value
pair in the specified dictionary, ANDs these qualifiers together
into an EOAndQualifier, and returns matching enterprise objects.

__See
Also:__  [objectMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2wmfwhkzlt), [objectsForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzum33sivxhi2lupfhgc3lfmq), [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thjnsxsqlomrlgc3dvmu)

---

### objectsOfClass

`public static NSArray objectsOfClass(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
Class classObject)`

Fetches and returns the enterprise objects associated
with the specified class. Throws an exception if more
than one entity for the class exists.

__See
Also:__  [entityForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpmvxhi2lupfdg64sdnrqxg4y)

---

### objectsWithFetchSpecificationAndBindings

`public static NSArray objectsWithFetchSpecificationAndBindings(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
String fetchSpecName,
NSDictionary bindings)`

Fetches and returns the enterprise objects retrieved
with the specified fetch specification and bindings.

__See
Also:__  [objectWithFetchSpecificationAndBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5diizsxiy3iknygky3jmzuwgylunfxw4qlomrbgs3tenfxgo4y)

---

### objectsWithQualifierFormat

`public static NSArray objectsWithQualifierFormat(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
String format,
NSArray arguments)`

Creates a qualifier with the provided format
string and arguments, and returns matching enterprise objects.

__See
Also:__  [objectWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5dikf2wc3djmzuwk4sgn5zg2ylu), [objectsForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzum33sivxhi2lupfhgc3lfmq)

---

### objectWithFetchSpecificationAndBindings

`public static com.apple.yellow.eocontrol.EOEnterpriseObject objectWithFetchSpecificationAndBindings(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
String fetchSpecName,
NSDictionary bindings)`

Fetches and returns the enterprise objects retrieved
with the specified fetch specification and bindings. Throws an exception unless
exactly one object is retrieved.

__See Also:__  [objectsWithFetchSpecificationAndBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63sbnzsee2lomruw4z3t)

---

### objectWithPrimaryKey

`public static com.apple.yellow.eocontrol.EOEnterpriseObject objectWithPrimaryKey(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
NSDictionary keyDictionary)`

Fetches and returns the enterprise object identified
by the specified primary key dictionary. Throws an exception unless
exactly one object is retrieved.

__See Also:__  [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2lmv4uc3tekzqwy5lf), [objectWithPrimaryKeyValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5dikbzgs3lboj4uwzlzkzqwy5lf), [primaryKeyForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpobzgs3lboj4uwzlzizxxet3cnjswg5a)

---

### objectWithPrimaryKeyValue

`public static com.apple.yellow.eocontrol.EOEnterpriseObject objectWithPrimaryKeyValue(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
Object value)`

Fetches and returns the enterprise object identified
by the specified primary key value. For use only with enterprise
objects that have non-compound primary keys. Throws an exception unless
exactly one object is retrieved.

__See Also:__  [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thkzqwy5lfom), [objectWithPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5dikbzgs3lboj4uwzlz)

---

### objectWithQualifierFormat

`public static com.apple.yellow.eocontrol.EOEnterpriseObject objectWithQualifierFormat(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
String format,
NSArray arguments)`

Creates a qualifier with the provided format
string and arguments, and returns matching enterprise objects. Throws an exception unless
exactly one object is retrieved.

__See Also:__  [objectsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzvo2lunbixkylmnftgszlsizxxe3lboq), [rawRowsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zvo2lunbixkylmnftgszlsizxxe3lboq)

---

### primaryKeyForObject

`public static NSDictionary primaryKeyForObject(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
com.apple.yellow.eocontrol.EOEnterpriseObject object)`

Returns the primary key dictionary for the specified
enterprise object.

__See Also:__  [objectWithPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5dikbzgs3lboj4uwzlz), [objectWithPrimaryKeyValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorlws5dikbzgs3lboj4uwzlzkzqwy5lf)

---

### rawRowsForSQL

`public static NSArray rawRowsForSQL(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String modelName,
String sqlString)`

Evaluates the specified SQL and returns the
resulting raw rows.

__See Also:__  [rawRowsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zvo2lunbixkylmnftgszlsizxxe3lboq), [rawRowsForStoredProcedureNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zum33skn2g64tfmrihe33dmvshk4tfjzqw2zle)

---

### rawRowsForStoredProcedureNamed

`public static NSArray rawRowsForStoredProcedureNamed(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String storedProcedureName,
NSDictionary arguments)`

Executes the specified stored procedure with
the provided arguments and returns the resulting raw rows.

__See
Also:__  [rawRowsForSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zum33skniuy)

---

### rawRowsMatchingKeyAndValue

`public static NSArray rawRowsMatchingKeyAndValue(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
String key,
Object value)`

Creates an EOKeyValueQualifier with the specified
key and value and returns matching raw rows.

__See
Also:__  [objectMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2lmv4uc3tekzqwy5lf), [objectsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thjnsxsqlomrlgc3dvmu), [rawRowsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zu2ylumnugs3thkzqwy5lfom)

---

### rawRowsMatchingValues

`public static NSArray rawRowsMatchingValues(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
NSDictionary values)`

Creates EOKeyValueQualifiers for each key-value
pair in the specified dictionary, ANDs these qualifiers together
into an EOAndQualifier, and returns matching raw rows.

__See
Also:__  [objectMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorgwc5ddnbuw4z2wmfwhkzlt), [objectsMatchingValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzu2ylumnugs3thkzqwy5lfom), [rawRowsMatchingKeyAndValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zu2ylumnugs3thjnsxsqlomrlgc3dvmu)

---

### rawRowsWithQualifierFormat

`public static NSArray rawRowsWithQualifierFormat(
com.apple.yellow.eocontrol.EOEditingContext editingContext,
String entityName,
String format,
NSArray arguments)`

Creates a qualifier for the specified entity
and with the specified qualifier format and returns matching raw
row dictionaries.

__See Also:__  [objectsWithQualifierFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpn5rguzldorzvo2lunbixkylmnftgszlsizxxe3lboq), [rawRowsForSQL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkv2gs3djoruwk4zpojqxoutpo5zum33skniuy)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
