---
title: PHProjectTypeDescriptionDataSource
framework: PhotosUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttypedescriptiondatasource
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescriptiondatasource.json'
content_hash: 'sha256:02a19aae3d8b21b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectTypeDescriptionDataSource

<sub>Protocol</sub>

A protocol that you use to provide the project with type description data.

<sub>macOS</sub>

```swift
protocol PHProjectTypeDescriptionDataSource : NSObjectProtocol
```

## Overview

An object adheres to this protocol to provide a type description for your app’s Photos project extension. You must implement this protocol to provide subtypes, a description, and footer text. You can optionally respond to the system discarding the data source by implementing [- extensionWillDiscardDataSource](<phprojecttypedescriptiondatasource/extensionwilldiscarddatasource().md>).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing Required Fields

- [- subtypesForProjectType:](<phprojecttypedescriptiondatasource/subtypes(for_).md>) — Provides the root-level project type descriptions and descriptions of any promised subtypes with [canProvideSubtypes](phprojecttypedescription/canprovidesubtypes.md) set to `true`.
- [- typeDescriptionForProjectType:](<phprojecttypedescriptiondatasource/typedescription(for_).md>) — Provides the updated project type description for previously invalidated project types.
- [- footerTextForSubtypesOfProjectType:](<phprojecttypedescriptiondatasource/footertext(forsubtypesof_).md>) — Provides the footer text for the subtypes of the given project type.

### Responding to Removal

- [- extensionWillDiscardDataSource](<phprojecttypedescriptiondatasource/extensionwilldiscarddatasource().md>) — Provides an opportunity to use the data source before it’s released.

## See Also

### Determining Project Type

- [projectType](phprojectinfo/projecttype.md) — The project type that the user selected from the project extension options.
- [PHProjectType](phprojecttype.md) — The type descriptor of a project extension.
- [creationSource](phprojectinfo/creationsource-swift.property.md) — The source from which the project was created.
- [sections](phprojectinfo/sections.md) — An array of project sections, each containing one or more section content objects.
- [PHProjectTypeDescription](phprojecttypedescription.md) — An extensible enumerator for [PHProjectType](phprojecttype.md) that’s presented to users in the project picker.
- [PHProjectTypeDescriptionInvalidator](phprojecttypedescriptioninvalidator.md) — A protocol that you use to tell the project when and how to invalidate type and footer text.
- [CreationSource](phprojectinfo/creationsource-swift.enum.md) — Defines the source of a project extension.
