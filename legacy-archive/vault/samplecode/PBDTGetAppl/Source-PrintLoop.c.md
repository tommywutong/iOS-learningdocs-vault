---
title: PBDTGetAppl
apple_id: DTS10000042
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBDTGetAppl/Listings/Source_PrintLoop_c.html
archived_at: '2026-07-18T03:18:20.097915Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBDTGetAppl](PBDTGetAppl.md)


[Next](Source-SlimFunctions.c.md)[Previous](Source-MenuDispatch.c.md)

# Source/PrintLoop.c

```c
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------

    Bare minimum printing loop.
    Hacked out of Tech Note #161
    Calls DrawImage inside Drawing.c to image the printed page
*/


#include "Printing.h"

pascal void PrintIdleProc()
{
    short   err;

    err = PrError();

    /*  we could spin the cursor here if we want */

    if(err) {
        InitCursor();       /* set to arrow */
        ErrMsgCode("\pI'm in the printing idle proc.",err);
    }
}

void PrintWindow()
/*
    This will call the drawing code set up in
    Drawing.c for the printing GrafPort
    when there is an error, the code gotoos the
    exit so the printer driver will be closed.
*/
{
    THPrint     tpr;
    TPPrPort    printPort;
    short       err;
    TPrStatus   tprStat;

    tpr = NewHandle(sizeof(TPrint));
    if(!tpr) {
        ErrMsgCode("\pAllocating TPrint failed.",0);
        return;  /* driver not open yet */
    }

    PrOpen();
    if(err = PrError()) {
        ErrMsgCode("\p PrOpen failed.",err);
        goto exit;
    }

    if(!PrStlDialog(tpr))   goto exit;
    if(err = PrError()) {
        ErrMsgCode("\p PrStlDialog failed.",err);
        goto exit;
    }

    if(!PrJobDialog(tpr))   goto exit;
    if(err = PrError()) {
        ErrMsgCode("\p PrJobDialog failed.",err);
        goto exit;
    }

    SetCursor(*GetCursor(watchCursor));
    (**tpr).prJob.pIdleProc = PrintIdleProc;

    printPort = PrOpenDoc(tpr, nil, nil);
    if(err = PrError()) {
        ErrMsgCode("\p PrOpenDoc failed.",err);
        goto exit;
    }

    PrOpenPage(printPort, nil);
    if(err = PrError()) {
        ErrMsgCode("\p PrOpenPage failed.",err);
        goto exit;
    }

    DrawImage(printPort);

    PrClosePage(printPort);
    if(err = PrError()) {
        ErrMsgCode("\p PrClosePage failed.",err);
        goto exit;
    }

    PrCloseDoc(printPort);
    if(err = PrError()) {
        ErrMsgCode("\p PrCloseDoc failed.",err);
        goto exit;
    }

    if( ((**tpr).prJob.bJDocLoop == bSpoolLoop))
        PrPicFile( tpr, nil, nil, nil, &tprStat);

    if(err = PrError()) {
        ErrMsgCode("\p PrPicFile failed.",err);
        goto exit;
    }

exit:
    PrClose();
    if(err = PrError())
        ErrMsgCode("\p PrClose failed.",err);

    InitCursor();
}
```

[Next](Source-SlimFunctions.c.md)[Previous](Source-MenuDispatch.c.md)

