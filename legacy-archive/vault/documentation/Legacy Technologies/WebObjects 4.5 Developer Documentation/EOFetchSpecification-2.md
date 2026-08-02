---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOFetchSpecification.html
archived_at: '2026-07-15T08:11:39.783168Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOFetchSpecification

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSCoding
> : NSCopying
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EOFetchSpecification.h

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

EOFetchSpecifications are most often used with the method __objectsWithFetchSpecification:editingContext:__,
defined by EOObjectStore, EOEditingContext, and EODatabaseContext,
as well as [objectsWithFetchSpecification:editingContext:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otfmruxi2lom5bw63tumv4hioq),
defined by EOEditingContext alone. EOAdaptorChannel and EODatabaseChannel
also define methods that use EOFetchSpecifications.

## Adopted Protocols

---

> NSCoding: __- encodeWithCoder:__
> : __- initWithCoder:__
>
> NSCopying: __- copyWithZone:__

## Method Types

---

> **Creating and accessing
> instances**
> : [+ fetchSpecificationWithEntityName:qualifier:sortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumzlumnufg4dfmnuwm2ldmf2gs33of5tgk5ddnbjxazldnftgsy3boruw63sxnf2gqrlooruxi6komfwwkotrovqwy2lgnfsxeottn5zhit3smrsxe2lom5ztu)
> : [- fetchSpecificationWithQualifierBindings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc6ztforrwqu3qmvrwsztjmnqxi2lpnzlws5dikf2wc3djmzuwk4scnfxgi2lom5ztu) (Yellow
> Box only)
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62lonf2a)
> : [- initWithEntityName:qualifier:sortOrderings:usesDistinct:isDeep:hints:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62lonf2fo2lunbcw45djor4u4ylnmu5hc5lbnruwm2lfoi5hg33sorhxezdfojuw4z3thj2xgzltiruxg5djnzrxiotjoncgkzlqhjugs3tuom5a)
> : [+ fetchSpecificationNamed:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumzlumnufg4dfmnuwm2ldmf2gs33of5tgk5ddnbjxazldnftgsy3boruw63somfwwkzb2mvxhi2lupfhgc3lfmq5a)
>
> **Setting the qualifier**
> : [- setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forixkylmnftgszlshi)
> : [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64lvmfwgsztjmvza)
>
> **Sorting**
> : [- setSortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjw64tuj5zgizlsnfxgo4z2)
> : [- sortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643poj2e64temvzgs3thom5a)
>
> **Removing duplicates**
> : [- setUsesDistinct:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forkxgzltiruxg5djnzrxioq)
> : [- usesDistinct:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc65ltmvzui2ltoruw4y3uhi)
>
> **Fetching objects in an
> inheritance hierarchy**
> : [- setIsDeep:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forexgrdfmvydu)
> : [- isDeep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62ltirswk4a)
> : [- setEntityName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forcw45djor4u4ylnmu5a)
> : [- entityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc6zlooruxi6komfwwk)
>
> **Controlling fetching
> behavior**
> : [- setFetchLimit:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643fordgk5ddnbggs3ljoq5a)
> : [- fetchLimit](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc6ztforrwqtdjnvuxi)
> : [- setFetchesRawRows:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643fordgk5ddnbsxgutbo5jg653thi)
> : [- fetchesRawRows](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc6ztforrwqzltkjqxoutpo5zq)
> : [- setPrefetchingRelationshipKeyPaths:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forihezlgmv2gg2djnztvezlmmf2gs33oonugs4clmv4vaylunbztu)
> : [- prefetchingRelationshipKeyPaths](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64dsmvtgk5ddnbuw4z2smvwgc5djn5xhg2djobfwk6kqmf2gq4y)
> : [- setPromptsAfterFetchLimit:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forihe33nob2hgqlgorsxertforrwqtdjnvuxioq)
> : [- promptsAfterFetchLimit](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64dsn5wxa5dtifthizlsizsxiy3ijruw22lu)
> : [- setRawRowKeyPaths:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjgc52sn53uwzlzkbqxi2dthi)
> : [- rawRowKeyPaths](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64tbo5jg652lmv4vaylunbzq)
> : [- setRequiresAllQualifierBindingVariables:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjgk4lvnfzgk42bnrwfc5lbnruwm2lfojbgs3tenfxgovtbojuwcytmmvztu)
> : [- requiresAllQualifierBindingVariables](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64tfof2ws4tfonawy3crovqwy2lgnfsxeqtjnzsgs3thkzqxe2lbmjwgk4y)
> : [- setHints:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643foregs3tuom5a)
> : [- hints](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62djnz2hg)
>
> **Locking objects**
> : [- setLocksObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forgg6y3lonhwe2tfmn2hgoq)
> : [- locksObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc63dpmnvxgt3cnjswg5dt)
>
> **Refreshing refetched
> objects**
> : [- setRefreshesRefetchedObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjgkztsmvzwqzltkjswmzlumnugkzcpmjvgky3uom5a)
> : [- refreshesRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64tfmzzgk43imvzvezlgmv2gg2dfmrhwe2tfmn2hg)

