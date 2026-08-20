---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreText.html
archived_at: '2026-07-18T02:56:10.660413Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreText Changes

## CoreText

Removed CTFontOptions.valueRemoved CTFontStylisticClass.valueRemoved CTFontSymbolicTraits.valueRemoved CTFontTableOptions.valueRemoved CTLineBoundsOptions.valueRemoved CTRunStatus.valueRemoved CTUnderlineStyle.valueRemoved CTUnderlineStyleModifiers.valueAdded CTFontOptions.init(rawValue: CFOptionFlags)Added CTFontStylisticClass.init(rawValue: UInt32)Added CTFontSymbolicTraits.init(rawValue: UInt32)Added CTFontTableOptions.init(rawValue: UInt32)Added CTLineBoundsOptions.init(rawValue: CFOptionFlags)Added CTRunStatus.init(rawValue: UInt32)Added CTUnderlineStyle.init(rawValue: Int32)Added CTUnderlineStyleModifiers.init(rawValue: Int32)Modified CTFontOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTFontOptions : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Default: CTFontOptions { get }     static var PreventAutoActivation: CTFontOptions { get }     static var PreferSystemFont: CTFontOptions { get } } ``` |
| To | ``` struct CTFontOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Default: CTFontOptions { get }     static var PreventAutoActivation: CTFontOptions { get }     static var PreferSystemFont: CTFontOptions { get } } ``` |

Modified CTFontOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CTFontStylisticClass [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTFontStylisticClass : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var ClassUnknown: CTFontStylisticClass { get }     static var ClassOldStyleSerifs: CTFontStylisticClass { get }     static var ClassTransitionalSerifs: CTFontStylisticClass { get }     static var ClassModernSerifs: CTFontStylisticClass { get }     static var ClassClarendonSerifs: CTFontStylisticClass { get }     static var ClassSlabSerifs: CTFontStylisticClass { get }     static var ClassFreeformSerifs: CTFontStylisticClass { get }     static var ClassSansSerif: CTFontStylisticClass { get }     static var ClassOrnamentals: CTFontStylisticClass { get }     static var ClassScripts: CTFontStylisticClass { get }     static var ClassSymbolic: CTFontStylisticClass { get }     static var UnknownClass: CTFontStylisticClass { get }     static var OldStyleSerifsClass: CTFontStylisticClass { get }     static var TransitionalSerifsClass: CTFontStylisticClass { get }     static var ModernSerifsClass: CTFontStylisticClass { get }     static var ClarendonSerifsClass: CTFontStylisticClass { get }     static var SlabSerifsClass: CTFontStylisticClass { get }     static var FreeformSerifsClass: CTFontStylisticClass { get }     static var SansSerifClass: CTFontStylisticClass { get }     static var OrnamentalsClass: CTFontStylisticClass { get }     static var ScriptsClass: CTFontStylisticClass { get }     static var SymbolicClass: CTFontStylisticClass { get } } ``` |
| To | ``` struct CTFontStylisticClass : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var ClassUnknown: CTFontStylisticClass { get }     static var ClassOldStyleSerifs: CTFontStylisticClass { get }     static var ClassTransitionalSerifs: CTFontStylisticClass { get }     static var ClassModernSerifs: CTFontStylisticClass { get }     static var ClassClarendonSerifs: CTFontStylisticClass { get }     static var ClassSlabSerifs: CTFontStylisticClass { get }     static var ClassFreeformSerifs: CTFontStylisticClass { get }     static var ClassSansSerif: CTFontStylisticClass { get }     static var ClassOrnamentals: CTFontStylisticClass { get }     static var ClassScripts: CTFontStylisticClass { get }     static var ClassSymbolic: CTFontStylisticClass { get }     static var UnknownClass: CTFontStylisticClass { get }     static var OldStyleSerifsClass: CTFontStylisticClass { get }     static var TransitionalSerifsClass: CTFontStylisticClass { get }     static var ModernSerifsClass: CTFontStylisticClass { get }     static var ClarendonSerifsClass: CTFontStylisticClass { get }     static var SlabSerifsClass: CTFontStylisticClass { get }     static var FreeformSerifsClass: CTFontStylisticClass { get }     static var SansSerifClass: CTFontStylisticClass { get }     static var OrnamentalsClass: CTFontStylisticClass { get }     static var ScriptsClass: CTFontStylisticClass { get }     static var SymbolicClass: CTFontStylisticClass { get } } ``` |

