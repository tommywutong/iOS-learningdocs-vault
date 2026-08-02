---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSCodingSppt.html
archived_at: '2026-07-15T08:13:55.837271Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSCoding.Support

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSCoding.Support is an abstract class that defines a mechanism for one class to provide [NSCoding](NSCoding.md#apple-ineucskcizbeq) behavior on behalf of another class. Subclasses of NSCoding.Support encode and decode objects of a different class. Subclasses of NSCoding.Support are needed to provide coding for classes whose code you don't own and that don't implement NSCoding.

For example, consider Java Client WebObjects applications that use NSCoding to distribute objects between client and server. Not all objects that Java Client distributes implement NSCoding (java.lang.String, for example). To encode and decode non-NSCoding objects, Java Client uses specialized subclasses of NSCoding.Support.

|  |
| --- |
| __Note:__ Java Client has private subclasses of NSCoding.Support to encode and decode objects basic Java value classes such as java.lang.String, java.lang.Number, java.math.BigDecimal, and java.util.Date. |

A subclass of NSCoding.Support should implement the methods [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwi2lom4xfg5lqobxxe5bpmvxgg33emvlws5diinxwizls) and [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstinxwi2lom4xfg5lqobxxe5bpmrswg33emvhwe2tfmn2a) to encode and decode objects of a specific non-NSCoding class. NSCoding.Support's implementations of these methods do nothing.

NSCoding.Support manages a registry of Support classes for classes that don't implement NSCoding. Use the methods [setSupportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgq3pmruw4zzokn2xa4dpoj2c643forjxk4dqn5zhirtpojbwyyltom) and [supportForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgq3pmruw4zzokn2xa4dpoj2c643vobyg64tuizxxeq3mmfzxg) to register and access the NSCoding.Support classes for performing coding on non-NSCoding objects.

## Constructors

---

### NSCoding.Support

`public NSCoding.Support()`

The no-arg constructor. Don't use this method; because NSCoding.Support is an abstract class, you can never create an instance of it.

---

## Static Methods

---

### setSupportForClass

`public static void setSupportForClass( NSCoding.Support supportClass, Class aClass)`

Sets _supportClass_ as the support class to use for coding instances of _aClass_.

---

### supportForClass

`public static NSCoding.Support supportForClass(Class aClass)`

Returns the support class used for coding instances of _aClass_.

---

## Instance Methods

---

### classForCoder

`public Class classForCoder(Object anObject)`

Returns the class a coder should record as the class for _anObject_ when _anObject_ is encoded. NSCoding.Support's implementation simply returns _anObject_'s actual class.

__See Also:__ [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) ( [NSCoding](NSCoding.md#apple-ineucskcizbeq))

---

### decodeObject

`public abstract Object decodeObject(NSCoder aCoder)`

Implemented by subclasses to decode an object of a specific type from the data in _aCoder_.

__See Also:__ The [NSCoding](NSCoding.md#apple-ineucskcizbeq) class description

---

### encodeWithCoder

`public abstract void encodeWithCoder( Object anObject, NSCoder aCoder)`

Implemented by subclasses to encode an object of a specific type into _aCoder_.

__See Also:__ [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) ( [NSCoding](NSCoding.md#apple-ineucskcizbeq))

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