## Class Methods

---

### fetchSpecificationNamed:entityNamed:

`+ (EOFetchSpecification *)fetchSpecificationNamed:(NSString
*)name
entityNamed:(NSString *)entityName`

Returns the fetch specification that the entity
specified by _entityName_ associates
with the fetch specification name _name_.

---

### fetchSpecificationWithEntityName:qualifier:sortOrderings:

`+ (EOFetchSpecification *)fetchSpecificationWithEntityName:(NSString
*)entityName
qualifier:(EOQualifier *)qualifier
sortOrderings:(NSArray *)sortOrderings`

Returns an EOFetchSpecification for _entityName_,
using _qualifier_ to select and _sortOrderings_ to
sort the results. The EOFetchSpecification created with this method
is deep, doesn't perform distinct selection, and has no hints.

__See
Also:__  [- initWithEntityName:qualifier:sortOrderings:usesDistinct:isDeep:hints:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62lonf2fo2lunbcw45djor4u4ylnmu5hc5lbnruwm2lfoi5hg33sorhxezdfojuw4z3thj2xgzltiruxg5djnzrxiotjoncgkzlqhjugs3tuom5a)

---

## Instance Methods

---

### entityName

`- (NSString *)entityName`

Returns the name of the entity to be fetched.

__See
Also:__  [- isDeep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62ltirswk4a), [- setEntityName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forcw45djor4u4ylnmu5a)

---

### fetchLimit

`- (unsigned)fetchLimit`

Returns the fetch limit value which indicates
the maximum number of objects to fetch. Depending on the value of
promptsAfterFetchLimit, the EODatabaseContext will either stop fetching
objects when this limit is reached or it will ask the editing context's
message handler to prompt the user as to whether or not it should
continue fetching. Use 0 (zero) to indicate no fetch limit. The
default is 0.

---

### fetchesRawRows

`- (BOOL)fetchesRawRows`

Returns YES if [rawRowKeyPaths](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64tbo5jg652lmv4vaylunbzq) returns non-nil.

---

### fetchSpecificationWithQualifierBindings:

`- (EOFetchSpecification *)fetchSpecificationWithQualifierBindings:(NSDictionary
*)bindings`

Applies bindings from _bindings_ to
its qualifier if there is one, and returns a new fetch specification
that can be used in a fetch. The default behavior is to prune any
nodes for which there are no bindings. Invoke [setRequiresAllQualifierBindingVariables:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjgk4lvnfzgk42bnrwfc5lbnruwm2lfojbgs3tenfxgovtbojuwcytmmvztu)with
an argument of YES to force an exception to be raised if a binding
is missing during variable substitution.

---

### hints

`- (NSDictionary *)hints`

Returns the receiver's hints, which other
objects can use to alter or optimize fetch operations.

__See
Also:__  [- setHints:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643foregs3tuom5a)

---

### init

`- (id)init`

