---
title: 'retry(destination:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetresourceuploadjobchangerequest/retry(destination:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/retry(destination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjobchangerequest/retry%28destination%3A%29.json'
content_hash: 'sha256:7be5a9e8a08698e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJobChangeRequest](../phassetresourceuploadjobchangerequest.md)

# retry(destination:)

<sub>Instance Method</sub>

Retries a job that is failed, unacknowledged, and has not been retried before. Successful retries also free up space for [jobLimit](../phassetresourceuploadjob/joblimit.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func retry(destination: URLRequest?)
```

## See Also

### Processing jobs

- [- acknowledge](<acknowledge().md>) — Acknowledges a successful or failed job. Jobs must be acknowledged to free up space for [jobLimit](../phassetresourceuploadjob/joblimit.md).
- [- cancel](<cancel().md>) — Cancels an upload job that is registered or pending.
