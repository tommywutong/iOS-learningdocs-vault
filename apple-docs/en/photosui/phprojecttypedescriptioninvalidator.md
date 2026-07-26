---
title: PHProjectTypeDescriptionInvalidator
framework: PhotosUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttypedescriptioninvalidator
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescriptioninvalidator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescriptioninvalidator.json'
content_hash: 'sha256:752a3af1101c7ca7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectTypeDescriptionInvalidator

<sub>Protocol</sub>

A protocol that you use to tell the project when and how to invalidate type and footer text.

<sub>macOS</sub>

```swift
protocol PHProjectTypeDescriptionInvalidator : NSObjectProtocol
```

## Overview

An object adheres to this protocol to implement custom behavior when you invalidate project information, such as type description and footer text.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Invalidating a Project Type

- [- invalidateTypeDescriptionForProjectType:](<phprojecttypedescriptioninvalidator/invalidatetypedescription(for_).md>) — Invalidates the type description for the given project type.
- [- invalidateFooterTextForSubtypesOfProjectType:](<phprojecttypedescriptioninvalidator/invalidatefootertext(forsubtypesof_).md>) — Invalidates the footer text for the subtypes of the given project type.

## See Also

### Determining Project Type

- [projectType](phprojectinfo/projecttype.md) — The project type that the user selected from the project extension options.
- [PHProjectType](phprojecttype.md) — The type descriptor of a project extension.
- [creationSource](phprojectinfo/creationsource-swift.property.md) — The source from which the project was created.
- [sections](phprojectinfo/sections.md) — An array of project sections, each containing one or more section content objects.
- [PHProjectTypeDescription](phprojecttypedescription.md) — An extensible enumerator for [PHProjectType](phprojecttype.md) that’s presented to users in the project picker.
- [PHProjectTypeDescriptionDataSource](phprojecttypedescriptiondatasource.md) — A protocol that you use to provide the project with type description data.
- [CreationSource](phprojectinfo/creationsource-swift.enum.md) — Defines the source of a project extension.
