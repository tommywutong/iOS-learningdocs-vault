---
title: CPlusTESample
apple_id: DTS10000730
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CPlusTESample/Listings/TESampleGlue_a.html
archived_at: '2026-07-18T03:02:44.085987Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CPlusTESample](CPlusTESample.md)


[Next](UMAFailure.a.md)[Previous](TESample.r.md)

# TESampleGlue.a

```
; ==========================================================================================
;
;   Program:    CPlusTESample 2.0
;   Files:      TESampleGlue.a
;
;   by Mark Bennett
;   of Apple Macintosh Developer Technical Support
;
;   Copyright © 1989-1990 Apple Computer, Inc.
;   All rights reserved.
;
; ==========================================================================================

;
;   AsmClickLoop
;
;   This routine gets called by the TextEdit Manager from TEClick.
;   It calls the old, default click loop routine that scrolls the
;   text, and then calls our own Pascal routine that handles
;   tracking the scroll bars to follow along.  It doesn't bother
;   with saving registers A0 and D0, because they are trashed
;   anyway by TextEdit.
;

AsmClickLoop    PROC        EXPORT

            IMPORT      GETOLDCLICKLOOP
            IMPORT      PASCALCLICKLOOP

            MOVEM.L     D1-D2/A1,-(SP)      ; D0 and A0 need not be saved

            CLR.L       -(SP)               ; make space for procedure pointer
            JSR         GETOLDCLICKLOOP     ; get the old clickLoop
            MOVEA.L     (SP)+,A0            ; into A0

            MOVEM.L     (SP)+,D1-D2/A1      ; restore the world as it was
            JSR         (A0)                ; and execute old clickLoop

            MOVEM.L     D1-D2/A1,-(SP)      ; D0 and A0 need not be saved
            JSR         PASCALCLICKLOOP     ; do our clickLoop
            MOVEQ       #1,D0               ; clear the zero flag so TextEdit keeps going
            MOVEM.L     (SP)+,D1-D2/A1      ; restore the world as it was
            RTS

            END
```

[Next](UMAFailure.a.md)[Previous](TESample.r.md)

