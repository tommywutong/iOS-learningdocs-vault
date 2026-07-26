---
title: MTLCPUCacheMode.writeCombined
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcpucachemode/writecombined
source_url: 'https://developer.apple.com/documentation/metal/mtlcpucachemode/writecombined'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcpucachemode/writecombined.json'
content_hash: 'sha256:1cd3a32c96d0f046'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCPUCacheMode](../mtlcpucachemode.md)

# MTLCPUCacheMode.writeCombined

<sub>Case</sub>

A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case writeCombined
```

## Discussion

Write-combined memory is optimized for resources that the CPU writes into, but never reads. On some implementations, writes may bypass caches to avoid cache pollution. Read actions may perform very poorly.

Applications should use write combining only if writing to normally cached buffers is known to cause performance issues due to cache pollution, as write-combined memory can have surprising performance pitfalls.  Another approach is to use non-temporal writes to normally cached memory (STNP on ARMv8, _mm_stream_* on x86_64).

## See Also

### Specifying the cache mode

- [MTLCPUCacheModeDefaultCache](defaultcache.md) — The default CPU cache mode for the resource, which guarantees that read and write operations are executed in the expected order.
