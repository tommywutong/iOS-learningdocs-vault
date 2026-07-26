---
title: error
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/error
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/error.json'
content_hash: 'sha256:928062f4e3d54401'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# error

<sub>Instance Property</sub>

The error that caused the job to fail.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var error: (any Error)? { get }
```

## Return Value

An error object describing the failure, or `nil` if the job has not failed.

## Discussion

This property is populated when the job reaches the `PHAssetResourceUploadJobStateFailed` state. It provides detailed information about why the upload failed, including network errors, server errors, or client-side errors.

> [!note] Note
> The error provided is sanitized and may not be the actual error returned from URLResponse.

## See Also

### Inspecting a job

- [type](type-swift.property.md) — The type of this upload job.
- [Type](type-swift.enum.md) — Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [destination](destination.md) — The destination to send the job’s resource.
- [resource](resource.md) — The asset resource this job promises to upload. _(deprecated)_
- [state](state-swift.property.md) — The state of this upload job.
- [State](state-swift.enum.md) — The stages of an upload job’s life cycle, from registered with the system through to completion.
- [responseHeaderFields](responseheaderfields.md) — The HTTP response headers received from the server upon completion of the upload.
