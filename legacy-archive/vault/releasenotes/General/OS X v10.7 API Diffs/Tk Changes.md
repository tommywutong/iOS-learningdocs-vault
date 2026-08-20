---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Tk.html
archived_at: '2026-07-18T02:54:40.655424Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Tk Changes

## Tk

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

tkInt.hAdded TkKeyEventtkIntDecls.hAdded #def TkCanvasDashParseProc_TCL_DECLAREDAdded #def TkCanvasDashPrintProc_TCL_DECLAREDAdded #def TkOffsetParseProc_TCL_DECLAREDAdded #def TkOffsetPrintProc_TCL_DECLAREDAdded #def TkOrientParseProc_TCL_DECLAREDAdded #def TkOrientPrintProc_TCL_DECLAREDAdded #def TkPixelParseProc_TCL_DECLAREDAdded #def TkPixelPrintProc_TCL_DECLAREDAdded #def TkSmoothParseProc_TCL_DECLAREDAdded #def TkSmoothPrintProc_TCL_DECLAREDAdded #def TkStateParseProc_TCL_DECLAREDAdded #def TkStatePrintProc_TCL_DECLAREDtkIntPlatDecls.hAdded TkIntPlatStubs::LRESULT() (no architecture available)Added TkWinChildProc() (no architecture available)Modified TkMacOSXGrowToplevel()

|  | Declaration |
| --- | --- |
| From | EXTERN int TkMacOSXGrowToplevel ( void \*whichWindow, Point start); |
| To | EXTERN int TkMacOSXGrowToplevel ( void \*whichWindow, XPoint start); |

Modified TkSetMacColor()

|  | Declaration |
| --- | --- |
| From | EXTERN int TkSetMacColor ( unsigned long pixel, CGColorRef \*macColor); |
| To | EXTERN int TkSetMacColor ( unsigned long pixel, void \*macColor); |

Modified TkMacOSXWinBounds()

|  | Declaration |
| --- | --- |
| From | EXTERN void TkMacOSXWinBounds ( TkWindow \*winPtr, Rect \*geometry); |
| To | EXTERN void TkMacOSXWinBounds ( TkWindow \*winPtr, void \*geometry); |

Modified TkMacOSXMakeStippleMap()

|  | Declaration |
| --- | --- |
| From | EXTERN BitMapPtr TkMacOSXMakeStippleMap ( Drawable d1, Drawable d2); |
| To | EXTERN void \* TkMacOSXMakeStippleMap ( Drawable d1, Drawable d2); |

Modified TkMacOSXDoHLEvent()

|  | Declaration |
| --- | --- |
| From | EXTERN int TkMacOSXDoHLEvent ( EventRecord \*theEvent); |
| To | EXTERN int TkMacOSXDoHLEvent ( void \*theEvent); |

ttkDecls.hModified Ttk_RegisterElement()

|  | Declaration |
| --- | --- |
| From | TTKAPI Ttk_ElementImpl Ttk_RegisterElement ( Tcl_Interp \*interp, Ttk_Theme theme, const char \*elementName, Ttk_ElementSpec \*elementSpec, void \*clientData); |
| To | TTKAPI Ttk_ElementClass \* Ttk_RegisterElement ( Tcl_Interp \*interp, Ttk_Theme theme, const char \*elementName, Ttk_ElementSpec \*elementSpec, void \*clientData); |

ttkTheme.hRemoved #def TTK_STATE_USER7Removed Ttk_ElementImplRemoved Ttk_LayoutFindNode()Removed Ttk_LayoutIdentify()Removed Ttk_LayoutNodeRemoved Ttk_LayoutNodeName()Removed Ttk_LayoutNodeParcel()Removed Ttk_PlaceLayoutNode()Added #def TTK_STATE_HOVERAdded TtkEnumerateHashTable()Added Ttk_ClientRegion()Added Ttk_ElementAdded Ttk_ElementClassAdded Ttk_ElementName()Added Ttk_ElementParcel()Added Ttk_EnsembleAdded Ttk_FindElement()Added Ttk_IdentifyElement()Added Ttk_InvokeEnsemble()Added Ttk_LayoutStyle()Added Ttk_PlaceElement()Added Ttk_StyleAdded Ttk_StyleDefault()Added Ttk_StyleMap()Modified Ttk_LayoutNodeInternalParcel()

|  | Declaration |
| --- | --- |
| From | Ttk_Box Ttk_LayoutNodeInternalParcel ( Ttk_Layout, Ttk_LayoutNode \*); |
| To | Ttk_Box Ttk_LayoutNodeInternalParcel ( Ttk_Layout, Ttk_Element); |

Modified Ttk_LayoutNodeReqSize()

|  | Declaration |
| --- | --- |
| From | void Ttk_LayoutNodeReqSize ( Ttk_Layout, Ttk_LayoutNode \*, int \*w, int \*h); |
| To | void Ttk_LayoutNodeReqSize ( Ttk_Layout, Ttk_Element, int \*w, int \*h); |

Modified Ttk_ChangeElementState()

|  | Declaration |
| --- | --- |
| From | void Ttk_ChangeElementState ( Ttk_LayoutNode \*, unsigned set, unsigned clr); |
| To | void Ttk_ChangeElementState ( Ttk_Element, unsigned set, unsigned clr); |

Modified Ttk_LayoutNodeInternalPadding()

|  | Declaration |
| --- | --- |
| From | Ttk_Padding Ttk_LayoutNodeInternalPadding ( Ttk_Layout, Ttk_LayoutNode \*); |
| To | Ttk_Padding Ttk_LayoutNodeInternalPadding ( Ttk_Layout, Ttk_Element); |

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
