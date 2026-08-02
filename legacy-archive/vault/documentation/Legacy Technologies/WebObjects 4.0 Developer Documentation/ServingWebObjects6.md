---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects6.html
archived_at: '2026-07-18T01:23:53.132657Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](Deploying%20With%20the%20Monitor%20Application.md)

## Starting Up Monitor

To start up Monitor, do the following:

- Open a command shell window.

Use __Terminal.app__ on Mac OS X Server and the Bourne Shell program on Windows NT.

- If you are on a Mac OS X Server (or similar) system, __su__ to root.
- Change directories to the location where WebObjects is installed (such as __/System__ on Mac OS X Server and __C:\Apple__ on Windows NT).
- Enter the following commands:

```
cd Library/WebObjects/Applications/Monitor.woa
Monitor
```


If you start Monitor on Windows NT platforms by double-clicking the icon in the Windows Explorer program, any application instances started with that Monitor are terminated when the Monitor instance itself terminates (which usually occurs when the Command-Prompt window is closed or upon failure).
When the Monitor application launches, it usually opens the default web browser and displays the Applications Page by default:
!

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects7.md)
