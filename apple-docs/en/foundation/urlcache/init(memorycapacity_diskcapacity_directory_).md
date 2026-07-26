---
title: 'init(memoryCapacity:diskCapacity:directory:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcache/init(memorycapacity:diskcapacity:directory:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/init(memorycapacity:diskcapacity:directory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/init%28memorycapacity%3Adiskcapacity%3Adirectory%3A%29.json'
content_hash: 'sha256:59f823cd8f25877d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# init(memoryCapacity:diskCapacity:directory:)

<sub>Initializer</sub>

Creates a URL cache object with the specified memory and disk capacities, in the specified directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(memoryCapacity: Int, diskCapacity: Int, directory: URL? = nil)
```

## Parameters

- `memoryCapacity` — The memory capacity of the cache, in bytes.

- `diskCapacity` — The disk capacity of the cache, in bytes.

- `directory` — The path to an on-disk directory, where the system stores the on-disk cache. If `directory` is `nil`, the cache uses a default directory.

## Discussion

A disk cache measured in the tens of megabytes is acceptable in most cases.

## See Also

### Creating a new cache object

- [- initWithMemoryCapacity:diskCapacity:diskPath:](<init(memorycapacity_diskcapacity_diskpath_).md>) — Creates a URL cache object with the specified values. _(deprecated)_
