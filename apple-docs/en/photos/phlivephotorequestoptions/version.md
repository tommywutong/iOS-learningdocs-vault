---
title: version
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotorequestoptions/version
source_url: 'https://developer.apple.com/documentation/photos/phlivephotorequestoptions/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotorequestoptions/version.json'
content_hash: 'sha256:ffb8a5e8fdb00050'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoRequestOptions](../phlivephotorequestoptions.md)

# version

<sub>Instance Property</sub>

The version of the Live Photo to be requested.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var version: PHImageRequestOptionsVersion { get set }
```

## Discussion

Use this property to request a version of the Live Photo with or without adjustments. See [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md).

## See Also

### Specifying Image Request Options

- [deliveryMode](deliverymode.md) — The requested Live Photo quality and delivery priority.
