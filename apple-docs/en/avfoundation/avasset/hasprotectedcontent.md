---
title: hasProtectedContent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+（16.0 起废弃）, iPadOS 4.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/hasprotectedcontent
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/hasprotectedcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/hasprotectedcontent.json'
content_hash: 'sha256:2555f8d092b43df1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# hasProtectedContent

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset contains protected content.

> [!warning] Deprecated
> Load the value of [hasProtectedContent](../avpartialasyncproperty/hasprotectedcontent.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var hasProtectedContent: Bool { get }
```

## Discussion

Assets that contain protected content may not be playable without successful authorization, even if the value of its [playable](isplayable.md) property is [true](../../swift/true.md).
