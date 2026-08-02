---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Source_SR_WinDialog_c.html
archived_at: '2026-07-18T03:19:19.951997Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Document%20Revision%20History.md)[Previous](Source-SRTriangle.c.md)

# Source/SR_WinDialog.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_WinDialog.c                                           **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Modal dialog routines                                    **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996-1997 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#include "QD3D.h"
#include "QD3DExtension.h"

#if defined(WINDOW_SYSTEM_WIN32) && WINDOW_SYSTEM_WIN32

#include "SR.h"
#include "SR_WinDialog.h"
#include "resource.h"

/******************************************************************************
 **                                                                          **
 **                         Globals and Externs                              **
 **                                                                          **
 *****************************************************************************/

extern HINSTANCE    hinstMyDLL;

static TSRPrivate   *SRgRendererPrivate = NULL;


/******************************************************************************
 **                                                                          **
 **                         Forward Declarations                             **
 **                                                                          **
 *****************************************************************************/

staticBOOL CALLBACK SR_ModalConfigure(
    HWND        hDlg,
    UINT        iMsg,
    WPARAM      wParam,
    LPARAM      lParam);


/******************************************************************************
 **                                                                          **
 **                             Dialog Routines                              **
 **                                                                          **
 *****************************************************************************/

/*===========================================================================*\
 *
 *  Routine:    SR_WinModalDialog()
 *
 *  Comments:   
 *
\*===========================================================================*/

TQ3Status SR_WinModalDialog(
    TQ3RendererObject           renderer,
    TQ3DialogAnchor             dialogAnchor, 
    TQ3Boolean                  *canceled,  
    void                        *rendererPrivate)
{
    TQ3Status   status = kQ3Success;
    BOOL        wasChanged;

    SRgRendererPrivate = rendererPrivate;

    if ((wasChanged = DialogBox(hinstMyDLL,
        MAKEINTRESOURCE(IDD_MODAL_CONFIGURE),
        dialogAnchor.ownerWindow, SR_ModalConfigure)) != -1) {
        *canceled = !wasChanged;
        status = kQ3Success;
    } else {
        *canceled = kQ3True;
        status = kQ3Failure;
    }

    SRgRendererPrivate = NULL;          
    return (status);
}


/*===========================================================================*\
 *
 *  Routine:    SR_ModalConfigure()
 *
 *  Comments:   
 *
\*===========================================================================*/

static BOOL CALLBACK SR_ModalConfigure(
    HWND    hDlg,
    UINT    iMsg,
    WPARAM  wParam,
    LPARAM  lParam)
{
    short   checkBoxValue;

    switch (iMsg) {
        case WM_INITDIALOG:
            checkBoxValue = SRgRendererPrivate->dummyConfigData;
            if (checkBoxValue) {
                CheckDlgButton(hDlg, IDC_DUMMYCONFIG, BST_CHECKED);
            } else {
                CheckDlgButton(hDlg, IDC_DUMMYCONFIG, BST_UNCHECKED);
            }

            return (TRUE);
        case WM_COMMAND:
            switch (LOWORD(wParam)) {
                case IDOK:
                    if (IsDlgButtonChecked(hDlg, IDC_DUMMYCONFIG)) {
                        SRgRendererPrivate->dummyConfigData = kQ3True;
                    } else {
                        SRgRendererPrivate->dummyConfigData = kQ3False;
                    }
                    EndDialog(hDlg, TRUE);

                    return (TRUE);

                case IDCANCEL:
                    EndDialog(hDlg, FALSE);

                    return (TRUE);
            }
    }

    return (FALSE);         
}

#endif  /*  WINDOW_SYSTEM_WIN32  */
```

[Next](Document%20Revision%20History.md)[Previous](Source-SRTriangle.c.md)

