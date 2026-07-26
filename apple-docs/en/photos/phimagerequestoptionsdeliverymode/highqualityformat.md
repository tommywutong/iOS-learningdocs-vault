---
title: PHImageRequestOptionsDeliveryMode.highQualityFormat
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsdeliverymode/highqualityformat
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsdeliverymode/highqualityformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsdeliverymode/highqualityformat.json'
content_hash: 'sha256:5ce6fe7c26a1b7df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md)

# PHImageRequestOptionsDeliveryMode.highQualityFormat

<sub>Case</sub>

Photos provides only the highest-quality image available, regardless of how much time it takes to load.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case highQualityFormat
```

## Discussion

If the [synchronous](../phimagerequestoptions/issynchronous.md) property is `true` or if using the [requestImageDataForAsset:options:resultHandler:](../phimagemanager/requestimagedataforasset_options_resulthandler_.md) method, this behavior is the default and only option (that is, specifying other delivery mode options has no effect).

## See Also

### Constants

- [PHImageRequestOptionsDeliveryModeOpportunistic](opportunistic.md) — Photos automatically provides one or more results in order to balance image quality and responsiveness.
- [PHImageRequestOptionsDeliveryModeFastFormat](fastformat.md) — Photos provides only a fast-loading image, possibly sacrificing image quality.
