---
title: AEObject-Edition Sample
apple_id: DTS10000204
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEObject-Edition_Sample/Listings/AEObject_Edition_Sample_r.html
archived_at: '2026-07-18T02:59:28.397849Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEObject-Edition Sample](AEObject-Edition%20Sample.md)


[Next](AEObject.c.md)[Previous](main.c.md)

# AEObject-Edition Sample.r

```
/* Our Rez file.  All this does is include the .rsrc file that contains the */
/* compiled resources */

type 'ERST' {
       integer = $$CountOf(ErrorArray); /*                */
       array ErrorArray {
           integer;                      /* error number */
           pstring;                    /* and the string       */
       };
};

include "AESamp.rsrc";
```

[Next](AEObject.c.md)[Previous](main.c.md)

