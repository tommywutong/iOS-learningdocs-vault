---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreText.html
archived_at: '2026-07-18T02:56:32.561889Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreText Changes for Objective-C

### CoreText

#### CoreText.h

Added [#def kCTVersionNumber10_11](https://developer.apple.com/documentation/coretext/kctversionnumber10_11)

#### CTDefines.h

Removed #def CT_BRIDGED_TYPE

#### CTFont.h

Modified [CTFontCreatePathForGlyph()](https://developer.apple.com/documentation/coretext/1510921-ctfontcreatepathforglyph)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CTFontCreatePathForGlyph (     CTFontRef font,     CGGlyph glyph,     const CGAffineTransform *transform ); ``` |
| To | ``` CGPathRef _Nullable CTFontCreatePathForGlyph (     CTFontRef _Nonnull font,     CGGlyph glyph,     const CGAffineTransform * _Nullable matrix ); ``` |

Modified [CTFontGetAdvancesForGlyphs()](https://developer.apple.com/documentation/coretext/1511265-ctfontgetadvancesforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` double CTFontGetAdvancesForGlyphs (     CTFontRef font,     CTFontOrientation orientation,     const CGGlyph glyphs[],     CGSize advances[],     CFIndex count ); ``` |
| To | ``` double CTFontGetAdvancesForGlyphs (     CTFontRef _Nonnull font,     CTFontOrientation orientation,     const CGGlyph glyphs[],     CGSize * _Nullable advances,     CFIndex count ); ``` |

Modified [CTFontGetBoundingRectsForGlyphs()](https://developer.apple.com/documentation/coretext/1509419-ctfontgetboundingrectsforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CTFontGetBoundingRectsForGlyphs (     CTFontRef font,     CTFontOrientation orientation,     const CGGlyph glyphs[],     CGRect boundingRects[],     CFIndex count ); ``` |
| To | ``` CGRect CTFontGetBoundingRectsForGlyphs (     CTFontRef _Nonnull font,     CTFontOrientation orientation,     const CGGlyph glyphs[],     CGRect * _Nullable boundingRects,     CFIndex count ); ``` |

Modified [CTFontGetLigatureCaretPositions()](https://developer.apple.com/documentation/coretext/1508820-ctfontgetligaturecaretpositions)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTFontGetLigatureCaretPositions (     CTFontRef font,     CGGlyph glyph,     CGFloat positions[],     CFIndex maxPositions ); ``` |
| To | ``` CFIndex CTFontGetLigatureCaretPositions (     CTFontRef _Nonnull font,     CGGlyph glyph,     CGFloat * _Nullable positions,     CFIndex maxPositions ); ``` |

Modified [CTFontGetOpticalBoundsForGlyphs()](https://developer.apple.com/documentation/coretext/1510531-ctfontgetopticalboundsforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CTFontGetOpticalBoundsForGlyphs (     CTFontRef font,     const CGGlyph glyphs[],     CGRect boundingRects[],     CFIndex count,     CFOptionFlags options ); ``` |
| To | ``` CGRect CTFontGetOpticalBoundsForGlyphs (     CTFontRef _Nonnull font,     const CGGlyph glyphs[],     CGRect * _Nullable boundingRects,     CFIndex count,     CFOptionFlags options ); ``` |

Modified [kCTFontAlertHeaderFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510101-kctfontalertheaderfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontApplicationFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontapplicationfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontControlContentFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508950-kctfontcontrolcontentfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontEmphasizedSystemDetailFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508682-kctfontemphasizedsystemdetailfon)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509236-kctfontemphasizedsystemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontLabelFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510353-kctfontlabelfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontMenuItemCmdKeyFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510054-kctfontmenuitemcmdkeyfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontMenuItemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontmenuitemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontMenuItemMarkFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1511482-kctfontmenuitemmarkfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontMenuTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509980-kctfontmenutitlefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontMessageFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontmessagefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontMiniEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1511329-kctfontminiemphasizedsystemfontt)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontMiniSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontminisystemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontNoFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1511298-kctfontnofonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontPaletteFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510763-kctfontpalettefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontPushButtonFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509856-kctfontpushbuttonfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontSmallEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509037-kctfontsmallemphasizedsystemfont)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontSmallSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontsmallsystemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontSmallToolbarFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontsmalltoolbarfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontSystemDetailFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1511000-kctfontsystemdetailfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509431-kctfontsystemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontToolbarFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfonttoolbarfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontToolTipFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfonttooltipfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontUserFixedPitchFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509494-kctfontuserfixedpitchfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontUserFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuserfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontUtilityWindowTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontutilitywindowtitlefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontViewsFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508656-kctfontviewsfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontWindowTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontwindowtitlefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### CTFontCollection.h

Removed [kCTFontCollectionCopyDefaultOptions](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/kctfontcollectioncopydefaultoptions)Removed [kCTFontCollectionCopyStandardSort](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/1509424-standardsort)Removed [kCTFontCollectionCopyUnique](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/kctfontcollectioncopyunique)

#### CTFontDescriptor.h

Modified [kCTFontDefaultOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfontdefaultorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontHorizontalOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfonthorizontalorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTFontVerticalOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfontverticalorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### CTGlyphInfo.h

Modified [kCTAdobeCNS1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobecns1charactercollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTAdobeGB1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobegb1charactercollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTAdobeJapan1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402052-kctadobejapan1charactercollectio)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTAdobeJapan2CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobejapan2charactercollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTAdobeKorea1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobekorea1charactercollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTIdentityMappingCharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402054-kctidentitymappingcharactercolle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### CTLine.h

Added [CTLineEnumerateCaretOffsets()](https://developer.apple.com/documentation/coretext/1508685-ctlineenumeratecaretoffsets)Modified [CTLineCreateWithAttributedString()](https://developer.apple.com/documentation/coretext/1509461-ctlinecreatewithattributedstring)

|  | Declaration |
| --- | --- |
| From | ``` CTLineRef CTLineCreateWithAttributedString (     CFAttributedStringRef string ); ``` |
| To | ``` CTLineRef _Nonnull CTLineCreateWithAttributedString (     CFAttributedStringRef _Nonnull attrString ); ``` |

#### CTParagraphStyle.h

Modified [kCTCenterTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctcentertextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTJustifiedTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/1496119-kctjustifiedtextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTLeftTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctlefttextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTNaturalTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctnaturaltextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kCTRightTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctrighttextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### CTStringAttributes.h

Modified [kCTCharacterShapeAttributeName](https://developer.apple.com/documentation/coretext/kctcharactershapeattributename)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
