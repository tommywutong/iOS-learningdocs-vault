---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/MFCMDIPlayer_MFCMDIPlayer_h.html
archived_at: '2026-07-18T03:29:51.742251Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](MFCMDIPlayer-MFCMDIPlayerDoc.cpp.md)[Previous](MFCMDIPlayer-MFCMDIPlayer.cpp.md)

# MFCMDIPlayer/MFCMDIPlayer.h

```c
// MFCMDIPlayer.h : main header file for the MFCMDIPLAYER application
//

#ifndef __AFXWIN_H__
    #error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CMFCMDIPlayerApp:
// See MFCMDIPlayer.cpp for the implementation of this class
//

class CMFCMDIPlayerApp : public CWinApp
{
public:
    CMFCMDIPlayerApp();

// Overrides
    // ClassWizard generated virtual function overrides
    //{{AFX_VIRTUAL(CMFCMDIPlayerApp)
    public:
    virtual BOOL InitInstance();
    virtual int ExitInstance();
    //}}AFX_VIRTUAL

// Implementation

    //{{AFX_MSG(CMFCMDIPlayerApp)
    afx_msg void OnAppAbout();
        // NOTE - the ClassWizard will add and remove member functions here.
        //    DO NOT EDIT what you see in these blocks of generated code !
    //}}AFX_MSG
    DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////
```

[Next](MFCMDIPlayer-MFCMDIPlayerDoc.cpp.md)[Previous](MFCMDIPlayer-MFCMDIPlayer.cpp.md)

