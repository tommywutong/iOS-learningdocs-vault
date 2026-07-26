---
title: 'update(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/update(with:)-2oa9l'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/update(with:)-2oa9l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/update%28with%3A%29-2oa9l.json'
content_hash: 'sha256:e826708d7ed882db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# update(with:)

<sub>Instance Method</sub>

Inserts the given element into the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func update(with newMember: Self.Element) -> Self.Element?
```

## Return Value

The intersection of `[newMember]` and the set if the intersection was nonempty; otherwise, `nil`.

## Discussion

If `newMember` is not contained in the set but subsumes current members of the set, the subsumed members are returned.

```swift
var options: ShippingOptions = [.secondDay, .priority]
let replaced = options.update(with: .express)
print(replaced == .secondDay)
// Prints "true"
```
