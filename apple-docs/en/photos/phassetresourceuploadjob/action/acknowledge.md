---
title: PHAssetResourceUploadJob.Action.acknowledge
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/action/acknowledge
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/action/acknowledge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/action/acknowledge.json'
content_hash: 'sha256:a465cc584f13351f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Photos](../../../photos.md) · [PHAssetResourceUploadJob](../../phassetresourceuploadjob.md) · [Action](../action.md)

# PHAssetResourceUploadJob.Action.acknowledge

<sub>Case</sub>

A job that requires acknowledgement.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
case acknowledge
```

## Discussion

An acknowledgeable job has a [state](../state-swift.property.md) of `succeeded` or `failed` and hasn’t been acknowledged.

Call [- acknowledge](<../../phassetresourceuploadjobchangerequest/acknowledge().md>) to acknowledge a job and free queue capacity for new uploads.

## See Also

### Actions

- [PHAssetResourceUploadJobActionRetry](retry.md) — A job to retry processing.
