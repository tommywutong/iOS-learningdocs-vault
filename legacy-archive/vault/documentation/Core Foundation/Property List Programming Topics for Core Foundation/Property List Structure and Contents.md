---
title: Property List Programming Topics for Core Foundation
apple_id: 10000130i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/StructureAndContents.html
archived_at: '2026-07-15T07:22:47.027394Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Property List Programming Topics for Core Foundation](Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Creating%20Property%20Lists.md)[Previous](Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md)

# Property List Structure and Contents

Property lists are constructed from the basic Core Foundation types CFString, CFNumber, CFBoolean, CFDate, and CFData. To build a complex data structure out of these basic types, you put them inside a CFDictionary or CFArray. To simplify programming with property lists, any of the property list types can also be referred to using a reference of type `CFPropertyListRef`.

CFPropertyList provides an abstraction for all the property list types—you can think of CFPropertyList in object-oriented terms as being the superclass of CFString, CFNumber, CFDictionary, and so on. When a Core Foundation function returns a `CFPropertyListRef`, it means that the value may be any of the property list types. For example, [CFPreferencesCopyAppValue](https://developer.apple.com/documentation/corefoundation/1515497-cfpreferencescopyappvalue) returns a `CFPropertyListRef`. This means that the value returned can be a CFString object, a CFNumber object, a CFDictionary object, and so on again. You can use [CFGetTypeID](https://developer.apple.com/documentation/corefoundation/1521218-cfgettypeid) to determine what type of object a property list value is.

In a CFDictionary object, data is structured as key-value pairs, where each key is a string and the key’s value can be a CFString, a CFNumber, a CFBoolean, a CFDate, a CFData, a CFArray, or another CFDictionary object. If you use a CFDictionary object as a property list, all its keys _must_ be CFString objects.

In a CFArray object, data is structured as an ordered collection of objects that can be accessed by index. In a property list, a CFArray object can contain any of the basic property list types, as well as CFDictionary objects and other CFArray objects.

Although CFDictionary and CFArray objects can contain data types other than the property list types, if they do, you can’t use the Core Foundation property list programming interface to work with them.

[Next](Creating%20Property%20Lists.md)[Previous](Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md)

