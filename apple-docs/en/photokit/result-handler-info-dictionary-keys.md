---
title: Result Handler Info Dictionary Keys
framework: Photos
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/result-handler-info-dictionary-keys
source_url: 'https://developer.apple.com/documentation/photokit/result-handler-info-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/result-handler-info-dictionary-keys.json'
content_hash: 'sha256:1fbeed7216c468f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md) · [Photos](../photos.md) · [PHLivePhoto](../photos/phlivephoto.md)

# Result Handler Info Dictionary Keys

<sub>API Collection</sub>

Info describing an attempt to load a Live Photo.

## Overview

These keys are in the `info` dictionary of the result handler you provide for the [+ requestLivePhotoWithResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:](<../photos/phlivephoto/request(withresourcefileurls_placeholderimage_targetsize_contentmode_resulthandler_).md>) method.

## Topics

### Constants

- [PHLivePhotoInfoErrorKey](../photos/phlivephotoinfoerrorkey.md) — An error that occurred while attempting to load the requested Live Photo.
- [PHLivePhotoInfoIsDegradedKey](../photos/phlivephotoinfoisdegradedkey.md) — A Boolean (`NSNumber`) value indicating whether the result Live Photo is a low-quality substitute for the requested Live Photo.
- [PHLivePhotoInfoCancelledKey](../photos/phlivephotoinfocancelledkey.md) — A Boolean (`NSNumber`) value indicating whether the Live Photo loading request was canceled.

## See Also

### Constants

- [PHLivePhotoRequestID](../photos/phlivephotorequestid.md) — A numeric identifier for an asynchronous Live Photo loading request.
- [Image Request Identifiers](image-request-identifiers.md) — Special values for the Live Photo request ID that are returned by asynchronous requests.
