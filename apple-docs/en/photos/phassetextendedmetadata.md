---
title: PHAssetExtendedMetadata
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phassetextendedmetadata
source_url: 'https://developer.apple.com/documentation/photos/phassetextendedmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetextendedmetadata.json'
content_hash: 'sha256:88086ba202f2f222'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetExtendedMetadata

<sub>Class</sub>

Represents other asset attributes that are not included when fetching `PHAsset` directly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetExtendedMetadata
```

## Overview

When `PHAsset.extendedMetadata` is called, these properties are fetched. They can be prefetched by toggling `PHFetchOptions.prefetchAssetExtendedMetadata` when fetching `PHAsset`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Reading metadata

- [caption](phassetextendedmetadata/caption.md) — The compact description for this asset. _(beta)_
- [originalFileName](phassetextendedmetadata/originalfilename.md) — The original file name of this asset. _(beta)_
- [keywords](phassetextendedmetadata/keywords.md) — The keywords associated with this asset _(beta)_
