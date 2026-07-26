---
title: taskInterval
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontaskmetrics/taskinterval
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/taskinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskmetrics/taskinterval.json'
content_hash: 'sha256:3bb0263b082dc1cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskMetrics](../urlsessiontaskmetrics.md)

# taskInterval

<sub>Instance Property</sub>

The time interval between when a task is instantiated and when the task is completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var taskInterval: DateInterval { get }
```

## See Also

### Accessing task metrics

- [transactionMetrics](transactionmetrics.md) — An array of metrics for each individual request-response transaction made during the execution of the task.
- [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md) — An object that encapsualtes the performance metrics collected by the URL Loading System during the execution of a session task.
- [redirectCount](redirectcount.md) — The number of redirects that occurred during the execution of the task.
