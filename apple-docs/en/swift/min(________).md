---
title: 'min(_:_:_:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/min(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/min(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/min%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0acf0f638f64d28c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# min(_:_:_:_:)

<sub>Function</sub>

Returns the least argument passed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func min<T>(_ x: T, _ y: T, _ z: T, _ rest: T...) -> T where T : Comparable
```

## Parameters

- `x` — A value to compare.

- `y` — Another value to compare.

- `z` — A third value to compare.

- `rest` — Zero or more additional values.

## Return Value

The least of all the arguments. If there are multiple equal least arguments, the result is the first one.

## See Also

### Choosing the Smallest and Largest Value

- [min(_:_:)](<min(____).md>) — Returns the lesser of two comparable values.
- [max(_:_:)](<max(____).md>) — Returns the greater of two comparable values.
- [max(_:_:_:_:)](<max(________).md>) — Returns the greatest argument passed.
