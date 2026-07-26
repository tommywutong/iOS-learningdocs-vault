---
title: PHAssetResourceUploadJob.Type
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/type-swift.enum
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/type-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/type-swift.enum.json'
content_hash: 'sha256:ef1edbbf77d325d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# PHAssetResourceUploadJob.Type

<sub>Enumeration</sub>

Indicates whether a job downloads and then uploads an asset to the server or only downloads it.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum `Type`
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [PHAssetResourceUploadJobTypeDownloadOnly](type-swift.enum/downloadonly.md) — A download job type (will download the resource from iCloud if required)
- [PHAssetResourceUploadJobTypeUpload](type-swift.enum/upload.md) — An upload job type (will download the resource from iCloud if required. then upload)

### Initializers

- [init(rawValue:)](<type-swift.enum/init(rawvalue_).md>)

## See Also

### Inspecting a job

- [type](type-swift.property.md) — The type of this upload job.
- [destination](destination.md) — The destination to send the job’s resource.
- [resource](resource.md) — The asset resource this job promises to upload. _(deprecated)_
- [state](state-swift.property.md) — The state of this upload job.
- [State](state-swift.enum.md) — The stages of an upload job’s life cycle, from registered with the system through to completion.
- [error](error.md) — The error that caused the job to fail.
- [responseHeaderFields](responseheaderfields.md) — The HTTP response headers received from the server upon completion of the upload.
