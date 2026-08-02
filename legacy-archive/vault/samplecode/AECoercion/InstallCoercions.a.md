---
title: AECoercion
apple_id: DTS10000202
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/AECoercion/Listings/InstallCoercions_a.html
archived_at: '2026-07-18T02:59:26.791765Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AECoercion](AECoercion.md)


[Next](InstallCoercions.c.md)[Previous](Coercions.c.md)

# InstallCoercions.a

```
;------------------------------------------------------------------------------
;
;   Apple Macintosh Developer Technical Support
;
;   Sample AppleEventª Coercion Handler Installing INIT
;   File:       InstallCoercions.a - Asm source
;   By: C.K. Haun <TR>
;   Copyright © 1991 Apple Computer, Inc.
;   All rights reserved.
;
;------------------------------------------------------------------------------
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;
;   Generic install routine. This is the code that gets executed when INIT 31
;   calls our INIT. The first thing we do is check to see if any of the scare
;   buttons are being pressed. If the user is holding the mouse button, 
;   then don't install, and show the unhappy icon. 
;   If the shift key is down, System 7 has already disallowed extensions,
;   so we don't need to double-check (since we're 7.0 only)
;   The we jump to the C routines that do the actual work.
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



                include 'ToolEqu.a'
                include 'SysEqu.a'
                include 'QuickEqu.a'
                include 'Traps.a'

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;   These are the IDs for the icons used by ShowINIT. ShowINIT is a really
;   cool hack by Paul Mercer that displays those icons across the bottom of
;   your screen when you boot up. You can choose what icon to show up, based
;   on how the installation went. If the installation went OK, we show the
;   INIT's icon.  If the installation didn't work, we
;   show a version of the icon with an X through it. 
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

IconID          EQU     128
BadIconID       EQU     129

INITInstall     PROC    EXPORT
                IMPORT  SHOWINIT
                IMPORT  cInstall:CODE
                tst.b   MBState                 ; don't install if mouse button is down
                bpl.s   NoInstall               ;
                bsr cInstall                    ; call cInstall to install the handlers
                tst.w   D0                      ; any errors?
                bne.s   NoInstall           ; yes, show bad icon
ExitInit
                move.w  #IconID,-(sp)           ; ICN# ID of happy icon
                bra.s   ShowTheIcon             ;
NoInstall
                move.w  #BadIconID,-(sp)        ; ICN# ID of unhappy icon
ShowTheIcon
                move.w  #-1,-(sp)               ; use default moveX
                bsr     SHOWINIT                ; draw the icon
                rts                             ; return to INIT 31
                ENDP
                END
```

[Next](InstallCoercions.c.md)[Previous](Coercions.c.md)

