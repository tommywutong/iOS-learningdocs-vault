---
title: BGContinuedProcessingTaskRequestResourcesDefault
framework: Background Tasks
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequestresources/bgcontinuedprocessingtaskrequestresourcesdefault
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequestresources/bgcontinuedprocessingtaskrequestresourcesdefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequestresources/bgcontinuedprocessingtaskrequestresourcesdefault.json'
content_hash: 'sha256:2be566e0d962671b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Background Tasks](../../backgroundtasks.md) · [Resources](../bgcontinuedprocessingtaskrequest/resources.md)

# BGContinuedProcessingTaskRequestResourcesDefault

<sub>Enumeration Case</sub>

An option for a task with no additional required system resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
BGContinuedProcessingTaskRequestResourcesDefault
```

## Discussion

Unless informed otherwise, the scheduler assumes the default resources, allowing background CPU and network access.

## See Also

### Identiying a resource

- [BGContinuedProcessingTaskRequestResourcesGPU](../bgcontinuedprocessingtaskrequest/resources/gpu.md) — An option that indicates a long-running task requires the GPU.
