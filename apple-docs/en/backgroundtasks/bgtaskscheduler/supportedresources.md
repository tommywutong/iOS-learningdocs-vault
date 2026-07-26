---
title: supportedResources
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler/supportedresources
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/supportedresources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/supportedresources.json'
content_hash: 'sha256:fa69c2ad2d266ecf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGTaskScheduler](../bgtaskscheduler.md)

# supportedResources

<sub>Type Property</sub>

Additional system resources that a continuous background task can request.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class var supportedResources: BGContinuedProcessingTaskRequest.Resources { get }
```

## Discussion

The [Resources](../bgcontinuedprocessingtaskrequest/resources.md) enumeration indicates optional system resources that a specific [BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md) instance can request through its [requiredResources](../bgcontinuedprocessingtaskrequest/requiredresources.md) property.

Before requesting a resource, check this property to ensure that the device supports it.
