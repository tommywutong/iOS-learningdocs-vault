---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_TAboutBoxPane_cp.html
archived_at: '2026-07-18T03:18:33.450775Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-TAboutBoxPane.h.md)[Previous](sources-RemoveServerKey.c.md)

# sources/TAboutBoxPane.cp

```c
//  TAboutBoxPane.cp -  AppleShare IP Dialog Pane Object
// 
// Apple Macintosh Developer Technical Support
// Written by:  Vinnie Moscaritolo
//
//  Copyright (work in progress)  Apple Computer, Inc All rights reserved.
//
// You may incorporate this sample code into your applications without
// restriction, though the sample code has been provided "AS IS" and the
// responsibility for its operation is 100% yours.  However, what you are
// not permitted to do is to redistribute the source as "DSC Sample Code"
// after having made changes. If you're going to re-distribute the source,
// we require that you make it clear in the source that the code was
// descended from Apple Sample Code, but that you've made changes.
// 



#include <Appearance.h>

#include "TAboutBoxPane.h"
#include "ICAPI.h"

#define PGP_MACINTOSH 1
#include "pgpFeatures.h"

static enum{
    kAboutBoxPanePaneDITL   = 142,
};

#define kAboutTextStringsID 142 

static enum {
    kCreditsText        =1,
    kAPICreditsText ,
    kAuthorURL,
    kTitleURL,
    };

enum
{
    kAuthorClick = 1,
    kTitleClick,
    kPictureItem,
    kBorderItem,
    kCreditsTxtItem,
    kCreditsTxtItem2
  };


 // ---------------------------------------------------------------------------
TAboutBoxPane::TAboutBoxPane( DialogPtr dialog, SInt16 items  )
                    : TPane (dialog, items) 
// ---------------------------------------------------------------------------
//
{   

    ControlFontStyleRec fontInfo;
    Str255              text;
    Str255              sdkInfo ;
    ControlHandle       theControl;

    AppendDialogItemList(dialog, kAboutBoxPanePaneDITL, overlayDITL );

    fontInfo.flags = kControlUseFontMask;
    fontInfo.font = kControlFontSmallSystemFont;

    GetIndString(text, kAboutTextStringsID, kCreditsText);
    GetDialogItemAsControl( dialog, items + kCreditsTxtItem,    &theControl );
    SetControlData( theControl, 0, kControlStaticTextTextTag, text[0], (Ptr)(text+1));
    SetControlData( theControl, 0, kControlStaticTextStyleTag, sizeof fontInfo, (Ptr)&fontInfo);

    GetIndString(text, kAboutTextStringsID, kAPICreditsText);
    PGPGetSDKString((char*)sdkInfo) ;
    c2pstr((char*)sdkInfo);

    PLstrcat(text,  sdkInfo);
    GetDialogItemAsControl( dialog, items + kCreditsTxtItem2,   &theControl );
    SetControlData( theControl, 0, kControlStaticTextTextTag, text[0], (Ptr)(text+1));
    SetControlData( theControl, 0, kControlStaticTextStyleTag, sizeof fontInfo, (Ptr)&fontInfo);



}   



// ---------------------------------------------------------------------------
TAboutBoxPane::~TAboutBoxPane()
// ---------------------------------------------------------------------------
//
{    

    ShortenDITL( fDialog, CountDITL(fDialog) - fOrigItems);
}


// ---------------------------------------------------------------------------
void TAboutBoxPane::Refresh(void)
// ---------------------------------------------------------------------------
//
{    
}


// ---------------------------------------------------------------------------
void TAboutBoxPane::Idle(void)
// ---------------------------------------------------------------------------
//
{    

}


// ---------------------------------------------------------------------------
void TAboutBoxPane::ItemHit(SInt16 item)
// ---------------------------------------------------------------------------
//
{    
    SInt16          localItem;
    Boolean         enable;
    Str255          text;
    ICInstance      icp;
    long            startSel;
    long            endSel;

    localItem = item - fOrigItems;

    switch ( localItem )
    {
            case kAuthorClick:  
                ICStart(&icp, (unsigned long)'????');
                ICFindConfigFile(icp, 0, nil);
                GetIndString(text, kAboutTextStringsID, kAuthorURL);
                startSel    = 0;
                endSel      = text[0];      
                ICLaunchURL(icp,"\pmailto:",  (char *) &text[1], text[0], &startSel, &endSel);
                ICStop(icp);
                break;

            case kTitleClick:
                ICStart(&icp, (unsigned long)'????');
                ICFindConfigFile(icp, 0, nil);
                GetIndString(text, kAboutTextStringsID, kTitleURL);
                startSel    = 0;
                endSel      = text[0];      
                ICLaunchURL(icp,"\p",  (char *) &text[1], text[0], &startSel, &endSel);
                ICStop(icp);
                break;

    }

}
```

[Next](sources-TAboutBoxPane.h.md)[Previous](sources-RemoveServerKey.c.md)

