---
title: 'repeatElement(_:count:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/repeatelement(_:count:)'
source_url: 'https://developer.apple.com/documentation/swift/repeatelement(_:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/repeatelement%28_%3Acount%3A%29.json'
content_hash: 'sha256:83d798f767a1825c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# repeatElement(_:count:)

<sub>Function</sub>

Creates a collection containing the specified number of the given element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func repeatElement<T>(_ element: T, count n: Int) -> Repeated<T>
```

## Parameters

- `element` — The element to repeat.

## Return Value

A collection that contains `count` elements that are all `element`.

## Discussion

The following example creates a `Repeated<Int>` collection containing five zeroes:

```swift
let zeroes = repeatElement(0, count: 5)
for x in zeroes {
    print(x)
}
// 0
// 0
// 0
// 0
// 0
```

## See Also

### Special-Use Collections

- [CollectionOfOne](collectionofone.md) — A collection containing a single element.
- [EmptyCollection](emptycollection.md) — A collection whose element type is `Element` but that is always empty.
- [KeyValuePairs](keyvaluepairs.md) — A lightweight collection of key-value pairs.
- [DictionaryLiteral](dictionaryliteral.md)
