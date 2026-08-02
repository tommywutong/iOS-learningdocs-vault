---
title: ATP Demo
apple_id: DTS10000228
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ATP_Demo/Listings/PreCompletion_a.html
archived_at: '2026-07-18T02:59:45.299783Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ATP Demo](ATP%20Demo.md)


[Next](Document%20Revision%20History.md)[Previous](ATP.c.md)

# PreCompletion.a

```

    CASE    ON

PreCompletion   PROC    EXPORT

    LINK    A6,#0               ; Link for the debugger.
    MOVEM.L A5,-(SP)            ; Preserve A5 register.

    MOVE.L  A0, -(SP)           ; Pass PB pointer as the parameter.
    MOVE.L  -8(A0),A5           ; Set A5 to passed value (ourA5).
    MOVE.L  -4(A0),A0           ; A0 = real completion routine address.
    JSR     (A0)                ; Transfer control to ourCompletion.

    MOVEM.L (SP)+,A5            ; Restore A5 register.
    UNLK    A6                  ; Unlink.
    RTS                         ; Return.

    STRING  ASIS                ; The debugger string.
    DC.B    $8D,'PreCompletion'
    DC.W    $0000
    STRING  PASCAL

    ENDP

    END
```

[Next](Document%20Revision%20History.md)[Previous](ATP.c.md)

