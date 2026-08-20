---
title: CullGroupSample
apple_id: DTS10000133
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CullGroupSample/Listings/Headers_3dmf_h.html
archived_at: '2026-07-18T03:05:31.149238Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CullGroupSample](CullGroupSample.md)


[Next](Headers-main.h.md)[Previous](CullGroupSample.md)

# Headers/3dmf.h

```c
//
// 3dmf.h
//

#include "qd3d_support.h"

extern  TQ3Object   Load3DMFModel(FSSpec *inFile);
extern  void Save3DMFModel(QD3DSetupOutputType *setupInfo,FSSpec *outFile, void (*callBack)(QD3DSetupOutputType *));
```

[Next](Headers-main.h.md)[Previous](CullGroupSample.md)

