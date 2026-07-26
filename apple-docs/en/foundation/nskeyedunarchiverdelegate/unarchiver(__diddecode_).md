---
title: 'unarchiver(_:didDecode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:diddecode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:diddecode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiverdelegate/unarchiver%28_%3Adiddecode%3A%29.json'
content_hash: 'sha256:3d206076ae11e34f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiverDelegate](../nskeyedunarchiverdelegate.md)

# unarchiver(_:didDecode:)

<sub>Instance Method</sub>

Informs the delegate that a given object has been decoded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, didDecode object: consuming Any?) -> Any?
```

## Parameters

- `unarchiver` — An unarchiver for which the receiver is the delegate.

- `object` — The object that has been decoded. `object` may be `nil`.

## Return Value

The object to use in place of `object`. The delegate can either return `object` or return a different object to replace the decoded one. In apps using ARC, the delegate should only return `nil` if `object` itself is `nil`. In apps not using ARC, the delegate can return `nil` to indicate that the decoded value is unchanged—that is, `object` will be decoded.

## Discussion

This method is called after `object` has been sent [- initWithCoder:](<../nscoding/init(coder_).md>) and [awakeAfter(using:)](<../../objectivec/nsobject-swift.class/awakeafter(using_).md>).

The delegate may use this method to keep track of the decoded objects.

## See Also

### Decoding Objects

- [- unarchiver:cannotDecodeObjectOfClassName:originalClasses:](<unarchiver(__cannotdecodeobjectofclassname_originalclasses_).md>) — Informs the delegate that the class with a given name is not available during decoding.
- [- unarchiver:willReplaceObject:withObject:](<unarchiver(__willreplace_with_).md>) — Informs the delegate that one object is being substituted for another.
