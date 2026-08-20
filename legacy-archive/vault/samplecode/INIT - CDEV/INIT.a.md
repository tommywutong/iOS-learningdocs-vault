---
title: INIT - CDEV
apple_id: DTS10000187
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/INIT_-_CDEV/Listings/INIT_a.html
archived_at: '2026-07-18T03:12:04.660230Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [INIT - CDEV](INIT%20-%20CDEV.md)


[Next](INIT.c.md)[Previous](Common.h.md)

# INIT.a

```
*------------------------------------------------------------------------------
*
*   Apple Macintosh Developer Technical Support
*
*   Sample Control Panel Device and INIT Combination
*
*   Program:    INIT - CDEV
*   File:       INIT.a  -   Asm Source
*
*   Copyright © 1990 Apple Computer, Inc.
*   All rights reserved.
*
*------------------------------------------------------------------------------

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;   void a_SystemTask()
;
;   This is the real patch to SystemTask(). It saves all registers that
;   shouldn't be tampered with, calls the C routine that does all the dirty
;   work, and restores the registers. It then pushes the address of the
;   real ROM SystemTask routine onto the stack and RTS, which is a neat
;   way to jump to that routine without messing up any registers.
;
;   "oldSystemTask" is filled in during INIT initialization by the routine
;   INITInstall.
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

a_SystemTask    PROC    EXPORT
                IMPORT  c_SystemTask:CODE
                EXPORT  oldSystemTask

                movem.l D0-D7/A0-A5,-(sp)       ; Save our registers
                bsr     c_SystemTask            ; call the C routine
                movem.l (sp)+,D0-D7/A0-A5       ; restore the registers
                move.l  oldSystemTask,-(sp)     ; push addr. of orig. SystemTask
                rts                             ; RTS will just jump to it.

oldSystemTask   ds.l    1                       ; address of original SystemTask

                ENDP


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;   void a_SetA5Ref(A5Ref)
;
;       Simply takes the value passed in and saves it in "A5Storage". This
;       routine uses the C calling convetion, so it doesn't need to pull
;       and parameters off of the stack.
;
;   long a_GetA5Ref()
;
;       Returns the value stored in "A5Storage". This routine uses the C
;       callin convention, so the result is returned in D0.
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

a_SetA5Ref      PROC    EXPORT
                EXPORT  a_GetA5Ref

                lea     A5Storage,A0            ; get address of storage
                move.l  4(sp),(A0)              ; move value to save into it
                rts                             ; return to caller

a_GetA5Ref
                move.l  A5Storage,D0            ; get result into D0
                rts                             ; return to caller

A5Storage       ds.l    1                       ; storage for A5 reference

                ENDP

                END
```

[Next](INIT.c.md)[Previous](Common.h.md)

