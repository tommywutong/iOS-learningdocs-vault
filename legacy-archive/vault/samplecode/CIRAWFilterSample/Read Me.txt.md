---
title: CIRAWFilterSample
apple_id: DTS40009217
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2009-09-08'
source_url: https://developer.apple.com/library/archive/samplecode/CIRAWFilterSample/Listings/Read_Me_txt.html
archived_at: '2026-07-18T03:02:41.067121Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CIRAWFilterSample](CIRAWFilterSample.md)


[Next](Document%20Revision%20History.md)[Previous](ImageWindowController.m.md)

# Read Me.txt

```
Copyright © 2004-2009 by Apple, Inc.  All Rights Reserved.

CIRAWFilterSample

The CIRAWFilter sample is a document based Cocoa application that showcases the use of the CIRAWFilter.

It uses a stack of Core Image filters to display an image. The first filter in the stack is a CIRAWFilter and the UI lets the user add additional CIFilters.

The example makes vast use of bindings (KVC and KVO) to keep the code concise. This illustrates how to use CIFilter instances' support for KVC and KVO. Note that the above mentioned filter stack's last filter is inserted into an NSObserver subclass to keep track of changes to the final output image.
```

[Next](Document%20Revision%20History.md)[Previous](ImageWindowController.m.md)