Modified CTFontStylisticClass.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CTFontSymbolicTraits [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTFontSymbolicTraits : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var TraitItalic: CTFontSymbolicTraits { get }     static var TraitBold: CTFontSymbolicTraits { get }     static var TraitExpanded: CTFontSymbolicTraits { get }     static var TraitCondensed: CTFontSymbolicTraits { get }     static var TraitMonoSpace: CTFontSymbolicTraits { get }     static var TraitVertical: CTFontSymbolicTraits { get }     static var TraitUIOptimized: CTFontSymbolicTraits { get }     static var TraitColorGlyphs: CTFontSymbolicTraits { get }     static var TraitComposite: CTFontSymbolicTraits { get }     static var TraitClassMask: CTFontSymbolicTraits { get }     static var ItalicTrait: CTFontSymbolicTraits { get }     static var BoldTrait: CTFontSymbolicTraits { get }     static var ExpandedTrait: CTFontSymbolicTraits { get }     static var CondensedTrait: CTFontSymbolicTraits { get }     static var MonoSpaceTrait: CTFontSymbolicTraits { get }     static var VerticalTrait: CTFontSymbolicTraits { get }     static var UIOptimizedTrait: CTFontSymbolicTraits { get }     static var ColorGlyphsTrait: CTFontSymbolicTraits { get }     static var CompositeTrait: CTFontSymbolicTraits { get }     static var ClassMaskTrait: CTFontSymbolicTraits { get } } ``` |
| To | ``` struct CTFontSymbolicTraits : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var TraitItalic: CTFontSymbolicTraits { get }     static var TraitBold: CTFontSymbolicTraits { get }     static var TraitExpanded: CTFontSymbolicTraits { get }     static var TraitCondensed: CTFontSymbolicTraits { get }     static var TraitMonoSpace: CTFontSymbolicTraits { get }     static var TraitVertical: CTFontSymbolicTraits { get }     static var TraitUIOptimized: CTFontSymbolicTraits { get }     static var TraitColorGlyphs: CTFontSymbolicTraits { get }     static var TraitComposite: CTFontSymbolicTraits { get }     static var TraitClassMask: CTFontSymbolicTraits { get }     static var ItalicTrait: CTFontSymbolicTraits { get }     static var BoldTrait: CTFontSymbolicTraits { get }     static var ExpandedTrait: CTFontSymbolicTraits { get }     static var CondensedTrait: CTFontSymbolicTraits { get }     static var MonoSpaceTrait: CTFontSymbolicTraits { get }     static var VerticalTrait: CTFontSymbolicTraits { get }     static var UIOptimizedTrait: CTFontSymbolicTraits { get }     static var ColorGlyphsTrait: CTFontSymbolicTraits { get }     static var CompositeTrait: CTFontSymbolicTraits { get }     static var ClassMaskTrait: CTFontSymbolicTraits { get } } ``` |

Modified CTFontSymbolicTraits.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CTFontTableOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTFontTableOptions : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var NoOptions: CTFontTableOptions { get }     static var ExcludeSynthetic: CTFontTableOptions { get } } ``` |
| To | ``` struct CTFontTableOptions : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var NoOptions: CTFontTableOptions { get }     static var ExcludeSynthetic: CTFontTableOptions { get } } ``` |

