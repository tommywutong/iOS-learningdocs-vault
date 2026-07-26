---
title: 'init(projectType:title:description:image:)'
framework: PhotosUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phprojecttypedescription/init(projecttype:title:description:image:)'
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescription/init(projecttype:title:description:image:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescription/init%28projecttype%3Atitle%3Adescription%3Aimage%3A%29.json'
content_hash: 'sha256:f9d1f31b2da27eef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescription](../phprojecttypedescription.md)

# init(projectType:title:description:image:)

<sub>Initializer</sub>

A convenience initializer without subtype descriptions.

<sub>macOS</sub>

```swift
convenience init(projectType: PHProjectType, title localizedTitle: String, description localizedDescription: String?, image: NSImage?)
```

## Parameters

- `projectType` — The type of project being described.

- `localizedTitle` — The localized title of the project type.

- `localizedDescription` — The localized attributed description of the project type.

- `image` — The image associated with the project type in the picker.

## See Also

### Creating a Project Type Description

- [- initWithProjectType:title:description:image:subtypeDescriptions:](<init(projecttype_title_description_image_subtypedescriptions_).md>) — A designated initializer for project type descriptions with the full subtype hierarchy specified up front and a standard string for description text.
- [- initWithProjectType:title:attributedDescription:image:subtypeDescriptions:](<init(projecttype_title_attributeddescription_image_subtypedescriptions_).md>) — A designated initializer for project type descriptions with the full subtype hierarchy specified up front and an attributed string for description text.
- [- initWithProjectType:title:description:image:canProvideSubtypes:](<init(projecttype_title_description_image_canprovidesubtypes_).md>) — A designated initializer for project type descriptions with lazily fetched subtypes and a standard description string.
- [- initWithProjectType:title:attributedDescription:image:canProvideSubtypes:](<init(projecttype_title_attributeddescription_image_canprovidesubtypes_).md>) — A designated initializer for project type descriptions with lazily fetched subtypes and an attributed description string.
