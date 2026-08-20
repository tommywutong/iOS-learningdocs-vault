---
title: Get Ethernet Address
apple_id: DTS10000232
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Get_Ethernet_Address/Listings/CallLAPMgr_a.html
archived_at: '2026-07-18T03:10:49.763755Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Get Ethernet Address](Get%20Ethernet%20Address.md)


[Next](GetEAddr.c.md)[Previous](Get%20Ethernet%20Address.md)

# CallLAPMgr.a

```
;*******************
;File: CallLAPMgr.a
;*******************
; C prototype 
; pascal long CallLAPMgr(short selector);
; Pascal prototype
; Function CallLAPMgr(selector : integer): longint;
*******************
LAPMgrPtr   EQU         $B18        ; This points to our start (???ATalkHk2?)
LAPMgrCall  EQU         2           ; Offset to make LAP manager calls

CallLAPMgr  PROC    EXPORT
        LINK        A6,#0           ; set up stack frame
        MOVE.W      8(A6),D0        ; move selector parameter into D0
        MOVE.L      A2,-(A7)        ; store A2 on stack
        MOVEA.L     LAPMgrPtr,A2    ; Set A2 to address of LAP Mgr.
        JSR         LAPMgrCall(A2)  ; Call LAP Manager
        MOVE.L      D1,$A(A6)       ; Place result onto stack
        MOVE.L      (A7)+,A2        ; Restore A2
        UNLK        A6              ; restore stack frame
        MOVEA.L     (A7)+,A0        ; put return address into A0
        ADDQ.W      #$2,A7          ; clear off the parameter
        JMP         (A0)            ; return to caller
        RTS
        ENDP

        END
;*******************
;End of file
;*******************
```

[Next](GetEAddr.c.md)[Previous](Get%20Ethernet%20Address.md)

