---
title: subtitle
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtask/subtitle
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask/subtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtask/subtitle.json'
content_hash: 'sha256:c450128b3bf9bc6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGContinuedProcessingTask](../bgcontinuedprocessingtask.md)

# subtitle

<sub>Instance Property</sub>

The localized subtitle displayed to a person.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var subtitle: String { get }
```

## Discussion

Define the value of this property as a parameter to the request initializer:  [- initWithIdentifier:title:subtitle:](<../bgcontinuedprocessingtaskrequest/init(identifier_title_subtitle_).md>). After that, this property is read only, however you can update the subtitle by calling [- updateTitle:subtitle:](<updatetitle(__subtitle_).md>).

## See Also

### Titling the task

- [title](title.md) — The localized title displayed to a person.
- [- updateTitle:subtitle:](<updatetitle(__subtitle_).md>) — Update the task title and subtitle that the system displays to a person.
