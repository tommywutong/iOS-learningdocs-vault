---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/subscript(_:)-4e8d9'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/subscript(_:)-4e8d9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/subscript%28_%3A%29-4e8d9.json'
content_hash: 'sha256:6297c95674e96615'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Int) -> Element { get set }
```

## Parameters

- `index` — The position of the element to access. `index` must be greater than or equal to `startIndex` and less than `endIndex`.

## Overview

The following example uses indexed subscripting to update an array’s second element. After assigning the new value (`"Butler"`) at a specific position, that value is immediately available at that same position.

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
streets[1] = "Butler"
print(streets[1])
// Prints "Butler"
```

> [!abstract] Complexity
> Reading an element from an array is O(1). Writing is O(1) unless the array’s storage is shared with another array or uses a bridged `NSArray` instance as its storage, in which case writing is O(_n_), where _n_ is the length of the array.
