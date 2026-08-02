---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/MFCMDIPlayer_MFCMDIPlayerView_h.html
archived_at: '2026-07-18T03:29:51.635393Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](MFCMDIPlayer-ReadMe.txt.md)[Previous](MFCMDIPlayer-MFCMDIPlayerView.cpp.md)

# MFCMDIPlayer/MFCMDIPlayerView.h

```c
// MFCMDIPlayerView.h : interface of the CMFCMDIPlayerView class
//
/////////////////////////////////////////////////////////////////////////////
#include "CQuickTime.h"

class CMFCMDIPlayerView : public CView
{
protected: // create from serialization only
    CMFCMDIPlayerView();
    DECLARE_DYNCREATE(CMFCMDIPlayerView)

// Attributes
public:
    CMFCMDIPlayerDoc* GetDocument();
    CString mfullPath;
    CQuickTime *pQuickTime;     // QuickTime object
    BOOL OpenMovie(void);       // Open a movie
    void CloseMovie(void);      // Close a movie

// Operations
public:

// Overrides
    // ClassWizard generated virtual function overrides
    //{{AFX_VIRTUAL(CMFCMDIPlayerView)
    public:
    virtual void OnDraw(CDC* pDC);  // overridden to draw this view
    virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
    virtual BOOL Create(LPCTSTR lpszClassName, LPCTSTR lpszWindowName, DWORD dwStyle, const RECT& rect, CWnd* pParentWnd, UINT nID, CCreateContext* pContext = NULL);
    protected:
    virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
    virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
    virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);
    virtual LRESULT WindowProc(UINT message, WPARAM wParam, LPARAM lParam);
    //}}AFX_VIRTUAL

// Implementation
public:
    virtual ~CMFCMDIPlayerView();
#ifdef _DEBUG
    virtual void AssertValid() const;
    virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
    //{{AFX_MSG(CMFCMDIPlayerView)
    afx_msg int OnCreate(LPCREATESTRUCT lpCreateStruct);
    afx_msg void OnDestroy();
    afx_msg void OnSize(UINT nType, int cx, int cy);
    //}}AFX_MSG
    DECLARE_MESSAGE_MAP()
};

#ifndef _DEBUG  // debug version in MFCMDIPlayerView.cpp
inline CMFCMDIPlayerDoc* CMFCMDIPlayerView::GetDocument()
   { return (CMFCMDIPlayerDoc*)m_pDocument; }
#endif

/////////////////////////////////////////////////////////////////////////////
```

[Next](MFCMDIPlayer-ReadMe.txt.md)[Previous](MFCMDIPlayer-MFCMDIPlayerView.cpp.md)

