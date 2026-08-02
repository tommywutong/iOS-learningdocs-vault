---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/SimpleEdit_SimpleEditMFC_h.html
archived_at: '2026-07-18T03:29:52.758490Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](SimpleEdit-SimpleEditMFCDoc.cpp.md)[Previous](SimpleEdit-SimpleEditMFC.cpp.md)

# SimpleEdit/SimpleEditMFC.h

```c
// SimpleEdit MFC.h : main header file for the SIMPLEEDIT MFC application
//

#ifndef __AFXWIN_H__
    #error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CSimpleEditMFCApp:
// See SimpleEdit MFC.cpp for the implementation of this class
//

class CSimpleEditMFCApp : public CWinApp
{
public:
    CSimpleEditMFCApp();

// Overrides
    // ClassWizard generated virtual function overrides
    //{{AFX_VIRTUAL(CSimpleEditMFCApp)
    public:
    virtual BOOL InitInstance();
    virtual int ExitInstance();
    //}}AFX_VIRTUAL

// Implementation

    //{{AFX_MSG(CSimpleEditMFCApp)
    afx_msg void OnAppAbout();
        // NOTE - the ClassWizard will add and remove member functions here.
        //    DO NOT EDIT what you see in these blocks of generated code !
    //}}AFX_MSG
    DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////
```

[Next](SimpleEdit-SimpleEditMFCDoc.cpp.md)[Previous](SimpleEdit-SimpleEditMFC.cpp.md)

