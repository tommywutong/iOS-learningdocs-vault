---
title: PHProjectExtensionContext
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectextensioncontext
source_url: 'https://developer.apple.com/documentation/photosui/phprojectextensioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectextensioncontext.json'
content_hash: 'sha256:31be996941b35ec8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectExtensionContext

<sub>Class</sub>

An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.

<sub>macOS</sub>

```swift
class PHProjectExtensionContext
```

## Overview

When a Photos project extension is initialized, it is handed an extension context object. This object provides the extension with access to the underlying project, as well as the photo library from which assets are fetched and edited.

## Relationships

- **Inherits From**: [NSExtensionContext](../foundation/nsextensioncontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Project and the Photo Library

- [project](phprojectextensioncontext/project.md) — A read-only version of the project being edited.
- [photoLibrary](phprojectextensioncontext/photolibrary.md) — A read-only version of the photo library being modified.

### Updating Assets

- [- showEditorForAsset:](<phprojectextensioncontext/showeditor(for_).md>) — Invokes the built-in photo editor for the given asset.
- [- updatedProjectInfoFromProjectInfo:completion:](<phprojectextensioncontext/updatedprojectinfo(from_completion_).md>) — Creates an updated [PHProjectInfo](phprojectinfo.md) instance from existing project information and current assets.

## See Also

### macOS Photos Project Extensions

- [Creating a Slideshow Project Extension for Photos](../photokit/creating-a-slideshow-project-extension-for-photos.md) — Augment the macOS Photos app with extensions that support project creation.
- [PHProject](../photos/phproject.md) — A representation of a Photos app project extension.
- [PHProjectInfo](phprojectinfo.md) — Information about the project extension.
- [PHProjectElement](phprojectelement.md) — The superclass for all element objects.
- [PHProjectSection](phprojectsection.md) — A collection of content representing curated asset and text elements.
- [PHProjectRegionOfInterest](phprojectregionofinterest.md) — A representation of a region of interest in a photo asset.
- [PHProjectChangeRequest](../photos/phprojectchangerequest.md) — A request to change asset data in a Photos project extension.
- [PHProjectExtensionController](phprojectextensioncontroller.md) — A protocol defining the life cycle and supported types of project extensions.
- [PHProjectCategory](phprojectcategory.md) — A representation of Photos project extension categories.
