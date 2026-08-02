---
title: EgretWakeup
apple_id: DTS10000017
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/EgretWakeup/Listings/EgretWakeUp_a.html
archived_at: '2026-07-18T03:07:32.815724Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EgretWakeup](EgretWakeup.md)


[Next](EgretWakeUpEqu.a.md)[Previous](EgretWakeup.md)

# EgretWakeUp.a

```
;________________________________________________________________________________________________
;  File:  EgretWakeUp.a
;  11/02/93 DTS
;________________________________________________________________________________________________

            BLANKS      ON
            STRING      ASIS

            PRINT       OFF

            MACHINE     MC68020

            INCLUDE     'EgretWakeUpEqu.a'
            INCLUDE     'Traps.a'

            PRINT       ON


;________________________________________________________________________________________________
;  PROCEDURE SetEgretWakeUpTime(WakeUpWhen: LONGINT);
;
;   This external Pascal procedure calls the egret trap set a wake up time for the IIsi.
;
;   Input arguments:    (on stack) Wake up time in seconds
;   Returns:            nothing
;   Destroys:           a1
;________________________________________________________________________________________________

SetEgretWakeUpTime  PROC    EXPORT                          ;it's a procedure, make it visible to outside


BuildPB     move.l  a0, -(sp)                               ;save a0
            sub.l   #EgretPB.EgretPBSize,sp                 ;make a param block on stack
            move.l  sp, a0                                  ;point a0 to pb

;fill in the parameter block

            move.b  #pseudoPkt,     EgretPB.pbCmdType(a0)
            move.b  #WrPwrupTime,   EgretPB.pbCmd(a0)
            move.l  4(a7),          EgretPB.pbParam(a0)     ;copy wake up time to pb.
            clr.w                   EgretPB.pbByteCnt(a0)   ;Power Up CDEV does this (instead of 
                                                            ;move.w #4, EgretPB.pbByteCnt(a0)
            clr.l                   EgretPB.pbBufPtr(a0)
            clr.b                   EgretPB.pbFlags(a0)
            clr.b                   EgretPB.pbSpareFlags(a0)
            clr.w                   EgretPB.pbResult(a0)
            clr.l                   EgretPB.pbCompletion(a0)

            _EgretDispatch

            add.l   #EgretPB.EgretPBSize,sp                 ;strip pb off stack

returnToCaller
            move.l  (sp)+,a0                                ;Restore a0
            move.l  (sp)+,a1                                ;pop return address
            add.l   #4,sp                                   ;kill input argument (wake up time)
            jmp     (a1)                                    ;return
            ENDPROC


            END
```

[Next](EgretWakeUpEqu.a.md)[Previous](EgretWakeup.md)

