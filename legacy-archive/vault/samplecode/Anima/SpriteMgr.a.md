---
title: Anima
apple_id: DTS10000065
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Anima/Listings/SpriteMgr_a.html
archived_at: '2026-07-18T03:01:00.293877Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Anima](Anima.md)


[Next](SpriteMgr.c.md)[Previous](AnimationTest.c.md)

# SpriteMgr.a

```


    STRING ASIS
    INCLUDE 'SysEqu.a'

VTASK   PROC    EXPORT

    move.w #1,10(a0)        ; reset vblCount
    move.w #1,14(a0)        ; set our global marker
    rts                     ; return to OS


    ENDP



    END
```

[Next](SpriteMgr.c.md)[Previous](AnimationTest.c.md)

