---
title: 'replaceSubrange(_:addingCount:initializingWith:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/replacesubrange(_:addingcount:initializingwith:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/replacesubrange(_:addingcount:initializingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/replacesubrange%28_%3Aaddingcount%3Ainitializingwith%3A%29.json'
content_hash: 'sha256:32e653f463208b30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# replaceSubrange(_:addingCount:initializingWith:)

<sub>Instance Method</sub>

Replaces the specified range of elements by a given count of new items, using a callback to directly initialize array storage by populating an output span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSubrange<E>(_ subrange: Range<Int>, addingCount newItemCount: Int, initializingWith initializer: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `subrange` — The subrange of the array to replace. The bounds of the range must be valid indices in the array.

- `newItemCount` — The maximum number of items to replace the old subrange.

- `initializer` — A callback that gets called at most once to directly populate newly reserved storage within the array. The function is always called with an empty output span.

## Discussion

The number of new items need not match the number of elements being removed.

This method has the same overall effect as calling

```swift
try array.removeSubrange(subrange)
try array.insert(
  addingCount: newItemCount,
  at: subrange.lowerBound,
  initializingWith: initializer)
```

Except it performs faster (by a constant factor), by avoiding moving some items in the array twice.

If the array does not have sufficient capacity to perform the replacement, then this reallocates storage to extend its capacity, using a geometric growth rate.

If the callback fails to fully populate its output span or if it throws an error, then the array keeps all items that were successfully initialized before the callback terminated the prepend.

Partial insertions create a gap in array storage that needs to be closed by moving newly inserted items to their correct positions given the adjusted count. This adds some overhead compared to adding exactly as many items as promised.

> [!abstract] Complexity
> O(`self.count` + `newItemCount`) in addition to the complexity of the callback invocations.
