---
title: getBytesAtPosition
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataproviderdirectcallbacks/getbytesatposition
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/getbytesatposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderdirectcallbacks/getbytesatposition.json'
content_hash: 'sha256:45340fb5d70810d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md)

# getBytesAtPosition

<sub>Instance Property</sub>

A pointer to a function that copies data from the provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?
```

## See Also

### Instance Properties

- [getBytePointer](getbytepointer.md) — A pointer to a function that returns a pointer to the provider’s data. For more information, see [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md).
- [releaseBytePointer](releasebytepointer.md) — A pointer to a function that Core Graphics calls to release a pointer to the provider’s data. For more information, see [CGDataProviderReleaseBytePointerCallback](../cgdataproviderreleasebytepointercallback.md).
- [releaseInfo](releaseinfo.md) — A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md).
- [version](version.md) — The version of this structure. It should be set to 0.
