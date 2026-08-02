---
title: Checking For QD3D Windows DLL's
apple_id: DTS10001882
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d84.html
archived_at: '2026-07-18T02:38:44.735664Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD3D84Checking For QD3D Windows DLL's |

|  |  |
| --- | --- |
| ---   Q: Is there any QuickDraw 3D `Gestalt` equivalent on the Windows side which will tell you if QD3D is present?  A: There is no exact equivalent to `Gestalt` on Windows. It's not really necessary because the entire system is just based on shared libraries (DLLs). The simplest way to check for the presence of QD3D is to try and load the QD3D library.   |  | | --- | | ``` #if defined (DEBUG)     hinst = LoadLibrary( "QD3D_D.DLL" );   #else     hinst = LoadLibrary( "QD3D.DLL" );   #endif     if ( hinst != NULL )     {        Q3GetVersion( &major, &minor );        // Use it...     }     else     {        // QuickDraw 3D not present        // handle that...     } ``` |   Additionally the QD3D DLLs all have version resources which can be queried using the Win32 version control API without loading the library.  The QD3D installer registers several keys in the registry which could also be used to determine if QD3D was installed. Note: Apple requires that Independent Software Vendors install QD3D using the QD3D installer or its equivalent. Just copying the DLLs is not sufficient. These include HKLM\SOFTWARE\Apple Computer Inc\QuickDraw 3D\...  Note there is no equivalent to "weak linking" on Windows. An application which links against QD3D will fail to load if QD3D is not present. An application which is concerned that QD3D might not be present will have to dynamically load and link against QD3D using the `LoadLibrary` and `GetProcAddress` routines or related functions. However, keep in mind that one of the most common reasons that Mac OS applications do not link against QD3D is because they wish to keep their memory image small. This is really not an issue on Windows due to the way virtual memory and the loader work in that environment. On Windows, a more accurate metric of runtime memory usage is working set.  QD3D should have only a minimal impact on working set if it is not fully initialized (via `Q3Initialize`) or used.  Note the QD3D Viewer can be used without explicit linking against the 3DViewer.DLL. See the Windows SDK sample "ViewerSampleWin32Only." [Jul 11 1997] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
