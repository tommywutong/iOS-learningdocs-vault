---
title: default
framework: Network
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/privacycontext/default
source_url: 'https://developer.apple.com/documentation/network/nwparameters/privacycontext/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/privacycontext/default.json'
content_hash: 'sha256:ebfc49803fcb1df5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWParameters](../../nwparameters.md) · [PrivacyContext](../privacycontext.md)

# default

<sub>Type Property</sub>

The privacy context that applies to all connections that do not use a custom context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: NWParameters.PrivacyContext
```

## Discussion

You cannot disable logging on the default privacy context.

Flushing the cache on the default privacy context will not affect other privacy contexts.

Changing name resolution settings will only affect privacy contexts that did not already explicitly configure resolution requirements.

## See Also

### Configuring Custom Privacy Settings

- [init(description:)](<init(description_).md>) — Initializes a privacy context with a description string.
- [disableLogging()](<disablelogging().md>) — Disables system logging of connection activity.
- [flushCache()](<flushcache().md>) — Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.
