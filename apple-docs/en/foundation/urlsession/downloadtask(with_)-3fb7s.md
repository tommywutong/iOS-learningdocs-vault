---
title: 'downloadTask(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/downloadtask(with:)-3fb7s'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/downloadtask(with:)-3fb7s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/downloadtask%28with%3A%29-3fb7s.json'
content_hash: 'sha256:db5ab3fe33cdd1e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# downloadTask(with:)

<sub>Instance Method</sub>

Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func downloadTask(with request: URLRequest) -> URLSessionDownloadTask
```

## Parameters

- `request` — A URL request object that provides the URL, cache policy, request type, body data or body stream, and so on.

## Return Value

The new session download task.

## Discussion

By creating a task based on a request object, you can tune various aspects of the task’s behavior, including the cache policy and timeout interval.

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method. The task calls methods on the session’s delegate to provide you with progress notifications, the location of the resulting temporary file, and so on.

## See Also

### Adding download tasks to a session

- [- downloadTaskWithURL:](<downloadtask(with_)-1onj.md>) — Creates a download task that retrieves the contents of the specified URL and saves the results to a file.
- [- downloadTaskWithURL:completionHandler:](<downloadtask(with_completionhandler_)-7cuje.md>) — Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithRequest:completionHandler:](<downloadtask(with_completionhandler_)-4a84s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithResumeData:](<downloadtask(withresumedata_).md>) — Creates a download task to resume a previously canceled or failed download.
- [- downloadTaskWithResumeData:completionHandler:](<downloadtask(withresumedata_completionhandler_).md>) — Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.
- [URLSessionDownloadTask](../urlsessiondownloadtask.md) — A URL session task that stores downloaded data to a file.
- [URLSessionDownloadDelegate](../urlsessiondownloaddelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.
