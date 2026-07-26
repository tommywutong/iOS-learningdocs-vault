---
title: 'setTaskCompleted(success:)'
framework: Background Tasks
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/backgroundtasks/bgtask/settaskcompleted(success:)'
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtask/settaskcompleted(success:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtask/settaskcompleted%28success%3A%29.json'
content_hash: 'sha256:78e17f98b714bbeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTask](../bgtask.md)

# setTaskCompleted(success:)

<sub>Instance Method</sub>

Informs the background task scheduler that the task is complete.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTaskCompleted(success: Bool)
```

## Parameters

- `success` — A `Boolean` indicating if the task completed successfully or not.

## Discussion

Not calling [- setTaskCompletedWithSuccess:](<settaskcompleted(success_).md>) before the time for the task expires may result in the system killing your app.

You can reschedule an unsuccessful required task.

> [!important] Important
> If you don’t set an expiration handler, the system will mark your task as complete and unsuccessful instead of sending a warning.

## See Also

### Configuring a Task

- [expirationHandler](expirationhandler.md) — A handler called shortly before the task’s background time expires.
