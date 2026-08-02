---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/WebKit.html
archived_at: '2026-07-15T07:34:47.566249Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# WebKit Changes

## WebKit

CarbonUtils.hModified WebConvertNSImageToCGImageRef()

|  | Introduction |
| --- | --- |
| From | OS X 10.2 |
| To | OS X 10.3 |

Modified WebInitForCarbon()

|  | Introduction |
| --- | --- |
| From | OS X 10.2 |
| To | OS X 10.3 |

DOMAbstractView.hModified [DOMAbstractView](https://developer.apple.com/documentation/webkit/domabstractview)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMAbstractView.document](https://developer.apple.com/documentation/webkit/domabstractview/1515358-document)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMDocument *document ``` |
| To | ``` @property(readonly, strong) DOMDocument *document ``` |

DOMAttr.hModified [DOMAttr](https://developer.apple.com/documentation/webkit/domattr)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMAttr.ownerElement](https://developer.apple.com/documentation/webkit/domattr/1536344-ownerelement)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMElement *ownerElement ``` |
| To | ``` @property(readonly, strong) DOMElement *ownerElement ``` |

Modified [DOMAttr.style](https://developer.apple.com/documentation/webkit/domattr/1536729-style)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSStyleDeclaration *style ``` |
| To | ``` @property(readonly, strong) DOMCSSStyleDeclaration *style ``` |

DOMBlob.hModified [DOMBlob](https://developer.apple.com/documentation/webkit/domblob)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

DOMCDATASection.hModified [DOMCDATASection](https://developer.apple.com/documentation/webkit/domcdatasection)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCSS.hModified [-[DOMCSSStyleDeclaration azimuth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537087-azimuth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration background]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537291-background)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration backgroundAttachment]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537399-backgroundattachment)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration backgroundColor]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536508-backgroundcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration backgroundImage]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537747-backgroundimage)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration backgroundPosition]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537212-backgroundposition)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration backgroundRepeat]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537415-backgroundrepeat)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration border]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537457-border)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderBottom]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537136-borderbottom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderBottomColor]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536522-borderbottomcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderBottomStyle]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536865-borderbottomstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderBottomWidth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537966-borderbottomwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderCollapse]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537897-bordercollapse)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderColor]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537814-bordercolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderLeft]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536544-borderleft)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderLeftColor]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537504-borderleftcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderLeftStyle]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537899-borderleftstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderLeftWidth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537527-borderleftwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderRight]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537216-borderright)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderRightColor]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536630-borderrightcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderRightStyle]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538198-borderrightstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderRightWidth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536486-borderrightwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderSpacing]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536488-borderspacing)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderStyle]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537384-borderstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderTop]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537619-bordertop)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderTopColor]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537557-bordertopcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderTopStyle]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536636-bordertopstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderTopWidth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536449-bordertopwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration borderWidth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537607-borderwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration bottom]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536221-bottom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration captionSide]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536185-captionside)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration clear]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536731-clear)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration clip]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536966-clip)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration color]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536621-color)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration content]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537719-content)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration counterIncrement]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537595-counterincrement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration counterReset]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537063-counterreset)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration cssFloat]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537488-cssfloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration cue]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536215-cue)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration cueAfter]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536557-cueafter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration cueBefore]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537217-cuebefore)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration cursor]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537597-cursor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration direction]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537340-direction)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration display]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536272-display)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration elevation]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537097-elevation)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration emptyCells]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536606-emptycells)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration font]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536196-font)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration fontFamily]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537588-fontfamily)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration fontSize]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538175-fontsize)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration fontSizeAdjust]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537039-fontsizeadjust)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration fontStretch]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537452-fontstretch)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration fontStyle]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537576-fontstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration fontVariant]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537762-fontvariant)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration fontWeight]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537495-fontweight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration height]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536925-height)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration left]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537622-left)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration letterSpacing]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538024-letterspacing)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration lineHeight]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536560-lineheight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration listStyle]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536240-liststyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration listStyleImage]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537725-liststyleimage)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration listStylePosition]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537637-liststyleposition)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration listStyleType]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537498-liststyletype)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration margin]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538039-margin)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration marginBottom]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536390-marginbottom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration marginLeft]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536298-marginleft)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration marginRight]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537806-marginright)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration marginTop]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536405-margintop)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration markerOffset]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536310-markeroffset)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration marks]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536295-marks)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration maxHeight]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537059-maxheight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration maxWidth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537577-maxwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration minHeight]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537968-minheight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration minWidth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537387-minwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration orphans]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536200-orphans)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration outline]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537652-outline)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration outlineColor]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536817-outlinecolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration outlineStyle]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538219-outlinestyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration outlineWidth]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537819-outlinewidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration overflow]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537327-overflow)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration padding]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537208-padding)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration paddingBottom]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538125-paddingbottom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration paddingLeft]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537561-paddingleft)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration paddingRight]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536223-paddingright)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration paddingTop]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537698-paddingtop)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration page]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537256-page)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration pageBreakAfter]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537432-pagebreakafter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration pageBreakBefore]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537033-pagebreakbefore)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration pageBreakInside]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538055-pagebreakinside)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration pause]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537631-pause)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration pauseAfter]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536316-pauseafter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration pauseBefore]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537469-pausebefore)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration pitch]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537996-pitch)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration pitchRange]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537451-pitchrange)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration playDuring]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537957-playduring)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration position]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537949-position)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration quotes]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537439-quotes)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration richness]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537821-richness)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration right]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536909-right)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setAzimuth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536701-setazimuth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBackground:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537919-setbackground)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBackgroundAttachment:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537695-setbackgroundattachment)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBackgroundColor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536820-setbackgroundcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBackgroundImage:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538180-setbackgroundimage)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBackgroundPosition:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538222-setbackgroundposition)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBackgroundRepeat:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536502-setbackgroundrepeat)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorder:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538163-setborder)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderBottom:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536978-setborderbottom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderBottomColor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537304-setborderbottomcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderBottomStyle:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537769-setborderbottomstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderBottomWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536783-setborderbottomwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderCollapse:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537486-setbordercollapse)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderColor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537641-setbordercolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderLeft:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537141-setborderleft)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderLeftColor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537964-setborderleftcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderLeftStyle:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537982-setborderleftstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderLeftWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537422-setborderleftwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderRight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536575-setborderright)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderRightColor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536661-setborderrightcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderRightStyle:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537468-setborderrightstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderRightWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537779-setborderrightwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderSpacing:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537743-setborderspacing)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderStyle:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536214-setborderstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderTop:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537037-setbordertop)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderTopColor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537536-setbordertopcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderTopStyle:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537004-setbordertopstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderTopWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536964-setbordertopwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBorderWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536431-setborderwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setBottom:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536531-setbottom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setCaptionSide:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537601-setcaptionside)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setClear:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538129-setclear)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setClip:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536697-setclip)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setColor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537213-setcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setContent:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537673-setcontent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setCounterIncrement:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537174-setcounterincrement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setCounterReset:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536331-setcounterreset)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setCssFloat:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538076-setcssfloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setCue:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537627-setcue)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setCueAfter:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537513-setcueafter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setCueBefore:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536519-setcuebefore)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setCursor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537311-setcursor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setDirection:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536956-setdirection)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setDisplay:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537000-setdisplay)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setElevation:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536650-setelevation)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setEmptyCells:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536195-setemptycells)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setFont:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536461-setfont)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setFontFamily:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537485-setfontfamily)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setFontSize:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536339-setfontsize)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setFontSizeAdjust:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536615-setfontsizeadjust)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setFontStretch:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537280-setfontstretch)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setFontStyle:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536843-setfontstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setFontVariant:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537586-setfontvariant)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setFontWeight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536632-setfontweight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setHeight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537760-setheight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setLeft:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536916-setleft)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setLetterSpacing:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537534-setletterspacing)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setLineHeight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537602-setlineheight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setListStyle:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537434-setliststyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setListStyleImage:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538098-setliststyleimage)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setListStylePosition:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537407-setliststyleposition)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setListStyleType:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536391-setliststyletype)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMargin:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537501-setmargin)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMarginBottom:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537361-setmarginbottom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMarginLeft:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536467-setmarginleft)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMarginRight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537758-setmarginright)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMarginTop:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537184-setmargintop)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMarkerOffset:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536269-setmarkeroffset)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMarks:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538135-setmarks)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMaxHeight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537947-setmaxheight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMaxWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538133-setmaxwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMinHeight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536334-setminheight)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setMinWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537610-setminwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setOrphans:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537541-setorphans)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setOutline:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537237-setoutline)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setOutlineColor:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537412-setoutlinecolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setOutlineStyle:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537915-setoutlinestyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setOutlineWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536742-setoutlinewidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setOverflow:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537548-setoverflow)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPadding:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537535-setpadding)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPaddingBottom:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537428-setpaddingbottom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPaddingLeft:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537543-setpaddingleft)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPaddingRight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537083-setpaddingright)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPaddingTop:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537395-setpaddingtop)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPage:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536179-setpage)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPageBreakAfter:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538004-setpagebreakafter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPageBreakBefore:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537929-setpagebreakbefore)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPageBreakInside:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537608-setpagebreakinside)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPause:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536470-setpause)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPauseAfter:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537591-setpauseafter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPauseBefore:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538116-setpausebefore)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPitch:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536246-setpitch)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPitchRange:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537383-setpitchrange)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPlayDuring:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537715-setplayduring)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setPosition:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537303-setposition)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setQuotes:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536734-setquotes)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setRichness:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537069-setrichness)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setRight:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536389-setright)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setSize:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536231-setsize)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setSpeak:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536305-setspeak)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setSpeakHeader:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536545-setspeakheader)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setSpeakNumeral:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536395-setspeaknumeral)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setSpeakPunctuation:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536570-setspeakpunctuation)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setSpeechRate:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537632-setspeechrate)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setStress:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536294-setstress)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setTableLayout:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537940-settablelayout)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setTextAlign:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536564-settextalign)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setTextDecoration:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537524-settextdecoration)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setTextIndent:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536327-settextindent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setTextShadow:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537435-settextshadow)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setTextTransform:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537484-settexttransform)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setTop:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537420-settop)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setUnicodeBidi:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536789-setunicodebidi)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setVerticalAlign:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537810-setverticalalign)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setVisibility:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537057-setvisibility)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setVoiceFamily:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537862-setvoicefamily)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setVolume:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536928-setvolume)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setWhiteSpace:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536604-setwhitespace)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setWidows:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537307-setwidows)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setWidth:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537062-setwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setWordSpacing:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537530-setwordspacing)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration setZIndex:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536811-setzindex)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration size]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538103-size)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration speak]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537827-speak)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration speakHeader]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536788-speakheader)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration speakNumeral]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536347-speaknumeral)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration speakPunctuation]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537181-speakpunctuation)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration speechRate]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537016-speechrate)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration stress]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537394-stress)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration tableLayout]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536287-tablelayout)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration textAlign]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536370-textalign)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration textDecoration]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537483-textdecoration)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration textIndent]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537671-textindent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration textShadow]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537426-textshadow)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration textTransform]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537403-texttransform)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration top]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537992-top)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration unicodeBidi]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537505-unicodebidi)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration verticalAlign]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536515-verticalalign)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration visibility]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537329-visibility)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration voiceFamily]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537517-voicefamily)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration volume]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1538123-volume)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration whiteSpace]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537569-whitespace)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration widows]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536961-widows)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration width]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536411-width)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration wordSpacing]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536882-wordspacing)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration zIndex]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1537553-zindex)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCSSCharsetRule.hModified [DOMCSSCharsetRule](https://developer.apple.com/documentation/webkit/domcsscharsetrule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCSSFontFaceRule.hModified [DOMCSSFontFaceRule](https://developer.apple.com/documentation/webkit/domcssfontfacerule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSFontFaceRule.style](https://developer.apple.com/documentation/webkit/domcssfontfacerule/1392014-style)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSStyleDeclaration *style ``` |
| To | ``` @property(readonly, strong) DOMCSSStyleDeclaration *style ``` |

DOMCSSImportRule.hModified [DOMCSSImportRule](https://developer.apple.com/documentation/webkit/domcssimportrule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSImportRule.media](https://developer.apple.com/documentation/webkit/domcssimportrule/1536435-media)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMMediaList *media ``` |
| To | ``` @property(readonly, strong) DOMMediaList *media ``` |

Modified [DOMCSSImportRule.styleSheet](https://developer.apple.com/documentation/webkit/domcssimportrule/1537048-stylesheet)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSStyleSheet *styleSheet ``` |
| To | ``` @property(readonly, strong) DOMCSSStyleSheet *styleSheet ``` |

DOMCSSMediaRule.hModified [DOMCSSMediaRule](https://developer.apple.com/documentation/webkit/domcssmediarule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSMediaRule.cssRules](https://developer.apple.com/documentation/webkit/domcssmediarule/1534823-cssrules)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSRuleList *cssRules ``` |
| To | ``` @property(readonly, strong) DOMCSSRuleList *cssRules ``` |

Modified [-[DOMCSSMediaRule insertRule::]](https://developer.apple.com/documentation/webkit/domcssmediarule/1534825-insertrule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSMediaRule.media](https://developer.apple.com/documentation/webkit/domcssmediarule/1534818-media)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMMediaList *media ``` |
| To | ``` @property(readonly, strong) DOMMediaList *media ``` |

DOMCSSPageRule.hModified [DOMCSSPageRule](https://developer.apple.com/documentation/webkit/domcsspagerule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSPageRule.style](https://developer.apple.com/documentation/webkit/domcsspagerule/1536576-style)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSStyleDeclaration *style ``` |
| To | ``` @property(readonly, strong) DOMCSSStyleDeclaration *style ``` |

DOMCSSPrimitiveValue.hModified [DOMCSSPrimitiveValue](https://developer.apple.com/documentation/webkit/domcssprimitivevalue)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSPrimitiveValue setFloatValue::]](https://developer.apple.com/documentation/webkit/domcssprimitivevalue/1418408-setfloatvalue)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSPrimitiveValue setStringValue::]](https://developer.apple.com/documentation/webkit/domcssprimitivevalue/1418440-setstringvalue)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_ATTR](https://developer.apple.com/documentation/webkit/dom_css_attr)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_CM](https://developer.apple.com/documentation/webkit/dom_css_cm)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_COUNTER](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_counter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_DEG](https://developer.apple.com/documentation/webkit/dom_css_deg)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_DIMENSION](https://developer.apple.com/documentation/webkit/dom_css_dimension)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_EMS](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_ems)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_EXS](https://developer.apple.com/documentation/webkit/dom_css_exs)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_GRAD](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_grad)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_HZ](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_hz)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_IDENT](https://developer.apple.com/documentation/webkit/dom_css_ident)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_IN](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_in)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_KHZ](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_khz)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_MM](https://developer.apple.com/documentation/webkit/dom_css_mm)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_MS](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_ms)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_NUMBER](https://developer.apple.com/documentation/webkit/dom_css_number)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_PC](https://developer.apple.com/documentation/webkit/dom_css_pc)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_PERCENTAGE](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_percentage)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_PT](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_pt)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_PX](https://developer.apple.com/documentation/webkit/dom_css_px)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_RAD](https://developer.apple.com/documentation/webkit/dom_css_rad)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_RECT](https://developer.apple.com/documentation/webkit/dom_css_rect)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_RGBCOLOR](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_rgbcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_S](https://developer.apple.com/documentation/webkit/dom_css_s)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_STRING](https://developer.apple.com/documentation/webkit/dom_css_string)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_UNKNOWN](https://developer.apple.com/documentation/webkit/dom_css_unknown)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_URI](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_uri)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_VH](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_vh)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.4 |

Modified [DOM_CSS_VMAX](https://developer.apple.com/documentation/webkit/dom_css_vmax)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.4 |

Modified [DOM_CSS_VMIN](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_vmin)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.4 |

Modified [DOM_CSS_VW](https://developer.apple.com/documentation/webkit/1418446-dom_measurement_enumeration_lega/dom_css_vw)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.4 |

DOMCSSRule.hModified [DOMCSSRule](https://developer.apple.com/documentation/webkit/domcssrule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSRule.parentRule](https://developer.apple.com/documentation/webkit/domcssrule/1403868-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSRule *parentRule ``` |
| To | ``` @property(readonly, strong) DOMCSSRule *parentRule ``` |

Modified [DOMCSSRule.parentStyleSheet](https://developer.apple.com/documentation/webkit/domcssrule/1403884-parentstylesheet)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSStyleSheet *parentStyleSheet ``` |
| To | ``` @property(readonly, strong) DOMCSSStyleSheet *parentStyleSheet ``` |

Modified [DOM_CHARSET_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_charset_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_FONT_FACE_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_font_face_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_IMPORT_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_import_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_MEDIA_RULE](https://developer.apple.com/documentation/webkit/dom_media_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_PAGE_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_page_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_STYLE_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_style_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_UNKNOWN_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_unknown_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_WEBKIT_KEYFRAMES_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_webkit_keyframes_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_WEBKIT_KEYFRAME_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_webkit_keyframe_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_WEBKIT_REGION_RULE](https://developer.apple.com/documentation/webkit/1403866-dom_rule_enumeration_legacy/dom_webkit_region_rule)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.4 |

DOMCSSRuleList.hModified [DOMCSSRuleList](https://developer.apple.com/documentation/webkit/domcssrulelist)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCSSStyleDeclaration.hModified [DOMCSSStyleDeclaration](https://developer.apple.com/documentation/webkit/domcssstyledeclaration)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCSSStyleDeclaration getPropertyShorthand:]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1580826-getpropertyshorthand)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.5 |

Modified [DOMCSSStyleDeclaration.parentRule](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1536387-parentrule)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSRule *parentRule ``` |
| To | ``` @property(readonly, strong) DOMCSSRule *parentRule ``` |

Modified [-[DOMCSSStyleDeclaration setProperty:::]](https://developer.apple.com/documentation/webkit/domcssstyledeclaration/1580825-setproperty)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCSSStyleRule.hModified [DOMCSSStyleRule](https://developer.apple.com/documentation/webkit/domcssstylerule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSStyleRule.style](https://developer.apple.com/documentation/webkit/domcssstylerule/1462932-style)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSStyleDeclaration *style ``` |
| To | ``` @property(readonly, strong) DOMCSSStyleDeclaration *style ``` |

DOMCSSStyleSheet.hModified [DOMCSSStyleSheet](https://developer.apple.com/documentation/webkit/domcssstylesheet)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSStyleSheet.cssRules](https://developer.apple.com/documentation/webkit/domcssstylesheet/1536358-cssrules)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSRuleList *cssRules ``` |
| To | ``` @property(readonly, strong) DOMCSSRuleList *cssRules ``` |

Modified [-[DOMCSSStyleSheet insertRule::]](https://developer.apple.com/documentation/webkit/domcssstylesheet/1561935-insertrule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMCSSStyleSheet.ownerRule](https://developer.apple.com/documentation/webkit/domcssstylesheet/1536785-ownerrule)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSRule *ownerRule ``` |
| To | ``` @property(readonly, strong) DOMCSSRule *ownerRule ``` |

Modified [DOMCSSStyleSheet.rules](https://developer.apple.com/documentation/webkit/domcssstylesheet/1536707-rules)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSRuleList *rules ``` |
| To | ``` @property(readonly, strong) DOMCSSRuleList *rules ``` |

DOMCSSUnknownRule.hModified [DOMCSSUnknownRule](https://developer.apple.com/documentation/webkit/domcssunknownrule)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCSSValue.hModified [DOMCSSValue](https://developer.apple.com/documentation/webkit/domcssvalue)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_CUSTOM](https://developer.apple.com/documentation/webkit/1518003-dom_inheritance_enumeration_lega/dom_css_custom)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_INHERIT](https://developer.apple.com/documentation/webkit/dom_css_inherit)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_PRIMITIVE_VALUE](https://developer.apple.com/documentation/webkit/dom_css_primitive_value)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CSS_VALUE_LIST](https://developer.apple.com/documentation/webkit/1518003-dom_inheritance_enumeration_lega/dom_css_value_list)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCSSValueList.hModified [DOMCSSValueList](https://developer.apple.com/documentation/webkit/domcssvaluelist)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCharacterData.hModified [DOMCharacterData](https://developer.apple.com/documentation/webkit/domcharacterdata)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCharacterData deleteData::]](https://developer.apple.com/documentation/webkit/domcharacterdata/1553037-deletedata)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCharacterData insertData::]](https://developer.apple.com/documentation/webkit/domcharacterdata/1553036-insertdata)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCharacterData replaceData:::]](https://developer.apple.com/documentation/webkit/domcharacterdata/1553038-replacedata)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMCharacterData substringData::]](https://developer.apple.com/documentation/webkit/domcharacterdata/1553039-substringdata)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMComment.hModified [DOMComment](https://developer.apple.com/documentation/webkit/domcomment)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMCounter.hModified [DOMCounter](https://developer.apple.com/documentation/webkit/domcounter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMDocument.hAdded [DOMDocument.activeElement](https://developer.apple.com/documentation/webkit/domdocument/1494875-activeelement)Added [-[DOMDocument hasFocus]](https://developer.apple.com/documentation/webkit/domdocument/1494886-hasfocus)Modified [DOMDocument](https://developer.apple.com/documentation/webkit/domdocument)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMDocument.anchors](https://developer.apple.com/documentation/webkit/domdocument/1494855-anchors)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *anchors ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *anchors ``` |

Modified [DOMDocument.applets](https://developer.apple.com/documentation/webkit/domdocument/1494970-applets)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *applets ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *applets ``` |

Modified [DOMDocument.body](https://developer.apple.com/documentation/webkit/domdocument/1494850-body)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) DOMHTMLElement *body ``` |
| To | ``` @property(strong) DOMHTMLElement *body ``` |

Modified [DOMDocument.characterSet](https://developer.apple.com/documentation/webkit/domdocument/1494872-characterset)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.charset](https://developer.apple.com/documentation/webkit/domdocument/1494878-charset)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument createAttributeNS::]](https://developer.apple.com/documentation/webkit/domdocument/1494940-createattributens)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMDocument createCSSStyleDeclaration]](https://developer.apple.com/documentation/webkit/domdocument/1494844-createcssstyledeclaration)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.5 |

Modified [-[DOMDocument createElementNS::]](https://developer.apple.com/documentation/webkit/domdocument/1494865-createelementns)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMDocument createNodeIterator::::]](https://developer.apple.com/documentation/webkit/domdocument/1494951-createnodeiterator)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMDocument createProcessingInstruction::]](https://developer.apple.com/documentation/webkit/domdocument/1494899-createprocessinginstruction)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMDocument createTreeWalker::::]](https://developer.apple.com/documentation/webkit/domdocument/1494934-createtreewalker)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMDocument.defaultCharset](https://developer.apple.com/documentation/webkit/domdocument/1494882-defaultcharset)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.defaultView](https://developer.apple.com/documentation/webkit/domdocument/1494968-defaultview)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMAbstractView *defaultView ``` |
| To | ``` @property(readonly, strong) DOMAbstractView *defaultView ``` |

Modified [DOMDocument.doctype](https://developer.apple.com/documentation/webkit/domdocument/1494927-doctype)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMDocumentType *doctype ``` |
| To | ``` @property(readonly, strong) DOMDocumentType *doctype ``` |

Modified [DOMDocument.documentElement](https://developer.apple.com/documentation/webkit/domdocument/1494932-documentelement)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMElement *documentElement ``` |
| To | ``` @property(readonly, strong) DOMElement *documentElement ``` |

Modified [DOMDocument.documentURI](https://developer.apple.com/documentation/webkit/domdocument/1494862-documenturi)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument elementFromPoint:y:]](https://developer.apple.com/documentation/webkit/domdocument/1494867-elementfrompoint)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument execCommand:]](https://developer.apple.com/documentation/webkit/domdocument/1494894-execcommand)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument execCommand:userInterface:]](https://developer.apple.com/documentation/webkit/domdocument/1494892-execcommand)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument execCommand:userInterface:value:]](https://developer.apple.com/documentation/webkit/domdocument/1494880-execcommand)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.forms](https://developer.apple.com/documentation/webkit/domdocument/1494929-forms)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *forms ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *forms ``` |

Modified [-[DOMDocument getComputedStyle::]](https://developer.apple.com/documentation/webkit/domdocument/1494889-getcomputedstyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMDocument getElementsByTagNameNS::]](https://developer.apple.com/documentation/webkit/domdocument/1494964-getelementsbytagnamens)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMDocument getOverrideStyle::]](https://developer.apple.com/documentation/webkit/domdocument/1494851-getoverridestyle)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMDocument.images](https://developer.apple.com/documentation/webkit/domdocument/1494864-images)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *images ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *images ``` |

Modified [DOMDocument.implementation](https://developer.apple.com/documentation/webkit/domdocument/1494905-implementation)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMImplementation *implementation ``` |
| To | ``` @property(readonly, strong) DOMImplementation *implementation ``` |

Modified [-[DOMDocument importNode::]](https://developer.apple.com/documentation/webkit/domdocument/1494874-importnode)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMDocument.inputEncoding](https://developer.apple.com/documentation/webkit/domdocument/1494959-inputencoding)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.links](https://developer.apple.com/documentation/webkit/domdocument/1494895-links)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *links ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *links ``` |

Modified [DOMDocument.preferredStylesheetSet](https://developer.apple.com/documentation/webkit/domdocument/1494857-preferredstylesheetset)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument queryCommandEnabled:]](https://developer.apple.com/documentation/webkit/domdocument/1494854-querycommandenabled)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument queryCommandIndeterm:]](https://developer.apple.com/documentation/webkit/domdocument/1494877-querycommandindeterm)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument queryCommandState:]](https://developer.apple.com/documentation/webkit/domdocument/1494860-querycommandstate)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument queryCommandSupported:]](https://developer.apple.com/documentation/webkit/domdocument/1494911-querycommandsupported)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMDocument queryCommandValue:]](https://developer.apple.com/documentation/webkit/domdocument/1494843-querycommandvalue)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.readyState](https://developer.apple.com/documentation/webkit/domdocument/1494962-readystate)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.selectedStylesheetSet](https://developer.apple.com/documentation/webkit/domdocument/1494907-selectedstylesheetset)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.styleSheets](https://developer.apple.com/documentation/webkit/domdocument/1494922-stylesheets)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMStyleSheetList *styleSheets ``` |
| To | ``` @property(readonly, strong) DOMStyleSheetList *styleSheets ``` |

Modified [-[DOMDocument webkitCancelFullScreen]](https://developer.apple.com/documentation/webkit/domdocument/1494852-webkitcancelfullscreen)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [DOMDocument.xmlEncoding](https://developer.apple.com/documentation/webkit/domdocument/1494918-xmlencoding)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.xmlStandalone](https://developer.apple.com/documentation/webkit/domdocument/1494901-xmlstandalone)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMDocument.xmlVersion](https://developer.apple.com/documentation/webkit/domdocument/1494926-xmlversion)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMDocumentFragment.hModified [DOMDocumentFragment](https://developer.apple.com/documentation/webkit/domdocumentfragment)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMDocumentType.hModified [DOMDocumentType](https://developer.apple.com/documentation/webkit/domdocumenttype)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMDocumentType.entities](https://developer.apple.com/documentation/webkit/domdocumenttype/1534544-entities)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNamedNodeMap *entities ``` |
| To | ``` @property(readonly, strong) DOMNamedNodeMap *entities ``` |

Modified [DOMDocumentType.notations](https://developer.apple.com/documentation/webkit/domdocumenttype/1534541-notations)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNamedNodeMap *notations ``` |
| To | ``` @property(readonly, strong) DOMNamedNodeMap *notations ``` |

DOMElement.hModified [DOMElement](https://developer.apple.com/documentation/webkit/domelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMElement blur]](https://developer.apple.com/documentation/webkit/domelement/1476187-blur)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.6 |

Modified [DOMElement.clientLeft](https://developer.apple.com/documentation/webkit/domelement/1476204-clientleft)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMElement.clientTop](https://developer.apple.com/documentation/webkit/domelement/1476216-clienttop)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMElement.firstElementChild](https://developer.apple.com/documentation/webkit/domelement/1476271-firstelementchild)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMElement *firstElementChild ``` |
| To | ``` @property(readonly, strong) DOMElement *firstElementChild ``` |

Modified [-[DOMElement focus]](https://developer.apple.com/documentation/webkit/domelement/1476261-focus)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.6 |

Modified [-[DOMElement getAttributeNS::]](https://developer.apple.com/documentation/webkit/domelement/1476244-getattributens)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMElement getAttributeNodeNS::]](https://developer.apple.com/documentation/webkit/domelement/1476256-getattributenodens)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMElement getElementsByTagNameNS::]](https://developer.apple.com/documentation/webkit/domelement/1476202-getelementsbytagnamens)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMElement hasAttributeNS::]](https://developer.apple.com/documentation/webkit/domelement/1476177-hasattributens)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMElement.innerText](https://developer.apple.com/documentation/webkit/domelement/1476267-innertext)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMElement.lastElementChild](https://developer.apple.com/documentation/webkit/domelement/1476232-lastelementchild)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMElement *lastElementChild ``` |
| To | ``` @property(readonly, strong) DOMElement *lastElementChild ``` |

Modified [DOMElement.nextElementSibling](https://developer.apple.com/documentation/webkit/domelement/1476197-nextelementsibling)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMElement *nextElementSibling ``` |
| To | ``` @property(readonly, strong) DOMElement *nextElementSibling ``` |

Modified [DOMElement.offsetParent](https://developer.apple.com/documentation/webkit/domelement/1476168-offsetparent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMElement *offsetParent ``` |
| To | ``` @property(readonly, strong) DOMElement *offsetParent ``` |

Modified [DOMElement.previousElementSibling](https://developer.apple.com/documentation/webkit/domelement/1476212-previouselementsibling)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMElement *previousElementSibling ``` |
| To | ``` @property(readonly, strong) DOMElement *previousElementSibling ``` |

Modified [-[DOMElement removeAttributeNS::]](https://developer.apple.com/documentation/webkit/domelement/1476254-removeattributens)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMElement scrollByLines:]](https://developer.apple.com/documentation/webkit/domelement/1476265-scrollbylines)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMElement scrollByPages:]](https://developer.apple.com/documentation/webkit/domelement/1476183-scrollbypages)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMElement setAttribute::]](https://developer.apple.com/documentation/webkit/domelement/1476210-setattribute)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMElement setAttributeNS:::]](https://developer.apple.com/documentation/webkit/domelement/1476220-setattributens)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMElement.style](https://developer.apple.com/documentation/webkit/domelement/1476234-style)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSStyleDeclaration *style ``` |
| To | ``` @property(readonly, strong) DOMCSSStyleDeclaration *style ``` |

Modified [-[DOMElement webkitRequestFullScreen:]](https://developer.apple.com/documentation/webkit/domelement/1476160-webkitrequestfullscreen)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [DOM_ALLOW_KEYBOARD_INPUT](https://developer.apple.com/documentation/webkit/1476191-dom_keyboard_input_enumeration_l/dom_allow_keyboard_input)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.4 |

DOMEntity.hModified [DOMEntity](https://developer.apple.com/documentation/webkit/domentity)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMEntityReference.hModified [DOMEntityReference](https://developer.apple.com/documentation/webkit/domentityreference)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMEvent.hModified [DOMEvent](https://developer.apple.com/documentation/webkit/domevent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMEvent.currentTarget](https://developer.apple.com/documentation/webkit/domevent/1536521-currenttarget)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id<DOMEventTarget> currentTarget ``` |
| To | ``` @property(readonly, strong) id<DOMEventTarget> currentTarget ``` |

Modified [-[DOMEvent initEvent:::]](https://developer.apple.com/documentation/webkit/domevent/1558621-initevent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMEvent.srcElement](https://developer.apple.com/documentation/webkit/domevent/1537830-srcelement)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id<DOMEventTarget> srcElement ``` |
| To | ``` @property(readonly, strong) id<DOMEventTarget> srcElement ``` |

Modified [DOMEvent.target](https://developer.apple.com/documentation/webkit/domevent/1537539-target)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id<DOMEventTarget> target ``` |
| To | ``` @property(readonly, strong) id<DOMEventTarget> target ``` |

Modified [DOM_AT_TARGET](https://developer.apple.com/documentation/webkit/dom_at_target)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_BUBBLING_PHASE](https://developer.apple.com/documentation/webkit/dom_bubbling_phase)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CAPTURING_PHASE](https://developer.apple.com/documentation/webkit/dom_capturing_phase)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_NONE](https://developer.apple.com/documentation/webkit/1558620-dom_phase_enumeration_legacy/dom_none)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.4 |

DOMEventException.hModified [DOMEventException](https://developer.apple.com/documentation/webkit/domeventexception)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMEventExceptionCode](https://developer.apple.com/documentation/webkit/domeventexceptioncode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_UNSPECIFIED_EVENT_TYPE_ERR](https://developer.apple.com/documentation/webkit/domeventexceptioncode/dom_unspecified_event_type_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMEventListener.hModified [DOMEventListener](https://developer.apple.com/documentation/webkit/domeventlistener)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMEventTarget.hModified [DOMEventTarget](https://developer.apple.com/documentation/webkit/domeventtarget)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMEventTarget addEventListener:::]](https://developer.apple.com/documentation/webkit/domeventtarget/1562690-addeventlistener)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMEventTarget removeEventListener:::]](https://developer.apple.com/documentation/webkit/domeventtarget/1562691-removeeventlistener)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMException.hModified [DOMException](https://developer.apple.com/documentation/webkit/domexception)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMExceptionCode](https://developer.apple.com/documentation/webkit/domexceptioncode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_DOMSTRING_SIZE_ERR](https://developer.apple.com/documentation/webkit/dom_domstring_size_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_HIERARCHY_REQUEST_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_hierarchy_request_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_INDEX_SIZE_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_index_size_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_INUSE_ATTRIBUTE_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_inuse_attribute_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_INVALID_ACCESS_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_invalid_access_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_INVALID_CHARACTER_ERR](https://developer.apple.com/documentation/webkit/dom_invalid_character_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_INVALID_MODIFICATION_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_invalid_modification_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_INVALID_STATE_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_invalid_state_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_NAMESPACE_ERR](https://developer.apple.com/documentation/webkit/dom_namespace_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_NOT_FOUND_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_not_found_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_NOT_SUPPORTED_ERR](https://developer.apple.com/documentation/webkit/dom_not_supported_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_NO_DATA_ALLOWED_ERR](https://developer.apple.com/documentation/webkit/dom_no_data_allowed_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_NO_MODIFICATION_ALLOWED_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_no_modification_allowed_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SYNTAX_ERR](https://developer.apple.com/documentation/webkit/dom_syntax_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_WRONG_DOCUMENT_ERR](https://developer.apple.com/documentation/webkit/domexceptioncode/dom_wrong_document_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLAnchorElement.hModified [DOMHTMLAnchorElement](https://developer.apple.com/documentation/webkit/domhtmlanchorelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLAnchorElement.accessKey](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520533-accesskey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.8 |

Modified [DOMHTMLAnchorElement.hashName](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520517-hashname)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAnchorElement.host](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520525-host)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAnchorElement.hostname](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520544-hostname)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAnchorElement.pathname](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520546-pathname)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAnchorElement.port](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520543-port)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAnchorElement.protocol](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520536-protocol)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAnchorElement.search](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520538-search)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAnchorElement.text](https://developer.apple.com/documentation/webkit/domhtmlanchorelement/1520530-text)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLAppletElement.hModified [DOMHTMLAppletElement](https://developer.apple.com/documentation/webkit/domhtmlappletelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLAreaElement.hModified [DOMHTMLAreaElement](https://developer.apple.com/documentation/webkit/domhtmlareaelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLAreaElement.accessKey](https://developer.apple.com/documentation/webkit/domhtmlareaelement/1561543-accesskey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.8 |

Modified [DOMHTMLAreaElement.hashName](https://developer.apple.com/documentation/webkit/domhtmlareaelement/1536873-hashname)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAreaElement.host](https://developer.apple.com/documentation/webkit/domhtmlareaelement/1537392-host)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAreaElement.hostname](https://developer.apple.com/documentation/webkit/domhtmlareaelement/1536646-hostname)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAreaElement.pathname](https://developer.apple.com/documentation/webkit/domhtmlareaelement/1537152-pathname)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAreaElement.port](https://developer.apple.com/documentation/webkit/domhtmlareaelement/1537490-port)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAreaElement.protocol](https://developer.apple.com/documentation/webkit/domhtmlareaelement/1537449-protocol)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLAreaElement.search](https://developer.apple.com/documentation/webkit/domhtmlareaelement/1537177-search)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLBRElement.hModified [DOMHTMLBRElement](https://developer.apple.com/documentation/webkit/domhtmlbrelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLBaseElement.hModified [DOMHTMLBaseElement](https://developer.apple.com/documentation/webkit/domhtmlbaseelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLBaseFontElement.hModified [DOMHTMLBaseFontElement](https://developer.apple.com/documentation/webkit/domhtmlbasefontelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLBodyElement.hModified [DOMHTMLBodyElement](https://developer.apple.com/documentation/webkit/domhtmlbodyelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLButtonElement.hModified [DOMHTMLButtonElement](https://developer.apple.com/documentation/webkit/domhtmlbuttonelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLButtonElement.accessKey](https://developer.apple.com/documentation/webkit/domhtmlbuttonelement/1532486-accesskey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.8 |

Modified [-[DOMHTMLButtonElement click]](https://developer.apple.com/documentation/webkit/domhtmlbuttonelement/1532489-click)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLButtonElement.form](https://developer.apple.com/documentation/webkit/domhtmlbuttonelement/1532490-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

DOMHTMLCollection.hModified [DOMHTMLCollection](https://developer.apple.com/documentation/webkit/domhtmlcollection)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLDListElement.hModified [DOMHTMLDListElement](https://developer.apple.com/documentation/webkit/domhtmldlistelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLDirectoryElement.hModified [DOMHTMLDirectoryElement](https://developer.apple.com/documentation/webkit/domhtmldirectoryelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLDivElement.hModified [DOMHTMLDivElement](https://developer.apple.com/documentation/webkit/domhtmldivelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLDocument.hRemoved DOMHTMLDocument.activeElementRemoved -[DOMHTMLDocument hasFocus]Modified [DOMHTMLDocument](https://developer.apple.com/documentation/webkit/domhtmldocument)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLDocument.alinkColor](https://developer.apple.com/documentation/webkit/domhtmldocument/1537988-alinkcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.bgColor](https://developer.apple.com/documentation/webkit/domhtmldocument/1536465-bgcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMHTMLDocument captureEvents]](https://developer.apple.com/documentation/webkit/domhtmldocument/1536980-captureevents)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.designMode](https://developer.apple.com/documentation/webkit/domhtmldocument/1537419-designmode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.dir](https://developer.apple.com/documentation/webkit/domhtmldocument/1536350-dir)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.embeds](https://developer.apple.com/documentation/webkit/domhtmldocument/1536475-embeds)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *embeds ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMHTMLCollection *embeds ``` | OS X 10.5 |

Modified [DOMHTMLDocument.fgColor](https://developer.apple.com/documentation/webkit/domhtmldocument/1537009-fgcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.height](https://developer.apple.com/documentation/webkit/domhtmldocument/1537520-height)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.linkColor](https://developer.apple.com/documentation/webkit/domhtmldocument/1536376-linkcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.plugins](https://developer.apple.com/documentation/webkit/domhtmldocument/1537594-plugins)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *plugins ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMHTMLCollection *plugins ``` | OS X 10.5 |

Modified [-[DOMHTMLDocument releaseEvents]](https://developer.apple.com/documentation/webkit/domhtmldocument/1538173-releaseevents)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.scripts](https://developer.apple.com/documentation/webkit/domhtmldocument/1537858-scripts)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *scripts ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMHTMLCollection *scripts ``` | OS X 10.5 |

Modified [DOMHTMLDocument.vlinkColor](https://developer.apple.com/documentation/webkit/domhtmldocument/1536209-vlinkcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLDocument.width](https://developer.apple.com/documentation/webkit/domhtmldocument/1537477-width)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLElement.hModified [DOMHTMLElement](https://developer.apple.com/documentation/webkit/domhtmlelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLElement.children](https://developer.apple.com/documentation/webkit/domhtmlelement/1536217-children)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *children ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *children ``` |

DOMHTMLEmbedElement.hModified [DOMHTMLEmbedElement](https://developer.apple.com/documentation/webkit/domhtmlembedelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLFieldSetElement.hModified [DOMHTMLFieldSetElement](https://developer.apple.com/documentation/webkit/domhtmlfieldsetelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLFieldSetElement.form](https://developer.apple.com/documentation/webkit/domhtmlfieldsetelement/1434336-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

DOMHTMLFontElement.hModified [DOMHTMLFontElement](https://developer.apple.com/documentation/webkit/domhtmlfontelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLFormElement.hModified [DOMHTMLFormElement](https://developer.apple.com/documentation/webkit/domhtmlformelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLFormElement.elements](https://developer.apple.com/documentation/webkit/domhtmlformelement/1536542-elements)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *elements ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *elements ``` |

Modified [DOMHTMLFormElement.encoding](https://developer.apple.com/documentation/webkit/domhtmlformelement/1536853-encoding)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLFrameElement.hModified [DOMHTMLFrameElement](https://developer.apple.com/documentation/webkit/domhtmlframeelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLFrameElement.contentDocument](https://developer.apple.com/documentation/webkit/domhtmlframeelement/1537430-contentdocument)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMDocument *contentDocument ``` |
| To | ``` @property(readonly, strong) DOMDocument *contentDocument ``` |

Modified [DOMHTMLFrameElement.contentWindow](https://developer.apple.com/documentation/webkit/domhtmlframeelement/1536585-contentwindow)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMAbstractView *contentWindow ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMAbstractView *contentWindow ``` | OS X 10.5 |

Modified [DOMHTMLFrameElement.height](https://developer.apple.com/documentation/webkit/domhtmlframeelement/1537462-height)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLFrameElement.location](https://developer.apple.com/documentation/webkit/domhtmlframeelement/1537620-location)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLFrameElement.width](https://developer.apple.com/documentation/webkit/domhtmlframeelement/1536831-width)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLFrameSetElement.hModified [DOMHTMLFrameSetElement](https://developer.apple.com/documentation/webkit/domhtmlframesetelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLHRElement.hModified [DOMHTMLHRElement](https://developer.apple.com/documentation/webkit/domhtmlhrelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLHeadElement.hModified [DOMHTMLHeadElement](https://developer.apple.com/documentation/webkit/domhtmlheadelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLHeadingElement.hModified [DOMHTMLHeadingElement](https://developer.apple.com/documentation/webkit/domhtmlheadingelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLHtmlElement.hModified [DOMHTMLHtmlElement](https://developer.apple.com/documentation/webkit/domhtmlhtmlelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLIFrameElement.hModified [DOMHTMLIFrameElement](https://developer.apple.com/documentation/webkit/domhtmliframeelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLIFrameElement.contentDocument](https://developer.apple.com/documentation/webkit/domhtmliframeelement/1408826-contentdocument)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMDocument *contentDocument ``` |
| To | ``` @property(readonly, strong) DOMDocument *contentDocument ``` |

Modified [DOMHTMLIFrameElement.contentWindow](https://developer.apple.com/documentation/webkit/domhtmliframeelement/1408822-contentwindow)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMAbstractView *contentWindow ``` |
| To | ``` @property(readonly, strong) DOMAbstractView *contentWindow ``` |

DOMHTMLImageElement.hModified [DOMHTMLImageElement](https://developer.apple.com/documentation/webkit/domhtmlimageelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLImageElement.complete](https://developer.apple.com/documentation/webkit/domhtmlimageelement/1538017-complete)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLImageElement.lowsrc](https://developer.apple.com/documentation/webkit/domhtmlimageelement/1537045-lowsrc)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLImageElement.naturalHeight](https://developer.apple.com/documentation/webkit/domhtmlimageelement/1536371-naturalheight)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLImageElement.naturalWidth](https://developer.apple.com/documentation/webkit/domhtmlimageelement/1536592-naturalwidth)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLImageElement.x](https://developer.apple.com/documentation/webkit/domhtmlimageelement/1537737-x)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLImageElement.y](https://developer.apple.com/documentation/webkit/domhtmlimageelement/1537605-y)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLInputElement.hModified [DOMHTMLInputElement](https://developer.apple.com/documentation/webkit/domhtmlinputelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLInputElement.accessKey](https://developer.apple.com/documentation/webkit/domhtmlinputelement/1501440-accesskey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.8 |

Modified [DOMHTMLInputElement.files](https://developer.apple.com/documentation/webkit/domhtmlinputelement/1501400-files)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) DOMFileList *files ``` |
| To | ``` @property(strong) DOMFileList *files ``` |

Modified [DOMHTMLInputElement.form](https://developer.apple.com/documentation/webkit/domhtmlinputelement/1501406-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

Modified [DOMHTMLInputElement.indeterminate](https://developer.apple.com/documentation/webkit/domhtmlinputelement/1501402-indeterminate)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLInputElement.selectionEnd](https://developer.apple.com/documentation/webkit/domhtmlinputelement/1501428-selectionend)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLInputElement.selectionStart](https://developer.apple.com/documentation/webkit/domhtmlinputelement/1501414-selectionstart)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMHTMLInputElement setSelectionRange:end:]](https://developer.apple.com/documentation/webkit/domhtmlinputelement/1501412-setselectionrange)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLLIElement.hModified [DOMHTMLLIElement](https://developer.apple.com/documentation/webkit/domhtmllielement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLLabelElement.hModified [DOMHTMLLabelElement](https://developer.apple.com/documentation/webkit/domhtmllabelelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLLabelElement.accessKey](https://developer.apple.com/documentation/webkit/domhtmllabelelement/1563240-accesskey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.8 |

Modified [DOMHTMLLabelElement.form](https://developer.apple.com/documentation/webkit/domhtmllabelelement/1536216-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

DOMHTMLLegendElement.hModified [DOMHTMLLegendElement](https://developer.apple.com/documentation/webkit/domhtmllegendelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLLegendElement.accessKey](https://developer.apple.com/documentation/webkit/domhtmllegendelement/1493970-accesskey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.8 |

Modified [DOMHTMLLegendElement.form](https://developer.apple.com/documentation/webkit/domhtmllegendelement/1493972-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

DOMHTMLLinkElement.hModified [DOMHTMLLinkElement](https://developer.apple.com/documentation/webkit/domhtmllinkelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLLinkElement.sheet](https://developer.apple.com/documentation/webkit/domhtmllinkelement/1537427-sheet)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMStyleSheet *sheet ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMStyleSheet *sheet ``` | OS X 10.4 |

DOMHTMLMapElement.hModified [DOMHTMLMapElement](https://developer.apple.com/documentation/webkit/domhtmlmapelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLMapElement.areas](https://developer.apple.com/documentation/webkit/domhtmlmapelement/1537887-areas)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *areas ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *areas ``` |

DOMHTMLMenuElement.hModified [DOMHTMLMenuElement](https://developer.apple.com/documentation/webkit/domhtmlmenuelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLMetaElement.hModified [DOMHTMLMetaElement](https://developer.apple.com/documentation/webkit/domhtmlmetaelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLModElement.hModified [DOMHTMLModElement](https://developer.apple.com/documentation/webkit/domhtmlmodelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLOListElement.hModified [DOMHTMLOListElement](https://developer.apple.com/documentation/webkit/domhtmlolistelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLObjectElement.hModified [DOMHTMLObjectElement](https://developer.apple.com/documentation/webkit/domhtmlobjectelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLObjectElement.contentDocument](https://developer.apple.com/documentation/webkit/domhtmlobjectelement/1431106-contentdocument)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMDocument *contentDocument ``` |
| To | ``` @property(readonly, strong) DOMDocument *contentDocument ``` |

Modified [DOMHTMLObjectElement.form](https://developer.apple.com/documentation/webkit/domhtmlobjectelement/1431096-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

DOMHTMLOptGroupElement.hModified [DOMHTMLOptGroupElement](https://developer.apple.com/documentation/webkit/domhtmloptgroupelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLOptionElement.hModified [DOMHTMLOptionElement](https://developer.apple.com/documentation/webkit/domhtmloptionelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLOptionElement.form](https://developer.apple.com/documentation/webkit/domhtmloptionelement/1536539-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

DOMHTMLOptionsCollection.hModified [DOMHTMLOptionsCollection](https://developer.apple.com/documentation/webkit/domhtmloptionscollection)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMHTMLOptionsCollection add:index:]](https://developer.apple.com/documentation/webkit/domhtmloptionscollection/1506877-add)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLOptionsCollection.selectedIndex](https://developer.apple.com/documentation/webkit/domhtmloptionscollection/1506880-selectedindex)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLParagraphElement.hModified [DOMHTMLParagraphElement](https://developer.apple.com/documentation/webkit/domhtmlparagraphelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLParamElement.hModified [DOMHTMLParamElement](https://developer.apple.com/documentation/webkit/domhtmlparamelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLPreElement.hModified [DOMHTMLPreElement](https://developer.apple.com/documentation/webkit/domhtmlpreelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLPreElement.wrap](https://developer.apple.com/documentation/webkit/domhtmlpreelement/1526260-wrap)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLQuoteElement.hModified [DOMHTMLQuoteElement](https://developer.apple.com/documentation/webkit/domhtmlquoteelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLScriptElement.hModified [DOMHTMLScriptElement](https://developer.apple.com/documentation/webkit/domhtmlscriptelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLSelectElement.hModified [DOMHTMLSelectElement](https://developer.apple.com/documentation/webkit/domhtmlselectelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMHTMLSelectElement add::]](https://developer.apple.com/documentation/webkit/domhtmlselectelement/1403432-add)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLSelectElement.form](https://developer.apple.com/documentation/webkit/domhtmlselectelement/1403409-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

Modified [DOMHTMLSelectElement.options](https://developer.apple.com/documentation/webkit/domhtmlselectelement/1403417-options)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLOptionsCollection *options ``` |
| To | ``` @property(readonly, strong) DOMHTMLOptionsCollection *options ``` |

DOMHTMLStyleElement.hModified [DOMHTMLStyleElement](https://developer.apple.com/documentation/webkit/domhtmlstyleelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLStyleElement.sheet](https://developer.apple.com/documentation/webkit/domhtmlstyleelement/1435839-sheet)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMStyleSheet *sheet ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMStyleSheet *sheet ``` | OS X 10.4 |

DOMHTMLTableCaptionElement.hModified [DOMHTMLTableCaptionElement](https://developer.apple.com/documentation/webkit/domhtmltablecaptionelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLTableCellElement.hModified [DOMHTMLTableCellElement](https://developer.apple.com/documentation/webkit/domhtmltablecellelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLTableColElement.hModified [DOMHTMLTableColElement](https://developer.apple.com/documentation/webkit/domhtmltablecolelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLTableElement.hModified [DOMHTMLTableElement](https://developer.apple.com/documentation/webkit/domhtmltableelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLTableElement.caption](https://developer.apple.com/documentation/webkit/domhtmltableelement/1416132-caption)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) DOMHTMLTableCaptionElement *caption ``` |
| To | ``` @property(strong) DOMHTMLTableCaptionElement *caption ``` |

Modified [DOMHTMLTableElement.rows](https://developer.apple.com/documentation/webkit/domhtmltableelement/1416112-rows)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *rows ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *rows ``` |

Modified [DOMHTMLTableElement.tBodies](https://developer.apple.com/documentation/webkit/domhtmltableelement/1416116-tbodies)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *tBodies ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *tBodies ``` |

Modified [DOMHTMLTableElement.tFoot](https://developer.apple.com/documentation/webkit/domhtmltableelement/1416140-tfoot)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) DOMHTMLTableSectionElement *tFoot ``` |
| To | ``` @property(strong) DOMHTMLTableSectionElement *tFoot ``` |

Modified [DOMHTMLTableElement.tHead](https://developer.apple.com/documentation/webkit/domhtmltableelement/1416118-thead)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) DOMHTMLTableSectionElement *tHead ``` |
| To | ``` @property(strong) DOMHTMLTableSectionElement *tHead ``` |

DOMHTMLTableRowElement.hModified [DOMHTMLTableRowElement](https://developer.apple.com/documentation/webkit/domhtmltablerowelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLTableRowElement.cells](https://developer.apple.com/documentation/webkit/domhtmltablerowelement/1538048-cells)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *cells ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *cells ``` |

DOMHTMLTableSectionElement.hModified [DOMHTMLTableSectionElement](https://developer.apple.com/documentation/webkit/domhtmltablesectionelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLTableSectionElement.rows](https://developer.apple.com/documentation/webkit/domhtmltablesectionelement/1488611-rows)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLCollection *rows ``` |
| To | ``` @property(readonly, strong) DOMHTMLCollection *rows ``` |

DOMHTMLTextAreaElement.hModified [DOMHTMLTextAreaElement](https://developer.apple.com/documentation/webkit/domhtmltextareaelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMHTMLTextAreaElement.accessKey](https://developer.apple.com/documentation/webkit/domhtmltextareaelement/1550798-accesskey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.4 | OS X 10.8 |

Modified [DOMHTMLTextAreaElement.form](https://developer.apple.com/documentation/webkit/domhtmltextareaelement/1538021-form)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMHTMLFormElement *form ``` |
| To | ``` @property(readonly, strong) DOMHTMLFormElement *form ``` |

Modified [DOMHTMLTextAreaElement.selectionEnd](https://developer.apple.com/documentation/webkit/domhtmltextareaelement/1536559-selectionend)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMHTMLTextAreaElement.selectionStart](https://developer.apple.com/documentation/webkit/domhtmltextareaelement/1537441-selectionstart)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMHTMLTextAreaElement setSelectionRange:end:]](https://developer.apple.com/documentation/webkit/domhtmltextareaelement/1537436-setselectionrange)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMHTMLTitleElement.hModified [DOMHTMLTitleElement](https://developer.apple.com/documentation/webkit/domhtmltitleelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMHTMLUListElement.hModified [DOMHTMLUListElement](https://developer.apple.com/documentation/webkit/domhtmlulistelement)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMImplementation.hModified [DOMImplementation](https://developer.apple.com/documentation/webkit/domimplementation)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMImplementation createCSSStyleSheet::]](https://developer.apple.com/documentation/webkit/domimplementation/1426483-createcssstylesheet)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMImplementation createDocument:::]](https://developer.apple.com/documentation/webkit/domimplementation/1426473-createdocument)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMImplementation createDocumentType:::]](https://developer.apple.com/documentation/webkit/domimplementation/1426476-createdocumenttype)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMImplementation hasFeature::]](https://developer.apple.com/documentation/webkit/domimplementation/1426475-hasfeature)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMKeyboardEvent.hAdded [-[DOMKeyboardEvent initKeyboardEvent:canBubble:cancelable:view:keyIdentifier:location:ctrlKey:altKey:shiftKey:metaKey:]](https://developer.apple.com/documentation/webkit/domkeyboardevent/1476923-initkeyboardevent)Added [-[DOMKeyboardEvent initKeyboardEvent:canBubble:cancelable:view:keyIdentifier:location:ctrlKey:altKey:shiftKey:metaKey:altGraphKey:]](https://developer.apple.com/documentation/webkit/domkeyboardevent/1476909-initkeyboardevent)Added [DOMKeyboardEvent.location](https://developer.apple.com/documentation/webkit/domkeyboardevent/1476943-location)Modified [DOMKeyboardEvent.altGraphKey](https://developer.apple.com/documentation/webkit/domkeyboardevent/1476941-altgraphkey)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMKeyboardEvent initKeyboardEvent:canBubble:cancelable:view:keyIdentifier:keyLocation:ctrlKey:altKey:shiftKey:metaKey:]](https://developer.apple.com/documentation/webkit/domkeyboardevent/1476930-initkeyboardevent)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.5 | OS X 10.5 |

Modified [-[DOMKeyboardEvent initKeyboardEvent:canBubble:cancelable:view:keyIdentifier:keyLocation:ctrlKey:altKey:shiftKey:metaKey:altGraphKey:]](https://developer.apple.com/documentation/webkit/domkeyboardevent/1476915-initkeyboardevent)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.5 | OS X 10.5 |

Modified [DOMKeyboardEvent.keyLocation](https://developer.apple.com/documentation/webkit/domkeyboardevent/1476938-keylocation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.5 |

DOMMediaList.hModified [DOMMediaList](https://developer.apple.com/documentation/webkit/dommedialist)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMMouseEvent.hModified [DOMMouseEvent](https://developer.apple.com/documentation/webkit/dommouseevent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMMouseEvent.fromElement](https://developer.apple.com/documentation/webkit/dommouseevent/1399598-fromelement)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMNode *fromElement ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMNode *fromElement ``` | OS X 10.5 |

Modified [-[DOMMouseEvent initMouseEvent:::::::::::::::]](https://developer.apple.com/documentation/webkit/dommouseevent/1399602-initmouseevent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMMouseEvent.offsetX](https://developer.apple.com/documentation/webkit/dommouseevent/1399594-offsetx)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMMouseEvent.offsetY](https://developer.apple.com/documentation/webkit/dommouseevent/1399581-offsety)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMMouseEvent.relatedTarget](https://developer.apple.com/documentation/webkit/dommouseevent/1399585-relatedtarget)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id<DOMEventTarget> relatedTarget ``` |
| To | ``` @property(readonly, strong) id<DOMEventTarget> relatedTarget ``` |

Modified [DOMMouseEvent.toElement](https://developer.apple.com/documentation/webkit/dommouseevent/1399596-toelement)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMNode *toElement ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMNode *toElement ``` | OS X 10.5 |

Modified [DOMMouseEvent.x](https://developer.apple.com/documentation/webkit/dommouseevent/1399567-x)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMMouseEvent.y](https://developer.apple.com/documentation/webkit/dommouseevent/1399575-y)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMMutationEvent.hModified [DOMMutationEvent](https://developer.apple.com/documentation/webkit/dommutationevent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMMutationEvent initMutationEvent::::::::]](https://developer.apple.com/documentation/webkit/dommutationevent/1393654-initmutationevent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMMutationEvent.relatedNode](https://developer.apple.com/documentation/webkit/dommutationevent/1393670-relatednode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *relatedNode ``` |
| To | ``` @property(readonly, strong) DOMNode *relatedNode ``` |

Modified [DOM_ADDITION](https://developer.apple.com/documentation/webkit/1393660-dom_modification_enumeration_leg/dom_addition)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_MODIFICATION](https://developer.apple.com/documentation/webkit/dom_modification)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_REMOVAL](https://developer.apple.com/documentation/webkit/dom_removal)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMNamedNodeMap.hModified [DOMNamedNodeMap](https://developer.apple.com/documentation/webkit/domnamednodemap)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMNamedNodeMap getNamedItemNS::]](https://developer.apple.com/documentation/webkit/domnamednodemap/1400529-getnameditemns)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMNamedNodeMap removeNamedItemNS::]](https://developer.apple.com/documentation/webkit/domnamednodemap/1400545-removenameditemns)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMNode.hModified [DOMNode](https://developer.apple.com/documentation/webkit/domnode)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMNode.attributes](https://developer.apple.com/documentation/webkit/domnode/1517965-attributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNamedNodeMap *attributes ``` |
| To | ``` @property(readonly, strong) DOMNamedNodeMap *attributes ``` |

Modified [DOMNode.baseURI](https://developer.apple.com/documentation/webkit/domnode/1517916-baseuri)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMNode.childNodes](https://developer.apple.com/documentation/webkit/domnode/1517959-childnodes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNodeList *childNodes ``` |
| To | ``` @property(readonly, strong) DOMNodeList *childNodes ``` |

Modified [-[DOMNode contains:]](https://developer.apple.com/documentation/webkit/domnode/1517986-contains)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.5 |

Modified [DOMNode.firstChild](https://developer.apple.com/documentation/webkit/domnode/1517947-firstchild)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *firstChild ``` |
| To | ``` @property(readonly, strong) DOMNode *firstChild ``` |

Modified [-[DOMNode insertBefore::]](https://developer.apple.com/documentation/webkit/domnode/1517937-insertbefore)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMNode.isContentEditable](https://developer.apple.com/documentation/webkit/domnode/1517934-iscontenteditable)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMNode isDefaultNamespace:]](https://developer.apple.com/documentation/webkit/domnode/1517928-isdefaultnamespace)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMNode isSupported::]](https://developer.apple.com/documentation/webkit/domnode/1517933-issupported)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMNode.lastChild](https://developer.apple.com/documentation/webkit/domnode/1517918-lastchild)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *lastChild ``` |
| To | ``` @property(readonly, strong) DOMNode *lastChild ``` |

Modified [-[DOMNode lookupNamespaceURI:]](https://developer.apple.com/documentation/webkit/domnode/1517970-lookupnamespaceuri)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMNode lookupPrefix:]](https://developer.apple.com/documentation/webkit/domnode/1517950-lookupprefix)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMNode.nextSibling](https://developer.apple.com/documentation/webkit/domnode/1517936-nextsibling)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *nextSibling ``` |
| To | ``` @property(readonly, strong) DOMNode *nextSibling ``` |

Modified [DOMNode.ownerDocument](https://developer.apple.com/documentation/webkit/domnode/1517917-ownerdocument)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMDocument *ownerDocument ``` |
| To | ``` @property(readonly, strong) DOMDocument *ownerDocument ``` |

Modified [DOMNode.parentElement](https://developer.apple.com/documentation/webkit/domnode/1517963-parentelement)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMElement *parentElement ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMElement *parentElement ``` | OS X 10.5 |

Modified [DOMNode.parentNode](https://developer.apple.com/documentation/webkit/domnode/1517952-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *parentNode ``` |
| To | ``` @property(readonly, strong) DOMNode *parentNode ``` |

Modified [DOMNode.previousSibling](https://developer.apple.com/documentation/webkit/domnode/1517926-previoussibling)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *previousSibling ``` |
| To | ``` @property(readonly, strong) DOMNode *previousSibling ``` |

Modified [-[DOMNode replaceChild::]](https://developer.apple.com/documentation/webkit/domnode/1517973-replacechild)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_ATTRIBUTE_NODE](https://developer.apple.com/documentation/webkit/dom_attribute_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_CDATA_SECTION_NODE](https://developer.apple.com/documentation/webkit/dom_cdata_section_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_COMMENT_NODE](https://developer.apple.com/documentation/webkit/dom_comment_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_FRAGMENT_NODE](https://developer.apple.com/documentation/webkit/dom_document_fragment_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_NODE](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_document_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_POSITION_CONTAINED_BY](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_document_position_contained_by)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_POSITION_CONTAINS](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_document_position_contains)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_POSITION_DISCONNECTED](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_document_position_disconnected)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_POSITION_FOLLOWING](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_document_position_following)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC](https://developer.apple.com/documentation/webkit/dom_document_position_implementation_specific)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_POSITION_PRECEDING](https://developer.apple.com/documentation/webkit/dom_document_position_preceding)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_DOCUMENT_TYPE_NODE](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_document_type_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_ELEMENT_NODE](https://developer.apple.com/documentation/webkit/dom_element_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_ENTITY_NODE](https://developer.apple.com/documentation/webkit/dom_entity_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_ENTITY_REFERENCE_NODE](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_entity_reference_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_NOTATION_NODE](https://developer.apple.com/documentation/webkit/dom_notation_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_PROCESSING_INSTRUCTION_NODE](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_processing_instruction_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_TEXT_NODE](https://developer.apple.com/documentation/webkit/1517978-dom_element_enumeration_legacy/dom_text_node)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMNodeFilter.hModified [DOMNodeFilter](https://developer.apple.com/documentation/webkit/domnodefilter)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_FILTER_ACCEPT](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_filter_accept)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_FILTER_REJECT](https://developer.apple.com/documentation/webkit/dom_filter_reject)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_FILTER_SKIP](https://developer.apple.com/documentation/webkit/dom_filter_skip)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_ALL](https://developer.apple.com/documentation/webkit/dom_show_all)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_ATTRIBUTE](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_attribute)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_CDATA_SECTION](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_cdata_section)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_COMMENT](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_comment)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_DOCUMENT](https://developer.apple.com/documentation/webkit/dom_show_document)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_DOCUMENT_FRAGMENT](https://developer.apple.com/documentation/webkit/dom_show_document_fragment)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_DOCUMENT_TYPE](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_document_type)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_ELEMENT](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_element)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_ENTITY](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_entity)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_ENTITY_REFERENCE](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_entity_reference)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_NOTATION](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_notation)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_PROCESSING_INSTRUCTION](https://developer.apple.com/documentation/webkit/1455659-dom_filter_enumeration_legacy/dom_show_processing_instruction)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_SHOW_TEXT](https://developer.apple.com/documentation/webkit/dom_show_text)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMNodeIterator.hModified [DOMNodeIterator](https://developer.apple.com/documentation/webkit/domnodeiterator)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMNodeIterator.filter](https://developer.apple.com/documentation/webkit/domnodeiterator/1496188-filter)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id<DOMNodeFilter> filter ``` |
| To | ``` @property(readonly, strong) id<DOMNodeFilter> filter ``` |

Modified [DOMNodeIterator.pointerBeforeReferenceNode](https://developer.apple.com/documentation/webkit/domnodeiterator/1496184-pointerbeforereferencenode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMNodeIterator.referenceNode](https://developer.apple.com/documentation/webkit/domnodeiterator/1496178-referencenode)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMNode *referenceNode ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMNode *referenceNode ``` | OS X 10.5 |

Modified [DOMNodeIterator.root](https://developer.apple.com/documentation/webkit/domnodeiterator/1496186-root)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *root ``` |
| To | ``` @property(readonly, strong) DOMNode *root ``` |

DOMNodeList.hModified [DOMNodeList](https://developer.apple.com/documentation/webkit/domnodelist)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMNotation.hModified DOMNotation

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMObject.hModified [DOMObject](https://developer.apple.com/documentation/webkit/domobject)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMObject.sheet](https://developer.apple.com/documentation/webkit/domobject/1521125-sheet)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMStyleSheet *sheet ``` | OS X 10.3 |
| To | ``` @property(readonly, strong) DOMStyleSheet *sheet ``` | OS X 10.4 |

DOMProcessingInstruction.hRemoved DOMProcessingInstruction.dataModified [DOMProcessingInstruction](https://developer.apple.com/documentation/webkit/domprocessinginstruction)

|  | Superclasses | Introduction |
| --- | --- | --- |
| From | DOMNode | OS X 10.3 |
| To | DOMCharacterData | OS X 10.4 |

Modified [DOMProcessingInstruction.sheet](https://developer.apple.com/documentation/webkit/domprocessinginstruction/1537207-sheet)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(readonly, retain) DOMStyleSheet *sheet ``` | OS X 10.6 |
| To | ``` @property(readonly, strong) DOMStyleSheet *sheet ``` | OS X 10.4 |

DOMRGBColor.hModified [DOMRGBColor](https://developer.apple.com/documentation/webkit/domrgbcolor)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMRGBColor.alpha](https://developer.apple.com/documentation/webkit/domrgbcolor/1434383-alpha)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSPrimitiveValue *alpha ``` |
| To | ``` @property(readonly, strong) DOMCSSPrimitiveValue *alpha ``` |

Modified [DOMRGBColor.blue](https://developer.apple.com/documentation/webkit/domrgbcolor/1434389-blue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSPrimitiveValue *blue ``` |
| To | ``` @property(readonly, strong) DOMCSSPrimitiveValue *blue ``` |

Modified [DOMRGBColor.green](https://developer.apple.com/documentation/webkit/domrgbcolor/1434385-green)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSPrimitiveValue *green ``` |
| To | ``` @property(readonly, strong) DOMCSSPrimitiveValue *green ``` |

Modified [DOMRGBColor.red](https://developer.apple.com/documentation/webkit/domrgbcolor/1434387-red)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSPrimitiveValue *red ``` |
| To | ``` @property(readonly, strong) DOMCSSPrimitiveValue *red ``` |

DOMRange.hModified [DOMRange](https://developer.apple.com/documentation/webkit/domrange)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMRange.commonAncestorContainer](https://developer.apple.com/documentation/webkit/domrange/1403325-commonancestorcontainer)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *commonAncestorContainer ``` |
| To | ``` @property(readonly, strong) DOMNode *commonAncestorContainer ``` |

Modified [-[DOMRange compareBoundaryPoints::]](https://developer.apple.com/documentation/webkit/domrange/1403308-compareboundarypoints)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMRange compareNode:]](https://developer.apple.com/documentation/webkit/domrange/1403284-comparenode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMRange comparePoint:offset:]](https://developer.apple.com/documentation/webkit/domrange/1403306-comparepoint)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMRange createContextualFragment:]](https://developer.apple.com/documentation/webkit/domrange/1403317-createcontextualfragment)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMRange.endContainer](https://developer.apple.com/documentation/webkit/domrange/1403294-endcontainer)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *endContainer ``` |
| To | ``` @property(readonly, strong) DOMNode *endContainer ``` |

Modified [-[DOMRange intersectsNode:]](https://developer.apple.com/documentation/webkit/domrange/1403302-intersectsnode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMRange isPointInRange:offset:]](https://developer.apple.com/documentation/webkit/domrange/1403282-ispointinrange)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMRange setEnd::]](https://developer.apple.com/documentation/webkit/domrange/1403288-setend)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[DOMRange setStart::]](https://developer.apple.com/documentation/webkit/domrange/1403274-setstart)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMRange.startContainer](https://developer.apple.com/documentation/webkit/domrange/1403271-startcontainer)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *startContainer ``` |
| To | ``` @property(readonly, strong) DOMNode *startContainer ``` |

Modified [DOM_END_TO_END](https://developer.apple.com/documentation/webkit/1403298-dom_direction_enumeration_legacy/dom_end_to_end)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_END_TO_START](https://developer.apple.com/documentation/webkit/dom_end_to_start)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_NODE_AFTER](https://developer.apple.com/documentation/webkit/1403298-dom_direction_enumeration_legacy/dom_node_after)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.4 |

Modified [DOM_NODE_BEFORE](https://developer.apple.com/documentation/webkit/1403298-dom_direction_enumeration_legacy/dom_node_before)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.4 |

Modified [DOM_NODE_BEFORE_AND_AFTER](https://developer.apple.com/documentation/webkit/1403298-dom_direction_enumeration_legacy/dom_node_before_and_after)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.4 |

Modified [DOM_NODE_INSIDE](https://developer.apple.com/documentation/webkit/dom_node_inside)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.4 |

Modified [DOM_START_TO_END](https://developer.apple.com/documentation/webkit/1403298-dom_direction_enumeration_legacy/dom_start_to_end)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_START_TO_START](https://developer.apple.com/documentation/webkit/dom_start_to_start)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMRangeException.hModified [DOMRangeException](https://developer.apple.com/documentation/webkit/domrangeexception)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMRangeExceptionCode](https://developer.apple.com/documentation/webkit/domrangeexceptioncode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_BAD_BOUNDARYPOINTS_ERR](https://developer.apple.com/documentation/webkit/domrangeexceptioncode/dom_bad_boundarypoints_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOM_INVALID_NODE_TYPE_ERR](https://developer.apple.com/documentation/webkit/dom_invalid_node_type_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMRect.hModified [DOMRect](https://developer.apple.com/documentation/webkit/domrect)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMRect.bottom](https://developer.apple.com/documentation/webkit/domrect/1538166-bottom)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSPrimitiveValue *bottom ``` |
| To | ``` @property(readonly, strong) DOMCSSPrimitiveValue *bottom ``` |

Modified [DOMRect.left](https://developer.apple.com/documentation/webkit/domrect/1536183-left)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSPrimitiveValue *left ``` |
| To | ``` @property(readonly, strong) DOMCSSPrimitiveValue *left ``` |

Modified [DOMRect.right](https://developer.apple.com/documentation/webkit/domrect/1537297-right)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSPrimitiveValue *right ``` |
| To | ``` @property(readonly, strong) DOMCSSPrimitiveValue *right ``` |

Modified [DOMRect.top](https://developer.apple.com/documentation/webkit/domrect/1536491-top)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMCSSPrimitiveValue *top ``` |
| To | ``` @property(readonly, strong) DOMCSSPrimitiveValue *top ``` |

DOMStyleSheet.hModified [DOMStyleSheet](https://developer.apple.com/documentation/webkit/domstylesheet)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMStyleSheet.media](https://developer.apple.com/documentation/webkit/domstylesheet/1537510-media)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMMediaList *media ``` |
| To | ``` @property(readonly, strong) DOMMediaList *media ``` |

Modified [DOMStyleSheet.ownerNode](https://developer.apple.com/documentation/webkit/domstylesheet/1537401-ownernode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *ownerNode ``` |
| To | ``` @property(readonly, strong) DOMNode *ownerNode ``` |

Modified [DOMStyleSheet.parentStyleSheet](https://developer.apple.com/documentation/webkit/domstylesheet/1536562-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMStyleSheet *parentStyleSheet ``` |
| To | ``` @property(readonly, strong) DOMStyleSheet *parentStyleSheet ``` |

DOMStyleSheetList.hModified [DOMStyleSheetList](https://developer.apple.com/documentation/webkit/domstylesheetlist)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMText.hModified [DOMText](https://developer.apple.com/documentation/webkit/domtext)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

DOMTreeWalker.hModified [DOMTreeWalker](https://developer.apple.com/documentation/webkit/domtreewalker)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMTreeWalker.currentNode](https://developer.apple.com/documentation/webkit/domtreewalker/1396811-currentnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) DOMNode *currentNode ``` |
| To | ``` @property(strong) DOMNode *currentNode ``` |

Modified [DOMTreeWalker.filter](https://developer.apple.com/documentation/webkit/domtreewalker/1396807-filter)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) id<DOMNodeFilter> filter ``` |
| To | ``` @property(readonly, strong) id<DOMNodeFilter> filter ``` |

Modified [DOMTreeWalker.root](https://developer.apple.com/documentation/webkit/domtreewalker/1396799-root)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *root ``` |
| To | ``` @property(readonly, strong) DOMNode *root ``` |

DOMUIEvent.hModified [DOMUIEvent](https://developer.apple.com/documentation/webkit/domuievent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMUIEvent.charCode](https://developer.apple.com/documentation/webkit/domuievent/1409591-charcode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [-[DOMUIEvent initUIEvent:::::]](https://developer.apple.com/documentation/webkit/domuievent/1409589-inituievent)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [DOMUIEvent.keyCode](https://developer.apple.com/documentation/webkit/domuievent/1409602-keycode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMUIEvent.layerX](https://developer.apple.com/documentation/webkit/domuievent/1409610-layerx)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | OS X 10.8 |
| To | OS X 10.5 | OS X 10.5 |

Modified [DOMUIEvent.layerY](https://developer.apple.com/documentation/webkit/domuievent/1409595-layery)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | OS X 10.8 |
| To | OS X 10.5 | OS X 10.5 |

Modified [DOMUIEvent.pageX](https://developer.apple.com/documentation/webkit/domuievent/1409601-pagex)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMUIEvent.pageY](https://developer.apple.com/documentation/webkit/domuievent/1409597-pagey)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMUIEvent.view](https://developer.apple.com/documentation/webkit/domuievent/1409606-view)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMAbstractView *view ``` |
| To | ``` @property(readonly, strong) DOMAbstractView *view ``` |

Modified [DOMUIEvent.which](https://developer.apple.com/documentation/webkit/domuievent/1409608-which)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

DOMWheelEvent.hModified [-[DOMWheelEvent initWheelEvent:wheelDeltaY:view:screenX:screenY:clientX:clientY:ctrlKey:altKey:shiftKey:metaKey:]](https://developer.apple.com/documentation/webkit/domwheelevent/1420221-initwheelevent)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMWheelEvent.wheelDeltaX](https://developer.apple.com/documentation/webkit/domwheelevent/1420223-wheeldeltax)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOMWheelEvent.wheelDeltaY](https://developer.apple.com/documentation/webkit/domwheelevent/1420210-wheeldeltay)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.5 |

Modified [DOM_DOM_DELTA_LINE](https://developer.apple.com/documentation/webkit/1420212-dom_delta_enumeration_legacy/dom_dom_delta_line)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.5 |

Modified [DOM_DOM_DELTA_PAGE](https://developer.apple.com/documentation/webkit/1420212-dom_delta_enumeration_legacy/dom_dom_delta_page)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.5 |

Modified [DOM_DOM_DELTA_PIXEL](https://developer.apple.com/documentation/webkit/1420212-dom_delta_enumeration_legacy/dom_dom_delta_pixel)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.5 |

DOMXPathException.hModified [DOMXPathException](https://developer.apple.com/documentation/webkit/domxpathexception)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.4 |

Modified [DOMXPathExceptionCode](https://developer.apple.com/documentation/webkit/domxpathexceptioncode)

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.4 |

Modified [DOM_INVALID_EXPRESSION_ERR](https://developer.apple.com/documentation/webkit/dom_invalid_expression_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.4 |

Modified [DOM_TYPE_ERR](https://developer.apple.com/documentation/webkit/dom_type_err)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.4 |

DOMXPathResult.hModified [DOMXPathResult.singleNodeValue](https://developer.apple.com/documentation/webkit/domxpathresult/1537445-singlenodevalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain) DOMNode *singleNodeValue ``` |
| To | ``` @property(readonly, strong) DOMNode *singleNodeValue ``` |

HIWebView.hModified HIWebViewCreate()

|  | Introduction |
| --- | --- |
| From | OS X 10.2 |
| To | OS X 10.3 |

Modified HIWebViewGetWebView()

|  | Introduction |
| --- | --- |
| From | OS X 10.2 |
| To | OS X 10.3 |

WKBackForwardList.h (Added)Added [WKBackForwardList](https://developer.apple.com/documentation/webkit/wkbackforwardlist)Added [WKBackForwardList.backItem](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516693-backitem)Added [WKBackForwardList.backList](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516698-backlist)Added [WKBackForwardList.currentItem](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516703-currentitem)Added [WKBackForwardList.forwardItem](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516700-forwarditem)Added [WKBackForwardList.forwardList](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516701-forwardlist)Added [-[WKBackForwardList itemAtIndex:]](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516694-item)WKBackForwardListItem.h (Added)Added [WKBackForwardListItem](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem)Added [WKBackForwardListItem.URL](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem/1455513-url)Added [WKBackForwardListItem.initialURL](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem/1455507-initialurl)Added [WKBackForwardListItem.title](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem/1455511-title)WKError.h (Added)Added [WKErrorCode](https://developer.apple.com/documentation/webkit/wkerrorcode)Added [WKErrorDomain](https://developer.apple.com/documentation/webkit/wkerrordomain)Added [WKErrorJavaScriptExceptionOccurred](https://developer.apple.com/documentation/webkit/wkerrorcode/wkerrorjavascriptexceptionoccurred)Added [WKErrorUnknown](https://developer.apple.com/documentation/webkit/wkerror/code/unknown)Added [WKErrorWebContentProcessTerminated](https://developer.apple.com/documentation/webkit/wkerror/code/webcontentprocessterminated)Added [WKErrorWebViewInvalidated](https://developer.apple.com/documentation/webkit/wkerrorcode/wkerrorwebviewinvalidated)WKFoundation.h (Added)Added [#def WK_API_ENABLED](https://developer.apple.com/documentation/webkit/wk_api_enabled)Added #def WK_EXTERNWKFrameInfo.h (Added)Added [WKFrameInfo](https://developer.apple.com/documentation/webkit/wkframeinfo)Added [WKFrameInfo.mainFrame](https://developer.apple.com/documentation/webkit/wkframeinfo/1503096-ismainframe)Added [WKFrameInfo.request](https://developer.apple.com/documentation/webkit/wkframeinfo/1503091-request)WKNavigation.h (Added)Added [WKNavigation](https://developer.apple.com/documentation/webkit/wknavigation)WKNavigationAction.h (Added)Added [WKNavigationAction](https://developer.apple.com/documentation/webkit/wknavigationaction)Added [WKNavigationAction.buttonNumber](https://developer.apple.com/documentation/webkit/wknavigationaction/1401916-buttonnumber)Added [WKNavigationAction.modifierFlags](https://developer.apple.com/documentation/webkit/wknavigationaction/1401934-modifierflags)Added [WKNavigationAction.navigationType](https://developer.apple.com/documentation/webkit/wknavigationaction/1401914-navigationtype)Added [WKNavigationAction.request](https://developer.apple.com/documentation/webkit/wknavigationaction/1401910-request)Added [WKNavigationAction.sourceFrame](https://developer.apple.com/documentation/webkit/wknavigationaction/1401926-sourceframe)Added [WKNavigationAction.targetFrame](https://developer.apple.com/documentation/webkit/wknavigationaction/1401918-targetframe)Added [WKNavigationType](https://developer.apple.com/documentation/webkit/wknavigationtype)Added [WKNavigationTypeBackForward](https://developer.apple.com/documentation/webkit/wknavigationtype/backforward)Added [WKNavigationTypeFormResubmitted](https://developer.apple.com/documentation/webkit/wknavigationtype/wknavigationtypeformresubmitted)Added [WKNavigationTypeFormSubmitted](https://developer.apple.com/documentation/webkit/wknavigationtype/formsubmitted)Added [WKNavigationTypeLinkActivated](https://developer.apple.com/documentation/webkit/wknavigationtype/wknavigationtypelinkactivated)Added [WKNavigationTypeOther](https://developer.apple.com/documentation/webkit/wknavigationtype/wknavigationtypeother)Added [WKNavigationTypeReload](https://developer.apple.com/documentation/webkit/wknavigationtype/reload)WKNavigationDelegate.h (Added)Added [WKNavigationDelegate](https://developer.apple.com/documentation/webkit/wknavigationdelegate)Added [-[WKNavigationDelegate webView:decidePolicyForNavigationAction:decisionHandler:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455641-webview)Added [-[WKNavigationDelegate webView:decidePolicyForNavigationResponse:decisionHandler:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455643-webview)Added [-[WKNavigationDelegate webView:didCommitNavigation:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455635-webview)Added [-[WKNavigationDelegate webView:didFailNavigation:withError:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455623-webview)Added [-[WKNavigationDelegate webView:didFailProvisionalNavigation:withError:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455637-webview)Added [-[WKNavigationDelegate webView:didFinishNavigation:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455629-webview)Added [-[WKNavigationDelegate webView:didReceiveAuthenticationChallenge:completionHandler:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455638-webview)Added [-[WKNavigationDelegate webView:didReceiveServerRedirectForProvisionalNavigation:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455627-webview)Added [-[WKNavigationDelegate webView:didStartProvisionalNavigation:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455621-webview)Added [WKNavigationActionPolicy](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy)Added [WKNavigationActionPolicyAllow](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy/wknavigationactionpolicyallow)Added [WKNavigationActionPolicyCancel](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy/cancel)Added [WKNavigationResponsePolicy](https://developer.apple.com/documentation/webkit/wknavigationresponsepolicy)Added [WKNavigationResponsePolicyAllow](https://developer.apple.com/documentation/webkit/wknavigationresponsepolicy/allow)Added [WKNavigationResponsePolicyCancel](https://developer.apple.com/documentation/webkit/wknavigationresponsepolicy/cancel)WKNavigationResponse.h (Added)Added [WKNavigationResponse](https://developer.apple.com/documentation/webkit/wknavigationresponse)Added [WKNavigationResponse.canShowMIMEType](https://developer.apple.com/documentation/webkit/wknavigationresponse/1459480-canshowmimetype)Added [WKNavigationResponse.forMainFrame](https://developer.apple.com/documentation/webkit/wknavigationresponse/1459482-isformainframe)Added [WKNavigationResponse.response](https://developer.apple.com/documentation/webkit/wknavigationresponse/1459484-response)WKPreferences.h (Added)Added [WKPreferences](https://developer.apple.com/documentation/webkit/wkpreferences)Added [WKPreferences.javaEnabled](https://developer.apple.com/documentation/webkit/wkpreferences/1538062-javaenabled)Added [WKPreferences.javaScriptCanOpenWindowsAutomatically](https://developer.apple.com/documentation/webkit/wkpreferences/1536573-javascriptcanopenwindowsautomati)Added [WKPreferences.javaScriptEnabled](https://developer.apple.com/documentation/webkit/wkpreferences/1536203-javascriptenabled)Added [WKPreferences.minimumFontSize](https://developer.apple.com/documentation/webkit/wkpreferences/1537155-minimumfontsize)Added [WKPreferences.plugInsEnabled](https://developer.apple.com/documentation/webkit/wkpreferences/1536894-pluginsenabled)WKProcessPool.h (Added)Added [WKProcessPool](https://developer.apple.com/documentation/webkit/wkprocesspool)WKScriptMessage.h (Added)Added [WKScriptMessage](https://developer.apple.com/documentation/webkit/wkscriptmessage)Added [WKScriptMessage.body](https://developer.apple.com/documentation/webkit/wkscriptmessage/1417901-body)Added [WKScriptMessage.frameInfo](https://developer.apple.com/documentation/webkit/wkscriptmessage/1417906-frameinfo)Added [WKScriptMessage.name](https://developer.apple.com/documentation/webkit/wkscriptmessage/1417908-name)Added [WKScriptMessage.webView](https://developer.apple.com/documentation/webkit/wkscriptmessage/1417903-webview)WKScriptMessageHandler.h (Added)Added [WKScriptMessageHandler](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler)Added [-[WKScriptMessageHandler userContentController:didReceiveScriptMessage:]](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler/1396222-usercontentcontroller)WKUIDelegate.h (Added)Added [WKUIDelegate](https://developer.apple.com/documentation/webkit/wkuidelegate)Added [-[WKUIDelegate webView:createWebViewWithConfiguration:forNavigationAction:windowFeatures:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1536907-webview)Added [-[WKUIDelegate webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:completionHandler:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1537406-webview)Added [-[WKUIDelegate webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:completionHandler:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1536489-webview)Added [-[WKUIDelegate webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:completionHandler:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1538086-webview)WKUserContentController.h (Added)Added [WKUserContentController](https://developer.apple.com/documentation/webkit/wkusercontentcontroller)Added [-[WKUserContentController addScriptMessageHandler:name:]](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1537172-addscriptmessagehandler)Added [-[WKUserContentController addUserScript:]](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1537448-adduserscript)Added [-[WKUserContentController removeAllUserScripts]](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1536540-removealluserscripts)Added [-[WKUserContentController removeScriptMessageHandlerForName:]](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1537532-removescriptmessagehandlerfornam)Added [WKUserContentController.userScripts](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1538046-userscripts)WKUserScript.h (Added)Added [WKUserScript](https://developer.apple.com/documentation/webkit/wkuserscript)Added [WKUserScript.forMainFrameOnly](https://developer.apple.com/documentation/webkit/wkuserscript/1537856-isformainframeonly)Added [-[WKUserScript initWithSource:injectionTime:forMainFrameOnly:]](https://developer.apple.com/documentation/webkit/wkuserscript/1537750-initwithsource)Added [WKUserScript.injectionTime](https://developer.apple.com/documentation/webkit/wkuserscript/1536492-injectiontime)Added [WKUserScript.source](https://developer.apple.com/documentation/webkit/wkuserscript/1537787-source)Added [WKUserScriptInjectionTime](https://developer.apple.com/documentation/webkit/wkuserscriptinjectiontime)Added [WKUserScriptInjectionTimeAtDocumentEnd](https://developer.apple.com/documentation/webkit/wkuserscriptinjectiontime/atdocumentend)Added [WKUserScriptInjectionTimeAtDocumentStart](https://developer.apple.com/documentation/webkit/wkuserscriptinjectiontime/atdocumentstart)WKWebView.h (Added)Added [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview)Added [WKWebView.UIDelegate](https://developer.apple.com/documentation/webkit/wkwebview/1415009-uidelegate)Added [WKWebView.URL](https://developer.apple.com/documentation/webkit/wkwebview/1415005-url)Added [WKWebView.allowsBackForwardNavigationGestures](https://developer.apple.com/documentation/webkit/wkwebview/1414995-allowsbackforwardnavigationgestu)Added [WKWebView.allowsMagnification](https://developer.apple.com/documentation/webkit/wkwebview/1414983-allowsmagnification)Added [WKWebView.backForwardList](https://developer.apple.com/documentation/webkit/wkwebview/1414977-backforwardlist)Added [WKWebView.canGoBack](https://developer.apple.com/documentation/webkit/wkwebview/1414966-cangoback)Added [WKWebView.canGoForward](https://developer.apple.com/documentation/webkit/wkwebview/1414962-cangoforward)Added [WKWebView.configuration](https://developer.apple.com/documentation/webkit/wkwebview/1414979-configuration)Added [WKWebView.estimatedProgress](https://developer.apple.com/documentation/webkit/wkwebview/1415007-estimatedprogress)Added [-[WKWebView evaluateJavaScript:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebview/1415017-evaluatejavascript)Added [-[WKWebView goBack]](https://developer.apple.com/documentation/webkit/wkwebview/1414952-goback)Added [-[WKWebView goBack:]](https://developer.apple.com/documentation/webkit/wkwebview/1414975-goback)Added [-[WKWebView goForward]](https://developer.apple.com/documentation/webkit/wkwebview/1414993-goforward)Added [-[WKWebView goForward:]](https://developer.apple.com/documentation/webkit/wkwebview/1414960-goforward)Added [-[WKWebView goToBackForwardListItem:]](https://developer.apple.com/documentation/webkit/wkwebview/1414991-go)Added [WKWebView.hasOnlySecureContent](https://developer.apple.com/documentation/webkit/wkwebview/1415002-hasonlysecurecontent)Added [-[WKWebView initWithFrame:configuration:]](https://developer.apple.com/documentation/webkit/wkwebview/1414998-initwithframe)Added [-[WKWebView loadHTMLString:baseURL:]](https://developer.apple.com/documentation/webkit/wkwebview/1415004-loadhtmlstring)Added [-[WKWebView loadRequest:]](https://developer.apple.com/documentation/webkit/wkwebview/1414954-loadrequest)Added [WKWebView.loading](https://developer.apple.com/documentation/webkit/wkwebview/1414964-isloading)Added [WKWebView.magnification](https://developer.apple.com/documentation/webkit/wkwebview/1414985-magnification)Added [WKWebView.navigationDelegate](https://developer.apple.com/documentation/webkit/wkwebview/1414971-navigationdelegate)Added [-[WKWebView reload]](https://developer.apple.com/documentation/webkit/wkwebview/1414969-reload)Added [-[WKWebView reload:]](https://developer.apple.com/documentation/webkit/wkwebview/1414987-reload)Added [-[WKWebView reloadFromOrigin]](https://developer.apple.com/documentation/webkit/wkwebview/1414956-reloadfromorigin)Added [-[WKWebView reloadFromOrigin:]](https://developer.apple.com/documentation/webkit/wkwebview/1414989-reloadfromorigin)Added [-[WKWebView setMagnification:centeredAtPoint:]](https://developer.apple.com/documentation/webkit/wkwebview/1414996-setmagnification)Added [-[WKWebView stopLoading]](https://developer.apple.com/documentation/webkit/wkwebview/1414981-stoploading)Added [-[WKWebView stopLoading:]](https://developer.apple.com/documentation/webkit/wkwebview/1415013-stoploading)Added [WKWebView.title](https://developer.apple.com/documentation/webkit/wkwebview/1415015-title)Added WKWebView(WKIBActions)WKWebViewConfiguration.h (Added)Added [WKWebViewConfiguration](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration)Added [WKWebViewConfiguration.preferences](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395666-preferences)Added [WKWebViewConfiguration.processPool](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395659-processpool)Added [WKWebViewConfiguration.suppressesIncrementalRendering](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395663-suppressesincrementalrendering)Added [WKWebViewConfiguration.userContentController](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395668-usercontentcontroller)WKWindowFeatures.h (Added)Added [WKWindowFeatures](https://developer.apple.com/documentation/webkit/wkwindowfeatures)Added [WKWindowFeatures.allowsResizing](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1536871-allowsresizing)Added [WKWindowFeatures.height](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1536826-height)Added [WKWindowFeatures.menuBarVisibility](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1538001-menubarvisibility)Added [WKWindowFeatures.statusBarVisibility](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1536638-statusbarvisibility)Added [WKWindowFeatures.toolbarsVisibility](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1536218-toolbarsvisibility)Added [WKWindowFeatures.width](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1537562-width)Added [WKWindowFeatures.x](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1537705-x)Added [WKWindowFeatures.y](https://developer.apple.com/documentation/webkit/wkwindowfeatures/1537052-y)WebArchive.hRemoved [-[WebArchive data]](https://developer.apple.com/documentation/webkit/webarchive/1407478-data)Removed [-[WebArchive mainResource]](https://developer.apple.com/documentation/webkit/webarchive/1407470-mainresource)Removed [-[WebArchive subframeArchives]](https://developer.apple.com/documentation/webkit/webarchive/1407472-subframearchives)Removed [-[WebArchive subresources]](https://developer.apple.com/documentation/webkit/webarchive/1407476-subresources)Added [WebArchive.data](https://developer.apple.com/documentation/webkit/webarchive/1407478-data)Added [WebArchive.mainResource](https://developer.apple.com/documentation/webkit/webarchive/1407470-mainresource)Added [WebArchive.subframeArchives](https://developer.apple.com/documentation/webkit/webarchive/1407472-subframearchives)Added [WebArchive.subresources](https://developer.apple.com/documentation/webkit/webarchive/1407476-subresources)Modified [-[WebArchive initWithData:]](https://developer.apple.com/documentation/webkit/webarchive/1407474-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data ``` |

Modified [-[WebArchive initWithMainResource:subresources:subframeArchives:]](https://developer.apple.com/documentation/webkit/webarchive/1407485-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMainResource:(WebResource *)mainResource subresources:(NSArray *)subresources subframeArchives:(NSArray *)subframeArchives ``` |
| To | ``` - (instancetype)initWithMainResource:(WebResource *)mainResource subresources:(NSArray *)subresources subframeArchives:(NSArray *)subframeArchives ``` |

WebBackForwardList.hRemoved [-[WebBackForwardList backItem]](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419963-backitem)Removed [-[WebBackForwardList backListCount]](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419934-backlistcount)Removed [-[WebBackForwardList capacity]](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419938-capacity)Removed [-[WebBackForwardList currentItem]](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419957-currentitem)Removed [-[WebBackForwardList forwardItem]](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419954-forwarditem)Removed [-[WebBackForwardList forwardListCount]](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419936-forwardlistcount)Removed [-[WebBackForwardList setCapacity:]](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419938-capacity)Added [WebBackForwardList.backItem](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419963-backitem)Added [WebBackForwardList.backListCount](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419934-backlistcount)Added [WebBackForwardList.capacity](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419938-capacity)Added [WebBackForwardList.currentItem](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419957-currentitem)Added [WebBackForwardList.forwardItem](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419954-forwarditem)Added [WebBackForwardList.forwardListCount](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419936-forwardlistcount)WebDOMOperations.hRemoved [-[DOMDocument webFrame]](https://developer.apple.com/documentation/webkit/domdocument/1536374-webframe)Removed [-[DOMHTMLFrameElement contentFrame]](https://developer.apple.com/documentation/webkit/domhtmlframeelement/1536194-contentframe)Removed [-[DOMHTMLIFrameElement contentFrame]](https://developer.apple.com/documentation/webkit/domhtmliframeelement/1537405-contentframe)Removed [-[DOMHTMLObjectElement contentFrame]](https://developer.apple.com/documentation/webkit/domhtmlobjectelement/1536848-contentframe)Removed [-[DOMNode webArchive]](https://developer.apple.com/documentation/webkit/domnode/1536220-webarchive)Removed [-[DOMRange markupString]](https://developer.apple.com/documentation/webkit/domrange/1537765-markupstring)Removed [-[DOMRange webArchive]](https://developer.apple.com/documentation/webkit/domrange/1536991-webarchive)Added [DOMDocument.webFrame](https://developer.apple.com/documentation/webkit/domdocument/1536374-webframe)Added [DOMHTMLFrameElement.contentFrame](https://developer.apple.com/documentation/webkit/domhtmlframeelement/1536194-contentframe)Added [DOMHTMLIFrameElement.contentFrame](https://developer.apple.com/documentation/webkit/domhtmliframeelement/1537405-contentframe)Added [DOMHTMLObjectElement.contentFrame](https://developer.apple.com/documentation/webkit/domhtmlobjectelement/1536848-contentframe)Added [DOMNode.webArchive](https://developer.apple.com/documentation/webkit/domnode/1536220-webarchive)Added [DOMRange.markupString](https://developer.apple.com/documentation/webkit/domrange/1537765-markupstring)Added [DOMRange.webArchive](https://developer.apple.com/documentation/webkit/domrange/1536991-webarchive)WebDataSource.hRemoved [-[WebDataSource data]](https://developer.apple.com/documentation/webkit/webdatasource/1529866-data)Removed [-[WebDataSource initialRequest]](https://developer.apple.com/documentation/webkit/webdatasource/1529871-initialrequest)Removed [-[WebDataSource isLoading]](https://developer.apple.com/documentation/webkit/webdatasource/1529868-loading)Removed [-[WebDataSource mainResource]](https://developer.apple.com/documentation/webkit/webdatasource/1529877-mainresource)Removed [-[WebDataSource pageTitle]](https://developer.apple.com/documentation/webkit/webdatasource/1529874-pagetitle)Removed [-[WebDataSource representation]](https://developer.apple.com/documentation/webkit/webdatasource/1529870-representation)Removed [-[WebDataSource request]](https://developer.apple.com/documentation/webkit/webdatasource/1529857-request)Removed [-[WebDataSource response]](https://developer.apple.com/documentation/webkit/webdatasource/1529858-response)Removed [-[WebDataSource subresources]](https://developer.apple.com/documentation/webkit/webdatasource/1529862-subresources)Removed [-[WebDataSource textEncodingName]](https://developer.apple.com/documentation/webkit/webdatasource/1529854-textencodingname)Removed [-[WebDataSource unreachableURL]](https://developer.apple.com/documentation/webkit/webdatasource/1529864-unreachableurl)Removed [-[WebDataSource webArchive]](https://developer.apple.com/documentation/webkit/webdatasource/1529856-webarchive)Removed [-[WebDataSource webFrame]](https://developer.apple.com/documentation/webkit/webdatasource/1529853-webframe)Added [WebDataSource.data](https://developer.apple.com/documentation/webkit/webdatasource/1529866-data)Added [WebDataSource.initialRequest](https://developer.apple.com/documentation/webkit/webdatasource/1529871-initialrequest)Added [WebDataSource.loading](https://developer.apple.com/documentation/webkit/webdatasource/1529868-loading)Added [WebDataSource.mainResource](https://developer.apple.com/documentation/webkit/webdatasource/1529877-mainresource)Added [WebDataSource.pageTitle](https://developer.apple.com/documentation/webkit/webdatasource/1529874-pagetitle)Added [WebDataSource.representation](https://developer.apple.com/documentation/webkit/webdatasource/1529870-representation)Added [WebDataSource.request](https://developer.apple.com/documentation/webkit/webdatasource/1529857-request)Added [WebDataSource.response](https://developer.apple.com/documentation/webkit/webdatasource/1529858-response)Added [WebDataSource.subresources](https://developer.apple.com/documentation/webkit/webdatasource/1529862-subresources)Added [WebDataSource.textEncodingName](https://developer.apple.com/documentation/webkit/webdatasource/1529854-textencodingname)Added [WebDataSource.unreachableURL](https://developer.apple.com/documentation/webkit/webdatasource/1529864-unreachableurl)Added [WebDataSource.webArchive](https://developer.apple.com/documentation/webkit/webdatasource/1529856-webarchive)Added [WebDataSource.webFrame](https://developer.apple.com/documentation/webkit/webdatasource/1529853-webframe)Modified [-[WebDataSource initWithRequest:]](https://developer.apple.com/documentation/webkit/webdatasource/1529860-initwithrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRequest:(NSURLRequest *)request ``` |
| To | ``` - (instancetype)initWithRequest:(NSURLRequest *)request ``` |

WebFrame.hRemoved [-[WebFrame DOMDocument]](https://developer.apple.com/documentation/webkit/webframe/1494248-domdocument)Removed [-[WebFrame childFrames]](https://developer.apple.com/documentation/webkit/webframe/1494257-childframes)Removed [-[WebFrame dataSource]](https://developer.apple.com/documentation/webkit/webframe/1494260-datasource)Removed [-[WebFrame frameElement]](https://developer.apple.com/documentation/webkit/webframe/1494267-frameelement)Removed [-[WebFrame frameView]](https://developer.apple.com/documentation/webkit/webframe/1494244-frameview)Removed [-[WebFrame globalContext]](https://developer.apple.com/documentation/webkit/webframe/1494270-globalcontext)Removed [-[WebFrame javaScriptContext]](https://developer.apple.com/documentation/webkit/webframe/1494240-javascriptcontext)Removed [-[WebFrame name]](https://developer.apple.com/documentation/webkit/webframe/1494252-name)Removed [-[WebFrame parentFrame]](https://developer.apple.com/documentation/webkit/webframe/1494254-parent)Removed [-[WebFrame provisionalDataSource]](https://developer.apple.com/documentation/webkit/webframe/1494238-provisionaldatasource)Removed [-[WebFrame webView]](https://developer.apple.com/documentation/webkit/webframe/1494259-webview)Removed [-[WebFrame windowObject]](https://developer.apple.com/documentation/webkit/webframe/1494239-windowobject)Added [WebFrame.DOMDocument](https://developer.apple.com/documentation/webkit/webframe/1494248-domdocument)Added [WebFrame.childFrames](https://developer.apple.com/documentation/webkit/webframe/1494257-childframes)Added [WebFrame.dataSource](https://developer.apple.com/documentation/webkit/webframe/1494260-datasource)Added [WebFrame.frameElement](https://developer.apple.com/documentation/webkit/webframe/1494267-frameelement)Added [WebFrame.frameView](https://developer.apple.com/documentation/webkit/webframe/1494244-frameview)Added [WebFrame.globalContext](https://developer.apple.com/documentation/webkit/webframe/1494270-globalcontext)Added [WebFrame.javaScriptContext](https://developer.apple.com/documentation/webkit/webframe/1494240-javascriptcontext)Added [WebFrame.name](https://developer.apple.com/documentation/webkit/webframe/1494252-name)Added [WebFrame.parentFrame](https://developer.apple.com/documentation/webkit/webframe/1494254-parentframe)Added [WebFrame.provisionalDataSource](https://developer.apple.com/documentation/webkit/webframe/1494238-provisionaldatasource)Added [WebFrame.webView](https://developer.apple.com/documentation/webkit/webframe/1494259-webview)Added [WebFrame.windowObject](https://developer.apple.com/documentation/webkit/webframe/1494239-windowobject)Modified [-[WebFrame initWithName:webFrameView:webView:]](https://developer.apple.com/documentation/webkit/webframe/1494255-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithName:(NSString *)name webFrameView:(WebFrameView *)view webView:(WebView *)webView ``` |
| To | ``` - (instancetype)initWithName:(NSString *)name webFrameView:(WebFrameView *)view webView:(WebView *)webView ``` |

WebFrameLoadDelegate.hModified -[NSObject webView:windowScriptObjectAvailable:]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | OS X 10.6 |
| To | OS X 10.4 | OS X 10.5 |

WebFrameView.hRemoved [-[WebFrameView allowsScrolling]](https://developer.apple.com/documentation/webkit/webframeview/1536807-allowsscrolling)Removed [-[WebFrameView canPrintHeadersAndFooters]](https://developer.apple.com/documentation/webkit/webframeview/1536876-canprintheadersandfooters)Removed [-[WebFrameView documentView]](https://developer.apple.com/documentation/webkit/webframeview/1536324-documentview)Removed [-[WebFrameView documentViewShouldHandlePrint]](https://developer.apple.com/documentation/webkit/webframeview/1538215-documentviewshouldhandleprint)Removed [-[WebFrameView setAllowsScrolling:]](https://developer.apple.com/documentation/webkit/webframeview/1536807-allowsscrolling)Removed [-[WebFrameView webFrame]](https://developer.apple.com/documentation/webkit/webframeview/1537506-webframe)Added [WebFrameView.allowsScrolling](https://developer.apple.com/documentation/webkit/webframeview/1536807-allowsscrolling)Added [WebFrameView.canPrintHeadersAndFooters](https://developer.apple.com/documentation/webkit/webframeview/1536876-canprintheadersandfooters)Added [WebFrameView.documentView](https://developer.apple.com/documentation/webkit/webframeview/1536324-documentview)Added [WebFrameView.documentViewShouldHandlePrint](https://developer.apple.com/documentation/webkit/webframeview/1538215-documentviewshouldhandleprint)Added [WebFrameView.webFrame](https://developer.apple.com/documentation/webkit/webframeview/1537506-webframe)WebHistory.hRemoved [-[WebHistory historyAgeInDaysLimit]](https://developer.apple.com/documentation/webkit/webhistory/1521415-historyageindayslimit)Removed [-[WebHistory historyItemLimit]](https://developer.apple.com/documentation/webkit/webhistory/1521410-historyitemlimit)Removed [-[WebHistory orderedLastVisitedDays]](https://developer.apple.com/documentation/webkit/webhistory/1521412-orderedlastvisiteddays)Removed [-[WebHistory setHistoryAgeInDaysLimit:]](https://developer.apple.com/documentation/webkit/webhistory/1521415-historyageindayslimit)Removed [-[WebHistory setHistoryItemLimit:]](https://developer.apple.com/documentation/webkit/webhistory/1521410-historyitemlimit)Added [WebHistory.historyAgeInDaysLimit](https://developer.apple.com/documentation/webkit/webhistory/1521415-historyageindayslimit)Added [WebHistory.historyItemLimit](https://developer.apple.com/documentation/webkit/webhistory/1521410-historyitemlimit)Added [WebHistory.orderedLastVisitedDays](https://developer.apple.com/documentation/webkit/webhistory/1521412-orderedlastvisiteddays)WebHistoryItem.hRemoved [-[WebHistoryItem URLString]](https://developer.apple.com/documentation/webkit/webhistoryitem/1525159-urlstring)Removed [-[WebHistoryItem alternateTitle]](https://developer.apple.com/documentation/webkit/webhistoryitem/1525149-alternatetitle)Removed [-[WebHistoryItem icon]](https://developer.apple.com/documentation/webkit/webhistoryitem/1525157-icon)Removed [-[WebHistoryItem lastVisitedTimeInterval]](https://developer.apple.com/documentation/webkit/webhistoryitem/1525148-lastvisitedtimeinterval)Removed [-[WebHistoryItem originalURLString]](https://developer.apple.com/documentation/webkit/webhistoryitem/1525155-originalurlstring)Removed [-[WebHistoryItem setAlternateTitle:]](https://developer.apple.com/documentation/webkit/webhistoryitem/1525149-alternatetitle)Removed [-[WebHistoryItem title]](https://developer.apple.com/documentation/webkit/webhistoryitem/1525158-title)Added [WebHistoryItem.URLString](https://developer.apple.com/documentation/webkit/webhistoryitem/1525159-urlstring)Added [WebHistoryItem.alternateTitle](https://developer.apple.com/documentation/webkit/webhistoryitem/1525149-alternatetitle)Added [WebHistoryItem.icon](https://developer.apple.com/documentation/webkit/webhistoryitem/1525157-icon)Added [WebHistoryItem.lastVisitedTimeInterval](https://developer.apple.com/documentation/webkit/webhistoryitem/1525148-lastvisitedtimeinterval)Added [WebHistoryItem.originalURLString](https://developer.apple.com/documentation/webkit/webhistoryitem/1525155-originalurlstring)Added [WebHistoryItem.title](https://developer.apple.com/documentation/webkit/webhistoryitem/1525158-title)Modified [-[WebHistoryItem initWithURLString:title:lastVisitedTimeInterval:]](https://developer.apple.com/documentation/webkit/webhistoryitem/1525150-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURLString:(NSString *)URLString title:(NSString *)title lastVisitedTimeInterval:(NSTimeInterval)time ``` |
| To | ``` - (instancetype)initWithURLString:(NSString *)URLString title:(NSString *)title lastVisitedTimeInterval:(NSTimeInterval)time ``` |

WebKitAvailability.h (Added)Added #def WEBKIT_AVAILABLE_MACAdded #def WEBKIT_CLASS_AVAILABLE_MACAdded #def WEBKIT_DEPRECATED_MACAdded #def WEBKIT_ENUM_AVAILABLE_MACAdded #def WebKit_WebKitAvailability_hWebKitLegacy.h (Added)WebPlugin.hRemoved [-[NSObject objectForWebScript]](https://developer.apple.com/documentation/objectivec/nsobject/1537612-objectforwebscript)Added [NSObject.objectForWebScript](https://developer.apple.com/documentation/objectivec/nsobject/1537612-objectforwebscript)WebPluginContainer.hRemoved [-[NSObject webFrame]](https://developer.apple.com/documentation/objectivec/nsobject/1537727-webframe)Removed [-[NSObject webPlugInContainerSelectionColor]](https://developer.apple.com/documentation/objectivec/nsobject/1536394-webplugincontainerselectioncolor)Added [NSObject.webFrame](https://developer.apple.com/documentation/objectivec/nsobject/1537727-webframe)Added [NSObject.webPlugInContainerSelectionColor](https://developer.apple.com/documentation/objectivec/nsobject/1536394-webplugincontainerselectioncolor)WebPreferences.hRemoved [-[WebPreferences allowsAnimatedImageLooping]](https://developer.apple.com/documentation/webkit/webpreferences/1537650-allowsanimatedimagelooping)Removed [-[WebPreferences allowsAnimatedImages]](https://developer.apple.com/documentation/webkit/webpreferences/1536208-allowsanimatedimages)Removed [-[WebPreferences arePlugInsEnabled]](https://developer.apple.com/documentation/webkit/webpreferences/1536911-pluginsenabled)Removed [-[WebPreferences autosaves]](https://developer.apple.com/documentation/webkit/webpreferences/1537467-autosaves)Removed [-[WebPreferences cacheModel]](https://developer.apple.com/documentation/webkit/webpreferences/1537584-cachemodel)Removed [-[WebPreferences cursiveFontFamily]](https://developer.apple.com/documentation/webkit/webpreferences/1536182-cursivefontfamily)Removed [-[WebPreferences defaultFixedFontSize]](https://developer.apple.com/documentation/webkit/webpreferences/1536790-defaultfixedfontsize)Removed [-[WebPreferences defaultFontSize]](https://developer.apple.com/documentation/webkit/webpreferences/1537812-defaultfontsize)Removed [-[WebPreferences defaultTextEncodingName]](https://developer.apple.com/documentation/webkit/webpreferences/1538190-defaulttextencodingname)Removed [-[WebPreferences fantasyFontFamily]](https://developer.apple.com/documentation/webkit/webpreferences/1537494-fantasyfontfamily)Removed [-[WebPreferences fixedFontFamily]](https://developer.apple.com/documentation/webkit/webpreferences/1537421-fixedfontfamily)Removed [-[WebPreferences identifier]](https://developer.apple.com/documentation/webkit/webpreferences/1537598-identifier)Removed [-[WebPreferences isJavaEnabled]](https://developer.apple.com/documentation/webkit/webpreferences/1537951-isjavaenabled)Removed [-[WebPreferences isJavaScriptEnabled]](https://developer.apple.com/documentation/webkit/webpreferences/1536400-isjavascriptenabled)Removed [-[WebPreferences javaScriptCanOpenWindowsAutomatically]](https://developer.apple.com/documentation/webkit/webpreferences/1536441-javascriptcanopenwindowsautomati)Removed [-[WebPreferences loadsImagesAutomatically]](https://developer.apple.com/documentation/webkit/webpreferences/1537550-loadsimagesautomatically)Removed [-[WebPreferences minimumFontSize]](https://developer.apple.com/documentation/webkit/webpreferences/1536187-minimumfontsize)Removed [-[WebPreferences minimumLogicalFontSize]](https://developer.apple.com/documentation/webkit/webpreferences/1536959-minimumlogicalfontsize)Removed [-[WebPreferences privateBrowsingEnabled]](https://developer.apple.com/documentation/webkit/webpreferences/1537050-privatebrowsingenabled)Removed [-[WebPreferences sansSerifFontFamily]](https://developer.apple.com/documentation/webkit/webpreferences/1538221-sansseriffontfamily)Removed [-[WebPreferences serifFontFamily]](https://developer.apple.com/documentation/webkit/webpreferences/1536297-seriffontfamily)Removed [-[WebPreferences setAllowsAnimatedImageLooping:]](https://developer.apple.com/documentation/webkit/webpreferences/1537650-allowsanimatedimagelooping)Removed [-[WebPreferences setAllowsAnimatedImages:]](https://developer.apple.com/documentation/webkit/webpreferences/1536208-allowsanimatedimages)Removed [-[WebPreferences setAutosaves:]](https://developer.apple.com/documentation/webkit/webpreferences/1537467-autosaves)Removed [-[WebPreferences setCacheModel:]](https://developer.apple.com/documentation/webkit/webpreferences/1537584-cachemodel)Removed [-[WebPreferences setCursiveFontFamily:]](https://developer.apple.com/documentation/webkit/webpreferences/1536182-cursivefontfamily)Removed [-[WebPreferences setDefaultFixedFontSize:]](https://developer.apple.com/documentation/webkit/webpreferences/1536790-defaultfixedfontsize)Removed [-[WebPreferences setDefaultFontSize:]](https://developer.apple.com/documentation/webkit/webpreferences/1537812-defaultfontsize)Removed [-[WebPreferences setDefaultTextEncodingName:]](https://developer.apple.com/documentation/webkit/webpreferences/1538190-defaulttextencodingname)Removed [-[WebPreferences setFantasyFontFamily:]](https://developer.apple.com/documentation/webkit/webpreferences/1537494-fantasyfontfamily)Removed [-[WebPreferences setFixedFontFamily:]](https://developer.apple.com/documentation/webkit/webpreferences/1537421-fixedfontfamily)Removed [-[WebPreferences setJavaEnabled:]](https://developer.apple.com/documentation/webkit/webpreferences/1537951-javaenabled)Removed [-[WebPreferences setJavaScriptCanOpenWindowsAutomatically:]](https://developer.apple.com/documentation/webkit/webpreferences/1536441-javascriptcanopenwindowsautomati)Removed [-[WebPreferences setJavaScriptEnabled:]](https://developer.apple.com/documentation/webkit/webpreferences/1536400-javascriptenabled)Removed [-[WebPreferences setLoadsImagesAutomatically:]](https://developer.apple.com/documentation/webkit/webpreferences/1537550-loadsimagesautomatically)Removed [-[WebPreferences setMinimumFontSize:]](https://developer.apple.com/documentation/webkit/webpreferences/1536187-minimumfontsize)Removed [-[WebPreferences setMinimumLogicalFontSize:]](https://developer.apple.com/documentation/webkit/webpreferences/1536959-minimumlogicalfontsize)Removed [-[WebPreferences setPlugInsEnabled:]](https://developer.apple.com/documentation/webkit/webpreferences/1536911-pluginsenabled)Removed [-[WebPreferences setPrivateBrowsingEnabled:]](https://developer.apple.com/documentation/webkit/webpreferences/1537050-privatebrowsingenabled)Removed [-[WebPreferences setSansSerifFontFamily:]](https://developer.apple.com/documentation/webkit/webpreferences/1538221-sansseriffontfamily)Removed [-[WebPreferences setSerifFontFamily:]](https://developer.apple.com/documentation/webkit/webpreferences/1536297-seriffontfamily)Removed [-[WebPreferences setShouldPrintBackgrounds:]](https://developer.apple.com/documentation/webkit/webpreferences/1537774-shouldprintbackgrounds)Removed [-[WebPreferences setStandardFontFamily:]](https://developer.apple.com/documentation/webkit/webpreferences/1536642-standardfontfamily)Removed [-[WebPreferences setSuppressesIncrementalRendering:]](https://developer.apple.com/documentation/webkit/webpreferences/1537563-suppressesincrementalrendering)Removed [-[WebPreferences setTabsToLinks:]](https://developer.apple.com/documentation/webkit/webpreferences/1537210-tabstolinks)Removed [-[WebPreferences setUserStyleSheetEnabled:]](https://developer.apple.com/documentation/webkit/webpreferences/1536396-userstylesheetenabled)Removed -[WebPreferences setUserStyleSheetLocation:]Removed [-[WebPreferences setUsesPageCache:]](https://developer.apple.com/documentation/webkit/webpreferences/1537460-usespagecache)Removed [-[WebPreferences shouldPrintBackgrounds]](https://developer.apple.com/documentation/webkit/webpreferences/1537774-shouldprintbackgrounds)Removed [-[WebPreferences standardFontFamily]](https://developer.apple.com/documentation/webkit/webpreferences/1536642-standardfontfamily)Removed [-[WebPreferences suppressesIncrementalRendering]](https://developer.apple.com/documentation/webkit/webpreferences/1537563-suppressesincrementalrendering)Removed [-[WebPreferences tabsToLinks]](https://developer.apple.com/documentation/webkit/webpreferences/1537210-tabstolinks)Removed [-[WebPreferences userStyleSheetEnabled]](https://developer.apple.com/documentation/webkit/webpreferences/1536396-userstylesheetenabled)Removed -[WebPreferences userStyleSheetLocation]Removed [-[WebPreferences usesPageCache]](https://developer.apple.com/documentation/webkit/webpreferences/1537460-usespagecache)Added [WebPreferences.allowsAnimatedImageLooping](https://developer.apple.com/documentation/webkit/webpreferences/1537650-allowsanimatedimagelooping)Added [WebPreferences.allowsAnimatedImages](https://developer.apple.com/documentation/webkit/webpreferences/1536208-allowsanimatedimages)Added [WebPreferences.autosaves](https://developer.apple.com/documentation/webkit/webpreferences/1537467-autosaves)Added [WebPreferences.cacheModel](https://developer.apple.com/documentation/webkit/webpreferences/1537584-cachemodel)Added [WebPreferences.cursiveFontFamily](https://developer.apple.com/documentation/webkit/webpreferences/1536182-cursivefontfamily)Added [WebPreferences.defaultFixedFontSize](https://developer.apple.com/documentation/webkit/webpreferences/1536790-defaultfixedfontsize)Added [WebPreferences.defaultFontSize](https://developer.apple.com/documentation/webkit/webpreferences/1537812-defaultfontsize)Added [WebPreferences.defaultTextEncodingName](https://developer.apple.com/documentation/webkit/webpreferences/1538190-defaulttextencodingname)Added [WebPreferences.fantasyFontFamily](https://developer.apple.com/documentation/webkit/webpreferences/1537494-fantasyfontfamily)Added [WebPreferences.fixedFontFamily](https://developer.apple.com/documentation/webkit/webpreferences/1537421-fixedfontfamily)Added [WebPreferences.identifier](https://developer.apple.com/documentation/webkit/webpreferences/1537598-identifier)Added [WebPreferences.javaEnabled](https://developer.apple.com/documentation/webkit/webpreferences/1537951-isjavaenabled)Added [WebPreferences.javaScriptCanOpenWindowsAutomatically](https://developer.apple.com/documentation/webkit/webpreferences/1536441-javascriptcanopenwindowsautomati)Added [WebPreferences.javaScriptEnabled](https://developer.apple.com/documentation/webkit/webpreferences/1536400-isjavascriptenabled)Added [WebPreferences.loadsImagesAutomatically](https://developer.apple.com/documentation/webkit/webpreferences/1537550-loadsimagesautomatically)Added [WebPreferences.minimumFontSize](https://developer.apple.com/documentation/webkit/webpreferences/1536187-minimumfontsize)Added [WebPreferences.minimumLogicalFontSize](https://developer.apple.com/documentation/webkit/webpreferences/1536959-minimumlogicalfontsize)Added [WebPreferences.plugInsEnabled](https://developer.apple.com/documentation/webkit/webpreferences/1536911-pluginsenabled)Added [WebPreferences.privateBrowsingEnabled](https://developer.apple.com/documentation/webkit/webpreferences/1537050-privatebrowsingenabled)Added [WebPreferences.sansSerifFontFamily](https://developer.apple.com/documentation/webkit/webpreferences/1538221-sansseriffontfamily)Added [WebPreferences.serifFontFamily](https://developer.apple.com/documentation/webkit/webpreferences/1536297-seriffontfamily)Added [WebPreferences.shouldPrintBackgrounds](https://developer.apple.com/documentation/webkit/webpreferences/1537774-shouldprintbackgrounds)Added [WebPreferences.standardFontFamily](https://developer.apple.com/documentation/webkit/webpreferences/1536642-standardfontfamily)Added [WebPreferences.suppressesIncrementalRendering](https://developer.apple.com/documentation/webkit/webpreferences/1537563-suppressesincrementalrendering)Added [WebPreferences.tabsToLinks](https://developer.apple.com/documentation/webkit/webpreferences/1537210-tabstolinks)Added [WebPreferences.userStyleSheetEnabled](https://developer.apple.com/documentation/webkit/webpreferences/1536396-userstylesheetenabled)Added [WebPreferences.userStyleSheetLocation](https://developer.apple.com/documentation/webkit/webpreferences/1536744-userstylesheetlocation)Added [WebPreferences.usesPageCache](https://developer.apple.com/documentation/webkit/webpreferences/1537460-usespagecache)Modified [-[WebPreferences initWithIdentifier:]](https://developer.apple.com/documentation/webkit/webpreferences/1538194-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIdentifier:(NSString *)anIdentifier ``` |
| To | ``` - (instancetype)initWithIdentifier:(NSString *)anIdentifier ``` |

WebResource.hRemoved [-[WebResource MIMEType]](https://developer.apple.com/documentation/webkit/webresource/1392187-mimetype)Removed [-[WebResource URL]](https://developer.apple.com/documentation/webkit/webresource/1392195-url)Removed [-[WebResource data]](https://developer.apple.com/documentation/webkit/webresource/1392191-data)Removed [-[WebResource frameName]](https://developer.apple.com/documentation/webkit/webresource/1392193-framename)Removed [-[WebResource textEncodingName]](https://developer.apple.com/documentation/webkit/webresource/1392189-textencodingname)Added [WebResource.MIMEType](https://developer.apple.com/documentation/webkit/webresource/1392187-mimetype)Added [WebResource.URL](https://developer.apple.com/documentation/webkit/webresource/1392195-url)Added [WebResource.data](https://developer.apple.com/documentation/webkit/webresource/1392191-data)Added [WebResource.frameName](https://developer.apple.com/documentation/webkit/webresource/1392193-framename)Added [WebResource.textEncodingName](https://developer.apple.com/documentation/webkit/webresource/1392189-textencodingname)Modified [-[WebResource initWithData:URL:MIMEType:textEncodingName:frameName:]](https://developer.apple.com/documentation/webkit/webresource/1392185-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data URL:(NSURL *)URL MIMEType:(NSString *)MIMEType textEncodingName:(NSString *)textEncodingName frameName:(NSString *)frameName ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data URL:(NSURL *)URL MIMEType:(NSString *)MIMEType textEncodingName:(NSString *)textEncodingName frameName:(NSString *)frameName ``` |

WebScriptObject.hModified [-[NSObject finalizeForWebScript]](https://developer.apple.com/documentation/objectivec/nsobject/1528546-finalizeforwebscript)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[NSObject invokeDefaultMethodWithArguments:]](https://developer.apple.com/documentation/objectivec/nsobject/1528543-invokedefaultmethodwitharguments)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [-[NSObject invokeUndefinedMethodFromWebScript:withArguments:]](https://developer.apple.com/documentation/objectivec/nsobject/1528562-invokeundefinedmethod)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [+[NSObject isKeyExcludedFromWebScript:]](https://developer.apple.com/documentation/objectivec/nsobject/1528545-iskeyexcludedfromwebscript)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [+[NSObject isSelectorExcludedFromWebScript:]](https://developer.apple.com/documentation/objectivec/nsobject/1528532-isselectorexcludedfromwebscript)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [+[NSObject webScriptNameForKey:]](https://developer.apple.com/documentation/objectivec/nsobject/1528541-webscriptnameforkey)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [+[NSObject webScriptNameForSelector:]](https://developer.apple.com/documentation/objectivec/nsobject/1528539-webscriptnameforselector)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [WebScriptObject](https://developer.apple.com/documentation/webkit/webscriptobject)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

Modified [WebUndefined](https://developer.apple.com/documentation/webkit/webundefined)

|  | Introduction |
| --- | --- |
| From | OS X 10.3 |
| To | OS X 10.4 |

WebUIDelegate.hModified -[NSObject webView:runJavaScriptAlertPanelWithMessage:]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | OS X 10.6 |
| To | OS X 10.3 | OS X 10.5 |

Modified -[NSObject webView:runJavaScriptConfirmPanelWithMessage:]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | OS X 10.6 |
| To | OS X 10.3 | OS X 10.5 |

Modified -[NSObject webView:runJavaScriptTextInputPanelWithPrompt:defaultText:]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | OS X 10.6 |
| To | OS X 10.3 | OS X 10.5 |

Modified -[NSObject webView:setContentRect:]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | OS X 10.6 |
| To | OS X 10.3 | OS X 10.5 |

Modified -[NSObject webViewContentRect:]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | OS X 10.6 |
| To | OS X 10.3 | OS X 10.5 |

WebView.hRemoved [-[WebView UIDelegate]](https://developer.apple.com/documentation/webkit/webview/1408544-uidelegate)Removed [-[WebView applicationNameForUserAgent]](https://developer.apple.com/documentation/webkit/webview/1408381-applicationnameforuseragent)Removed [-[WebView backForwardList]](https://developer.apple.com/documentation/webkit/webview/1408403-backforwardlist)Removed [-[WebView canGoBack]](https://developer.apple.com/documentation/webkit/webview/1408500-cangoback)Removed [-[WebView canGoForward]](https://developer.apple.com/documentation/webkit/webview/1408444-cangoforward)Removed [-[WebView canMakeTextLarger]](https://developer.apple.com/documentation/webkit/webview/1408484-canmaketextlarger)Removed [-[WebView canMakeTextSmaller]](https://developer.apple.com/documentation/webkit/webview/1408347-canmaketextsmaller)Removed [-[WebView canMakeTextStandardSize]](https://developer.apple.com/documentation/webkit/webview/1408502-canmaketextstandardsize)Removed [-[WebView customTextEncodingName]](https://developer.apple.com/documentation/webkit/webview/1408397-customtextencodingname)Removed [-[WebView customUserAgent]](https://developer.apple.com/documentation/webkit/webview/1408377-customuseragent)Removed [-[WebView downloadDelegate]](https://developer.apple.com/documentation/webkit/webview/1408536-downloaddelegate)Removed [-[WebView drawsBackground]](https://developer.apple.com/documentation/webkit/webview/1408486-drawsbackground)Removed [-[WebView editingDelegate]](https://developer.apple.com/documentation/webkit/webview/1408349-editingdelegate)Removed [-[WebView estimatedProgress]](https://developer.apple.com/documentation/webkit/webview/1408538-estimatedprogress)Removed [-[WebView frameLoadDelegate]](https://developer.apple.com/documentation/webkit/webview/1408540-frameloaddelegate)Removed [-[WebView groupName]](https://developer.apple.com/documentation/webkit/webview/1408478-groupname)Removed [-[WebView hostWindow]](https://developer.apple.com/documentation/webkit/webview/1408574-hostwindow)Removed [-[WebView isContinuousSpellCheckingEnabled]](https://developer.apple.com/documentation/webkit/webview/1408385-continuousspellcheckingenabled)Removed [-[WebView isEditable]](https://developer.apple.com/documentation/webkit/webview/1408556-iseditable)Removed [-[WebView isLoading]](https://developer.apple.com/documentation/webkit/webview/1408566-loading)Removed [-[WebView mainFrame]](https://developer.apple.com/documentation/webkit/webview/1408470-mainframe)Removed [-[WebView mainFrameDocument]](https://developer.apple.com/documentation/webkit/webview/1408525-mainframedocument)Removed [-[WebView mainFrameIcon]](https://developer.apple.com/documentation/webkit/webview/1408527-mainframeicon)Removed [-[WebView mainFrameTitle]](https://developer.apple.com/documentation/webkit/webview/1408498-mainframetitle)Removed [-[WebView mainFrameURL]](https://developer.apple.com/documentation/webkit/webview/1408351-mainframeurl)Removed [-[WebView maintainsInactiveSelection]](https://developer.apple.com/documentation/webkit/webview/1408494-maintainsinactiveselection)Removed [-[WebView mediaStyle]](https://developer.apple.com/documentation/webkit/webview/1408514-mediastyle)Removed [-[WebView pasteboardTypesForSelection]](https://developer.apple.com/documentation/webkit/webview/1408353-pasteboardtypesforselection)Removed [-[WebView policyDelegate]](https://developer.apple.com/documentation/webkit/webview/1408391-policydelegate)Removed [-[WebView preferences]](https://developer.apple.com/documentation/webkit/webview/1408387-preferences)Removed [-[WebView preferencesIdentifier]](https://developer.apple.com/documentation/webkit/webview/1408545-preferencesidentifier)Removed [-[WebView resourceLoadDelegate]](https://developer.apple.com/documentation/webkit/webview/1408367-resourceloaddelegate)Removed [-[WebView selectedDOMRange]](https://developer.apple.com/documentation/webkit/webview/1408428-selecteddomrange)Removed [-[WebView selectedFrame]](https://developer.apple.com/documentation/webkit/webview/1408434-selectedframe)Removed [-[WebView selectionAffinity]](https://developer.apple.com/documentation/webkit/webview/1408452-selectionaffinity)Removed [-[WebView setApplicationNameForUserAgent:]](https://developer.apple.com/documentation/webkit/webview/1408381-applicationnameforuseragent)Removed [-[WebView setContinuousSpellCheckingEnabled:]](https://developer.apple.com/documentation/webkit/webview/1408385-continuousspellcheckingenabled)Removed [-[WebView setCustomTextEncodingName:]](https://developer.apple.com/documentation/webkit/webview/1408397-customtextencodingname)Removed [-[WebView setCustomUserAgent:]](https://developer.apple.com/documentation/webkit/webview/1408377-customuseragent)Removed [-[WebView setDownloadDelegate:]](https://developer.apple.com/documentation/webkit/webview/1408536-downloaddelegate)Removed [-[WebView setDrawsBackground:]](https://developer.apple.com/documentation/webkit/webview/1408486-drawsbackground)Removed [-[WebView setEditable:]](https://developer.apple.com/documentation/webkit/webview/1408556-editable)Removed [-[WebView setEditingDelegate:]](https://developer.apple.com/documentation/webkit/webview/1408349-editingdelegate)Removed [-[WebView setFrameLoadDelegate:]](https://developer.apple.com/documentation/webkit/webview/1408540-frameloaddelegate)Removed [-[WebView setGroupName:]](https://developer.apple.com/documentation/webkit/webview/1408478-groupname)Removed [-[WebView setHostWindow:]](https://developer.apple.com/documentation/webkit/webview/1408574-hostwindow)Removed [-[WebView setMainFrameURL:]](https://developer.apple.com/documentation/webkit/webview/1408351-mainframeurl)Removed [-[WebView setMediaStyle:]](https://developer.apple.com/documentation/webkit/webview/1408514-mediastyle)Removed [-[WebView setPolicyDelegate:]](https://developer.apple.com/documentation/webkit/webview/1408391-policydelegate)Removed [-[WebView setPreferences:]](https://developer.apple.com/documentation/webkit/webview/1408387-preferences)Removed [-[WebView setPreferencesIdentifier:]](https://developer.apple.com/documentation/webkit/webview/1408545-preferencesidentifier)Removed [-[WebView setResourceLoadDelegate:]](https://developer.apple.com/documentation/webkit/webview/1408367-resourceloaddelegate)Removed [-[WebView setShouldCloseWithWindow:]](https://developer.apple.com/documentation/webkit/webview/1408337-shouldclosewithwindow)Removed [-[WebView setShouldUpdateWhileOffscreen:]](https://developer.apple.com/documentation/webkit/webview/1408454-shouldupdatewhileoffscreen)Removed [-[WebView setSmartInsertDeleteEnabled:]](https://developer.apple.com/documentation/webkit/webview/1408389-smartinsertdeleteenabled)Removed [-[WebView setTextSizeMultiplier:]](https://developer.apple.com/documentation/webkit/webview/1408533-textsizemultiplier)Removed [-[WebView setTypingStyle:]](https://developer.apple.com/documentation/webkit/webview/1408415-typingstyle)Removed [-[WebView setUIDelegate:]](https://developer.apple.com/documentation/webkit/webview/1408544-uidelegate)Removed [-[WebView shouldCloseWithWindow]](https://developer.apple.com/documentation/webkit/webview/1408337-shouldclosewithwindow)Removed [-[WebView shouldUpdateWhileOffscreen]](https://developer.apple.com/documentation/webkit/webview/1408454-shouldupdatewhileoffscreen)Removed [-[WebView smartInsertDeleteEnabled]](https://developer.apple.com/documentation/webkit/webview/1408389-smartinsertdeleteenabled)Removed [-[WebView spellCheckerDocumentTag]](https://developer.apple.com/documentation/webkit/webview/1408411-spellcheckerdocumenttag)Removed [-[WebView supportsTextEncoding]](https://developer.apple.com/documentation/webkit/webview/1408464-supportstextencoding)Removed [-[WebView textSizeMultiplier]](https://developer.apple.com/documentation/webkit/webview/1408533-textsizemultiplier)Removed [-[WebView typingStyle]](https://developer.apple.com/documentation/webkit/webview/1408415-typingstyle)Removed [-[WebView undoManager]](https://developer.apple.com/documentation/webkit/webview/1408335-undomanager)Removed [-[WebView windowScriptObject]](https://developer.apple.com/documentation/webkit/webview/1408426-windowscriptobject)Added [WebView.UIDelegate](https://developer.apple.com/documentation/webkit/webview/1408544-uidelegate)Added [WebView.applicationNameForUserAgent](https://developer.apple.com/documentation/webkit/webview/1408381-applicationnameforuseragent)Added [WebView.backForwardList](https://developer.apple.com/documentation/webkit/webview/1408403-backforwardlist)Added [WebView.canGoBack](https://developer.apple.com/documentation/webkit/webview/1408500-cangoback)Added [WebView.canGoForward](https://developer.apple.com/documentation/webkit/webview/1408444-cangoforward)Added [WebView.canMakeTextLarger](https://developer.apple.com/documentation/webkit/webview/1408484-canmaketextlarger)Added [WebView.canMakeTextSmaller](https://developer.apple.com/documentation/webkit/webview/1408347-canmaketextsmaller)Added [WebView.canMakeTextStandardSize](https://developer.apple.com/documentation/webkit/webview/1408502-canmaketextstandardsize)Added [WebView.continuousSpellCheckingEnabled](https://developer.apple.com/documentation/webkit/webview/1408385-continuousspellcheckingenabled)Added [WebView.customTextEncodingName](https://developer.apple.com/documentation/webkit/webview/1408397-customtextencodingname)Added [WebView.customUserAgent](https://developer.apple.com/documentation/webkit/webview/1408377-customuseragent)Added [WebView.downloadDelegate](https://developer.apple.com/documentation/webkit/webview/1408536-downloaddelegate)Added [WebView.drawsBackground](https://developer.apple.com/documentation/webkit/webview/1408486-drawsbackground)Added [WebView.editable](https://developer.apple.com/documentation/webkit/webview/1408556-iseditable)Added [WebView.editingDelegate](https://developer.apple.com/documentation/webkit/webview/1408349-editingdelegate)Added [WebView.estimatedProgress](https://developer.apple.com/documentation/webkit/webview/1408538-estimatedprogress)Added [WebView.frameLoadDelegate](https://developer.apple.com/documentation/webkit/webview/1408540-frameloaddelegate)Added [WebView.groupName](https://developer.apple.com/documentation/webkit/webview/1408478-groupname)Added [WebView.hostWindow](https://developer.apple.com/documentation/webkit/webview/1408574-hostwindow)Added [WebView.loading](https://developer.apple.com/documentation/webkit/webview/1408566-isloading)Added [WebView.mainFrame](https://developer.apple.com/documentation/webkit/webview/1408470-mainframe)Added [WebView.mainFrameDocument](https://developer.apple.com/documentation/webkit/webview/1408525-mainframedocument)Added [WebView.mainFrameIcon](https://developer.apple.com/documentation/webkit/webview/1408527-mainframeicon)Added [WebView.mainFrameTitle](https://developer.apple.com/documentation/webkit/webview/1408498-mainframetitle)Added [WebView.mainFrameURL](https://developer.apple.com/documentation/webkit/webview/1408351-mainframeurl)Added [WebView.maintainsInactiveSelection](https://developer.apple.com/documentation/webkit/webview/1408494-maintainsinactiveselection)Added [WebView.mediaStyle](https://developer.apple.com/documentation/webkit/webview/1408514-mediastyle)Added [WebView.pasteboardTypesForSelection](https://developer.apple.com/documentation/webkit/webview/1408353-pasteboardtypesforselection)Added [WebView.policyDelegate](https://developer.apple.com/documentation/webkit/webview/1408391-policydelegate)Added [WebView.preferences](https://developer.apple.com/documentation/webkit/webview/1408387-preferences)Added [WebView.preferencesIdentifier](https://developer.apple.com/documentation/webkit/webview/1408545-preferencesidentifier)Added [WebView.resourceLoadDelegate](https://developer.apple.com/documentation/webkit/webview/1408367-resourceloaddelegate)Added [WebView.selectedDOMRange](https://developer.apple.com/documentation/webkit/webview/1408428-selecteddomrange)Added [WebView.selectedFrame](https://developer.apple.com/documentation/webkit/webview/1408434-selectedframe)Added [WebView.selectionAffinity](https://developer.apple.com/documentation/webkit/webview/1408452-selectionaffinity)Added [WebView.shouldCloseWithWindow](https://developer.apple.com/documentation/webkit/webview/1408337-shouldclosewithwindow)Added [WebView.shouldUpdateWhileOffscreen](https://developer.apple.com/documentation/webkit/webview/1408454-shouldupdatewhileoffscreen)Added [WebView.smartInsertDeleteEnabled](https://developer.apple.com/documentation/webkit/webview/1408389-smartinsertdeleteenabled)Added [WebView.spellCheckerDocumentTag](https://developer.apple.com/documentation/webkit/webview/1408411-spellcheckerdocumenttag)Added [WebView.supportsTextEncoding](https://developer.apple.com/documentation/webkit/webview/1408464-supportstextencoding)Added [WebView.textSizeMultiplier](https://developer.apple.com/documentation/webkit/webview/1408533-textsizemultiplier)Added [WebView.typingStyle](https://developer.apple.com/documentation/webkit/webview/1408415-typingstyle)Added [WebView.undoManager](https://developer.apple.com/documentation/webkit/webview/1408335-undomanager)Added [WebView.windowScriptObject](https://developer.apple.com/documentation/webkit/webview/1408426-windowscriptobject)Modified [-[WebView goBack:]](https://developer.apple.com/documentation/webkit/webview/1408482-goback)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goBack:(id)sender ``` |
| To | ``` - (IBAction)goBack:(id)sender ``` |

Modified [-[WebView goForward:]](https://developer.apple.com/documentation/webkit/webview/1408365-goforward)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goForward:(id)sender ``` |
| To | ``` - (IBAction)goForward:(id)sender ``` |

Modified [-[WebView initWithFrame:frameName:groupName:]](https://developer.apple.com/documentation/webkit/webview/1408359-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frame frameName:(NSString *)frameName groupName:(NSString *)groupName ``` |
| To | ``` - (instancetype)initWithFrame:(NSRect)frame frameName:(NSString *)frameName groupName:(NSString *)groupName ``` |

Modified [-[WebView makeTextLarger:]](https://developer.apple.com/documentation/webkit/webview/1408492-maketextlarger)

|  | Declaration |
| --- | --- |
| From | ``` - (void)makeTextLarger:(id)sender ``` |
| To | ``` - (IBAction)makeTextLarger:(id)sender ``` |

Modified [-[WebView makeTextSmaller:]](https://developer.apple.com/documentation/webkit/webview/1408520-maketextsmaller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)makeTextSmaller:(id)sender ``` |
| To | ``` - (IBAction)makeTextSmaller:(id)sender ``` |

Modified [-[WebView makeTextStandardSize:]](https://developer.apple.com/documentation/webkit/webview/1408504-maketextstandardsize)

|  | Declaration |
| --- | --- |
| From | ``` - (void)makeTextStandardSize:(id)sender ``` |
| To | ``` - (IBAction)makeTextStandardSize:(id)sender ``` |

Modified [-[WebView reload:]](https://developer.apple.com/documentation/webkit/webview/1408554-reload)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reload:(id)sender ``` |
| To | ``` - (IBAction)reload:(id)sender ``` |

Modified [-[WebView reloadFromOrigin:]](https://developer.apple.com/documentation/webkit/webview/1408446-reloadfromorigin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reloadFromOrigin:(id)sender ``` |
| To | ``` - (IBAction)reloadFromOrigin:(id)sender ``` |

Modified [-[WebView stopLoading:]](https://developer.apple.com/documentation/webkit/webview/1408568-stoploading)

|  | Declaration |
| --- | --- |
| From | ``` - (void)stopLoading:(id)sender ``` |
| To | ``` - (IBAction)stopLoading:(id)sender ``` |

Modified [-[WebView takeStringURLFrom:]](https://developer.apple.com/documentation/webkit/webview/1408441-takestringurlfrom)

|  | Declaration |
| --- | --- |
| From | ``` - (void)takeStringURLFrom:(id)sender ``` |
| To | ``` - (IBAction)takeStringURLFrom:(id)sender ``` |

Modified [-[WebView toggleContinuousSpellChecking:]](https://developer.apple.com/documentation/webkit/webview/1408433-togglecontinuousspellchecking)

|  | Declaration |
| --- | --- |
| From | ``` - (void)toggleContinuousSpellChecking:(id)sender ``` |
| To | ``` - (IBAction)toggleContinuousSpellChecking:(id)sender ``` |

Modified [-[WebView toggleSmartInsertDelete:]](https://developer.apple.com/documentation/webkit/webview/1408333-togglesmartinsertdelete)

|  | Declaration |
| --- | --- |
| From | ``` - (void)toggleSmartInsertDelete:(id)sender ``` |
| To | ``` - (IBAction)toggleSmartInsertDelete:(id)sender ``` |

npapi.hRemoved NPImageExpose

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
