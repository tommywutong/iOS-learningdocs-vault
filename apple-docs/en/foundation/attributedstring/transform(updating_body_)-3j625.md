---
title: 'transform(updating:body:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/transform(updating:body:)-3j625'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-3j625'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/transform%28updating%3Abody%3A%29-3j625.json'
content_hash: 'sha256:2b6e4a98452ad96e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# transform(updating:body:)

<sub>Instance Method</sub>

Tracks the location of the provided ranges throughout the mutation closure, updating them to new ranges that represent the same effective locations after the mutation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func transform<E>(updating ranges: inout [Range<AttributedString.Index>], body: (inout AttributedString) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `ranges` — A list of ranges to track throughout the `body` closure. The updated array (after the function is called) is guaranteed to be the same size as the provided array. Updated ranges are located at the same indices as their respective original ranges in the input `ranges` array.

- `body` — A mutating operation, or set of operations, to perform on the value of `self`. The value of `self` is provided to the closure as an `inout AttributedString` that the closure should mutate directly. Do not capture the value of `self` in the provided closure - the closure should mutate the provided `inout` copy.

## Discussion

If updating the provided ranges is not possible (tracking failed) then this function will fatal error. Use the `Optional`-returning variants to provide custom fallback behavior.
