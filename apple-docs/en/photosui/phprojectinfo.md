---
title: PHProjectInfo
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectinfo
source_url: 'https://developer.apple.com/documentation/photosui/phprojectinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectinfo.json'
content_hash: 'sha256:0b04de3cabc1b0d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectInfo

<sub>Class</sub>

Information about the project extension.

<sub>macOS</sub>

```swift
class PHProjectInfo
```

## Overview

macOS Photos automatically generates a [PHProjectInfo](phprojectinfo.md) object when creating a new project. Photos passes along the project information with a [PHProjectExtensionContext](phprojectextensioncontext.md) object. This object contains metadata about the project’s creation source, sections, product type, branding, and page numbers. Your extension leverages project information to influence project layout, autoflow, and theme selection. The properties of this class are immutable, and your extension can’t instantiate the object directly.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Determining Project Type

- [projectType](phprojectinfo/projecttype.md) — The project type that the user selected from the project extension options.
- [PHProjectType](phprojecttype.md) — The type descriptor of a project extension.
- [creationSource](phprojectinfo/creationsource-swift.property.md) — The source from which the project was created.
- [sections](phprojectinfo/sections.md) — An array of project sections, each containing one or more section content objects.
- [PHProjectTypeDescription](phprojecttypedescription.md) — An extensible enumerator for [PHProjectType](phprojecttype.md) that’s presented to users in the project picker.
- [PHProjectTypeDescriptionDataSource](phprojecttypedescriptiondatasource.md) — A protocol that you use to provide the project with type description data.
- [PHProjectTypeDescriptionInvalidator](phprojecttypedescriptioninvalidator.md) — A protocol that you use to tell the project when and how to invalidate type and footer text.
- [CreationSource](phprojectinfo/creationsource-swift.enum.md) — Defines the source of a project extension.

### Creating a Project from an Apple Print Product

- [brandingEnabled](phprojectinfo/brandingenabled.md) — A Boolean value indicating whether branding was enabled in the source project.
- [pageNumbersEnabled](phprojectinfo/pagenumbersenabled.md) — A Boolean value indicating whether page numbering was enabled in the source project.
- [productIdentifier](phprojectinfo/productidentifier.md) — The product identifier of the originating Apple Print Product.
- [themeIdentifier](phprojectinfo/themeidentifier.md) — The product theme identifier of the originating Apple Print Product.

### Initializers

- [init(coder:)](<phprojectinfo/init(coder_).md>)

## See Also

### macOS Photos Project Extensions

- [Creating a Slideshow Project Extension for Photos](../photokit/creating-a-slideshow-project-extension-for-photos.md) — Augment the macOS Photos app with extensions that support project creation.
- [PHProject](../photos/phproject.md) — A representation of a Photos app project extension.
- [PHProjectExtensionContext](phprojectextensioncontext.md) — An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
- [PHProjectElement](phprojectelement.md) — The superclass for all element objects.
- [PHProjectSection](phprojectsection.md) — A collection of content representing curated asset and text elements.
- [PHProjectRegionOfInterest](phprojectregionofinterest.md) — A representation of a region of interest in a photo asset.
- [PHProjectChangeRequest](../photos/phprojectchangerequest.md) — A request to change asset data in a Photos project extension.
- [PHProjectExtensionController](phprojectextensioncontroller.md) — A protocol defining the life cycle and supported types of project extensions.
- [PHProjectCategory](phprojectcategory.md) — A representation of Photos project extension categories.
