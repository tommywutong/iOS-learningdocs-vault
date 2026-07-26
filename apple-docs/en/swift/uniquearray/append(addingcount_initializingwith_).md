---
title: 'append(addingCount:initializingWith:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/append(addingcount:initializingwith:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/append(addingcount:initializingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/append%28addingcount%3Ainitializingwith%3A%29.json'
content_hash: 'sha256:86f9cb78e804c887'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# append(addingCount:initializingWith:)

<sub>Instance Method</sub>

Append a given number of items to the end of this array by populating an output span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<E>(addingCount newItemCount: Int, initializingWith initializer: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `newItemCount` — The number of items to append to the array.

- `initializer` — A callback that gets called at most once to directly populate newly reserved storage within the array. The function is allowed to initialize fewer than `uninitializedCount` items. The array is appended however many items the callback adds to the output span before it returns (or before it throws an error).

## Discussion

If the array does not have sufficient capacity to hold the requested number of new elements, then this reallocates the array’s storage to grow its capacity, using a geometric growth rate.

If the callback fails to fully populate its output span or if it throws an error, then the array keeps all items that were successfully initialized before the callback terminated the insertion.

> [!abstract] Complexity
> O(`uninitializedCount`)
