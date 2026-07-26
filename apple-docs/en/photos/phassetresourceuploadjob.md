---
title: PHAssetResourceUploadJob
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob.json'
content_hash: 'sha256:47475827adbb886e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResourceUploadJob

<sub>Class</sub>

An object that represents a request to upload an asset resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class PHAssetResourceUploadJob
```

## Overview

Use within an application’s `com.apple.photos.background-upload` extension to request an upload of a [PHAssetResource](phassetresource.md) to a destination [NSURLRequest](../foundation/nsurlrequest.md).

When the extension’s principal class receives a call to [process()](<phbackgroundresourceuploadextension/process().md>) background uploads, it can create new [PHAssetResourceUploadJob](phassetresourceuploadjob.md) objects using [PHAssetResourceUploadJobChangeRequest](phassetresourceuploadjobchangerequest.md).

The maximum number of jobs that can be in flight is limited to the [jobLimit](phassetresourceuploadjob/joblimit.md). To make space for new jobs, you must call `PHAssetResourceUploadJobChangeRequest/fetchJobsWithAction:options:` and retry/acknowledge them with `PHAssetResourceUploadJobChangeRequest/acknowledge:` or [- retryWithDestination:](<phassetresourceuploadjobchangerequest/retry(destination_).md>) respectively.

## Relationships

- **Inherits From**: [PHObject](phobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Fetching jobs

- [jobLimit](phassetresourceuploadjob/joblimit.md) — The maximum number of unacknowledged upload jobs allowed.
- [+ fetchJobsWithAction:options:](<phassetresourceuploadjob/fetchjobs(action_options_).md>) — Returns all asset resource upload jobs applicable for a given action.
- [Action](phassetresourceuploadjob/action.md) — An action to perform on an upload job.

### Inspecting a job

- [type](phassetresourceuploadjob/type-swift.property.md) — The type of this upload job.
- [Type](phassetresourceuploadjob/type-swift.enum.md) — Indicates whether a job downloads and then uploads an asset to the server or only downloads it.
- [destination](phassetresourceuploadjob/destination.md) — The destination to send the job’s resource.
- [resource](phassetresourceuploadjob/resource.md) — The asset resource this job promises to upload. _(deprecated)_
- [state](phassetresourceuploadjob/state-swift.property.md) — The state of this upload job.
- [State](phassetresourceuploadjob/state-swift.enum.md) — The stages of an upload job’s life cycle, from registered with the system through to completion.
- [error](phassetresourceuploadjob/error.md) — The error that caused the job to fail.
- [responseHeaderFields](phassetresourceuploadjob/responseheaderfields.md) — The HTTP response headers received from the server upon completion of the upload.

## See Also

### Background resource upload extensions

- [Uploading asset resources in the background](../photokit/uploading-asset-resources-in-the-background.md) — Enable reliable cloud backup for photo library assets with background processing.
- [PHBackgroundResourceUploadExtension](phbackgroundresourceuploadextension.md) _(deprecated)_
- [PHAssetResourceUploadJobChangeRequest](phassetresourceuploadjobchangerequest.md) — Use within an application’s `com.apple.photos.background-upload` extension to create and change [PHAssetResourceUploadJob](phassetresourceuploadjob.md) records.
