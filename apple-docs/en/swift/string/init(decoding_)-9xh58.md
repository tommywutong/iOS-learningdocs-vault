---
title: 'init(decoding:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(decoding:)-9xh58'
source_url: 'https://developer.apple.com/documentation/swift/string/init(decoding:)-9xh58'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28decoding%3A%29-9xh58.json'
content_hash: 'sha256:fb66ded773a095c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(decoding:)

<sub>Initializer</sub>

Creates a string by interpreting the path component’s content as UTF-8 on Unix and UTF-16 on Windows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(decoding component: FilePath.Component)
```

## Parameters

- `component` — The path component to be interpreted as `CInterop.PlatformUnicodeEncoding`.

## Discussion

If the content of the path component isn’t a well-formed Unicode string, this initializer replaces invalid bytes with U+FFFD. This means that, depending on the semantics of the specific file system, conversion to a string and back to a path component might result in a value that’s different from the original path component.
