---
title: PHAssetResourceUploadJob.State
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/state-swift.enum
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/state-swift.enum.json'
content_hash: 'sha256:9674e8fb8273fcd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# PHAssetResourceUploadJob.State

<sub>Enumeration</sub>

The stages of an upload job’s life cycle, from registered with the system through to completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### States

- [PHAssetResourceUploadJobStateRegistered](state-swift.enum/registered.md) — The job has been registered.
- [PHAssetResourceUploadJobStatePending](state-swift.enum/pending.md) — A request has been made to send the asset resource to the destination, but has not yet been fulfilled.
- [PHAssetResourceUploadJobStateSucceeded](state-swift.enum/succeeded.md) — The job has sent over successfully.
- [PHAssetResourceUploadJobStateFailed](state-swift.enum/failed.md) — The job has failed to send over.
- [PHAssetResourceUploadJobStateCancelled](state-swift.enum/cancelled.md) — The job has been cancelled.

### Initializers

- [init(rawValue:)](<state-swift.enum/init(rawvalue_).md>)

## See Also

### Inspecting a job

- [type](type-swift.property.md) — The type of this upload job.
- [Type](type-swift.enum.md) — Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [destination](destination.md) — The destination to send the job’s resource.
- [resource](resource.md) — The asset resource this job promises to upload. _(deprecated)_
- [state](state-swift.property.md) — The state of this upload job.
- [error](error.md) — The error that caused the job to fail.
- [responseHeaderFields](responseheaderfields.md) — The HTTP response headers received from the server upon completion of the upload.
