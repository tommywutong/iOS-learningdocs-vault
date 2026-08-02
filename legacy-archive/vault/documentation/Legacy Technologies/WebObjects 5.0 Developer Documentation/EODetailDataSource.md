---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EODetailDataSource.html
archived_at: '2026-07-15T08:13:46.741647Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EODetailDataSource

> **__Inherits from:__**
> : [EODataSource](EODataSource.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuiylumfjw65lsmnsq)

> **__Implements:__**
> : EOKeyValueArchiving: Serializable

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EODetailDataSource defines a data source for use in master-detail configurations, where operations in the detail data source are applied directly to properties of a master object. EODetailDataSource implements the standard [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwmzlumnue6ytkmvrxi4y), [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxws3ttmvzhit3cnjswg5a), and [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwizlmmv2gkt3cnjswg5a) methods to operate on a relationship property of its master object, so it works for any concrete subclass of EODataSource, including another EODetailDataSource (for a chain of three master and detail data sources).

To set up an EODetailDataSource programmatically, you typically create it by sending a dataSourceQualifiedByKey message to the master data source, then establish the master object with a [qualifyWithRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxxc5lbnruwm6kxnf2gqutfnrqxi2lpnzzwq2lqjnsxs) message. The latter method records the name of a relationship for a particular object to resolve in __fetchObjects__ and to modify in __insertObject__, and __deleteObject__. These three methods then manipulate the relationship property of the master object to perform the operations requested. See the individual method descriptions for more information.

## Method Types

---

> **Constructors**
> : [EODetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxukt2emv2gc2lmirqxiyktn52xey3f)
>
> **Qualifying instances**
> : [qualifyWithRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxxc5lbnruwm6kxnf2gqutfnrqxi2lpnzzwq2lqjnsxs)
>
> **Examining instances**
> : [masterDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxw2yltorsxerdborqvg33vojrwk): [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwizlumfuwys3fpe): [masterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxw2yltorsxet3cnjswg5a)
>
> **Accessing the master class description**
> : [masterClassDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxw2yltorsxeq3mmfzxgrdfonrxe2lqoruw63q): [setMasterClassDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxxgzlujvqxg5dfojbwyyltoncgk43dojuxa5djn5xa)
>
> **Accessing the objects**
> : [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwmzlumnue6ytkmvrxi4y)
>
> **Inserting and deleting objects**
> : [insertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxws3ttmvzhit3cnjswg5a): [deleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwizlmmv2gkt3cnjswg5a)
>
> **Accessing the master editing context**
> : [editingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwkzdjoruw4z2dn5xhizlyoq)

## Constructors

---

### EODetailDataSource

`public EODetailDataSource( EOClassDescription masterClassDescription, String relationshipKey)`

Creates and returns a new EODetailDataSource object. The new data source's [masterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxw2yltorsxet3cnjswg5a) is associated with _masterClassDescription_, and _relationshipKey_ is assigned to the new data source's [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwizlumfuwys3fpe). The constructor invokes [qualifyWithRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxxc5lbnruwm6kxnf2gqutfnrqxi2lpnzzwq2lqjnsxs) specifying _relationshipKey_ as the relationship key and null as the object.

__See Also:__ [masterClassDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxw2yltorsxeq3mmfzxgrdfonrxe2lqoruw63q)

`public EODetailDataSource( EODataSource masterDataSource, String relationshipKey)`

Creates and returns a new EODetailDataSource object. The new data source provides destination objects for the relationship named by _relationshipKey_ from a __masterObject__ in _masterDataSource_.

__See Also:__ [masterDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxw2yltorsxerdborqvg33vojrwk)

---

## Static Methods

---

### decodeWithKeyValueUnarchiver

`public static Object decodeWithKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

## Instance Methods

---

### __classDescriptionForObjects__

`public EOClassDescription classDescriptionForObjects()`

Description forthcoming.

---

### __dataSourceQualifierByKey__

`public EODataSource dataSourceQualifiedByKey(String aKey)`

Description forthcoming.

---

### deleteObject

`public void deleteObject(Object anObject)`

Sends a removeObjectFromPropertyWithKey message (defined in the EORelationshipManipulation interface) to the master object with _anObject_ and the receiver's detail key as the arguments. Throws an exception if there's no master object or no detail key set.

---

### detailKey

`public String detailKey()`

Returns the name of the relationship for which the receiver provides objects, as provided to the constructor when the receiver was createdor as set in [qualifyWithRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxxc5lbnruwm6kxnf2gqutfnrqxi2lpnzzwq2lqjnsxs). If none has been set yet, returns `null`.

---

### editingContext

`public EOEditingContext editingContext()`

Returns the EOEditingContext of the master object, or `null` if there isn't one.

---

### encodeWithKeyValueUnarchiver

`public void encodeWithKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

### fetchObjects

`public NSArray fetchObjects()`

Sends valueForKey (defined in the NSKeyValueCoding interface) to the master object with the receiver's detail key as the argument, constructs an array for the returned object or objects, and returns it. Returns an empty array if there's no master object, or returns an array containing the master object itself if no detail key is set.

---

### insertObject

`public void insertObject(Object anObject)`

Sends an addObjectToBothSidesOfRelationshipWithKey message (defined in the EORelationshipManipulation interface) to the master object with _anObject_ and the receiver's detail key as the arguments. Throws an exception if there's no master object or no detail key set.

---

### masterClassDescription

`public EOClassDescription masterClassDescription()`

Returns the EOClassDescription of the receiver's master object.

__See Also:__ [setMasterClassDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxxgzlujvqxg5dfojbwyyltoncgk43dojuxa5djn5xa), [EODetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxukt2emv2gc2lmirqxiyktn52xey3f) constructor

---

### masterDataSource

`public EODataSource masterDataSource()`

Returns the receiver's master data source.

__See Also:__ [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwizlumfuwys3fpe), [EODetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxukt2emv2gc2lmirqxiyktn52xey3f) constructor

---

### masterObject

`public Object masterObject()`

Returns the object in the master data source for which the receiver provides objects. You can change this with a [qualifyWithRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxxc5lbnruwm6kxnf2gqutfnrqxi2lpnzzwq2lqjnsxs) message.

__See Also:__ [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwizlumfuwys3fpe)

---

### __qualifyWithRelationshipKey__

`public void qualifyWithRelationshipKey( String relationshipKey, Object masterObject)`

Configures the receiver to provide objects based on the relationship of _masterObject_ named by _relationshipKey_. _relationshipKey_ can be different from the one provided to the constructor, which changes the relationship the receiver operates on. If _masterObject_ is `null`, this method causes the receiver to return an empty array when sent a [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwmzlumnue6ytkmvrxi4y) message.

__See Also:__ [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxwizlumfuwys3fpe)

---

### setDetailKey

`public void setDetailKey(String detailKey)`

Description forthcoming.

---

### setMasterClassDescription

`public void setMasterClassDescription(EOClassDescription classDescription)`

Assigns _classDescription_ as the EOClassDescription for the receiver's master object.

__See Also:__ [masterClassDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirsxiyljnrcgc5dbknxxk4tdmuxw2yltorsxeq3mmfzxgrdfonrxe2lqoruw63q)

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
