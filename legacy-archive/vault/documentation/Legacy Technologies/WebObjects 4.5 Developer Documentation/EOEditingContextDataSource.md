---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOEditingContextDataSrc.html
archived_at: '2026-07-15T08:11:37.531144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOEditingContextDataSource

> **__Inherits
> from:__**
> : [EODataSource](EODataSource.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuiylumfjw65lsmnsq) : Object

> **__Package:__**
> : com.apple.client.eocontrol

---

## Class Description

---

EOEditingContextDataSource is a concrete subclass
of EODataSource that uses an EOEditingContext as its source of objects.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eocontrol package. |

EOEditingContextDataSource implements all the functionality
defined by EODataSource: In addition to fetching objects, it can
insert and delete them (provided the entity isn't read-only).
See the EODataSource class specification for more information on
these topics.

EOEditingContextDataSource provides several methods in addition
to those defined by EODataSource. The additional methods- [fetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpmzsxiy3iivxgcytmmvsa) and [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirtforrwqrlomfrgyzle), [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpmzsxiy3iknygky3jmzuwgylunfxw4) and [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirtforrwqu3qmvrwsztjmnqxi2lpny),
and [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxiulvmfwgsztjmvza)-are
added to support enabling and disabling fetching and to support
fetching with an EOFetchSpecification.

## Method Types

---

> **Constructors**
> : [EOEditingContextDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpivhukzdjoruw4z2dn5xhizlyorcgc5dbknxxk4tdmu)
>
> **Fetching objects**
> : [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpmzsxiy3ij5rguzldorzq)
> : [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirtforrwqu3qmvrwsztjmnqxi2lpny)
> : [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpmzsxiy3iknygky3jmzuwgylunfxw4)
> : [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxiulvmfwgsztjmvza)
>
> **Enabling fetching**
> : [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirtforrwqrlomfrgyzle)
> : [fetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpmzsxiy3iivxgcytmmvsa)
> : [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirlenf2gs3thinxw45dfpb2a)

## Constructors

---

### EOEditingContextDataSource

`public EOEditingContextDataSource(String entityName)`

`public EOEditingContextDataSource(
EOEditingContext anEditingContext,
String entityName)`

Creates and returns a new EOEditingContextDataSource
for the entity identified by _entityName._
If _anEditingContext_ is provided,
the new data source uses it as its source of objects, and fetching
on the new data source is enabled. If anEditingContext isn't provided,
you must assign one with [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirlenf2gs3thinxw45dfpb2a);
until you assign one, fetching is disabled.

__See
Also:__  [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirtforrwqrlomfrgyzle)

---

## Instance Methods

---

### fetchEnabled

`public boolean fetchEnabled()`

Returns `true` if fetching
is enabled, `false` if not.

__See
Also:__  [EOEditingContextDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpivhukzdjoruw4z2dn5xhizlyorcgc5dbknxxk4tdmu) constructor, [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirtforrwqrlomfrgyzle), [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirlenf2gs3thinxw45dfpb2a)

---

### fetchObjects

`public NSArray fetchObjects()`

If fetching is enabled, fetches and returns
objects with the receiver's fetch specification; `null` otherwise.

---

### fetchSpecification

`public EOFetchSpecification fetchSpecification()`

Returns the receiver's fetch specification,
which fetches all the objects for the receiver's entity until
it is further restricted with [setFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirtforrwqu3qmvrwsztjmnqxi2lpny) or [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxiulvmfwgsztjmvza).

---

### setEditingContext

`public void setEditingContext(EOEditingContext anEditingContext)`

Sets the receiver's editing context to _anEditingContext._
If _anEditingContext_ is non-`null`,
fetching is enabled.

__See Also:__  [setFetchEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirtforrwqrlomfrgyzle)

---

### setFetchEnabled

`public void setFetchEnabled(boolean flag)`

Sets whether or not fetching is enabled in the
receiver.

__See Also:__  [EOEditingContextDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpivhukzdjoruw4z2dn5xhizlyorcgc5dbknxxk4tdmu) constructor, [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjponsxirlenf2gs3thinxw45dfpb2a)

---

### setFetchSpecification

`public void setFetchSpecification(EOFetchSpecification fetchSpec)`

Assigns _fetchSpec_ to
the receiver as the fetch specification to use when fetching objects.

__See
Also:__  [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5cemf2gcu3povzggzjpmzsxiy3iknygky3jmzuwgylunfxw4)

---

### setQualifier

`public void setQualifier(EOQualifier aQualifier)`

Assigns _aQualifier_ to
the receiver's fetch specification.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
