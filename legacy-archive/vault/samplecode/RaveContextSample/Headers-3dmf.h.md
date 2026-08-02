---
title: RaveContextSample
apple_id: DTS10000156
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RaveContextSample/Listings/Headers_3dmf_h.html
archived_at: '2026-07-18T03:21:50.411818Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RaveContextSample](RaveContextSample.md)


[Next](Headers-misc.h.md)[Previous](RaveContextSample.md)

# Headers/3dmf.h

```c
//
// 3dmf.h
//

#include "qd3d_support.h"

extern  TQ3Object   Load3DMFModel(FSSpec *inFile);
extern  void Save3DMFModel(QD3DSetupOutputType *setupInfo,FSSpec *outFile, void (*callBack)(QD3DSetupOutputType *));
```

[Next](Headers-misc.h.md)[Previous](RaveContextSample.md)

