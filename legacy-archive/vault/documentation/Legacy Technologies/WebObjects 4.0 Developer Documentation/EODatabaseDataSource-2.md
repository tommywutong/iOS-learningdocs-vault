---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODatabaseDataSource.html
archived_at: '2026-07-18T01:28:16.209438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](More%20about%20EODatabaseContext.md)
[!](EODatabaseOperation-2.md)

---

# EODatabaseDataSource

__Inherits From:__
EODataSource : NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EODatabaseDataSource.h

---

## Class Description

EODatabaseDataSource is a concrete subclass of EODataSource (defined in EOControl) that fetches objects based on an EOModel, using an EODatabaseContext that services the data source's EOEditingContext (defined in EOControl). An EODatabaseDataSource can be set up to fetch all objects for its root entity, to fetch objects matching a particular EOFetchSpecification, and to further filter its fetching with an auxiliary qualifier.

EODatabaseDataSource implements all the functionality defined by EODataSource: In addition to fetching objects, it can insert and delete them (provided the entity isn't read-only). See the EODataSource class specification for more information on these topics.

As with other data sources, EODatabaseDataSource can also provide a detail data source. The most significant consequence of using an master-detail configuration is that the detail operates directly on the master's object graph. The EODetailDataSource has a _master object_ and a _detail key_ through which the detail data source accesses the its objects. The master object is simply the object that's selected in the master display group, and the detail key is the name of a relationship property in the master object. When the detail display group asks its data source to fetch, the EODetailDataSource simply gets the value for the relationship property named _detail key_ from its master object and returns it. When you add and remove objects from the detail, you're directly modifying the master's relationship array. In fact, you can think of EODetailDataSource as an interface to its master object's relationship property.

---

## Method Types

**Creating instances**

**[- initWithEditingContext:entityName:fetchSpecificationName:](#apple-haytcoa)

**[- initWithEditingContext:entityName:fetchSpecificationName:](#apple-haytcoa)****

**Accessing selection criteria**

**[- auxiliaryQualifier](#apple-gi3deoi)

**[- fetchSpecification](#apple-gi3tsny)

**[- fetchSpecificationForFetch](#apple-gi2dg)

**[- fetchSpecificationName](#apple-haytkmi)

**[- setAuxiliaryQualifier:](#apple-ha2dqmi)

**[- setFetchSpecification:](#apple-gi3de)

**[- setFetchSpecificationByName:](#apple-haytsma)**************

**Accessing objects used for fetching**

**[- entity](#apple-haztgny)

**[- databaseContext](#apple-giztg)****

**Enabling fetching**

**[- setFetchEnabled:](#apple-gi2tq)

**[- isFetchEnabled](#apple-gi2ta)****

**Accessing qualifier bindings**

**[- qualifierBindingKeys](#apple-ha2tsmy)

**[- qualifierBindings](#apple-ha3damq)

**[- setQualifierBindings:](#apple-ha3dgoi)******

---

## Instance Methods

---

### auxiliaryQualifier

- (EOQualifier \*)`auxiliaryQualifier`

Returns the EOQualifier used to further filter the objects fetched by the receiver's EOFetchSpecification (in EOControl).

__See also:__
[- `setAuxiliaryQualifier:`](#apple-ha2dqmi), [- `fetchSpecificationForFetch`](#apple-gi2dg), [- `fetchSpecification`](#apple-gi3tsny)

---

### databaseContext

- (EODatabaseContext \*)`databaseContext`

Returns the EODatabaseContext that the receiver uses to access the external database. This is either the root EOObjectStore for the receiver's EOEditingContext, or if the root is an EOCooperatingObjectStore, it's the EODatabaseContext under that EOCooperatingObjectStore that services the EOModel containing the EOEntity for the receiver. (EOObjectStore, EOEditingContext, and EOCooperatingObjectStore are all defined in EOControl.)

Deletes _anObject_ from the data source. This method raises an exception on failure. If the receiver registers undos for the deletion, the receiver may receive a possibly redundant `insertObject` call.

---

### entity

- (EOEntity \*)`entity`

Returns the EOEntity from which the receiver fetches objects.

---

### fetchSpecification

- (EOFetchSpecification \*)`fetchSpecification`

Returns the receiver's basic EOFetchSpecification. Its EOQualifier is conjoined with the receiver's auxiliary EOQualifier when the receiver fetches objects. The sender of this message can alter the EOFetchSpecification directly, or replace it using [`setFetchSpecification:`](#apple-gi3de).

__See also:__
[`fetchSpecificationForFetch`](#apple-gi2dg), [`auxiliaryQualifier`](#apple-gi3deoi)

---

### fetchSpecificationForFetch

- (EOFetchSpecification \*)`fetchSpecificationForFetch`

Returns a copy of the EOFetchSpecification that the receiver uses to fetch. This is constructed by conjoining the EOQualifier of the receiver's EOFetchSpecification with its auxiliary EOQualifier. Modifying the returned EOFetchSpecification doesn't affect the receiver's fetching behavior; use [`setFetchSpecification:`](#apple-gi3de) and [`setAuxiliaryQualifier:`](#apple-ha2dqmi) for that purpose.

__See also:__
[- `fetchSpecification`](#apple-gi3tsny), [- `auxiliaryQualifier`](#apple-gi3deoi)

---

### fetchSpecificationName

- (NSString \*)`fetchSpecificationName`

Returns the name of the fetch specification (or `nil` if there is no name).

__See also:__
[- `setFetchSpecificationByName:`](#apple-haytsma)

---

### initWithEditingContext:entityName:

- (id)`initWithEditingContext:`(EOEditingContext \*)_anEditingContext_`entityName:`(NSString \*)_anEntityName_

Initializes a newly allocated EODatabaseDataSource to fetch objects into _anEditingContext_ for the EOEntity named by _anEntityName_. This method checks _anEditingContext_'s EOObjectStoreCoordinator for an EODatabaseChannel that services the EOModel containing the named EOEntity. If none exists, this method creates one. This method works by calling [`initWithEditingContext:entityName:fetchSpecificationName:`](#apple-haytcoa) and specifying `nil` for the fetchSpecificationName.

---

### initWithEditingContext:entityName:fetchSpecificationName:

- (id)`initWithEditingContext:`(EOEditingContext \*)_anEditingContext_`entityName:`(NSString \*)_anEntityName_`fetchSpecificationName:`(NSString \*)_fetchSpecificationName_

Initializes a newly allocated EODatabaseDataSource to fetch objects into _anEditingContext_ for the EOEntity named by _anEntityName_. This method checks _anEditingContext_'s EOObjectStoreCoordinator for an EODatabaseChannel that services the EOModel containing the named EOEntity. If none exists, this method creates one. The _fetchSpecificationName_ argument is used to find the named fetch specification in the entity. If the _fetchSpecificationName_ is `nil`, a new fetch specification will be instantiated that will fetch all objects of the entity. This is the primitive initializer. Returns `self`.

Inserts _object into the data source_.

---

### isFetchEnabled

- (BOOL)`isFetchEnabled`

Returns YES if the receiver's `fetchObjects` method actually fetches objects, NO if it returns an empty array without fetching. Fetching is typically disabled in a master-peer configuration when no object is selected in the master.

__See also:__
[- `setFetchEnabled:`](#apple-gi2tq)

---

### qualifierBindingKeys

- (NSArray \*)`qualifierBindingKeys`

Returns an array of strings which is a union of the binding keys from the fetch specification's qualifier and the data source's auxiliary qualifier.

__See also:__
[- `setQualifierBindings:`](#apple-ha3dgoi)

---

### qualifierBindings

- (NSDictionary \*)`qualifierBindings`

Returns a set of bindings that will be used for variable replacement on the fetch specification's qualifier and the auxiliary qualifier before the fetch is executed.

__See also:__
[- `setQualifierBindings:`](#apple-ha3dgoi)

---

### setAuxiliaryQualifier:

- (void)`setAuxiliaryQualifier:`(EOQualifier \*)_aQualifier_

Sets the receiver's auxiliary qualifier to _aQualifier_. The auxiliary qualifier usually adds conditions to the primary qualifier and is useful for narrowing the scope of a data source without altering its primary qualifier. This is especially useful for setting a qualifier on a qualified peer data source, since a peer's primary qualifiers specifies the matching criteria for the relationship it fetches for. For more information on auxiliary qualifiers, see "Creating a Master-Peer Configuration" in the "WebObjects Programming Topics."

__See also:__
[- `fetchSpecificationForFetch`](#apple-gi2dg), [- `fetchSpecification`](#apple-gi3tsny), [- `auxiliaryQualifier`](#apple-gi3deoi)

---

### setFetchEnabled:

- (void)`setFetchEnabled:`(BOOL)_flag_

Controls whether the receiver can fetch. If _flag_ is YES the receiver's `fetchObjects` method actually fetches objects, if NO it returns an empty array without fetching. Fetching is typically disabled in a master-peer configuration when no object is selected in the master. For example, EODatabaseDataSource's implementation of

---

#

qualifyWithRelationshipKey:ofObject:
invokes this method to enable or disable fetching based on whether a master object is provided.

__See also:__
[- `isFetchEnabled`](#apple-gi2ta)

---

### setFetchSpecification:

- (void)`setFetchSpecification:`(EOFetchSpecification \*)_aFetchSpecification_

Sets the receiver's basic EOFetchSpecification to _aFetchSpecification_. Its EOQualifier is conjoined with the receiver's auxiliary EOQualifier when the receiver fetches objects. This method also sets the name of the fetch specification to nil.

__See also:__
[- `setAuxiliaryQualifier:`](#apple-ha2dqmi), [- `fetchSpecificationForFetch`](#apple-gi2dg), [- `fetchSpecification`](#apple-gi3tsny),
[- `setFetchSpecificationByName:`](#apple-haytsma)

---

### setFetchSpecificationByName:

- (void)`setFetchSpecificationByName:`(NSString \*)_fetchSpecificationName_

Sets the _fetchSpecificationName_ as given, and sets the fetch specification (used when supplying objects) to the named fetch specification of the entity that was used to initialize the data source. This method is an alternative to [`setFetchSpecification:`](#apple-gi3de).

__See also:__
[- `fetchSpecificationName`](#apple-haytkmi)

---

### setQualifierBindings:

- (NSDictionary \*)`setQualifierBindings:`(NSDictionary \*)_bindings_

Sets a set of bindings that will be used for variable replacement on the fetch specification's qualifier and the auxiliary qualifier before the fetch is executed.

__See also:__
[- `qualifierBindingKeys`](#apple-ha2tsmy), [- `qualifierBindings`](#apple-ha3damq)

---

[!](More%20about%20EODatabaseContext.md)
[!](EODatabaseOperation-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
