---
title: 'revertAssetContent(to:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photos/phassetchangerequest/revertassetcontent(to:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/revertassetcontent(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/revertassetcontent%28to%3A%29.json'
content_hash: 'sha256:b379f47ddfa2cb5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# revertAssetContent(to:)

<sub>Instance Method</sub>

Reverts the asset’s content to its original, choosing which original resource to use as the unadjusted base for all renders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func revertAssetContent(to choice: PHAsset.OriginalResourceChoice)
```

## Parameters

- `choice` — The original resource to use as the unadjusted base after reverting.

## Discussion

In addition to reverting all adjustments, this selects either the RAW ([PHOriginalResourceChoiceRaw](../phasset/originalresourcechoice-swift.enum/raw.md)) or the compressed ([PHOriginalResourceChoiceCompressed](../phasset/originalresourcechoice-swift.enum/compressed.md)) resource as the source for all renders. This applies to RAW+JPEG assets only. Using this with other types of assets is not supported.

## See Also

### Editing Asset Content

- [contentEditingOutput](contenteditingoutput.md) — The output of an asset content editing session.
- [- revertAssetContentToOriginal](<revertassetcontenttooriginal().md>) — Request to revert any edits made to the asset’s content.
