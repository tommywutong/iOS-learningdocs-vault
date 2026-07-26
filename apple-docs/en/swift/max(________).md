---
title: 'max(_:_:_:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/max(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/max(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/max%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:df319a034f96afa6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# max(_:_:_:_:)

<sub>Function</sub>

Returns the greatest argument passed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func max<T>(_ x: T, _ y: T, _ z: T, _ rest: T...) -> T where T : Comparable
```

## Parameters

- `x` — A value to compare.

- `y` — Another value to compare.

- `z` — A third value to compare.

- `rest` — Zero or more additional values.

## Return Value

The greatest of all the arguments. If there are multiple equal greatest arguments, the result is the last one.

## See Also

### Choosing the Smallest and Largest Value

- [min(_:_:)](<min(____).md>) — Returns the lesser of two comparable values.
- [min(_:_:_:_:)](<min(________).md>) — Returns the least argument passed.
- [max(_:_:)](<max(____).md>) — Returns the greater of two comparable values.
