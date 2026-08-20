---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/SimpleEdit_SimpleEditMFCDoc_h.html
archived_at: '2026-07-18T03:29:52.510384Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](SimpleEdit-SimpleEditMFCView.cpp.md)[Previous](SimpleEdit-SimpleEditMFCDoc.cpp.md)

# SimpleEdit/SimpleEditMFCDoc.h

```
// SimpleEdit MFCDoc.h : interface of the CSimpleEditMFCDoc class
//
/////////////////////////////////////////////////////////////////////////////

class CSimpleEditMFCDoc : public CDocument
{
protected: // create from serialization only
    CSimpleEditMFCDoc();
    DECLARE_DYNCREATE(CSimpleEditMFCDoc)

// Attributes
public:

// Operations
public:

// Overrides
    // ClassWizard generated virtual function overrides
    //{{AFX_VIRTUAL(CSimpleEditMFCDoc)
    public:
    virtual BOOL OnNewDocument();
    virtual void Serialize(CArchive& ar);
    virtual BOOL OnOpenDocument(LPCTSTR lpszPathName);
    //}}AFX_VIRTUAL

// Implementation
public:
    virtual ~CSimpleEditMFCDoc();
#ifdef _DEBUG
    virtual void AssertValid() const;
    virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
    //{{AFX_MSG(CSimpleEditMFCDoc)
        // NOTE - the ClassWizard will add and remove member functions here.
        //    DO NOT EDIT what you see in these blocks of generated code !
    //}}AFX_MSG
    DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////
```

[Next](SimpleEdit-SimpleEditMFCView.cpp.md)[Previous](SimpleEdit-SimpleEditMFCDoc.cpp.md)

