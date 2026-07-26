---
title: subtypeDescriptions
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttypedescription/subtypedescriptions
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescription/subtypedescriptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescription/subtypedescriptions.json'
content_hash: 'sha256:e989f995e19724af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescription](../phprojecttypedescription.md)

# subtypeDescriptions

<sub>Instance Property</sub>

An array of type descriptions used for subtype descriptions.

<sub>macOS</sub>

```swift
var subtypeDescriptions: [PHProjectTypeDescription] { get }
```

## Discussion

This array may be empty.

## See Also

### Describing a Project Type

- [projectType](projecttype.md) — An identifier for the project type.
- [localizedTitle](localizedtitle.md) — The localized title of the project type as shown to the user.
- [localizedDescription](localizeddescription.md) — The localized description of the project type as shown to the user.
- [localizedAttributedDescription](localizedattributeddescription.md) — The localized attributed description of the project type as shown to the user.
- [image](image.md) — An optional image associated with the project type in the picker.
- [canProvideSubtypes](canprovidesubtypes.md) — A Boolean variable indicating whether subtypes can be fetched from the data source.
