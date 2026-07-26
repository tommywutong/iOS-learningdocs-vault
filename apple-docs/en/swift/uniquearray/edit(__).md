---
title: 'edit(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/edit(_:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/edit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/edit%28_%3A%29.json'
content_hash: 'sha256:5ae8293282a4b378'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# edit(_:)

<sub>Instance Method</sub>

Arbitrarily edit the storage underlying this array by invoking a user-supplied closure with a mutable `OutputSpan` view over it. This method calls its function argument at most once, allowing it to arbitrarily modify the contents of the output span it is given. The argument is free to add, remove or reorder any items; however, it is not allowed to replace the span or change its capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func edit<E, R>(_ body: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Parameters

- `body` — A function that edits the contents of this array through an `OutputSpan` argument. This method invokes this function at most once.

## Return Value

This method returns the result of its function argument.

## Discussion

When the function argument finishes (whether by returning or throwing an error) the rigid array instance is updated to match the final contents of the output span.

> [!abstract] Complexity
> Adds O(1) overhead to the complexity of the function argument.
