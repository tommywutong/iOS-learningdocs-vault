---
title: 'updateTitle(_:subtitle:)'
framework: Background Tasks
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/backgroundtasks/bgcontinuedprocessingtask/updatetitle(_:subtitle:)'
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask/updatetitle(_:subtitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtask/updatetitle%28_%3Asubtitle%3A%29.json'
content_hash: 'sha256:caf79125071eb1c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGContinuedProcessingTask](../bgcontinuedprocessingtask.md)

# updateTitle(_:subtitle:)

<sub>Instance Method</sub>

Update the task title and subtitle that the system displays to a person.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func updateTitle(_ title: String, subtitle: String)
```

## Parameters

- `title` — The localized title displayed to a person.

- `subtitle` — The localized subtitle displayed to a person.

## Discussion

The system displays Continuous Background Task requests in a Live Activity for a person to monitor progress and cancel a task, if they wish.

## See Also

### Titling the task

- [title](title.md) — The localized title displayed to a person.
- [subtitle](subtitle.md) — The localized subtitle displayed to a person.
