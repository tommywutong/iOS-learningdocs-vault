---
title: resourceLoader
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasset/resourceloader
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/resourceloader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/resourceloader.json'
content_hash: 'sha256:67e073370eb544f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# resourceLoader

<sub>Instance Property</sub>

The resource loader for the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var resourceLoader: AVAssetResourceLoader { get }
```

## Discussion

During loading, the system may ask the resource loader to assist loading the resource. For example, a resource that requires decryption may require the resource loader to provide the appropriate decryption keys. You can assign a delegate object to the resource loader object and use your delegate to intercept these requests and provide appropriate responses.

## See Also

### Assisting with resource loading

- [mayRequireContentKeysForMediaDataProcessing](mayrequirecontentkeysformediadataprocessing.md) — A Boolean value that indicates whether you can add this asset as a content key recipient to a content key session.
