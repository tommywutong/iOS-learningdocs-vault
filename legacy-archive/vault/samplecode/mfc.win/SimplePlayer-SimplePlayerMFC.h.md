---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/SimplePlayer_SimplePlayerMFC_h.html
archived_at: '2026-07-18T03:29:53.327649Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](SimplePlayer-SimplePlayerMFCDoc.cpp.md)[Previous](SimplePlayer-SimplePlayerMFC.cpp.md)

# SimplePlayer/SimplePlayerMFC.h

```c
// SimplePlayer MFC.h : main header file for the SIMPLEPLAYER MFC application
//

#ifndef __AFXWIN_H__
    #error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CSimplePlayerMFCApp:
// See SimplePlayer MFC.cpp for the implementation of this class
//

class CSimplePlayerMFCApp : public CWinApp
{
public:
    CSimplePlayerMFCApp();

// Overrides
    // ClassWizard generated virtual function overrides
    //{{AFX_VIRTUAL(CSimplePlayerMFCApp)
    public:
    virtual BOOL InitInstance();
    virtual int ExitInstance();
    //}}AFX_VIRTUAL

// Implementation

    //{{AFX_MSG(CSimplePlayerMFCApp)
    afx_msg void OnAppAbout();
        // NOTE - the ClassWizard will add and remove member functions here.
        //    DO NOT EDIT what you see in these blocks of generated code !
    //}}AFX_MSG
    DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////
```

[Next](SimplePlayer-SimplePlayerMFCDoc.cpp.md)[Previous](SimplePlayer-SimplePlayerMFC.cpp.md)

