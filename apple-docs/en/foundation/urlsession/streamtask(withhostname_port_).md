---
title: 'streamTask(withHostName:port:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/streamtask(withhostname:port:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/streamtask(withhostname:port:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/streamtask%28withhostname%3Aport%3A%29.json'
content_hash: 'sha256:e00ce84384ab6221'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# streamTask(withHostName:port:)

<sub>Instance Method</sub>

Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func streamTask(withHostName hostname: String, port: Int) -> URLSessionStreamTask
```

## Parameters

- `hostname` — The hostname of the connection endpoint.

- `port` — The port of the connection endpoint.

## Return Value

The new session stream task.

## Discussion

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method.

## See Also

### Adding stream tasks to a session

- [- streamTaskWithNetService:](<streamtask(with_).md>) — Creates a task that establishes a bidirectional TCP/IP connection using a specified network service. _(deprecated)_
- [URLSessionStreamTask](../urlsessionstreamtask.md) — A URL session task that is stream-based.
- [URLSessionStreamDelegate](../urlsessionstreamdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.
