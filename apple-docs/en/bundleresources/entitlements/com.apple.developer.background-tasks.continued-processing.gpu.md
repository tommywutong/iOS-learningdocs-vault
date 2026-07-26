---
title: Background GPU Access
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu.json'
content_hash: 'sha256:15749c83eb845dd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Background GPU Access

<sub>Property List Key</sub>

The entitlement the system requires for a continuous background task to use the GPU.

## Discussion

This entitlement works with [BGContinuedProcessingTask](../../backgroundtasks/bgcontinuedprocessingtask.md), which allows your app’s critical work to complete even when the app goes into the background before the task finishes.

To enable GPU use in the task, add this entitlement to your app by adding the Background GPU Access capability to your target in Xcode. For more information, see [Adding capabilities to your app](../../xcode/adding-capabilities-to-your-app.md).

For more information about continuous background tasks, see [Performing long-running tasks on iOS and iPadOS](../../backgroundtasks/performing-long-running-tasks-on-ios-and-ipados.md).

## See Also

### Background tasks

- [Background Inference](com.apple.developer.background-tasks.continued-processing.inference.md) — An entitlement that lets a background task run inference on the Neural Engine. _(beta)_
