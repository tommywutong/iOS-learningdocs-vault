---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOClassDescClassDelegate.html
archived_at: '2026-07-18T01:28:40.855601Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](NSObject%20Additions.md)
[!](EOEditingContextDelegate.md)

---

# EOClassDescriptionClassDelegate

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOClassDescription.h

## Category Description

The EOClassDescriptionClassDelegate informal protocol defines a method that the EOClassDescription class can invoke in its delegate. Delegates are not required to provide an implementation for the method. Instead, declare and implement the method if you need it, and use the EOClassDescription method [__setClassDelegate:__](EOClassDescription-3.md)method to assign your object as the class delegate. The EOClassDescription class can determine if the delegate doesn't implement the delegate method and only attempts to invoke it if it's actually implemented.

---

#### shouldPropagateDeleteForObject:inEditingContext:forRelationshipKey:

- (BOOL)`shouldPropagateDeleteForObject:`(id)_anObject_
`inEditingContext:`(EOEditingContext \*)_anEditingContext_
`forRelationshipKey:`(NSString \*)_key_

Invoked from [__propagateDeleteForObject:editingContext:__](EOClassDescription-3.md). If the class delegate returns NO, it prevents _anObject_ in _anEditingContext_ from propagating deletion to the objects at the destination of _key_. This can be useful if you have a large model and a small application that only deals with a subset of the model's entities. In such a case you might want to disable delete propagation to entities that will never be accessed. You should use this method with caution, however-returning NO and not propagating deletion can lead to dangling references in your object graph.

---

[!](NSObject%20Additions.md)
[!](EOEditingContextDelegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
