---
title: 'nw_privacy_context_flush_cache(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_privacy_context_flush_cache(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_privacy_context_flush_cache(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_privacy_context_flush_cache%28_%3A%29.json'
content_hash: 'sha256:0a20efba90b2da93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_privacy_context_flush_cache(_:)

<sub>Function</sub>

Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_privacy_context_flush_cache(_ privacy_context: nw_privacy_context_t)
```

## Discussion

Flushing the cache may be asynchronous, which means that it will take effect shortly after you invoke the function.

## See Also

### Configuring Custom Privacy Settings

- [nw_privacy_context_create](<nw_privacy_context_create(__).md>) — Initializes a privacy context with a description string.
- [nw_privacy_context_disable_logging](<nw_privacy_context_disable_logging(__).md>) — Disables system logging of connection activity.
