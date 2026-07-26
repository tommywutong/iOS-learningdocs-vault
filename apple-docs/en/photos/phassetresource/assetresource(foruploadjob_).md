---
title: 'assetResource(forUploadJob:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photos/phassetresource/assetresource(foruploadjob:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresource/assetresource(foruploadjob:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresource/assetresource%28foruploadjob%3A%29.json'
content_hash: 'sha256:bbf7a7ff5221da67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResource](../phassetresource.md)

# assetResource(forUploadJob:)

<sub>Type Method</sub>

Returns the asset resource associated with the given upload job.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func assetResource(forUploadJob job: PHAssetResourceUploadJob) -> PHAssetResource?
```

## Return Value

The asset resource associated with the upload job, or nil if the resource cannot be found.

## Discussion

- job: the upload job whose associated asset resource is returned
