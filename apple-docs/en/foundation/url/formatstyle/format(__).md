---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/formatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/format%28_%3A%29.json'
content_hash: 'sha256:28c946f4e60fbc49'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [FormatStyle](../formatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Formats a URL, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: URL) -> String
```

## Parameters

- `value` — The URL to format.

## Return Value

A string representation of `value`, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple URL instances. The following example creates a custom format style and then uses it to format a variety of URLs in an array:

```swift
let style = URL.FormatStyle(
    scheme: .never,
    user: .never,
    password: .never,
    host: .omitSpecificSubdomains(["www", "mobile", "m."],
                                  includeMultiLevelSubdomains: true),
    port: .never,
    path: .always,
    query: .never,
    fragment: .never)
let urls = [
    URL(string: "https://www.example.com/path/one")!,
    URL(string: "https://beta.example.com/path/two")!,
    URL(string: "https://beta.staging.west.example.com/three")!,
    URL(string: "https://query.example.com/four?key4=value4")!
]
let formatted = urls.map { $0.formatted(style) } // ["example.com/path/one", "beta.example.com/path/two", "west.example.com/three", "query.example.com/four"]
```

To format a single floating-point value, use the [URL](../../url.md) instance method [formatted(_:)](<../formatted(__).md>) method passing in an instance of [FormatStyle](../formatstyle.md), or [formatted()](<../formatted().md>) to use a default style.
