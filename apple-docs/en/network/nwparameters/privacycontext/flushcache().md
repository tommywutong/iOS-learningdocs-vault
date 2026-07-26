---
title: flushCache()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/privacycontext/flushcache()
source_url: 'https://developer.apple.com/documentation/network/nwparameters/privacycontext/flushcache()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/privacycontext/flushcache%28%29.json'
content_hash: 'sha256:7fe2947b20574f1a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWParameters](../../nwparameters.md) · [PrivacyContext](../privacycontext.md)

# flushCache()

<sub>Instance Method</sub>

Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flushCache()
```

## Discussion

Flushing the cache may be asynchronous, which means that it will take effect shortly after you invoke the function.

## See Also

### Configuring Custom Privacy Settings

- [init(description:)](<init(description_).md>) — Initializes a privacy context with a description string.
- [default](default.md) — The privacy context that applies to all connections that do not use a custom context.
- [disableLogging()](<disablelogging().md>) — Disables system logging of connection activity.
