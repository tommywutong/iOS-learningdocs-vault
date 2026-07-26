---
title: creationDate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（16.0 起废弃）, iPadOS 5.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/creationdate
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/creationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/creationdate.json'
content_hash: 'sha256:0917fe16f44024bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# creationDate

<sub>Instance Property</sub>

A metadata item that indicates the asset’s creation date.

> [!warning] Deprecated
> Load the value of [creationDate](../avpartialasyncproperty/creationdate.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var creationDate: AVMetadataItem? { get }
```

## Discussion

If the asset contains metadata that the framework can convert to an [NSDate](../../foundation/nsdate.md), you can retrieve it from the metadata item using its [dateValue](../avmetadataitem/datevalue.md) property. Otherwise, you retrieve it as a string by using the metadata item’s [stringValue](../avmetadataitem/stringvalue.md) property.

This property value is `nil` if no creation date metadata exists.
