---
title: PHProjectRegionOfInterest
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectregionofinterest
source_url: 'https://developer.apple.com/documentation/photosui/phprojectregionofinterest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectregionofinterest.json'
content_hash: 'sha256:9410ec1618fe5fa0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectRegionOfInterest

<sub>Class</sub>

A representation of a region of interest in a photo asset.

<sub>macOS</sub>

```swift
class PHProjectRegionOfInterest
```

## Overview

A region of interest defines a rectangular portion of a photo corresponding to a face. Use a region of interest to determine where to focus, zoom, or crop your image in your project extension; for example, you can customize your slideshow’s transitions based on each photo’s highest-quality region of interest, as shown in [Creating a Slideshow Project Extension for Photos](../photokit/creating-a-slideshow-project-extension-for-photos.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Identifying Regions of Interest

- [Identifier](phprojectregionofinterest/identifier-swift.struct.md) — A descriptor identifying a region of interest.

### Determining Region Properties

- [rect](phprojectregionofinterest/rect.md) — The rectangle representing the region’s location.
- [identifier](phprojectregionofinterest/identifier-swift.property.md) — The region’s unique identifier.
- [weight](phprojectregionofinterest/weight.md) — The face region’s weight.
- [quality](phprojectregionofinterest/quality.md) — The region’s quality.

### Initializers

- [init(coder:)](<phprojectregionofinterest/init(coder_).md>)

## See Also

### macOS Photos Project Extensions

- [Creating a Slideshow Project Extension for Photos](../photokit/creating-a-slideshow-project-extension-for-photos.md) — Augment the macOS Photos app with extensions that support project creation.
- [PHProject](../photos/phproject.md) — A representation of a Photos app project extension.
- [PHProjectInfo](phprojectinfo.md) — Information about the project extension.
- [PHProjectExtensionContext](phprojectextensioncontext.md) — An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
- [PHProjectElement](phprojectelement.md) — The superclass for all element objects.
- [PHProjectSection](phprojectsection.md) — A collection of content representing curated asset and text elements.
- [PHProjectChangeRequest](../photos/phprojectchangerequest.md) — A request to change asset data in a Photos project extension.
- [PHProjectExtensionController](phprojectextensioncontroller.md) — A protocol defining the life cycle and supported types of project extensions.
- [PHProjectCategory](phprojectcategory.md) — A representation of Photos project extension categories.
