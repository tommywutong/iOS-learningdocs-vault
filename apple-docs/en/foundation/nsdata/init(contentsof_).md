---
title: 'init(contentsOf:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(contentsof:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28contentsof%3A%29.json'
content_hash: 'sha256:a21d7cd3391fc409'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(contentsOf:)

<sub>Initializer</sub>

Creates a data object from the data at the specified file URL, or returns `nil` if the system can’t create one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(contentsOf url: URL)
```

## Parameters

- `url` — The location on disk of the data to read.

## Discussion

> [!important] Important
> As this method runs synchronously and blocks the calling thread until it finishes, don’t invoke it from the main thread. Use file coordination or one of the nonblocking file-related APIs instead.

If you specify a malformed URL or the referenced location doesn’t exist on disk, the initializer fails and returns `nil`. To handle such errors, use `NSData/init(contentsOfURL:options:)-5abi3` instead.
