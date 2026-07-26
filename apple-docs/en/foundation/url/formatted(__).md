---
title: 'formatted(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatted%28_%3A%29.json'
content_hash: 'sha256:fe6b5c7ca91ae748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# formatted(_:)

<sub>Instance Method</sub>

Formats the URL, using the provided format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<F>(_ format: F) -> F.FormatOutput where F : FormatStyle, F.FormatInput == URL
```

## Parameters

- `format` — The format style to apply when formatting the URL.

## Return Value

A formatted string representation of the URL.

## Discussion

Use this method when you want to format a single URL value with a specific format style, or call it repeatedly with different format styles. The following example uses the static accessor [url](../formatstyle/url.md) to get a default style, then modifies its behavior to include or omit different URL components when [formatted(_:)](<formatted(__).md>) creates the string:

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let formatted = url.formatted(.url
    .scheme(.never)
    .host(.always)
    .port(.never)
    .path(.always)
    .query(.never)) // "www.example.com/path/to/endpoint"

```

## See Also

### Formatting a URL

- [formatted()](<formatted().md>) — Formats the URL using a default format style.
- [FormatStyle](formatstyle.md) — A structure that converts between URL instances and their textual representations.
