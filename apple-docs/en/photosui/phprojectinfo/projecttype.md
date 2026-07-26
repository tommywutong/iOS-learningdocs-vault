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
doc_path: /documentation/photosui/phprojectinfo/projecttype
source_url: 'https://developer.apple.com/documentation/photosui/phprojectinfo/projecttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectinfo/projecttype.json'
content_hash: 'sha256:093112d4bc62e980'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectInfo](../phprojectinfo.md)

# projectType

<sub>Instance Property</sub>

The project type that the user selected from the project extension options.

<sub>macOS</sub>

```swift
var projectType: PHProjectType { get }
```

## Discussion

See the [PHProjectExtensionController](../phprojectextensioncontroller.md) protocol for more information on configuring the options.

## See Also

### Determining Project Type

- [PHProjectType](../phprojecttype.md) — The type descriptor of a project extension.
- [creationSource](creationsource-swift.property.md) — The source from which the project was created.
- [sections](sections.md) — An array of project sections, each containing one or more section content objects.
- [PHProjectTypeDescription](../phprojecttypedescription.md) — An extensible enumerator for [PHProjectType](../phprojecttype.md) that’s presented to users in the project picker.
- [PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md) — A protocol that you use to provide the project with type description data.
- [PHProjectTypeDescriptionInvalidator](../phprojecttypedescriptioninvalidator.md) — A protocol that you use to tell the project when and how to invalidate type and footer text.
- [CreationSource](creationsource-swift.enum.md) — Defines the source of a project extension.
