---
title: 'filter(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/filter(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/filter%28_%3A%29.json'
content_hash: 'sha256:47a9f6deaa20a5eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# filter(_:)

<sub>Instance Method</sub>

Republishes all elements that match a provided closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(_ isIncluded: @escaping (Self.Output) -> Bool) -> Publishers.Filter<Self>
```

## Parameters

- `isIncluded` — A closure that takes one element and returns a Boolean value indicating whether to republish the element.

## Return Value

A publisher that republishes all elements that satisfy the closure.

## Discussion

Combine’s [filter(_:)](<filter(__).md>) operator performs an operation similar to that of doc://com.apple.documentation/documentation/Swift/Sequence/filter(_:)-5y9d2 in the Swift Standard Library: it uses a closure to test each element to determine whether to republish the element to the downstream subscriber.

The following example, uses a filter operation that receives an `Int` and only republishes a value if it’s even.

```swift
let numbers: [Int] = [1, 2, 3, 4, 5]
cancellable = numbers.publisher
    .filter { $0 % 2 == 0 }
    .sink { print("\($0)", terminator: " ") }

// Prints: "2 4"
```

## See Also

### Filtering elements

- [tryFilter(_:)](<tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [compactMap(_:)](<compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [tryCompactMap(_:)](<trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [removeDuplicates(by:)](<removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceEmpty(with:)](<replaceempty(with_).md>) — Replaces an empty stream with the provided element.
- [replaceError(with:)](<replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.
