---
title: STD File Saver
apple_id: DTS10000307
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/STD_File_Saver/Listings/Source_MyPDEF_4_HandlingDialogs_a.html
archived_at: '2026-07-18T03:22:48.348591Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [STD File Saver](STD%20File%20Saver.md)


[Next](Source-MyPDEF4HandlingDialogs.c.md)[Previous](Source-MyPDEF0DraftMode.c.md)

# Source/MyPDEF_4_HandlingDialogs.a

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

HANDLINGDLGS    PROC    EXPORT

    IMPORT  FILEPRINTDEFAULT
    IMPORT  FILEPRSTLDIALOG
    IMPORT  FILEPRJOBDIALOG
    IMPORT  FILEPRSTLINIT
    IMPORT  FILEPRJOBINIT
    IMPORT  FILEPRDLGMAIN
    IMPORT  FILEPRVALIDATE
    IMPORT  FILEPRJOBMERGE

    JMP FILEPRINTDEFAULT
    JMP FILEPRSTLDIALOG
    JMP FILEPRJOBDIALOG
    JMP FILEPRSTLINIT
    JMP FILEPRJOBINIT
    JMP FILEPRDLGMAIN
    JMP FILEPRVALIDATE
    JMP FILEPRJOBMERGE

    ENDPROC

    END
```

[Next](Source-MyPDEF4HandlingDialogs.c.md)[Previous](Source-MyPDEF0DraftMode.c.md)

