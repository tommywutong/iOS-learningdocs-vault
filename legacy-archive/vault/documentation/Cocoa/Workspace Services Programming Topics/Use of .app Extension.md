---
title: Workspace Services Programming Topics
apple_id: 10000100i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2009-06-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/AppExtensions.html
archived_at: '2026-07-15T07:21:20.485253Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Workspace Services Programming Topics](Introduction%20to%20Workspace%20Services.md)


[Next](Retrieving%20Information%20About%20Files.md)[Previous](About%20Workspace%20Services.md)

# Use of .app Extension

One of the ways OS X determines if a package is an application is through the use of file extensions. The rules to determine if a package is an application are:

- On all file systems: the presence of a `.app` suffix
- On HFS+ only: the `.app` suffix is optional, if the package bit is set and the folder contains a new style `info.xml`.

[Next](Retrieving%20Information%20About%20Files.md)[Previous](About%20Workspace%20Services.md)

