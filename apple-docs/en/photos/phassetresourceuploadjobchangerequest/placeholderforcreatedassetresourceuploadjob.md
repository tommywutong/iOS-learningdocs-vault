---
title: placeholderForCreatedAssetResourceUploadJob
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjobchangerequest/placeholderforcreatedassetresourceuploadjob
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/placeholderforcreatedassetresourceuploadjob'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjobchangerequest/placeholderforcreatedassetresourceuploadjob.json'
content_hash: 'sha256:9c8f5e0c8def65cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJobChangeRequest](../phassetresourceuploadjobchangerequest.md)

# placeholderForCreatedAssetResourceUploadJob

<sub>Instance Property</sub>

A placeholder for the asset resource upload job created by this request.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var placeholderForCreatedAssetResourceUploadJob: PHObjectPlaceholder? { get }
```

## Discussion

The placeholder can be used to obtain the local identifier of the job that will be created when the change block completes.