Initializes a new EOFetchSpecification with
no state, except that it fetches deeply and doesn't use distinct.
Use the __set...__ methods to add other parts
of the specification. This is the designated initializer for the
EOFetchSpecification class. Returns __self__.

__See
Also:__  [- initWithEntityName:qualifier:sortOrderings:usesDistinct:isDeep:hints:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62lonf2fo2lunbcw45djor4u4ylnmu5hc5lbnruwm2lfoi5hg33sorhxezdfojuw4z3thj2xgzltiruxg5djnzrxiotjoncgkzlqhjugs3tuom5a)

---

### initWithEntityName:qualifier:sortOrderings:usesDistinct:isDeep:hints:

`- (id)initWithEntityName:(NSString
*)entityName
qualifier:(EOQualifier *)qualifier
sortOrderings:(NSArray *)sortOrderings
usesDistinct:(BOOL)distinctFlag
isDeep:(BOOL)deepFlag
hints:(NSDictionary *)hints`

Initializes a new EOFetchSpecification with
the given arguments. Returns __self__.

__See
Also:__  [+ fetchSpecificationWithEntityName:qualifier:sortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumzlumnufg4dfmnuwm2ldmf2gs33of5tgk5ddnbjxazldnftgsy3boruw63sxnf2gqrlooruxi6komfwwkotrovqwy2lgnfsxeottn5zhit3smrsxe2lom5ztu)

---

### isDeep

`- (BOOL)isDeep`

Returns YES if a fetch should include sub-entities
of the receiver's entity, NO if it shouldn't. EOFetchSpecifications
are deep by default.

For example, if you have a Person entity
with two sub-entities, Employee and Customer, fetching Persons deeply
also fetches all Employees and Customers matching the qualifier.
Fetching Persons shallowly fetches only Persons matching the qualifier.

---

### locksObjects

`- (BOOL)locksObjects`

Returns YES if a fetch should result in the
selected objects being locked in the data repository, NO if it shouldn't.
The default is NO.

__See Also:__  [- setLocksObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forgg6y3lonhwe2tfmn2hgoq)

---

### prefetchingRelationshipKeyPaths

`- (NSArray *)prefetchingRelationshipKeyPaths`

Returns an array of relationship key paths that
should be prefetched along with the main fetch. For example, if
fetching from the Movie entity, you might specify paths of the form
(@"directors", @"roles.talent", @"plotSummary").

---

### promptsAfterFetchLimit

`- (BOOL)promptsAfterFetchLimit`

Returns whether to prompt user after the fetch
limit has been reached. Default is NO.

---

### qualifier

`- (EOQualifier *)qualifier`

Returns the EOQualifier that indicates which
records or objects the receiver is to fetch.

__See
Also:__  [- setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forixkylmnftgszlshi)

---

### rawRowKeyPaths

`- (NSArray *)rawRowKeyPaths`

Returns an array of attribute key paths that
should be fetched as raw data and returned as an array of dictionaries
(instead of the normal result of full objects). The raw fetch can
increase speed, but forgoes most of the benefits of full Enterprise
Objects. The default value is nil, indicating that full objects
will be returned from the fetch. An empty array may be used to indicate
that the fetch should query the entity named by the fetch specification
using the method __attributesToFetch__. As
long as the primary key attributes are included in the raw attributes,
the raw row may be used to generate a fault for the corresponding
object using EOEditingContext's [faultForRawRow:entityNamed:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gmf2wy5cgn5zfeylxkjxxootfnz2gs5dzjzqw2zlehi) method.

__See
Also:__  [- setFetchesRawRows:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643fordgk5ddnbsxgutbo5jg653thi)

---

### refreshesRefetchedObjects

`- (BOOL)refreshesRefetchedObjects`

Returns YES if existing objects are overwritten
with fetched values when they've been updated or changed. Returns NO if
existing objects aren't touched when their data is refetched (the
fetched data is simply discarded). The default is NO. Note that
this setting does not affect relationships

