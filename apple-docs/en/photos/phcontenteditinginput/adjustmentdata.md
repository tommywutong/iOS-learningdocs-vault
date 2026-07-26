---
title: adjustmentData
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/adjustmentdata
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/adjustmentdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/adjustmentdata.json'
content_hash: 'sha256:cec264a7ef5ae59a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# adjustmentData

<sub>Instance Property</sub>

An object that describes the most recent edit to the asset’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var adjustmentData: PHAdjustmentData? { get }
```

## Discussion

Adjustment data describes the “recipe” for the last edit made to an asset’s photo or video content. For example, a photo editing app can use this property to read information about a set of filters applied to a photo. With this information, your app can later allow a user to change the filter parameters.
