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
doc_path: /documentation/coregraphics/cgdataproviderdirectcallbacks/version
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderdirectcallbacks/version.json'
content_hash: 'sha256:3df4b17523b4a0a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md)

# version

<sub>Instance Property</sub>

The version of this structure. It should be set to 0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var version: UInt32
```

## See Also

### Instance Properties

- [getBytePointer](getbytepointer.md) — A pointer to a function that returns a pointer to the provider’s data. For more information, see [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md).
- [getBytesAtPosition](getbytesatposition.md) — A pointer to a function that copies data from the provider.
- [releaseBytePointer](releasebytepointer.md) — A pointer to a function that Core Graphics calls to release a pointer to the provider’s data. For more information, see [CGDataProviderReleaseBytePointerCallback](../cgdataproviderreleasebytepointercallback.md).
- [releaseInfo](releaseinfo.md) — A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md).
