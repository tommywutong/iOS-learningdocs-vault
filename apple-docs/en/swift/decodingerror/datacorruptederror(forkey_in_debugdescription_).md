---
title: 'dataCorruptedError(forKey:in:debugDescription:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decodingerror/datacorruptederror(forkey:in:debugdescription:)'
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/datacorruptederror(forkey:in:debugdescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/datacorruptederror%28forkey%3Ain%3Adebugdescription%3A%29.json'
content_hash: 'sha256:93aa904a1e61e16c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DecodingError](../decodingerror.md)

# dataCorruptedError(forKey:in:debugDescription:)

<sub>Type Method</sub>

Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func dataCorruptedError<C>(forKey key: C.Key, in container: C, debugDescription: String) -> DecodingError where C : KeyedDecodingContainerProtocol
```

## Return Value

A new `.dataCorrupted` error with the given information.

## Discussion

The coding path for the returned error is constructed by appending the given key to the given container’s coding path.

- param key: The key which caused the failure.
- param container: The container in which the corrupted data was accessed.
- param debugDescription: A description of the error to aid in debugging.
