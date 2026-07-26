---
title: state
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/state-swift.property
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/state-swift.property.json'
content_hash: 'sha256:104597106788dcc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# state

<sub>Instance Property</sub>

The state of this upload job.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var state: PHAssetResourceUploadJob.State { get }
```

## See Also

### Inspecting a job

- [type](type-swift.property.md) — The type of this upload job.
- [Type](type-swift.enum.md) — Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [destination](destination.md) — The destination to send the job’s resource.
- [resource](resource.md) — The asset resource this job promises to upload. _(deprecated)_
- [State](state-swift.enum.md) — The stages of an upload job’s life cycle, from registered with the system through to completion.
- [error](error.md) — The error that caused the job to fail.
- [responseHeaderFields](responseheaderfields.md) — The HTTP response headers received from the server upon completion of the upload.
