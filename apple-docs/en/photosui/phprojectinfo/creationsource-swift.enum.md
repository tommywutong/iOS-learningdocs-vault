---
title: PHProjectInfo.CreationSource
framework: PhotosUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectinfo/creationsource-swift.enum
source_url: 'https://developer.apple.com/documentation/photosui/phprojectinfo/creationsource-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectinfo/creationsource-swift.enum.json'
content_hash: 'sha256:439927637cd9db0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectInfo](../phprojectinfo.md)

# PHProjectInfo.CreationSource

<sub>Enumeration</sub>

Defines the source of a project extension.

<sub>macOS</sub>

```swift
enum CreationSource
```

## Overview

Each source represents a file type from which users can create a project extension.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Project Sources

- [PHProjectCreationSourceUndefined](creationsource-swift.enum/undefined.md) — An undefined project extension.
- [PHProjectCreationSourceUserSelection](creationsource-swift.enum/userselection.md) — A project extension created from a user selection of photos.
- [PHProjectCreationSourceAlbum](creationsource-swift.enum/album.md) — A project extension created from a photo album.
- [PHProjectCreationSourceMemory](creationsource-swift.enum/memory.md) — A project extension created from a memory.
- [PHProjectCreationSourceMoment](creationsource-swift.enum/moment.md) — A project extension created from a moment.
- [PHProjectCreationSourceProject](creationsource-swift.enum/project.md) — A project extension created from an existing Photos project.
- [PHProjectCreationSourceProjectBook](creationsource-swift.enum/projectbook.md) — A project extension created from a Photos project book.
- [PHProjectCreationSourceProjectCalendar](creationsource-swift.enum/projectcalendar.md) — A project extension created from a calendar.
- [PHProjectCreationSourceProjectCard](creationsource-swift.enum/projectcard.md) — A project extension created from a card.
- [PHProjectCreationSourceProjectPrintOrder](creationsource-swift.enum/projectprintorder.md) — A project extension created from a print order.
- [PHProjectCreationSourceProjectSlideshow](creationsource-swift.enum/projectslideshow.md) — A project slideshow extension.
- [PHProjectCreationSourceProjectExtension](creationsource-swift.enum/projectextension.md) — A project extension created from another project extension.

### Initializers

- [init(rawValue:)](<creationsource-swift.enum/init(rawvalue_).md>)

## See Also

### Determining Project Type

- [projectType](projecttype.md) — The project type that the user selected from the project extension options.
- [PHProjectType](../phprojecttype.md) — The type descriptor of a project extension.
- [creationSource](creationsource-swift.property.md) — The source from which the project was created.
- [sections](sections.md) — An array of project sections, each containing one or more section content objects.
- [PHProjectTypeDescription](../phprojecttypedescription.md) — An extensible enumerator for [PHProjectType](../phprojecttype.md) that’s presented to users in the project picker.
- [PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md) — A protocol that you use to provide the project with type description data.
- [PHProjectTypeDescriptionInvalidator](../phprojecttypedescriptioninvalidator.md) — A protocol that you use to tell the project when and how to invalidate type and footer text.
