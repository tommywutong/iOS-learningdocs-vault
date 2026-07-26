---
title: PHProjectTypeDescription
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttypedescription
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescription.json'
content_hash: 'sha256:e3d35a3add912932'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectTypeDescription

<sub>Class</sub>

An extensible enumerator for [PHProjectType](phprojecttype.md) that’s presented to users in the project picker.

<sub>macOS</sub>

```swift
class PHProjectTypeDescription
```

## Overview

This object represents one project type choice presented in the project picker when a user is creating a project through project extensions. The [PHProjectTypeDescriptionDataSource](phprojecttypedescriptiondatasource.md) object returns this descriptor from [- typeDescriptionDataSourceForCategory:invalidator:](<phprojectextensioncontroller/typedescriptiondatasource(for_invalidator_).md>).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Project Type Description

- [- initWithProjectType:title:description:image:](<phprojecttypedescription/init(projecttype_title_description_image_).md>) — A convenience initializer without subtype descriptions.
- [- initWithProjectType:title:description:image:subtypeDescriptions:](<phprojecttypedescription/init(projecttype_title_description_image_subtypedescriptions_).md>) — A designated initializer for project type descriptions with the full subtype hierarchy specified up front and a standard string for description text.
- [- initWithProjectType:title:attributedDescription:image:subtypeDescriptions:](<phprojecttypedescription/init(projecttype_title_attributeddescription_image_subtypedescriptions_).md>) — A designated initializer for project type descriptions with the full subtype hierarchy specified up front and an attributed string for description text.
- [- initWithProjectType:title:description:image:canProvideSubtypes:](<phprojecttypedescription/init(projecttype_title_description_image_canprovidesubtypes_).md>) — A designated initializer for project type descriptions with lazily fetched subtypes and a standard description string.
- [- initWithProjectType:title:attributedDescription:image:canProvideSubtypes:](<phprojecttypedescription/init(projecttype_title_attributeddescription_image_canprovidesubtypes_).md>) — A designated initializer for project type descriptions with lazily fetched subtypes and an attributed description string.

### Describing a Project Type

- [projectType](phprojecttypedescription/projecttype.md) — An identifier for the project type.
- [localizedTitle](phprojecttypedescription/localizedtitle.md) — The localized title of the project type as shown to the user.
- [localizedDescription](phprojecttypedescription/localizeddescription.md) — The localized description of the project type as shown to the user.
- [localizedAttributedDescription](phprojecttypedescription/localizedattributeddescription.md) — The localized attributed description of the project type as shown to the user.
- [image](phprojecttypedescription/image.md) — An optional image associated with the project type in the picker.
- [subtypeDescriptions](phprojecttypedescription/subtypedescriptions.md) — An array of type descriptions used for subtype descriptions.
- [canProvideSubtypes](phprojecttypedescription/canprovidesubtypes.md) — A Boolean variable indicating whether subtypes can be fetched from the data source.

### Initializers

- [init(coder:)](<phprojecttypedescription/init(coder_).md>)

## See Also

### Determining Project Type

- [projectType](phprojectinfo/projecttype.md) — The project type that the user selected from the project extension options.
- [PHProjectType](phprojecttype.md) — The type descriptor of a project extension.
- [creationSource](phprojectinfo/creationsource-swift.property.md) — The source from which the project was created.
- [sections](phprojectinfo/sections.md) — An array of project sections, each containing one or more section content objects.
- [PHProjectTypeDescriptionDataSource](phprojecttypedescriptiondatasource.md) — A protocol that you use to provide the project with type description data.
- [PHProjectTypeDescriptionInvalidator](phprojecttypedescriptioninvalidator.md) — A protocol that you use to tell the project when and how to invalidate type and footer text.
- [CreationSource](phprojectinfo/creationsource-swift.enum.md) — Defines the source of a project extension.
