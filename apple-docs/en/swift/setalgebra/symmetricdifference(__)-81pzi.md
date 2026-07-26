---
title: 'symmetricDifference(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/symmetricdifference(_:)-81pzi'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/symmetricdifference(_:)-81pzi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/symmetricdifference%28_%3A%29-81pzi.json'
content_hash: 'sha256:80993bd7fef8df7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# symmetricDifference(_:)

<sub>Instance Method</sub>

Returns a new option set with the elements contained in this set or in the given set, but not in both.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func symmetricDifference(_ other: Self) -> Self
```

## Parameters

- `other` — An option set.

## Return Value

A new option set with only the elements contained in either this set or `other`, but not in both.
