---
title: projectType
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttypedescription/projecttype
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescription/projecttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescription/projecttype.json'
content_hash: 'sha256:13c6826c92b2501e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescription](../phprojecttypedescription.md)

# projectType

<sub>Instance Property</sub>

An identifier for the project type.

<sub>macOS</sub>

```swift
var projectType: PHProjectType { get }
```

## Discussion

Add these identifiers to [PHProjectType](../phprojecttype.md), the extensible string enumeration.

## See Also

### Describing a Project Type

- [localizedTitle](localizedtitle.md) — The localized title of the project type as shown to the user.
- [localizedDescription](localizeddescription.md) — The localized description of the project type as shown to the user.
- [localizedAttributedDescription](localizedattributeddescription.md) — The localized attributed description of the project type as shown to the user.
- [image](image.md) — An optional image associated with the project type in the picker.
- [subtypeDescriptions](subtypedescriptions.md) — An array of type descriptions used for subtype descriptions.
- [canProvideSubtypes](canprovidesubtypes.md) — A Boolean variable indicating whether subtypes can be fetched from the data source.
