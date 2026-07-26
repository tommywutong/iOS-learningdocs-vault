---
title: 'init(contentsOfFile:usedEncoding:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(contentsoffile:usedencoding:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(contentsoffile:usedencoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28contentsoffile%3Ausedencoding%3A%29.json'
content_hash: 'sha256:8e4fa21fe6cc8a2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(contentsOfFile:usedEncoding:)

<sub>Initializer</sub>

Produces a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(contentsOfFile path: String, usedEncoding: inout String.Encoding) throws
```

## See Also

### Creating a String from a File or URL

- [init(contentsOf:)](<init(contentsof_).md>) _(deprecated)_
- [init(contentsOf:encoding:)](<init(contentsof_encoding_).md>) — Produces a string created by reading data from a given URL interpreted using a given encoding.
- [init(contentsOf:usedEncoding:)](<init(contentsof_usedencoding_).md>) — Produces a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [init(contentsOfFile:)](<init(contentsoffile_).md>) _(deprecated)_
- [init(contentsOfFile:encoding:)](<init(contentsoffile_encoding_).md>) — Produces a string created by reading data from the file at a given path interpreted using a given encoding.
