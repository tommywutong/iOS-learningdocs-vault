---
title: 'compactMap(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/compactmap(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/compactmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/compactmap%28_%3A%29.json'
content_hash: 'sha256:f09ed17baaf3ae73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# compactMap(_:)

<sub>Instance Method</sub>

Calls a closure with each received element and publishes any returned optional that has a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compactMap<T>(_ transform: @escaping (Self.Output) -> T?) -> Publishers.CompactMap<Self, T>
```

## Parameters

- `transform` — A closure that receives a value and returns an optional value.

## Return Value

Any non-`nil` optional results of the calling the supplied closure.

## Discussion

Combine’s [compactMap(_:)](<compactmap(__).md>) operator performs a function similar to that of [compactMap(_:)](<../../swift/sequence/compactmap(__).md>) in the Swift standard library: the [compactMap(_:)](<compactmap(__).md>) operator in Combine removes `nil` elements in a publisher’s stream and republishes non-`nil` elements to the downstream subscriber.

The example below uses a range of numbers as the source for a collection based publisher. The [compactMap(_:)](<compactmap(__).md>) operator consumes each element from the `numbers` publisher attempting to access the dictionary using the element as the key. If the example’s dictionary returns a `nil`, due to a non-existent key, [compactMap(_:)](<compactmap(__).md>) filters out the `nil` (missing) elements.

```swift
let numbers = (0...5)
let romanNumeralDict: [Int : String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]

cancellable = numbers.publisher
    .compactMap { romanNumeralDict[$0] }
    .sink { print("\($0)", terminator: " ") }

// Prints: "I II III V"
```

## See Also

### Filtering elements

- [filter(_:)](<filter(__).md>) — Republishes all elements that match a provided closure.
- [tryFilter(_:)](<tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [tryCompactMap(_:)](<trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [removeDuplicates(by:)](<removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [tryRemoveDuplicates(by:)](<tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceEmpty(with:)](<replaceempty(with_).md>) — Replaces an empty stream with the provided element.
- [replaceError(with:)](<replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.
