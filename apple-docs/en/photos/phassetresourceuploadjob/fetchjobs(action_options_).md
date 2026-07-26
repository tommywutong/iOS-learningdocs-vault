---
title: 'fetchJobs(action:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetresourceuploadjob/fetchjobs(action:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/fetchjobs(action:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/fetchjobs%28action%3Aoptions%3A%29.json'
content_hash: 'sha256:460582eb3c775784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# fetchJobs(action:options:)

<sub>Type Method</sub>

Returns all asset resource upload jobs applicable for a given action.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func fetchJobs(action: PHAssetResourceUploadJob.Action, options: PHFetchOptions?) -> PHFetchResult<PHAssetResourceUploadJob>
```

## Parameters

- `action` — The actions a client can take on a job.

- `options` — The fetch options to be passed in.

## Return Value

The jobs available on which you can apply an action found in [Action](action.md).

## See Also

### Fetching jobs

- [jobLimit](joblimit.md) — The maximum number of unacknowledged upload jobs allowed.
- [Action](action.md) — An action to perform on an upload job.
