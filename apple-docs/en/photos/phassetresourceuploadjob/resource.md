---
title: resource
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.1+（27.0 起废弃）, iPadOS 26.1+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phassetresourceuploadjob/resource
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/resource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/resource.json'
content_hash: 'sha256:4b2f38ff7dfd2d71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# resource

<sub>Instance Property</sub>

The asset resource this job promises to upload.

> [!warning] Deprecated
> Use +[PHAssetResource assetResourceForUploadJob:] instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var resource: PHAssetResource { get }
```

## See Also

### Inspecting a job

- [type](type-swift.property.md) — The type of this upload job.
- [Type](type-swift.enum.md) — Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [destination](destination.md) — The destination to send the job’s resource.
- [state](state-swift.property.md) — The state of this upload job.
- [State](state-swift.enum.md) — The stages of an upload job’s life cycle, from registered with the system through to completion.
- [error](error.md) — The error that caused the job to fail.
- [responseHeaderFields](responseheaderfields.md) — The HTTP response headers received from the server upon completion of the upload.
