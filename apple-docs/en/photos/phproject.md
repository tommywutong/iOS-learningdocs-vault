---
title: PHProject
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phproject
source_url: 'https://developer.apple.com/documentation/photos/phproject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phproject.json'
content_hash: 'sha256:43a5f9dac42f7d30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHProject

<sub>Class</sub>

A representation of a Photos app project extension.

<sub>macOS</sub>

```swift
class PHProject
```

## Overview

This class represents the project when extended from macOS Photos. Projects can have the following types:

- Book
- Calendar
- Card
- Prints
- Slideshow
- Wall decor

Users create projects by selecting one or more assets, right-clicking the selection, and grouping the assets, much like an album collection. Your app treats the project as a separate entity, represented as a [PHProject](phproject.md).

## Relationships

- **Inherits From**: [PHAssetCollection](phassetcollection.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Project Extension Properties

- [hasProjectPreview](phproject/hasprojectpreview.md) — A property that indicates whether a project preview was previously set.
- [projectExtensionData](phproject/projectextensiondata.md) — Data associated with the project extension.

## See Also

### Classes

- [PHProjectChangeRequest](phprojectchangerequest.md) — A request to change asset data in a Photos project extension.
