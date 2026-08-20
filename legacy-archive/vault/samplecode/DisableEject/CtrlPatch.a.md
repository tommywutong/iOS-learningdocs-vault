---
title: DisableEject
apple_id: DTS10000014
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DisableEject/Listings/CtrlPatch_a.html
archived_at: '2026-07-18T03:06:59.610544Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DisableEject](DisableEject.md)


[Next](Document%20Revision%20History.md)[Previous](DisableEject.md)

# CtrlPatch.a

```
    INCLUDE 'traps.a'
    INCLUDE 'SysEqu.a'
    INCLUDE 'SysErr.a'

Control EQU $A004

PatchIt PROC    EXPORT

    IMPORT  MyCtrl
    IMPORT  OldCtrlPtr
    IMPORT  MyProcEnd

    lea         MyProcEnd,a2
    lea         MyCtrl,a3
    suba.l      a3,a2
    move.l      a2,d0                   ;make a block in the sys heap this big
    _NewPtr     ,SYS
    move.l      a0,d1                   ;keep new ptr around for later, and test it
    beq.s       exit                    ;if nil, give up
    move.l      a0,a1                   ;make a destination ptr
    lea         MyCtrl,a0               ;make a source ptr
    move.l      a2,d0                   ;make how many to move
    _BlockMove                          ;move some bytes

    move.l      d1,a1                   ;get the address of the pointer in sys heap
    move.w      #Control,d0             ;now get the address of the _Control routine
    _GetTrapAddress     ,NEWOS
    move.l      a0,OldCtrlPtr-MyCtrl(a1) ;save it for later

    move.w      #Control,d0             ;set up trap num
    move.l      a1,a0                   ;set up new trap address
    _SetTrapAddress         ,NEWOS      ;install the patch
exit    
    rts

    ENDP

MyCtrl  PROC    EXPORT

    IMPORT  OldCtrlPtr

    cmpi.w      #-5,ioRefNUm(a0)
    bne.s       PassItOn
    cmpi.w      #ejectCode,csCode(a0)
    bne.s       PassItOn
    move.w      IODrvNum(a0),D0             ; keep the drive number for postEvent msg
    move.w      #noErr,ioResult(a0)
    tst.l       ioCompletion(a0)
    beq.s       exit
    movem.l     a0-a1/d0-d2,-(sp)
    move.l      ioCompletion(a0),a1
    jsr         (a1)
    movem.l     (sp)+,a0-a1/d0-d2
exit
    MOVE.L      #diskInsertEvt, A0              ; get event number where it belongs
    _PostEvent                              ; post the event
    rts
PassItOn
    move.l      OldCtrlPtr,-(sp)
    rts

    ENDP

OldCtrlPtr  PROC    EXPORT
        DC.L    0

    ENDP

MyProcEnd   PROC    EXPORT
            ENDP

            END
```

[Next](Document%20Revision%20History.md)[Previous](DisableEject.md)

