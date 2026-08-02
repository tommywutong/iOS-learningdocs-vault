---
title: Implementing optional methods of the IKImageBrowserItem Protocol
apple_id: DTS40011164
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2011-07-22'
source_url: https://developer.apple.com/library/archive/qa/qa1746/_index.html
archived_at: '2026-07-18T02:34:32.672506Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1746

# Implementing optional methods of the IKImageBrowserItem Protocol

## Q:  I have implemented the optional `imageSubtitle` method of the `IKImageBrowserItem` Protocol, but it is not being called. Is there something else that needs to be done for this method to be invoked?

A: You must enable the cell's subtitles using the `setCellsStyleMask` method:

`- (void)setCellsStyleMask:(NSUInteger)mask`

This method defines the appearance style of the cells. The mask parameter is an integer mask of the cell appearance styles (shadow / outline / title / subtitle). The mask for subtitles is `IKCellsStyleSubtitled`. You must specify this mask in order for the subtitles to appear. Here's an example usage:

__Listing 1__  Setting the appearance style of the cells.

```objc
#import <Quartz/Quartz.h>  IKImageBrowserView *imageBrowser = <#Your IKImageBrowserView instance#>; [imageBrowser setCellsStyleMask:IKCellsStyleTitled | IKCellsStyleOutlined                           | IKCellsStyleSubtitled];
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-22 | New document that shows how to implement optional methods of the IKImageBrowserItem Protocol. |

