---
title: 'remove(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/remove(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/remove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/remove%28_%3A%29.json'
content_hash: 'sha256:4e72facb00a69ab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# remove(_:)

<sub>Instance Method</sub>

Removes the given element and any elements subsumed by the given element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(_ member: Self.Element) -> Self.Element?
```

## Parameters

- `member` — The element of the set to remove.

## Return Value

For ordinary sets, an element equal to `member` if `member` is contained in the set; otherwise, `nil`. In some cases, a returned element may be distinguishable from `member` by identity comparison or some other means.

For sets where the set type and element type are the same, like `OptionSet` types, this method returns any intersection between the set and `[member]`, or `nil` if the intersection is empty.

## Default Implementations

### SetAlgebra Implementations

- [remove(_:)](<remove(__)-1pj2m.md>) — Removes the given element and all elements subsumed by it.

## See Also

### Adding and Removing Elements

- [insert(_:)](<insert(__).md>) — Inserts the given element in the set if it is not already present.
- [update(with:)](<update(with_).md>) — Inserts the given element into the set unconditionally.
