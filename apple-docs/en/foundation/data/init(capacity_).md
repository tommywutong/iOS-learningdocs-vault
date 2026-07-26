---
title: 'init(capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28capacity%3A%29.json'
content_hash: 'sha256:98210a841035d405'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(capacity:)

<sub>Initializer</sub>

Creates an empty data buffer of a specified size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(capacity: Int)
```

## Parameters

- `capacity` — The size of the data.

## Discussion

This initializer doesn’t necessarily allocate the requested memory right away. `Data` allocates additional memory as needed, so `capacity` simply establishes the initial capacity. When it does allocate the initial memory, though, it allocates the specified amount.

This method sets the `count` of the data to 0.

If the capacity specified in `capacity` is greater than four memory pages in size, this may round the amount of requested memory up to the nearest full page.

## See Also

### Creating Empty Data

- [init()](<init().md>) — Creates an empty data buffer.
- [init(count:)](<init(count_).md>) — Creates a new data buffer with the specified count of zeroed bytes.
- [resetBytes(in:)](<resetbytes(in_).md>) — Sets a region of the data buffer to `0`.
