---
title: 'union(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/union(_:)-7mfo6'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/union(_:)-7mfo6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/union%28_%3A%29-7mfo6.json'
content_hash: 'sha256:347afb7c80f1b121'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# union(_:)

<sub>Instance Method</sub>

Returns a new option set of the elements contained in this set, in the given set, or in both.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func union(_ other: Self) -> Self
```

## Parameters

- `other` — An option set.

## Return Value

A new option set made up of the elements contained in this set, in `other`, or in both.

## Discussion

This example uses the `union(_:)` method to add two more shipping options to the default set.

```swift
let defaultShipping = ShippingOptions.standard
let memberShipping = defaultShipping.union([.secondDay, .priority])
print(memberShipping.contains(.priority))
// Prints "true"
```
