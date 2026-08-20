---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/SimplePlayer_SimplePlayerMFCDoc_h.html
archived_at: '2026-07-18T03:29:53.098855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](SimplePlayer-SimplePlayerMFCView.cpp.md)[Previous](SimplePlayer-SimplePlayerMFCDoc.cpp.md)

# SimplePlayer/SimplePlayerMFCDoc.h

```
// SimplePlayer MFCDoc.h : interface of the CSimplePlayerMFCDoc class
//
/////////////////////////////////////////////////////////////////////////////

class CSimplePlayerMFCDoc : public CDocument
{
protected: // create from serialization only
    CSimplePlayerMFCDoc();
    DECLARE_DYNCREATE(CSimplePlayerMFCDoc)

// Attributes
public:

// Operations
public:

// Overrides
    // ClassWizard generated virtual function overrides
    //{{AFX_VIRTUAL(CSimplePlayerMFCDoc)
    public:
    virtual BOOL OnNewDocument();
    virtual void Serialize(CArchive& ar);
    virtual BOOL OnOpenDocument(LPCTSTR lpszPathName);
    //}}AFX_VIRTUAL

// Implementation
public:
    virtual ~CSimplePlayerMFCDoc();
#ifdef _DEBUG
    virtual void AssertValid() const;
    virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
    //{{AFX_MSG(CSimplePlayerMFCDoc)
        // NOTE - the ClassWizard will add and remove member functions here.
        //    DO NOT EDIT what you see in these blocks of generated code !
    //}}AFX_MSG
    DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////
```

[Next](SimplePlayer-SimplePlayerMFCView.cpp.md)[Previous](SimplePlayer-SimplePlayerMFCDoc.cpp.md)

