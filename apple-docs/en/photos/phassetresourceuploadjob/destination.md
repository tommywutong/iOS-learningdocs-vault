---
title: destination
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/destination
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/destination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/destination.json'
content_hash: 'sha256:fb92b71f8e3a7890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# destination

<sub>Instance Property</sub>

The destination to send the job’s resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var destination: URLRequest { get }
```

## See Also

### Inspecting a job

- [type](type-swift.property.md) — The type of this upload job.
- [Type](type-swift.enum.md) — Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [resource](resource.md) — The asset resource this job promises to upload. _(deprecated)_
- [state](state-swift.property.md) — The state of this upload job.
- [State](state-swift.enum.md) — The stages of an upload job’s life cycle, from registered with the system through to completion.
- [error](error.md) — The error that caused the job to fail.
- [responseHeaderFields](responseheaderfields.md) — The HTTP response headers received from the server upon completion of the upload.
