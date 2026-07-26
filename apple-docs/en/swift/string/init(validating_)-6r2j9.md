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
doc_path: '/documentation/swift/string/init(validating:)-6r2j9'
source_url: 'https://developer.apple.com/documentation/swift/string/init(validating:)-6r2j9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28validating%3A%29-6r2j9.json'
content_hash: 'sha256:5cc8cf21c62edaea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(validating:)

<sub>Initializer</sub>

On Unix, creates the string `"/"`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(validating root: FilePath.Root)
```

## Parameters

- `root` — The path root to be interpreted as `CInterop.PlatformUnicodeEncoding`.

## Discussion

On Windows, creates a string from a path root, validating its contents as UTF-16 on Windows.

On Windows, if the contents of the path root isn’t a well-formed Unicode string, this initializer returns `nil`.
