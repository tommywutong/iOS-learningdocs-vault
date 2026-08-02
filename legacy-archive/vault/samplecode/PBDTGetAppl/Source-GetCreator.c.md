---
title: PBDTGetAppl
apple_id: DTS10000042
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBDTGetAppl/Listings/Source_GetCreator_c.html
archived_at: '2026-07-18T03:18:19.930759Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBDTGetAppl](PBDTGetAppl.md)


[Next](Source-InitMac.c.md)[Previous](Source-EventLoop.c.md)

# Source/GetCreator.c

```
void GetTextItem(DialogPtr theDialog, short itemNumber, Str255 text)
{
    Handle  iHandle;
    Rect    box;
    int     iType;

    GetDItem(theDialog,itemNumber,&iType,&iHandle,&box);
    GetIText(iHandle,text);
}


#define ASK_ALERT   500
#define OK_BTN      1
#define CANCEL_BTN  2
#define CREATOR_STR 3

short GetCreator(char creator[4])
{

    DialogPtr   dp;
    short       item;
    Str255      createStr;
    short       i;

    dp = GetNewDialog(ASK_ALERT,nil,(WindowPtr)-1);

    ModalDialog(nil,&item);

    if(item == CANCEL_BTN) goto bail;

    GetTextItem(dp,CREATOR_STR,createStr);
    if(createStr[0] < 4) {
        Msg("\pYou Must enter at least 4 characters.");
        goto bail;
    }

    for(i = 0; i < 4; i++)
        creator[i] = createStr[i + 1];

bail:
    DisposeDialog(dp);
    /* Do three events to update windows behind */
    MainEvent();
    MainEvent();
    MainEvent();
    return item;
}
```

[Next](Source-InitMac.c.md)[Previous](Source-EventLoop.c.md)

