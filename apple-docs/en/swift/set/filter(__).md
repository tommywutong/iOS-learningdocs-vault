---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/filter(_:)'
source_url: 'https://developer.apple.com/documentation/swift/set/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/filter%28_%3A%29.json'
content_hash: 'sha256:c7d13c80ea6b6f52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# filter(_:)

<sub>Instance Method</sub>

Returns a new set containing the elements of the set that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func filter<E>(_ isIncluded: (Element) throws(E) -> Bool) throws(E) -> Set<Element> where E : Error
```

## Parameters

- `isIncluded` — A closure that takes an element as its argument and returns a Boolean value indicating whether the element should be included in the returned set.

## Return Value

A set of the elements that `isIncluded` allows.

## Discussion

In this example, `filter(_:)` is used to include only names shorter than five characters.

```swift
let cast: Set = ["Vivien", "Marlon", "Kim", "Karl"]
let shortNames = cast.filter { $0.count < 5 }

shortNames.isSubset(of: cast)
// true
shortNames.contains("Vivien")
// false
```

## See Also

### Removing Elements

- [remove(_:)](<remove(__)-8p2tv.md>) — Removes the specified element from the set.
- [remove(_:)](<remove(__)-4d3i1.md>)
- [removeFirst()](<removefirst().md>) — Removes the first element of the set.
- [remove(at:)](<remove(at_).md>) — Removes the element at the given index of the set.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all members from the set.
