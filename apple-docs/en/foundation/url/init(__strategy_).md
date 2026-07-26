---
title: 'init(_:strategy:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(_:strategy:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(_:strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28_%3Astrategy%3A%29.json'
content_hash: 'sha256:4a72b8b513006a06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(_:strategy:)

<sub>Initializer</sub>

Creates a URL instance by parsing the provided input in accordance with a parse strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ value: T.ParseInput, strategy: T) throws where T : ParseStrategy, T.ParseOutput == URL
```

## Parameters

- `value` — The value to parse, as the input type accepted by `strategy`. For [ParseStrategy](parsestrategy.md), this is [String](../../swift/string.md).

- `strategy` — A parse strategy to apply when parsing `value`.

## Discussion

The following example parses a URL string, with a custom strategy that provides a default value for the port component if the source string doesn’t specify one.

```swift
let urlString = "https://internal.example.com/path/to/endpoint?key=value"
let url = try? URL(urlString, strategy: .url
    .port(.defaultValue(8080))) // https://internal.example.com:8080/path/to/endpoint?key=value

```

## See Also

### Creating a URL by parsing

- [ParseStrategy](parsestrategy.md) — A parse strategy for creating URLs from formatted strings.
