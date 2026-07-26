---
title: version
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataprovidersequentialcallbacks/version
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovidersequentialcallbacks/version.json'
content_hash: 'sha256:483179e03602b799'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProviderSequentialCallbacks](../cgdataprovidersequentialcallbacks.md)

# version

<sub>Instance Property</sub>

The version of this structure. It should be set to 0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var version: UInt32
```

## See Also

### Instance Properties

- [getBytes](getbytes.md) — A pointer to a function that copies data from the provider. For more information, see [CGDataProviderGetBytesCallback](../cgdataprovidergetbytescallback.md).
- [releaseInfo](releaseinfo.md) — A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md).
- [rewind](rewind.md) — A pointer to a function Core Graphics calls to return the provider to the beginning of the data stream. For more information, see [CGDataProviderRewindCallback](../cgdataproviderrewindcallback.md).
- [skipForward](skipforward.md) — A pointer to a function that Core Graphics calls to advance the stream of data supplied by the provider.
