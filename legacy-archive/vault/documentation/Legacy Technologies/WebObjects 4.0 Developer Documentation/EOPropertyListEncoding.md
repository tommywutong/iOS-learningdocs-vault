---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOPropertyListEncoding.html
archived_at: '2026-07-18T01:28:14.869474Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOModelGroup.Delegate.md)

---

# EOPropertyListEncoding

[EOAttribute](EOAttribute.md)
[EOEntity](EOEntity.md)
[EORelationship](EORelationship.md)
[EOStoredProcedure](EOStoredProcedure.md)

The EOPropertyListEncoding interface declares methods that read and write objects to _property lists_-a dictionary containing only property list data types (that is, NSDictionary objects, java.lang.Strings, NSArray objects, and NSData objects).

Classes that implement this interface must also provide a constructor that creates objects from a property list and an owner:

public _ClassName_(NSDictionary _propertyList_, java.lang.Object _owner_)

Objects created with a constructor of this type are initialized from _propertyList_. The _owner_ argument is optional and should be used only by objects requiring a reference to their owner. The newly created object isn't considered fully functional until it receives an [`awakeWithPropertyList`](#apple-hazto) message, which finishes initializing the object. The `awakeWithPropertyList` invocation should be deferred until after all of the objects identified in _propertyList_ have been created.

The method [`encodeIntoPropertyList`](#apple-ha3di) is responsible for encoding the receiver into a property list for later restoration.

This interface is used to read and write modeling objects (EOModel, EOEntity, EOAttribute, and so on) to a model file.

---

### awakeWithPropertyList

public abstract void `awakeWithPropertyList`(NSDictionary _propertyList_)

Finishes initializing the receiver from _propertyList_, which must have been created with a constructor of the form:

public _ClassName_(NSDictionary _propertyList_, java.lang.Object _owner_)

`awakeWithPropertyList` is responsible for restoring references to other objects. Consequently, it should not be invoked until all other objects that the receiver might reference have been created from _propertyList_.

---

### encodeIntoPropertyList

public abstract void `encodeIntoPropertyList`(NSMutableDictionary _propertyList_)

Returns the receiver as a property list.

---

[!](EOModelGroup.Delegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
