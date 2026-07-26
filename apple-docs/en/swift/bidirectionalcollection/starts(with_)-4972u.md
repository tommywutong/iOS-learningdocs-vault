---
title: 'starts(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/starts(with:)-4972u'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/starts(with:)-4972u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/starts%28with%3A%29-4972u.json'
content_hash: 'sha256:3f452558087a339f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# starts(with:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in the specified regex.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func starts(with regex: some RegexComponent) -> Bool
```

## Parameters

- `regex` — A regex to compare to this sequence.

## Return Value

`true` if the initial elements of the sequence matches the beginning of `regex`; otherwise, `false`.
