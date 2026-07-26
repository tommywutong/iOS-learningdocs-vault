---
title: PHProjectSectionContent
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectsectioncontent
source_url: 'https://developer.apple.com/documentation/photosui/phprojectsectioncontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectsectioncontent.json'
content_hash: 'sha256:95051849a84b040c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectSectionContent

<sub>Class</sub>

An object containing section elements and layout information for a single level of curation.

<sub>macOS</sub>

```swift
class PHProjectSectionContent
```

## Overview

A section content object contains suggested layout information for every element at a specific level of curation within a [PHProjectSection](phprojectsection.md). A single section can provide multiple content objects, but only one is used at a time, depending on the level of curation and the amount of content detail.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Determining Content Properties

- [elements](phprojectsectioncontent/elements.md) — An array of asset, text, or journal entry elements contained in the content.
- [numberOfColumns](phprojectsectioncontent/numberofcolumns.md) — The number of columns if section content is displayed in a grid layout.
- [aspectRatio](phprojectsectioncontent/aspectratio.md) — The aspect ratio of the full content layout, defined as width over height.
- [cloudAssetIdentifiers](phprojectsectioncontent/cloudassetidentifiers.md) — An array containing all cloud asset identifiers referenced in the content.
- [backgroundColor](phprojectsectioncontent/backgroundcolor.md) — The background color of the section content when created from an Apple Print Product.

### Initializers

- [init(coder:)](<phprojectsectioncontent/init(coder_).md>)

## See Also

### Determining Section Contents

- [title](phprojectsection/title.md) — The optional section title.
- [sectionContents](phprojectsection/sectioncontents.md) — An array containing PHProjectionSessionContent objects.
