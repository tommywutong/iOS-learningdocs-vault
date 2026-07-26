---
title: 'firstIndex(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/scalar/utf8view/firstindex(of:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/utf8view/firstindex(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/utf8view/firstindex%28of%3A%29.json'
content_hash: 'sha256:3c2b2a1b849cafd2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [UTF8View](../utf8view.md)

# firstIndex(of:)

<sub>Instance Method</sub>

Returns the first index where the specified value appears in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstIndex(of element: Self.Element) -> Self.Index?
```

## Parameters

- `element` — An element to search for in the collection.

## Return Value

The first index where `element` is found. If `element` is not found in the collection, returns `nil`.

## Discussion

After using `firstIndex(of:)` to find the position of a particular element in a collection, you can use it to access the element by subscripting. This example shows how you can modify one of the names in an array of students.

```swift
var students = ["Ben", "Ivy", "Jordell", "Maxime"]
if let i = students.firstIndex(of: "Maxime") {
    students[i] = "Max"
}
print(students)
// Prints "["Ben", "Ivy", "Jordell", "Max"]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
