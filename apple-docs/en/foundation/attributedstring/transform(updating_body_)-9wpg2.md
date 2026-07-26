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
doc_path: '/documentation/foundation/attributedstring/transform(updating:body:)-9wpg2'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-9wpg2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/transform%28updating%3Abody%3A%29-9wpg2.json'
content_hash: 'sha256:dcec67f384b49275'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# transform(updating:body:)

<sub>Instance Method</sub>

Tracks the location of the selection throughout the mutation closure, updating the selection so it represents the same effective locations after the mutation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func transform<E>(updating selection: inout AttributedTextSelection, body: (inout AttributedString) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `selection` — The selection to track throughout the `body` closure.

- `body` — A mutating operation, or set of operations, to perform on the value of `self`. The value of `self` is provided to the closure as an `inout AttributedString` that the closure should mutate directly. Do not capture the value of `self` in the provided closure - the closure should mutate the provided `inout` copy.

## Discussion

> [!note] Note
> If the mutation performed does not allow for tracking to succeed (such as replacing the provided inout variable with an entirely different `AttributedString`), the selection is reset to the fallback location at the end of the text.
