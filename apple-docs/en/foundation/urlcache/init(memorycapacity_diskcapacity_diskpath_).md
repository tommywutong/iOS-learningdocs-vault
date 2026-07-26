---
title: 'init(memoryCapacity:diskCapacity:diskPath:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/urlcache/init(memorycapacity:diskcapacity:diskpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/init(memorycapacity:diskcapacity:diskpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/init%28memorycapacity%3Adiskcapacity%3Adiskpath%3A%29.json'
content_hash: 'sha256:d0faceeecd711d84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# init(memoryCapacity:diskCapacity:diskPath:)

<sub>Initializer</sub>

Creates a URL cache object with the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(memoryCapacity: Int, diskCapacity: Int, diskPath path: String?)
```

## Parameters

- `memoryCapacity` — The memory capacity of the cache, in bytes.

- `diskCapacity` — The disk capacity of the cache, in bytes.

- `path` — In macOS, `path` is the location at which to store the on-disk cache. In iOS, `path` is the name of a subdirectory of the application’s default cache directory in which to store the on-disk cache (the subdirectory is created if it does not exist).

## Return Value

The initialized cache object.

## Discussion

The returned cache instance is backed by disk, so you have more leeway when choosing the capacity for this kind of cache. A disk cache measured in the tens of megabytes should be acceptable in most cases.

## See Also

### Related Documentation

- [sharedURLCache](shared.md) — The shared URL cache instance.

### Creating a new cache object

- [init(memoryCapacity:diskCapacity:directory:)](<init(memorycapacity_diskcapacity_directory_).md>) — Creates a URL cache object with the specified memory and disk capacities, in the specified directory.
