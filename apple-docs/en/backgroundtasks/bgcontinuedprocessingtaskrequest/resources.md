---
title: BGContinuedProcessingTaskRequest.Resources
framework: Background Tasks
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources.json'
content_hash: 'sha256:225787a1f24f46a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md)

# BGContinuedProcessingTaskRequest.Resources

<sub>Structure</sub>

Options that specify additional system resources a background task needs.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct Resources
```

## Overview

The following properties are of this type:

- Continuous Background Task request ([BGContinuedProcessingTaskRequest](../bgcontinuedprocessingtaskrequest.md)) property [requiredResources](requiredresources.md).
- [BGTaskScheduler](../bgtaskscheduler.md) property [supportedResources](../bgtaskscheduler/supportedresources.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Identiying a resource

- [BGContinuedProcessingTaskRequestResourcesGPU](resources/gpu.md) — An option that indicates a long-running task requires the GPU.

### Creating a resource

- [init(rawValue:)](<resources/init(rawvalue_).md>) — Initializes a required resource for a Continuous Background Task by raw value.

## See Also

### Identifying resource dependencies

- [requiredResources](requiredresources.md) — An option that indicates any special system resources that the task requires.
