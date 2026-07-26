---
title: url
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/url
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/url.json'
content_hash: 'sha256:032d0b2ba523d15f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# url

<sub>Type Property</sub>

A style for formatting a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var url: URL.FormatStyle { get }
```

## Discussion

Use the dot-notation form of this type property when the call point allows the use of [FormatStyle](../url/formatstyle.md). You typically do this when calling the [formatted(_:)](<../url/formatted(__).md>) method of [URL](../url.md).

The format style provided by this static accessor provides a default behavior. To customize formatting behavior, use the modifiers in Customizing style behavior.

The following example shows the use of a customized URL format style, created by modifying the default style. The custom style strips the scheme and port and omits the `www` subdomain, but leaves the path intact. This produces a simplified URL representation that a browser could use as a window title.

```swift
let url = URL(string: "http://www.example.com:8080/path/to/file.txt")!
let formatted = url.formatted(.url
    .scheme(.never)
    .host(.omitSpecificSubdomains(["www"]))
    .port(.never)) // "example.com/path/to/file.txt"
```

## See Also

### Applying URL styles

- [FormatStyle](../url/formatstyle.md) — A structure that converts between URL instances and their textual representations.
