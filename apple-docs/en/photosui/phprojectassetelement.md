---
title: PHProjectAssetElement
framework: PhotosUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojectassetelement
source_url: 'https://developer.apple.com/documentation/photosui/phprojectassetelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojectassetelement.json'
content_hash: 'sha256:c6e224d93ea63514'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHProjectAssetElement

<sub>Class</sub>

An element that represents a media asset within project section content.

<sub>macOS</sub>

```swift
class PHProjectAssetElement
```

## Overview

Access the underlying [PHAsset](../photos/phasset.md) by converting the provided [cloudAssetIdentifiers](phprojectsectioncontent/cloudassetidentifiers.md) to a [assetLocalIdentifier](../photos/phassetresource/assetlocalidentifier.md), then calling [+ fetchAssetsWithLocalIdentifiers:options:](<../photos/phasset/fetchassets(withlocalidentifiers_options_).md>).

## Relationships

- **Inherits From**: [PHProjectElement](phprojectelement.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Characterizing an Asset Element

- [annotation](phprojectassetelement/annotation.md) — A string annotation attached to the asset.
- [cloudAssetIdentifier](phprojectassetelement/cloudassetidentifier.md) — The asset’s identifier in the cloud.
- [cropRect](phprojectassetelement/croprect.md) — A rectangle defining the cropped portion of the asset.
- [regionsOfInterest](phprojectassetelement/regionsofinterest.md) — An array of regions of interest in the photo asset.
- [horizontallyFlipped](phprojectassetelement/horizontallyflipped.md) — A Boolean indicating whether the asset is vertically flipped.
- [verticallyFlipped](phprojectassetelement/verticallyflipped.md) — A Boolean indicating whether the asset is vertically flipped.

## See Also

### Subclassing Project Elements

- [PHProjectTextElement](phprojecttextelement.md) — An element that represents text within project section content.
- [PHProjectJournalEntryElement](phprojectjournalentryelement.md) — An element that represents a journal entry within project section content.
- [PHProjectMapElement](phprojectmapelement.md) — An element that represents a map within project section content.
