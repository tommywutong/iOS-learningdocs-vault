---
title: releaseInfo
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataproviderdirectcallbacks/releaseinfo
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/releaseinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderdirectcallbacks/releaseinfo.json'
content_hash: 'sha256:f2884c65e769cbd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md)

# releaseInfo

<sub>Instance Property</sub>

A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var releaseInfo: CGDataProviderReleaseInfoCallback?
```

## See Also

### Instance Properties

- [getBytePointer](getbytepointer.md) — A pointer to a function that returns a pointer to the provider’s data. For more information, see [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md).
- [getBytesAtPosition](getbytesatposition.md) — A pointer to a function that copies data from the provider.
- [releaseBytePointer](releasebytepointer.md) — A pointer to a function that Core Graphics calls to release a pointer to the provider’s data. For more information, see [CGDataProviderReleaseBytePointerCallback](../cgdataproviderreleasebytepointercallback.md).
- [version](version.md) — The version of this structure. It should be set to 0.
