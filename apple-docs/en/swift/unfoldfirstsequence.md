---
title: UnfoldFirstSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unfoldfirstsequence
source_url: 'https://developer.apple.com/documentation/swift/unfoldfirstsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unfoldfirstsequence.json'
content_hash: 'sha256:686170fcf9a12cce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnfoldFirstSequence

<sub>Type Alias</sub>

The return type of `sequence(first:next:)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias UnfoldFirstSequence<T> = UnfoldSequence<T, (T?, Bool)>
```

## See Also

### Type Aliases

- [Iterator](unfoldsequence/iterator.md) — A type that provides the sequence’s iteration interface and encapsulates its iteration state.
