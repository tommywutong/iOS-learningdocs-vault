---
title: On-Demand Resources Guide
apple_id: TP40015083
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: Foundation
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/AboutDesigningODR.html
archived_at: '2026-07-15T07:32:02.297420Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [On-Demand Resources Guide](index.md)



## General Design Principles

The goal of designing for on-demand resources is to create an app that provides optimum content and functionality with a responsive user experience. On-demand resources provide the content. Keeping the app responsive requires that you design the tags and and content requests so that resources:

- Are available when needed
- Have minimal impact during download
- Have minimal impact on app memory

### Four General Design Principles

Designing any app for on-demand resources follows four general design principles:

- Download what you need.
- Download early.
- Release resources when you are done.
- Optimize with testing.

Some types of apps have additional design considerations; see [Patterns of On-Demand Resource Use](PreservingDownloadedResources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmrsfvjvomi).

For information on using testing to optimize on-demand resource use, see [Optimization with Testing](TestingPerformance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmrrfvjvomi).

### Download What You Need

Optimize the number and size of tags to download only the resources you need. For most apps, the target size for a tag is 64 MB. Smaller tag sizes provide a few benefits:

- Faster download times
- Best use of the maximum memory size for on-demand resources
- Best flexibility for preserving cached resources

### Download Early

Downloading early means required resources have the best chance of being ready when the user needs them. Downloading early also minimizes the impact on app performance.

Designing for early download means balancing the time taken to download the required resources and the total amount of on-demand resources in use at any time.

### Release When Done

Releasing resources when you have finished with them keeps the maximum amount of on-demand resource memory space open. System caching means that you can usually access previously downloaded resources without requiring another download.

[Generating Hosted Asset Packs](GeneratingHostedContent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmjzfvjvomi)

[Optimization with Testing](TestingPerformance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmrrfvjvomi)
