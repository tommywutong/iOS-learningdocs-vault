---
title: 'initWithMemoryCapacity:diskCapacity:directoryURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcache/initwithmemorycapacity:diskcapacity:directoryurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcache/initwithmemorycapacity:diskcapacity:directoryurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcache/initwithmemorycapacity%3Adiskcapacity%3Adirectoryurl%3A.json'
content_hash: 'sha256:4a0e0d945595241d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# initWithMemoryCapacity:diskCapacity:directoryURL:

<sub>Instance Method</sub>

Creates a URL cache object with the specified memory and disk capacities, in the specified directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithMemoryCapacity:(NSUInteger) memoryCapacity diskCapacity:(NSUInteger) diskCapacity directoryURL:(NSURL *) directoryURL;
```

## Parameters

- `memoryCapacity` — The memory capacity of the cache, in bytes.

- `diskCapacity` — The disk capacity of the cache, in bytes.

- `directoryURL` — The path to an on-disk directory at which to store the on-disk cache. If `directory` is `nil`, the cache uses a default directory.

## Discussion

A disk cache measured in the tens of megabytes should be acceptable in most cases.

## See Also

### Creating a new cache object

- [- initWithMemoryCapacity:diskCapacity:diskPath:](<../urlcache/init(memorycapacity_diskcapacity_diskpath_).md>) — Creates a URL cache object with the specified values. _(deprecated)_
