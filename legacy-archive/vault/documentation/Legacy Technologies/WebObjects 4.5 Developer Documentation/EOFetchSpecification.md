---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOFetchSpecification.html
archived_at: '2026-07-15T08:11:37.606132Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOFetchSpecification

> **__Inherits from:__**
> : (com.apple.client.eocontrol) Object
>
> (com.apple.yellow.eocontrol) NSObject

> **__Implements:__**
> : (com.apple.client.eocontrol only) NSCoding
> : (com.apple.client.eocontrol only) Cloneable

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

An EOFetchSpecification collects the criteria needed to select
and order a group of records or enterprise objects, whether from
an external repository such as a relational database or an internal
store such as an EOEditingContext. An EOFetchSpecification contains
these elements:

- The name of an entity for which to fetch records
  or objects. This is the only mandatory element.
- An EOQualifier, indicating which properties to select by and
  how to do so.
- An array of EOSortOrderings, which indicate how the selected
  records or objects should be ordered when fetched.
- An indicator of whether to produce distinct results or not.
  Normally if a record or object is selected several times, such as
  when forming a join, it appears several times in the fetched results.
  An EOFetchSpecification that makes distinct selections causes duplicates
  to be filtered out, so each record or object selected appears exactly
  once in the result set.
- An indicator of whether to fetch deeply or not. This is used
  with inheritance hierarchies when fetching for an entity with sub-entities.
  A deep fetch produces all instances of the entity and its sub-entities,
  while a shallow fetch produces instances only of the entity in the
  fetch specification.
- A fetch limit indicating how many objects to fetch before
  giving the user or program an opportunity to intervene.
- A listing of relationships for which the destination of the
  relationship should be prefetched along with the entity being fetched.
  Proper use of this feature allows for substantially increased performance
  in some cases.
- A dictionary of hints, which an EODatabaseContext or other
  object can use to optimize or alter the results of the fetch.

EOFetchSpecifications are most often used with the method `objectsWithFetchSpecification`,
defined by EOObjectStore, EOEditingContext, and EODatabaseContext. EOAdaptorChannel
and EODatabaseChannel also define methods that use EOFetchSpecifications.

## Interfaces Implemented

---

> NSCoding (com.apple.client.eocontrol only): `classForCoder`
> : `encodeWithCoder`

## Method Types

---

> **Constructors**
> : [EOFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l2fj5dgk5ddnbjxazldnftgsy3boruw63q)
>
> **Setting the qualifier**
> : [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fc5lbnruwm2lfoi)
> : [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3rovqwy2lgnfsxe)
>
> **Sorting**
> : [setSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fg33sorhxezdfojuw4z3t)
> : [sortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tn5zhit3smrsxe2lom5zq)
>
> **Removing duplicates**
> : [setUsesDistinct](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fk43foncgs43unfxgg5a)
> : [usesDistinct](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3vonsxgrdjon2gs3tdoq)
>
> **Fetching objects in an
> inheritance hierarchy**
> : [setIsDeep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2es42emvsxa)
> : [isDeep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3joncgkzlq)
> : [setEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2ek3tunf2hsttbnvsq)
> : [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3fnz2gs5dzjzqw2zi)
>
> **Controlling fetching
> behavior**
> : [setFetchLimit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2emzlumnuey2lnnf2a)
> : [fetchLimit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3gmv2gg2cmnfwws5a)
> : [setFetchesRawRows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2emzlumnugk42smf3ve33xom)
> : [fetchesRawRows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3gmv2gg2dfonjgc52sn53xg)
> : [setPrefetchingRelationshipKeyPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fa4tfmzsxiy3infxgoutfnrqxi2lpnzzwq2lqjnsxsudboruhg)
> : [prefetchingRelationshipKeyPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3qojswmzlumnugs3thkjswyylunfxw443infyewzlzkbqxi2dt)
> : [setPromptsAfterFetchLimit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fa4tpnvyhi42bmz2gk4sgmv2gg2cmnfwws5a)
> : [promptsAfterFetchLimit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3qojxw24duonawm5dfojdgk5ddnbggs3ljoq)
> : [setRawRowKeyPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2feylxkjxxos3fpfigc5diom)
> : [rawRowKeyPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3smf3ve33xjnsxsudboruhg)
> : [setRequiresAllQualifierBindingVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fezlrovuxezltifwgyulvmfwgsztjmvzee2lomruw4z2wmfzgsylcnrsxg)
> : [requiresAllQualifierBindingVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3smvyxk2lsmvzuc3dmkf2wc3djmzuwk4scnfxgi2lom5lgc4tjmfrgyzlt)
> : [setHints](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2eq2loorzq)
> : [hints](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3infxhi4y)
>
> **Locking objects**
> : [setLocksObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2ey33dnnzu6ytkmvrxi4y)
> : [locksObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3mn5rww42pmjvgky3uom)
>
> **Refreshing refetched
> objects**
> : [setRefreshesRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fezlgojsxg2dfonjgkztforrwqzlej5rguzldorzq)
> : [refreshesRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3smvthezltnbsxgutfmzsxiy3imvse6ytkmvrxi4y)

