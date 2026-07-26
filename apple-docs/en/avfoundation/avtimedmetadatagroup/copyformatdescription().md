---
title: copyFormatDescription()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avtimedmetadatagroup/copyformatdescription()
source_url: 'https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/copyformatdescription()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtimedmetadatagroup/copyformatdescription%28%29.json'
content_hash: 'sha256:d1fbf50cdc0d5ef7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTimedMetadataGroup](../avtimedmetadatagroup.md)

# copyFormatDescription()

<sub>Instance Method</sub>

Creates a format description based on the receiver’s items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyFormatDescription() -> CMMetadataFormatDescription?
```

## Return Value

An instance of [CMMetadataFormatDescription](../../coremedia/cmmetadataformatdescription.md) sufficient to describe the contents of all the items referenced by the object.

## Discussion

The returned format description is suitable for use as the format hint parameter when creating an instance of [AVAssetWriterInput](../avassetwriterinput.md).

Each item referenced by the receiver must carry a non-`nil` value for its `dataType` property.  An exception will be thrown if any item does not have a data type.
