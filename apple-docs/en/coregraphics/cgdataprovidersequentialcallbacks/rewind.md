---
title: rewind
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataprovidersequentialcallbacks/rewind
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/rewind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovidersequentialcallbacks/rewind.json'
content_hash: 'sha256:ed0203e80a27db2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProviderSequentialCallbacks](../cgdataprovidersequentialcallbacks.md)

# rewind

<sub>Instance Property</sub>

A pointer to a function Core Graphics calls to return the provider to the beginning of the data stream. For more information, see [CGDataProviderRewindCallback](../cgdataproviderrewindcallback.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rewind: CGDataProviderRewindCallback?
```

## See Also

### Instance Properties

- [getBytes](getbytes.md) — A pointer to a function that copies data from the provider. For more information, see [CGDataProviderGetBytesCallback](../cgdataprovidergetbytescallback.md).
- [releaseInfo](releaseinfo.md) — A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md).
- [skipForward](skipforward.md) — A pointer to a function that Core Graphics calls to advance the stream of data supplied by the provider.
- [version](version.md) — The version of this structure. It should be set to 0.
