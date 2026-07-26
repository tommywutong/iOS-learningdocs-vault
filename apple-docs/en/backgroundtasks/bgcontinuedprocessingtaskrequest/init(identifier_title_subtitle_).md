---
title: 'init(identifier:title:subtitle:)'
framework: Background Tasks
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/init(identifier:title:subtitle:)'
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/init(identifier:title:subtitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/init%28identifier%3Atitle%3Asubtitle%3A%29.json'
content_hash: 'sha256:7ec4a902254c6f46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md)

# init(identifier:title:subtitle:)

<sub>Initializer</sub>

Creates an instance on behalf of the currently foregrounded app.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(identifier: String, title: String, subtitle: String)
```

## Parameters

- `identifier` — The task identifier.

- `title` — The localized title displayed to a person before the task begins running.

- `subtitle` — The localized subtitle displayed to a person before the task begins running.

## Discussion

Apps and their extensions need to use this method to initialize any tasks due to the underlying association to the currently foregrounded app. Note that [earliestBeginDate](../bgtaskrequest/earliestbegindate.md) is ignored by the scheduler in favor of `NSDate.now`.

The identifier must leverage a base wildcard notation, where the prefix of the identifier must at least contain the bundle ID of the submitting application, followed by optional semantic context, and finally ending with `.*`. An example: `<MainBundle>.<SemanticContext>.*` transforms to `com.foo.MyApplication.continuedProcessingTask.*`. Thus, a submitted identifier is of the form `com.foo.MyApplication.continuedProcessingTask.HD830D`.

> [!warning] Warning
> Successful creation of this object does not guarantee successful submission to the scheduler.
