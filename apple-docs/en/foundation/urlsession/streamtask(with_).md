---
title: 'streamTask(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/urlsession/streamtask(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/streamtask(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/streamtask%28with%3A%29.json'
content_hash: 'sha256:c6a24670947ea5e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# streamTask(with:)

<sub>Instance Method</sub>

Creates a task that establishes a bidirectional TCP/IP connection using a specified network service.

> [!warning] Deprecated
> Use nw_connection_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func streamTask(with service: NetService) -> URLSessionStreamTask
```

## Parameters

- `service` — A [NetService](../netservice.md) object used to determine the endpoint of the TCP/IP connection. This network service is resolved before any data is read or written to the resulting stream task.

## Return Value

The new session stream task.

## Discussion

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method.

## See Also

### Adding stream tasks to a session

- [- streamTaskWithHostName:port:](<streamtask(withhostname_port_).md>) — Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [URLSessionStreamTask](../urlsessionstreamtask.md) — A URL session task that is stream-based.
- [URLSessionStreamDelegate](../urlsessionstreamdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.
