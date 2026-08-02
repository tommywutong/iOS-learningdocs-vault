---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/UtilCode_GrafUtils_h.html
archived_at: '2026-07-18T03:28:34.912837Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](UtilCode-GWorldUtils.c.md)[Previous](UtilCode-GrafUtils.c.md)

# UtilCode/GrafUtils.h

```
#pragma once



GWorldPtr PictureToGWorld(PicHandle pict, int gdepth);
PixMapHandle PreserveGraf(GWorldPtr newPort);
void RestoreGraf(void);

#define RECT_WD(rekt) ((rekt).right - (rekt).left)
#define RECT_HT(rekt) ((rekt).bottom - (rekt).top)
```

[Next](UtilCode-GWorldUtils.c.md)[Previous](UtilCode-GrafUtils.c.md)

