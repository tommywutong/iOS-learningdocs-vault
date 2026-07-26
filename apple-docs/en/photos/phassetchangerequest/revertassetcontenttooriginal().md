---
title: revertAssetContentToOriginal()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetchangerequest/revertassetcontenttooriginal()
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/revertassetcontenttooriginal()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/revertassetcontenttooriginal%28%29.json'
content_hash: 'sha256:8699e0a0ae7e664d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# revertAssetContentToOriginal()

<sub>Instance Method</sub>

Request to revert any edits made to the asset’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func revertAssetContentToOriginal()
```

## Discussion

When an asset has been edited, Photos stores multiple versions of the asset: the original version of the asset as it was first captured or imported, and the input and output of the most recent edit. (You work with asset versions when requesting to edit an asset’s content—see [PHContentEditingInputRequestOptions](../phcontenteditinginputrequestoptions.md).) Call this method to revert to the original version of the asset, discarding all edits.

> [!important] Important
> This request fails if original content for the asset is not available on the current device (for example, if iCloud Photo Library is enabled and the user has edited the asset on a different device). Use [PHAssetResourceManager](../phassetresourcemanager.md) to ensure that original asset content is downloaded to the current device before making this request.

## See Also

### Editing Asset Content

- [contentEditingOutput](contenteditingoutput.md) — The output of an asset content editing session.
- [- revertAssetContentToOriginalResourceChoice:](<revertassetcontent(to_).md>) — Reverts the asset’s content to its original, choosing which original resource to use as the unadjusted base for all renders. _(beta)_
