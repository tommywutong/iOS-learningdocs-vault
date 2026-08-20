---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EORelationshipMnpltn.html
archived_at: '2026-07-15T08:11:43.559854Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EORelationshipManipulation

> __(informal protocol)__

> __Declared in:__ : EOControl/EOClassDescription.h

---

## Protocol Description

---

The EORelationshipManipulation informal protocol builds on
the basic EOKeyValueCoding informal protocol to allow you to modify
to-many relationship properties. the Framework additions to NSObject provide
default implementations of EORelationshipManipulation, which you
rarely (if ever) need to override.

The primitive methods [addObject:toPropertyWithKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3bmrse6ytkmvrxiotun5ihe33qmvzhi6kxnf2gqs3fpe5a) and [removeObject:fromPropertyWithKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3smvww65tfj5rguzldoq5gm4tpnvihe33qmvzhi6kxnf2gqs3fpe5a) add and
remove single objects from to-many relationship arrays. The two
other methods in the informal protocol, [addObject:toBothSidesOfRelationshipWithKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3bmrse6ytkmvrxiotun5bg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe5a) and [removeObject:fromBothSidesOfRelationshipWithKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3smvww65tfj5rguzldoq5gm4tpnvbg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe5a),
are implemented in terms of the two primitives to handle reciprocal
relationships. These methods find the inverse relationship to the
one identified by the specified key (if there is such an inverse
relationship) and use __addObject:toPropertyWithKey:__ and __removeObject:fromPropertyWithKey:__ to
alter both relationships, whether they're to-one or to-many.

The primitive methods check first for a method you might implement, __addTo___Key_ or __removeFrom___Key_, invoking
that method if it's implemented, otherwise using the basic key-value
coding methods to do the work. Consequently, you rarely need to
provide your own implementations of EORelationshipManipulation.
Rather, you can provide relationship accessors (__addTo___Key_ or __removeFrom___Key_)
whenever you need to implement custom business logic.

## Instance Methods

---

### addObject:toBothSidesOfRelationshipWithKey:

`- (void)addObject:(id)anObject
toBothSidesOfRelationshipWithKey:(NSString
*)key`

Sets or adds _anObject_ as
the destination for the receiver's relationship identified by _key_,
and also sets or adds the receiver for _anObject_'s
reciprocal relationship if there is one. For a to-one relationship, _anObject_ is
set using [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi). For a to-many
relationship, _anObject_ is added using [addObject:toBothSidesOfRelationshipWithKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3bmrse6ytkmvrxiotun5bg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe5a).

This method also properly handles removing `self` and _anObject_ from
their previous relationship as needed. For example, if an Employee
object belongs to the Research department, invoking this method with
the Maintenance department removes the Employee from the Research
department as well as setting the Employee's department to Maintenance.

---

### addObject:toPropertyWithKey:

`- (void)addObject:(id)anObject
toPropertyWithKey:(NSString *)key`

Adds _anObject_ to
the receiver's to-many relationship identified by _key_,
without setting a reciprocal relationship. Similar to the implementation
of [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi), NSObject's implementation
of this method first attempts to invoke a method of the form __addTo___Key_:.
If the receiver doesn't have such a method, this method gets the
property array using [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi) and operates directly
on that. For a to-many relationship, this method adds _anObject_ to
the array if it is not already in the array. For a to-one relationship,
this method replaces the previous value with _anObject_.

---

### removeObject:fromBothSidesOfRelationshipWithKey:

`- (void)removeObject:(id)anObject
fromBothSidesOfRelationshipWithKey:(NSString
*)key`

Removes _anObject_ from
the receiver's relationship identified by _key_,
and also removes the receiver from _anObject_'s
reciprocal relationship if there is one. For a to-one relationship, _anObject_ is
removed using [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi) with `nil` as
the value. For a to-many relationship, _anObject_ is
removed using [removeObject:fromPropertyWithKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3smvww65tfj5rguzldoq5gm4tpnvihe33qmvzhi6kxnf2gqs3fpe5a).

---

### removeObject:fromPropertyWithKey:

`- (void)removeObject:(id)anObject
fromPropertyWithKey:(NSString
*)key`

Removes _anObject_ from
the receiver's to-many relationship identified by _key_,
without modifying a reciprocal relationship. Similar to the implementation
of [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi), NSObject's implementation
of this method first attempts to invoke a method of the form __removeFrom___Key___:__.
If the receiver doesn't have such a method, this method gets the
property array using [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi) and operates directly
on that. For a to-many relationship, this method removes _anObject_ from
the array. For a to-one relationship, this method replaces _anObject_ with `nil`.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
