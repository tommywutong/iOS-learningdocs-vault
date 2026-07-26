---
title: 'creationRequestForJob(destination:resource:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetresourceuploadjobchangerequest/creationrequestforjob(destination:resource:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/creationrequestforjob(destination:resource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjobchangerequest/creationrequestforjob%28destination%3Aresource%3A%29.json'
content_hash: 'sha256:64f5c025b94f0eb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJobChangeRequest](../phassetresourceuploadjobchangerequest.md)

# creationRequestForJob(destination:resource:)

<sub>Type Method</sub>

Creates an asset resource upload job and returns the change request.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func creationRequestForJob(destination: URLRequest, resource: PHAssetResource) -> Self
```

## Return Value

A change request for the created job.

## Discussion

This method creates an upload job and returns a change request that can be used to access the placeholder for the created job. Use the placeholder to obtain the local identifier before the change block completes.

If the number of jobs exceeds [jobLimit](../phassetresourceuploadjob/joblimit.md) the photo library `performChanges` request will fail with a `PHPhotosErrorLimitExceeded` error. To generate jobs after this limit is triggered, you must acknowledge succeeded/failed jobs, and wait for the registered/pending ones to finish uploading, which will make those jobs also succeeded/failed.

- Parameter:

    - destination: the destination [NSURLRequest](../../foundation/nsurlrequest.md) to which this asset resource will be sent.
    - resource: the asset resource to be uploaded.

## See Also

### Creating jobs

- [+ creationRequestForDownloadJobWithResource:](<creationrequestfordownloadjob(resource_).md>) — Creates a download-only job request for the specified asset resource.
