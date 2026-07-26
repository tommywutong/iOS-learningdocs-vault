---
title: 'dataCorruptedError(in:debugDescription:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decodingerror/datacorruptederror(in:debugdescription:)-4ruvu'
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/datacorruptederror(in:debugdescription:)-4ruvu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/datacorruptederror%28in%3Adebugdescription%3A%29-4ruvu.json'
content_hash: 'sha256:bf11c53c379470f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DecodingError](../decodingerror.md)

# dataCorruptedError(in:debugDescription:)

<sub>Type Method</sub>

Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func dataCorruptedError(in container: any SingleValueDecodingContainer, debugDescription: String) -> DecodingError
```

## Return Value

A new `.dataCorrupted` error with the given information.

## Discussion

The coding path for the returned error is the given container’s coding path.

- param container: The container in which the corrupted data was accessed.
- param debugDescription: A description of the error to aid in debugging.
