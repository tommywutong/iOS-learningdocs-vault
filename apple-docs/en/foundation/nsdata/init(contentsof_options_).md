---
title: 'init(contentsOf:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(contentsof:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(contentsof:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28contentsof%3Aoptions%3A%29.json'
content_hash: 'sha256:4b21e25f5379da19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(contentsOf:options:)

<sub>Initializer</sub>

Creates a data object from the data at the provided file URL using specific reading options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(contentsOf url: URL, options readOptionsMask: NSData.ReadingOptions = []) throws
```

## Parameters

- `url` — The location on disk of the data to read.

- `readOptionsMask` — The mask specifying the options to use when reading the data. For more information, see [ReadingOptions](readingoptions.md).

## Discussion

> [!important] Important
> As this method runs synchronously and blocks the calling thread until it finishes, don’t invoke it from the main thread. Use file coordination or one of the nonblocking file-related APIs instead.

If the system can’t create an instance, the initializer may throw in Swift, or return `nil` in Objective-C.
