---
title: deliveryMode
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotorequestoptions/deliverymode
source_url: 'https://developer.apple.com/documentation/photos/phlivephotorequestoptions/deliverymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotorequestoptions/deliverymode.json'
content_hash: 'sha256:f2499a43c1eead6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoRequestOptions](../phlivephotorequestoptions.md)

# deliveryMode

<sub>Instance Property</sub>

The requested Live Photo quality and delivery priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var deliveryMode: PHImageRequestOptionsDeliveryMode { get set }
```

## Discussion

Use this property to tell Photos to provide a Live Photo quickly (possibly sacrificing image quality), to provide a high-quality Live Photo (possibly sacrificing speed), or to provide both automatically if needed. See [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md).

## See Also

### Specifying Image Request Options

- [version](version.md) — The version of the Live Photo to be requested.
