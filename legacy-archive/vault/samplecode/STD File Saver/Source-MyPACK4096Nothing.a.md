---
title: STD File Saver
apple_id: DTS10000307
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/STD_File_Saver/Listings/Source_MyPACK_4096_Nothing_a.html
archived_at: '2026-07-18T03:22:47.725430Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [STD File Saver](STD%20File%20Saver.md)


[Next](Source-MyPDEF0DraftMode.a.md)[Previous](Source-MyPACK4096.c.md)

# Source/MyPACK_4096_Nothing.a

```
;
; Copyright 1991-1996 Apple Computer. All rights reserved.
;
;   You may incorporate this sample code into your applications without
;   restriction, though the sample code has been provided "AS IS" and the
;   responsibility for its operation is 100% yours.  However, what you are
;   not permitted to do is to redistribute the source as "DSC Sample Code"
;   after having made changes. If you're going to re-distribute the source,
;   we require that you make it clear in the source that the code was
;   descended from Apple Sample Code, but that you've made changes.
;

 IF &TYPE('__INCLUDINGTRAPS__') = 'UNDEFINED' THEN
 INCLUDE 'Traps.a'
 ENDIF

MYPACK  PROC    EXPORT
    IMPORT  CHOOSERMAIN

    BRA.S   @1
    DC.W    $5346   ; 'SF' - device ID
    DC.L    $5041434B   ; this means PACK - don't change
    DC.W    $F000   ; -4096 - don't change this
    DC.W    $0201   ; version 2.1
    DC.L    $0C13F800   ; flags - see below
;
; Description of flags word
;
; Bit   hex meaning
; ---           --- -------
; 31    $80000000   IsAppleTalkDevice
; 30-29 n/a reserved (always 0)
; 28    $10000000   PACK is reentrant
; 27    $08000000   usesLeftButton
; 26    $04000000   usesRightButton
; 25    $02000000   noSavedZoneName
; 24    $01000000   usesZoneNames
; 23-21 n/a reserved (always 0)
; 20    $00100000   usesRadioButtons (and label)
; 19-18 n/a reserved (always 0)
; 17    $00020000   acceptsChooserInitMsg
; 16    $00010000   acceptsNewSelMsg
; 15    $00008000   acceptsFillListMsg
; 14    $00004000   acceptsGetSelMsg
; 13    $00002000   acceptsSelectMsg
; 12    $00001000   acceptsDeselectMsg
; 11    $00000800   acceptsTerminateMsg
; 10-0  n/a reserved (always 0)
;
@1  
    JMP CHOOSERMAIN

    ENDPROC
    END
```

[Next](Source-MyPDEF0DraftMode.a.md)[Previous](Source-MyPACK4096.c.md)

