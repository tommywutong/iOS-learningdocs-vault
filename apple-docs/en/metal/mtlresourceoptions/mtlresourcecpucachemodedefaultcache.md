---
title: MTLResourceCPUCacheModeDefaultCache
framework: Metal
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceoptions/mtlresourcecpucachemodedefaultcache
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcecpucachemodedefaultcache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceoptions/mtlresourcecpucachemodedefaultcache.json'
content_hash: 'sha256:f80cef4b098ea55a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceOptions](../mtlresourceoptions.md)

# MTLResourceCPUCacheModeDefaultCache

<sub>Enumeration Case</sub>

The default CPU cache mode for the resource, which guarantees that read and write operations are executed in the expected order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
MTLResourceCPUCacheModeDefaultCache
```

## See Also

### Specifying CPU cache modes

- [MTLResourceCPUCacheModeWriteCombined](cpucachemodewritecombined.md) — A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.
