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
doc_path: '/documentation/swift/string/init(decoding:)-364r2'
source_url: 'https://developer.apple.com/documentation/swift/string/init(decoding:)-364r2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28decoding%3A%29-364r2.json'
content_hash: 'sha256:4910e59a0316a5dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(decoding:)

<sub>Initializer</sub>

On Unix, creates the string `"/"`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(decoding root: FilePath.Root)
```

## Parameters

- `root` — The path root to be interpreted as `CInterop.PlatformUnicodeEncoding`.

## Discussion

On Windows, creates a string by interpreting the path root’s content as UTF-16.

If the content of the path root isn’t a well-formed Unicode string, this initializer replaces invalid bytes with U+FFFD. This means that on Windows, conversion to a string and back to a path root might result in a value that’s different from the original path root.
