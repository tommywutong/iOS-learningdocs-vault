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
doc_path: '/documentation/swift/setalgebra/remove(_:)-1pj2m'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/remove(_:)-1pj2m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/remove%28_%3A%29-1pj2m.json'
content_hash: 'sha256:871b1e476a188583'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# remove(_:)

<sub>Instance Method</sub>

Removes the given element and all elements subsumed by it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(_ member: Self.Element) -> Self.Element?
```

## Parameters

- `member` — The element of the set to remove.

## Return Value

The intersection of `[member]` and the set, if the intersection was nonempty; otherwise, `nil`.

## Discussion

In the following example, the `.priority` shipping option is removed from the `options` option set. Attempting to remove the same shipping option a second time results in `nil`, because `options` no longer contains `.priority` as a member.

```swift
var options: ShippingOptions = [.secondDay, .priority]
let priorityOption = options.remove(.priority)
print(priorityOption == .priority)
// Prints "true"

print(options.remove(.priority))
// Prints "nil"
```

In the next example, the `.express` element is passed to `remove(_:)`. Although `.express` is not a member of `options`, `.express` subsumes the remaining `.secondDay` element of the option set. Therefore, `options` is emptied and the intersection between `.express` and `options` is returned.

```swift
let expressOption = options.remove(.express)
print(expressOption == .express)
// Prints "false"
print(expressOption == .secondDay)
// Prints "true"
```
