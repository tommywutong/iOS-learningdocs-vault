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
doc_path: '/documentation/swift/decodingerror/datacorruptederror(in:debugdescription:)-5on9z'
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/datacorruptederror(in:debugdescription:)-5on9z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/datacorruptederror%28in%3Adebugdescription%3A%29-5on9z.json'
content_hash: 'sha256:f84409058360b257'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DecodingError](../decodingerror.md)

# dataCorruptedError(in:debugDescription:)

<sub>Type Method</sub>

Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func dataCorruptedError(in container: any UnkeyedDecodingContainer, debugDescription: String) -> DecodingError
```

## Return Value

A new `.dataCorrupted` error with the given information.

## Discussion

The coding path for the returned error is constructed by appending the given container’s current index to its coding path.

- param container: The container in which the corrupted data was accessed.
- param debugDescription: A description of the error to aid in debugging.
