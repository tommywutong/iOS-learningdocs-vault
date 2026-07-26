---
title: 'cancel(taskRequestWithIdentifier:)'
framework: Background Tasks
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/backgroundtasks/bgtaskscheduler/cancel(taskrequestwithidentifier:)'
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/cancel(taskrequestwithidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/cancel%28taskrequestwithidentifier%3A%29.json'
content_hash: 'sha256:d943aa103c83366b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTaskScheduler](../bgtaskscheduler.md)

# cancel(taskRequestWithIdentifier:)

<sub>Instance Method</sub>

Cancel a previously scheduled task request.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cancel(taskRequestWithIdentifier identifier: String)
```

## Parameters

- `identifier` — The string identifier of the task request to cancel.

## See Also

### Canceling a task

- [- cancelAllTaskRequests](<cancelalltaskrequests().md>) — Cancel all scheduled task requests.
