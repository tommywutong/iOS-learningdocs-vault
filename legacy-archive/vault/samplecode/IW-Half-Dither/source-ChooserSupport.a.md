---
title: IW-Half-Dither
apple_id: DTS10000151
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/IW-Half-Dither/Listings/source_ChooserSupport_a.html
archived_at: '2026-07-18T03:12:11.278656Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IW-Half-Dither](IW-Half-Dither.md)


[Next](source-ChooserSupport.r.md)[Previous](IW-Half-Dither.md)

# source/ChooserSupport.a

```
;  ------------------------------------------------------------------------------
;
;   FILENAME
;       ChooserSupport.a
;
;   DESCRIPTION
;       Contains the code to form the first part of the Chooser 'PACK' for
;       this driver.
;
;   COPYRIGHT
;       Copyright © Apple Computer, Inc. 1992-1994
;       All rights reserved. 
;
;   12/20/93        dmh             Sync'd with the shipping 1.0b3 GX driver.
;
;--------------------------------------------------------------------------------

    STRING  ASIS
    CASE OBJ

kAppleTalkDevice        EQU $80000000
kIsPAPDevice            EQU $40000000
kIsPostScriptDevice     EQU $20000000
kMultiSelect            EQU $10000000
kLeftButton             EQU $08000000
kRightButton            EQU $04000000
kNoSavedZone            EQU $02000000
kActualZoneNames        EQU $01000000
kNoIntlChars            EQU $00800000
kEvenUpName             EQU $00400000
kLengthOnRename         EQU $00200000
kUsesOnAndOff           EQU $00100000
kNoSetSelfSend          EQU $00080000
kUnused18               EQU $00040000
kAcceptsInit            EQU $00020000
kAcceptsNewSel          EQU $00010000
kAcceptsFillList        EQU $00008000
kAcceptsGetSel          EQU $00004000
kAcceptsSelect          EQU $00002000
kAcceptsDeselect        EQU $00001000
kAcceptsTerminate       EQU $00000800

    IMPORT DEVICE                               ; from ChooserSupport.c
EntryPoint  PROC EXPORT
        BRA.S   code                            ; branch to our actual code
        DC.W    169                             ; device ID
        DC.L    'PACK'                          ; device Type
        DC.W    $F000                           ; master ID for resources (-4096)
        DC.W    2                               ; version
        DC.L    kLeftButton+kUsesOnAndOff+kAcceptsInit+kAcceptsTerminate    ; flags

data:
    ds.b    38              ; sizeof(PACKglobalRec)
code:
    MOVE.L  (a7)+,a0        ; move return address into a0
    PEA     data            ; add a pointer to our global data onto stack as last parameter
    MOVE.L  a0,-(a7)        ; put the return address back on the stack
    jmp     DEVICE          ; jump to it, so when it does the return, it goes to OUR caller
    rts

    END
```

[Next](source-ChooserSupport.r.md)[Previous](IW-Half-Dither.md)

