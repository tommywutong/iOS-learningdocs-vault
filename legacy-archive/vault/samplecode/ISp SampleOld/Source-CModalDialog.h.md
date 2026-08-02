---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_CModalDialog_h.html
archived_at: '2026-07-18T03:12:08.852091Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-ErrorAlert.c.md)[Previous](Source-CModalDialog.cp.md)

# Source/CModalDialog.h

```c
/*
    File:       CModalDialog.h

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

#ifndef __CModalDialog__
#define __CModalDialog__

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes

#ifndef __MENUS__
#include <Menus.h>
#endif

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Types

class CModalDialog
{
protected:

    DialogPtr   dialog;
    short       numBaseItems;

public:

    CModalDialog(const short inDialogID);
    ~CModalDialog();

    void Show(void);
    void Hide(void);
    void MakeCurrentPort(void);
    void SetDefaultItem(const short inWhichItem);
    void SetCancelItem(const short inWhichItem);

    short GetItemValue(const short inWhichCheckBox);
    void GetEditText(const short inWhichItem, Str255 outText);
    void GetStaticText(const short inWhichItem, Str255 outText);
    MenuHandle GetItemMenuHandle(const short inWhichItem);

    void GetItemValue(const short inWhichCheckBox, const short inValue);
    void SetEditText(const short inWhichItem, Str255 inText);
    void SetStaticText(const short inWhichItem, Str255 inText);

    void SelectEditText(const short inWhichItem, const short inStart, const short inEnd);
};

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Functions

#ifdef __cplusplus
extern "C" {
#endif

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-ErrorAlert.c.md)[Previous](Source-CModalDialog.cp.md)

