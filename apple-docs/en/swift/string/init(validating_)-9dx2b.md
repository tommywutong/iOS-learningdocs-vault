---
title: 'init(validating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(validating:)-9dx2b'
source_url: 'https://developer.apple.com/documentation/swift/string/init(validating:)-9dx2b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28validating%3A%29-9dx2b.json'
content_hash: 'sha256:9bdf68ad81ab997d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(validating:)

<sub>Initializer</sub>

Creates a string from a file path, validating its contents as UTF-8 on Unix and UTF-16 on Windows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(validating path: FilePath)
```

## Parameters

- `path` — The file path to be interpreted as `CInterop.PlatformUnicodeEncoding`.

## Discussion

If the contents of the file path isn’t a well-formed Unicode string, this initializer returns `nil`.
