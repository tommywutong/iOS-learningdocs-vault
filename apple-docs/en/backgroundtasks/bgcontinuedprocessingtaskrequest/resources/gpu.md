---
title: gpu
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources/gpu
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources/gpu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources/gpu.json'
content_hash: 'sha256:c4e84268c5a5bdbb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Background Tasks](../../../backgroundtasks.md) · [BGContinuedProcessingTaskRequest](../../bgcontinuedprocessingtaskrequest.md) · [Resources](../resources.md)

# gpu

<sub>Type Property</sub>

An option that indicates a long-running task requires the GPU.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var gpu: BGContinuedProcessingTaskRequest.Resources { get }
```

## Discussion

The system requires your app to have the [Background GPU Access](../../../bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu.md) entitlement with a value of `true` to use the GPU in the background. To do that, enable the Background GPU Access capability on your app’s target. For more information about capabilities in Xcode, see [Adding capabilities to your app](../../../xcode/adding-capabilities-to-your-app.md).

Not all devices support background GPU use. For more information, see [Performing long-running tasks on iOS and iPadOS](../../performing-long-running-tasks-on-ios-and-ipados.md).
