---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EODatabaseDataSource.html
archived_at: '2026-07-15T08:13:41.502181Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

# EODatabaseDataSource

> **__Inherits from:__**
> : com.webobjects.eocontrol.EODataSource

> **__Implements:__**
> : Serializable

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

EODatabaseDataSource is a concrete subclass of EODataSource (defined in EOControl) that fetches objects based on an EOModel, using an EODatabaseContext that services the data source's EOEditingContext (defined in EOControl). An EODatabaseDataSource can be set up to fetch all objects for its root entity, to fetch objects matching a particular EOFetchSpecification, and to further filter its fetching with an auxiliary qualifier.

EODatabaseDataSource implements all the functionality defined by EODataSource: In addition to fetching objects, it can insert and delete them (provided the entity isn't read-only). See the EODataSource class specification for more information on these topics.

As with other data sources, EODatabaseDataSource can also provide a detail data source. The most significant consequence of using an master-detail configuration is that the detail operates directly on the master's object graph. The EODetailDataSource has a __master object__ and a __detail key__ through which the detail data source accesses the its objects. The master object is simply the object that's selected in the master display group, and the detail key is the name of a relationship property in the master object. When the detail display group asks its data source to fetch, the EODetailDataSource simply gets the value for the relationship property identified by the detail key from its master object and returns it. When you add and remove objects from the detail, you're directly modifying the master's relationship array. In fact, you can think of EODetailDataSource as an interface to its master object's relationship property.

## Method Types

---

> **Constructors**
> : [EODatabaseDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl2fj5cgc5dbmjqxgzkemf2gcu3povzggzi)
>
> **Accessing selection criteria**
> : [auxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3bov4gs3djmfzhsulvmfwgsztjmvza): [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xa): [fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xem33sizsxiy3i): [fetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xe4ylnmu): [setAuxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2ec5lynfwgsylspfixkylmnftgszls): [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnufg4dfmnuwm2ldmf2gs33o): [setFetchSpecificationByName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnufg4dfmnuwm2ldmf2gs33oij4u4ylnmu)
>
> **Accessing objects used for fetching**
> : [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3fnz2gs5dz): [databaseContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3emf2gcytbonsug33oorsxq5a)
>
> **Enabling fetching**
> : [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnuek3tbmjwgkza): [isFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3jondgk5ddnbcw4ylcnrswi)
>
> **Accessing qualifier bindings**
> : [qualifierBindingKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3rovqwy2lgnfsxeqtjnzsgs3thjnsxs4y): [qualifierBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3rovqwy2lgnfsxeqtjnzsgs3thom): [setQualifierBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2fc5lbnruwm2lfojbgs3tenfxgo4y)
>
> **Other**
> : [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3emvwgk5dfj5rguzldoq): [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3jnzzwk4tuj5rguzldoq): [dataSourceQualifiedByKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3emf2gcu3povzggzkrovqwy2lgnfswiqtzjnsxs): [qualifyWithRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3rovqwy2lgpflws5dikjswyylunfxw443infyewzlz)

## Constructors

---

### EODatabaseDataSource

`public EODatabaseDataSource( com.webobjects.eocontrol.EOEditingContext anEditingContext, String anEntityName)`

Creates and returns a new EODatabaseDataSource object. The new EODatabaseDataSource fetches objects into _anEditingContext_ for the EOEntity named by _anEntityName_. If anEditingContext's EOObjectStoreCoordinator (EOControl) doesn't have an EODatabaseContext to service the model containing the named entity, one is created. The new data source uses a fetch specification that fetches all the entity's objects.

`public EODatabaseDataSource( com.webobjects.eocontrol.EOEditingContext anEditingContext, String anEntityName, String fetchSpecificationName)`

Creates and returns a new EODatabaseDataSource object. The new EODatabaseDataSource fetches objects into _anEditingContext_ for the EOEntity named by _anEntityName_. If anEditingContext's EOObjectStoreCoordinator (EOControl) doesn't have an EODatabaseContext to service the model containing the named entity, one is created. The _fetchSpecificationName_ argument is used to find the named fetch specification in the entity. If the _fetchSpecificationName_ is not included or is __null__, a new fetch specification that fetches all the entity's objects is created.

---

## Static Methods

---

### __decodeObject__

`public static Object decodeObject(NSCoder object)`

Description forthcoming.

---

### decodeWithKeyValueUnarchiver

`public static Object decodeWithKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

## Instance Methods

---

### auxiliaryQualifier

`public com.webobjects.eocontrol.EOQualifier auxiliaryQualifier()`

Returns the EOQualifier used to further filter the objects fetched by the receiver's EOFetchSpecification (in EOControl).

__See Also:__ [fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xem33sizsxiy3i), [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xa)

---

### awakeFromKeyValueUnarchiver

`public void awakeFromKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.Awaking.

---

### __awakeFromNib__

`public void awakeFromNib()`

Description forthcoming.

---

### __classDescriptionForObjects__

`public com.webobjects.eocontrol.EOClassDescription classDescriptionForObjects()`

Description forthcoming.

---

### __classForCoder__

`public Class classForCoder()`

Description forthcoming.

---

### databaseContext

`public EODatabaseContext databaseContext()`

Returns the EODatabaseContext that the receiver uses to access the external database. This is either the root EOObjectStore for the receiver's EOEditingContext, or if the root is an EOCooperatingObjectStore, it's the EODatabaseContext under that EOCooperatingObjectStore that services the EOModel containing the EOEntity for the receiver. (EOObjectStore, EOEditingContext, and EOCooperatingObjectStore are all defined in EOControl.)

---

### dataSourceQualifiedByKey

`public com.webobjects.eocontrol.EODataSource dataSourceQualifiedByKey(String key)`

Returns a detail data source that provides the destination objects of the relationship named by _key_. The returned detail data source can be qualified by using __qualifierWithKey__ to set a specific master object or to change the relationship key.

---

### deleteObject

`public void deleteObject(Object anObject)`

Deletes _anObject_ from the data source. This method raises an exception on failure. If the receiver registers undos for the deletion, the receiver may receive a possibly redundant [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3jnzzwk4tuj5rguzldoq) call.

---

### __editingContext__

`public com.webobjects.eocontrol.EOEditingContext editingContext()`

Description forthcoming.

---

### __encodeWithCoder__

`public void encodeWithCoder(NSCoder coder)`

Description forthcoming.

---

### encodeWithKeyValueArchiver

`public void encodeWithKeyValueArchiver( com.webobjects.eocontrol.EOKeyValueArchiver archiver)`

Conformance to EOKeyValueArchiving.

---

### entity

`public EOEntity entity()`

Returns the EOEntity from which the receiver fetches objects.

---

### __fetchObjects__

`public NSArray fetchObjects()`

Description forthcoming.

---

### fetchSpecification

`public com.webobjects.eocontrol.EOFetchSpecification fetchSpecification()`

Returns the receiver's basic EOFetchSpecification. Its EOQualifier is conjoined with the receiver's auxiliary EOQualifier when the receiver fetches objects. The sender of this message can alter the EOFetchSpecification directly, or replace it using [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnufg4dfmnuwm2ldmf2gs33o).

__See Also:__ [fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xem33sizsxiy3i), [auxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3bov4gs3djmfzhsulvmfwgsztjmvza)

---

### fetchSpecificationForFetch

`public com.webobjects.eocontrol.EOFetchSpecification fetchSpecificationForFetch()`

Returns a copy of the EOFetchSpecification that the receiver uses to fetch. This is constructed by conjoining the EOQualifier of the receiver's EOFetchSpecification with its auxiliary EOQualifier. Modifying the returned EOFetchSpecification doesn't affect the receiver's fetching behavior; use [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnufg4dfmnuwm2ldmf2gs33o) and [setAuxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2ec5lynfwgsylspfixkylmnftgszls) for that purpose.

__See Also:__ [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xa), [auxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3bov4gs3djmfzhsulvmfwgsztjmvza)

---

### fetchSpecificationName

`public String fetchSpecificationName()`

Returns the name of the fetch specification (or null if there is no name).

__See Also:__ [setFetchSpecificationByName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnufg4dfmnuwm2ldmf2gs33oij4u4ylnmu)

---

### insertObject

`public void insertObject(Object anObject)`

Inserts _anObject_ into the data source.

---

### isFetchEnabled

`public boolean isFetchEnabled()`

Returns true if the receiver's __fetchObjects__ method actually fetches objects, false if it returns an empty array without fetching. Fetching is typically disabled in a master-peer configuration when no object is selected in the master.

__See Also:__ [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnuek3tbmjwgkza)

---

### qualifierBindingKeys

`public NSArray qualifierBindingKeys()`

Returns an array of strings which is a union of the binding keys from the fetch specification's qualifier and the data source's auxiliary qualifier.

__See Also:__ [setQualifierBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2fc5lbnruwm2lfojbgs3tenfxgo4y)

---

### qualifierBindings

`public NSDictionary qualifierBindings()`

Returns a set of bindings that will be used for variable replacement on the fetch specification's qualifier and the auxiliary qualifier before the fetch is executed.

---

### qualifyWithRelationshipKey

`public void qualifyWithRelationshipKey( String key, Object sourceObject)`

Displays destination objects for the relationship named _key_ belonging to _sourceObject_. _key_ should be the same as the key specified in the [dataSourceQualifiedByKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3emf2gcu3povzggzkrovqwy2lgnfswiqtzjnsxs) message that created the receiver. If _sourceObject_ is __null__, the receiver qualifies itself to provide no objects.

---

### setAuxiliaryQualifier

`public void setAuxiliaryQualifier(com.webobjects.eocontrol.EOQualifier aQualifier)`

Sets the receiver's auxiliary qualifier to _aQualifier_. The auxiliary qualifier usually adds conditions to the primary qualifier and is useful for narrowing the scope of a data source without altering its primary qualifier. This is especially useful for setting a qualifier on a qualified peer data source, since a peer's primary qualifiers specifies the matching criteria for the relationship it fetches for. For more information on auxiliary qualifiers, see "Creating a Master-Peer Configuration" in the "WebObjects Programming Topics."

__See Also:__ [fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xem33sizsxiy3i), [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xa)

---

### setFetchEnabled

`public void setFetchEnabled(boolean flag)`

Controls whether the receiver can fetch. If _flag_ is true the receiver's __fetchObjects__ method actually fetches objects, if false it returns an empty array without fetching. Fetching is typically disabled in a master-peer configuration when no object is selected in the master. For example, EODatabaseDataSource's implementation of __qualifyWithRelationshipKey__ invokes this method to enable or disable fetching based on whether a master object is provided.

__See Also:__ [isFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3jondgk5ddnbcw4ylcnrswi)

---

### setFetchSpecification

`public void setFetchSpecification( com.webobjects.eocontrol.EOFetchSpecification fetchSpec)`

Sets the receiver's basic EOFetchSpecification to _fetchSpec_. Its EOQualifier is conjoined with the receiver's auxiliary EOQualifier when the receiver fetches objects. This method also sets the name of the fetch specification to null.

__See Also:__ [setAuxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2ec5lynfwgsylspfixkylmnftgszls), [fetchSpecificationForFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xem33sizsxiy3i), [setFetchSpecificationByName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnufg4dfmnuwm2ldmf2gs33oij4u4ylnmu)

---

### setFetchSpecificationByName

`public void setFetchSpecificationByName(String fetchSpecificationName)`

Sets the _fetchSpecificationName_ as given, and sets the fetch specification (used when supplying objects) to the named fetch specification of the entity that was used to initialize the data source. This method is an alternative to [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3tmv2emzlumnufg4dfmnuwm2ldmf2gs33o).

__See Also:__ [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xa), [fetchSpecificationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3gmv2gg2ctobswg2lgnfrwc5djn5xe4ylnmu)

---

### __setParentDataSourceRelationshipKey__

`public void setParentDataSourceRelationshipKey( com.webobjects.eocontrol.EODataSource dataSource, String key)`

Description forthcoming.

---

### setQualifierBindings

`public void setQualifierBindings(NSDictionary bindings)`

Sets a set of bindings that will be used for variable replacement on the fetch specification's qualifier and the auxiliary qualifier before the fetch is executed.

__See Also:__ [qualifierBindingKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkrdborqvg33vojrwkl3rovqwy2lgnfsxeqtjnzsgs3thjnsxs4y)

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
