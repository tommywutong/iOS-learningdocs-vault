---
title: 'saveJSONLines(to:includeReportMetadata:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/collection/savejsonlines(to:includereportmetadata:)'
source_url: 'https://developer.apple.com/documentation/swift/collection/savejsonlines(to:includereportmetadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/savejsonlines%28to%3Aincludereportmetadata%3A%29.json'
content_hash: 'sha256:0015f6ff58295817'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# saveJSONLines(to:includeReportMetadata:)

<sub>Instance Method</sub>

Saves the array of evaluation results as a JSONL file

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@discardableResult func saveJSONLines(to url: URL, includeReportMetadata: Bool = false) throws -> URL
```

## Parameters

- `url` — The file URL to write the JSONL output to.

- `includeReportMetadata` — Whether to include report metadata in each entry. Defaults to `false`.

## Return Value

The URL of the saved file.
