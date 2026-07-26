---
title: 'intersection(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/intersection(_:)-73uhs'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/intersection(_:)-73uhs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/intersection%28_%3A%29-73uhs.json'
content_hash: 'sha256:cb4165404d3dec7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# intersection(_:)

<sub>Instance Method</sub>

Returns a new option set with only the elements contained in both this set and the given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersection(_ other: Self) -> Self
```

## Parameters

- `other` — An option set.

## Return Value

A new option set with only the elements contained in both this set and `other`.

## Discussion

This example uses the `intersection(_:)` method to limit the available shipping options to what can be used with a PO Box destination.

```swift
// Can only ship standard or priority to PO Boxes
let poboxShipping: ShippingOptions = [.standard, .priority]
let memberShipping: ShippingOptions =
        [.standard, .priority, .secondDay]

let availableOptions = memberShipping.intersection(poboxShipping)
print(availableOptions.contains(.priority))
// Prints "true"
print(availableOptions.contains(.secondDay))
// Prints "false"
```
