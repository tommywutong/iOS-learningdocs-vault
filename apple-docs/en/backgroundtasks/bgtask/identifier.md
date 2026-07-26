---
title: identifier
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtask/identifier
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtask/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtask/identifier.json'
content_hash: 'sha256:2866c4d6e5173e2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTask](../bgtask.md)

# identifier

<sub>Instance Property</sub>

The string identifier of the task.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var identifier: String { get }
```

## Discussion

The identifier is the same as the one used to register the launch handler in [- registerForTaskWithIdentifier:usingQueue:launchHandler:](<../bgtaskscheduler/register(fortaskwithidentifier_using_launchhandler_).md>).
