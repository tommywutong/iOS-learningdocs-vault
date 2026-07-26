---
title: CGDataProviderRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataproviderretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderretain.json'
content_hash: 'sha256:1c4c1302fa518004'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderRetain

<sub>Function</sub>

Increments the retain count of a data provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGDataProviderRefCGDataProviderRetain(CGDataProviderRef provider);
```

## Parameters

- `provider` — The data provider to retain.

## Return Value

The same data provider you passed in as the `provider` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `provider` parameter is `NULL`.

## See Also

### Retaining and Releasing Data Providers

- [CGDataProviderRelease](cgdataproviderrelease.md) — Decrements the retain count of a data provider.
