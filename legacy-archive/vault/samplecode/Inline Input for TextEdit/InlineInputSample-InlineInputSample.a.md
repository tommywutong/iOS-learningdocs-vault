---
title: Inline Input for TextEdit
apple_id: DTS10001094
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Inline_Input_for_TextEdit/Listings/InlineInputSample_InlineInputSample_a.html
archived_at: '2026-07-18T03:12:55.326525Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Inline Input for TextEdit](Inline%20Input%20for%20TextEdit.md)


[Next](InlineInputSample-InlineInputSample.c.md)[Previous](Inline%20Input%20for%20TextEdit.md)

# InlineInputSample/InlineInputSample.a

```
;
;   File:       InlineInputSample.a
;
;   Contains:   68K Assembly source file for InlineInputSample
;
;   Copyright:  © 1989, 1993 Apple Computer, Inc. All rights reserved.


;
;   AsmClickLoopProc
;
;   This routine gets called by the TextEdit Manager from TEClick.
;   It calls the old, default click loop routine that scrolls the
;   text, and then calls our own Pascal routine that handles
;   tracking the scroll bars to follow along.  It doesn't bother
;   with saving registers A0 and D0, because they are trashed
;   anyway by TextEdit.
;

AsmClickLoopProc    PROC        EXPORT

            IMPORT      GETOLDCLICKLOOP
            IMPORT      CLICKLOOPADDON

            MOVEM.L     D1-D2/A1,-(SP)      ; D0 and A0 need not be saved
            CLR.L       -(SP)               ; make space for procedure pointer
            JSR         GETOLDCLICKLOOP     ; get the old clikLoop
            MOVEA.L     (SP)+,A0            ; into A0
            MOVEM.L     (SP)+,D1-D2/A1      ; restore the world as it was

            JSR         (A0)                ; and execute old clikLoop

            MOVEM.L     D1-D2/A1,-(SP)      ; D0 and A0 need not be saved
            JSR         CLICKLOOPADDON      ; do our clikLoop
            MOVEM.L     (SP)+,D1-D2/A1      ; restore the world as it was
            MOVEQ       #1,D0               ; clear the zero flag so TextEdit keeps going
            RTS

            END 
```

[Next](InlineInputSample-InlineInputSample.c.md)[Previous](Inline%20Input%20for%20TextEdit.md)

