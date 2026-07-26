---
title: localizedAttributedDescription
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttypedescription/localizedattributeddescription
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescription/localizedattributeddescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescription/localizedattributeddescription.json'
content_hash: 'sha256:c1592055d9c2864f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescription](../phprojecttypedescription.md)

# localizedAttributedDescription

<sub>Instance Property</sub>

The localized attributed description of the project type as shown to the user.

<sub>macOS</sub>

```swift
@NSCopying var localizedAttributedDescription: NSAttributedString? { get }
```

## Discussion

The attributed description is optional. If you don’t provide one, it defaults to the standard nonattributed description.

## See Also

### Describing a Project Type

- [projectType](projecttype.md) — An identifier for the project type.
- [localizedTitle](localizedtitle.md) — The localized title of the project type as shown to the user.
- [localizedDescription](localizeddescription.md) — The localized description of the project type as shown to the user.
- [image](image.md) — An optional image associated with the project type in the picker.
- [subtypeDescriptions](subtypedescriptions.md) — An array of type descriptions used for subtype descriptions.
- [canProvideSubtypes](canprovidesubtypes.md) — A Boolean variable indicating whether subtypes can be fetched from the data source.
