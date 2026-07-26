---
title: deliveryMode
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptions/deliverymode
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptions/deliverymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptions/deliverymode.json'
content_hash: 'sha256:7eeeae28e6aaa08f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHVideoRequestOptions](../phvideorequestoptions.md)

# deliveryMode

<sub>Instance Property</sub>

A mode specifying the requested video quality and delivery priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var deliveryMode: PHVideoRequestOptionsDeliveryMode { get set }
```

## Discussion

Use this property to tell Photos to provide a video quickly (possibly sacrificing image quality) or to provide a high-quality video (possibly sacrificing speed). This option applies only when requesting the current version of the video (that is, only when the [version](version.md) property is [PHVideoRequestOptionsVersionCurrent](../phvideorequestoptionsversion/current.md)).

The default option is [PHVideoRequestOptionsDeliveryModeAutomatic](../phvideorequestoptionsdeliverymode/automatic.md). See [PHVideoRequestOptionsDeliveryMode](../phvideorequestoptionsdeliverymode.md).

## See Also

### Specifying Video Request Options

- [version](version.md) — The version of the video to request.
- [PHVideoRequestOptionsVersion](../phvideorequestoptionsversion.md) — Options for requesting a video asset with or without adjustments, used by the [version](version.md) property.
- [PHVideoRequestOptionsDeliveryMode](../phvideorequestoptionsdeliverymode.md) — Options for delivering requested video data, used by the [deliveryMode](deliverymode.md) property.
