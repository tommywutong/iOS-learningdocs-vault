---
title: canProvideSubtypes
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttypedescription/canprovidesubtypes
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescription/canprovidesubtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescription/canprovidesubtypes.json'
content_hash: 'sha256:3252344946604ae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescription](../phprojecttypedescription.md)

# canProvideSubtypes

<sub>Instance Property</sub>

A Boolean variable indicating whether subtypes can be fetched from the data source.

<sub>macOS</sub>

```swift
var canProvideSubtypes: Bool { get }
```

## Discussion

The value is `true` if [subtypeDescriptions](subtypedescriptions.md) is not empty.

## See Also

### Describing a Project Type

- [projectType](projecttype.md) — An identifier for the project type.
- [localizedTitle](localizedtitle.md) — The localized title of the project type as shown to the user.
- [localizedDescription](localizeddescription.md) — The localized description of the project type as shown to the user.
- [localizedAttributedDescription](localizedattributeddescription.md) — The localized attributed description of the project type as shown to the user.
- [image](image.md) — An optional image associated with the project type in the picker.
- [subtypeDescriptions](subtypedescriptions.md) — An array of type descriptions used for subtype descriptions.
