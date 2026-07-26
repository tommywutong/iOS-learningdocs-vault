---
title: 'init(named:inBundle:compatibleWithTraitCollection:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/init(named:inbundle:compatiblewithtraitcollection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/init(named:inbundle:compatiblewithtraitcollection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/init%28named%3Ainbundle%3Acompatiblewithtraitcollection%3A%29.json'
content_hash: 'sha256:2a45e28c396cf123'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# init(named:inBundle:compatibleWithTraitCollection:)

<sub>Initializer</sub>

Creates a color object using the named asset that’s compatible with the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(named name: String, inBundle bundle: Bundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?)
```

## Parameters

- `name` — The name of the asset containing the color.

- `bundle` — The bundle containing the asset.

- `traitCollection` — The trait collection that specifies the gamut to use when selecting the color.

## Return Value

An initialized color object. The returned object uses the color space specified for the asset.
