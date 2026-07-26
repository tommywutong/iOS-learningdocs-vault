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
doc_path: '/documentation/foundation/attributedstring/transform(updating:body:)-79te9'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-79te9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/transform%28updating%3Abody%3A%29-79te9.json'
content_hash: 'sha256:ac1527d3e1f86b3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# transform(updating:body:)

<sub>Instance Method</sub>

Tracks the location of the provided range throughout the mutation closure, returning a new, updated range that represents the same effective locations after the mutation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func transform<E>(updating range: Range<AttributedString.Index>, body: (inout AttributedString) throws(E) -> Void) throws(E) -> Range<AttributedString.Index>? where E : Error
```

## Parameters

- `range` — A range to track throughout the `body` block.

- `body` — A mutating operation, or set of operations, to perform on this `AttributedString`.

## Return Value

The updated `Range` that is valid after the mutation has been performed, or `nil` if the mutation performed does not allow for tracking to succeed (such as replacing the provided inout variable with an entirely different `AttributedString`).
