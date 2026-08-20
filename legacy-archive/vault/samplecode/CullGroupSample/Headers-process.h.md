---
title: CullGroupSample
apple_id: DTS10000133
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CullGroupSample/Listings/Headers_process_h.html
archived_at: '2026-07-18T03:05:31.548670Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CullGroupSample](CullGroupSample.md)


[Next](Headers-QD3DSupport.h.md)[Previous](Headers-objects.h.md)

# Headers/process.h

```
//
// process.h
//

#define NUM_TEST    5
enum
{
    TEST_TRIMESH,
    TEST_SPHERE,
    TEST_TORUS
};


extern  void InitTest(void);
extern  void DoModelWindowNullEvent(void);
extern  void UpdateModelWindow(void);
extern  void DrawModelWindow(void);
extern  void BuildCurrentTest(void);
```

[Next](Headers-QD3DSupport.h.md)[Previous](Headers-objects.h.md)

