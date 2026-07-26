---
title: 'creationRequestForDownloadJob(resource:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetresourceuploadjobchangerequest/creationrequestfordownloadjob(resource:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/creationrequestfordownloadjob(resource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjobchangerequest/creationrequestfordownloadjob%28resource%3A%29.json'
content_hash: 'sha256:06828e86c55ae7b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJobChangeRequest](../phassetresourceuploadjobchangerequest.md)

# creationRequestForDownloadJob(resource:)

<sub>Type Method</sub>

Creates a download-only job request for the specified asset resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func creationRequestForDownloadJob(resource: PHAssetResource) -> Self
```

## Parameters

- `resource` — The asset resource to download.

## Return Value

A change request for the created job.

## Discussion

This method registers a job that requests an asset resource be downloaded from iCloud to the device without uploading it to a remote server. The download operation is performed asynchronously by the system over time. This is useful when you need to ensure a resource is available locally for processing.

The job will transition through the same states as upload jobs (`PHAssetResourceUploadJobStateRegistered`, `PHAssetResourceUploadJobStatePending`, and eventually `PHAssetResourceUploadJobStateSucceeded` or `PHAssetResourceUploadJobStateFailed`), but will only perform a download operation.

Use `fetchJobsWithAction:options:` to check the job’s state. When the job reaches `PHAssetResourceUploadJobStateSucceeded`, the download has completed successfully.

> [!note] Note
> The system may subsequently purge the downloaded resource due to system conditions.

## See Also

### Creating jobs

- [+ creationRequestForJobWithDestination:resource:](<creationrequestforjob(destination_resource_).md>) — Creates an asset resource upload job and returns the change request.
