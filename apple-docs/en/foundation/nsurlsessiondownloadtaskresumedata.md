---
title: NSURLSessionDownloadTaskResumeData
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlsessiondownloadtaskresumedata
source_url: 'https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtaskresumedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlsessiondownloadtaskresumedata.json'
content_hash: 'sha256:3f550666f0cd23e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLSessionDownloadTaskResumeData

<sub>Global Variable</sub>

A key in the error dictionary that provides resume data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLSessionDownloadTaskResumeData: String
```

## Discussion

When a transfer error occurs or when you call the [- cancelByProducingResumeData:](<urlsessiondownloadtask/cancel(byproducingresumedata_).md>) method, the delegate object or completion handler gets an [NSError](nserror.md) object. If the transfer is resumable, that error object’s `userInfo` dictionary contains a value for this key. To resume the transfer, your app can pass that value to the [- downloadTaskWithResumeData:](<urlsession/downloadtask(withresumedata_).md>) or [- downloadTaskWithResumeData:completionHandler:](<urlsession/downloadtask(withresumedata_completionhandler_).md>) method.

## See Also

### User info dictionary keys

- [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) — A key in the error dictionary that provides the reason for canceling a background task.
