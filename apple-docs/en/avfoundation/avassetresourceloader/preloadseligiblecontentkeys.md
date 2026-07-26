---
title: preloadsEligibleContentKeys
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloader/preloadseligiblecontentkeys
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloader/preloadseligiblecontentkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloader/preloadseligiblecontentkeys.json'
content_hash: 'sha256:5778e8eb547ad86d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoader](../avassetresourceloader.md)

# preloadsEligibleContentKeys

<sub>Instance Property</sub>

A Boolean value that indicates whether content keys will be loaded as quickly as possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preloadsEligibleContentKeys: Bool { get set }
```

## Discussion

Set this property to `true` to load eligible keys. This may result in network activity. All work done as a result of setting this property to `true` is performed asynchronously.
