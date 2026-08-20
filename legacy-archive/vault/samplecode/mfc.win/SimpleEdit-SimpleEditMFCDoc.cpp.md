---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/SimpleEdit_SimpleEditMFCDoc_cpp.html
archived_at: '2026-07-18T03:29:52.463196Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](SimpleEdit-SimpleEditMFCDoc.h.md)[Previous](SimpleEdit-SimpleEditMFC.h.md)

# SimpleEdit/SimpleEditMFCDoc.cpp

```c
// SimpleEdit MFCDoc.cpp : implementation of the CSimpleEditMFCDoc class
//

#include "stdafx.h"
#include "SimpleEditMFC.h"

#include "SimpleEditMFCDoc.h"
#include "SimpleEditMFCView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CSimpleEditMFCDoc

IMPLEMENT_DYNCREATE(CSimpleEditMFCDoc, CDocument)

BEGIN_MESSAGE_MAP(CSimpleEditMFCDoc, CDocument)
    //{{AFX_MSG_MAP(CSimpleEditMFCDoc)
        // NOTE - the ClassWizard will add and remove mapping macros here.
        //    DO NOT EDIT what you see in these blocks of generated code!
    //}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CSimpleEditMFCDoc construction/destruction

CSimpleEditMFCDoc::CSimpleEditMFCDoc()
{
    // TODO: add one-time construction code here

}

CSimpleEditMFCDoc::~CSimpleEditMFCDoc()
{
}

BOOL CSimpleEditMFCDoc::OnNewDocument()
{
    if (!CDocument::OnNewDocument())
        return FALSE;

    // TODO: add reinitialization code here
    // (SDI documents will reuse this document)

    return TRUE;
}

/////////////////////////////////////////////////////////////////////////////
// CSimpleEditMFCDoc serialization

void CSimpleEditMFCDoc::Serialize(CArchive& ar)
{
    if (ar.IsStoring())
    {
        // TODO: add storing code here
    }
    else
    {
        // TODO: add loading code here
    }
}

/////////////////////////////////////////////////////////////////////////////
// CSimpleEditMFCDoc diagnostics

#ifdef _DEBUG
void CSimpleEditMFCDoc::AssertValid() const
{
    CDocument::AssertValid();
}

void CSimpleEditMFCDoc::Dump(CDumpContext& dc) const
{
    CDocument::Dump(dc);
}
#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// CSimpleEditMFCDoc commands

BOOL CSimpleEditMFCDoc::OnOpenDocument(LPCTSTR lpszPathName) 
{
    if (!CDocument::OnOpenDocument(lpszPathName))
        return FALSE;

    // Set the Movie filename for the view
    POSITION pos = GetFirstViewPosition();
    CSimpleEditMFCView* pView = (CSimpleEditMFCView*)GetNextView(pos);
    if (pView){
        pView->mfullPath = lpszPathName;
        if (pView->OpenMovie() != TRUE)
            return FALSE;
    }
    return TRUE;
}
```

[Next](SimpleEdit-SimpleEditMFCDoc.h.md)[Previous](SimpleEdit-SimpleEditMFC.h.md)

