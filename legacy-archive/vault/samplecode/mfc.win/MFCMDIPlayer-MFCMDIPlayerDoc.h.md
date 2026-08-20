---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/MFCMDIPlayer_MFCMDIPlayerDoc_h.html
archived_at: '2026-07-18T03:29:51.547147Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](MFCMDIPlayer-MFCMDIPlayerView.cpp.md)[Previous](MFCMDIPlayer-MFCMDIPlayerDoc.cpp.md)

# MFCMDIPlayer/MFCMDIPlayerDoc.h

```
// MFCMDIPlayerDoc.h : interface of the CMFCMDIPlayerDoc class
//
/////////////////////////////////////////////////////////////////////////////

class CMFCMDIPlayerDoc : public CDocument
{
protected: // create from serialization only
    CMFCMDIPlayerDoc();
    DECLARE_DYNCREATE(CMFCMDIPlayerDoc)

// Attributes
public:

// Operations
public:

// Overrides
    // ClassWizard generated virtual function overrides
    //{{AFX_VIRTUAL(CMFCMDIPlayerDoc)
    public:
    virtual BOOL OnNewDocument();
    virtual void Serialize(CArchive& ar);
    virtual BOOL OnOpenDocument(LPCTSTR lpszPathName);
    //}}AFX_VIRTUAL

// Implementation
public:
    virtual ~CMFCMDIPlayerDoc();
#ifdef _DEBUG
    virtual void AssertValid() const;
    virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
    //{{AFX_MSG(CMFCMDIPlayerDoc)
        // NOTE - the ClassWizard will add and remove member functions here.
        //    DO NOT EDIT what you see in these blocks of generated code !
    //}}AFX_MSG
    DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////
```

[Next](MFCMDIPlayer-MFCMDIPlayerView.cpp.md)[Previous](MFCMDIPlayer-MFCMDIPlayerDoc.cpp.md)

