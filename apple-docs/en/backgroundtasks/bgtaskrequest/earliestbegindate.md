---
title: earliestBeginDate
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskrequest/earliestbegindate
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskrequest/earliestbegindate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskrequest/earliestbegindate.json'
content_hash: 'sha256:163af56609c1b4de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTaskRequest](../bgtaskrequest.md)

# earliestBeginDate

<sub>Instance Property</sub>

The earliest date and time at which to run the task.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var earliestBeginDate: Date? { get set }
```

## Discussion

Specify `nil` for no start delay.

Setting the property indicates that the background task shouldn’t start any earlier than this date. However, the system doesn’t guarantee launching the task at the specified date, but only that it won’t begin sooner.

## See Also

### Configuring a Task Request

- [identifier](identifier.md) — The identifier of the task associated with the request.
