---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/SMIL_Elements.html
archived_at: '2026-07-18T02:20:17.828454Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/pUsing_Quick__Extensions.html) [!](WOSMILDocument.md)

# SMIL Elements

This chapter covers the details about each
SMIL element in WebObjects. [Table 4-1](#apple-ijbegskgijbeo) lists the SMIL
elements in WebObjects, their possible parents and children, and
the corresponding SMIL tag. Following the table, there are sections
with more information on each element in the table.

__Table
4-1 SMIL elements in WebObjects__

| Element | Parents | Possible children | Corresponding tag |
| WOSMILDocument | _None_ | WOSMILHead WOSMILBody | `<smil>` |
| WOSMILHead | WOSMILDocument | WOSMILHeadMeta WOSMILHeadLayout WOSMILSwitch | `<head>` |
| WOSMILBody | WOSMILDocument | WOSMILMediaObject WOSMILActiveLink WOSMILPar WOSMILSeq WOSMILSwitch | `<body>` |
| WOSMILHeadMeta | WOSMILHead | _None_ | `<meta>` |
| WOSMILHeadLayout | WOSMILHead | WOSMILRootLayout WOSMILRegion | `<layout>` |
| WOSMILRootLayout | WOSMILHeadLayout | _None_ | `<root-layout>` |
| WOSMILRegion | WOSMILHeadLayout | _None_ | `<region>` |
| WOSMILSwitch | WOSMILHead WOSMILBody | WOSMILHeadLayout WOSMILActiveLink WOSMILPar WOSMILSeq WOSMILMediaObject WOSMILSwitch | `<switch>` |
| WOSMILMediaObject | WOSMILBody WOSMILPar WOSMILSeq WOSMILSwitch | WOSMILAnchor | `<ref>`, `<animation>`, `<audio>`, `<img>`, `<video>`, `<text>`, and `<textstream>` |
| WOSMILSeq | WOSMILBody WOSMILSwitch | WOSMILMediaObject WOSMILActiveLink WOSMILPar WOSMILSeq WOSMILSwitch | `<seq>` |
| WOSMILPar | WOSMILBody WOSMILSwitch | WOSMILMediaObject WOSMILActiveLink WOSMILPar WOSMILSeq WOSMILSwitch | `<par>` |
| WOSMILActiveLink | WOSMILBody WOSMILSeq WOSMILPar WOSMILSwitch | WOSMILMediaObject WOSMILPar WOSMILSeq WOSMILSwitch | `<a>` |
| WOSMILAnchor | WOSMILMediaObject | _None_ | `<anchor>` |

When any SMIL element requires an easy-to-read ID, you can
add the `elementID` binding to
it. Also, you can add bindings for namespace declarations using `otherTagString`.
See ["Using QuickTime SMIL Extensions"](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/iUsing_Quick_JBJEIAI.html) for
more information.

[!](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/pUsing_Quick__Extensions.html) [!](WOSMILDocument.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
