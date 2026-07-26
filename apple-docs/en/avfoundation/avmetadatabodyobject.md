---
title: AVMetadataBodyObject
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatabodyobject
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatabodyobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatabodyobject.json'
content_hash: 'sha256:e13ad3a29c593859'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataBodyObject

<sub>Class</sub>

An abstract class that defines the interface for a metadata body object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVMetadataBodyObject
```

## Overview

A metadata body object represents a single detected body in a picture. It’s the base object used to represent bodies, for example [AVMetadataHumanBodyObject](avmetadatahumanbodyobject.md), [AVMetadataDogBodyObject](avmetadatadogbodyobject.md), and [AVMetadataCatBodyObject](avmetadatacatbodyobject.md).

## Relationships

- **Inherits From**: [AVMetadataObject](avmetadataobject.md)

- **Inherited By**: [AVMetadataCatBodyObject](avmetadatacatbodyobject.md), [AVMetadataDogBodyObject](avmetadatadogbodyobject.md), [AVMetadataHumanBodyObject](avmetadatahumanbodyobject.md), [AVMetadataHumanFullBodyObject](avmetadatahumanfullbodyobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting metadata

- [bodyID](avmetadatabodyobject/bodyid.md) — An integer value that defines the unique identifier of an object in a picture.

## See Also

### Bodies

- [AVMetadataCatBodyObject](avmetadatacatbodyobject.md) — An object representing a single detected cat body in a picture.
- [AVMetadataDogBodyObject](avmetadatadogbodyobject.md) — An object representing a single detected dog body in a picture.
- [AVMetadataHumanBodyObject](avmetadatahumanbodyobject.md) — An object representing a single detected human body in a picture.
- [AVMetadataHumanFullBodyObject](avmetadatahumanfullbodyobject.md) — An object that represents a detected human full body in a picture.
