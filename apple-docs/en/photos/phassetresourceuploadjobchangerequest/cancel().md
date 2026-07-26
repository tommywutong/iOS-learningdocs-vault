---
title: cancel()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjobchangerequest/cancel()
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjobchangerequest/cancel%28%29.json'
content_hash: 'sha256:38bda7672a0a53fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJobChangeRequest](../phassetresourceuploadjobchangerequest.md)

# cancel()

<sub>Instance Method</sub>

Cancels an upload job that is registered or pending.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func cancel()
```

## Discussion

Use this method to cancel an upload job that has not yet completed. This is useful when a resource is uploaded through another path (e.g., the main app) and the background upload job is no longer needed, avoiding wasteful duplicate uploads.

Only jobs in the `PHAssetResourceUploadJobStateRegistered` or `PHAssetResourceUploadJobStatePending` states can be cancelled. Cancelled jobs transition to the `PHAssetResourceUploadJobStateCancelled` state and are automatically acknowledged.

## See Also

### Processing jobs

- [- acknowledge](<acknowledge().md>) — Acknowledges a successful or failed job. Jobs must be acknowledged to free up space for [jobLimit](../phassetresourceuploadjob/joblimit.md).
- [- retryWithDestination:](<retry(destination_).md>) — Retries a job that is failed, unacknowledged, and has not been retried before. Successful retries also free up space for [jobLimit](../phassetresourceuploadjob/joblimit.md).
