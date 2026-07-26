---
title: PHProjectElement
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectelement
source_url: 'https://developer.apple.com/documentation/photosui/phprojectelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectelement.json'
content_hash: 'sha256:5c8ecd31b617034a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectElement

<sub>Class</sub>

The superclass for all element objects.

<sub>macOS</sub>

```swift
class PHProjectElement
```

## Overview

You should never use this class directly; opt instead for one of its subclasses. It defines the shared properties of any element in an instance of [PHProjectSectionContent](phprojectsectioncontent.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [PHProjectAssetElement](phprojectassetelement.md), [PHProjectJournalEntryElement](phprojectjournalentryelement.md), [PHProjectMapElement](phprojectmapelement.md), [PHProjectTextElement](phprojecttextelement.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Subclassing Project Elements

- [PHProjectAssetElement](phprojectassetelement.md) — An element that represents a media asset within project section content.
- [PHProjectTextElement](phprojecttextelement.md) — An element that represents text within project section content.
- [PHProjectJournalEntryElement](phprojectjournalentryelement.md) — An element that represents a journal entry within project section content.
- [PHProjectMapElement](phprojectmapelement.md) — An element that represents a map within project section content.

### Describing Project Elements

- [weight](phprojectelement/weight.md) — A value between 0 and 1 representing relative significance of the element in its section.
- [placement](phprojectelement/placement.md) — A rectangle defining where an element is placed in grid space coordinates.

### Initializers

- [init(coder:)](<phprojectelement/init(coder_).md>)

## See Also

### macOS Photos Project Extensions

- [Creating a Slideshow Project Extension for Photos](../photokit/creating-a-slideshow-project-extension-for-photos.md) — Augment the macOS Photos app with extensions that support project creation.
- [PHProject](../photos/phproject.md) — A representation of a Photos app project extension.
- [PHProjectInfo](phprojectinfo.md) — Information about the project extension.
- [PHProjectExtensionContext](phprojectextensioncontext.md) — An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
- [PHProjectSection](phprojectsection.md) — A collection of content representing curated asset and text elements.
- [PHProjectRegionOfInterest](phprojectregionofinterest.md) — A representation of a region of interest in a photo asset.
- [PHProjectChangeRequest](../photos/phprojectchangerequest.md) — A request to change asset data in a Photos project extension.
- [PHProjectExtensionController](phprojectextensioncontroller.md) — A protocol defining the life cycle and supported types of project extensions.
- [PHProjectCategory](phprojectcategory.md) — A representation of Photos project extension categories.
