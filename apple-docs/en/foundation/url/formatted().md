---
title: formatted()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/formatted()
source_url: 'https://developer.apple.com/documentation/foundation/url/formatted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatted%28%29.json'
content_hash: 'sha256:fb647225454ec5b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# formatted()

<sub>Instance Method</sub>

Formats the URL using a default format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted() -> String
```

## Return Value

A string representation of the URL, formatted according to the default format style.

## Discussion

Use this method to create a string representation of a URL using the default [FormatStyle](formatstyle.md) configuration. As seen in the following example, the default style creates a string with the scheme, host, and path, but not the port or query.

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let formatted = url.formatted() // "https://www.example.com/path/to/endpoint"
```

To customize formatting of the URL, use [formatted(_:)](<formatted(__).md>), passing in a customized [FormatStyle](formatstyle.md).

## See Also

### Formatting a URL

- [formatted(_:)](<formatted(__).md>) — Formats the URL, using the provided format style.
- [FormatStyle](formatstyle.md) — A structure that converts between URL instances and their textual representations.
