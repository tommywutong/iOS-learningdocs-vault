---
title: 'init(contentsOf:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(contentsof:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(contentsof:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28contentsof%3Aoptions%3A%29.json'
content_hash: 'sha256:b1d77efc103c5b14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(contentsOf:options:)

<sub>Initializer</sub>

Creates data by reading from the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(contentsOf url: URL, options: Data.ReadingOptions = []) throws
```

## Parameters

- `url` — The `URL` to read.

- `options` — Options for the read operation. Default value is `[]`.

## Discussion

> [!danger] Throws
> An error in the Cocoa domain, if `url` cannot be read.
