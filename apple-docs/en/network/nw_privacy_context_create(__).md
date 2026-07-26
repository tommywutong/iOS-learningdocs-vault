---
title: 'nw_privacy_context_create(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_privacy_context_create(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_privacy_context_create(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_privacy_context_create%28_%3A%29.json'
content_hash: 'sha256:30acc348aa2f167f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_privacy_context_create(_:)

<sub>Function</sub>

Initializes a privacy context with a description string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_privacy_context_create(_ description: UnsafePointer<CChar>) -> nw_privacy_context_t
```

## See Also

### Configuring Custom Privacy Settings

- [nw_privacy_context_disable_logging](<nw_privacy_context_disable_logging(__).md>) — Disables system logging of connection activity.
- [nw_privacy_context_flush_cache](<nw_privacy_context_flush_cache(__).md>) — Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.