Modified CTFontTableOptions.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CTLineBoundsOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTLineBoundsOptions : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var ExcludeTypographicLeading: CTLineBoundsOptions { get }     static var ExcludeTypographicShifts: CTLineBoundsOptions { get }     static var UseHangingPunctuation: CTLineBoundsOptions { get }     static var UseGlyphPathBounds: CTLineBoundsOptions { get }     static var UseOpticalBounds: CTLineBoundsOptions { get }     static var IncludeLanguageExtents: CTLineBoundsOptions { get } } ``` |
| To | ``` struct CTLineBoundsOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var ExcludeTypographicLeading: CTLineBoundsOptions { get }     static var ExcludeTypographicShifts: CTLineBoundsOptions { get }     static var UseHangingPunctuation: CTLineBoundsOptions { get }     static var UseGlyphPathBounds: CTLineBoundsOptions { get }     static var UseOpticalBounds: CTLineBoundsOptions { get }     static var IncludeLanguageExtents: CTLineBoundsOptions { get } } ``` |

Modified CTLineBoundsOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CTRunStatus [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTRunStatus : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var NoStatus: CTRunStatus { get }     static var RightToLeft: CTRunStatus { get }     static var NonMonotonic: CTRunStatus { get }     static var HasNonIdentityMatrix: CTRunStatus { get } } ``` |
| To | ``` struct CTRunStatus : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var NoStatus: CTRunStatus { get }     static var RightToLeft: CTRunStatus { get }     static var NonMonotonic: CTRunStatus { get }     static var HasNonIdentityMatrix: CTRunStatus { get } } ``` |

Modified CTRunStatus.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CTUnderlineStyle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTUnderlineStyle : RawOptionSetType {     init(_ value: Int32)     var value: Int32     static var None: CTUnderlineStyle { get }     static var Single: CTUnderlineStyle { get }     static var Thick: CTUnderlineStyle { get }     static var Double: CTUnderlineStyle { get } } ``` |
| To | ``` struct CTUnderlineStyle : RawOptionSetType {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     static var None: CTUnderlineStyle { get }     static var Single: CTUnderlineStyle { get }     static var Thick: CTUnderlineStyle { get }     static var Double: CTUnderlineStyle { get } } ``` |

Modified CTUnderlineStyle.init(_: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: Int32) ``` |
| To | ``` init(_ rawValue: Int32) ``` |

