---
title: PHVideoRequestOptionsDeliveryMode.automatic
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptionsdeliverymode/automatic
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptionsdeliverymode/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptionsdeliverymode/automatic.json'
content_hash: 'sha256:1ea88453e12ab9fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHVideoRequestOptionsDeliveryMode](../phvideorequestoptionsdeliverymode.md)

# PHVideoRequestOptionsDeliveryMode.automatic

<sub>Case</sub>

Photos automatically determines which quality of video data to provide based on the request and current conditions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

When you request an [AVAsset](../../avfoundation/avasset.md) or [AVPlayerItem](../../avfoundation/avplayeritem.md) object, Photos typically uses the medium-quality format. When you request an [AVAssetExportSession](../../avfoundation/avassetexportsession.md) object for writing out the asset’s contents, Photos always uses the high-quality format.

## See Also

### Constants

- [PHVideoRequestOptionsDeliveryModeHighQualityFormat](highqualityformat.md) — Photos provides only the highest quality video available.
- [PHVideoRequestOptionsDeliveryModeMediumQualityFormat](mediumqualityformat.md) — Photos provides a video of moderate quality unless a higher quality version is locally cached.
- [PHVideoRequestOptionsDeliveryModeFastFormat](fastformat.md) — Photos provides whatever quality of video can be most quickly loaded.
