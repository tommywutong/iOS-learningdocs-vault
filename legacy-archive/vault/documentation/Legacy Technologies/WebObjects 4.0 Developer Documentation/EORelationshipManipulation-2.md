---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EORelManipulation.html
archived_at: '2026-07-18T01:28:41.683861Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOQualifierEvaluation-2.md)
[!](EOQualifierComparison.md)

---

# EORelationshipManipulation

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOClassDescription.h

## Protocol Description

The EORelationshipManipulation informal protocol builds on the basic EOKeyValueCoding informal protocol to allow you to modify to-many relationship properties. the Framework additions to NSObject provide default implementations of EORelationshipManipulation, which you rarely (if ever) need to override.

The primitive methods __addObject:toPropertyWithKey:__ and __removeObject:fromPropertyWithKey:__ add and remove single objects from to-many relationship arrays. The two other methods in the informal protocol, __addObject:toBothSidesOfRelationshipWithKey:__ and __removeObject:fromBothSidesOfRelationshipWithKey:__ , are implemented in terms of the two primitives to handle reciprocal relationships. These methods find the inverse relationship to the one identified by the specified key (if there is such an inverse relationship) and use __addObject:toPropertyWithKey:__ and __removeObject:fromPropertyWithKey:__ to alter both relationships, whether they're to-one or to-many.

The primitive methods check first for a method you might implement, __addTo__ _Key_ or __removeFrom__ _Key_, invoking that method if it's implemented, otherwise using the basic key-value coding methods to do the work. Consequently, you rarely need to provide your own implementations of EORelationshipManipulation. Rather, you can provide relationship accessors (__addTo__ _Key_ or __removeFrom__ _Key_) whenever you need to implement custom business logic.

---

#### addObject:toBothSidesOfRelationshipWithKey:

- (void)__addObject:__ (id)_anObject___toBothSidesOfRelationshipWithKey:__ (NSString \*)_key_

Sets or adds _anObject_ as the destination for the receiver's relationship identified by _key_, and also sets or adds the receiver for _anObject_'s reciprocal relationship if there is one. For a to-one relationship, _anObject_ is set using __[takeValue:forKey:](EOKeyValueCoding-3.md)__ . For a to-many relationship, _anObject_ is added using __addObject:toBothSidesOfRelationshipWithKey:__ .

This method also properly handles removing __self__ and _anObject_ from their previous relationship as needed. For example, if an Employee object belongs to the Research department, invoking this method with the Maintenance department removes the Employee from the Research department as well as setting the Employee's department to Maintenance.

---

#### addObject:toPropertyWithKey:

- (void)__addObject:__ (id)_anObject___toPropertyWithKey:__ (NSString \*)_key_

Adds _anObject_ to the receiver's to-many relationship identified by _key_, without setting a reciprocal relationship. Similar to the implementation of __[takeValue:forKey:](EOKeyValueCoding-3.md)__ , NSObject's implementation of this method first attempts to invoke a method of the form __addTo__ _Key___:__ . If the receiver doesn't have such a method, this method gets the property array using [__valueForKey:__](EOKeyValueCoding-3.md)and operates directly on that. For a to-many relationship, this method adds _anObject_ to the array if it is not already in the array. For a to-one relationship, this method replaces the previous value with _anObject_ .

---

#### removeObject:fromBothSidesOfRelationshipWithKey:

- (void)__removeObject:__ (id)_anObject___fromBothSidesOfRelationshipWithKey:__ (NSString \*)_key_

Removes _anObject_ from the receiver's relationship identified by _key_, and also removes the receiver from _anObject_'s reciprocal relationship if there is one. For a to-one relationship, _anObject_ is removed using __[takeValue:forKey:](EOKeyValueCoding-3.md)__ with __nil__ as the value. For a to-many relationship, _anObject_ is removed using __removeObject:fromPropertyWithKey:__ .

---

#### removeObject:fromPropertyWithKey:

- (void)__removeObject:__ (id)_anObject___fromPropertyWithKey:__ (NSString \*)_key_

Removes _anObject_ from the receiver's to-many relationship identified by _key_, without modifying a reciprocal relationship. Similar to the implementation of __[takeValue:forKey:](EOKeyValueCoding-3.md)__ , NSObject's implementation of this method first attempts to invoke a method of the form __removeFrom__ _Key___:__ . If the receiver doesn't have such a method, this method gets the property array using [__valueForKey:__](EOKeyValueCoding-3.md)and operates directly on that. For a to-many relationship, this method removes _anObject_ from the array. For a to-one relationship, this method replaces _anObject_ with nil.

---

[!](EOQualifierEvaluation-2.md)
[!](EOQualifierComparison.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
