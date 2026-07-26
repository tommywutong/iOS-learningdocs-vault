---
title: 'init(projectType:title:description:image:canProvideSubtypes:)'
framework: PhotosUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojecttypedescription/init(projecttype:title:description:image:canprovidesubtypes:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescription/init(projecttype:title:description:image:canprovidesubtypes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescription/init%28projecttype%3Atitle%3Adescription%3Aimage%3Acanprovidesubtypes%3A%29.json'
content_hash: 'sha256:512ec59a7efd8936'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescription](../phprojecttypedescription.md)

# init(projectType:title:description:image:canProvideSubtypes:)

<sub>Initializer</sub>

A designated initializer for project type descriptions with lazily fetched subtypes and a standard description string.

<sub>macOS</sub>

```swift
init(projectType: PHProjectType, title localizedTitle: String, description localizedDescription: String?, image: NSImage?, canProvideSubtypes: Bool)
```

## Parameters

- `projectType` — The type of project being described.

- `localizedTitle` — The localized title of the project type.

- `localizedDescription` — The localized description of the project type.

- `image` — The image associated with the project type in the picker.

- `canProvideSubtypes` — A Boolean variable indicating whether subtypes can be fetched from the data source.

## See Also

### Creating a Project Type Description

- [- initWithProjectType:title:description:image:](<init(projecttype_title_description_image_).md>) — A convenience initializer without subtype descriptions.
- [- initWithProjectType:title:description:image:subtypeDescriptions:](<init(projecttype_title_description_image_subtypedescriptions_).md>) — A designated initializer for project type descriptions with the full subtype hierarchy specified up front and a standard string for description text.
- [- initWithProjectType:title:attributedDescription:image:subtypeDescriptions:](<init(projecttype_title_attributeddescription_image_subtypedescriptions_).md>) — A designated initializer for project type descriptions with the full subtype hierarchy specified up front and an attributed string for description text.
- [- initWithProjectType:title:attributedDescription:image:canProvideSubtypes:](<init(projecttype_title_attributeddescription_image_canprovidesubtypes_).md>) — A designated initializer for project type descriptions with lazily fetched subtypes and an attributed description string.
