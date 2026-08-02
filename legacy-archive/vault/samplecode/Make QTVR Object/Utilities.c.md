---
title: Make QTVR Object
apple_id: DTS10000338
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Object/Listings/Utilities_c.html
archived_at: '2026-07-18T03:14:24.313224Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Object](Make%20QTVR%20Object.md)


[Next](Document%20Revision%20History.md)[Previous](QTVRObjectAuthoring.h.md)

# Utilities.c

```c
//
//      This is sample code which will make QTVR object movies from Linear QuickTime movies.
//
//      © 1991-1996 Apple Computer, Inc.  All rights reserved.
//

#include "MakeQTVRObject.h"
#include "extern.h" 

#include<fp.h>
float   StringToFloat(StringPtr theString)
{
    decimal d;
    short   ix=0,vp=0;

    theString[theString[0]+1] = 0;
    str2dec ( (const char *)&theString[1], &ix, &d , &vp );
    return dec2f ( &d);
}

void    FloatToString(float num,Str255  *theString,short    digits)
{
    decform theForm;
    decimal d;
    short   i = 1;

    theForm.style = FIXEDDECIMAL;                            /*  FLOATDECIMAL or FIXEDDECIMAL */
    theForm.digits = digits;

    num2dec ( &theForm, (double_t) num, &d );
    dec2str ( &theForm, &d, (char*)&((*theString)[1]) );
    (*theString)[0] = 0;
    while((*theString)[i] != 0)
        {
        i++;
        (*theString)[0]++;
        }
}



void    UserMessage(Str255  theMessage)
{
    short   itemHit;
    DialogPtr   myDlg;
    short   itemType;
    Handle  itemHandle;
    Rect    itemRect;

    Boolean done = false;
    SysBeep(10);

    myDlg = GetNewDialog( kGenericMessageDLOG, 0, (WindowPtr) -1);
    SetDialogDefaultItem(myDlg,kDefaultOK);
    GetDItem(myDlg,kMessageID,&itemType,&itemHandle,&itemRect);
    SetDialogItemText (itemHandle, theMessage);


    while ( !done)
        {
        ModalDialog( 0, &itemHit );
        switch ( itemHit ) 
            {
            case kDefaultOK:
                done = true;
                break;
            }
        } 
    DisposDialog( myDlg);

}

Boolean UserQuestion(Str255 theMessage)
{
    short   itemHit;
    DialogPtr   myDlg;
    short   itemType;
    Handle  itemHandle;
    Rect    itemRect;

    Boolean done = false,result;
    SysBeep(10);

    myDlg = GetNewDialog( kGenericQuestionDLOG, 0, (WindowPtr) -1);
    SetDialogDefaultItem(myDlg,kDefaultOK);
    GetDItem(myDlg,kMessageID,&itemType,&itemHandle,&itemRect);
    SetDialogItemText (itemHandle, theMessage);


    while ( !done)
        {
        ModalDialog( 0, &itemHit );
        switch ( itemHit ) 
            {
            case kDefaultOK:
                done = true;
                result = true;
                break;
            case kDefaultCancel:
                done = true;
                result = false;
                break;
            }
        } 
    DisposDialog( myDlg);
    return result;
}

void EnDisItem (MenuHandle mh, short item, Boolean enable)
{
    if (enable) {
        EnableItem(mh, item);
    } else {
        DisableItem(mh, item);
    }
}

OSErr   AttachMovieToWindow(WindowPtr   theWindow,MovieInstance *theMovie)
{
if(!theWindow)
    return 1;
if(!theMovie)
    return 1;

SetWRefCon (theWindow, (long)theMovie);
return 0;
}

MovieInstance   *GetMovieInstanceFromWindow(WindowPtr   theWindow)
{
if(!theWindow)
    return nil;
return (MovieInstance *)GetWRefCon(theWindow);
}
```

[Next](Document%20Revision%20History.md)[Previous](QTVRObjectAuthoring.h.md)

