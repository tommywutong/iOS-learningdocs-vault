---
title: sections
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectinfo/sections
source_url: 'https://developer.apple.com/documentation/photosui/phprojectinfo/sections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectinfo/sections.json'
content_hash: 'sha256:30d48e4979f35a64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectInfo](../phprojectinfo.md)

# sections

<sub>Instance Property</sub>

An array of project sections, each containing one or more section content objects.

<sub>macOS</sub>

```swift
var sections: [PHProjectSection] { get }
```

## See Also

### Determining Project Type

- [projectType](projecttype.md) — The project type that the user selected from the project extension options.
- [PHProjectType](../phprojecttype.md) — The type descriptor of a project extension.
- [creationSource](creationsource-swift.property.md) — The source from which the project was created.
- [PHProjectTypeDescription](../phprojecttypedescription.md) — An extensible enumerator for [PHProjectType](../phprojecttype.md) that’s presented to users in the project picker.
- [PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md) — A protocol that you use to provide the project with type description data.
- [PHProjectTypeDescriptionInvalidator](../phprojecttypedescriptioninvalidator.md) — A protocol that you use to tell the project when and how to invalidate type and footer text.
- [CreationSource](creationsource-swift.enum.md) — Defines the source of a project extension.
