---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOPropertyListEncoding.html
archived_at: '2026-07-18T01:28:24.306209Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOModelGroupDelegation.md)
[!](EOQualifierSQLGeneration.md)

---

EOPropertyListEncoding

[EOAttribute](EOAttribute-2.md)
[EOEntity](EOEntity-2.md)
[EORelationship](EORelationship-2.md)
[EOStoredProcedure](EOStoredProcedure-2.md)

The EOPropertyListEncoding protocol declares methods that read and write objects to _property lists_-a dictionary containing only property list data types (that is, NSDictionary objects, NStrings, NSArray objects, and NSData objects).

Classes that implement this protocol must also initialize their instances with [`initWithPropertyList:owner:`](#apple-gi3tgny).

Objects initialized with `initWithPropertyList:owner:` are initialized from _propertyList_. The _owner_ argument is optional and should be used only by objects requiring a reference to their owner. The newly created object isn't considered fully functional until it receives an [`awakeWithPropertyList`](#apple-hazto) message, which finishes initializing the object. The `awakeWithPropertyList` invocation should be deferred until after all of the objects identified in _propertyList_ have been created.

The method [`encodeIntoPropertyList:`](#apple-ha3di) is responsible for encoding the receiver into a property list for later restoration.

This interface is used to read and write modeling objects (EOModel, EOEntity, EOAttribute, and so on) to a model file.

---

### awakeWithPropertyList

- (void)`awakeWithPropertyList:`(NSDictionary \*)_propertyList_

Finishes initializing the receiver from _propertyList_, which must have been initialized with [`initWithPropertyList:owner:`](#apple-gi3tgny).

`awakeWithPropertyList` is responsible for restoring references to other objects. Consequently, it should not be invoked until all other objects that the receiver might reference have been initialized from _propertyList_.

---

### encodeIntoPropertyList:

- (void)`encodeIntoPropertyList:`(NSMutableDictionary \*)_propertyList_

Returns the receiver as a property list.

---

### initWithPropertyList:owner:

- `initWithPropertyList:`(NSDictionary \*)_propertyList_ `owner:`(id)_owner_

Intializes a newly-allocated object from a property list. owner is optional, and should be used by objects requiring a back pointer to their owner. This method must be followed by a call to [`awakeWithPropertyList`](#apple-hazto) in order to create a fully-functional object. The call to `awakeWithPropertyList` should be deferred until after all other objects have been sent `init` messages.

---

[!](EOModelGroupDelegation.md)
[!](EOQualifierSQLGeneration.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
