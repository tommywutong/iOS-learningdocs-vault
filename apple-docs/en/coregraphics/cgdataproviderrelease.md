---
title: CGDataProviderRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataproviderrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderrelease.json'
content_hash: 'sha256:796828da608f41fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderRelease

<sub>Function</sub>

Decrements the retain count of a data provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGDataProviderRelease(CGDataProviderRef provider);
```

## Parameters

- `provider` — The data provider to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `provider` parameter is `NULL`.

## See Also

### Retaining and Releasing Data Providers

- [CGDataProviderRetain](cgdataproviderretain.md) — Increments the retain count of a data provider.
