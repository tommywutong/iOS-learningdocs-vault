---
title: PHVideoRequestOptionsDeliveryMode.fastFormat
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptionsdeliverymode/fastformat
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptionsdeliverymode/fastformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptionsdeliverymode/fastformat.json'
content_hash: 'sha256:44019d19818abc17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHVideoRequestOptionsDeliveryMode](../phvideorequestoptionsdeliverymode.md)

# PHVideoRequestOptionsDeliveryMode.fastFormat

<sub>Case</sub>

Photos provides whatever quality of video can be most quickly loaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case fastFormat
```

## Discussion

When the [networkAccessAllowed](../phvideorequestoptions/isnetworkaccessallowed.md) property is `true`, the fast option provides a version of the video asset suitable for streaming from iCloud over a low-quality connection—for example, an MP4 video with 360p resolution. If a higher-quality version is already cached on the device, Photos provides that video instead.

## See Also

### Constants

- [PHVideoRequestOptionsDeliveryModeAutomatic](automatic.md) — Photos automatically determines which quality of video data to provide based on the request and current conditions.
- [PHVideoRequestOptionsDeliveryModeHighQualityFormat](highqualityformat.md) — Photos provides only the highest quality video available.
- [PHVideoRequestOptionsDeliveryModeMediumQualityFormat](mediumqualityformat.md) — Photos provides a video of moderate quality unless a higher quality version is locally cached.
