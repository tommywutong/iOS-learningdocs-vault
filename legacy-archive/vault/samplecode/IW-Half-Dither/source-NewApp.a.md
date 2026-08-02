---
title: IW-Half-Dither
apple_id: DTS10000151
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/IW-Half-Dither/Listings/source_NewApp_a.html
archived_at: '2026-07-18T03:12:12.000343Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IW-Half-Dither](IW-Half-Dither.md)


[Next](source-NewApp.c.md)[Previous](source-GXPrintingResTypes.r.md)

# source/NewApp.a

```
;------------------------------------------------------------------------------
;
;   FILENAME
;       NewApp.a
;
;   DESCRIPTION
;       Contains the code necessary to dispatch from a routine in one code
;       module to a code segment in another module or within the same module
;
;   COPYRIGHT
;       Copyright © Apple Computer, Inc. 1989-1996
;       All rights reserved. 
;
;   MODIFICATION HISTORY
;
;       04/23/90        Tom Dowdy   New Today
;       12/20/93        dmh         Sync'd with the shipping 1.0b3 GX driver.
;       08/26/94        dmh         Sync'd with the shipping 1.0.1 GX driver.
;       05/21/96        Jason H-H   Updated for ETO#19/MW.
;       05/21/96        Don Swatman Modifications for halftoning, dithering and plane seperations.
;
;--------------------------------------------------------------------------------

                CASE    OBJ
                STRING  ASIS

SD_JumpTable    PROC    EXPORT
                dc.l    0           

    ; Universal messages

                IMPORT SD_Initialize
                JMP SD_Initialize

                IMPORT SD_ShutDown
                JMP SD_ShutDown

                IMPORT SD_DefaultPrinter
                JMP SD_DefaultPrinter

                IMPORT SD_DefaultFormat
                JMP SD_DefaultFormat

                IMPORT SD_DefaultJob
                JMP SD_DefaultJob

                IMPORT SD_JobFormatDialog
                JMP SD_JobFormatDialog

                IMPORT SD_JobFormatModeQuery
                JMP SD_JobFormatModeQuery

                IMPORT SD_RenderPage
                JMP SD_RenderPage

                IMPORT SD_OpenConnection
                JMP SD_OpenConnection

                IMPORT SD_CloseConnection
                JMP SD_CloseConnection

                IMPORT SD_StartSendPage
                JMP SD_StartSendPage

                IMPORT SD_FinishSendPage
                JMP SD_FinishSendPage

                IMPORT SD_DumpBuffer
                JMP SD_DumpBuffer

                IMPORT SD_FreeBuffer
                JMP SD_FreeBuffer

                IMPORT SD_SetupImageData
                JMP SD_SetupImageData

                IMPORT SD_JobIdle
                JMP SD_JobIdle

    ; print dialog stuff

                IMPORT SD_JobPrintDialog
                JMP SD_JobPrintDialog

                IMPORT SD_HandlePanelEvent
                JMP SD_HandlePanelEvent

    ; Raster messages

                IMPORT SD_PackageBitmap
                JMP SD_PackageBitmap

                IMPORT SD_LineFeed
                JMP SD_LineFeed

    END
```

[Next](source-NewApp.c.md)[Previous](source-GXPrintingResTypes.r.md)

