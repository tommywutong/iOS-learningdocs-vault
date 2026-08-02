---
title: BlitVBL
apple_id: DTS10000488
resource_type: Sample Code
platform: macOS
topic: Performance
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BlitVBL/Listings/BlitVBL_Read_Me_txt.html
archived_at: '2026-07-18T03:02:08.401661Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BlitVBL](BlitVBL.md)


[Next](main.r.md)[Previous](main.h.md)

# BlitVBL Read Me.txt

```
BlitVBL
Version 1.0
6/22/2001



What is BlitVBL?

The BlitVBL sample shows how to have Mac OS X try its best to sync to the VBL for you.  Note that it is not possible in all cases to sync to the VBL.  Some hardware and drivers don't have the concept of a beam position or have a very short or non-existent vertical blank.  See the separate BlitNoVBL sample to see how to draw directly to the screen without syncing to the VBL of the monitor.

Note the use of QDFlushPortBuffer in the timer callback.  QDFlushPortBuffer flushes a portion of the port's back buffer to the screen synced to the VBL where possible.

If you have any feedback regarding this sample, please see <http://developer.apple.com/contact/feedback.html>.
```

[Next](main.r.md)[Previous](main.h.md)

