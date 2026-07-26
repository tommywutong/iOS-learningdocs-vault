---
title: PHImageRequestOptionsDeliveryMode.fastFormat
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsdeliverymode/fastformat
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsdeliverymode/fastformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsdeliverymode/fastformat.json'
content_hash: 'sha256:8ff36e99cae0d7ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md)

# PHImageRequestOptionsDeliveryMode.fastFormat

<sub>Case</sub>

Photos provides only a fast-loading image, possibly sacrificing image quality.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case fastFormat
```

## Discussion

Photos calls your `resultHandler` block once. If a high-quality image cannot be loaded quickly, the result handler provides a low-quality image. Check the [PHImageResultIsDegradedKey](../phimageresultisdegradedkey.md) key in the info dictionary to determine the quality of image provided to the result handler.

This option is available only if the [synchronous](../phimagerequestoptions/issynchronous.md) property is `false`.

## See Also

### Constants

- [PHImageRequestOptionsDeliveryModeOpportunistic](opportunistic.md) — Photos automatically provides one or more results in order to balance image quality and responsiveness.
- [PHImageRequestOptionsDeliveryModeHighQualityFormat](highqualityformat.md) — Photos provides only the highest-quality image available, regardless of how much time it takes to load.
