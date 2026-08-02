---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreText.html
archived_at: '2026-07-18T02:53:01.053933Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreText Changes for Objective-C

### CoreText

#### CoreText.h

Added [#def kCTVersionNumber10_11](https://developer.apple.com/documentation/coretext/kctversionnumber10_11)

#### CTDefines.h

Removed #def CT_BRIDGED_TYPE

#### CTFont.h

Modified [CTFontCopyAttribute()](https://developer.apple.com/documentation/coretext/1508984-ctfontcopyattribute)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CTFontCopyAttribute (     CTFontRef font,     CFStringRef attribute ); ``` |
| To | ``` CFTypeRef _Nullable CTFontCopyAttribute (     CTFontRef _Nonnull font,     CFStringRef _Nonnull attribute ); ``` |

Modified [CTFontCopyAvailableTables()](https://developer.apple.com/documentation/coretext/1510774-ctfontcopyavailabletables)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCopyAvailableTables (     CTFontRef font,     CTFontTableOptions options ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCopyAvailableTables (     CTFontRef _Nonnull font,     CTFontTableOptions options ); ``` |

Modified [CTFontCopyCharacterSet()](https://developer.apple.com/documentation/coretext/1511049-ctfontcopycharacterset)

|  | Declaration |
| --- | --- |
| From | ``` CFCharacterSetRef CTFontCopyCharacterSet (     CTFontRef font ); ``` |
| To | ``` CFCharacterSetRef _Nonnull CTFontCopyCharacterSet (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyDefaultCascadeListForLanguages()](https://developer.apple.com/documentation/coretext/1509992-ctfontcopydefaultcascadelistforl)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCopyDefaultCascadeListForLanguages (     CTFontRef font,     CFArrayRef languagePrefList ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCopyDefaultCascadeListForLanguages (     CTFontRef _Nonnull font,     CFArrayRef _Nullable languagePrefList ); ``` |

Modified [CTFontCopyDisplayName()](https://developer.apple.com/documentation/coretext/1509316-ctfontcopydisplayname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CTFontCopyDisplayName (     CTFontRef font ); ``` |
| To | ``` CFStringRef _Nonnull CTFontCopyDisplayName (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyFamilyName()](https://developer.apple.com/documentation/coretext/1509166-ctfontcopyfamilyname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CTFontCopyFamilyName (     CTFontRef font ); ``` |
| To | ``` CFStringRef _Nonnull CTFontCopyFamilyName (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyFeatures()](https://developer.apple.com/documentation/coretext/1509767-ctfontcopyfeatures)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCopyFeatures (     CTFontRef font ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCopyFeatures (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyFeatureSettings()](https://developer.apple.com/documentation/coretext/1509455-ctfontcopyfeaturesettings)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCopyFeatureSettings (     CTFontRef font ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCopyFeatureSettings (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyFontDescriptor()](https://developer.apple.com/documentation/coretext/1508996-ctfontcopyfontdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontCopyFontDescriptor (     CTFontRef font ); ``` |
| To | ``` CTFontDescriptorRef _Nonnull CTFontCopyFontDescriptor (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyFullName()](https://developer.apple.com/documentation/coretext/1510931-ctfontcopyfullname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CTFontCopyFullName (     CTFontRef font ); ``` |
| To | ``` CFStringRef _Nonnull CTFontCopyFullName (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyGraphicsFont()](https://developer.apple.com/documentation/coretext/1508712-ctfontcopygraphicsfont)

|  | Declaration |
| --- | --- |
| From | ``` CGFontRef CTFontCopyGraphicsFont (     CTFontRef font,     CTFontDescriptorRef *attributes ); ``` |
| To | ``` CGFontRef _Nonnull CTFontCopyGraphicsFont (     CTFontRef _Nonnull font,     CTFontDescriptorRef  _Nullable * _Nullable attributes ); ``` |

Modified [CTFontCopyLocalizedName()](https://developer.apple.com/documentation/coretext/1510714-ctfontcopylocalizedname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CTFontCopyLocalizedName (     CTFontRef font,     CFStringRef nameKey,     CFStringRef *actualLanguage ); ``` |
| To | ``` CFStringRef _Nullable CTFontCopyLocalizedName (     CTFontRef _Nonnull font,     CFStringRef _Nonnull nameKey,     CFStringRef  _Nullable * _Nullable actualLanguage ); ``` |

Modified [CTFontCopyName()](https://developer.apple.com/documentation/coretext/1511240-ctfontcopyname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CTFontCopyName (     CTFontRef font,     CFStringRef nameKey ); ``` |
| To | ``` CFStringRef _Nullable CTFontCopyName (     CTFontRef _Nonnull font,     CFStringRef _Nonnull nameKey ); ``` |

Modified [CTFontCopyPostScriptName()](https://developer.apple.com/documentation/coretext/1510887-ctfontcopypostscriptname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CTFontCopyPostScriptName (     CTFontRef font ); ``` |
| To | ``` CFStringRef _Nonnull CTFontCopyPostScriptName (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopySupportedLanguages()](https://developer.apple.com/documentation/coretext/1510096-ctfontcopysupportedlanguages)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCopySupportedLanguages (     CTFontRef font ); ``` |
| To | ``` CFArrayRef _Nonnull CTFontCopySupportedLanguages (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyTable()](https://developer.apple.com/documentation/coretext/1510755-ctfontcopytable)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CTFontCopyTable (     CTFontRef font,     CTFontTableTag table,     CTFontTableOptions options ); ``` |
| To | ``` CFDataRef _Nullable CTFontCopyTable (     CTFontRef _Nonnull font,     CTFontTableTag table,     CTFontTableOptions options ); ``` |

Modified [CTFontCopyTraits()](https://developer.apple.com/documentation/coretext/1509723-ctfontcopytraits)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CTFontCopyTraits (     CTFontRef font ); ``` |
| To | ``` CFDictionaryRef _Nonnull CTFontCopyTraits (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyVariation()](https://developer.apple.com/documentation/coretext/1508767-ctfontcopyvariation)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CTFontCopyVariation (     CTFontRef font ); ``` |
| To | ``` CFDictionaryRef _Nullable CTFontCopyVariation (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCopyVariationAxes()](https://developer.apple.com/documentation/coretext/1509987-ctfontcopyvariationaxes)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCopyVariationAxes (     CTFontRef font ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCopyVariationAxes (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontCreateCopyWithAttributes()](https://developer.apple.com/documentation/coretext/1511225-ctfontcreatecopywithattributes)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateCopyWithAttributes (     CTFontRef font,     CGFloat size,     const CGAffineTransform *matrix,     CTFontDescriptorRef attributes ); ``` |
| To | ``` CTFontRef _Nonnull CTFontCreateCopyWithAttributes (     CTFontRef _Nonnull font,     CGFloat size,     const CGAffineTransform * _Nullable matrix,     CTFontDescriptorRef _Nullable attributes ); ``` |

Modified [CTFontCreateCopyWithFamily()](https://developer.apple.com/documentation/coretext/1510945-ctfontcreatecopywithfamily)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateCopyWithFamily (     CTFontRef font,     CGFloat size,     const CGAffineTransform *matrix,     CFStringRef family ); ``` |
| To | ``` CTFontRef _Nullable CTFontCreateCopyWithFamily (     CTFontRef _Nonnull font,     CGFloat size,     const CGAffineTransform * _Nullable matrix,     CFStringRef _Nonnull family ); ``` |

Modified [CTFontCreateCopyWithSymbolicTraits()](https://developer.apple.com/documentation/coretext/1511394-ctfontcreatecopywithsymbolictrai)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateCopyWithSymbolicTraits (     CTFontRef font,     CGFloat size,     const CGAffineTransform *matrix,     CTFontSymbolicTraits symTraitValue,     CTFontSymbolicTraits symTraitMask ); ``` |
| To | ``` CTFontRef _Nullable CTFontCreateCopyWithSymbolicTraits (     CTFontRef _Nonnull font,     CGFloat size,     const CGAffineTransform * _Nullable matrix,     CTFontSymbolicTraits symTraitValue,     CTFontSymbolicTraits symTraitMask ); ``` |

Modified [CTFontCreateForString()](https://developer.apple.com/documentation/coretext/1509506-ctfontcreateforstring)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateForString (     CTFontRef currentFont,     CFStringRef string,     CFRange range ); ``` |
| To | ``` CTFontRef _Nonnull CTFontCreateForString (     CTFontRef _Nonnull currentFont,     CFStringRef _Nonnull string,     CFRange range ); ``` |

Modified [CTFontCreatePathForGlyph()](https://developer.apple.com/documentation/coretext/1510921-ctfontcreatepathforglyph)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CTFontCreatePathForGlyph (     CTFontRef font,     CGGlyph glyph,     const CGAffineTransform *transform ); ``` |
| To | ``` CGPathRef _Nullable CTFontCreatePathForGlyph (     CTFontRef _Nonnull font,     CGGlyph glyph,     const CGAffineTransform * _Nullable matrix ); ``` |

Modified [CTFontCreateUIFontForLanguage()](https://developer.apple.com/documentation/coretext/1511312-ctfontcreateuifontforlanguage)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateUIFontForLanguage (     CTFontUIFontType uiType,     CGFloat size,     CFStringRef language ); ``` |
| To | ``` CTFontRef _Nullable CTFontCreateUIFontForLanguage (     CTFontUIFontType uiType,     CGFloat size,     CFStringRef _Nullable language ); ``` |

Modified [CTFontCreateWithFontDescriptor()](https://developer.apple.com/documentation/coretext/1509056-ctfontcreatewithfontdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateWithFontDescriptor (     CTFontDescriptorRef descriptor,     CGFloat size,     const CGAffineTransform *matrix ); ``` |
| To | ``` CTFontRef _Nonnull CTFontCreateWithFontDescriptor (     CTFontDescriptorRef _Nonnull descriptor,     CGFloat size,     const CGAffineTransform * _Nullable matrix ); ``` |

Modified [CTFontCreateWithFontDescriptorAndOptions()](https://developer.apple.com/documentation/coretext/1510463-ctfontcreatewithfontdescriptoran)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateWithFontDescriptorAndOptions (     CTFontDescriptorRef descriptor,     CGFloat size,     const CGAffineTransform *matrix,     CTFontOptions options ); ``` |
| To | ``` CTFontRef _Nonnull CTFontCreateWithFontDescriptorAndOptions (     CTFontDescriptorRef _Nonnull descriptor,     CGFloat size,     const CGAffineTransform * _Nullable matrix,     CTFontOptions options ); ``` |

Modified [CTFontCreateWithGraphicsFont()](https://developer.apple.com/documentation/coretext/1508745-ctfontcreatewithgraphicsfont)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateWithGraphicsFont (     CGFontRef graphicsFont,     CGFloat size,     const CGAffineTransform *matrix,     CTFontDescriptorRef attributes ); ``` |
| To | ``` CTFontRef _Nonnull CTFontCreateWithGraphicsFont (     CGFontRef _Nonnull graphicsFont,     CGFloat size,     const CGAffineTransform * _Nullable matrix,     CTFontDescriptorRef _Nullable attributes ); ``` |

Modified [CTFontCreateWithName()](https://developer.apple.com/documentation/coretext/1509153-ctfontcreatewithname)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateWithName (     CFStringRef name,     CGFloat size,     const CGAffineTransform *matrix ); ``` |
| To | ``` CTFontRef _Nonnull CTFontCreateWithName (     CFStringRef _Nullable name,     CGFloat size,     const CGAffineTransform * _Nullable matrix ); ``` |

Modified [CTFontCreateWithNameAndOptions()](https://developer.apple.com/documentation/coretext/1508624-ctfontcreatewithnameandoptions)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateWithNameAndOptions (     CFStringRef name,     CGFloat size,     const CGAffineTransform *matrix,     CTFontOptions options ); ``` |
| To | ``` CTFontRef _Nonnull CTFontCreateWithNameAndOptions (     CFStringRef _Nonnull name,     CGFloat size,     const CGAffineTransform * _Nullable matrix,     CTFontOptions options ); ``` |

Modified [CTFontCreateWithPlatformFont()](https://developer.apple.com/documentation/coretext/1510362-ctfontcreatewithplatformfont)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateWithPlatformFont (     ATSFontRef platformFont,     CGFloat size,     const CGAffineTransform *matrix,     CTFontDescriptorRef attributes ); ``` |
| To | ``` CTFontRef _Nullable CTFontCreateWithPlatformFont (     ATSFontRef platformFont,     CGFloat size,     const CGAffineTransform * _Nullable matrix,     CTFontDescriptorRef _Nullable attributes ); ``` |

Modified [CTFontCreateWithQuickdrawInstance()](https://developer.apple.com/documentation/coretext/1509337-ctfontcreatewithquickdrawinstanc)

|  | Declaration |
| --- | --- |
| From | ``` CTFontRef CTFontCreateWithQuickdrawInstance (     ConstStr255Param name,     int16_t identifier,     uint8_t style,     CGFloat size ); ``` |
| To | ``` CTFontRef _Nonnull CTFontCreateWithQuickdrawInstance (     ConstStr255Param _Nullable name,     int16_t identifier,     uint8_t style,     CGFloat size ); ``` |

Modified [CTFontDrawGlyphs()](https://developer.apple.com/documentation/coretext/1509850-ctfontdrawglyphs)

|  | Declaration |
| --- | --- |
| From | ``` void CTFontDrawGlyphs (     CTFontRef font,     const CGGlyph glyphs[],     const CGPoint positions[],     size_t count,     CGContextRef context ); ``` |
| To | ``` void CTFontDrawGlyphs (     CTFontRef _Nonnull font,     const CGGlyph glyphs[],     const CGPoint positions[],     size_t count,     CGContextRef _Nonnull context ); ``` |

Modified [CTFontGetAdvancesForGlyphs()](https://developer.apple.com/documentation/coretext/1511265-ctfontgetadvancesforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` double CTFontGetAdvancesForGlyphs (     CTFontRef font,     CTFontOrientation orientation,     const CGGlyph glyphs[],     CGSize advances[],     CFIndex count ); ``` |
| To | ``` double CTFontGetAdvancesForGlyphs (     CTFontRef _Nonnull font,     CTFontOrientation orientation,     const CGGlyph glyphs[],     CGSize * _Nullable advances,     CFIndex count ); ``` |

Modified [CTFontGetAscent()](https://developer.apple.com/documentation/coretext/1510018-ctfontgetascent)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetAscent (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetAscent (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetBoundingBox()](https://developer.apple.com/documentation/coretext/1509253-ctfontgetboundingbox)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CTFontGetBoundingBox (     CTFontRef font ); ``` |
| To | ``` CGRect CTFontGetBoundingBox (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetBoundingRectsForGlyphs()](https://developer.apple.com/documentation/coretext/1509419-ctfontgetboundingrectsforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CTFontGetBoundingRectsForGlyphs (     CTFontRef font,     CTFontOrientation orientation,     const CGGlyph glyphs[],     CGRect boundingRects[],     CFIndex count ); ``` |
| To | ``` CGRect CTFontGetBoundingRectsForGlyphs (     CTFontRef _Nonnull font,     CTFontOrientation orientation,     const CGGlyph glyphs[],     CGRect * _Nullable boundingRects,     CFIndex count ); ``` |

Modified [CTFontGetCapHeight()](https://developer.apple.com/documentation/coretext/1511349-ctfontgetcapheight)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetCapHeight (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetCapHeight (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetDescent()](https://developer.apple.com/documentation/coretext/1510313-ctfontgetdescent)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetDescent (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetDescent (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetGlyphCount()](https://developer.apple.com/documentation/coretext/1511330-ctfontgetglyphcount)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTFontGetGlyphCount (     CTFontRef font ); ``` |
| To | ``` CFIndex CTFontGetGlyphCount (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetGlyphsForCharacters()](https://developer.apple.com/documentation/coretext/1510813-ctfontgetglyphsforcharacters)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontGetGlyphsForCharacters (     CTFontRef font,     const UniChar characters[],     CGGlyph glyphs[],     CFIndex count ); ``` |
| To | ``` bool CTFontGetGlyphsForCharacters (     CTFontRef _Nonnull font,     const UniChar characters[],     CGGlyph glyphs[],     CFIndex count ); ``` |

Modified [CTFontGetGlyphWithName()](https://developer.apple.com/documentation/coretext/1510788-ctfontgetglyphwithname)

|  | Declaration |
| --- | --- |
| From | ``` CGGlyph CTFontGetGlyphWithName (     CTFontRef font,     CFStringRef glyphName ); ``` |
| To | ``` CGGlyph CTFontGetGlyphWithName (     CTFontRef _Nonnull font,     CFStringRef _Nonnull glyphName ); ``` |

Modified [CTFontGetLeading()](https://developer.apple.com/documentation/coretext/1509426-ctfontgetleading)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetLeading (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetLeading (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetLigatureCaretPositions()](https://developer.apple.com/documentation/coretext/1508820-ctfontgetligaturecaretpositions)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTFontGetLigatureCaretPositions (     CTFontRef font,     CGGlyph glyph,     CGFloat positions[],     CFIndex maxPositions ); ``` |
| To | ``` CFIndex CTFontGetLigatureCaretPositions (     CTFontRef _Nonnull font,     CGGlyph glyph,     CGFloat * _Nullable positions,     CFIndex maxPositions ); ``` |

Modified [CTFontGetMatrix()](https://developer.apple.com/documentation/coretext/1510407-ctfontgetmatrix)

|  | Declaration |
| --- | --- |
| From | ``` CGAffineTransform CTFontGetMatrix (     CTFontRef font ); ``` |
| To | ``` CGAffineTransform CTFontGetMatrix (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetOpticalBoundsForGlyphs()](https://developer.apple.com/documentation/coretext/1510531-ctfontgetopticalboundsforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CTFontGetOpticalBoundsForGlyphs (     CTFontRef font,     const CGGlyph glyphs[],     CGRect boundingRects[],     CFIndex count,     CFOptionFlags options ); ``` |
| To | ``` CGRect CTFontGetOpticalBoundsForGlyphs (     CTFontRef _Nonnull font,     const CGGlyph glyphs[],     CGRect * _Nullable boundingRects,     CFIndex count,     CFOptionFlags options ); ``` |

Modified [CTFontGetPlatformFont()](https://developer.apple.com/documentation/coretext/1510544-ctfontgetplatformfont)

|  | Declaration |
| --- | --- |
| From | ``` ATSFontRef CTFontGetPlatformFont (     CTFontRef font,     CTFontDescriptorRef *attributes ); ``` |
| To | ``` ATSFontRef CTFontGetPlatformFont (     CTFontRef _Nonnull font,     CTFontDescriptorRef  _Nullable * _Nullable attributes ); ``` |

Modified [CTFontGetSize()](https://developer.apple.com/documentation/coretext/1511100-ctfontgetsize)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetSize (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetSize (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetSlantAngle()](https://developer.apple.com/documentation/coretext/1511178-ctfontgetslantangle)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetSlantAngle (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetSlantAngle (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetStringEncoding()](https://developer.apple.com/documentation/coretext/1509519-ctfontgetstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` CFStringEncoding CTFontGetStringEncoding (     CTFontRef font ); ``` |
| To | ``` CFStringEncoding CTFontGetStringEncoding (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetSymbolicTraits()](https://developer.apple.com/documentation/coretext/1509142-ctfontgetsymbolictraits)

|  | Declaration |
| --- | --- |
| From | ``` CTFontSymbolicTraits CTFontGetSymbolicTraits (     CTFontRef font ); ``` |
| To | ``` CTFontSymbolicTraits CTFontGetSymbolicTraits (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetUnderlinePosition()](https://developer.apple.com/documentation/coretext/1511320-ctfontgetunderlineposition)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetUnderlinePosition (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetUnderlinePosition (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetUnderlineThickness()](https://developer.apple.com/documentation/coretext/1508963-ctfontgetunderlinethickness)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetUnderlineThickness (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetUnderlineThickness (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetUnitsPerEm()](https://developer.apple.com/documentation/coretext/1510550-ctfontgetunitsperem)

|  | Declaration |
| --- | --- |
| From | ``` unsigned int CTFontGetUnitsPerEm (     CTFontRef font ); ``` |
| To | ``` unsigned int CTFontGetUnitsPerEm (     CTFontRef _Nonnull font ); ``` |

Modified [CTFontGetVerticalTranslationsForGlyphs()](https://developer.apple.com/documentation/coretext/1511102-ctfontgetverticaltranslationsfor)

|  | Declaration |
| --- | --- |
| From | ``` void CTFontGetVerticalTranslationsForGlyphs (     CTFontRef font,     const CGGlyph glyphs[],     CGSize translations[],     CFIndex count ); ``` |
| To | ``` void CTFontGetVerticalTranslationsForGlyphs (     CTFontRef _Nonnull font,     const CGGlyph glyphs[],     CGSize translations[],     CFIndex count ); ``` |

Modified [CTFontGetXHeight()](https://developer.apple.com/documentation/coretext/1510255-ctfontgetxheight)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTFontGetXHeight (     CTFontRef font ); ``` |
| To | ``` CGFloat CTFontGetXHeight (     CTFontRef _Nonnull font ); ``` |

Modified [kCTFontAlertHeaderFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510101-kctfontalertheaderfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontApplicationFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontapplicationfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontControlContentFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508950-kctfontcontrolcontentfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontEmphasizedSystemDetailFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508682-kctfontemphasizedsystemdetailfon)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509236-kctfontemphasizedsystemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontLabelFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510353-kctfontlabelfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontMenuItemCmdKeyFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510054-kctfontmenuitemcmdkeyfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontMenuItemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontmenuitemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontMenuItemMarkFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1511482-kctfontmenuitemmarkfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontMenuTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509980-kctfontmenutitlefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontMessageFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontmessagefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontMiniEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1511329-kctfontminiemphasizedsystemfontt)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontMiniSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontminisystemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontNoFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1511298-kctfontnofonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontPaletteFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510763-kctfontpalettefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontPushButtonFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509856-kctfontpushbuttonfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontSmallEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509037-kctfontsmallemphasizedsystemfont)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontSmallSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontsmallsystemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontSmallToolbarFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontsmalltoolbarfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontSystemDetailFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1511000-kctfontsystemdetailfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509431-kctfontsystemfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontToolbarFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfonttoolbarfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontToolTipFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfonttooltipfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontUserFixedPitchFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509494-kctfontuserfixedpitchfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontUserFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuserfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontUtilityWindowTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontutilitywindowtitlefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontViewsFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508656-kctfontviewsfonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontWindowTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontwindowtitlefonttype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### CTFontCollection.h

Modified [CTFontCollectionCopyExclusionDescriptors()](https://developer.apple.com/documentation/coretext/1510000-ctfontcollectioncopyexclusiondes)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCollectionCopyExclusionDescriptors (     CTFontCollectionRef collection ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCollectionCopyExclusionDescriptors (     CTFontCollectionRef _Nonnull collection ); ``` |

Modified [CTFontCollectionCopyFontAttribute()](https://developer.apple.com/documentation/coretext/1509577-ctfontcollectioncopyfontattribut)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCollectionCopyFontAttribute (     CTFontCollectionRef collection,     CFStringRef attributeName,     CTFontCollectionCopyOptions options ); ``` |
| To | ``` CFArrayRef _Nonnull CTFontCollectionCopyFontAttribute (     CTFontCollectionRef _Nonnull collection,     CFStringRef _Nonnull attributeName,     CTFontCollectionCopyOptions options ); ``` |

Modified [CTFontCollectionCopyFontAttributes()](https://developer.apple.com/documentation/coretext/1511083-ctfontcollectioncopyfontattribut)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCollectionCopyFontAttributes (     CTFontCollectionRef collection,     CFSetRef attributeNames,     CTFontCollectionCopyOptions options ); ``` |
| To | ``` CFArrayRef _Nonnull CTFontCollectionCopyFontAttributes (     CTFontCollectionRef _Nonnull collection,     CFSetRef _Nonnull attributeNames,     CTFontCollectionCopyOptions options ); ``` |

Modified [CTFontCollectionCopyQueryDescriptors()](https://developer.apple.com/documentation/coretext/1510010-ctfontcollectioncopyquerydescrip)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCollectionCopyQueryDescriptors (     CTFontCollectionRef collection ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCollectionCopyQueryDescriptors (     CTFontCollectionRef _Nonnull collection ); ``` |

Modified [CTFontCollectionCreateCopyWithFontDescriptors()](https://developer.apple.com/documentation/coretext/1510692-ctfontcollectioncreatecopywithfo)

|  | Declaration |
| --- | --- |
| From | ``` CTFontCollectionRef CTFontCollectionCreateCopyWithFontDescriptors (     CTFontCollectionRef original,     CFArrayRef queryDescriptors,     CFDictionaryRef options ); ``` |
| To | ``` CTFontCollectionRef _Nonnull CTFontCollectionCreateCopyWithFontDescriptors (     CTFontCollectionRef _Nonnull original,     CFArrayRef _Nullable queryDescriptors,     CFDictionaryRef _Nullable options ); ``` |

Modified [CTFontCollectionCreateFromAvailableFonts()](https://developer.apple.com/documentation/coretext/1509907-ctfontcollectioncreatefromavaila)

|  | Declaration |
| --- | --- |
| From | ``` CTFontCollectionRef CTFontCollectionCreateFromAvailableFonts (     CFDictionaryRef options ); ``` |
| To | ``` CTFontCollectionRef _Nonnull CTFontCollectionCreateFromAvailableFonts (     CFDictionaryRef _Nullable options ); ``` |

Modified [CTFontCollectionCreateMatchingFontDescriptors()](https://developer.apple.com/documentation/coretext/1511091-ctfontcollectioncreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCollectionCreateMatchingFontDescriptors (     CTFontCollectionRef collection ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCollectionCreateMatchingFontDescriptors (     CTFontCollectionRef _Nonnull collection ); ``` |

Modified [CTFontCollectionCreateMatchingFontDescriptorsForFamily()](https://developer.apple.com/documentation/coretext/1508637-ctfontcollectioncreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCollectionCreateMatchingFontDescriptorsForFamily (     CTFontCollectionRef collection,     CFStringRef familyName,     CFDictionaryRef options ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCollectionCreateMatchingFontDescriptorsForFamily (     CTFontCollectionRef _Nonnull collection,     CFStringRef _Nonnull familyName,     CFDictionaryRef _Nullable options ); ``` |

Modified [CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback()](https://developer.apple.com/documentation/coretext/1510434-ctfontcollectioncreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback (     CTFontCollectionRef collection,     CTFontCollectionSortDescriptorsCallback sortCallback,     void *refCon ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback (     CTFontCollectionRef _Nonnull collection,     CTFontCollectionSortDescriptorsCallback _Nullable sortCallback,     void * _Nullable refCon ); ``` |

Modified [CTFontCollectionCreateMatchingFontDescriptorsWithOptions()](https://developer.apple.com/documentation/coretext/1509397-ctfontcollectioncreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontCollectionCreateMatchingFontDescriptorsWithOptions (     CTFontCollectionRef collection,     CFDictionaryRef options ); ``` |
| To | ``` CFArrayRef _Nullable CTFontCollectionCreateMatchingFontDescriptorsWithOptions (     CTFontCollectionRef _Nonnull collection,     CFDictionaryRef _Nullable options ); ``` |

Modified [CTFontCollectionCreateMutableCopy()](https://developer.apple.com/documentation/coretext/1509247-ctfontcollectioncreatemutablecop)

|  | Declaration |
| --- | --- |
| From | ``` CTMutableFontCollectionRef CTFontCollectionCreateMutableCopy (     CTFontCollectionRef original ); ``` |
| To | ``` CTMutableFontCollectionRef _Nonnull CTFontCollectionCreateMutableCopy (     CTFontCollectionRef _Nonnull original ); ``` |

Modified [CTFontCollectionCreateWithFontDescriptors()](https://developer.apple.com/documentation/coretext/1509202-ctfontcollectioncreatewithfontde)

|  | Declaration |
| --- | --- |
| From | ``` CTFontCollectionRef CTFontCollectionCreateWithFontDescriptors (     CFArrayRef queryDescriptors,     CFDictionaryRef options ); ``` |
| To | ``` CTFontCollectionRef _Nonnull CTFontCollectionCreateWithFontDescriptors (     CFArrayRef _Nullable queryDescriptors,     CFDictionaryRef _Nullable options ); ``` |

Modified [CTFontCollectionSetExclusionDescriptors()](https://developer.apple.com/documentation/coretext/1509406-ctfontcollectionsetexclusiondesc)

|  | Declaration |
| --- | --- |
| From | ``` void CTFontCollectionSetExclusionDescriptors (     CTMutableFontCollectionRef collection,     CFArrayRef descriptors ); ``` |
| To | ``` void CTFontCollectionSetExclusionDescriptors (     CTMutableFontCollectionRef _Nonnull collection,     CFArrayRef _Nullable descriptors ); ``` |

Modified [CTFontCollectionSetQueryDescriptors()](https://developer.apple.com/documentation/coretext/1509060-ctfontcollectionsetquerydescript)

|  | Declaration |
| --- | --- |
| From | ``` void CTFontCollectionSetQueryDescriptors (     CTMutableFontCollectionRef collection,     CFArrayRef descriptors ); ``` |
| To | ``` void CTFontCollectionSetQueryDescriptors (     CTMutableFontCollectionRef _Nonnull collection,     CFArrayRef _Nullable descriptors ); ``` |

#### CTFontDescriptor.h

Modified [CTFontDescriptorCopyAttribute()](https://developer.apple.com/documentation/coretext/1510346-ctfontdescriptorcopyattribute)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CTFontDescriptorCopyAttribute (     CTFontDescriptorRef descriptor,     CFStringRef attribute ); ``` |
| To | ``` CFTypeRef _Nullable CTFontDescriptorCopyAttribute (     CTFontDescriptorRef _Nonnull descriptor,     CFStringRef _Nonnull attribute ); ``` |

Modified [CTFontDescriptorCopyAttributes()](https://developer.apple.com/documentation/coretext/1509327-ctfontdescriptorcopyattributes)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CTFontDescriptorCopyAttributes (     CTFontDescriptorRef descriptor ); ``` |
| To | ``` CFDictionaryRef _Nonnull CTFontDescriptorCopyAttributes (     CTFontDescriptorRef _Nonnull descriptor ); ``` |

Modified [CTFontDescriptorCopyLocalizedAttribute()](https://developer.apple.com/documentation/coretext/1509510-ctfontdescriptorcopylocalizedatt)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CTFontDescriptorCopyLocalizedAttribute (     CTFontDescriptorRef descriptor,     CFStringRef attribute,     CFStringRef *language ); ``` |
| To | ``` CFTypeRef _Nullable CTFontDescriptorCopyLocalizedAttribute (     CTFontDescriptorRef _Nonnull descriptor,     CFStringRef _Nonnull attribute,     CFStringRef  _Nullable * _Nullable language ); ``` |

Modified [CTFontDescriptorCreateCopyWithAttributes()](https://developer.apple.com/documentation/coretext/1511076-ctfontdescriptorcreatecopywithat)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontDescriptorCreateCopyWithAttributes (     CTFontDescriptorRef original,     CFDictionaryRef attributes ); ``` |
| To | ``` CTFontDescriptorRef _Nonnull CTFontDescriptorCreateCopyWithAttributes (     CTFontDescriptorRef _Nonnull original,     CFDictionaryRef _Nonnull attributes ); ``` |

Modified [CTFontDescriptorCreateCopyWithFamily()](https://developer.apple.com/documentation/coretext/1510392-ctfontdescriptorcreatecopywithfa)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontDescriptorCreateCopyWithFamily (     CTFontDescriptorRef original,     CFStringRef family ); ``` |
| To | ``` CTFontDescriptorRef _Nullable CTFontDescriptorCreateCopyWithFamily (     CTFontDescriptorRef _Nonnull original,     CFStringRef _Nonnull family ); ``` |

Modified [CTFontDescriptorCreateCopyWithFeature()](https://developer.apple.com/documentation/coretext/1508652-ctfontdescriptorcreatecopywithfe)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontDescriptorCreateCopyWithFeature (     CTFontDescriptorRef original,     CFNumberRef featureTypeIdentifier,     CFNumberRef featureSelectorIdentifier ); ``` |
| To | ``` CTFontDescriptorRef _Nonnull CTFontDescriptorCreateCopyWithFeature (     CTFontDescriptorRef _Nonnull original,     CFNumberRef _Nonnull featureTypeIdentifier,     CFNumberRef _Nonnull featureSelectorIdentifier ); ``` |

Modified [CTFontDescriptorCreateCopyWithSymbolicTraits()](https://developer.apple.com/documentation/coretext/1509171-ctfontdescriptorcreatecopywithsy)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontDescriptorCreateCopyWithSymbolicTraits (     CTFontDescriptorRef original,     CTFontSymbolicTraits symTraitValue,     CTFontSymbolicTraits symTraitMask ); ``` |
| To | ``` CTFontDescriptorRef _Nullable CTFontDescriptorCreateCopyWithSymbolicTraits (     CTFontDescriptorRef _Nonnull original,     CTFontSymbolicTraits symTraitValue,     CTFontSymbolicTraits symTraitMask ); ``` |

Modified [CTFontDescriptorCreateCopyWithVariation()](https://developer.apple.com/documentation/coretext/1508650-ctfontdescriptorcreatecopywithva)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontDescriptorCreateCopyWithVariation (     CTFontDescriptorRef original,     CFNumberRef variationIdentifier,     CGFloat variationValue ); ``` |
| To | ``` CTFontDescriptorRef _Nonnull CTFontDescriptorCreateCopyWithVariation (     CTFontDescriptorRef _Nonnull original,     CFNumberRef _Nonnull variationIdentifier,     CGFloat variationValue ); ``` |

Modified [CTFontDescriptorCreateMatchingFontDescriptor()](https://developer.apple.com/documentation/coretext/1508848-ctfontdescriptorcreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontDescriptorCreateMatchingFontDescriptor (     CTFontDescriptorRef descriptor,     CFSetRef mandatoryAttributes ); ``` |
| To | ``` CTFontDescriptorRef _Nullable CTFontDescriptorCreateMatchingFontDescriptor (     CTFontDescriptorRef _Nonnull descriptor,     CFSetRef _Nullable mandatoryAttributes ); ``` |

Modified [CTFontDescriptorCreateMatchingFontDescriptors()](https://developer.apple.com/documentation/coretext/1508794-ctfontdescriptorcreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontDescriptorCreateMatchingFontDescriptors (     CTFontDescriptorRef descriptor,     CFSetRef mandatoryAttributes ); ``` |
| To | ``` CFArrayRef _Nullable CTFontDescriptorCreateMatchingFontDescriptors (     CTFontDescriptorRef _Nonnull descriptor,     CFSetRef _Nullable mandatoryAttributes ); ``` |

Modified [CTFontDescriptorCreateWithAttributes()](https://developer.apple.com/documentation/coretext/1510642-ctfontdescriptorcreatewithattrib)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontDescriptorCreateWithAttributes (     CFDictionaryRef attributes ); ``` |
| To | ``` CTFontDescriptorRef _Nonnull CTFontDescriptorCreateWithAttributes (     CFDictionaryRef _Nonnull attributes ); ``` |

Modified [CTFontDescriptorCreateWithNameAndSize()](https://developer.apple.com/documentation/coretext/1510226-ctfontdescriptorcreatewithnamean)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontDescriptorCreateWithNameAndSize (     CFStringRef name,     CGFloat size ); ``` |
| To | ``` CTFontDescriptorRef _Nonnull CTFontDescriptorCreateWithNameAndSize (     CFStringRef _Nonnull name,     CGFloat size ); ``` |

Modified [CTFontDescriptorMatchFontDescriptorsWithProgressHandler()](https://developer.apple.com/documentation/coretext/1511433-ctfontdescriptormatchfontdescrip)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontDescriptorMatchFontDescriptorsWithProgressHandler (     CFArrayRef descriptors,     CFSetRef mandatoryAttributes,     CTFontDescriptorProgressHandler progressBlock ); ``` |
| To | ``` bool CTFontDescriptorMatchFontDescriptorsWithProgressHandler (     CFArrayRef _Nonnull descriptors,     CFSetRef _Nullable mandatoryAttributes,     CTFontDescriptorProgressHandler _Nonnull progressBlock ); ``` |

Modified [kCTFontDefaultOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfontdefaultorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontHorizontalOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfonthorizontalorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTFontVerticalOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfontverticalorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### CTFontManager.h

Modified [CTFontManagerCompareFontFamilyNames()](https://developer.apple.com/documentation/coretext/1499513-ctfontmanagercomparefontfamilyna)

|  | Declaration |
| --- | --- |
| From | ``` CFComparisonResult CTFontManagerCompareFontFamilyNames (     const void *family1,     const void *family2,     void *context ); ``` |
| To | ``` CFComparisonResult CTFontManagerCompareFontFamilyNames (     const void * _Nonnull family1,     const void * _Nonnull family2,     void * _Nullable context ); ``` |

Modified [CTFontManagerCopyAvailableFontFamilyNames()](https://developer.apple.com/documentation/coretext/1499494-ctfontmanagercopyavailablefontfa)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontManagerCopyAvailableFontFamilyNames (     void ); ``` |
| To | ``` CFArrayRef _Nonnull CTFontManagerCopyAvailableFontFamilyNames (     void ); ``` |

Modified [CTFontManagerCopyAvailableFontURLs()](https://developer.apple.com/documentation/coretext/1499478-ctfontmanagercopyavailablefontur)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontManagerCopyAvailableFontURLs (     void ); ``` |
| To | ``` CFArrayRef _Nonnull CTFontManagerCopyAvailableFontURLs (     void ); ``` |

Modified [CTFontManagerCopyAvailablePostScriptNames()](https://developer.apple.com/documentation/coretext/1499516-ctfontmanagercopyavailablepostsc)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontManagerCopyAvailablePostScriptNames (     void ); ``` |
| To | ``` CFArrayRef _Nonnull CTFontManagerCopyAvailablePostScriptNames (     void ); ``` |

Modified [CTFontManagerCreateFontDescriptorFromData()](https://developer.apple.com/documentation/coretext/1499509-ctfontmanagercreatefontdescripto)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef CTFontManagerCreateFontDescriptorFromData (     CFDataRef data ); ``` |
| To | ``` CTFontDescriptorRef _Nullable CTFontManagerCreateFontDescriptorFromData (     CFDataRef _Nonnull data ); ``` |

Modified [CTFontManagerCreateFontDescriptorsFromURL()](https://developer.apple.com/documentation/coretext/1499500-ctfontmanagercreatefontdescripto)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFontManagerCreateFontDescriptorsFromURL (     CFURLRef fileURL ); ``` |
| To | ``` CFArrayRef _Nullable CTFontManagerCreateFontDescriptorsFromURL (     CFURLRef _Nonnull fileURL ); ``` |

Modified [CTFontManagerCreateFontRequestRunLoopSource()](https://developer.apple.com/documentation/coretext/1499507-ctfontmanagercreatefontrequestru)

|  | Declaration |
| --- | --- |
| From | ``` CFRunLoopSourceRef CTFontManagerCreateFontRequestRunLoopSource (     CFIndex sourceOrder,     CFArrayRef (^createMatchesCallback)(CFDictionaryRef requestAttributes, pid_t requestingProcess) ); ``` |
| To | ``` CFRunLoopSourceRef _Nullable CTFontManagerCreateFontRequestRunLoopSource (     CFIndex sourceOrder,     CFArrayRef  _Nonnull (^ _NonnullcreateMatchesCallback)(CFDictionaryRef _Nonnull requestAttributes, pid_t requestingProcess) ); ``` |

Modified [CTFontManagerEnableFontDescriptors()](https://developer.apple.com/documentation/coretext/1499515-ctfontmanagerenablefontdescripto)

|  | Declaration |
| --- | --- |
| From | ``` void CTFontManagerEnableFontDescriptors (     CFArrayRef descriptors,     bool enable ); ``` |
| To | ``` void CTFontManagerEnableFontDescriptors (     CFArrayRef _Nonnull descriptors,     bool enable ); ``` |

Modified [CTFontManagerGetAutoActivationSetting()](https://developer.apple.com/documentation/coretext/1499473-ctfontmanagergetautoactivationse)

|  | Declaration |
| --- | --- |
| From | ``` CTFontManagerAutoActivationSetting CTFontManagerGetAutoActivationSetting (     CFStringRef bundleIdentifier ); ``` |
| To | ``` CTFontManagerAutoActivationSetting CTFontManagerGetAutoActivationSetting (     CFStringRef _Nullable bundleIdentifier ); ``` |

Modified [CTFontManagerGetScopeForURL()](https://developer.apple.com/documentation/coretext/1499506-ctfontmanagergetscopeforurl)

|  | Declaration |
| --- | --- |
| From | ``` CTFontManagerScope CTFontManagerGetScopeForURL (     CFURLRef fontURL ); ``` |
| To | ``` CTFontManagerScope CTFontManagerGetScopeForURL (     CFURLRef _Nonnull fontURL ); ``` |

Modified [CTFontManagerIsSupportedFont()](https://developer.apple.com/documentation/coretext/1499491-ctfontmanagerissupportedfont)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontManagerIsSupportedFont (     CFURLRef fontURL ); ``` |
| To | ``` bool CTFontManagerIsSupportedFont (     CFURLRef _Nonnull fontURL ); ``` |

Modified [CTFontManagerRegisterFontsForURL()](https://developer.apple.com/documentation/coretext/1499468-ctfontmanagerregisterfontsforurl)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontManagerRegisterFontsForURL (     CFURLRef fontURL,     CTFontManagerScope scope,     CFErrorRef *error ); ``` |
| To | ``` bool CTFontManagerRegisterFontsForURL (     CFURLRef _Nonnull fontURL,     CTFontManagerScope scope,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [CTFontManagerRegisterFontsForURLs()](https://developer.apple.com/documentation/coretext/1499470-ctfontmanagerregisterfontsforurl)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontManagerRegisterFontsForURLs (     CFArrayRef fontURLs,     CTFontManagerScope scope,     CFArrayRef *errors ); ``` |
| To | ``` bool CTFontManagerRegisterFontsForURLs (     CFArrayRef _Nonnull fontURLs,     CTFontManagerScope scope,     CFArrayRef  _Nullable * _Nullable errors ); ``` |

Modified [CTFontManagerRegisterGraphicsFont()](https://developer.apple.com/documentation/coretext/1499499-ctfontmanagerregistergraphicsfon)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontManagerRegisterGraphicsFont (     CGFontRef font,     CFErrorRef *error ); ``` |
| To | ``` bool CTFontManagerRegisterGraphicsFont (     CGFontRef _Nonnull font,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [CTFontManagerSetAutoActivationSetting()](https://developer.apple.com/documentation/coretext/1499481-ctfontmanagersetautoactivationse)

|  | Declaration |
| --- | --- |
| From | ``` void CTFontManagerSetAutoActivationSetting (     CFStringRef bundleIdentifier,     CTFontManagerAutoActivationSetting setting ); ``` |
| To | ``` void CTFontManagerSetAutoActivationSetting (     CFStringRef _Nullable bundleIdentifier,     CTFontManagerAutoActivationSetting setting ); ``` |

Modified [CTFontManagerUnregisterFontsForURL()](https://developer.apple.com/documentation/coretext/1499496-ctfontmanagerunregisterfontsforu)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontManagerUnregisterFontsForURL (     CFURLRef fontURL,     CTFontManagerScope scope,     CFErrorRef *error ); ``` |
| To | ``` bool CTFontManagerUnregisterFontsForURL (     CFURLRef _Nonnull fontURL,     CTFontManagerScope scope,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [CTFontManagerUnregisterFontsForURLs()](https://developer.apple.com/documentation/coretext/1499477-ctfontmanagerunregisterfontsforu)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontManagerUnregisterFontsForURLs (     CFArrayRef fontURLs,     CTFontManagerScope scope,     CFArrayRef *errors ); ``` |
| To | ``` bool CTFontManagerUnregisterFontsForURLs (     CFArrayRef _Nonnull fontURLs,     CTFontManagerScope scope,     CFArrayRef  _Nullable * _Nullable errors ); ``` |

Modified [CTFontManagerUnregisterGraphicsFont()](https://developer.apple.com/documentation/coretext/1499472-ctfontmanagerunregistergraphicsf)

|  | Declaration |
| --- | --- |
| From | ``` bool CTFontManagerUnregisterGraphicsFont (     CGFontRef font,     CFErrorRef *error ); ``` |
| To | ``` bool CTFontManagerUnregisterGraphicsFont (     CGFontRef _Nonnull font,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### CTFrame.h

Modified [CTFrameDraw()](https://developer.apple.com/documentation/coretext/1509589-ctframedraw)

|  | Declaration |
| --- | --- |
| From | ``` void CTFrameDraw (     CTFrameRef frame,     CGContextRef context ); ``` |
| To | ``` void CTFrameDraw (     CTFrameRef _Nonnull frame,     CGContextRef _Nonnull context ); ``` |

Modified [CTFrameGetFrameAttributes()](https://developer.apple.com/documentation/coretext/1510750-ctframegetframeattributes)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CTFrameGetFrameAttributes (     CTFrameRef frame ); ``` |
| To | ``` CFDictionaryRef _Nullable CTFrameGetFrameAttributes (     CTFrameRef _Nonnull frame ); ``` |

Modified [CTFrameGetLineOrigins()](https://developer.apple.com/documentation/coretext/1510610-ctframegetlineorigins)

|  | Declaration |
| --- | --- |
| From | ``` void CTFrameGetLineOrigins (     CTFrameRef frame,     CFRange range,     CGPoint origins[] ); ``` |
| To | ``` void CTFrameGetLineOrigins (     CTFrameRef _Nonnull frame,     CFRange range,     CGPoint origins[] ); ``` |

Modified [CTFrameGetLines()](https://developer.apple.com/documentation/coretext/1510385-ctframegetlines)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTFrameGetLines (     CTFrameRef frame ); ``` |
| To | ``` CFArrayRef _Nonnull CTFrameGetLines (     CTFrameRef _Nonnull frame ); ``` |

Modified [CTFrameGetPath()](https://developer.apple.com/documentation/coretext/1510806-ctframegetpath)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CTFrameGetPath (     CTFrameRef frame ); ``` |
| To | ``` CGPathRef _Nonnull CTFrameGetPath (     CTFrameRef _Nonnull frame ); ``` |

Modified [CTFrameGetStringRange()](https://developer.apple.com/documentation/coretext/1508707-ctframegetstringrange)

|  | Declaration |
| --- | --- |
| From | ``` CFRange CTFrameGetStringRange (     CTFrameRef frame ); ``` |
| To | ``` CFRange CTFrameGetStringRange (     CTFrameRef _Nonnull frame ); ``` |

Modified [CTFrameGetVisibleStringRange()](https://developer.apple.com/documentation/coretext/1511109-ctframegetvisiblestringrange)

|  | Declaration |
| --- | --- |
| From | ``` CFRange CTFrameGetVisibleStringRange (     CTFrameRef frame ); ``` |
| To | ``` CFRange CTFrameGetVisibleStringRange (     CTFrameRef _Nonnull frame ); ``` |

#### CTFramesetter.h

Modified [CTFramesetterCreateFrame()](https://developer.apple.com/documentation/coretext/1478564-ctframesettercreateframe)

|  | Declaration |
| --- | --- |
| From | ``` CTFrameRef CTFramesetterCreateFrame (     CTFramesetterRef framesetter,     CFRange stringRange,     CGPathRef path,     CFDictionaryRef frameAttributes ); ``` |
| To | ``` CTFrameRef _Nonnull CTFramesetterCreateFrame (     CTFramesetterRef _Nonnull framesetter,     CFRange stringRange,     CGPathRef _Nonnull path,     CFDictionaryRef _Nullable frameAttributes ); ``` |

Modified [CTFramesetterCreateWithAttributedString()](https://developer.apple.com/documentation/coretext/1478568-ctframesettercreatewithattribute)

|  | Declaration |
| --- | --- |
| From | ``` CTFramesetterRef CTFramesetterCreateWithAttributedString (     CFAttributedStringRef string ); ``` |
| To | ``` CTFramesetterRef _Nonnull CTFramesetterCreateWithAttributedString (     CFAttributedStringRef _Nonnull string ); ``` |

Modified [CTFramesetterGetTypesetter()](https://developer.apple.com/documentation/coretext/1478562-ctframesettergettypesetter)

|  | Declaration |
| --- | --- |
| From | ``` CTTypesetterRef CTFramesetterGetTypesetter (     CTFramesetterRef framesetter ); ``` |
| To | ``` CTTypesetterRef _Nonnull CTFramesetterGetTypesetter (     CTFramesetterRef _Nonnull framesetter ); ``` |

Modified [CTFramesetterSuggestFrameSizeWithConstraints()](https://developer.apple.com/documentation/coretext/1478566-ctframesettersuggestframesizewit)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CTFramesetterSuggestFrameSizeWithConstraints (     CTFramesetterRef framesetter,     CFRange stringRange,     CFDictionaryRef frameAttributes,     CGSize constraints,     CFRange *fitRange ); ``` |
| To | ``` CGSize CTFramesetterSuggestFrameSizeWithConstraints (     CTFramesetterRef _Nonnull framesetter,     CFRange stringRange,     CFDictionaryRef _Nullable frameAttributes,     CGSize constraints,     CFRange * _Nullable fitRange ); ``` |

#### CTGlyphInfo.h

Modified [CTGlyphInfoCreateWithCharacterIdentifier()](https://developer.apple.com/documentation/coretext/1402042-ctglyphinfocreatewithcharacterid)

|  | Declaration |
| --- | --- |
| From | ``` CTGlyphInfoRef CTGlyphInfoCreateWithCharacterIdentifier (     CGFontIndex cid,     CTCharacterCollection collection,     CFStringRef baseString ); ``` |
| To | ``` CTGlyphInfoRef _Nonnull CTGlyphInfoCreateWithCharacterIdentifier (     CGFontIndex cid,     CTCharacterCollection collection,     CFStringRef _Nonnull baseString ); ``` |

Modified [CTGlyphInfoCreateWithGlyph()](https://developer.apple.com/documentation/coretext/1402062-ctglyphinfocreatewithglyph)

|  | Declaration |
| --- | --- |
| From | ``` CTGlyphInfoRef CTGlyphInfoCreateWithGlyph (     CGGlyph glyph,     CTFontRef font,     CFStringRef baseString ); ``` |
| To | ``` CTGlyphInfoRef _Nonnull CTGlyphInfoCreateWithGlyph (     CGGlyph glyph,     CTFontRef _Nonnull font,     CFStringRef _Nonnull baseString ); ``` |

Modified [CTGlyphInfoCreateWithGlyphName()](https://developer.apple.com/documentation/coretext/1402026-ctglyphinfocreatewithglyphname)

|  | Declaration |
| --- | --- |
| From | ``` CTGlyphInfoRef CTGlyphInfoCreateWithGlyphName (     CFStringRef glyphName,     CTFontRef font,     CFStringRef baseString ); ``` |
| To | ``` CTGlyphInfoRef _Nonnull CTGlyphInfoCreateWithGlyphName (     CFStringRef _Nonnull glyphName,     CTFontRef _Nonnull font,     CFStringRef _Nonnull baseString ); ``` |

Modified [CTGlyphInfoGetCharacterCollection()](https://developer.apple.com/documentation/coretext/1402034-ctglyphinfogetcharactercollectio)

|  | Declaration |
| --- | --- |
| From | ``` CTCharacterCollection CTGlyphInfoGetCharacterCollection (     CTGlyphInfoRef glyphInfo ); ``` |
| To | ``` CTCharacterCollection CTGlyphInfoGetCharacterCollection (     CTGlyphInfoRef _Nonnull glyphInfo ); ``` |

Modified [CTGlyphInfoGetCharacterIdentifier()](https://developer.apple.com/documentation/coretext/1402064-ctglyphinfogetcharacteridentifie)

|  | Declaration |
| --- | --- |
| From | ``` CGFontIndex CTGlyphInfoGetCharacterIdentifier (     CTGlyphInfoRef glyphInfo ); ``` |
| To | ``` CGFontIndex CTGlyphInfoGetCharacterIdentifier (     CTGlyphInfoRef _Nonnull glyphInfo ); ``` |

Modified [CTGlyphInfoGetGlyphName()](https://developer.apple.com/documentation/coretext/1402050-ctglyphinfogetglyphname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CTGlyphInfoGetGlyphName (     CTGlyphInfoRef glyphInfo ); ``` |
| To | ``` CFStringRef _Nullable CTGlyphInfoGetGlyphName (     CTGlyphInfoRef _Nonnull glyphInfo ); ``` |

Modified [kCTAdobeCNS1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobecns1charactercollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTAdobeGB1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobegb1charactercollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTAdobeJapan1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402052-kctadobejapan1charactercollectio)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTAdobeJapan2CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobejapan2charactercollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTAdobeKorea1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobekorea1charactercollection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTIdentityMappingCharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402054-kctidentitymappingcharactercolle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### CTLine.h

Added [CTLineEnumerateCaretOffsets()](https://developer.apple.com/documentation/coretext/1508685-ctlineenumeratecaretoffsets)Added [kCTLineBoundsIncludeLanguageExtents](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/1511234-includelanguageextents)Modified [CTLineCreateJustifiedLine()](https://developer.apple.com/documentation/coretext/1511238-ctlinecreatejustifiedline)

|  | Declaration |
| --- | --- |
| From | ``` CTLineRef CTLineCreateJustifiedLine (     CTLineRef line,     CGFloat justificationFactor,     double justificationWidth ); ``` |
| To | ``` CTLineRef _Nullable CTLineCreateJustifiedLine (     CTLineRef _Nonnull line,     CGFloat justificationFactor,     double justificationWidth ); ``` |

Modified [CTLineCreateTruncatedLine()](https://developer.apple.com/documentation/coretext/1510688-ctlinecreatetruncatedline)

|  | Declaration |
| --- | --- |
| From | ``` CTLineRef CTLineCreateTruncatedLine (     CTLineRef line,     double width,     CTLineTruncationType truncationType,     CTLineRef truncationToken ); ``` |
| To | ``` CTLineRef _Nullable CTLineCreateTruncatedLine (     CTLineRef _Nonnull line,     double width,     CTLineTruncationType truncationType,     CTLineRef _Nullable truncationToken ); ``` |

Modified [CTLineCreateWithAttributedString()](https://developer.apple.com/documentation/coretext/1509461-ctlinecreatewithattributedstring)

|  | Declaration |
| --- | --- |
| From | ``` CTLineRef CTLineCreateWithAttributedString (     CFAttributedStringRef string ); ``` |
| To | ``` CTLineRef _Nonnull CTLineCreateWithAttributedString (     CFAttributedStringRef _Nonnull attrString ); ``` |

Modified [CTLineDraw()](https://developer.apple.com/documentation/coretext/1511145-ctlinedraw)

|  | Declaration |
| --- | --- |
| From | ``` void CTLineDraw (     CTLineRef line,     CGContextRef context ); ``` |
| To | ``` void CTLineDraw (     CTLineRef _Nonnull line,     CGContextRef _Nonnull context ); ``` |

Modified [CTLineGetBoundsWithOptions()](https://developer.apple.com/documentation/coretext/1511332-ctlinegetboundswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CTLineGetBoundsWithOptions (     CTLineRef line,     CTLineBoundsOptions options ); ``` |
| To | ``` CGRect CTLineGetBoundsWithOptions (     CTLineRef _Nonnull line,     CTLineBoundsOptions options ); ``` |

Modified [CTLineGetGlyphCount()](https://developer.apple.com/documentation/coretext/1509985-ctlinegetglyphcount)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTLineGetGlyphCount (     CTLineRef line ); ``` |
| To | ``` CFIndex CTLineGetGlyphCount (     CTLineRef _Nonnull line ); ``` |

Modified [CTLineGetGlyphRuns()](https://developer.apple.com/documentation/coretext/1509800-ctlinegetglyphruns)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CTLineGetGlyphRuns (     CTLineRef line ); ``` |
| To | ``` CFArrayRef _Nonnull CTLineGetGlyphRuns (     CTLineRef _Nonnull line ); ``` |

Modified [CTLineGetImageBounds()](https://developer.apple.com/documentation/coretext/1510967-ctlinegetimagebounds)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CTLineGetImageBounds (     CTLineRef line,     CGContextRef context ); ``` |
| To | ``` CGRect CTLineGetImageBounds (     CTLineRef _Nonnull line,     CGContextRef _Nullable context ); ``` |

Modified [CTLineGetOffsetForStringIndex()](https://developer.apple.com/documentation/coretext/1509629-ctlinegetoffsetforstringindex)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTLineGetOffsetForStringIndex (     CTLineRef line,     CFIndex charIndex,     CGFloat *secondaryOffset ); ``` |
| To | ``` CGFloat CTLineGetOffsetForStringIndex (     CTLineRef _Nonnull line,     CFIndex charIndex,     CGFloat * _Nullable secondaryOffset ); ``` |

Modified [CTLineGetPenOffsetForFlush()](https://developer.apple.com/documentation/coretext/1511056-ctlinegetpenoffsetforflush)

|  | Declaration |
| --- | --- |
| From | ``` double CTLineGetPenOffsetForFlush (     CTLineRef line,     CGFloat flushFactor,     double flushWidth ); ``` |
| To | ``` double CTLineGetPenOffsetForFlush (     CTLineRef _Nonnull line,     CGFloat flushFactor,     double flushWidth ); ``` |

Modified [CTLineGetStringIndexForPosition()](https://developer.apple.com/documentation/coretext/1508876-ctlinegetstringindexforposition)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTLineGetStringIndexForPosition (     CTLineRef line,     CGPoint position ); ``` |
| To | ``` CFIndex CTLineGetStringIndexForPosition (     CTLineRef _Nonnull line,     CGPoint position ); ``` |

Modified [CTLineGetStringRange()](https://developer.apple.com/documentation/coretext/1509733-ctlinegetstringrange)

|  | Declaration |
| --- | --- |
| From | ``` CFRange CTLineGetStringRange (     CTLineRef line ); ``` |
| To | ``` CFRange CTLineGetStringRange (     CTLineRef _Nonnull line ); ``` |

Modified [CTLineGetTrailingWhitespaceWidth()](https://developer.apple.com/documentation/coretext/1511357-ctlinegettrailingwhitespacewidth)

|  | Declaration |
| --- | --- |
| From | ``` double CTLineGetTrailingWhitespaceWidth (     CTLineRef line ); ``` |
| To | ``` double CTLineGetTrailingWhitespaceWidth (     CTLineRef _Nonnull line ); ``` |

Modified [CTLineGetTypographicBounds()](https://developer.apple.com/documentation/coretext/1510360-ctlinegettypographicbounds)

|  | Declaration |
| --- | --- |
| From | ``` double CTLineGetTypographicBounds (     CTLineRef line,     CGFloat *ascent,     CGFloat *descent,     CGFloat *leading ); ``` |
| To | ``` double CTLineGetTypographicBounds (     CTLineRef _Nonnull line,     CGFloat * _Nullable ascent,     CGFloat * _Nullable descent,     CGFloat * _Nullable leading ); ``` |

#### CTParagraphStyle.h

Modified [CTParagraphStyleCreate()](https://developer.apple.com/documentation/coretext/1496164-ctparagraphstylecreate)

|  | Declaration |
| --- | --- |
| From | ``` CTParagraphStyleRef CTParagraphStyleCreate (     const CTParagraphStyleSetting *settings,     size_t settingCount ); ``` |
| To | ``` CTParagraphStyleRef _Nonnull CTParagraphStyleCreate (     const CTParagraphStyleSetting * _Nullable settings,     size_t settingCount ); ``` |

Modified [CTParagraphStyleCreateCopy()](https://developer.apple.com/documentation/coretext/1496153-ctparagraphstylecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` CTParagraphStyleRef CTParagraphStyleCreateCopy (     CTParagraphStyleRef paragraphStyle ); ``` |
| To | ``` CTParagraphStyleRef _Nonnull CTParagraphStyleCreateCopy (     CTParagraphStyleRef _Nonnull paragraphStyle ); ``` |

Modified [CTParagraphStyleGetValueForSpecifier()](https://developer.apple.com/documentation/coretext/1496169-ctparagraphstylegetvalueforspeci)

|  | Declaration |
| --- | --- |
| From | ``` bool CTParagraphStyleGetValueForSpecifier (     CTParagraphStyleRef paragraphStyle,     CTParagraphStyleSpecifier spec,     size_t valueBufferSize,     void *valueBuffer ); ``` |
| To | ``` bool CTParagraphStyleGetValueForSpecifier (     CTParagraphStyleRef _Nonnull paragraphStyle,     CTParagraphStyleSpecifier spec,     size_t valueBufferSize,     void * _Nonnull valueBuffer ); ``` |

Modified [kCTCenterTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctcentertextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTJustifiedTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/1496119-kctjustifiedtextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTLeftTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctlefttextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTNaturalTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctnaturaltextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCTRightTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctrighttextalignment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### CTRubyAnnotation.h

Modified [CTRubyAnnotationCreate()](https://developer.apple.com/documentation/coretext/1510191-ctrubyannotationcreate)

|  | Declaration |
| --- | --- |
| From | ``` CTRubyAnnotationRef CTRubyAnnotationCreate (     CTRubyAlignment alignment,     CTRubyOverhang overhang,     CGFloat sizeFactor,     CFStringRef text[4] ); ``` |
| To | ``` CTRubyAnnotationRef _Nonnull CTRubyAnnotationCreate (     CTRubyAlignment alignment,     CTRubyOverhang overhang,     CGFloat sizeFactor,     CFStringRef  _Nonnull text[4] ); ``` |

Modified [CTRubyAnnotationCreateCopy()](https://developer.apple.com/documentation/coretext/1508925-ctrubyannotationcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` CTRubyAnnotationRef CTRubyAnnotationCreateCopy (     CTRubyAnnotationRef rubyAnnotation ); ``` |
| To | ``` CTRubyAnnotationRef _Nonnull CTRubyAnnotationCreateCopy (     CTRubyAnnotationRef _Nonnull rubyAnnotation ); ``` |

Modified [CTRubyAnnotationGetAlignment()](https://developer.apple.com/documentation/coretext/1508832-ctrubyannotationgetalignment)

|  | Declaration |
| --- | --- |
| From | ``` CTRubyAlignment CTRubyAnnotationGetAlignment (     CTRubyAnnotationRef rubyAnnotation ); ``` |
| To | ``` CTRubyAlignment CTRubyAnnotationGetAlignment (     CTRubyAnnotationRef _Nonnull rubyAnnotation ); ``` |

Modified [CTRubyAnnotationGetOverhang()](https://developer.apple.com/documentation/coretext/1509866-ctrubyannotationgetoverhang)

|  | Declaration |
| --- | --- |
| From | ``` CTRubyOverhang CTRubyAnnotationGetOverhang (     CTRubyAnnotationRef rubyAnnotation ); ``` |
| To | ``` CTRubyOverhang CTRubyAnnotationGetOverhang (     CTRubyAnnotationRef _Nonnull rubyAnnotation ); ``` |

Modified [CTRubyAnnotationGetSizeFactor()](https://developer.apple.com/documentation/coretext/1509594-ctrubyannotationgetsizefactor)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CTRubyAnnotationGetSizeFactor (     CTRubyAnnotationRef rubyAnnotation ); ``` |
| To | ``` CGFloat CTRubyAnnotationGetSizeFactor (     CTRubyAnnotationRef _Nonnull rubyAnnotation ); ``` |

Modified [CTRubyAnnotationGetTextForPosition()](https://developer.apple.com/documentation/coretext/1511023-ctrubyannotationgettextforpositi)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CTRubyAnnotationGetTextForPosition (     CTRubyAnnotationRef rubyAnnotation,     CTRubyPosition position ); ``` |
| To | ``` CFStringRef _Nullable CTRubyAnnotationGetTextForPosition (     CTRubyAnnotationRef _Nonnull rubyAnnotation,     CTRubyPosition position ); ``` |

#### CTRun.h

Modified [CTRunDraw()](https://developer.apple.com/documentation/coretext/1509440-ctrundraw)

|  | Declaration |
| --- | --- |
| From | ``` void CTRunDraw (     CTRunRef run,     CGContextRef context,     CFRange range ); ``` |
| To | ``` void CTRunDraw (     CTRunRef _Nonnull run,     CGContextRef _Nonnull context,     CFRange range ); ``` |

Modified [CTRunGetAdvances()](https://developer.apple.com/documentation/coretext/1510488-ctrungetadvances)

|  | Declaration |
| --- | --- |
| From | ``` void CTRunGetAdvances (     CTRunRef run,     CFRange range,     CGSize buffer[] ); ``` |
| To | ``` void CTRunGetAdvances (     CTRunRef _Nonnull run,     CFRange range,     CGSize buffer[] ); ``` |

Modified [CTRunGetAdvancesPtr()](https://developer.apple.com/documentation/coretext/1508625-ctrungetadvancesptr)

|  | Declaration |
| --- | --- |
| From | ``` const CGSize * CTRunGetAdvancesPtr (     CTRunRef run ); ``` |
| To | ``` const CGSize * _Nullable CTRunGetAdvancesPtr (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetAttributes()](https://developer.apple.com/documentation/coretext/1510805-ctrungetattributes)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CTRunGetAttributes (     CTRunRef run ); ``` |
| To | ``` CFDictionaryRef _Nonnull CTRunGetAttributes (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetGlyphCount()](https://developer.apple.com/documentation/coretext/1510779-ctrungetglyphcount)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTRunGetGlyphCount (     CTRunRef run ); ``` |
| To | ``` CFIndex CTRunGetGlyphCount (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetGlyphs()](https://developer.apple.com/documentation/coretext/1509249-ctrungetglyphs)

|  | Declaration |
| --- | --- |
| From | ``` void CTRunGetGlyphs (     CTRunRef run,     CFRange range,     CGGlyph buffer[] ); ``` |
| To | ``` void CTRunGetGlyphs (     CTRunRef _Nonnull run,     CFRange range,     CGGlyph buffer[] ); ``` |

Modified [CTRunGetGlyphsPtr()](https://developer.apple.com/documentation/coretext/1509952-ctrungetglyphsptr)

|  | Declaration |
| --- | --- |
| From | ``` const CGGlyph * CTRunGetGlyphsPtr (     CTRunRef run ); ``` |
| To | ``` const CGGlyph * _Nullable CTRunGetGlyphsPtr (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetImageBounds()](https://developer.apple.com/documentation/coretext/1509963-ctrungetimagebounds)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CTRunGetImageBounds (     CTRunRef run,     CGContextRef context,     CFRange range ); ``` |
| To | ``` CGRect CTRunGetImageBounds (     CTRunRef _Nonnull run,     CGContextRef _Nullable context,     CFRange range ); ``` |

Modified [CTRunGetPositions()](https://developer.apple.com/documentation/coretext/1508678-ctrungetpositions)

|  | Declaration |
| --- | --- |
| From | ``` void CTRunGetPositions (     CTRunRef run,     CFRange range,     CGPoint buffer[] ); ``` |
| To | ``` void CTRunGetPositions (     CTRunRef _Nonnull run,     CFRange range,     CGPoint buffer[] ); ``` |

Modified [CTRunGetPositionsPtr()](https://developer.apple.com/documentation/coretext/1510044-ctrungetpositionsptr)

|  | Declaration |
| --- | --- |
| From | ``` const CGPoint * CTRunGetPositionsPtr (     CTRunRef run ); ``` |
| To | ``` const CGPoint * _Nullable CTRunGetPositionsPtr (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetStatus()](https://developer.apple.com/documentation/coretext/1510665-ctrungetstatus)

|  | Declaration |
| --- | --- |
| From | ``` CTRunStatus CTRunGetStatus (     CTRunRef run ); ``` |
| To | ``` CTRunStatus CTRunGetStatus (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetStringIndices()](https://developer.apple.com/documentation/coretext/1511382-ctrungetstringindices)

|  | Declaration |
| --- | --- |
| From | ``` void CTRunGetStringIndices (     CTRunRef run,     CFRange range,     CFIndex buffer[] ); ``` |
| To | ``` void CTRunGetStringIndices (     CTRunRef _Nonnull run,     CFRange range,     CFIndex buffer[] ); ``` |

Modified [CTRunGetStringIndicesPtr()](https://developer.apple.com/documentation/coretext/1510605-ctrungetstringindicesptr)

|  | Declaration |
| --- | --- |
| From | ``` const CFIndex * CTRunGetStringIndicesPtr (     CTRunRef run ); ``` |
| To | ``` const CFIndex * _Nullable CTRunGetStringIndicesPtr (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetStringRange()](https://developer.apple.com/documentation/coretext/1510020-ctrungetstringrange)

|  | Declaration |
| --- | --- |
| From | ``` CFRange CTRunGetStringRange (     CTRunRef run ); ``` |
| To | ``` CFRange CTRunGetStringRange (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetTextMatrix()](https://developer.apple.com/documentation/coretext/1508680-ctrungettextmatrix)

|  | Declaration |
| --- | --- |
| From | ``` CGAffineTransform CTRunGetTextMatrix (     CTRunRef run ); ``` |
| To | ``` CGAffineTransform CTRunGetTextMatrix (     CTRunRef _Nonnull run ); ``` |

Modified [CTRunGetTypographicBounds()](https://developer.apple.com/documentation/coretext/1510569-ctrungettypographicbounds)

|  | Declaration |
| --- | --- |
| From | ``` double CTRunGetTypographicBounds (     CTRunRef run,     CFRange range,     CGFloat *ascent,     CGFloat *descent,     CGFloat *leading ); ``` |
| To | ``` double CTRunGetTypographicBounds (     CTRunRef _Nonnull run,     CFRange range,     CGFloat * _Nullable ascent,     CGFloat * _Nullable descent,     CGFloat * _Nullable leading ); ``` |

#### CTRunDelegate.h

Modified [CTRunDelegateCreate()](https://developer.apple.com/documentation/coretext/1498167-ctrundelegatecreate)

|  | Declaration |
| --- | --- |
| From | ``` CTRunDelegateRef CTRunDelegateCreate (     const CTRunDelegateCallbacks *callbacks,     void *refCon ); ``` |
| To | ``` CTRunDelegateRef _Nullable CTRunDelegateCreate (     const CTRunDelegateCallbacks * _Nonnull callbacks,     void * _Nullable refCon ); ``` |

Modified [CTRunDelegateGetRefCon()](https://developer.apple.com/documentation/coretext/1498169-ctrundelegategetrefcon)

|  | Declaration |
| --- | --- |
| From | ``` void * CTRunDelegateGetRefCon (     CTRunDelegateRef runDelegate ); ``` |
| To | ``` void * _Nonnull CTRunDelegateGetRefCon (     CTRunDelegateRef _Nonnull runDelegate ); ``` |

#### CTStringAttributes.h

Modified [kCTCharacterShapeAttributeName](https://developer.apple.com/documentation/coretext/kctcharactershapeattributename)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### CTTextTab.h

Modified [CTTextTabCreate()](https://developer.apple.com/documentation/coretext/1511279-cttexttabcreate)

|  | Declaration |
| --- | --- |
| From | ``` CTTextTabRef CTTextTabCreate (     CTTextAlignment alignment,     double location,     CFDictionaryRef options ); ``` |
| To | ``` CTTextTabRef _Nonnull CTTextTabCreate (     CTTextAlignment alignment,     double location,     CFDictionaryRef _Nullable options ); ``` |

Modified [CTTextTabGetAlignment()](https://developer.apple.com/documentation/coretext/1509582-cttexttabgetalignment)

|  | Declaration |
| --- | --- |
| From | ``` CTTextAlignment CTTextTabGetAlignment (     CTTextTabRef tab ); ``` |
| To | ``` CTTextAlignment CTTextTabGetAlignment (     CTTextTabRef _Nonnull tab ); ``` |

Modified [CTTextTabGetLocation()](https://developer.apple.com/documentation/coretext/1510746-cttexttabgetlocation)

|  | Declaration |
| --- | --- |
| From | ``` double CTTextTabGetLocation (     CTTextTabRef tab ); ``` |
| To | ``` double CTTextTabGetLocation (     CTTextTabRef _Nonnull tab ); ``` |

Modified [CTTextTabGetOptions()](https://developer.apple.com/documentation/coretext/1509173-cttexttabgetoptions)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CTTextTabGetOptions (     CTTextTabRef tab ); ``` |
| To | ``` CFDictionaryRef _Nullable CTTextTabGetOptions (     CTTextTabRef _Nonnull tab ); ``` |

#### CTTypesetter.h

Modified [CTTypesetterCreateLine()](https://developer.apple.com/documentation/coretext/1510513-cttypesettercreateline)

|  | Declaration |
| --- | --- |
| From | ``` CTLineRef CTTypesetterCreateLine (     CTTypesetterRef typesetter,     CFRange stringRange ); ``` |
| To | ``` CTLineRef _Nonnull CTTypesetterCreateLine (     CTTypesetterRef _Nonnull typesetter,     CFRange stringRange ); ``` |

Modified [CTTypesetterCreateLineWithOffset()](https://developer.apple.com/documentation/coretext/1510023-cttypesettercreatelinewithoffset)

|  | Declaration |
| --- | --- |
| From | ``` CTLineRef CTTypesetterCreateLineWithOffset (     CTTypesetterRef typesetter,     CFRange stringRange,     double offset ); ``` |
| To | ``` CTLineRef _Nonnull CTTypesetterCreateLineWithOffset (     CTTypesetterRef _Nonnull typesetter,     CFRange stringRange,     double offset ); ``` |

Modified [CTTypesetterCreateWithAttributedString()](https://developer.apple.com/documentation/coretext/1511438-cttypesettercreatewithattributed)

|  | Declaration |
| --- | --- |
| From | ``` CTTypesetterRef CTTypesetterCreateWithAttributedString (     CFAttributedStringRef string ); ``` |
| To | ``` CTTypesetterRef _Nonnull CTTypesetterCreateWithAttributedString (     CFAttributedStringRef _Nonnull string ); ``` |

Modified [CTTypesetterCreateWithAttributedStringAndOptions()](https://developer.apple.com/documentation/coretext/1510401-cttypesettercreatewithattributed)

|  | Declaration |
| --- | --- |
| From | ``` CTTypesetterRef CTTypesetterCreateWithAttributedStringAndOptions (     CFAttributedStringRef string,     CFDictionaryRef options ); ``` |
| To | ``` CTTypesetterRef _Nonnull CTTypesetterCreateWithAttributedStringAndOptions (     CFAttributedStringRef _Nonnull string,     CFDictionaryRef _Nullable options ); ``` |

Modified [CTTypesetterSuggestClusterBreak()](https://developer.apple.com/documentation/coretext/1508669-cttypesettersuggestclusterbreak)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTTypesetterSuggestClusterBreak (     CTTypesetterRef typesetter,     CFIndex startIndex,     double width ); ``` |
| To | ``` CFIndex CTTypesetterSuggestClusterBreak (     CTTypesetterRef _Nonnull typesetter,     CFIndex startIndex,     double width ); ``` |

Modified [CTTypesetterSuggestClusterBreakWithOffset()](https://developer.apple.com/documentation/coretext/1511119-cttypesettersuggestclusterbreakw)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTTypesetterSuggestClusterBreakWithOffset (     CTTypesetterRef typesetter,     CFIndex startIndex,     double width,     double offset ); ``` |
| To | ``` CFIndex CTTypesetterSuggestClusterBreakWithOffset (     CTTypesetterRef _Nonnull typesetter,     CFIndex startIndex,     double width,     double offset ); ``` |

Modified [CTTypesetterSuggestLineBreak()](https://developer.apple.com/documentation/coretext/1510080-cttypesettersuggestlinebreak)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTTypesetterSuggestLineBreak (     CTTypesetterRef typesetter,     CFIndex startIndex,     double width ); ``` |
| To | ``` CFIndex CTTypesetterSuggestLineBreak (     CTTypesetterRef _Nonnull typesetter,     CFIndex startIndex,     double width ); ``` |

Modified [CTTypesetterSuggestLineBreakWithOffset()](https://developer.apple.com/documentation/coretext/1508862-cttypesettersuggestlinebreakwith)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CTTypesetterSuggestLineBreakWithOffset (     CTTypesetterRef typesetter,     CFIndex startIndex,     double width,     double offset ); ``` |
| To | ``` CFIndex CTTypesetterSuggestLineBreakWithOffset (     CTTypesetterRef _Nonnull typesetter,     CFIndex startIndex,     double width,     double offset ); ``` |

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