__See
Also:__  [- setRefreshesRefetchedObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjgkztsmvzwqzltkjswmzlumnugkzcpmjvgky3uom5a)

---

### requiresAllQualifierBindingVariables

`- (BOOL)requiresAllQualifierBindingVariables`

Returns YES to indicate that a missing binding
will cause an exception to be raised during variable substitution.
The default value is NO, which says to prune any nodes for which
there are no bindings.

---

### setEntityName:

`- (void)setEntityName:(NSString
*)entityName`

Sets the name of the root entity to be fetched
to _entityName_.

__See
Also:__  [- isDeep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62ltirswk4a), [- entityName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc6zlooruxi6komfwwk)

---

### setFetchesRawRows:

`- (void)setFetchesRawRows:(BOOL)fetchRawRows`

Sets the behavior for fetching raw rows. If
set to YES, the behavior is the same as if [setRawRowKeyPaths:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjgc52sn53uwzlzkbqxi2dthi) were called with
an empty array. If set to NO, the behavior is as if __setRawRowKeyPaths:__ were
called with a nil argument.

---

### setFetchLimit:

`- (void)setFetchLimit:(unsigned)fetchLimit`

Sets the fetch limit value, which indicates
the maximum number of objects to fetch. Depending on the value of [promptsAfterFetchLimit](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64dsn5wxa5dtifthizlsizsxiy3ijruw22lu),
the EODatabaseContext either stops fetching objects when this limit is
reached or asks the editing context's message handler to prompt
the user as to whether or not it should continue fetching. Use 0
(zero) to indicate no fetch limit. The default is 0.

---

### setHints:

`- (void)setHints:(NSDictionary
*)hints`

Sets the receiver's hints to _hints_.
Any object that uses an EOFetchSpecification can define its own
hints that it uses to alter or optimize fetch operations. For example,
EODatabaseContext uses a hint identified by the key `EOCustomQueryExpressionHintKey`.
EODatabaseContext is the only class in Enterprise Objects Framework
that defines fetch specification hints. For information about EODatabaseContext's
hints, see the EODatabaseContext class specification.

__See
Also:__  [- hints](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62djnz2hg)

---

### setIsDeep:

`- (void)setIsDeep:(BOOL)flag`

Controls whether a fetch should include sub-entities
of the receiver's entity. If _flag_ is YES,
sub-entities are also fetched; if _flag_ is NO,
they aren't. EOFetchSpecifications are deep by default.

For
example, if you have a Person entity /class /table with two sub-entities
and subclasses, Employee and Customer, fetching Persons deeply also
fetches all Employees and Customers matching the qualifier, while
fetching Persons shallowly fetches only Persons matching the qualifier.

__See
Also:__  [- isDeep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc62ltirswk4a)

---

### setLocksObjects:

`- (void)setLocksObjects:(BOOL)flag`

Controls whether a fetch should result in the
selected objects being locked in the data repository. If _flag_ is YES it
should, if NO it shouldn't. The default is NO.

__See
Also:__  [- locksObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc63dpmnvxgt3cnjswg5dt)

---

### setPrefetchingRelationshipKeyPaths:

`- (void)setPrefetchingRelationshipKeyPaths:(NSArray
*)prefetchingRelationshipKeyPaths`

Sets an array of relationship key paths that
should be prefetched along with the main fetch. For example, if
fetching from the Movie entity, you might specify paths of the form
(@"directors", @"roles.talent", @"plotSummary").

Prefetching
increases the initial fetch cost, but it can improve overall performance
by reducing the number of round trips made to the database server.
Assigning relationships to prefetch also has an effect on how an
EOFetchSpecification refreshes. "Refreshing" refers to existing
objects being overwritten with fetched values-this allows your
application to see changes to the database that have been made by
someone else. Normally, when you set an EOFetchSpecification to
refresh using [setRefreshesRefetchedObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forjgkztsmvzwqzltkjswmzlumnugkzcpmjvgky3uom5a),
it only refreshes the objects you're fetching. For example, if
you fetch employees, you don't also fetch the employees' departments.
However, if you prefetch relationships, the refetch is propagated
for all of the relationships specified.

