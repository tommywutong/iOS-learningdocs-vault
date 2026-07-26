---
title: CFTypeRef
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftyperef
source_url: 'https://developer.apple.com/documentation/corefoundation/cftyperef'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftyperef.json'
content_hash: 'sha256:982d2d405c089f96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTypeRef

<sub>Type Alias</sub>

An untyped “generic” reference to any Core Foundation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFTypeRef = AnyObject
```

## Discussion

All other Core Foundation opaque types derive from `CFTypeRef`. The functions, callbacks, data types, and constants defined for CFType can be used by any derived opaque type. Hence, `CFTypeRef` functions are referred to as “polymorphic functions.” You use `CFTypeRef` functions to retain and release objects, to compare and inspect objects, get descriptions of objects and opaque types, and to get object allocators.

## Topics

### Memory Management

- [CFGetAllocator](<cfgetallocator(__).md>) — Returns the allocator used to allocate a Core Foundation object.
- [CFGetRetainCount](<cfgetretaincount(__).md>) — Returns the reference count of a Core Foundation object.

### Determining Equality

- [CFEqual](<cfequal(____).md>) — Determines whether two Core Foundation objects are considered equal.

### Hashing

- [CFHash](<cfhash(__).md>) — Returns a code that can be used to identify an object in a hashing structure.

### Miscellaneous Functions

- [CFCopyDescription](<cfcopydescription(__).md>) — Returns a textual description of a Core Foundation object.
- [CFCopyTypeIDDescription](<cfcopytypeiddescription(__).md>) — Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.
- [CFGetTypeID](<cfgettypeid(__).md>) — Returns the unique identifier of an opaque type to which a Core Foundation object belongs.
- [CFShow](<cfshow(__).md>) — Prints a description of a Core Foundation object to stderr.

### Data Types

- [CFHashCode](cfhashcode.md) — A type for hash codes returned by the `CFHash` function.
- [CFTypeID](cftypeid.md) — A type for unique, constant integer values that identify particular Core Foundation opaque types.

## See Also

### Related Documentation

- [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)
- [Core Foundation Design Concepts](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/CFDesignConcepts.html#//apple_ref/doc/uid/10000122i)

### Data Types

- [CFAllocatorTypeID](cfallocatortypeid.md)
- [CFCalendarIdentifier](cfcalendaridentifier.md)
- [CFDateFormatterKey](cfdateformatterkey.md)
- [CFErrorDomain](cferrordomain.md)
- [CFLocaleIdentifier](cflocaleidentifier.md)
- [CFLocaleKey](cflocalekey.md)
- [CFNotificationName](cfnotificationname.md)
- [CFNumberFormatterKey](cfnumberformatterkey.md)
- [CFRunLoopMode](cfrunloopmode.md)
- [CFStreamPropertyKey](cfstreampropertykey.md)
