---
title: PHProjectSection
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectsection
source_url: 'https://developer.apple.com/documentation/photosui/phprojectsection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectsection.json'
content_hash: 'sha256:97b52c2029260b23'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectSection

<sub>Class</sub>

A collection of content representing curated asset and text elements.

<sub>macOS</sub>

```swift
class PHProjectSection
```

## Overview

Each project section contains at least one [PHProjectSectionContent](phprojectsectioncontent.md) object, which represents a suggested curation of the content. The number of sections included in [PHProjectInfo](phprojectinfo.md) varies depending on the source used to initialize the project:

- **A Memory.** There will be one cover section with a key asset element and title, as well as a section containing multiple levels of curation, mirroring the Show Summary and Show More options of the Memory in Photos.
- **A single Album.** The number of sections depends on the Album size. A small Album yields a single section, but an Album with a large quantity of photos is broken down into sections based on Moments in the user’s Photo Library.
- **An existing Apple Book, Card, or Calendar.** The sections will match the pagination in that project; for example, a book will break down into one section per page.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Determining Section Contents

- [title](phprojectsection/title.md) — The optional section title.
- [sectionContents](phprojectsection/sectioncontents.md) — An array containing PHProjectionSessionContent objects.
- [PHProjectSectionContent](phprojectsectioncontent.md) — An object containing section elements and layout information for a single level of curation.

### Defining the Section Type

- [sectionType](phprojectsection/sectiontype-swift.property.md) — The intended usage of the section: cover, content, or auxiliary.
- [SectionType](phprojectsection/sectiontype-swift.enum.md) — The intended usage of the section: cover, content, or auxiliary.

### Initializers

- [init(coder:)](<phprojectsection/init(coder_).md>)

## See Also

### macOS Photos Project Extensions

- [Creating a Slideshow Project Extension for Photos](../photokit/creating-a-slideshow-project-extension-for-photos.md) — Augment the macOS Photos app with extensions that support project creation.
- [PHProject](../photos/phproject.md) — A representation of a Photos app project extension.
- [PHProjectInfo](phprojectinfo.md) — Information about the project extension.
- [PHProjectExtensionContext](phprojectextensioncontext.md) — An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
- [PHProjectElement](phprojectelement.md) — The superclass for all element objects.
- [PHProjectRegionOfInterest](phprojectregionofinterest.md) — A representation of a region of interest in a photo asset.
- [PHProjectChangeRequest](../photos/phprojectchangerequest.md) — A request to change asset data in a Photos project extension.
- [PHProjectExtensionController](phprojectextensioncontroller.md) — A protocol defining the life cycle and supported types of project extensions.
- [PHProjectCategory](phprojectcategory.md) — A representation of Photos project extension categories.
