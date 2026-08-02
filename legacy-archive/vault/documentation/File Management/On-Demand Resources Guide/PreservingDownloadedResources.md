---
title: On-Demand Resources Guide
apple_id: TP40015083
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: Foundation
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/PreservingDownloadedResources.html
archived_at: '2026-07-15T07:32:10.413548Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [On-Demand Resources Guide](index.md)



## Patterns of On-Demand Resource Use

Most apps access on-demand resources in one of three patterns. Those patterns guide the design approach, shown in column 3 of Table 12-1.

__Table 12-1__Patterns of on-demand resource use

| Name | Example | Access pattern | Design approach |
| --- | --- | --- | --- |
| Random access | Browsing app | No pattern | - Many tags - Small tag sizes - Progressive loading |
| Limited Prediction | Open world game | Access subset based on current app state | - Many tags - Small tag sizes - Progressive loading - Loading subsets based on app state - Quickly ending access to unused tags |
| Linear Progression | Leveled game | Access order highly predictable | - Download in advance - Ending access to tags when done |

- __Many tags.__ Enables downloading only what is needed or might be needed.
- __Small tag sizes.__ Provides several benefits:

  - Faster downloads
  - Optimal app performance
  - Best-use memory limits for on-demand resources
  - Minimized penalty for downloading tags that are not needed
- __Progressive loading.__ Enables a smooth experience by downloading the resources for the next phase of the app as soon as the user starts the current phase.
- __Loading subsets based on the app state.__ Downloads resources for the next likely app states.

  For example, in an open world game the current game location constrains the next set of location resources.
- __Quickly ending access to unused tags.__ Frees up memory for more on-demand resources. This is particularly important for apps that download subsets of resources based current app state.
- __Downloading in advance.__ Enables a smooth progression through the app.

  Linear progression apps tend to have larger amounts of resources associated with each stage. Downloading in advance is important for uninterrupted game play and maximizing performance.
- __Ending access to tags when done.__ Enables more free space for the next stage in a linear progression app.

[Optimization with Testing](TestingPerformance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmrrfvjvomi)