## Constructors

---

### EOFetchSpecification

`public EOFetchSpecification()`

`public EOFetchSpecification(
String entityName,
EOQualifier qualifier,
NSArray sortOrderings)`

`public EOFetchSpecification(
String entityName,
EOQualifier qualifier,
NSArray sortOrderings,
boolean distinctFlag,
boolean deepFlag,
NSDictionary hints)`

Creates a new EOFetchSpecification with the
arguments specified. If no arguments are provided, the new EOFetchSpecification
has no state, except that it fetches deeply and doesn't use distinct.
Use the `set...` methods to add other parts
of the specification. Minimally, you must set the entity name.

If
only _entityName,_ _qualifier,_
and _sortOrderings_ are provided, the
new EOFetchSpecification is deep, doesn't perform distinct selection,
and has no hints.

---

## Static Methods

---

### fetchSpecificationNamed

`public static EOFetchSpecification fetchSpecificationNamed(
String name,
String entityName)`

Returns the fetch specification that the entity
specified by _entityName_ associates
with the fetch specification name _name._

---

## Instance Methods

---

### entityName

`public String entityName()`

Returns the name of the entity to be fetched.

__See
Also:__  [isDeep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3joncgkzlq), [setEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2ek3tunf2hsttbnvsq)

---

### fetchLimit

`public int fetchLimit()`

Returns the fetch limit value which indicates
the maximum number of objects to fetch. Depending on the value of
promptsAfterFetchLimit, the EODatabaseContext will either stop fetching
objects when this limit is reached or it will ask the editing context's
message handler to prompt the user as to whether or not it should
continue fetching. Use 0 (zero) to indicate no fetch limit. The
default is 0.

---

### fetchesRawRows

`public boolean fetchesRawRows()`

Returns true if [rawRowKeyPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3smf3ve33xjnsxsudboruhg) returns non-nil.

---

### fetchSpecificationWithQualifierBindings

`public EOFetchSpecification fetchSpecificationWithQualifierBindings(NSDictionary bindings)`

(com.apple.yellow.eocontrol only) Applies bindings
from _bindings_ to its qualifier if
there is one, and returns a new fetch specification that can be
used in a fetch. The default behavior is to prune any nodes for
which there are no bindings. Invoke [setRequiresAllQualifierBindingVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fezlrovuxezltifwgyulvmfwgsztjmvzee2lomruw4z2wmfzgsylcnrsxg)with
an argument of true to force an exception to be raised if a binding
is missing during variable substitution.

---

### hints

`public NSDictionary hints()`

Returns the receiver's hints, which other
objects can use to alter or optimize fetch operations.

__See
Also:__  [setHints](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2eq2loorzq)

---

### isDeep

`public boolean isDeep()`

Returns true if a fetch should include sub-entities
of the receiver's entity, false if it shouldn't. EOFetchSpecifications
are deep by default.

For example, if you have a Person entity
with two sub-entities, Employee and Customer, fetching Persons deeply
also fetches all Employees and Customers matching the qualifier.
Fetching Persons shallowly fetches only Persons matching the qualifier.

---

### locksObjects

`public boolean locksObjects()`

Returns true if a fetch should result in the
selected objects being locked in the data repository, false if it
shouldn't. The default is false.

__See Also:__  [setLocksObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2ey33dnnzu6ytkmvrxi4y)

---

### prefetchingRelationshipKeyPaths

`public NSArray prefetchingRelationshipKeyPaths()`

Returns an array of relationship key paths that
should be prefetched along with the main fetch. For example, if
fetching from the Movie entity, you might specify paths of the form
("directors", "roles.talent", "plotSummary").

---

### promptsAfterFetchLimit

`public boolean promptsAfterFetchLimit()`

Returns whether to prompt user after the fetch
limit has been reached. Default is false.

---

### qualifier

`EOQualifier qualifier()`

Returns the EOQualifier that indicates which
records or objects the receiver is to fetch.

__See
Also:__  [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fc5lbnruwm2lfoi)

---

### rawRowKeyPaths

`public NSArray rawRowKeyPaths()`

