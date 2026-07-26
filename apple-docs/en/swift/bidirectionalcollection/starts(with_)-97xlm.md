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
doc_path: '/documentation/swift/bidirectionalcollection/starts(with:)-97xlm'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/starts(with:)-97xlm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/starts%28with%3A%29-97xlm.json'
content_hash: 'sha256:d72e8017eb57a952'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# starts(with:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the initial elements of this collection are a match for the regex created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func starts(@RegexComponentBuilder with content: () -> some RegexComponent) -> Bool
```

## Parameters

- `content` — A closure that returns a regex to match at the beginning of this collection.

## Return Value

`true` if the initial elements of this collection match regex returned by `content`; otherwise, `false`.
