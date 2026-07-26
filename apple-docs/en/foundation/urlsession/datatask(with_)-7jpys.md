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
doc_path: '/documentation/foundation/urlsession/datatask(with:)-7jpys'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/datatask(with:)-7jpys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/datatask%28with%3A%29-7jpys.json'
content_hash: 'sha256:58f68e663362a2e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# dataTask(with:)

<sub>Instance Method</sub>

Creates a task that retrieves the contents of a URL based on the specified URL request object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dataTask(with request: URLRequest) -> URLSessionDataTask
```

## Parameters

- `request` — A URL request object that provides request-specific information such as the URL, cache policy, request type, and body data or body stream.

## Return Value

The new session data task.

## Discussion

By creating a task based on a request object, you can tune various aspects of the task’s behavior, including the cache policy and timeout interval.

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method.

## See Also

### Adding data tasks to a session

- [- dataTaskWithURL:](<datatask(with_)-10dy7.md>) — Creates a task that retrieves the contents of the specified URL.
- [- dataTaskWithURL:completionHandler:](<datatask(with_completionhandler_)-52wk8.md>) — Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [- dataTaskWithRequest:completionHandler:](<datatask(with_completionhandler_)-e6xv.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [URLSessionDataTask](../urlsessiondatatask.md) — A URL session task that returns downloaded data directly to the app in memory.
- [URLSessionDataDelegate](../urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.