Modified CTUnderlineStyleModifiers [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTUnderlineStyleModifiers : RawOptionSetType {     init(_ value: Int32)     var value: Int32     static var PatternSolid: CTUnderlineStyleModifiers { get }     static var PatternDot: CTUnderlineStyleModifiers { get }     static var PatternDash: CTUnderlineStyleModifiers { get }     static var PatternDashDot: CTUnderlineStyleModifiers { get }     static var PatternDashDotDot: CTUnderlineStyleModifiers { get } } ``` |
| To | ``` struct CTUnderlineStyleModifiers : RawOptionSetType {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     static var PatternSolid: CTUnderlineStyleModifiers { get }     static var PatternDot: CTUnderlineStyleModifiers { get }     static var PatternDash: CTUnderlineStyleModifiers { get }     static var PatternDashDot: CTUnderlineStyleModifiers { get }     static var PatternDashDotDot: CTUnderlineStyleModifiers { get } } ``` |

Modified CTUnderlineStyleModifiers.init(_: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: Int32) ``` |
| To | ``` init(_ rawValue: Int32) ``` |

Modified CTFontCollectionCreateCopyWithFontDescriptors(CTFontCollection!, CFArray!, CFDictionary!) -> CTFontCollection!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCollectionCreateFromAvailableFonts(CFDictionary!) -> CTFontCollection!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection!, CTFontCollectionSortDescriptorsCallback, UnsafeMutablePointer<Void>) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCollectionCreateWithFontDescriptors(CFArray!, CFDictionary!) -> CTFontCollection!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCollectionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyAttribute(CTFont!, CFString!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyAvailableTables(CTFont!, CTFontTableOptions) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyCharacterSet(CTFont!) -> CFCharacterSet!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyDefaultCascadeListForLanguages(CTFont!, CFArray!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CTFontCopyDisplayName(CTFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyFamilyName(CTFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyFeatureSettings(CTFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyFeatures(CTFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyFontDescriptor(CTFont!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyFullName(CTFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyGraphicsFont(CTFont!, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> CGFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyLocalizedName(CTFont!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyName(CTFont!, CFString!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyPostScriptName(CTFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopySupportedLanguages(CTFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyTable(CTFont!, CTFontTableTag, CTFontTableOptions) -> CFData!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyTraits(CTFont!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyVariation(CTFont!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCopyVariationAxes(CTFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateCopyWithAttributes(CTFont!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontDescriptor!) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateCopyWithFamily(CTFont!, CGFloat, UnsafePointer<CGAffineTransform>, CFString!) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateCopyWithSymbolicTraits(CTFont!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateForString(CTFont!, CFString!, CFRange) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreatePathForGlyph(CTFont!, CGGlyph, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateUIFontForLanguage(CTFontUIFontType, CGFloat, CFString!) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateWithFontDescriptor(CTFontDescriptor!, CGFloat, UnsafePointer<CGAffineTransform>) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateWithFontDescriptorAndOptions(CTFontDescriptor!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontOptions) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateWithGraphicsFont(CGFont!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontDescriptor!) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateWithName(CFString!, CGFloat, UnsafePointer<CGAffineTransform>) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontCreateWithNameAndOptions(CFString!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontOptions) -> CTFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCopyAttribute(CTFontDescriptor!, CFString!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCopyAttributes(CTFontDescriptor!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCopyLocalizedAttribute(CTFontDescriptor!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCreateCopyWithAttributes(CTFontDescriptor!, CFDictionary!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCreateCopyWithFamily(CTFontDescriptor!, CFString!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CTFontDescriptorCreateCopyWithFeature(CTFontDescriptor!, CFNumber!, CFNumber!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCreateCopyWithSymbolicTraits(CTFontDescriptor!, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CTFontDescriptorCreateCopyWithVariation(CTFontDescriptor!, CFNumber!, CGFloat) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCreateMatchingFontDescriptor(CTFontDescriptor!, CFSet!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCreateMatchingFontDescriptors(CTFontDescriptor!, CFSet!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCreateWithAttributes(CFDictionary!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorCreateWithNameAndSize(CFString!, CGFloat) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontDescriptorMatchFontDescriptorsWithProgressHandler(CFArray!, CFSet!, CTFontDescriptorProgressHandler!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CTFontDrawGlyphs(CTFont!, UnsafePointer<CGGlyph>, UnsafePointer<CGPoint>, UInt, CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified CTFontGetAdvancesForGlyphs(CTFont!, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetAscent(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetBoundingBox(CTFont!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetBoundingRectsForGlyphs(CTFont!, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>, CFIndex) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetCapHeight(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetDescent(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetGlyphCount(CTFont!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetGlyphWithName(CTFont!, CFString!) -> CGGlyph

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetGlyphsForCharacters(CTFont!, UnsafePointer<UniChar>, UnsafeMutablePointer<CGGlyph>, CFIndex) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetLeading(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetLigatureCaretPositions(CTFont!, CGGlyph, UnsafeMutablePointer<CGFloat>, CFIndex) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetMatrix(CTFont!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetOpticalBoundsForGlyphs(CTFont!, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>, CFIndex, CFOptionFlags) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CTFontGetSize(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetSlantAngle(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetStringEncoding(CTFont!) -> CFStringEncoding

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetSymbolicTraits(CTFont!) -> CTFontSymbolicTraits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetUnderlinePosition(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetUnderlineThickness(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetUnitsPerEm(CTFont!) -> UInt32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetVerticalTranslationsForGlyphs(CTFont!, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontGetXHeight(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFontManagerCreateFontDescriptorFromData(CFData!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CTFontManagerCreateFontDescriptorsFromURL(CFURL!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CTFontManagerRegisterFontsForURL(CFURL!, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified CTFontManagerRegisterFontsForURLs(CFArray!, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified CTFontManagerRegisterGraphicsFont(CGFont!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified CTFontManagerUnregisterFontsForURL(CFURL!, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified CTFontManagerUnregisterFontsForURLs(CFArray!, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified CTFontManagerUnregisterGraphicsFont(CGFont!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified CTFrameDraw(CTFrame!, CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFrameGetFrameAttributes(CTFrame!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFrameGetLineOrigins(CTFrame!, CFRange, UnsafeMutablePointer<CGPoint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFrameGetLines(CTFrame!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFrameGetPath(CTFrame!) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFrameGetStringRange(CTFrame!) -> CFRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFrameGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFrameGetVisibleStringRange(CTFrame!) -> CFRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFramesetterCreateFrame(CTFramesetter!, CFRange, CGPath!, CFDictionary!) -> CTFrame!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFramesetterCreateWithAttributedString(CFAttributedString!) -> CTFramesetter!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFramesetterGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFramesetterGetTypesetter(CTFramesetter!) -> CTTypesetter!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTFramesetterSuggestFrameSizeWithConstraints(CTFramesetter!, CFRange, CFDictionary!, CGSize, UnsafeMutablePointer<CFRange>) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTGetCoreTextVersion() -> UInt32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTGlyphInfoCreateWithCharacterIdentifier(CGFontIndex, CTCharacterCollection, CFString!) -> CTGlyphInfo!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTGlyphInfoCreateWithGlyph(CGGlyph, CTFont!, CFString!) -> CTGlyphInfo!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTGlyphInfoCreateWithGlyphName(CFString!, CTFont!, CFString!) -> CTGlyphInfo!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTGlyphInfoGetCharacterCollection(CTGlyphInfo!) -> CTCharacterCollection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTGlyphInfoGetCharacterIdentifier(CTGlyphInfo!) -> CGFontIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTGlyphInfoGetGlyphName(CTGlyphInfo!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTGlyphInfoGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineCreateJustifiedLine(CTLine!, CGFloat, Double) -> CTLine!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineCreateTruncatedLine(CTLine!, Double, CTLineTruncationType, CTLine!) -> CTLine!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineCreateWithAttributedString(CFAttributedString!) -> CTLine!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineDraw(CTLine!, CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetBoundsWithOptions(CTLine!, CTLineBoundsOptions) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CTLineGetGlyphCount(CTLine!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetGlyphRuns(CTLine!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetImageBounds(CTLine!, CGContext!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetOffsetForStringIndex(CTLine!, CFIndex, UnsafeMutablePointer<CGFloat>) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetPenOffsetForFlush(CTLine!, CGFloat, Double) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetStringIndexForPosition(CTLine!, CGPoint) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetStringRange(CTLine!) -> CFRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetTrailingWhitespaceWidth(CTLine!) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTLineGetTypographicBounds(CTLine!, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTParagraphStyleCreate(UnsafePointer<CTParagraphStyleSetting>, UInt) -> CTParagraphStyle!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTParagraphStyleCreateCopy(CTParagraphStyle!) -> CTParagraphStyle!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTParagraphStyleGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTParagraphStyleGetValueForSpecifier(CTParagraphStyle!, CTParagraphStyleSpecifier, UInt, UnsafeMutablePointer<Void>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunDelegateCreate(UnsafePointer<CTRunDelegateCallbacks>, UnsafeMutablePointer<Void>) -> CTRunDelegate!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunDelegateGetRefCon(CTRunDelegate!) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunDelegateGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunDraw(CTRun!, CGContext!, CFRange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetAdvances(CTRun!, CFRange, UnsafeMutablePointer<CGSize>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetAdvancesPtr(CTRun!) -> UnsafePointer<CGSize>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetAttributes(CTRun!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetGlyphCount(CTRun!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetGlyphs(CTRun!, CFRange, UnsafeMutablePointer<CGGlyph>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetGlyphsPtr(CTRun!) -> UnsafePointer<CGGlyph>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetImageBounds(CTRun!, CGContext!, CFRange) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetPositions(CTRun!, CFRange, UnsafeMutablePointer<CGPoint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetPositionsPtr(CTRun!) -> UnsafePointer<CGPoint>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetStatus(CTRun!) -> CTRunStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetStringIndices(CTRun!, CFRange, UnsafeMutablePointer<CFIndex>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetStringIndicesPtr(CTRun!) -> UnsafePointer<CFIndex>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetStringRange(CTRun!) -> CFRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetTextMatrix(CTRun!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTRunGetTypographicBounds(CTRun!, CFRange, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTextTabCreate(CTTextAlignment, Double, CFDictionary!) -> CTTextTab!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTextTabGetAlignment(CTTextTab!) -> CTTextAlignment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTextTabGetLocation(CTTextTab!) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTextTabGetOptions(CTTextTab!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTextTabGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterCreateLine(CTTypesetter!, CFRange) -> CTLine!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterCreateLineWithOffset(CTTypesetter!, CFRange, Double) -> CTLine!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterCreateWithAttributedString(CFAttributedString!) -> CTTypesetter!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterCreateWithAttributedStringAndOptions(CFAttributedString!, CFDictionary!) -> CTTypesetter!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterSuggestClusterBreak(CTTypesetter!, CFIndex, Double) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterSuggestClusterBreakWithOffset(CTTypesetter!, CFIndex, Double, Double) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterSuggestLineBreak(CTTypesetter!, CFIndex, Double) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CTTypesetterSuggestLineBreakWithOffset(CTTypesetter!, CFIndex, Double, Double) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTBaselineClassAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineClassHanging

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineClassIdeographicCentered

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineClassIdeographicHigh

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineClassIdeographicLow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineClassMath

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineClassRoman

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineInfoAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineOriginalFont

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineReferenceFont

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTBaselineReferenceInfoAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTCharacterShapeAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontBaselineAdjustAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontCascadeListAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontCharacterSetAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontCollectionRemoveDuplicatesOption

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontCopyrightNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontDescriptionNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontDescriptorMatchingCurrentAssetSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDescriptorMatchingDescriptors

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDescriptorMatchingError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDescriptorMatchingPercentage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDescriptorMatchingResult

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDescriptorMatchingSourceDescriptor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDescriptorMatchingTotalAssetSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDescriptorMatchingTotalDownloadedSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDesignerNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontDesignerURLNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontDisplayNameAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontDownloadableAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCTFontDownloadedAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCTFontEnabledAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFamilyNameAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFamilyNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureSelectorDefaultKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureSelectorIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureSelectorNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureSelectorSettingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureSettingsAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureTypeExclusiveKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureTypeIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureTypeNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeatureTypeSelectorsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFeaturesAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFixedAdvanceAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFormatAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontFullNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontLanguagesAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontLicenseNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontLicenseURLNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontMacintoshEncodingsAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontManagerErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontManagerErrorFontURLsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontManagerRegisteredFontsChangedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCTFontManufacturerNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontMatrixAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontNameAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontOrientationAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontPostScriptCIDNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontPostScriptNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontPriorityAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontRegistrationScopeAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontSampleTextNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontSizeAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontSlantTrait

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontStyleNameAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontStyleNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontSubFamilyNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontSymbolicTrait

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontTrademarkNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontTraitsAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontURLAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontUniqueNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontVariationAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontVariationAxisDefaultValueKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontVariationAxisIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontVariationAxisMaximumValueKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontVariationAxisMinimumValueKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontVariationAxisNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontVendorURLNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontVersionNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontWeightTrait

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFontWidthTrait

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTForegroundColorAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTForegroundColorFromContextAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTFrameClippingPathsAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCTFramePathClippingPathAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCTFramePathFillRuleAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kCTFramePathWidthAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified kCTFrameProgressionAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTGlyphInfoAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTKernAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTLanguageAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCTLigatureAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTParagraphStyleAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTRunDelegateAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTStrokeColorAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTStrokeWidthAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTSuperscriptAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTTabColumnTerminatorsAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTTypesetterOptionForcedEmbeddingLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTUnderlineColorAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTUnderlineStyleAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCTVerticalFormsAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCTWritingDirectionAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

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
