---
title: assetCache
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasset/assetcache
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/assetcache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/assetcache.json'
content_hash: 'sha256:525721c83d2c39ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# assetCache

<sub>Instance Property</sub>

The asset’s associated asset cache, if it exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var assetCache: AVAssetCache? { get }
```

## Discussion

This property provides access to an instance of [AVAssetCache](../avassetcache.md) to use for inspection of locally cached media data. The value of this property is `nil` if you haven’t configured the asset to store or access media data from disk.
