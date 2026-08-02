---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EODatabaseDataSource.html
archived_at: '2026-07-15T08:11:33.551718Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EODatabaseDataSource

> __Inherits
> from:__  EODataSource (EOControl) : NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EODatabaseDataSource.h

---

## Class Description

---

EODatabaseDataSource is a concrete subclass of EODataSource
(defined in EOControl) that fetches objects based on an EOModel,
using an EODatabaseContext that services the data source's EOEditingContext
(defined in EOControl). An EODatabaseDataSource can be set up to
fetch all objects for its root entity, to fetch objects matching
a particular EOFetchSpecification, and to further filter its fetching
with an auxiliary qualifier.

EODatabaseDataSource implements all the functionality defined
by EODataSource: In addition to fetching objects, it can insert
and delete them (provided the entity isn't read-only). See the EODataSource
class specification for more information on these topics.

As with other data sources, EODatabaseDataSource can also
provide a detail data source. The most significant consequence of
using an master-detail configuration is that the detail operates
directly on the master's object graph. The EODetailDataSource
has a __master object__ and a __detail key__ through which
the detail data source accesses the its objects. The master object
is simply the object that's selected in the master display group,
and the detail key is the name of a relationship property in the
master object. When the detail display group asks its data source
to fetch, the EODetailDataSource simply gets the value for the relationship
property identified by the detail key from its master object and
returns it. When you add and remove objects from the detail, you're
directly modifying the master's relationship array. In fact, you
can think of EODetailDataSource as an interface to its master object's
relationship property.

## Method Types

---

> **Creating instances**
> : [- initWithEditingContext:entityName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss62lonf2fo2lunbcwi2lunfxgoq3pnz2gk6duhjsw45djor4u4ylnmu5a)
> : [- initWithEditingContext:entityName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss62lonf2fo2lunbcwi2lunfxgoq3pnz2gk6duhjsw45djor4u4ylnmu5a)
>
> **Accessing selection criteria**
> : [- auxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ylvpbuwy2lboj4vc5lbnruwm2lfoi)
> : [- fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpny)
> : [- fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpnzdg64sgmv2gg2a)
> : [- fetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpnzhgc3lf)
> : [- setAuxiliaryQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643foraxk6djnruwc4tzkf2wc3djmzuwk4r2)
> : [- setFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbjxazldnftgsy3boruw63r2)
> : [- setFetchSpecificationByName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbjxazldnftgsy3boruw63scpfhgc3lfhi)
>
> **Accessing objects used
> for fetching**
> : [- entity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6zlooruxi6i)
> : [- databaseContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6zdborqweyltmvbw63tumv4hi)
>
> **Enabling fetching**
> : [- setFetchEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbcw4ylcnrswioq)
> : [- isFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss62ltizsxiy3iivxgcytmmvsa)
>
> **Accessing qualifier bindings**
> : [- qualifierBindingKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss64lvmfwgsztjmvzee2lomruw4z2lmv4xg)
> : [- qualifierBindings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss64lvmfwgsztjmvzee2lomruw4z3t)
> : [- setQualifierBindings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643forixkylmnftgszlsijuw4zdjnztxgoq)

## Instance Methods

---

### auxiliaryQualifier

`- (EOQualifier *)auxiliaryQualifier`

Returns the EOQualifier used to further filter
the objects fetched by the receiver's EOFetchSpecification (in
EOControl).

__See Also:__  [- fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpnzdg64sgmv2gg2a), [- fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpny)

---

### databaseContext

`- (EODatabaseContext *)databaseContext`

Returns the EODatabaseContext that the receiver
uses to access the external database. This is either the root EOObjectStore
for the receiver's EOEditingContext, or if the root is an EOCooperatingObjectStore, it's
the EODatabaseContext under that EOCooperatingObjectStore that services
the EOModel containing the EOEntity for the receiver. (EOObjectStore,
EOEditingContext, and EOCooperatingObjectStore are all defined in
EOControl.)

---

### entity

`- (EOEntity *)entity`

Returns the EOEntity from which the receiver
fetches objects.

---

### fetchSpecification

`- (EOFetchSpecification *)fetchSpecification`

Returns the receiver's basic EOFetchSpecification.
Its EOQualifier is conjoined with the receiver's auxiliary EOQualifier
when the receiver fetches objects. The sender of this message can
alter the EOFetchSpecification directly, or replace it using [setFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbjxazldnftgsy3boruw63r2).

__See
Also:__  [fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpnzdg64sgmv2gg2a), [auxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ylvpbuwy2lboj4vc5lbnruwm2lfoi)

---

### fetchSpecificationForFetch

`- (EOFetchSpecification *)fetchSpecificationForFetch`

Returns a copy of the EOFetchSpecification that
the receiver uses to fetch. This is constructed by conjoining the
EOQualifier of the receiver's EOFetchSpecification with its auxiliary
EOQualifier. Modifying the returned EOFetchSpecification doesn't
affect the receiver's fetching behavior; use [setFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbjxazldnftgsy3boruw63r2) and [setAuxiliaryQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643foraxk6djnruwc4tzkf2wc3djmzuwk4r2) for that purpose.

__See
Also:__  [- fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpny), [- auxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ylvpbuwy2lboj4vc5lbnruwm2lfoi)

---

### fetchSpecificationName

`- (NSString *)fetchSpecificationName`

Returns the name of the fetch specification
(or nil if there is no name).

