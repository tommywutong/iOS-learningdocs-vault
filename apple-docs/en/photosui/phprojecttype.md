---
title: PHProjectType
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttype
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttype.json'
content_hash: 'sha256:103783e792b30718'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectType

<sub>Structure</sub>

The type descriptor of a project extension.

<sub>macOS</sub>

```swift
struct PHProjectType
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a Project Type

- [init(_:)](<phprojecttype/init(__).md>) — Initializes a project type from a string.
- [init(rawValue:)](<phprojecttype/init(rawvalue_).md>) — Initializes a project type from its raw string value.

### Defining a Project Type

- [PHProjectTypeUndefined](phprojecttype/undefined.md) — An undefined project type.

## See Also

### Determining Project Type

- [projectType](phprojectinfo/projecttype.md) — The project type that the user selected from the project extension options.
- [creationSource](phprojectinfo/creationsource-swift.property.md) — The source from which the project was created.
- [sections](phprojectinfo/sections.md) — An array of project sections, each containing one or more section content objects.
- [PHProjectTypeDescription](phprojecttypedescription.md) — An extensible enumerator for [PHProjectType](phprojecttype.md) that’s presented to users in the project picker.
- [PHProjectTypeDescriptionDataSource](phprojecttypedescriptiondatasource.md) — A protocol that you use to provide the project with type description data.
- [PHProjectTypeDescriptionInvalidator](phprojecttypedescriptioninvalidator.md) — A protocol that you use to tell the project when and how to invalidate type and footer text.
- [CreationSource](phprojectinfo/creationsource-swift.enum.md) — Defines the source of a project extension.
