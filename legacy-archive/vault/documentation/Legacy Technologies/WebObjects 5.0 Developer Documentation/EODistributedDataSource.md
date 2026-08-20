---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EODistributionRef/Java/Client/Classes/EODistributedDataSource.html
archived_at: '2026-07-15T08:13:48.532873Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EODistributionRef/Java/Client/Art/up.gif)](../../EODistributionTOC.md) 

# EODistributedDataSource

> **__Inherits from:__**
> : EODataSource : Object

> **__Package:__**
> : com.webobjects.eodistribution.client

---

## Class Description

---

EODistributedDataSource is a concrete subclass of EODataSource (defined in EOControl) that fetches using an EOEditingContext as its source of objects; the editing context, in turn, forwards the fetch requests to its object store (usually an instance of EODistributedObjectStore) where it is ultimately serviced by an EODatabaseContext on the server.

EODistributedDataSource implements all the functionality defined by EODataSource: In addition to fetching objects, it can insert and delete them (provided the entity isn't read-only). See the EODataSource class specification for more information on these topics.

EODistributedDataSource provides several methods in addition to those defined by EODataSource. The additional methods- [fetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxwmzlumnuek3tbmjwgkza) and [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluizsxiy3iivxgcytmmvsa), [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxwmzlumnufg4dfmnuwm2ldmf2gs33o) and [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluizsxiy3iknygky3jmzuwgylunfxw4), and [setAuxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluif2xq2lmnfqxe6krovqwy2lgnfsxe)-are added to support enabling and disabling fetching and to support fetching with an EOFetchSpecification.

## Method Types

---

> **Fetching objects**
>
> : [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxwmzlumnue6ytkmvrxi4y): [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluizsxiy3iknygky3jmzuwgylunfxw4): [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxwmzlumnufg4dfmnuwm2ldmf2gs33o): [setAuxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluif2xq2lmnfqxe6krovqwy2lgnfsxe)
>
> **Enabling fetching**
>
> : [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluizsxiy3iivxgcytmmvsa): [fetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxwmzlumnuek3tbmjwgkza): [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluivsgs5djnztug33oorsxq5a)

## Constructors

---

### __EODistributedDataSource__

`public EODistributedDataSource(String entityName)`

`public EODistributedDataSource( EOEditingContext anEditingContext, String entityName)`

`public EODistributedDataSource( EOEditingContext anEditingContext, String entityName, String fetchSpecification)`

Creates and returns a new EODistributedDataSource for the entity identified by _entityName_. If _anEditingContext_ is provided, the new data source uses it as its source of objects and fetching is enabled. If it isn't provided, you must assign one with [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluivsgs5djnztug33oorsxq5a); until you do, fetching is disabled. The three-argument constructor allows you to designate a fetch specification (_fetchSpecification_) to be used by the initialized instance.

__See Also:__ [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluizsxiy3iivxgcytmmvsa)

---

## Instance Methods

---

### fetchEnabled

`public boolean fetchEnabled()`

Returns __true__ if fetching is enabled, __false__ if not.

__See Also:__ [EODistributedDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxukt2enfzxi4tjmj2xizleirqxiyktn52xey3f) constructor, [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluizsxiy3iivxgcytmmvsa), [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluivsgs5djnztug33oorsxq5a)

---

### fetchObjects

`public NSArray fetchObjects()`

If fetching is enabled, fetches and returns objects with the receiver's fetch specification; returns __null__ otherwise.

---

### fetchSpecification

`public EOFetchSpecification fetchSpecification()`

Returns the receiver's fetch specification, which fetches all the objects for the receiver's entity until it is further restricted with [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluizsxiy3iknygky3jmzuwgylunfxw4) or [setAuxiliaryQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluif2xq2lmnfqxe6krovqwy2lgnfsxe).

---

### setAuxiliaryQualifier

`public void setAuxiliaryQualifier(EOQualifier aQualifier)`

Assigns auxiliary qualifier _aQualifier_ to the receiver's fetch specification. This qualifier is combined with the qualifier with the fetch specification with an AND.

---

### setEditingContext

`public void setEditingContext(EOEditingContext anEditingContext)`

Sets the receiver's editing context to _anEditingContext_. If _anEditingContext_ is __null__, fetching is disabled.

__See Also:__ [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluizsxiy3iivxgcytmmvsa)

---

### setFetchEnabled

`public void setFetchEnabled(boolean flag)`

Sets whether or not fetching is enabled in the receiver.

__See Also:__ [EODistributedDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxukt2enfzxi4tjmj2xizleirqxiyktn52xey3f) constructor, [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxxgzluivsgs5djnztug33oorsxq5a)

---

### setFetchSpecification

`public void setFetchSpecification(EOFetchSpecification fetchSpec)`

Assigns _fetchSpec_ to the receiver as the fetch specification to use when fetching objects.

__See Also:__ [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5dfmrcgc5dbknxxk4tdmuxwmzlumnufg4dfmnuwm2ldmf2gs33o)

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/EODistributionRef/Java/Client/Art/up.gif)](../../EODistributionTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
