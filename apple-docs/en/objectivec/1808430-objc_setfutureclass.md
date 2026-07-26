---
title: objc_setFutureClass
framework: Objective-C Runtime
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/1808430-objc_setfutureclass
source_url: 'https://developer.apple.com/documentation/objectivec/1808430-objc_setfutureclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/1808430-objc_setfutureclass.json'
content_hash: 'sha256:bbb79ac05ed56f15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [Objective-C Runtime](objective-c-runtime.md)

# objc_setFutureClass

<sub>Article</sub>

Used by CoreFoundation’s toll-free bridging.

## Overview

Do not call this function yourself.

## See Also

### Working with Classes

- [class_getName](<class_getname(__).md>) — Returns the name of a class.
- [class_getSuperclass](<class_getsuperclass(__).md>) — Returns the superclass of a class.
- [class_setSuperclass](<class_setsuperclass(____).md>) — Sets the superclass of a given class. _(deprecated)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — Returns a Boolean value that indicates whether a class object is a metaclass.
- [class_getInstanceSize](<class_getinstancesize(__).md>) — Returns the size of instances of a class.
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — Returns the `Ivar` for a specified instance variable of a given class.
- [class_getClassVariable](<class_getclassvariable(____).md>) — Returns the `Ivar` for a specified class variable of a given class.
- [class_addIvar](<class_addivar(__________).md>) — Adds a new instance variable to a class.
- [class_copyIvarList](<class_copyivarlist(____).md>) — Describes the instance variables declared by a class.
- [class_getIvarLayout](<class_getivarlayout(__).md>) — Returns a description of the `Ivar` layout for a given class.
- [class_setIvarLayout](<class_setivarlayout(____).md>) — Sets the `Ivar` layout for a given class.
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — Returns a description of the layout of weak `Ivar`s for a given class.
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — Sets the layout for weak `Ivar`s for a given class.
- [class_getProperty](<class_getproperty(____).md>) — Returns a property with a given name of a given class.
- [class_copyPropertyList](<class_copypropertylist(____).md>) — Describes the properties declared by a class.