---

### setPromptsAfterFetchLimit:

`- (void)setPromptsAfterFetchLimit:(BOOL)promptsAfterFetchLimit`

Sets whether to prompt user after the fetch
limit has been reached. Default is NO.

---

### setQualifier:

`- (void)setQualifier:(EOQualifier
*)qualifier`

Sets the receiver's qualifier to _qualifier_.

__See
Also:__  [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64lvmfwgsztjmvza)

---

### setRawRowKeyPaths:

`- (void)setRawRowKeyPaths:(NSArray
*)rawRowKeyPaths`

Sets an array of attribute key paths that should
be fetched as raw data and returned as an array of dictionaries
(instead of the normal result of full objects). The raw fetch can
increase speed, but forgoes most of the benefits of full Enterprise
Objects. The default value is nil, indicating that full objects
will be returned from the fetch. An empty array may be used to indicate
that the fetch should query the entity named by the fetch specification
using the method __attributesToFetch__. As
long as the primary key attributes are included in the raw attributes,
the raw row may be used to generate a fault for the corresponding
object using EOEditingContext's [faultForRawRow:entityNamed:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3gmf2wy5cgn5zfeylxkjxxootfnz2gs5dzjzqw2zlehi) method.

__See
Also:__  [- setFetchesRawRows:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643fordgk5ddnbsxgutbo5jg653thi)

---

### setRefreshesRefetchedObjects:

`- (void)setRefreshesRefetchedObjects:(BOOL)flag`

Controls whether existing objects are overwritten
with fetched values when they have been updated or changed. If _flag_ is YES,
they are; if _flag_ is NO, they aren't
(the fetched data is simply discarded). The default is NO.

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
on an EODatabaseContext's refreshing behavior than you can with
an EOFetchSpecification by using the delegate method __databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:databaseChannel:__.
For more information see the EODatabaseContext class specification.

__See
Also:__  [- refreshesRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc64tfmzzgk43imvzvezlgmv2gg2dfmrhwe2tfmn2hg)

---

### setRequiresAllQualifierBindingVariables:

`- (void)setRequiresAllQualifierBindingVariables:(BOOL)allVariablesRequired`

Sets the behavior when a missing binding is
encountered during variable substitution. If _allVariablesRequired_ is YES,
then a missing binding will cause an exception to be raised during
variable substitution. The default value is NO, which says to prune
any nodes for which there are no bindings.

__See
Also:__  [- fetchSpecificationWithQualifierBindings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc6ztforrwqu3qmvrwsztjmnqxi2lpnzlws5dikf2wc3djmzuwk4scnfxgi2lom5ztu)

---

### setSortOrderings:

`- (void)setSortOrderings:(NSArray
*)sortOrderings`

Sets the receiver's array of EOSortOrderings
to _sortOrderings_. When a fetch is
performed with the receiver, the results are sorted by applying
each EOSortOrdering in the array.

---

### setUsesDistinct:

`- (void)setUsesDistinct:(BOOL)flag`

Controls whether duplicate objects or records
are removed after fetching. If _flag_ is YES they're
removed; if _flag_ is NO they aren't.
EOFetchSpecifications by default don't use distinct.

__See
Also:__  [- usesDistinct:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc65ltmvzui2ltoruw4y3uhi)

---

### sortOrderings:

`- (NSArray *)sortOrderings`

Returns the receiver's array of EOSortOrderings.
When a fetch is performed with the receiver, the results are sorted
by applying each EOSortOrdering in the array.

---

### usesDistinct:

`- (BOOL)usesDistinct`

Returns YES if duplicate objects or records
are removed after fetching, NO if they aren't. EOFetchSpecifications
by default don't use distinct.

__See Also:__  [- setUsesDistinct:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmv2gg2ctobswg2lgnfrwc5djn5xc643forkxgzltiruxg5djnzrxioq)

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
