---
title: PHAssetResourceUploadJob.Action.retry
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/action/retry
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/action/retry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/action/retry.json'
content_hash: 'sha256:fcc4a4c3d2ae40cb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Photos](../../../photos.md) · [PHAssetResourceUploadJob](../../phassetresourceuploadjob.md) · [Action](../action.md)

# PHAssetResourceUploadJob.Action.retry

<sub>Case</sub>

A job to retry processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
case retry
```

## Discussion

A retryable job has a [state](../state-swift.property.md) of `failed` and hasn’t previously been retried.

Call [- retryWithDestination:](<../../phassetresourceuploadjobchangerequest/retry(destination_).md>) to retry the job.

## See Also

### Actions

- [PHAssetResourceUploadJobActionAcknowledge](acknowledge.md) — A job that requires acknowledgement.
