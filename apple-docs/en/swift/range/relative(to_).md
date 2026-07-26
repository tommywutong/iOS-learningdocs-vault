---
title: 'relative(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/relative(to:)'
source_url: 'https://developer.apple.com/documentation/swift/range/relative(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/relative%28to%3A%29.json'
content_hash: 'sha256:2f8af417b0992ef1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# relative(to:)

<sub>Instance Method</sub>

Returns the range of indices described by this range expression within the given collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func relative<C>(to collection: C) -> Range<Bound> where Bound == C.Index, C : Collection
```

## Parameters

- `collection` — The collection to evaluate this range expression in relation to.

## Return Value

A range suitable for slicing `collection`. The returned range is _not_ guaranteed to be inside the bounds of `collection`. Callers should apply the same preconditions to the return value as they would to a range provided directly by the user.

## See Also

### Converting Ranges

- [init(_:in:)](<init(__in_)-5cclx.md>)
- [init(_:in:)](<init(__in_)-5qfor.md>)