Returns an array of attribute key paths that
should be fetched as raw data and returned as an array of dictionaries
(instead of the normal result of full objects). The raw fetch can
increase speed, but forgoes most of the benefits of full Enterprise
Objects. The default value is nil, indicating that full objects
will be returned from the fetch. An empty array may be used to indicate
that the fetch should query the entity named by the fetch specification
using the method `attributesToFetch`. As
long as the primary key attributes are included in the raw attributes,
the raw row may be used to generate a fault for the corresponding
object using EOEditingContext's [faultForRawRow](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmzqxk3duizxxeutbo5jg65y) method. (Note that
this faulting behavior does not occur in com.apple.client.eocontrol.)

__See
Also:__  [setFetchesRawRows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2emzlumnugk42smf3ve33xom)

---

### refreshesRefetchedObjects

`public boolean refreshesRefetchedObjects()`

Returns true if existing objects are overwritten
with fetched values when they've been updated or changed. Returns false if
existing objects aren't touched when their data is refetched (the
fetched data is simply discarded). The default is false. Note that
this setting does not affect relationships

__See
Also:__  [setRefreshesRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fezlgojsxg2dfonjgkztforrwqzlej5rguzldorzq)

---

### requiresAllQualifierBindingVariables

`public boolean requiresAllQualifierBindingVariables()`

Returns true to indicate that a missing binding
will cause an exception to be raised during variable substitution.
The default value is false, which says to prune any nodes for which
there are no bindings.

---

### setEntityName

`public void setEntityName(String entityName)`

Sets the name of the root entity to be fetched
to _entityName._

__See
Also:__  [isDeep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3joncgkzlq), [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3fnz2gs5dzjzqw2zi)

---

### setFetchesRawRows

`public void setFetchesRawRows(boolean fetchRawRows)`

Sets the behavior for fetching raw rows. If
set to true, the behavior is the same as if [setRawRowKeyPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2feylxkjxxos3fpfigc5diom) were called with
an empty array. If set to false, the behavior is as if `setRawRowKeyPaths` were
called with a nil argument.

---

### setFetchLimit

`public void setFetchLimit(int fetchLimit)`

Sets the fetch limit value, which indicates
the maximum number of objects to fetch. Depending on the value of [promptsAfterFetchLimit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3qojxw24duonawm5dfojdgk5ddnbggs3ljoq),
the EODatabaseContext either stops fetching objects when this limit is
reached or asks the editing context's message handler to prompt
the user as to whether or not it should continue fetching. Use 0
(zero) to indicate no fetch limit. The default is 0.

---

### setHints

`public void setHints(NSDictionary hints)`

Sets the receiver's hints to _hints._
Any object that uses an EOFetchSpecification can define its own
hints that it uses to alter or optimize fetch operations. For example,
EODatabaseContext uses a hint identified by the key `CustomQueryExpressionHintKey`.
EODatabaseContext is the only class in Enterprise Objects Framework
that defines fetch specification hints. For information about EODatabaseContext's
hints, see the EODatabaseContext class specification.

__See
Also:__  [hints](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3infxhi4y)

---

### setIsDeep

`public void setIsDeep(boolean flag)`

Controls whether a fetch should include sub-entities
of the receiver's entity. If _flag_ is true,
sub-entities are also fetched; if _flag_ is false,
they aren't. EOFetchSpecifications are deep by default.

For
example, if you have a Person entity /class /table with two sub-entities
and subclasses, Employee and Customer, fetching Persons deeply also
fetches all Employees and Customers matching the qualifier, while
fetching Persons shallowly fetches only Persons matching the qualifier.

__See
Also:__  [isDeep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3joncgkzlq)

---

### setLocksObjects

`public void setLocksObjects(boolean flag)`

Controls whether a fetch should result in the
selected objects being locked in the data repository. If _flag_ is true it
should, if false it shouldn't. The default is false.

__See
Also:__  [locksObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3mn5rww42pmjvgky3uom)

---

### setPrefetchingRelationshipKeyPaths

`public void setPrefetchingRelationshipKeyPaths(NSArray prefetchingRelationshipKeyPaths)`

Sets an array of relationship key paths that
should be prefetched along with the main fetch. For example, if
fetching from the Movie entity, you might specify paths of the form
("directors", "roles.talent", "plotSummary").

Prefetching
increases the initial fetch cost, but it can improve overall performance
by reducing the number of round trips made to the database server.
Assigning relationships to prefetch also has an effect on how an
EOFetchSpecification refreshes. "Refreshing" refers to existing
objects being overwritten with fetched values-this allows your
application to see changes to the database that have been made by
someone else. Normally, when you set an EOFetchSpecification to
refresh using [setRefreshesRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fezlgojsxg2dfonjgkztforrwqzlej5rguzldorzq),
it only refreshes the objects you're fetching. For example, if
you fetch employees, you don't also fetch the employees' departments.
However, if you prefetch relationships, the refetch is propagated
for all of the relationships specified.

