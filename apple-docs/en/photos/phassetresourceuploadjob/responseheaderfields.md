---
title: responseHeaderFields
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/responseheaderfields
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/responseheaderfields'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/responseheaderfields.json'
content_hash: 'sha256:0fe818fd595899ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# responseHeaderFields

<sub>Instance Property</sub>

The HTTP response headers received from the server upon completion of the upload.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var responseHeaderFields: [String : String]? { get }
```

## Return Value

A dictionary of response header fields, or `nil` if the job has not completed or no HTTP response was received.

## Discussion

This property is populated when the job reaches a terminal state (`PHAssetResourceUploadJobStateSucceeded` or `PHAssetResourceUploadJobStateFailed`). It contains the HTTP response headers returned by the destination server.

Header field names are normalized to lowercase for consistent lookup.

## See Also

### Inspecting a job

- [type](type-swift.property.md) — The type of this upload job.
- [Type](type-swift.enum.md) — Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [destination](destination.md) — The destination to send the job’s resource.
- [resource](resource.md) — The asset resource this job promises to upload. _(deprecated)_
- [state](state-swift.property.md) — The state of this upload job.
- [State](state-swift.enum.md) — The stages of an upload job’s life cycle, from registered with the system through to completion.
- [error](error.md) — The error that caused the job to fail.
