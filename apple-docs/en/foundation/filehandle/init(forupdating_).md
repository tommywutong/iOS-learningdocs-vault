---
title: 'init(forUpdating:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/init(forupdating:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/init(forupdating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/init%28forupdating%3A%29.json'
content_hash: 'sha256:ef96885ee406a5e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# init(forUpdating:)

<sub>Initializer</sub>

Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(forUpdating url: URL) throws
```

## Parameters

- `url` — The URL of the file, device, or named socket to access.

## Return Value

The initialized file handle object or `nil` if no file exists at `url`.

## Discussion

The file pointer is set to the beginning of the file. The returned object responds to both read and [- writeData:](<write(__).md>) messages.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.
