---
title: PHAssetResourceUploadJobChangeRequest
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjobchangerequest
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjobchangerequest.json'
content_hash: 'sha256:11043ebe451d3d31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResourceUploadJobChangeRequest

<sub>Class</sub>

Use within an application’s `com.apple.photos.background-upload` extension to create and change [PHAssetResourceUploadJob](phassetresourceuploadjob.md) records.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class PHAssetResourceUploadJobChangeRequest
```

## Overview

When the extension’s principal class receives a call to `process` background uploads, it can create new [PHAssetResourceUploadJob](phassetresourceuploadjob.md)s through calls to perform changes on a PHPhotoLibrary using [PHAssetResourceUploadJobChangeRequest](phassetresourceuploadjobchangerequest.md) and any in-flight upload jobs can be handled by updating their state to mark them as acknowledged, or to be retried. The maximum number of jobs that can be in flight is limited to the `PHAssetResourceUploadJob.jobLimit`.

[PHAssetResourceUploadJobChangeRequest](phassetresourceuploadjobchangerequest.md) can only be created or used within a photo library change block. For details on change blocks, see [PHPhotoLibrary](phphotolibrary.md).

## Relationships

- **Inherits From**: [PHChangeRequest](phchangerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a change request

- [+ changeRequestForUploadJob:](<phassetresourceuploadjobchangerequest/init(for_).md>) — Creates a request for modifying the specified upload job.

### Creating jobs

- [+ creationRequestForDownloadJobWithResource:](<phassetresourceuploadjobchangerequest/creationrequestfordownloadjob(resource_).md>) — Creates a download-only job request for the specified asset resource.
- [+ creationRequestForJobWithDestination:resource:](<phassetresourceuploadjobchangerequest/creationrequestforjob(destination_resource_).md>) — Creates an asset resource upload job and returns the change request.

### Processing jobs

- [- acknowledge](<phassetresourceuploadjobchangerequest/acknowledge().md>) — Acknowledges a successful or failed job. Jobs must be acknowledged to free up space for [jobLimit](phassetresourceuploadjob/joblimit.md).
- [- retryWithDestination:](<phassetresourceuploadjobchangerequest/retry(destination_).md>) — Retries a job that is failed, unacknowledged, and has not been retried before. Successful retries also free up space for [jobLimit](phassetresourceuploadjob/joblimit.md).
- [- cancel](<phassetresourceuploadjobchangerequest/cancel().md>) — Cancels an upload job that is registered or pending.

### Accessing details about the job

- [placeholderForCreatedAssetResourceUploadJob](phassetresourceuploadjobchangerequest/placeholderforcreatedassetresourceuploadjob.md) — A placeholder for the asset resource upload job created by this request.

### Deprecated

- [+ createJobWithDestination:resource:](<phassetresourceuploadjobchangerequest/createjob(destination_resource_).md>) — Creates an asset resource upload job.

### Initializers

- [init(forUploadJob:)](<phassetresourceuploadjobchangerequest/init(foruploadjob_).md>)

## See Also

### Background resource upload extensions

- [Uploading asset resources in the background](../photokit/uploading-asset-resources-in-the-background.md) — Enable reliable cloud backup for photo library assets with background processing.
- [PHBackgroundResourceUploadExtension](phbackgroundresourceuploadextension.md) _(deprecated)_
- [PHAssetResourceUploadJob](phassetresourceuploadjob.md) — An object that represents a request to upload an asset resource.
