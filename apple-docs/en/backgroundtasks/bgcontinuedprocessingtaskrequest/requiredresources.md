---
title: requiredResources
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/requiredresources
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/requiredresources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/requiredresources.json'
content_hash: 'sha256:f91fc1bf3687fe65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md)

# requiredResources

<sub>Instance Property</sub>

An option that indicates any special system resources that the task requires.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var requiredResources: BGContinuedProcessingTaskRequest.Resources { get set }
```

## Discussion

To request background GPU support for the task, set this property to [BGContinuedProcessingTaskRequestResourcesGPU](resources/gpu.md). First, check whether the device supports background GPU use; see [supportedResources](../bgtaskscheduler/supportedresources.md).

The default value is [BGContinuedProcessingTaskRequestResourcesDefault](../bgcontinuedprocessingtaskrequestresources/bgcontinuedprocessingtaskrequestresourcesdefault.md).

## See Also

### Identifying resource dependencies

- [Resources](resources.md) — Options that specify additional system resources a background task needs.
