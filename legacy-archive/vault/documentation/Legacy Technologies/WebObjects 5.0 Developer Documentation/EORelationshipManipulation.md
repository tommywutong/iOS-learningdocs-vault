---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EORelationshipManipulatio.html
archived_at: '2026-07-15T08:13:48.205524Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EORelationshipManipulation

> __(informal interface)__

> __Implemented by:__ : EOEnterpriseObject: EOCustomObject: EOGenericRecord

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The EORelationshipManipulation interface builds on the basic EOKeyValueCoding interface to allow you to modify to-many relationship properties. EOCustomObject and EOGenericRecord provide default implementations of EORelationshipManipulation, which you rarely (if ever) need to override.

The primitive methods [addObjectToPropertyWithKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpmfsgit3cnjswg5cun5ihe33qmvzhi6kxnf2gqs3fpe) and [removeObjectFromPropertyWithKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpojsw233wmvhwe2tfmn2em4tpnvihe33qmvzhi6kxnf2gqs3fpe) add and remove single objects from to-many relationship arrays. The two other methods in the interface, [addObjectToBothSidesOfRelationshipWithKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpmfsgit3cnjswg5cun5bg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe) and [removeObjectFromBothSidesOfRelationshipWithKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpojsw233wmvhwe2tfmn2em4tpnvbg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe), are implemented in terms of the two primitives to handle reciprocal relationships. These methods find the inverse relationship to the one identified by the specified key (if there is such an inverse relationship) and use __addObjectToPropertyWithKey__ and __removeObjectFromPropertyWithKey__ to alter both relationships, whether they're to-one or to-many.

The primitive methods check first for a method you might implement, __addTo___Key_ or __removeFrom___Key_, invoking that method if it's implemented, otherwise using the basic key-value coding methods to do the work. Consequently, you rarely need to provide your own implementations of EORelationshipManipulation. Rather, you can provide relationship accessors (__addTo___Key_ or __removeFrom___Key_) whenever you need to implement custom business logic.

## Instance Methods

---

### addObjectToBothSidesOfRelationshipWithKey

`public abstract void addObjectToBothSidesOfRelationshipWithKey( EORelationshipManipulation anObject, String key)`

Sets or adds _anObject_ as the destination for the receiver's relationship identified by _key_, and also sets or adds the receiver for _anObject_'s reciprocal relationship if there is one. For a to-one relationship, _anObject_ is set using takeValueForKey. For a to-many relationship, _anObject_ is added using [addObjectToBothSidesOfRelationshipWithKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpmfsgit3cnjswg5cun5bg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe).

This method also properly handles removing `this` and _anObject_ from their previous relationship as needed. For example, if an Employee object belongs to the Research department, invoking this method with the Maintenance department removes the Employee from the Research department as well as setting the Employee's department to Maintenance.

---

### addObjectToPropertyWithKey

`public abstract void addObjectToPropertyWithKey( Object anObject, String key)`

Adds _anObject_ to the receiver's to-many relationship identified by _key_, without setting a reciprocal relationship. Similar to the implementation of takeValueForKey, EOCustomObject's implementation of this method first attempts to invoke a method of the form __addTo___Key_:. If the receiver doesn't have such a method, this method gets the property array using valueForKey and operates directly on that. For a to-many relationship, this method adds _anObject_ to the array if it is not already in the array. For a to-one relationship, this method replaces the previous value with _anObject_.

---

### removeObjectFromBothSidesOfRelationshipWithKey

`public abstract void removeObjectFromBothSidesOfRelationshipWithKey( EORelationshipManipulation anObject, String key)`

Removes _anObject_ from the receiver's relationship identified by _key_, and also removes the receiver from _anObject_'s reciprocal relationship if there is one. For a to-one relationship, _anObject_ is removed using takeValueForKey with `null` as the value. For a to-many relationship, _anObject_ is removed using [removeObjectFromPropertyWithKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkjswyylunfxw443infye2ylonfyhk3dboruw63rpojsw233wmvhwe2tfmn2em4tpnvihe33qmvzhi6kxnf2gqs3fpe).

---

### removeObjectFromPropertyWithKey

`public abstract void removeObjectFromPropertyWithKey( Object anObject, String key)`

Removes _anObject_ from the receiver's to-many relationship identified by _key_, without modifying a reciprocal relationship. Similar to the implementation of takeValueForKey, EOCustomObject's implementation of this method first attempts to invoke a method of the form __removeFrom___Key___:__. If the receiver doesn't have such a method, this method gets the property array using valueForKey and operates directly on that. For a to-many relationship, this method removes _anObject_ from the array. For a to-one relationship, this method replaces _anObject_ with `null`.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
