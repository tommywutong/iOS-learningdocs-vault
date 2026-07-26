---
title: 'init(minimumCapacity:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/init(minimumcapacity:)'
source_url: 'https://developer.apple.com/documentation/swift/set/init(minimumcapacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/init%28minimumcapacity%3A%29.json'
content_hash: 'sha256:3c414390d757ac08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# init(minimumCapacity:)

<sub>Initializer</sub>

Creates an empty set with preallocated space for at least the specified number of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(minimumCapacity: Int)
```

## Parameters

- `minimumCapacity` — The minimum number of elements that the newly created set should be able to store without reallocating its storage buffer.

## Discussion

Use this initializer to avoid intermediate reallocations of a set’s storage buffer when you know how many elements you’ll insert into the set after creation.

## See Also

### Creating a Set

- [init()](<init().md>) — Creates an empty set.
- [init(_:)](<init(__)-9cgks.md>) — Creates a new set from a finite sequence of items.
- [init(_:)](<init(__).md>) — Creates a new set from a finite sequence of items.
