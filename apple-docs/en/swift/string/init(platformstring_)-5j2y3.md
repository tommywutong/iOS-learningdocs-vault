---
title: 'init(platformString:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(platformstring:)-5j2y3'
source_url: 'https://developer.apple.com/documentation/swift/string/init(platformstring:)-5j2y3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28platformstring%3A%29-5j2y3.json'
content_hash: 'sha256:51f2301854acaffc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(platformString:)

<sub>Initializer</sub>

Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(platformString: UnsafePointer<CInterop.PlatformChar>)
```

## Parameters

- `platformString` — The null-terminated platform string to be interpreted as `CInterop.PlatformUnicodeEncoding`.

## Discussion

If the content of the platform string isn’t well-formed Unicode, this initializer replaces invalid bytes with U+FFFD. This means that, depending on the semantics of the specific platform, conversion to a string and back might result in a value that’s different from the original platform string.
