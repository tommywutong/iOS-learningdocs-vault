---
title: MTLCPUCacheMode.defaultCache
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcpucachemode/defaultcache
source_url: 'https://developer.apple.com/documentation/metal/mtlcpucachemode/defaultcache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcpucachemode/defaultcache.json'
content_hash: 'sha256:11106845149d202a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCPUCacheMode](../mtlcpucachemode.md)

# MTLCPUCacheMode.defaultCache

<sub>Case</sub>

The default CPU cache mode for the resource, which guarantees that read and write operations are executed in the expected order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case defaultCache
```

## See Also

### Specifying the cache mode

- [MTLCPUCacheModeWriteCombined](writecombined.md) — A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.
