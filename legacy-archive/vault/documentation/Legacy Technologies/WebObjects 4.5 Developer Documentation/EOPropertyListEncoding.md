---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOPropertyListEncoding.html
archived_at: '2026-07-15T08:11:33.262650Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOPropertyListEncoding

> __Implemented by:__
> [EOAttribute](EOAttribute.md#apple-incuqq2ijfeue)
> [EOEntity](EOEntity.md#apple-irauuq2ginduu)
> [EORelationship](EORelationship.md#apple-ijdegrchi5auo)
> [EOStoredProcedure](EOStoredProcedure.md#apple-inbuuqsdjjeei)

> __Package:__
> com.apple.yellow.eoaccess

## Interface Description

---

The EOPropertyListEncoding interface declares methods that
read and write objects to __property lists__-a
dictionary containing only property list data types (that is, NSDictionary
objects, Strings, NSArray objects, and NSData objects).

Classes that implement this interface must also provide a
constructor that creates objects from a property list and an owner:

> ```
> public ClassName(NSDictionary propertyList, Object owner)
> ```

Objects created with a constructor of this type are initialized
from the provided property list. The owner argument is optional
and should be used only by objects requiring a reference to their
owner. The newly created object isn't considered fully functional
until it receives an [awakeWithPropertyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5qxoyllmvlws5dikbzg64dfoj2hstdjon2a) message,
which finishes initializing the object. The __awakeWithPropertyList__ invocation
should be deferred until after all of the objects identified in
the property list have been created.

The method [encodeIntoPropertyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkbzg64dfoj2hstdjon2ek3tdn5sgs3thf5sw4y3pmrsus3tun5ihe33qmvzhi6kmnfzxi) is
responsible for encoding the receiver into a property list for later
restoration.

This interface is used to read and write modeling objects
(EOModel, EOEntity, EOAttribute, and so on) to a model file.

## Instance Methods

---

### awakeWithPropertyList

`public abstract void awakeWithPropertyList(NSDictionary propertyList)`

Finishes initializing the receiver from _propertyList_,
which must have been created with a constructor of the form:
> ```
> public ClassName(NSDictionary propertyList, Object owner)
> ```

__awakeWithPropertyList__ is
responsible for restoring references to other objects. Consequently,
it should not be invoked until all other objects that the receiver
might reference have been created from _propertyList_.

---

### encodeIntoPropertyList

`public abstract void encodeIntoPropertyList(NSMutableDictionary propertyList)`

Encodes the receiver as a property list.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
