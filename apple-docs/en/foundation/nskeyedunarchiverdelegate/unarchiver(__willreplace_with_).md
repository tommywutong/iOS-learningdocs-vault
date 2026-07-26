---
title: 'unarchiver(_:willReplace:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:willreplace:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:willreplace:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiverdelegate/unarchiver%28_%3Awillreplace%3Awith%3A%29.json'
content_hash: 'sha256:4d31a268a9db1626'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiverDelegate](../nskeyedunarchiverdelegate.md)

# unarchiver(_:willReplace:with:)

<sub>Instance Method</sub>

Informs the delegate that one object is being substituted for another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, willReplace object: Any, with newObject: Any)
```

## Parameters

- `unarchiver` — An unarchiver for which the receiver is the delegate.

- `object` — An object in the archive.

- `newObject` — The object with which `unarchiver` will replace `object`.

## Discussion

This method is called even when the delegate itself is doing, or has done, the substitution with [- unarchiver:didDecodeObject:](<unarchiver(__diddecode_).md>).

The delegate may use this method if it is keeping track of the encoded or decoded objects.

## See Also

### Decoding Objects

- [- unarchiver:cannotDecodeObjectOfClassName:originalClasses:](<unarchiver(__cannotdecodeobjectofclassname_originalclasses_).md>) — Informs the delegate that the class with a given name is not available during decoding.
- [- unarchiver:didDecodeObject:](<unarchiver(__diddecode_).md>) — Informs the delegate that a given object has been decoded.
