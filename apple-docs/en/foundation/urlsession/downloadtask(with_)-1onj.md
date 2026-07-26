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
doc_path: '/documentation/foundation/urlsession/downloadtask(with:)-1onj'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/downloadtask(with:)-1onj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/downloadtask%28with%3A%29-1onj.json'
content_hash: 'sha256:d22af3d8c5ab2004'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# downloadTask(with:)

<sub>Instance Method</sub>

Creates a download task that retrieves the contents of the specified URL and saves the results to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func downloadTask(with url: URL) -> URLSessionDownloadTask
```

## Parameters

- `url` — The URL to download.

## Return Value

The new session download task.

## Discussion

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method.

## See Also

### Adding download tasks to a session

- [- downloadTaskWithURL:completionHandler:](<downloadtask(with_completionhandler_)-7cuje.md>) — Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithRequest:](<downloadtask(with_)-3fb7s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.
- [- downloadTaskWithRequest:completionHandler:](<downloadtask(with_completionhandler_)-4a84s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithResumeData:](<downloadtask(withresumedata_).md>) — Creates a download task to resume a previously canceled or failed download.
- [- downloadTaskWithResumeData:completionHandler:](<downloadtask(withresumedata_completionhandler_).md>) — Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.
- [URLSessionDownloadTask](../urlsessiondownloadtask.md) — A URL session task that stores downloaded data to a file.
- [URLSessionDownloadDelegate](../urlsessiondownloaddelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.
