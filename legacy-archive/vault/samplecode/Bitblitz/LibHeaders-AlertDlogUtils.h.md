---
title: Bitblitz
apple_id: DTS10000066
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Bitblitz/Listings/LibHeaders_AlertDlogUtils_h.html
archived_at: '2026-07-18T03:01:55.053994Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Bitblitz](Bitblitz.md)


[Next](LibHeaders-AlrtDlogTools.h.md)[Previous](Bitblitz.md)

# LibHeaders/AlertDlogUtils.h

```
/*========================================================================================
    File:   AlertDlogUtils.c

    By:     George Delaney
            Mac CPU Software Quality    
    Date:   5/14/90

    Contents:
    Header declarations for standard Dialog and Alert routines.
  ======================================================================================*/



/*--------------------------------------------------------------------------------------*/
/*  Constants  */

#define  OK         1
#define  CANCEL     2



/*--------------------------------------------------------------------------------------*/
/*  Alert Utils */



/*--------------------------------------------------------------------------------------*/
/*  Alerts  */

pascal void  OKStrAlert         (Str255 str1, Str255 str2, Str255 str3, Str255 str4);
pascal void  OKRsrcAlert        (short rsrcID, short strIndex);



/*--------------------------------------------------------------------------------------*/
/*  Dialog Utils    */

pascal void  GetDlogShort       (DialogPtr dptr, short item, short *value);
pascal void  SetDlogShort       (DialogPtr dptr, short item, short  value);

pascal void  GetDlogLong        (DialogPtr dptr, short item, long  *value);
pascal void  SetDlogLong        (DialogPtr dptr, short item, long   value);

pascal Rect  GetDlogRect        (DialogPtr dptr, short item);

pascal void  SetDlogCtl         (DialogPtr dptr, short item, short value);
pascal short GetDlogCtl         (DialogPtr dptr, short item);

pascal void  FrameDlogButton    (DialogPtr dptr, short item);

pascal void  GetDlogItemRect    (DialogPtr dptr, short item, Rect *itemRect);
pascal void  FrameDlogItemRect  (DialogPtr dptr, short item);

pascal void  SetDlogItemProc    (DialogPtr dptr, short item, Ptr procPtr);

pascal void  SetDlogString      (DialogPtr dptr, short item, Str255 str);


/*--------------------------------------------------------------------------------------*/
/*  Dialogs  */
```

[Next](LibHeaders-AlrtDlogTools.h.md)[Previous](Bitblitz.md)

