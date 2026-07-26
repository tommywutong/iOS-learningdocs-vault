---
title: 'dataTask(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/datatask(with:)-10dy7'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/datatask(with:)-10dy7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/datatask%28with%3A%29-10dy7.json'
content_hash: 'sha256:385a3a46cfc52f64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# dataTask(with:)

<sub>Instance Method</sub>

Creates a task that retrieves the contents of the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dataTask(with url: URL) -> URLSessionDataTask
```

## Parameters

- `url` — The URL to be retrieved.

## Return Value

The new session data task.

## Discussion

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method. The task calls methods on the session’s delegate to provide you with the response metadata, response data, and so on.

## See Also

### Adding data tasks to a session

- [- dataTaskWithURL:completionHandler:](<datatask(with_completionhandler_)-52wk8.md>) — Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [- dataTaskWithRequest:](<datatask(with_)-7jpys.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [- dataTaskWithRequest:completionHandler:](<datatask(with_completionhandler_)-e6xv.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [URLSessionDataTask](../urlsessiondatatask.md) — A URL session task that returns downloaded data directly to the app in memory.
- [URLSessionDataDelegate](../urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.
