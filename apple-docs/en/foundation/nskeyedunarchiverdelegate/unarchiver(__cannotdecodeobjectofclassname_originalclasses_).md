---
title: 'unarchiver(_:cannotDecodeObjectOfClassName:originalClasses:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:cannotdecodeobjectofclassname:originalclasses:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:cannotdecodeobjectofclassname:originalclasses:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiverdelegate/unarchiver%28_%3Acannotdecodeobjectofclassname%3Aoriginalclasses%3A%29.json'
content_hash: 'sha256:3c657419e3da1a45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiverDelegate](../nskeyedunarchiverdelegate.md)

# unarchiver(_:cannotDecodeObjectOfClassName:originalClasses:)

<sub>Instance Method</sub>

Informs the delegate that the class with a given name is not available during decoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, cannotDecodeObjectOfClassName name: String, originalClasses classNames: [String]) -> AnyClass?
```

## Parameters

- `unarchiver` — An unarchiver for which the receiver is the delegate.

- `name` — The name of the class of an object `unarchiver` is trying to decode.

- `classNames` — An array describing the class hierarchy of the encoded object, where the first element is the class name string of the encoded object, the second element is the class name of its immediate superclass, and so on.

## Return Value

The class unarchiver should use in place of the class named `name`.

## Discussion

The delegate may, for example, load some code to introduce the class to the runtime and return the class, or substitute a different class object. If the delegate returns `nil`, unarchiving aborts and the method raises an `NSInvalidUnarchiveOperationException`.

## See Also

### Related Documentation

- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)

### Decoding Objects

- [- unarchiver:didDecodeObject:](<unarchiver(__diddecode_).md>) — Informs the delegate that a given object has been decoded.
- [- unarchiver:willReplaceObject:withObject:](<unarchiver(__willreplace_with_).md>) — Informs the delegate that one object is being substituted for another.
