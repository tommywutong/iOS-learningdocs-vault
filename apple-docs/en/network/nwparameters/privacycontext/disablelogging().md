---
title: disableLogging()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/privacycontext/disablelogging()
source_url: 'https://developer.apple.com/documentation/network/nwparameters/privacycontext/disablelogging()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/privacycontext/disablelogging%28%29.json'
content_hash: 'sha256:0a2fcf719b62d055'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWParameters](../../nwparameters.md) · [PrivacyContext](../privacycontext.md)

# disableLogging()

<sub>Instance Method</sub>

Disables system logging of connection activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func disableLogging()
```

## See Also

### Configuring Custom Privacy Settings

- [init(description:)](<init(description_).md>) — Initializes a privacy context with a description string.
- [default](default.md) — The privacy context that applies to all connections that do not use a custom context.
- [flushCache()](<flushcache().md>) — Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.
