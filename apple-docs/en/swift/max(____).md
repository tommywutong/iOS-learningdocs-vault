---
title: 'max(_:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/max(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/max(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/max%28_%3A_%3A%29.json'
content_hash: 'sha256:2946b4321854e280'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# max(_:_:)

<sub>Function</sub>

Returns the greater of two comparable values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func max<T>(_ x: T, _ y: T) -> T where T : Comparable
```

## Parameters

- `x` — A value to compare.

- `y` — Another value to compare.

## Return Value

The greater of `x` and `y`. If `x` is equal to `y`, returns `y`.

## See Also

### Choosing the Smallest and Largest Value

- [min(_:_:)](<min(____).md>) — Returns the lesser of two comparable values.
- [min(_:_:_:_:)](<min(________).md>) — Returns the least argument passed.
- [max(_:_:_:_:)](<max(________).md>) — Returns the greatest argument passed.