---

### setPromptsAfterFetchLimit

`public void setPromptsAfterFetchLimit(boolean promptsAfterFetchLimit)`

Sets whether to prompt user after the fetch
limit has been reached. Default is false.

---

### setQualifier

`public void setQualifier(EOQualifier qualifier)`

Sets the receiver's qualifier to _qualifier._

__See
Also:__  [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3rovqwy2lgnfsxe)

---

### setRawRowKeyPaths

`public void setRawRowKeyPaths(NSArray rawRowKeyPaths)`

Sets an array of attribute key paths that should
be fetched as raw data and returned as an array of dictionaries
(instead of the normal result of full objects). The raw fetch can
increase speed, but forgoes most of the benefits of full Enterprise
Objects. The default value is nil, indicating that full objects
will be returned from the fetch. An empty array may be used to indicate
that the fetch should query the entity named by the fetch specification
using the method `attributesToFetch`. As
long as the primary key attributes are included in the raw attributes,
the raw row may be used to generate a fault for the corresponding
object using EOEditingContext's [faultForRawRow](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpmzqxk3duizxxeutbo5jg65y) method. (Note that
this faulting behavior does not occur in com.apple.client.eocontrol.)

__See
Also:__  [setFetchesRawRows](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2emzlumnugk42smf3ve33xom)

---

### setRefreshesRefetchedObjects

`public void setRefreshesRefetchedObjects(boolean flag)`

Controls whether existing objects are overwritten
with fetched values when they have been updated or changed. If _flag_ is true,
they are; if _flag_ is false, they
aren't (the fetched data is simply discarded). The default is false.

For
example, suppose that you fetch an employee object and then refetch
it, without changing the employee between fetches. In this case,
you want to refresh the employee when you refetch it, because another
application might have updated the object since your first fetch.
To keep your employee in sync with the employee data in the external
repository, you'd need to replace the employee's outdated values
with the new ones. On the other hand, if you were to fetch the employee,
change it, and then refetch it, you would not want to refresh the
employee. If you to refreshed it-whether or not another application
had changed the employee-you would lose the changes that you had
made to the object.

You can get finer-grain control
on an EODatabaseContext's refreshing behavior in com.apple.yellow.eocontrol than
you can with an EOFetchSpecification by using the delegate method `databaseContextShouldUpdateCurrentSnapshot`.
For more information see the EODatabaseContext class specification and
EODatabaseContext.Delegate interface specification.

__See
Also:__  [refreshesRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3smvthezltnbsxgutfmzsxiy3imvse6ytkmvrxi4y)

---

### setRequiresAllQualifierBindingVariables

`public void setRequiresAllQualifierBindingVariables(boolean allVariablesRequired)`

Sets the behavior when a missing binding is
encountered during variable substitution. If _allVariablesRequired_ is true,
then a missing binding will cause an exception to be raised during variable
substitution. The default value is false, which says to prune any
nodes for which there are no bindings.

__See
Also:__  [fetchSpecificationWithQualifierBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3gmv2gg2ctobswg2lgnfrwc5djn5xfo2lunbixkylmnftgszlsijuw4zdjnztxg)

---

### setSortOrderings

`public void setSortOrderings(NSArray sortOrderings)`

Sets the receiver's array of EOSortOrderings
to _sortOrderings._ When a fetch is
performed with the receiver, the results are sorted by applying
each EOSortOrdering in the array.

---

### setUsesDistinct

`public void setUsesDistinct(boolean flag)`

Controls whether duplicate objects or records
are removed after fetching. If _flag_ is true they're removed;
if _flag_ is false they aren't. EOFetchSpecifications
by default don't use distinct.

__See Also:__  [usesDistinct](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3vonsxgrdjon2gs3tdoq)

---

### sortOrderings

`public NSArray sortOrderings()`

Returns the receiver's array of EOSortOrderings.
When a fetch is performed with the receiver, the results are sorted
by applying each EOSortOrdering in the array.

---

### usesDistinct

`public boolean usesDistinct`

Returns true if duplicate objects or records
are removed after fetching, false if they aren't. EOFetchSpecifications
by default don't use distinct.

__See Also:__  [setUsesDistinct](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizsxiy3iknygky3jmzuwgylunfxw4l3tmv2fk43foncgs43unfxgg5a)

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
