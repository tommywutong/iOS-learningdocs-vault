---
title: 'urlSession(_:task:didFinishCollecting:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didfinishcollecting:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didfinishcollecting:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Atask%3Adidfinishcollecting%3A%29.json'
content_hash: 'sha256:54d0ee743b9d6e17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:task:didFinishCollecting:)

<sub>Instance Method</sub>

Tells the delegate that the session finished collecting metrics for the task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didFinishCollecting metrics: URLSessionTaskMetrics)
```

## Parameters

- `session` — The session collecting the metrics.

- `task` — The task whose metrics have been collected.

- `metrics` — The collected metrics.

## See Also

### Collecting task metrics

- [URLSessionTaskMetrics](../urlsessiontaskmetrics.md) — An object encapsulating the metrics for a session task.
