---
title: PHProjectCategory
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectcategory
source_url: 'https://developer.apple.com/documentation/photosui/phprojectcategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectcategory.json'
content_hash: 'sha256:0c113cbb5ad2b636'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectCategory

<sub>Structure</sub>

A representation of Photos project extension categories.

<sub>macOS</sub>

```swift
struct PHProjectCategory
```

## Overview

This structure encapsulates macOS Photos project extension categories. Use this category to designate the types of projects your extension can create, such as books, calendars, cards, and slideshows.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Project Category

- [init(rawValue:)](<phprojectcategory/init(rawvalue_).md>) — Intializes a project category from its raw string value.

### Designating Type Properties

- [PHProjectCategoryBook](phprojectcategory/book.md) — The project category for a printed book.
- [PHProjectCategoryCalendar](phprojectcategory/calendar.md) — The project category for a printed calendar.
- [PHProjectCategoryCard](phprojectcategory/card.md) — The project category for a printed card.
- [PHProjectCategoryPrints](phprojectcategory/prints.md) — The project category for physical prints.
- [PHProjectCategorySlideshow](phprojectcategory/slideshow.md) — The project category for a slideshow.
- [PHProjectCategoryWallDecor](phprojectcategory/walldecor.md) — The project category for wall décor.
- [PHProjectCategoryOther](phprojectcategory/other.md) — The project category for a custom extension type.
- [PHProjectCategoryUndefined](phprojectcategory/undefined.md) — An undefined project category.

## See Also

### macOS Photos Project Extensions

- [Creating a Slideshow Project Extension for Photos](../photokit/creating-a-slideshow-project-extension-for-photos.md) — Augment the macOS Photos app with extensions that support project creation.
- [PHProject](../photos/phproject.md) — A representation of a Photos app project extension.
- [PHProjectInfo](phprojectinfo.md) — Information about the project extension.
- [PHProjectExtensionContext](phprojectextensioncontext.md) — An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
- [PHProjectElement](phprojectelement.md) — The superclass for all element objects.
- [PHProjectSection](phprojectsection.md) — A collection of content representing curated asset and text elements.
- [PHProjectRegionOfInterest](phprojectregionofinterest.md) — A representation of a region of interest in a photo asset.
- [PHProjectChangeRequest](../photos/phprojectchangerequest.md) — A request to change asset data in a Photos project extension.
- [PHProjectExtensionController](phprojectextensioncontroller.md) — A protocol defining the life cycle and supported types of project extensions.
