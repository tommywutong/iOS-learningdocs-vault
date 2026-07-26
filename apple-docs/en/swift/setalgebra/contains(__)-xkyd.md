---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/contains(_:)-xkyd'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/contains(_:)-xkyd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/contains%28_%3A%29-xkyd.json'
content_hash: 'sha256:1e40ba46bc500387'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given element is a member of the option set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ member: Self) -> Bool
```

## Parameters

- `member` — The element to look for in the option set.

## Return Value

`true` if the option set contains `member`; otherwise, `false`.

## Discussion

This example uses the `contains(_:)` method to check whether next-day shipping is in the `availableOptions` instance.

```swift
let availableOptions = ShippingOptions.express
if availableOptions.contains(.nextDay) {
    print("Next day shipping available")
}
// Prints "Next day shipping available"
```
