---
title: CompressedPixmapSample
apple_id: DTS10000132
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CompressedPixmapSample/Listings/Headers_3dmf_h.html
archived_at: '2026-07-18T03:04:10.056228Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CompressedPixmapSample](CompressedPixmapSample.md)


[Next](Headers-misc.h.md)[Previous](CompressedPixmapSample.md)

# Headers/3dmf.h

```c
//
// 3dmf.h
//
#include <Files.h>

#include "qd3d_support.h"

extern  TQ3Object   Load3DMFModel(FSSpec *inFile);
extern  void Save3DMFModel(QD3DSetupOutputType *setupInfo,FSSpec *outFile, void (*callBack)(QD3DSetupOutputType *));
```

[Next](Headers-misc.h.md)[Previous](CompressedPixmapSample.md)

