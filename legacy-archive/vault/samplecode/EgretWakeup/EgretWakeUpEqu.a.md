---
title: EgretWakeup
apple_id: DTS10000017
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/EgretWakeup/Listings/EgretWakeUpEqu_a.html
archived_at: '2026-07-18T03:07:32.759758Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EgretWakeup](EgretWakeup.md)


[Next](Document%20Revision%20History.md)[Previous](EgretWakeUp.a.md)

# EgretWakeUpEqu.a

```
                Eject
************************************************************************
;           EGRET Manager Equates
;
;   File:       EgretWakeUp.a
;
;   Contains:   Some Equate definitions used by EgretMgr.a 
;
;   11/02/93 DTS
************************************************************************

    IF &TYPE('__Includingegretequ__') = 'UNDEFINED' THEN
__Includingegretequ__   SET 1
;
;                           Egret parameter block
;

EgretPB     RECORD      0,increment
pbCmdType       ds.b    1               ; command type
pbCmd           ds.b    1               ; Egret command
pbParam         ds.b    4               ; Generic parameter (Addr, Time, etc), if needed for this command
pbByteCnt       ds.w    1               ; # bytes of send/rcv data, if needed for this command
pbBufPtr        ds.l    1               ; ptr to send/receive data, if any
pbFlags         ds.b    1               ; Egrets flags (from response packet)
pbSpareFlags    ds.b    1               ; 
pbResult        ds.w    1               ; result code (if any)
pbCompletion    ds.l    1               ; ptr to completion routine
EgretPBSize     EQU     *
            ENDR


;________________________________________________________________________________________________
;                       Packet types
pseudoPkt       EQU     $0001           ; pseudo commands packet type

;________________________________________________________________________________________________
;                       Pseudo commands
WrPwrupTime     equ     $0B             ; Set powerup time


    ENDIF   ; ...already included
```

[Next](Document%20Revision%20History.md)[Previous](EgretWakeUp.a.md)

