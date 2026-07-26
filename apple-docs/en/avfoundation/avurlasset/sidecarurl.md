---
title: sidecarURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasset/sidecarurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/sidecarurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/sidecarurl.json'
content_hash: 'sha256:c46ef44214b342ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# sidecarURL

<sub>Instance Property</sub>

The sidecar URL used by the MediaExtension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, nullable) NSURL * sidecarURL;
```

## Discussion

The sidecar URL is returned only if the MediaExtension format reader supports sidecar files, and implements this property [MEFileInfo setSidecarFilename:]. Will return nil otherwise.

## See Also

### Accessing Media Extension properties

- [mediaExtensionProperties](mediaextensionproperties.md) — The properties of the media extension format reader that decodes the asset.
- [AVMediaExtensionProperties](../avmediaextensionproperties.md) — An object that describes a Media Extension.
