---
title: type
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/type-swift.property
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/type-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/type-swift.property.json'
content_hash: 'sha256:1e05e53a6a768018'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# type

<sub>Instance Property</sub>

The type of this upload job.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var type: PHAssetResourceUploadJob.Type { get }
```

## See Also

### Inspecting a job

- [Type](type-swift.enum.md) — Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [destination](destination.md) — The destination to send the job’s resource.
- [resource](resource.md) — The asset resource this job promises to upload. _(deprecated)_
- [state](state-swift.property.md) — The state of this upload job.
- [State](state-swift.enum.md) — The stages of an upload job’s life cycle, from registered with the system through to completion.
- [error](error.md) — The error that caused the job to fail.
- [responseHeaderFields](responseheaderfields.md) — The HTTP response headers received from the server upon completion of the upload.
