---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/isequal%28to%3A%29.json'
content_hash: 'sha256:98bccc96b308cc95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# isEqual(to:)

<sub>Instance Method</sub>

Compares the receiving array to another array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to otherArray: [Any]) -> Bool
```

## Parameters

- `otherArray` — An array.

## Return Value

[true](../../swift/true.md) if the contents of `otherArray` are equal to the contents of the receiving array, otherwise [false](../../swift/false.md).

## Discussion

Two arrays have equal contents if they each hold the same number of objects and objects at a given index in each array satisfy the [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) test.

## See Also

### Comparing Arrays

- [- firstObjectCommonWithArray:](<firstobjectcommon(with_).md>) — Returns the first object contained in the receiving array that’s equal to an object in another given array.
