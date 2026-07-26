---
title: contentEditingOutput
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetchangerequest/contenteditingoutput
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/contenteditingoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/contenteditingoutput.json'
content_hash: 'sha256:d8cc4ce73ff1dc07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# contentEditingOutput

<sub>Instance Property</sub>

The output of an asset content editing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentEditingOutput: PHContentEditingOutput? { get set }
```

## Discussion

To edit an asset’s image or video content, you must first begin a content editing session with the asset’s [- requestContentEditingInputWithOptions:completionHandler:](<../phasset/requestcontenteditinginput(with_completionhandler_).md>) method. You commit a content edit by setting the [contentEditingOutput](contenteditingoutput.md) property of a change request within a change block. For more information about asset content editing, see [PHAsset](../phasset.md).

## See Also

### Editing Asset Content

- [- revertAssetContentToOriginal](<revertassetcontenttooriginal().md>) — Request to revert any edits made to the asset’s content.
- [- revertAssetContentToOriginalResourceChoice:](<revertassetcontent(to_).md>) — Reverts the asset’s content to its original, choosing which original resource to use as the unadjusted base for all renders. _(beta)_
