---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anyregexoutput/subscript(_:)-6qdcr'
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput/subscript(_:)-6qdcr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput/subscript%28_%3A%29-6qdcr.json'
content_hash: 'sha256:e4aec7c7c7ab1a21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRegexOutput](../anyregexoutput.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the capture with the specified name, if a capture with that name exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(name: String) -> AnyRegexOutput.Element? { get }
```

## Parameters

- `name` — The name of the capture to access.

## Return Value

An element providing information about the capture, if there is a capture named `name`; otherwise, `nil`.