__See Also:__  [- setFetchSpecificationByName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbjxazldnftgsy3boruw63scpfhgc3lfhi)

---

### initWithEditingContext:entityName:

`- (id)initWithEditingContext:(EOEditingContext
*)anEditingContext
entityName:(NSString *)anEntityName`

Initializes a newly allocated EODatabaseDataSource
to fetch objects into _anEditingContext_ for
the EOEntity named by _anEntityName_.
This method checks _anEditingContext_'s
EOObjectStoreCoordinator for an EODatabaseChannel that services
the EOModel containing the named EOEntity. If none exists, this
method creates one. This method works by calling [initWithEditingContext:entityName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss62lonf2fo2lunbcwi2lunfxgoq3pnz2gk6duhjsw45djor4u4ylnmu5a) and specifying __nil__ for
the fetchSpecificationName.

---

### initWithEditingContext:entityName:fetchSpecificationName:

`- (id)initWithEditingContext:(EOEditingContext
*)anEditingContext
entityName:(NSString *)anEntityName
fetchSpecificationName:(NSString
*)fetchSpecificationName`

Initializes a newly allocated EODatabaseDataSource
to fetch objects into _anEditingContext_ for
the EOEntity named by _anEntityName_.
This method checks _anEditingContext_'s
EOObjectStoreCoordinator for an EODatabaseChannel that services
the EOModel containing the named EOEntity. If none exists, this
method creates one. The _fetchSpecificationName_ argument
is used to find the named fetch specification in the entity. If
the _fetchSpecificationName_ is __nil__,
a new fetch specification will be instantiated that will fetch all
objects of the entity. This is the primitive initializer. Returns __self__.

---

### isFetchEnabled

`- (BOOL)isFetchEnabled`

Returns YES if the receiver's __fetchObjects__ method
actually fetches objects, NO if it returns an empty array without
fetching. Fetching is typically disabled in a master-peer configuration
when no object is selected in the master.

__See
Also:__  [- setFetchEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbcw4ylcnrswioq)

---

### qualifierBindingKeys

`- (NSArray *)qualifierBindingKeys`

Returns an array of strings which is a union
of the binding keys from the fetch specification's qualifier and
the data source's auxiliary qualifier.

__See
Also:__  [- setQualifierBindings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643forixkylmnftgszlsijuw4zdjnztxgoq)

---

### qualifierBindings

`- (NSDictionary *)qualifierBindings`

Returns a set of bindings that will be used
for variable replacement on the fetch specification's qualifier and
the auxiliary qualifier before the fetch is executed.

---

### setAuxiliaryQualifier:

`- (void)setAuxiliaryQualifier:(EOQualifier
*)aQualifier`

Sets the receiver's auxiliary qualifier to _aQualifier_.
The auxiliary qualifier usually adds conditions to the primary qualifier
and is useful for narrowing the scope of a data source without altering
its primary qualifier. This is especially useful for setting a qualifier
on a qualified peer data source, since a peer's primary qualifiers
specifies the matching criteria for the relationship it fetches
for. For more information on auxiliary qualifiers, see "Creating
a Master-Peer Configuration" in the "WebObjects Programming
Topics."

__See Also:__  [- fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpnzdg64sgmv2gg2a), [- fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpny)

---

### setFetchEnabled:

`- (void)setFetchEnabled:(BOOL)flag`

Controls whether the receiver can fetch. If _flag_ is YES the
receiver's __fetchObjects__ method actually fetches
objects, if NO it returns an empty array without fetching. Fetching
is typically disabled in a master-peer configuration when no object
is selected in the master. For example, EODatabaseDataSource's
implementation of __qualifyWithRelationshipKey:ofObject:__ invokes
this method to enable or disable fetching based on whether a master
object is provided.

__See Also:__  [- isFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss62ltizsxiy3iivxgcytmmvsa)

---

### setFetchSpecification:

`- (void)setFetchSpecification:(EOFetchSpecification
*)fetchSpec`

Sets the receiver's basic EOFetchSpecification
to _fetchSpec_. Its EOQualifier is
conjoined with the receiver's auxiliary EOQualifier when the receiver
fetches objects. This method also sets the name of the fetch specification
to nil.

__See Also:__  [- setAuxiliaryQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643foraxk6djnruwc4tzkf2wc3djmzuwk4r2), [- fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpnzdg64sgmv2gg2a), [- setFetchSpecificationByName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbjxazldnftgsy3boruw63scpfhgc3lfhi)

---

### setFetchSpecificationByName:

`- (void)setFetchSpecificationByName:(NSString
*)fetchSpecificationName`

Sets the _fetchSpecificationName_ as
given, and sets the fetch specification (used when supplying objects)
to the named fetch specification of the entity that was used to
initialize the data source. This method is an alternative to [setFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss643fordgk5ddnbjxazldnftgsy3boruw63r2).

__See
Also:__  [- fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpny), [- fetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss6ztforrwqu3qmvrwsztjmnqxi2lpnzhgc3lf)

---

### setQualifierBindings:

`- (NSDictionary *)setQualifierBindings:(NSDictionary
*)bindings`

Sets a set of bindings that will be used for
variable replacement on the fetch specification's qualifier and the
auxiliary qualifier before the fetch is executed.

__See
Also:__  [- qualifierBindingKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsuiylumfjw65lsmnss64lvmfwgsztjmvzee2lomruw4z2lmv4xg)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
