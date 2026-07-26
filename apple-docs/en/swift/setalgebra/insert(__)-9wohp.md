---
title: 'insert(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/insert(_:)-9wohp'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/insert(_:)-9wohp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/insert%28_%3A%29-9wohp.json'
content_hash: 'sha256:3ab17e2349d1b7cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# insert(_:)

<sub>Instance Method</sub>

Adds the given element to the option set if it is not already a member.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func insert(_ newMember: Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)
```

## Parameters

- `newMember` — The element to insert.

## Return Value

`(true, newMember)` if `newMember` was not contained in `self`. Otherwise, returns `(false, oldMember)`, where `oldMember` is the member of the set equal to `newMember`.

## Discussion

In the following example, the `.secondDay` shipping option is added to the `freeOptions` option set if `purchasePrice` is greater than 50.0. For the `ShippingOptions` declaration, see the `OptionSet` protocol discussion.

```swift
let purchasePrice = 87.55

var freeOptions: ShippingOptions = [.standard, .priority]
if purchasePrice > 50 {
    freeOptions.insert(.secondDay)
}
print(freeOptions.contains(.secondDay))
// Prints "true"
```
