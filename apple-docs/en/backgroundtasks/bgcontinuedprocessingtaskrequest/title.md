---
title: title
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/title
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/title.json'
content_hash: 'sha256:76b525191d9963b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md)

# title

<sub>Instance Property</sub>

The localized task title displayed to a person.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var title: String { get set }
```

## Discussion

Define the value of this property as a parameter to the request initializer:  [- initWithIdentifier:title:subtitle:](<init(identifier_title_subtitle_).md>).

## See Also

### Titling the task

- [subtitle](subtitle.md) — The localized subtitle displayed to a person.
