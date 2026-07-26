---
title: PHAssetBurstSelectionType
framework: Photos
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetburstselectiontype
source_url: 'https://developer.apple.com/documentation/photos/phassetburstselectiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetburstselectiontype.json'
content_hash: 'sha256:9af510f3aa6a067c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetBurstSelectionType

<sub>Structure</sub>

Bit mask values indicating whether and how an asset is marked as a favorite member of a burst photo sequence. Used by the [burstSelectionTypes](phasset/burstselectiontypes.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct PHAssetBurstSelectionType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<phassetburstselectiontype/init(rawvalue_).md>) — Creates an asset burst selection type from a raw value.

### Constants

- [PHAssetBurstSelectionTypeAutoPick](phassetburstselectiontype/autopick.md) — Photos has automatically identified the asset as a potential user favorite.
- [PHAssetBurstSelectionTypeUserPick](phassetburstselectiontype/userpick.md) — The user has marked the asset as a favorite member of its burst sequence.

## See Also

### Working with Burst Photo Assets

- [burstIdentifier](phasset/burstidentifier.md) — The unique identifier shared by photo assets from the same burst sequence.
- [burstSelectionTypes](phasset/burstselectiontypes.md) — The selection type of the asset in a burst photo sequence.
- [representsBurst](phasset/representsburst.md) — A Boolean value that indicates whether the asset is the representative photo from a burst photo sequence.
