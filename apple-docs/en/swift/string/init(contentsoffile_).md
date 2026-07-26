---
title: 'init(contentsOfFile:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 8.0+（18.0 起废弃）, macOS 10.10+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+, watchOS 2.0+（11.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/string/init(contentsoffile:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(contentsoffile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28contentsoffile%3A%29.json'
content_hash: 'sha256:3764440bbae2cd1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(contentsOfFile:)

<sub>Initializer</sub>

> [!warning] Deprecated
> Use `init(contentsOfFile:encoding:)` instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(contentsOfFile path: String) throws
```

## See Also

### Creating a String from a File or URL

- [init(contentsOf:)](<init(contentsof_).md>) _(deprecated)_
- [init(contentsOf:encoding:)](<init(contentsof_encoding_).md>) — Produces a string created by reading data from a given URL interpreted using a given encoding.
- [init(contentsOf:usedEncoding:)](<init(contentsof_usedencoding_).md>) — Produces a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [init(contentsOfFile:encoding:)](<init(contentsoffile_encoding_).md>) — Produces a string created by reading data from the file at a given path interpreted using a given encoding.
- [init(contentsOfFile:usedEncoding:)](<init(contentsoffile_usedencoding_).md>) — Produces a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.
