---
title: version
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptions/version
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptions/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptions/version.json'
content_hash: 'sha256:73622b114a560ee0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHVideoRequestOptions](../phvideorequestoptions.md)

# version

<sub>Instance Property</sub>

The version of the video to request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var version: PHVideoRequestOptionsVersion { get set }
```

## Discussion

If a video asset has been edited, use this property to request a video with or without adjustments.

The default option is [PHVideoRequestOptionsVersionCurrent](../phvideorequestoptionsversion/current.md). See [PHVideoRequestOptionsVersion](../phvideorequestoptionsversion.md).

## See Also

### Specifying Video Request Options

- [PHVideoRequestOptionsVersion](../phvideorequestoptionsversion.md) — Options for requesting a video asset with or without adjustments, used by the [version](version.md) property.
- [deliveryMode](deliverymode.md) — A mode specifying the requested video quality and delivery priority.
- [PHVideoRequestOptionsDeliveryMode](../phvideorequestoptionsdeliverymode.md) — Options for delivering requested video data, used by the [deliveryMode](deliverymode.md) property.
