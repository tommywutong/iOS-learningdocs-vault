---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreText.html
archived_at: '2026-07-18T02:56:47.159779Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreText Changes for Swift

### CoreText

Removed CTFontOptions.init(_: CFOptionFlags)Removed CTFontStylisticClass.init(_: UInt32)Removed CTFontSymbolicTraits.init(_: UInt32)Removed CTFontTableOptions.init(_: UInt32)Removed CTLineBoundsOptions.init(_: CFOptionFlags)Removed CTParagraphStyleSetting.init()Removed CTParagraphStyleSetting.init(spec: CTParagraphStyleSpecifier, valueSize: Int, value: UnsafePointer<Void>)Removed CTRunDelegateCallbacks.init()Removed CTRunDelegateCallbacks.init(version: CFIndex, dealloc: CTRunDelegateDeallocateCallback, getAscent: CTRunDelegateGetAscentCallback, getDescent: CTRunDelegateGetDescentCallback, getWidth: CTRunDelegateGetWidthCallback)Removed CTRunStatus.init(_: UInt32)Removed CTUnderlineStyle.init(_: Int32)Removed CTUnderlineStyleModifiers.init(_: Int32)Removed CTFontCollectionCopyOptionsRemoved kCTFontCollectionCopyDefaultOptionsRemoved kCTFontCollectionCopyStandardSortRemoved kCTFontCollectionCopyUniqueAdded [CTCharacterCollection.kCTAdobeCNS1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402036-kctadobecns1charactercollection)Added [CTCharacterCollection.kCTAdobeGB1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402024-kctadobegb1charactercollection)Added [CTCharacterCollection.kCTAdobeJapan1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctadobejapan1charactercollection)Added [CTCharacterCollection.kCTAdobeJapan2CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402048-kctadobejapan2charactercollectio)Added [CTCharacterCollection.kCTAdobeKorea1CharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402058-kctadobekorea1charactercollectio)Added [CTCharacterCollection.kCTIdentityMappingCharacterCollection](https://developer.apple.com/documentation/coretext/ctcharactercollection/1402054-kctidentitymappingcharactercolle)Added [CTFontOrientation.kCTFontDefaultOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfontdefaultorientation)Added [CTFontOrientation.kCTFontHorizontalOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/1509711-kctfonthorizontalorientation)Added [CTFontOrientation.kCTFontVerticalOrientation](https://developer.apple.com/documentation/coretext/ctfontorientation/kctfontverticalorientation)Added [CTFontUIFontType.kCTFontAlertHeaderFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510101-kctfontalertheaderfonttype)Added [CTFontUIFontType.kCTFontApplicationFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontapplicationfonttype)Added [CTFontUIFontType.kCTFontControlContentFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508950-kctfontcontrolcontentfonttype)Added [CTFontUIFontType.kCTFontEmphasizedSystemDetailFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508682-kctfontemphasizedsystemdetailfon)Added [CTFontUIFontType.kCTFontEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontemphasizedsystemfonttype)Added [CTFontUIFontType.kCTFontLabelFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontlabelfonttype)Added [CTFontUIFontType.kCTFontMenuItemCmdKeyFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1510054-kctfontmenuitemcmdkeyfonttype)Added [CTFontUIFontType.kCTFontMenuItemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontmenuitemfonttype)Added [CTFontUIFontType.kCTFontMenuItemMarkFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontmenuitemmarkfonttype)Added [CTFontUIFontType.kCTFontMenuTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontmenutitlefonttype)Added [CTFontUIFontType.kCTFontMessageFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontmessagefonttype)Added [CTFontUIFontType.kCTFontMiniEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontminiemphasizedsystemfonttype)Added [CTFontUIFontType.kCTFontMiniSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontminisystemfonttype)Added [CTFontUIFontType.kCTFontNoFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontnofonttype)Added [CTFontUIFontType.kCTFontPaletteFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontpalettefonttype)Added [CTFontUIFontType.kCTFontPushButtonFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontpushbuttonfonttype)Added [CTFontUIFontType.kCTFontSmallEmphasizedSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509037-kctfontsmallemphasizedsystemfont)Added [CTFontUIFontType.kCTFontSmallSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508710-kctfontsmallsystemfonttype)Added [CTFontUIFontType.kCTFontSmallToolbarFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontsmalltoolbarfonttype)Added [CTFontUIFontType.kCTFontSystemDetailFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontsystemdetailfonttype)Added [CTFontUIFontType.kCTFontSystemFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509431-kctfontsystemfonttype)Added [CTFontUIFontType.kCTFontToolbarFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfonttoolbarfonttype)Added [CTFontUIFontType.kCTFontToolTipFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1509396-kctfonttooltipfonttype)Added [CTFontUIFontType.kCTFontUserFixedPitchFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuserfixedpitchfonttype)Added [CTFontUIFontType.kCTFontUserFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuserfonttype)Added [CTFontUIFontType.kCTFontUtilityWindowTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/1508716-kctfontutilitywindowtitlefonttyp)Added [CTFontUIFontType.kCTFontViewsFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontviewsfonttype)Added [CTFontUIFontType.kCTFontWindowTitleFontType](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontwindowtitlefonttype)Added [CTTextAlignment.kCTCenterTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/1496175-kctcentertextalignment)Added [CTTextAlignment.kCTJustifiedTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctjustifiedtextalignment)Added [CTTextAlignment.kCTLeftTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/1496101-kctlefttextalignment)Added [CTTextAlignment.kCTNaturalTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/1496130-kctnaturaltextalignment)Added [CTTextAlignment.kCTRightTextAlignment](https://developer.apple.com/documentation/coretext/cttextalignment/kctrighttextalignment)Added [CTLineEnumerateCaretOffsets(_: CTLine, _: (Double, CFIndex, Bool, UnsafeMutablePointer<Bool>) -> Void)](https://developer.apple.com/documentation/coretext/1508685-ctlineenumeratecaretoffsets)Added [kCTVersionNumber10_11](https://developer.apple.com/documentation/coretext/kctversionnumber10_11)Modified [CTCharacterCollection [enum]](https://developer.apple.com/documentation/coretext/ctcharactercollection)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum CTCharacterCollection : UInt16 {     case CharacterCollectionIdentityMapping     case CharacterCollectionAdobeCNS1     case CharacterCollectionAdobeGB1     case CharacterCollectionAdobeJapan1     case CharacterCollectionAdobeJapan2     case CharacterCollectionAdobeKorea1 } ``` | -- |
| To | ``` enum CTCharacterCollection : UInt16 {     case IdentityMapping     case AdobeCNS1     case AdobeGB1     case AdobeJapan1     case AdobeJapan2     case AdobeKorea1     static var kCTIdentityMappingCharacterCollection: CTCharacterCollection { get }     static var kCTAdobeCNS1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeGB1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeJapan1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeJapan2CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeKorea1CharacterCollection: CTCharacterCollection { get } } ``` | UInt16 |

Modified [CTCharacterCollection.AdobeCNS1](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctcharactercollectionadobecns1)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CharacterCollectionAdobeCNS1 ``` | iOS 8.0 |
| To | ``` case AdobeCNS1 ``` | iOS 6.0 |

Modified [CTCharacterCollection.AdobeGB1](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctcharactercollectionadobegb1)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CharacterCollectionAdobeGB1 ``` | iOS 8.0 |
| To | ``` case AdobeGB1 ``` | iOS 6.0 |

Modified [CTCharacterCollection.AdobeJapan1](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobejapan1)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CharacterCollectionAdobeJapan1 ``` | iOS 8.0 |
| To | ``` case AdobeJapan1 ``` | iOS 6.0 |

Modified [CTCharacterCollection.AdobeJapan2](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobejapan2)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CharacterCollectionAdobeJapan2 ``` | iOS 8.0 |
| To | ``` case AdobeJapan2 ``` | iOS 6.0 |

Modified [CTCharacterCollection.AdobeKorea1](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobekorea1)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CharacterCollectionAdobeKorea1 ``` | iOS 8.0 |
| To | ``` case AdobeKorea1 ``` | iOS 6.0 |

Modified [CTCharacterCollection.IdentityMapping](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctcharactercollectionidentitymapping)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CharacterCollectionIdentityMapping ``` | iOS 8.0 |
| To | ``` case IdentityMapping ``` | iOS 6.0 |

Modified [CTFontDescriptorMatchingState [enum]](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CTFontFormat [enum]](https://developer.apple.com/documentation/coretext/ctfontformat)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CTFontManagerAutoActivationSetting [enum]](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CTFontManagerScope [enum]](https://developer.apple.com/documentation/coretext/ctfontmanagerscope)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CTFontOptions [struct]](https://developer.apple.com/documentation/coretext/ctfontoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Default: CTFontOptions { get }     static var PreventAutoActivation: CTFontOptions { get }     static var PreferSystemFont: CTFontOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CTFontOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Default: CTFontOptions { get }     static var PreventAutoActivation: CTFontOptions { get }     static var PreferSystemFont: CTFontOptions { get } } ``` | OptionSetType |

Modified [CTFontOrientation [enum]](https://developer.apple.com/documentation/coretext/ctfontorientation)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum CTFontOrientation : UInt32 {     case OrientationDefault     case OrientationHorizontal     case OrientationVertical } ``` | -- |
| To | ``` enum CTFontOrientation : UInt32 {     case Default     case Horizontal     case Vertical     static var kCTFontDefaultOrientation: CTFontOrientation { get }     static var kCTFontHorizontalOrientation: CTFontOrientation { get }     static var kCTFontVerticalOrientation: CTFontOrientation { get } } ``` | UInt32 |

Modified [CTFontOrientation.Default](https://developer.apple.com/documentation/coretext/ctfontorientation/default)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case OrientationDefault ``` | iOS 8.0 |
| To | ``` case Default ``` | iOS 6.0 |

Modified [CTFontOrientation.Horizontal](https://developer.apple.com/documentation/coretext/ctfontorientation/horizontal)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case OrientationHorizontal ``` | iOS 8.0 |
| To | ``` case Horizontal ``` | iOS 6.0 |

Modified [CTFontOrientation.Vertical](https://developer.apple.com/documentation/coretext/ctfontorientation/vertical)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case OrientationVertical ``` | iOS 8.0 |
| To | ``` case Vertical ``` | iOS 6.0 |

Modified [CTFontStylisticClass [struct]](https://developer.apple.com/documentation/coretext/ctfontstylisticclass)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontStylisticClass : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var ClassUnknown: CTFontStylisticClass { get }     static var ClassOldStyleSerifs: CTFontStylisticClass { get }     static var ClassTransitionalSerifs: CTFontStylisticClass { get }     static var ClassModernSerifs: CTFontStylisticClass { get }     static var ClassClarendonSerifs: CTFontStylisticClass { get }     static var ClassSlabSerifs: CTFontStylisticClass { get }     static var ClassFreeformSerifs: CTFontStylisticClass { get }     static var ClassSansSerif: CTFontStylisticClass { get }     static var ClassOrnamentals: CTFontStylisticClass { get }     static var ClassScripts: CTFontStylisticClass { get }     static var ClassSymbolic: CTFontStylisticClass { get }     static var UnknownClass: CTFontStylisticClass { get }     static var OldStyleSerifsClass: CTFontStylisticClass { get }     static var TransitionalSerifsClass: CTFontStylisticClass { get }     static var ModernSerifsClass: CTFontStylisticClass { get }     static var ClarendonSerifsClass: CTFontStylisticClass { get }     static var SlabSerifsClass: CTFontStylisticClass { get }     static var FreeformSerifsClass: CTFontStylisticClass { get }     static var SansSerifClass: CTFontStylisticClass { get }     static var OrnamentalsClass: CTFontStylisticClass { get }     static var ScriptsClass: CTFontStylisticClass { get }     static var SymbolicClass: CTFontStylisticClass { get } } ``` | RawOptionSetType |
| To | ``` struct CTFontStylisticClass : OptionSetType {     init(rawValue rawValue: UInt32)     static var ClassUnknown: CTFontStylisticClass { get }     static var ClassOldStyleSerifs: CTFontStylisticClass { get }     static var ClassTransitionalSerifs: CTFontStylisticClass { get }     static var ClassModernSerifs: CTFontStylisticClass { get }     static var ClassClarendonSerifs: CTFontStylisticClass { get }     static var ClassSlabSerifs: CTFontStylisticClass { get }     static var ClassFreeformSerifs: CTFontStylisticClass { get }     static var ClassSansSerif: CTFontStylisticClass { get }     static var ClassOrnamentals: CTFontStylisticClass { get }     static var ClassScripts: CTFontStylisticClass { get }     static var ClassSymbolic: CTFontStylisticClass { get }     static var UnknownClass: CTFontStylisticClass { get }     static var OldStyleSerifsClass: CTFontStylisticClass { get }     static var TransitionalSerifsClass: CTFontStylisticClass { get }     static var ModernSerifsClass: CTFontStylisticClass { get }     static var ClarendonSerifsClass: CTFontStylisticClass { get }     static var SlabSerifsClass: CTFontStylisticClass { get }     static var FreeformSerifsClass: CTFontStylisticClass { get }     static var SansSerifClass: CTFontStylisticClass { get }     static var OrnamentalsClass: CTFontStylisticClass { get }     static var ScriptsClass: CTFontStylisticClass { get }     static var SymbolicClass: CTFontStylisticClass { get } } ``` | OptionSetType |

Modified [CTFontSymbolicTraits [struct]](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontSymbolicTraits : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var TraitItalic: CTFontSymbolicTraits { get }     static var TraitBold: CTFontSymbolicTraits { get }     static var TraitExpanded: CTFontSymbolicTraits { get }     static var TraitCondensed: CTFontSymbolicTraits { get }     static var TraitMonoSpace: CTFontSymbolicTraits { get }     static var TraitVertical: CTFontSymbolicTraits { get }     static var TraitUIOptimized: CTFontSymbolicTraits { get }     static var TraitColorGlyphs: CTFontSymbolicTraits { get }     static var TraitComposite: CTFontSymbolicTraits { get }     static var TraitClassMask: CTFontSymbolicTraits { get }     static var ItalicTrait: CTFontSymbolicTraits { get }     static var BoldTrait: CTFontSymbolicTraits { get }     static var ExpandedTrait: CTFontSymbolicTraits { get }     static var CondensedTrait: CTFontSymbolicTraits { get }     static var MonoSpaceTrait: CTFontSymbolicTraits { get }     static var VerticalTrait: CTFontSymbolicTraits { get }     static var UIOptimizedTrait: CTFontSymbolicTraits { get }     static var ColorGlyphsTrait: CTFontSymbolicTraits { get }     static var CompositeTrait: CTFontSymbolicTraits { get }     static var ClassMaskTrait: CTFontSymbolicTraits { get } } ``` | RawOptionSetType |
| To | ``` struct CTFontSymbolicTraits : OptionSetType {     init(rawValue rawValue: UInt32)     static var TraitItalic: CTFontSymbolicTraits { get }     static var TraitBold: CTFontSymbolicTraits { get }     static var TraitExpanded: CTFontSymbolicTraits { get }     static var TraitCondensed: CTFontSymbolicTraits { get }     static var TraitMonoSpace: CTFontSymbolicTraits { get }     static var TraitVertical: CTFontSymbolicTraits { get }     static var TraitUIOptimized: CTFontSymbolicTraits { get }     static var TraitColorGlyphs: CTFontSymbolicTraits { get }     static var TraitComposite: CTFontSymbolicTraits { get }     static var TraitClassMask: CTFontSymbolicTraits { get }     static var ItalicTrait: CTFontSymbolicTraits { get }     static var BoldTrait: CTFontSymbolicTraits { get }     static var ExpandedTrait: CTFontSymbolicTraits { get }     static var CondensedTrait: CTFontSymbolicTraits { get }     static var MonoSpaceTrait: CTFontSymbolicTraits { get }     static var VerticalTrait: CTFontSymbolicTraits { get }     static var UIOptimizedTrait: CTFontSymbolicTraits { get }     static var ColorGlyphsTrait: CTFontSymbolicTraits { get }     static var CompositeTrait: CTFontSymbolicTraits { get }     static var ClassMaskTrait: CTFontSymbolicTraits { get } } ``` | OptionSetType |

Modified [CTFontTableOptions [struct]](https://developer.apple.com/documentation/coretext/ctfonttableoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontTableOptions : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var NoOptions: CTFontTableOptions { get }     static var ExcludeSynthetic: CTFontTableOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CTFontTableOptions : OptionSetType {     init(rawValue rawValue: UInt32)     static var NoOptions: CTFontTableOptions { get }     static var ExcludeSynthetic: CTFontTableOptions { get } } ``` | OptionSetType |

Modified [CTFontTableOptions.NoOptions](https://developer.apple.com/documentation/coretext/ctfonttableoptions/kctfonttableoptionnooptions)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [CTFontUIFontType [enum]](https://developer.apple.com/documentation/coretext/ctfontuifonttype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum CTFontUIFontType : UInt32 {     case UIFontNone     case UIFontUser     case UIFontUserFixedPitch     case UIFontSystem     case UIFontEmphasizedSystem     case UIFontSmallSystem     case UIFontSmallEmphasizedSystem     case UIFontMiniSystem     case UIFontMiniEmphasizedSystem     case UIFontViews     case UIFontApplication     case UIFontLabel     case UIFontMenuTitle     case UIFontMenuItem     case UIFontMenuItemMark     case UIFontMenuItemCmdKey     case UIFontWindowTitle     case UIFontPushButton     case UIFontUtilityWindowTitle     case UIFontAlertHeader     case UIFontSystemDetail     case UIFontEmphasizedSystemDetail     case UIFontToolbar     case UIFontSmallToolbar     case UIFontMessage     case UIFontPalette     case UIFontToolTip     case UIFontControlContent } ``` | -- |
| To | ``` enum CTFontUIFontType : UInt32 {     case None     case User     case UserFixedPitch     case System     case EmphasizedSystem     case SmallSystem     case SmallEmphasizedSystem     case MiniSystem     case MiniEmphasizedSystem     case Views     case Application     case Label     case MenuTitle     case MenuItem     case MenuItemMark     case MenuItemCmdKey     case WindowTitle     case PushButton     case UtilityWindowTitle     case AlertHeader     case SystemDetail     case EmphasizedSystemDetail     case Toolbar     case SmallToolbar     case Message     case Palette     case ToolTip     case ControlContent     static var kCTFontNoFontType: CTFontUIFontType { get }     static var kCTFontUserFontType: CTFontUIFontType { get }     static var kCTFontUserFixedPitchFontType: CTFontUIFontType { get }     static var kCTFontSystemFontType: CTFontUIFontType { get }     static var kCTFontEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontSmallSystemFontType: CTFontUIFontType { get }     static var kCTFontSmallEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontMiniSystemFontType: CTFontUIFontType { get }     static var kCTFontMiniEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontViewsFontType: CTFontUIFontType { get }     static var kCTFontApplicationFontType: CTFontUIFontType { get }     static var kCTFontLabelFontType: CTFontUIFontType { get }     static var kCTFontMenuTitleFontType: CTFontUIFontType { get }     static var kCTFontMenuItemFontType: CTFontUIFontType { get }     static var kCTFontMenuItemMarkFontType: CTFontUIFontType { get }     static var kCTFontMenuItemCmdKeyFontType: CTFontUIFontType { get }     static var kCTFontWindowTitleFontType: CTFontUIFontType { get }     static var kCTFontPushButtonFontType: CTFontUIFontType { get }     static var kCTFontUtilityWindowTitleFontType: CTFontUIFontType { get }     static var kCTFontAlertHeaderFontType: CTFontUIFontType { get }     static var kCTFontSystemDetailFontType: CTFontUIFontType { get }     static var kCTFontEmphasizedSystemDetailFontType: CTFontUIFontType { get }     static var kCTFontToolbarFontType: CTFontUIFontType { get }     static var kCTFontSmallToolbarFontType: CTFontUIFontType { get }     static var kCTFontMessageFontType: CTFontUIFontType { get }     static var kCTFontPaletteFontType: CTFontUIFontType { get }     static var kCTFontToolTipFontType: CTFontUIFontType { get }     static var kCTFontControlContentFontType: CTFontUIFontType { get } } ``` | UInt32 |

Modified [CTFontUIFontType.AlertHeader](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontalertheader)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontAlertHeader ``` | iOS 8.0 |
| To | ``` case AlertHeader ``` | iOS 6.0 |

Modified [CTFontUIFontType.Application](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontapplication)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontApplication ``` | iOS 8.0 |
| To | ``` case Application ``` | iOS 6.0 |

Modified [CTFontUIFontType.ControlContent](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontcontrolcontent)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontControlContent ``` | iOS 8.0 |
| To | ``` case ControlContent ``` | iOS 6.0 |

Modified [CTFontUIFontType.EmphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/emphasizedsystem)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontEmphasizedSystem ``` | iOS 8.0 |
| To | ``` case EmphasizedSystem ``` | iOS 6.0 |

Modified [CTFontUIFontType.EmphasizedSystemDetail](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontemphasizedsystemdetail)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontEmphasizedSystemDetail ``` | iOS 8.0 |
| To | ``` case EmphasizedSystemDetail ``` | iOS 6.0 |

Modified [CTFontUIFontType.Label](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontlabel)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontLabel ``` | iOS 8.0 |
| To | ``` case Label ``` | iOS 6.0 |

Modified [CTFontUIFontType.MenuItem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/menuitem)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontMenuItem ``` | iOS 8.0 |
| To | ``` case MenuItem ``` | iOS 6.0 |

Modified [CTFontUIFontType.MenuItemCmdKey](https://developer.apple.com/documentation/coretext/ctfontuifonttype/menuitemcmdkey)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontMenuItemCmdKey ``` | iOS 8.0 |
| To | ``` case MenuItemCmdKey ``` | iOS 6.0 |

Modified [CTFontUIFontType.MenuItemMark](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontmenuitemmark)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontMenuItemMark ``` | iOS 8.0 |
| To | ``` case MenuItemMark ``` | iOS 6.0 |

Modified [CTFontUIFontType.MenuTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontmenutitle)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontMenuTitle ``` | iOS 8.0 |
| To | ``` case MenuTitle ``` | iOS 6.0 |

Modified [CTFontUIFontType.Message](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontmessage)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontMessage ``` | iOS 8.0 |
| To | ``` case Message ``` | iOS 6.0 |

Modified [CTFontUIFontType.MiniEmphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontminiemphasizedsystem)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontMiniEmphasizedSystem ``` | iOS 8.0 |
| To | ``` case MiniEmphasizedSystem ``` | iOS 6.0 |

Modified [CTFontUIFontType.MiniSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/minisystem)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontMiniSystem ``` | iOS 8.0 |
| To | ``` case MiniSystem ``` | iOS 6.0 |

Modified [CTFontUIFontType.None](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontnone)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontNone ``` | iOS 8.0 |
| To | ``` case None ``` | iOS 6.0 |

Modified [CTFontUIFontType.Palette](https://developer.apple.com/documentation/coretext/ctfontuifonttype/palette)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontPalette ``` | iOS 8.0 |
| To | ``` case Palette ``` | iOS 6.0 |

Modified [CTFontUIFontType.PushButton](https://developer.apple.com/documentation/coretext/ctfontuifonttype/pushbutton)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontPushButton ``` | iOS 8.0 |
| To | ``` case PushButton ``` | iOS 6.0 |

Modified [CTFontUIFontType.SmallEmphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/smallemphasizedsystem)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontSmallEmphasizedSystem ``` | iOS 8.0 |
| To | ``` case SmallEmphasizedSystem ``` | iOS 6.0 |

Modified [CTFontUIFontType.SmallSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/smallsystem)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontSmallSystem ``` | iOS 8.0 |
| To | ``` case SmallSystem ``` | iOS 6.0 |

Modified [CTFontUIFontType.SmallToolbar](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsmalltoolbar)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontSmallToolbar ``` | iOS 8.0 |
| To | ``` case SmallToolbar ``` | iOS 6.0 |

Modified [CTFontUIFontType.System](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsystem)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontSystem ``` | iOS 8.0 |
| To | ``` case System ``` | iOS 6.0 |

Modified [CTFontUIFontType.SystemDetail](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsystemdetail)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontSystemDetail ``` | iOS 8.0 |
| To | ``` case SystemDetail ``` | iOS 6.0 |

Modified [CTFontUIFontType.Toolbar](https://developer.apple.com/documentation/coretext/ctfontuifonttype/toolbar)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontToolbar ``` | iOS 8.0 |
| To | ``` case Toolbar ``` | iOS 6.0 |

Modified [CTFontUIFontType.ToolTip](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifonttooltip)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontToolTip ``` | iOS 8.0 |
| To | ``` case ToolTip ``` | iOS 6.0 |

Modified [CTFontUIFontType.User](https://developer.apple.com/documentation/coretext/ctfontuifonttype/user)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontUser ``` | iOS 8.0 |
| To | ``` case User ``` | iOS 6.0 |

Modified [CTFontUIFontType.UserFixedPitch](https://developer.apple.com/documentation/coretext/ctfontuifonttype/userfixedpitch)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontUserFixedPitch ``` | iOS 8.0 |
| To | ``` case UserFixedPitch ``` | iOS 6.0 |

Modified [CTFontUIFontType.UtilityWindowTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/utilitywindowtitle)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontUtilityWindowTitle ``` | iOS 8.0 |
| To | ``` case UtilityWindowTitle ``` | iOS 6.0 |

Modified [CTFontUIFontType.Views](https://developer.apple.com/documentation/coretext/ctfontuifonttype/views)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontViews ``` | iOS 8.0 |
| To | ``` case Views ``` | iOS 6.0 |

Modified [CTFontUIFontType.WindowTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/windowtitle)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UIFontWindowTitle ``` | iOS 8.0 |
| To | ``` case WindowTitle ``` | iOS 6.0 |

Modified [CTFramePathFillRule [enum]](https://developer.apple.com/documentation/coretext/ctframepathfillrule)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CTFrameProgression [enum]](https://developer.apple.com/documentation/coretext/ctframeprogression)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CTLineBoundsOptions [struct]](https://developer.apple.com/documentation/coretext/ctlineboundsoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTLineBoundsOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var ExcludeTypographicLeading: CTLineBoundsOptions { get }     static var ExcludeTypographicShifts: CTLineBoundsOptions { get }     static var UseHangingPunctuation: CTLineBoundsOptions { get }     static var UseGlyphPathBounds: CTLineBoundsOptions { get }     static var UseOpticalBounds: CTLineBoundsOptions { get }     static var IncludeLanguageExtents: CTLineBoundsOptions { get } } ``` | RawOptionSetType |
| To | ``` struct CTLineBoundsOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var ExcludeTypographicLeading: CTLineBoundsOptions { get }     static var ExcludeTypographicShifts: CTLineBoundsOptions { get }     static var UseHangingPunctuation: CTLineBoundsOptions { get }     static var UseGlyphPathBounds: CTLineBoundsOptions { get }     static var UseOpticalBounds: CTLineBoundsOptions { get }     static var IncludeLanguageExtents: CTLineBoundsOptions { get } } ``` | OptionSetType |

Modified [CTLineBreakMode [enum]](https://developer.apple.com/documentation/coretext/ctlinebreakmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt8 |

Modified [CTLineTruncationType [enum]](https://developer.apple.com/documentation/coretext/ctlinetruncationtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CTParagraphStyleSetting [struct]](https://developer.apple.com/documentation/coretext/ctparagraphstylesetting)

|  | Declaration |
| --- | --- |
| From | ``` struct CTParagraphStyleSetting {     var spec: CTParagraphStyleSpecifier     var valueSize: Int     var value: UnsafePointer<Void>     init()     init(spec spec: CTParagraphStyleSpecifier, valueSize valueSize: Int, value value: UnsafePointer<Void>) } ``` |
| To | ``` struct CTParagraphStyleSetting {     var spec: CTParagraphStyleSpecifier     var valueSize: Int     var value: UnsafePointer<Void> } ``` |

Modified [CTParagraphStyleSpecifier [enum]](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt32 |

Modified [CTRubyAlignment [enum]](https://developer.apple.com/documentation/coretext/ctrubyalignment)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt8 |

Modified [CTRubyOverhang [enum]](https://developer.apple.com/documentation/coretext/ctrubyoverhang)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt8 |

Modified [CTRubyPosition [enum]](https://developer.apple.com/documentation/coretext/ctrubyposition)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt8 |

Modified [CTRunDelegateCallbacks [struct]](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CTRunDelegateCallbacks {     var version: CFIndex     var dealloc: CTRunDelegateDeallocateCallback     var getAscent: CTRunDelegateGetAscentCallback     var getDescent: CTRunDelegateGetDescentCallback     var getWidth: CTRunDelegateGetWidthCallback     init()     init(version version: CFIndex, dealloc dealloc: CTRunDelegateDeallocateCallback, getAscent getAscent: CTRunDelegateGetAscentCallback, getDescent getDescent: CTRunDelegateGetDescentCallback, getWidth getWidth: CTRunDelegateGetWidthCallback) } ``` |
| To | ``` struct CTRunDelegateCallbacks {     var version: CFIndex     var dealloc: CTRunDelegateDeallocateCallback     var getAscent: CTRunDelegateGetAscentCallback     var getDescent: CTRunDelegateGetDescentCallback     var getWidth: CTRunDelegateGetWidthCallback } ``` |

Modified [CTRunStatus [struct]](https://developer.apple.com/documentation/coretext/ctrunstatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTRunStatus : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var NoStatus: CTRunStatus { get }     static var RightToLeft: CTRunStatus { get }     static var NonMonotonic: CTRunStatus { get }     static var HasNonIdentityMatrix: CTRunStatus { get } } ``` | RawOptionSetType |
| To | ``` struct CTRunStatus : OptionSetType {     init(rawValue rawValue: UInt32)     static var NoStatus: CTRunStatus { get }     static var RightToLeft: CTRunStatus { get }     static var NonMonotonic: CTRunStatus { get }     static var HasNonIdentityMatrix: CTRunStatus { get } } ``` | OptionSetType |

Modified [CTTextAlignment [enum]](https://developer.apple.com/documentation/coretext/cttextalignment)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum CTTextAlignment : UInt8 {     case TextAlignmentLeft     case TextAlignmentRight     case TextAlignmentCenter     case TextAlignmentJustified     case TextAlignmentNatural } ``` | -- |
| To | ``` enum CTTextAlignment : UInt8 {     case Left     case Right     case Center     case Justified     case Natural     static var kCTLeftTextAlignment: CTTextAlignment { get }     static var kCTRightTextAlignment: CTTextAlignment { get }     static var kCTCenterTextAlignment: CTTextAlignment { get }     static var kCTJustifiedTextAlignment: CTTextAlignment { get }     static var kCTNaturalTextAlignment: CTTextAlignment { get } } ``` | UInt8 |

Modified [CTTextAlignment.Center](https://developer.apple.com/documentation/coretext/cttextalignment/center)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TextAlignmentCenter ``` | iOS 8.0 |
| To | ``` case Center ``` | iOS 6.0 |

Modified [CTTextAlignment.Justified](https://developer.apple.com/documentation/coretext/cttextalignment/justified)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TextAlignmentJustified ``` | iOS 8.0 |
| To | ``` case Justified ``` | iOS 6.0 |

Modified [CTTextAlignment.Left](https://developer.apple.com/documentation/coretext/cttextalignment/kcttextalignmentleft)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TextAlignmentLeft ``` | iOS 8.0 |
| To | ``` case Left ``` | iOS 6.0 |

Modified [CTTextAlignment.Natural](https://developer.apple.com/documentation/coretext/cttextalignment/kcttextalignmentnatural)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TextAlignmentNatural ``` | iOS 8.0 |
| To | ``` case Natural ``` | iOS 6.0 |

Modified [CTTextAlignment.Right](https://developer.apple.com/documentation/coretext/cttextalignment/right)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TextAlignmentRight ``` | iOS 8.0 |
| To | ``` case Right ``` | iOS 6.0 |

Modified [CTUnderlineStyle [struct]](https://developer.apple.com/documentation/coretext/ctunderlinestyle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTUnderlineStyle : RawOptionSetType {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     static var None: CTUnderlineStyle { get }     static var Single: CTUnderlineStyle { get }     static var Thick: CTUnderlineStyle { get }     static var Double: CTUnderlineStyle { get } } ``` | RawOptionSetType |
| To | ``` struct CTUnderlineStyle : OptionSetType {     init(rawValue rawValue: Int32)     static var None: CTUnderlineStyle { get }     static var Single: CTUnderlineStyle { get }     static var Thick: CTUnderlineStyle { get }     static var Double: CTUnderlineStyle { get } } ``` | OptionSetType |

Modified [CTUnderlineStyleModifiers [struct]](https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTUnderlineStyleModifiers : RawOptionSetType {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     static var PatternSolid: CTUnderlineStyleModifiers { get }     static var PatternDot: CTUnderlineStyleModifiers { get }     static var PatternDash: CTUnderlineStyleModifiers { get }     static var PatternDashDot: CTUnderlineStyleModifiers { get }     static var PatternDashDotDot: CTUnderlineStyleModifiers { get } } ``` | RawOptionSetType |
| To | ``` struct CTUnderlineStyleModifiers : OptionSetType {     init(rawValue rawValue: Int32)     static var PatternSolid: CTUnderlineStyleModifiers { get }     static var PatternDot: CTUnderlineStyleModifiers { get }     static var PatternDash: CTUnderlineStyleModifiers { get }     static var PatternDashDot: CTUnderlineStyleModifiers { get }     static var PatternDashDotDot: CTUnderlineStyleModifiers { get } } ``` | OptionSetType |

Modified [CTWritingDirection [enum]](https://developer.apple.com/documentation/coretext/ctwritingdirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int8 |

Modified [CTFontCollectionCreateCopyWithFontDescriptors(_: CTFontCollection, _: CFArray?, _: CFDictionary?) -> CTFontCollection](https://developer.apple.com/documentation/coretext/1510692-ctfontcollectioncreatecopywithfo)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCollectionCreateCopyWithFontDescriptors(_ original: CTFontCollection!, _ queryDescriptors: CFArray!, _ options: CFDictionary!) -> CTFontCollection! ``` |
| To | ``` func CTFontCollectionCreateCopyWithFontDescriptors(_ original: CTFontCollection, _ queryDescriptors: CFArray?, _ options: CFDictionary?) -> CTFontCollection ``` |

Modified [CTFontCollectionCreateFromAvailableFonts(_: CFDictionary?) -> CTFontCollection](https://developer.apple.com/documentation/coretext/1509907-ctfontcollectioncreatefromavaila)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCollectionCreateFromAvailableFonts(_ options: CFDictionary!) -> CTFontCollection! ``` |
| To | ``` func CTFontCollectionCreateFromAvailableFonts(_ options: CFDictionary?) -> CTFontCollection ``` |

Modified [CTFontCollectionCreateMatchingFontDescriptors(_: CTFontCollection) -> CFArray?](https://developer.apple.com/documentation/coretext/1511091-ctfontcollectioncreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCollectionCreateMatchingFontDescriptors(_ collection: CTFontCollection!) -> CFArray! ``` |
| To | ``` func CTFontCollectionCreateMatchingFontDescriptors(_ collection: CTFontCollection) -> CFArray? ``` |

Modified [CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_: CTFontCollection, _: CTFontCollectionSortDescriptorsCallback?, _: UnsafeMutablePointer<Void>) -> CFArray?](https://developer.apple.com/documentation/coretext/1510434-ctfontcollectioncreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_ collection: CTFontCollection!, _ sortCallback: CTFontCollectionSortDescriptorsCallback, _ refCon: UnsafeMutablePointer<Void>) -> CFArray! ``` |
| To | ``` func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_ collection: CTFontCollection, _ sortCallback: CTFontCollectionSortDescriptorsCallback?, _ refCon: UnsafeMutablePointer<Void>) -> CFArray? ``` |

Modified [CTFontCollectionCreateWithFontDescriptors(_: CFArray?, _: CFDictionary?) -> CTFontCollection](https://developer.apple.com/documentation/coretext/1509202-ctfontcollectioncreatewithfontde)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCollectionCreateWithFontDescriptors(_ queryDescriptors: CFArray!, _ options: CFDictionary!) -> CTFontCollection! ``` |
| To | ``` func CTFontCollectionCreateWithFontDescriptors(_ queryDescriptors: CFArray?, _ options: CFDictionary?) -> CTFontCollection ``` |

Modified [CTFontCollectionSortDescriptorsCallback](https://developer.apple.com/documentation/coretext/ctfontcollectionsortdescriptorscallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTFontCollectionSortDescriptorsCallback = CFunctionPointer<((CTFontDescriptor!, CTFontDescriptor!, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |
| To | ``` typealias CTFontCollectionSortDescriptorsCallback = (CTFontDescriptor, CTFontDescriptor, UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |

Modified [CTFontCopyAttribute(_: CTFont, _: CFString) -> AnyObject?](https://developer.apple.com/documentation/coretext/1508984-ctfontcopyattribute)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyAttribute(_ font: CTFont!, _ attribute: CFString!) -> AnyObject! ``` |
| To | ``` func CTFontCopyAttribute(_ font: CTFont, _ attribute: CFString) -> AnyObject? ``` |

Modified [CTFontCopyAvailableTables(_: CTFont, _: CTFontTableOptions) -> CFArray?](https://developer.apple.com/documentation/coretext/1510774-ctfontcopyavailabletables)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyAvailableTables(_ font: CTFont!, _ options: CTFontTableOptions) -> CFArray! ``` |
| To | ``` func CTFontCopyAvailableTables(_ font: CTFont, _ options: CTFontTableOptions) -> CFArray? ``` |

Modified [CTFontCopyCharacterSet(_: CTFont) -> CFCharacterSet](https://developer.apple.com/documentation/coretext/1511049-ctfontcopycharacterset)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyCharacterSet(_ font: CTFont!) -> CFCharacterSet! ``` |
| To | ``` func CTFontCopyCharacterSet(_ font: CTFont) -> CFCharacterSet ``` |

Modified [CTFontCopyDefaultCascadeListForLanguages(_: CTFont, _: CFArray?) -> CFArray?](https://developer.apple.com/documentation/coretext/1509992-ctfontcopydefaultcascadelistforl)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyDefaultCascadeListForLanguages(_ font: CTFont!, _ languagePrefList: CFArray!) -> CFArray! ``` |
| To | ``` func CTFontCopyDefaultCascadeListForLanguages(_ font: CTFont, _ languagePrefList: CFArray?) -> CFArray? ``` |

Modified [CTFontCopyDisplayName(_: CTFont) -> CFString](https://developer.apple.com/documentation/coretext/1509316-ctfontcopydisplayname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyDisplayName(_ font: CTFont!) -> CFString! ``` |
| To | ``` func CTFontCopyDisplayName(_ font: CTFont) -> CFString ``` |

Modified [CTFontCopyFamilyName(_: CTFont) -> CFString](https://developer.apple.com/documentation/coretext/1509166-ctfontcopyfamilyname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyFamilyName(_ font: CTFont!) -> CFString! ``` |
| To | ``` func CTFontCopyFamilyName(_ font: CTFont) -> CFString ``` |

Modified [CTFontCopyFeatures(_: CTFont) -> CFArray?](https://developer.apple.com/documentation/coretext/1509767-ctfontcopyfeatures)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyFeatures(_ font: CTFont!) -> CFArray! ``` |
| To | ``` func CTFontCopyFeatures(_ font: CTFont) -> CFArray? ``` |

Modified [CTFontCopyFeatureSettings(_: CTFont) -> CFArray?](https://developer.apple.com/documentation/coretext/1509455-ctfontcopyfeaturesettings)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyFeatureSettings(_ font: CTFont!) -> CFArray! ``` |
| To | ``` func CTFontCopyFeatureSettings(_ font: CTFont) -> CFArray? ``` |

Modified [CTFontCopyFontDescriptor(_: CTFont) -> CTFontDescriptor](https://developer.apple.com/documentation/coretext/1508996-ctfontcopyfontdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyFontDescriptor(_ font: CTFont!) -> CTFontDescriptor! ``` |
| To | ``` func CTFontCopyFontDescriptor(_ font: CTFont) -> CTFontDescriptor ``` |

Modified [CTFontCopyFullName(_: CTFont) -> CFString](https://developer.apple.com/documentation/coretext/1510931-ctfontcopyfullname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyFullName(_ font: CTFont!) -> CFString! ``` |
| To | ``` func CTFontCopyFullName(_ font: CTFont) -> CFString ``` |

Modified [CTFontCopyGraphicsFont(_: CTFont, _: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> CGFont](https://developer.apple.com/documentation/coretext/1508712-ctfontcopygraphicsfont)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyGraphicsFont(_ font: CTFont!, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> CGFont! ``` |
| To | ``` func CTFontCopyGraphicsFont(_ font: CTFont, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> CGFont ``` |

Modified [CTFontCopyLocalizedName(_: CTFont, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFString?](https://developer.apple.com/documentation/coretext/1510714-ctfontcopylocalizedname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyLocalizedName(_ font: CTFont!, _ nameKey: CFString!, _ actualLanguage: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFString! ``` |
| To | ``` func CTFontCopyLocalizedName(_ font: CTFont, _ nameKey: CFString, _ actualLanguage: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFString? ``` |

Modified [CTFontCopyName(_: CTFont, _: CFString) -> CFString?](https://developer.apple.com/documentation/coretext/1511240-ctfontcopyname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyName(_ font: CTFont!, _ nameKey: CFString!) -> CFString! ``` |
| To | ``` func CTFontCopyName(_ font: CTFont, _ nameKey: CFString) -> CFString? ``` |

Modified [CTFontCopyPostScriptName(_: CTFont) -> CFString](https://developer.apple.com/documentation/coretext/1510887-ctfontcopypostscriptname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyPostScriptName(_ font: CTFont!) -> CFString! ``` |
| To | ``` func CTFontCopyPostScriptName(_ font: CTFont) -> CFString ``` |

Modified [CTFontCopySupportedLanguages(_: CTFont) -> CFArray](https://developer.apple.com/documentation/coretext/1510096-ctfontcopysupportedlanguages)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopySupportedLanguages(_ font: CTFont!) -> CFArray! ``` |
| To | ``` func CTFontCopySupportedLanguages(_ font: CTFont) -> CFArray ``` |

Modified [CTFontCopyTable(_: CTFont, _: CTFontTableTag, _: CTFontTableOptions) -> CFData?](https://developer.apple.com/documentation/coretext/1510755-ctfontcopytable)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyTable(_ font: CTFont!, _ table: CTFontTableTag, _ options: CTFontTableOptions) -> CFData! ``` |
| To | ``` func CTFontCopyTable(_ font: CTFont, _ table: CTFontTableTag, _ options: CTFontTableOptions) -> CFData? ``` |

Modified [CTFontCopyTraits(_: CTFont) -> CFDictionary](https://developer.apple.com/documentation/coretext/1509723-ctfontcopytraits)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyTraits(_ font: CTFont!) -> CFDictionary! ``` |
| To | ``` func CTFontCopyTraits(_ font: CTFont) -> CFDictionary ``` |

Modified [CTFontCopyVariation(_: CTFont) -> CFDictionary?](https://developer.apple.com/documentation/coretext/1508767-ctfontcopyvariation)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyVariation(_ font: CTFont!) -> CFDictionary! ``` |
| To | ``` func CTFontCopyVariation(_ font: CTFont) -> CFDictionary? ``` |

Modified [CTFontCopyVariationAxes(_: CTFont) -> CFArray?](https://developer.apple.com/documentation/coretext/1509987-ctfontcopyvariationaxes)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyVariationAxes(_ font: CTFont!) -> CFArray! ``` |
| To | ``` func CTFontCopyVariationAxes(_ font: CTFont) -> CFArray? ``` |

Modified [CTFontCreateCopyWithAttributes(_: CTFont, _: CGFloat, _: UnsafePointer<CGAffineTransform>, _: CTFontDescriptor?) -> CTFont](https://developer.apple.com/documentation/coretext/1511225-ctfontcreatecopywithattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateCopyWithAttributes(_ font: CTFont!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor!) -> CTFont! ``` |
| To | ``` func CTFontCreateCopyWithAttributes(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor?) -> CTFont ``` |

Modified [CTFontCreateCopyWithFamily(_: CTFont, _: CGFloat, _: UnsafePointer<CGAffineTransform>, _: CFString) -> CTFont?](https://developer.apple.com/documentation/coretext/1510945-ctfontcreatecopywithfamily)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateCopyWithFamily(_ font: CTFont!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ family: CFString!) -> CTFont! ``` |
| To | ``` func CTFontCreateCopyWithFamily(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ family: CFString) -> CTFont? ``` |

Modified [CTFontCreateCopyWithSymbolicTraits(_: CTFont, _: CGFloat, _: UnsafePointer<CGAffineTransform>, _: CTFontSymbolicTraits, _: CTFontSymbolicTraits) -> CTFont?](https://developer.apple.com/documentation/coretext/1511394-ctfontcreatecopywithsymbolictrai)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateCopyWithSymbolicTraits(_ font: CTFont!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFont! ``` |
| To | ``` func CTFontCreateCopyWithSymbolicTraits(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFont? ``` |

Modified [CTFontCreateForString(_: CTFont, _: CFString, _: CFRange) -> CTFont](https://developer.apple.com/documentation/coretext/1509506-ctfontcreateforstring)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateForString(_ currentFont: CTFont!, _ string: CFString!, _ range: CFRange) -> CTFont! ``` |
| To | ``` func CTFontCreateForString(_ currentFont: CTFont, _ string: CFString, _ range: CFRange) -> CTFont ``` |

Modified [CTFontCreatePathForGlyph(_: CTFont, _: CGGlyph, _: UnsafePointer<CGAffineTransform>) -> CGPath?](https://developer.apple.com/documentation/coretext/1510921-ctfontcreatepathforglyph)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreatePathForGlyph(_ font: CTFont!, _ glyph: CGGlyph, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` |
| To | ``` func CTFontCreatePathForGlyph(_ font: CTFont, _ glyph: CGGlyph, _ matrix: UnsafePointer<CGAffineTransform>) -> CGPath? ``` |

Modified [CTFontCreateUIFontForLanguage(_: CTFontUIFontType, _: CGFloat, _: CFString?) -> CTFont?](https://developer.apple.com/documentation/coretext/1511312-ctfontcreateuifontforlanguage)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateUIFontForLanguage(_ uiType: CTFontUIFontType, _ size: CGFloat, _ language: CFString!) -> CTFont! ``` |
| To | ``` func CTFontCreateUIFontForLanguage(_ uiType: CTFontUIFontType, _ size: CGFloat, _ language: CFString?) -> CTFont? ``` |

Modified [CTFontCreateWithFontDescriptor(_: CTFontDescriptor, _: CGFloat, _: UnsafePointer<CGAffineTransform>) -> CTFont](https://developer.apple.com/documentation/coretext/1509056-ctfontcreatewithfontdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithFontDescriptor(_ descriptor: CTFontDescriptor!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>) -> CTFont! ``` |
| To | ``` func CTFontCreateWithFontDescriptor(_ descriptor: CTFontDescriptor, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>) -> CTFont ``` |

Modified [CTFontCreateWithFontDescriptorAndOptions(_: CTFontDescriptor, _: CGFloat, _: UnsafePointer<CGAffineTransform>, _: CTFontOptions) -> CTFont](https://developer.apple.com/documentation/coretext/1510463-ctfontcreatewithfontdescriptoran)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithFontDescriptorAndOptions(_ descriptor: CTFontDescriptor!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont! ``` |
| To | ``` func CTFontCreateWithFontDescriptorAndOptions(_ descriptor: CTFontDescriptor, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont ``` |

Modified [CTFontCreateWithGraphicsFont(_: CGFont, _: CGFloat, _: UnsafePointer<CGAffineTransform>, _: CTFontDescriptor?) -> CTFont](https://developer.apple.com/documentation/coretext/1508745-ctfontcreatewithgraphicsfont)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithGraphicsFont(_ graphicsFont: CGFont!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor!) -> CTFont! ``` |
| To | ``` func CTFontCreateWithGraphicsFont(_ graphicsFont: CGFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor?) -> CTFont ``` |

Modified [CTFontCreateWithName(_: CFString?, _: CGFloat, _: UnsafePointer<CGAffineTransform>) -> CTFont](https://developer.apple.com/documentation/coretext/1509153-ctfontcreatewithname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithName(_ name: CFString!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>) -> CTFont! ``` |
| To | ``` func CTFontCreateWithName(_ name: CFString?, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>) -> CTFont ``` |

Modified [CTFontCreateWithNameAndOptions(_: CFString, _: CGFloat, _: UnsafePointer<CGAffineTransform>, _: CTFontOptions) -> CTFont](https://developer.apple.com/documentation/coretext/1508624-ctfontcreatewithnameandoptions)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithNameAndOptions(_ name: CFString!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont! ``` |
| To | ``` func CTFontCreateWithNameAndOptions(_ name: CFString, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont ``` |

Modified [CTFontDescriptorCopyAttribute(_: CTFontDescriptor, _: CFString) -> AnyObject?](https://developer.apple.com/documentation/coretext/1510346-ctfontdescriptorcopyattribute)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCopyAttribute(_ descriptor: CTFontDescriptor!, _ attribute: CFString!) -> AnyObject! ``` |
| To | ``` func CTFontDescriptorCopyAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString) -> AnyObject? ``` |

Modified [CTFontDescriptorCopyAttributes(_: CTFontDescriptor) -> CFDictionary](https://developer.apple.com/documentation/coretext/1509327-ctfontdescriptorcopyattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCopyAttributes(_ descriptor: CTFontDescriptor!) -> CFDictionary! ``` |
| To | ``` func CTFontDescriptorCopyAttributes(_ descriptor: CTFontDescriptor) -> CFDictionary ``` |

Modified [CTFontDescriptorCopyLocalizedAttribute(_: CTFontDescriptor, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject?](https://developer.apple.com/documentation/coretext/1509510-ctfontdescriptorcopylocalizedatt)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCopyLocalizedAttribute(_ descriptor: CTFontDescriptor!, _ attribute: CFString!, _ language: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject! ``` |
| To | ``` func CTFontDescriptorCopyLocalizedAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString, _ language: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject? ``` |

Modified [CTFontDescriptorCreateCopyWithAttributes(_: CTFontDescriptor, _: CFDictionary) -> CTFontDescriptor](https://developer.apple.com/documentation/coretext/1511076-ctfontdescriptorcreatecopywithat)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateCopyWithAttributes(_ original: CTFontDescriptor!, _ attributes: CFDictionary!) -> CTFontDescriptor! ``` |
| To | ``` func CTFontDescriptorCreateCopyWithAttributes(_ original: CTFontDescriptor, _ attributes: CFDictionary) -> CTFontDescriptor ``` |

Modified [CTFontDescriptorCreateCopyWithFamily(_: CTFontDescriptor, _: CFString) -> CTFontDescriptor?](https://developer.apple.com/documentation/coretext/1510392-ctfontdescriptorcreatecopywithfa)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateCopyWithFamily(_ original: CTFontDescriptor!, _ family: CFString!) -> CTFontDescriptor! ``` |
| To | ``` func CTFontDescriptorCreateCopyWithFamily(_ original: CTFontDescriptor, _ family: CFString) -> CTFontDescriptor? ``` |

Modified [CTFontDescriptorCreateCopyWithFeature(_: CTFontDescriptor, _: CFNumber, _: CFNumber) -> CTFontDescriptor](https://developer.apple.com/documentation/coretext/1508652-ctfontdescriptorcreatecopywithfe)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateCopyWithFeature(_ original: CTFontDescriptor!, _ featureTypeIdentifier: CFNumber!, _ featureSelectorIdentifier: CFNumber!) -> CTFontDescriptor! ``` |
| To | ``` func CTFontDescriptorCreateCopyWithFeature(_ original: CTFontDescriptor, _ featureTypeIdentifier: CFNumber, _ featureSelectorIdentifier: CFNumber) -> CTFontDescriptor ``` |

Modified [CTFontDescriptorCreateCopyWithSymbolicTraits(_: CTFontDescriptor, _: CTFontSymbolicTraits, _: CTFontSymbolicTraits) -> CTFontDescriptor?](https://developer.apple.com/documentation/coretext/1509171-ctfontdescriptorcreatecopywithsy)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateCopyWithSymbolicTraits(_ original: CTFontDescriptor!, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFontDescriptor! ``` |
| To | ``` func CTFontDescriptorCreateCopyWithSymbolicTraits(_ original: CTFontDescriptor, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFontDescriptor? ``` |

Modified [CTFontDescriptorCreateCopyWithVariation(_: CTFontDescriptor, _: CFNumber, _: CGFloat) -> CTFontDescriptor](https://developer.apple.com/documentation/coretext/1508650-ctfontdescriptorcreatecopywithva)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateCopyWithVariation(_ original: CTFontDescriptor!, _ variationIdentifier: CFNumber!, _ variationValue: CGFloat) -> CTFontDescriptor! ``` |
| To | ``` func CTFontDescriptorCreateCopyWithVariation(_ original: CTFontDescriptor, _ variationIdentifier: CFNumber, _ variationValue: CGFloat) -> CTFontDescriptor ``` |

Modified [CTFontDescriptorCreateMatchingFontDescriptor(_: CTFontDescriptor, _: CFSet?) -> CTFontDescriptor?](https://developer.apple.com/documentation/coretext/1508848-ctfontdescriptorcreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateMatchingFontDescriptor(_ descriptor: CTFontDescriptor!, _ mandatoryAttributes: CFSet!) -> CTFontDescriptor! ``` |
| To | ``` func CTFontDescriptorCreateMatchingFontDescriptor(_ descriptor: CTFontDescriptor, _ mandatoryAttributes: CFSet?) -> CTFontDescriptor? ``` |

Modified [CTFontDescriptorCreateMatchingFontDescriptors(_: CTFontDescriptor, _: CFSet?) -> CFArray?](https://developer.apple.com/documentation/coretext/1508794-ctfontdescriptorcreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateMatchingFontDescriptors(_ descriptor: CTFontDescriptor!, _ mandatoryAttributes: CFSet!) -> CFArray! ``` |
| To | ``` func CTFontDescriptorCreateMatchingFontDescriptors(_ descriptor: CTFontDescriptor, _ mandatoryAttributes: CFSet?) -> CFArray? ``` |

Modified [CTFontDescriptorCreateWithAttributes(_: CFDictionary) -> CTFontDescriptor](https://developer.apple.com/documentation/coretext/1510642-ctfontdescriptorcreatewithattrib)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateWithAttributes(_ attributes: CFDictionary!) -> CTFontDescriptor! ``` |
| To | ``` func CTFontDescriptorCreateWithAttributes(_ attributes: CFDictionary) -> CTFontDescriptor ``` |

Modified [CTFontDescriptorCreateWithNameAndSize(_: CFString, _: CGFloat) -> CTFontDescriptor](https://developer.apple.com/documentation/coretext/1510226-ctfontdescriptorcreatewithnamean)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCreateWithNameAndSize(_ name: CFString!, _ size: CGFloat) -> CTFontDescriptor! ``` |
| To | ``` func CTFontDescriptorCreateWithNameAndSize(_ name: CFString, _ size: CGFloat) -> CTFontDescriptor ``` |

Modified [CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_: CFArray, _: CFSet?, _: CTFontDescriptorProgressHandler) -> Bool](https://developer.apple.com/documentation/coretext/1511433-ctfontdescriptormatchfontdescrip)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_ descriptors: CFArray!, _ mandatoryAttributes: CFSet!, _ progressBlock: CTFontDescriptorProgressHandler!) -> Bool ``` |
| To | ``` func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_ descriptors: CFArray, _ mandatoryAttributes: CFSet?, _ progressBlock: CTFontDescriptorProgressHandler) -> Bool ``` |

Modified [CTFontDescriptorProgressHandler](https://developer.apple.com/documentation/coretext/ctfontdescriptorprogresshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTFontDescriptorProgressHandler = (CTFontDescriptorMatchingState, CFDictionary!) -> Bool ``` |
| To | ``` typealias CTFontDescriptorProgressHandler = (CTFontDescriptorMatchingState, CFDictionary) -> Bool ``` |

Modified [CTFontDrawGlyphs(_: CTFont, _: UnsafePointer<CGGlyph>, _: UnsafePointer<CGPoint>, _: Int, _: CGContext)](https://developer.apple.com/documentation/coretext/1509850-ctfontdrawglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDrawGlyphs(_ font: CTFont!, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int, _ context: CGContext!) ``` |
| To | ``` func CTFontDrawGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int, _ context: CGContext) ``` |

Modified [CTFontGetAdvancesForGlyphs(_: CTFont, _: CTFontOrientation, _: UnsafePointer<CGGlyph>, _: UnsafeMutablePointer<CGSize>, _: CFIndex) -> Double](https://developer.apple.com/documentation/coretext/1511265-ctfontgetadvancesforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetAdvancesForGlyphs(_ font: CTFont!, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ advances: UnsafeMutablePointer<CGSize>, _ count: CFIndex) -> Double ``` |
| To | ``` func CTFontGetAdvancesForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ advances: UnsafeMutablePointer<CGSize>, _ count: CFIndex) -> Double ``` |

Modified [CTFontGetAscent(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1510018-ctfontgetascent)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetAscent(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetAscent(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontGetBoundingBox(_: CTFont) -> CGRect](https://developer.apple.com/documentation/coretext/1509253-ctfontgetboundingbox)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetBoundingBox(_ font: CTFont!) -> CGRect ``` |
| To | ``` func CTFontGetBoundingBox(_ font: CTFont) -> CGRect ``` |

Modified [CTFontGetBoundingRectsForGlyphs(_: CTFont, _: CTFontOrientation, _: UnsafePointer<CGGlyph>, _: UnsafeMutablePointer<CGRect>, _: CFIndex) -> CGRect](https://developer.apple.com/documentation/coretext/1509419-ctfontgetboundingrectsforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetBoundingRectsForGlyphs(_ font: CTFont!, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>, _ count: CFIndex) -> CGRect ``` |
| To | ``` func CTFontGetBoundingRectsForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>, _ count: CFIndex) -> CGRect ``` |

Modified [CTFontGetCapHeight(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1511349-ctfontgetcapheight)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetCapHeight(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetCapHeight(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontGetDescent(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1510313-ctfontgetdescent)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetDescent(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetDescent(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontGetGlyphCount(_: CTFont) -> CFIndex](https://developer.apple.com/documentation/coretext/1511330-ctfontgetglyphcount)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetGlyphCount(_ font: CTFont!) -> CFIndex ``` |
| To | ``` func CTFontGetGlyphCount(_ font: CTFont) -> CFIndex ``` |

Modified [CTFontGetGlyphsForCharacters(_: CTFont, _: UnsafePointer<UniChar>, _: UnsafeMutablePointer<CGGlyph>, _: CFIndex) -> Bool](https://developer.apple.com/documentation/coretext/1510813-ctfontgetglyphsforcharacters)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetGlyphsForCharacters(_ font: CTFont!, _ characters: UnsafePointer<UniChar>, _ glyphs: UnsafeMutablePointer<CGGlyph>, _ count: CFIndex) -> Bool ``` |
| To | ``` func CTFontGetGlyphsForCharacters(_ font: CTFont, _ characters: UnsafePointer<UniChar>, _ glyphs: UnsafeMutablePointer<CGGlyph>, _ count: CFIndex) -> Bool ``` |

Modified [CTFontGetGlyphWithName(_: CTFont, _: CFString) -> CGGlyph](https://developer.apple.com/documentation/coretext/1510788-ctfontgetglyphwithname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetGlyphWithName(_ font: CTFont!, _ glyphName: CFString!) -> CGGlyph ``` |
| To | ``` func CTFontGetGlyphWithName(_ font: CTFont, _ glyphName: CFString) -> CGGlyph ``` |

Modified [CTFontGetLeading(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1509426-ctfontgetleading)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetLeading(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetLeading(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontGetLigatureCaretPositions(_: CTFont, _: CGGlyph, _: UnsafeMutablePointer<CGFloat>, _: CFIndex) -> CFIndex](https://developer.apple.com/documentation/coretext/1508820-ctfontgetligaturecaretpositions)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetLigatureCaretPositions(_ font: CTFont!, _ glyph: CGGlyph, _ positions: UnsafeMutablePointer<CGFloat>, _ maxPositions: CFIndex) -> CFIndex ``` |
| To | ``` func CTFontGetLigatureCaretPositions(_ font: CTFont, _ glyph: CGGlyph, _ positions: UnsafeMutablePointer<CGFloat>, _ maxPositions: CFIndex) -> CFIndex ``` |

Modified [CTFontGetMatrix(_: CTFont) -> CGAffineTransform](https://developer.apple.com/documentation/coretext/1510407-ctfontgetmatrix)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetMatrix(_ font: CTFont!) -> CGAffineTransform ``` |
| To | ``` func CTFontGetMatrix(_ font: CTFont) -> CGAffineTransform ``` |

Modified [CTFontGetOpticalBoundsForGlyphs(_: CTFont, _: UnsafePointer<CGGlyph>, _: UnsafeMutablePointer<CGRect>, _: CFIndex, _: CFOptionFlags) -> CGRect](https://developer.apple.com/documentation/coretext/1510531-ctfontgetopticalboundsforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetOpticalBoundsForGlyphs(_ font: CTFont!, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>, _ count: CFIndex, _ options: CFOptionFlags) -> CGRect ``` |
| To | ``` func CTFontGetOpticalBoundsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>, _ count: CFIndex, _ options: CFOptionFlags) -> CGRect ``` |

Modified [CTFontGetSize(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1511100-ctfontgetsize)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetSize(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetSize(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontGetSlantAngle(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1511178-ctfontgetslantangle)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetSlantAngle(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetSlantAngle(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontGetStringEncoding(_: CTFont) -> CFStringEncoding](https://developer.apple.com/documentation/coretext/1509519-ctfontgetstringencoding)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetStringEncoding(_ font: CTFont!) -> CFStringEncoding ``` |
| To | ``` func CTFontGetStringEncoding(_ font: CTFont) -> CFStringEncoding ``` |

Modified [CTFontGetSymbolicTraits(_: CTFont) -> CTFontSymbolicTraits](https://developer.apple.com/documentation/coretext/1509142-ctfontgetsymbolictraits)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetSymbolicTraits(_ font: CTFont!) -> CTFontSymbolicTraits ``` |
| To | ``` func CTFontGetSymbolicTraits(_ font: CTFont) -> CTFontSymbolicTraits ``` |

Modified [CTFontGetUnderlinePosition(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1511320-ctfontgetunderlineposition)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetUnderlinePosition(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetUnderlinePosition(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontGetUnderlineThickness(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1508963-ctfontgetunderlinethickness)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetUnderlineThickness(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetUnderlineThickness(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontGetUnitsPerEm(_: CTFont) -> UInt32](https://developer.apple.com/documentation/coretext/1510550-ctfontgetunitsperem)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetUnitsPerEm(_ font: CTFont!) -> UInt32 ``` |
| To | ``` func CTFontGetUnitsPerEm(_ font: CTFont) -> UInt32 ``` |

Modified [CTFontGetVerticalTranslationsForGlyphs(_: CTFont, _: UnsafePointer<CGGlyph>, _: UnsafeMutablePointer<CGSize>, _: CFIndex)](https://developer.apple.com/documentation/coretext/1511102-ctfontgetverticaltranslationsfor)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetVerticalTranslationsForGlyphs(_ font: CTFont!, _ glyphs: UnsafePointer<CGGlyph>, _ translations: UnsafeMutablePointer<CGSize>, _ count: CFIndex) ``` |
| To | ``` func CTFontGetVerticalTranslationsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ translations: UnsafeMutablePointer<CGSize>, _ count: CFIndex) ``` |

Modified [CTFontGetXHeight(_: CTFont) -> CGFloat](https://developer.apple.com/documentation/coretext/1510255-ctfontgetxheight)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetXHeight(_ font: CTFont!) -> CGFloat ``` |
| To | ``` func CTFontGetXHeight(_ font: CTFont) -> CGFloat ``` |

Modified [CTFontManagerCreateFontDescriptorFromData(_: CFData) -> CTFontDescriptor?](https://developer.apple.com/documentation/coretext/1499509-ctfontmanagercreatefontdescripto)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerCreateFontDescriptorFromData(_ data: CFData!) -> CTFontDescriptor! ``` |
| To | ``` func CTFontManagerCreateFontDescriptorFromData(_ data: CFData) -> CTFontDescriptor? ``` |

Modified [CTFontManagerCreateFontDescriptorsFromURL(_: CFURL) -> CFArray?](https://developer.apple.com/documentation/coretext/1499500-ctfontmanagercreatefontdescripto)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerCreateFontDescriptorsFromURL(_ fileURL: CFURL!) -> CFArray! ``` |
| To | ``` func CTFontManagerCreateFontDescriptorsFromURL(_ fileURL: CFURL) -> CFArray? ``` |

Modified [CTFontManagerRegisterFontsForURL(_: CFURL, _: CTFontManagerScope, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/coretext/1499468-ctfontmanagerregisterfontsforurl)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerRegisterFontsForURL(_ fontURL: CFURL!, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CTFontManagerRegisterFontsForURL(_ fontURL: CFURL, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CTFontManagerRegisterFontsForURLs(_: CFArray, _: CTFontManagerScope, _: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool](https://developer.apple.com/documentation/coretext/1499470-ctfontmanagerregisterfontsforurl)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerRegisterFontsForURLs(_ fontURLs: CFArray!, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool ``` |
| To | ``` func CTFontManagerRegisterFontsForURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool ``` |

Modified [CTFontManagerRegisterGraphicsFont(_: CGFont, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/coretext/1499499-ctfontmanagerregistergraphicsfon)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerRegisterGraphicsFont(_ font: CGFont!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CTFontManagerRegisterGraphicsFont(_ font: CGFont, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CTFontManagerUnregisterFontsForURL(_: CFURL, _: CTFontManagerScope, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/coretext/1499496-ctfontmanagerunregisterfontsforu)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerUnregisterFontsForURL(_ fontURL: CFURL!, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CTFontManagerUnregisterFontsForURL(_ fontURL: CFURL, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CTFontManagerUnregisterFontsForURLs(_: CFArray, _: CTFontManagerScope, _: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool](https://developer.apple.com/documentation/coretext/1499477-ctfontmanagerunregisterfontsforu)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerUnregisterFontsForURLs(_ fontURLs: CFArray!, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool ``` |
| To | ``` func CTFontManagerUnregisterFontsForURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool ``` |

Modified [CTFontManagerUnregisterGraphicsFont(_: CGFont, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/coretext/1499472-ctfontmanagerunregistergraphicsf)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerUnregisterGraphicsFont(_ font: CGFont!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CTFontManagerUnregisterGraphicsFont(_ font: CGFont, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CTFrameDraw(_: CTFrame, _: CGContext)](https://developer.apple.com/documentation/coretext/1509589-ctframedraw)

|  | Declaration |
| --- | --- |
| From | ``` func CTFrameDraw(_ frame: CTFrame!, _ context: CGContext!) ``` |
| To | ``` func CTFrameDraw(_ frame: CTFrame, _ context: CGContext) ``` |

Modified [CTFrameGetFrameAttributes(_: CTFrame) -> CFDictionary?](https://developer.apple.com/documentation/coretext/1510750-ctframegetframeattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CTFrameGetFrameAttributes(_ frame: CTFrame!) -> CFDictionary! ``` |
| To | ``` func CTFrameGetFrameAttributes(_ frame: CTFrame) -> CFDictionary? ``` |

Modified [CTFrameGetLineOrigins(_: CTFrame, _: CFRange, _: UnsafeMutablePointer<CGPoint>)](https://developer.apple.com/documentation/coretext/1510610-ctframegetlineorigins)

|  | Declaration |
| --- | --- |
| From | ``` func CTFrameGetLineOrigins(_ frame: CTFrame!, _ range: CFRange, _ origins: UnsafeMutablePointer<CGPoint>) ``` |
| To | ``` func CTFrameGetLineOrigins(_ frame: CTFrame, _ range: CFRange, _ origins: UnsafeMutablePointer<CGPoint>) ``` |

Modified [CTFrameGetLines(_: CTFrame) -> CFArray](https://developer.apple.com/documentation/coretext/1510385-ctframegetlines)

|  | Declaration |
| --- | --- |
| From | ``` func CTFrameGetLines(_ frame: CTFrame!) -> CFArray! ``` |
| To | ``` func CTFrameGetLines(_ frame: CTFrame) -> CFArray ``` |

Modified [CTFrameGetPath(_: CTFrame) -> CGPath](https://developer.apple.com/documentation/coretext/1510806-ctframegetpath)

|  | Declaration |
| --- | --- |
| From | ``` func CTFrameGetPath(_ frame: CTFrame!) -> CGPath! ``` |
| To | ``` func CTFrameGetPath(_ frame: CTFrame) -> CGPath ``` |

Modified [CTFrameGetStringRange(_: CTFrame) -> CFRange](https://developer.apple.com/documentation/coretext/1508707-ctframegetstringrange)

|  | Declaration |
| --- | --- |
| From | ``` func CTFrameGetStringRange(_ frame: CTFrame!) -> CFRange ``` |
| To | ``` func CTFrameGetStringRange(_ frame: CTFrame) -> CFRange ``` |

Modified [CTFrameGetVisibleStringRange(_: CTFrame) -> CFRange](https://developer.apple.com/documentation/coretext/1511109-ctframegetvisiblestringrange)

|  | Declaration |
| --- | --- |
| From | ``` func CTFrameGetVisibleStringRange(_ frame: CTFrame!) -> CFRange ``` |
| To | ``` func CTFrameGetVisibleStringRange(_ frame: CTFrame) -> CFRange ``` |

Modified [CTFramesetterCreateFrame(_: CTFramesetter, _: CFRange, _: CGPath, _: CFDictionary?) -> CTFrame](https://developer.apple.com/documentation/coretext/1478564-ctframesettercreateframe)

|  | Declaration |
| --- | --- |
| From | ``` func CTFramesetterCreateFrame(_ framesetter: CTFramesetter!, _ stringRange: CFRange, _ path: CGPath!, _ frameAttributes: CFDictionary!) -> CTFrame! ``` |
| To | ``` func CTFramesetterCreateFrame(_ framesetter: CTFramesetter, _ stringRange: CFRange, _ path: CGPath, _ frameAttributes: CFDictionary?) -> CTFrame ``` |

Modified [CTFramesetterCreateWithAttributedString(_: CFAttributedString) -> CTFramesetter](https://developer.apple.com/documentation/coretext/1478568-ctframesettercreatewithattribute)

|  | Declaration |
| --- | --- |
| From | ``` func CTFramesetterCreateWithAttributedString(_ string: CFAttributedString!) -> CTFramesetter! ``` |
| To | ``` func CTFramesetterCreateWithAttributedString(_ string: CFAttributedString) -> CTFramesetter ``` |

Modified [CTFramesetterGetTypesetter(_: CTFramesetter) -> CTTypesetter](https://developer.apple.com/documentation/coretext/1478562-ctframesettergettypesetter)

|  | Declaration |
| --- | --- |
| From | ``` func CTFramesetterGetTypesetter(_ framesetter: CTFramesetter!) -> CTTypesetter! ``` |
| To | ``` func CTFramesetterGetTypesetter(_ framesetter: CTFramesetter) -> CTTypesetter ``` |

Modified [CTFramesetterSuggestFrameSizeWithConstraints(_: CTFramesetter, _: CFRange, _: CFDictionary?, _: CGSize, _: UnsafeMutablePointer<CFRange>) -> CGSize](https://developer.apple.com/documentation/coretext/1478566-ctframesettersuggestframesizewit)

|  | Declaration |
| --- | --- |
| From | ``` func CTFramesetterSuggestFrameSizeWithConstraints(_ framesetter: CTFramesetter!, _ stringRange: CFRange, _ frameAttributes: CFDictionary!, _ constraints: CGSize, _ fitRange: UnsafeMutablePointer<CFRange>) -> CGSize ``` |
| To | ``` func CTFramesetterSuggestFrameSizeWithConstraints(_ framesetter: CTFramesetter, _ stringRange: CFRange, _ frameAttributes: CFDictionary?, _ constraints: CGSize, _ fitRange: UnsafeMutablePointer<CFRange>) -> CGSize ``` |

Modified [CTGlyphInfoCreateWithCharacterIdentifier(_: CGFontIndex, _: CTCharacterCollection, _: CFString) -> CTGlyphInfo](https://developer.apple.com/documentation/coretext/1402042-ctglyphinfocreatewithcharacterid)

|  | Declaration |
| --- | --- |
| From | ``` func CTGlyphInfoCreateWithCharacterIdentifier(_ cid: CGFontIndex, _ collection: CTCharacterCollection, _ baseString: CFString!) -> CTGlyphInfo! ``` |
| To | ``` func CTGlyphInfoCreateWithCharacterIdentifier(_ cid: CGFontIndex, _ collection: CTCharacterCollection, _ baseString: CFString) -> CTGlyphInfo ``` |

Modified [CTGlyphInfoCreateWithGlyph(_: CGGlyph, _: CTFont, _: CFString) -> CTGlyphInfo](https://developer.apple.com/documentation/coretext/1402062-ctglyphinfocreatewithglyph)

|  | Declaration |
| --- | --- |
| From | ``` func CTGlyphInfoCreateWithGlyph(_ glyph: CGGlyph, _ font: CTFont!, _ baseString: CFString!) -> CTGlyphInfo! ``` |
| To | ``` func CTGlyphInfoCreateWithGlyph(_ glyph: CGGlyph, _ font: CTFont, _ baseString: CFString) -> CTGlyphInfo ``` |

Modified [CTGlyphInfoCreateWithGlyphName(_: CFString, _: CTFont, _: CFString) -> CTGlyphInfo](https://developer.apple.com/documentation/coretext/1402026-ctglyphinfocreatewithglyphname)

|  | Declaration |
| --- | --- |
| From | ``` func CTGlyphInfoCreateWithGlyphName(_ glyphName: CFString!, _ font: CTFont!, _ baseString: CFString!) -> CTGlyphInfo! ``` |
| To | ``` func CTGlyphInfoCreateWithGlyphName(_ glyphName: CFString, _ font: CTFont, _ baseString: CFString) -> CTGlyphInfo ``` |

Modified [CTGlyphInfoGetCharacterCollection(_: CTGlyphInfo) -> CTCharacterCollection](https://developer.apple.com/documentation/coretext/1402034-ctglyphinfogetcharactercollectio)

|  | Declaration |
| --- | --- |
| From | ``` func CTGlyphInfoGetCharacterCollection(_ glyphInfo: CTGlyphInfo!) -> CTCharacterCollection ``` |
| To | ``` func CTGlyphInfoGetCharacterCollection(_ glyphInfo: CTGlyphInfo) -> CTCharacterCollection ``` |

Modified [CTGlyphInfoGetCharacterIdentifier(_: CTGlyphInfo) -> CGFontIndex](https://developer.apple.com/documentation/coretext/1402064-ctglyphinfogetcharacteridentifie)

|  | Declaration |
| --- | --- |
| From | ``` func CTGlyphInfoGetCharacterIdentifier(_ glyphInfo: CTGlyphInfo!) -> CGFontIndex ``` |
| To | ``` func CTGlyphInfoGetCharacterIdentifier(_ glyphInfo: CTGlyphInfo) -> CGFontIndex ``` |

Modified [CTGlyphInfoGetGlyphName(_: CTGlyphInfo) -> CFString?](https://developer.apple.com/documentation/coretext/1402050-ctglyphinfogetglyphname)

|  | Declaration |
| --- | --- |
| From | ``` func CTGlyphInfoGetGlyphName(_ glyphInfo: CTGlyphInfo!) -> CFString! ``` |
| To | ``` func CTGlyphInfoGetGlyphName(_ glyphInfo: CTGlyphInfo) -> CFString? ``` |

Modified [CTLineCreateJustifiedLine(_: CTLine, _: CGFloat, _: Double) -> CTLine?](https://developer.apple.com/documentation/coretext/1511238-ctlinecreatejustifiedline)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineCreateJustifiedLine(_ line: CTLine!, _ justificationFactor: CGFloat, _ justificationWidth: Double) -> CTLine! ``` |
| To | ``` func CTLineCreateJustifiedLine(_ line: CTLine, _ justificationFactor: CGFloat, _ justificationWidth: Double) -> CTLine? ``` |

Modified [CTLineCreateTruncatedLine(_: CTLine, _: Double, _: CTLineTruncationType, _: CTLine?) -> CTLine?](https://developer.apple.com/documentation/coretext/1510688-ctlinecreatetruncatedline)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineCreateTruncatedLine(_ line: CTLine!, _ width: Double, _ truncationType: CTLineTruncationType, _ truncationToken: CTLine!) -> CTLine! ``` |
| To | ``` func CTLineCreateTruncatedLine(_ line: CTLine, _ width: Double, _ truncationType: CTLineTruncationType, _ truncationToken: CTLine?) -> CTLine? ``` |

Modified [CTLineCreateWithAttributedString(_: CFAttributedString) -> CTLine](https://developer.apple.com/documentation/coretext/1509461-ctlinecreatewithattributedstring)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineCreateWithAttributedString(_ string: CFAttributedString!) -> CTLine! ``` |
| To | ``` func CTLineCreateWithAttributedString(_ attrString: CFAttributedString) -> CTLine ``` |

Modified [CTLineDraw(_: CTLine, _: CGContext)](https://developer.apple.com/documentation/coretext/1511145-ctlinedraw)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineDraw(_ line: CTLine!, _ context: CGContext!) ``` |
| To | ``` func CTLineDraw(_ line: CTLine, _ context: CGContext) ``` |

Modified [CTLineGetBoundsWithOptions(_: CTLine, _: CTLineBoundsOptions) -> CGRect](https://developer.apple.com/documentation/coretext/1511332-ctlinegetboundswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetBoundsWithOptions(_ line: CTLine!, _ options: CTLineBoundsOptions) -> CGRect ``` |
| To | ``` func CTLineGetBoundsWithOptions(_ line: CTLine, _ options: CTLineBoundsOptions) -> CGRect ``` |

Modified [CTLineGetGlyphCount(_: CTLine) -> CFIndex](https://developer.apple.com/documentation/coretext/1509985-ctlinegetglyphcount)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetGlyphCount(_ line: CTLine!) -> CFIndex ``` |
| To | ``` func CTLineGetGlyphCount(_ line: CTLine) -> CFIndex ``` |

Modified [CTLineGetGlyphRuns(_: CTLine) -> CFArray](https://developer.apple.com/documentation/coretext/1509800-ctlinegetglyphruns)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetGlyphRuns(_ line: CTLine!) -> CFArray! ``` |
| To | ``` func CTLineGetGlyphRuns(_ line: CTLine) -> CFArray ``` |

Modified [CTLineGetImageBounds(_: CTLine, _: CGContext?) -> CGRect](https://developer.apple.com/documentation/coretext/1510967-ctlinegetimagebounds)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetImageBounds(_ line: CTLine!, _ context: CGContext!) -> CGRect ``` |
| To | ``` func CTLineGetImageBounds(_ line: CTLine, _ context: CGContext?) -> CGRect ``` |

Modified [CTLineGetOffsetForStringIndex(_: CTLine, _: CFIndex, _: UnsafeMutablePointer<CGFloat>) -> CGFloat](https://developer.apple.com/documentation/coretext/1509629-ctlinegetoffsetforstringindex)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetOffsetForStringIndex(_ line: CTLine!, _ charIndex: CFIndex, _ secondaryOffset: UnsafeMutablePointer<CGFloat>) -> CGFloat ``` |
| To | ``` func CTLineGetOffsetForStringIndex(_ line: CTLine, _ charIndex: CFIndex, _ secondaryOffset: UnsafeMutablePointer<CGFloat>) -> CGFloat ``` |

Modified [CTLineGetPenOffsetForFlush(_: CTLine, _: CGFloat, _: Double) -> Double](https://developer.apple.com/documentation/coretext/1511056-ctlinegetpenoffsetforflush)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetPenOffsetForFlush(_ line: CTLine!, _ flushFactor: CGFloat, _ flushWidth: Double) -> Double ``` |
| To | ``` func CTLineGetPenOffsetForFlush(_ line: CTLine, _ flushFactor: CGFloat, _ flushWidth: Double) -> Double ``` |

Modified [CTLineGetStringIndexForPosition(_: CTLine, _: CGPoint) -> CFIndex](https://developer.apple.com/documentation/coretext/1508876-ctlinegetstringindexforposition)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetStringIndexForPosition(_ line: CTLine!, _ position: CGPoint) -> CFIndex ``` |
| To | ``` func CTLineGetStringIndexForPosition(_ line: CTLine, _ position: CGPoint) -> CFIndex ``` |

Modified [CTLineGetStringRange(_: CTLine) -> CFRange](https://developer.apple.com/documentation/coretext/1509733-ctlinegetstringrange)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetStringRange(_ line: CTLine!) -> CFRange ``` |
| To | ``` func CTLineGetStringRange(_ line: CTLine) -> CFRange ``` |

Modified [CTLineGetTrailingWhitespaceWidth(_: CTLine) -> Double](https://developer.apple.com/documentation/coretext/1511357-ctlinegettrailingwhitespacewidth)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetTrailingWhitespaceWidth(_ line: CTLine!) -> Double ``` |
| To | ``` func CTLineGetTrailingWhitespaceWidth(_ line: CTLine) -> Double ``` |

Modified [CTLineGetTypographicBounds(_: CTLine, _: UnsafeMutablePointer<CGFloat>, _: UnsafeMutablePointer<CGFloat>, _: UnsafeMutablePointer<CGFloat>) -> Double](https://developer.apple.com/documentation/coretext/1510360-ctlinegettypographicbounds)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetTypographicBounds(_ line: CTLine!, _ ascent: UnsafeMutablePointer<CGFloat>, _ descent: UnsafeMutablePointer<CGFloat>, _ leading: UnsafeMutablePointer<CGFloat>) -> Double ``` |
| To | ``` func CTLineGetTypographicBounds(_ line: CTLine, _ ascent: UnsafeMutablePointer<CGFloat>, _ descent: UnsafeMutablePointer<CGFloat>, _ leading: UnsafeMutablePointer<CGFloat>) -> Double ``` |

Modified [CTParagraphStyleCreate(_: UnsafePointer<CTParagraphStyleSetting>, _: Int) -> CTParagraphStyle](https://developer.apple.com/documentation/coretext/1496164-ctparagraphstylecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CTParagraphStyleCreate(_ settings: UnsafePointer<CTParagraphStyleSetting>, _ settingCount: Int) -> CTParagraphStyle! ``` |
| To | ``` func CTParagraphStyleCreate(_ settings: UnsafePointer<CTParagraphStyleSetting>, _ settingCount: Int) -> CTParagraphStyle ``` |

Modified [CTParagraphStyleCreateCopy(_: CTParagraphStyle) -> CTParagraphStyle](https://developer.apple.com/documentation/coretext/1496153-ctparagraphstylecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CTParagraphStyleCreateCopy(_ paragraphStyle: CTParagraphStyle!) -> CTParagraphStyle! ``` |
| To | ``` func CTParagraphStyleCreateCopy(_ paragraphStyle: CTParagraphStyle) -> CTParagraphStyle ``` |

Modified [CTParagraphStyleGetValueForSpecifier(_: CTParagraphStyle, _: CTParagraphStyleSpecifier, _: Int, _: UnsafeMutablePointer<Void>) -> Bool](https://developer.apple.com/documentation/coretext/1496169-ctparagraphstylegetvalueforspeci)

|  | Declaration |
| --- | --- |
| From | ``` func CTParagraphStyleGetValueForSpecifier(_ paragraphStyle: CTParagraphStyle!, _ spec: CTParagraphStyleSpecifier, _ valueBufferSize: Int, _ valueBuffer: UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` func CTParagraphStyleGetValueForSpecifier(_ paragraphStyle: CTParagraphStyle, _ spec: CTParagraphStyleSpecifier, _ valueBufferSize: Int, _ valueBuffer: UnsafeMutablePointer<Void>) -> Bool ``` |

Modified [CTRubyAnnotationCreate(_: CTRubyAlignment, _: CTRubyOverhang, _: CGFloat, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CTRubyAnnotation](https://developer.apple.com/documentation/coretext/1510191-ctrubyannotationcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CTRubyAnnotationCreate(_ alignment: CTRubyAlignment, _ overhang: CTRubyOverhang, _ sizeFactor: CGFloat, _ text: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CTRubyAnnotation>! ``` |
| To | ``` func CTRubyAnnotationCreate(_ alignment: CTRubyAlignment, _ overhang: CTRubyOverhang, _ sizeFactor: CGFloat, _ text: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CTRubyAnnotation ``` |

Modified [CTRubyAnnotationCreateCopy(_: CTRubyAnnotation) -> CTRubyAnnotation](https://developer.apple.com/documentation/coretext/1508925-ctrubyannotationcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CTRubyAnnotationCreateCopy(_ rubyAnnotation: CTRubyAnnotation!) -> Unmanaged<CTRubyAnnotation>! ``` |
| To | ``` func CTRubyAnnotationCreateCopy(_ rubyAnnotation: CTRubyAnnotation) -> CTRubyAnnotation ``` |

Modified [CTRubyAnnotationGetAlignment(_: CTRubyAnnotation) -> CTRubyAlignment](https://developer.apple.com/documentation/coretext/1508832-ctrubyannotationgetalignment)

|  | Declaration |
| --- | --- |
| From | ``` func CTRubyAnnotationGetAlignment(_ rubyAnnotation: CTRubyAnnotation!) -> CTRubyAlignment ``` |
| To | ``` func CTRubyAnnotationGetAlignment(_ rubyAnnotation: CTRubyAnnotation) -> CTRubyAlignment ``` |

Modified [CTRubyAnnotationGetOverhang(_: CTRubyAnnotation) -> CTRubyOverhang](https://developer.apple.com/documentation/coretext/1509866-ctrubyannotationgetoverhang)

|  | Declaration |
| --- | --- |
| From | ``` func CTRubyAnnotationGetOverhang(_ rubyAnnotation: CTRubyAnnotation!) -> CTRubyOverhang ``` |
| To | ``` func CTRubyAnnotationGetOverhang(_ rubyAnnotation: CTRubyAnnotation) -> CTRubyOverhang ``` |

Modified [CTRubyAnnotationGetSizeFactor(_: CTRubyAnnotation) -> CGFloat](https://developer.apple.com/documentation/coretext/1509594-ctrubyannotationgetsizefactor)

|  | Declaration |
| --- | --- |
| From | ``` func CTRubyAnnotationGetSizeFactor(_ rubyAnnotation: CTRubyAnnotation!) -> CGFloat ``` |
| To | ``` func CTRubyAnnotationGetSizeFactor(_ rubyAnnotation: CTRubyAnnotation) -> CGFloat ``` |

Modified [CTRubyAnnotationGetTextForPosition(_: CTRubyAnnotation, _: CTRubyPosition) -> CFString?](https://developer.apple.com/documentation/coretext/1511023-ctrubyannotationgettextforpositi)

|  | Declaration |
| --- | --- |
| From | ``` func CTRubyAnnotationGetTextForPosition(_ rubyAnnotation: CTRubyAnnotation!, _ position: CTRubyPosition) -> Unmanaged<CFString>! ``` |
| To | ``` func CTRubyAnnotationGetTextForPosition(_ rubyAnnotation: CTRubyAnnotation, _ position: CTRubyPosition) -> CFString? ``` |

Modified [CTRunDelegateCreate(_: UnsafePointer<CTRunDelegateCallbacks>, _: UnsafeMutablePointer<Void>) -> CTRunDelegate?](https://developer.apple.com/documentation/coretext/1498167-ctrundelegatecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunDelegateCreate(_ callbacks: UnsafePointer<CTRunDelegateCallbacks>, _ refCon: UnsafeMutablePointer<Void>) -> CTRunDelegate! ``` |
| To | ``` func CTRunDelegateCreate(_ callbacks: UnsafePointer<CTRunDelegateCallbacks>, _ refCon: UnsafeMutablePointer<Void>) -> CTRunDelegate? ``` |

Modified [CTRunDelegateDeallocateCallback](https://developer.apple.com/documentation/coretext/ctrundelegatedeallocatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateDeallocateCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CTRunDelegateDeallocateCallback = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CTRunDelegateGetAscentCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetascentcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetAscentCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> CGFloat)> ``` |
| To | ``` typealias CTRunDelegateGetAscentCallback = (UnsafeMutablePointer<Void>) -> CGFloat ``` |

Modified [CTRunDelegateGetDescentCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetdescentcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetDescentCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> CGFloat)> ``` |
| To | ``` typealias CTRunDelegateGetDescentCallback = (UnsafeMutablePointer<Void>) -> CGFloat ``` |

Modified [CTRunDelegateGetRefCon(_: CTRunDelegate) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/coretext/1498169-ctrundelegategetrefcon)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunDelegateGetRefCon(_ runDelegate: CTRunDelegate!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CTRunDelegateGetRefCon(_ runDelegate: CTRunDelegate) -> UnsafeMutablePointer<Void> ``` |

Modified [CTRunDelegateGetWidthCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetwidthcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetWidthCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> CGFloat)> ``` |
| To | ``` typealias CTRunDelegateGetWidthCallback = (UnsafeMutablePointer<Void>) -> CGFloat ``` |

Modified [CTRunDraw(_: CTRun, _: CGContext, _: CFRange)](https://developer.apple.com/documentation/coretext/1509440-ctrundraw)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunDraw(_ run: CTRun!, _ context: CGContext!, _ range: CFRange) ``` |
| To | ``` func CTRunDraw(_ run: CTRun, _ context: CGContext, _ range: CFRange) ``` |

Modified [CTRunGetAdvances(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CGSize>)](https://developer.apple.com/documentation/coretext/1510488-ctrungetadvances)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetAdvances(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGSize>) ``` |
| To | ``` func CTRunGetAdvances(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGSize>) ``` |

Modified [CTRunGetAdvancesPtr(_: CTRun) -> UnsafePointer<CGSize>](https://developer.apple.com/documentation/coretext/1508625-ctrungetadvancesptr)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetAdvancesPtr(_ run: CTRun!) -> UnsafePointer<CGSize> ``` |
| To | ``` func CTRunGetAdvancesPtr(_ run: CTRun) -> UnsafePointer<CGSize> ``` |

Modified [CTRunGetAttributes(_: CTRun) -> CFDictionary](https://developer.apple.com/documentation/coretext/1510805-ctrungetattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetAttributes(_ run: CTRun!) -> CFDictionary! ``` |
| To | ``` func CTRunGetAttributes(_ run: CTRun) -> CFDictionary ``` |

Modified [CTRunGetGlyphCount(_: CTRun) -> CFIndex](https://developer.apple.com/documentation/coretext/1510779-ctrungetglyphcount)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetGlyphCount(_ run: CTRun!) -> CFIndex ``` |
| To | ``` func CTRunGetGlyphCount(_ run: CTRun) -> CFIndex ``` |

Modified [CTRunGetGlyphs(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CGGlyph>)](https://developer.apple.com/documentation/coretext/1509249-ctrungetglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetGlyphs(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGGlyph>) ``` |
| To | ``` func CTRunGetGlyphs(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGGlyph>) ``` |

Modified [CTRunGetGlyphsPtr(_: CTRun) -> UnsafePointer<CGGlyph>](https://developer.apple.com/documentation/coretext/1509952-ctrungetglyphsptr)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetGlyphsPtr(_ run: CTRun!) -> UnsafePointer<CGGlyph> ``` |
| To | ``` func CTRunGetGlyphsPtr(_ run: CTRun) -> UnsafePointer<CGGlyph> ``` |

Modified [CTRunGetImageBounds(_: CTRun, _: CGContext?, _: CFRange) -> CGRect](https://developer.apple.com/documentation/coretext/1509963-ctrungetimagebounds)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetImageBounds(_ run: CTRun!, _ context: CGContext!, _ range: CFRange) -> CGRect ``` |
| To | ``` func CTRunGetImageBounds(_ run: CTRun, _ context: CGContext?, _ range: CFRange) -> CGRect ``` |

Modified [CTRunGetPositions(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CGPoint>)](https://developer.apple.com/documentation/coretext/1508678-ctrungetpositions)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetPositions(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGPoint>) ``` |
| To | ``` func CTRunGetPositions(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGPoint>) ``` |

Modified [CTRunGetPositionsPtr(_: CTRun) -> UnsafePointer<CGPoint>](https://developer.apple.com/documentation/coretext/1510044-ctrungetpositionsptr)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetPositionsPtr(_ run: CTRun!) -> UnsafePointer<CGPoint> ``` |
| To | ``` func CTRunGetPositionsPtr(_ run: CTRun) -> UnsafePointer<CGPoint> ``` |

Modified [CTRunGetStatus(_: CTRun) -> CTRunStatus](https://developer.apple.com/documentation/coretext/1510665-ctrungetstatus)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetStatus(_ run: CTRun!) -> CTRunStatus ``` |
| To | ``` func CTRunGetStatus(_ run: CTRun) -> CTRunStatus ``` |

Modified [CTRunGetStringIndices(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CFIndex>)](https://developer.apple.com/documentation/coretext/1511382-ctrungetstringindices)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetStringIndices(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafeMutablePointer<CFIndex>) ``` |
| To | ``` func CTRunGetStringIndices(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CFIndex>) ``` |

Modified [CTRunGetStringIndicesPtr(_: CTRun) -> UnsafePointer<CFIndex>](https://developer.apple.com/documentation/coretext/1510605-ctrungetstringindicesptr)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetStringIndicesPtr(_ run: CTRun!) -> UnsafePointer<CFIndex> ``` |
| To | ``` func CTRunGetStringIndicesPtr(_ run: CTRun) -> UnsafePointer<CFIndex> ``` |

Modified [CTRunGetStringRange(_: CTRun) -> CFRange](https://developer.apple.com/documentation/coretext/1510020-ctrungetstringrange)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetStringRange(_ run: CTRun!) -> CFRange ``` |
| To | ``` func CTRunGetStringRange(_ run: CTRun) -> CFRange ``` |

Modified [CTRunGetTextMatrix(_: CTRun) -> CGAffineTransform](https://developer.apple.com/documentation/coretext/1508680-ctrungettextmatrix)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetTextMatrix(_ run: CTRun!) -> CGAffineTransform ``` |
| To | ``` func CTRunGetTextMatrix(_ run: CTRun) -> CGAffineTransform ``` |

Modified [CTRunGetTypographicBounds(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CGFloat>, _: UnsafeMutablePointer<CGFloat>, _: UnsafeMutablePointer<CGFloat>) -> Double](https://developer.apple.com/documentation/coretext/1510569-ctrungettypographicbounds)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetTypographicBounds(_ run: CTRun!, _ range: CFRange, _ ascent: UnsafeMutablePointer<CGFloat>, _ descent: UnsafeMutablePointer<CGFloat>, _ leading: UnsafeMutablePointer<CGFloat>) -> Double ``` |
| To | ``` func CTRunGetTypographicBounds(_ run: CTRun, _ range: CFRange, _ ascent: UnsafeMutablePointer<CGFloat>, _ descent: UnsafeMutablePointer<CGFloat>, _ leading: UnsafeMutablePointer<CGFloat>) -> Double ``` |

Modified [CTTextTabCreate(_: CTTextAlignment, _: Double, _: CFDictionary?) -> CTTextTab](https://developer.apple.com/documentation/coretext/1511279-cttexttabcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CTTextTabCreate(_ alignment: CTTextAlignment, _ location: Double, _ options: CFDictionary!) -> CTTextTab! ``` |
| To | ``` func CTTextTabCreate(_ alignment: CTTextAlignment, _ location: Double, _ options: CFDictionary?) -> CTTextTab ``` |

Modified [CTTextTabGetAlignment(_: CTTextTab) -> CTTextAlignment](https://developer.apple.com/documentation/coretext/1509582-cttexttabgetalignment)

|  | Declaration |
| --- | --- |
| From | ``` func CTTextTabGetAlignment(_ tab: CTTextTab!) -> CTTextAlignment ``` |
| To | ``` func CTTextTabGetAlignment(_ tab: CTTextTab) -> CTTextAlignment ``` |

Modified [CTTextTabGetLocation(_: CTTextTab) -> Double](https://developer.apple.com/documentation/coretext/1510746-cttexttabgetlocation)

|  | Declaration |
| --- | --- |
| From | ``` func CTTextTabGetLocation(_ tab: CTTextTab!) -> Double ``` |
| To | ``` func CTTextTabGetLocation(_ tab: CTTextTab) -> Double ``` |

Modified [CTTextTabGetOptions(_: CTTextTab) -> CFDictionary?](https://developer.apple.com/documentation/coretext/1509173-cttexttabgetoptions)

|  | Declaration |
| --- | --- |
| From | ``` func CTTextTabGetOptions(_ tab: CTTextTab!) -> CFDictionary! ``` |
| To | ``` func CTTextTabGetOptions(_ tab: CTTextTab) -> CFDictionary? ``` |

Modified [CTTypesetterCreateLine(_: CTTypesetter, _: CFRange) -> CTLine](https://developer.apple.com/documentation/coretext/1510513-cttypesettercreateline)

|  | Declaration |
| --- | --- |
| From | ``` func CTTypesetterCreateLine(_ typesetter: CTTypesetter!, _ stringRange: CFRange) -> CTLine! ``` |
| To | ``` func CTTypesetterCreateLine(_ typesetter: CTTypesetter, _ stringRange: CFRange) -> CTLine ``` |

Modified [CTTypesetterCreateLineWithOffset(_: CTTypesetter, _: CFRange, _: Double) -> CTLine](https://developer.apple.com/documentation/coretext/1510023-cttypesettercreatelinewithoffset)

|  | Declaration |
| --- | --- |
| From | ``` func CTTypesetterCreateLineWithOffset(_ typesetter: CTTypesetter!, _ stringRange: CFRange, _ offset: Double) -> CTLine! ``` |
| To | ``` func CTTypesetterCreateLineWithOffset(_ typesetter: CTTypesetter, _ stringRange: CFRange, _ offset: Double) -> CTLine ``` |

Modified [CTTypesetterCreateWithAttributedString(_: CFAttributedString) -> CTTypesetter](https://developer.apple.com/documentation/coretext/1511438-cttypesettercreatewithattributed)

|  | Declaration |
| --- | --- |
| From | ``` func CTTypesetterCreateWithAttributedString(_ string: CFAttributedString!) -> CTTypesetter! ``` |
| To | ``` func CTTypesetterCreateWithAttributedString(_ string: CFAttributedString) -> CTTypesetter ``` |

Modified [CTTypesetterCreateWithAttributedStringAndOptions(_: CFAttributedString, _: CFDictionary?) -> CTTypesetter](https://developer.apple.com/documentation/coretext/1510401-cttypesettercreatewithattributed)

|  | Declaration |
| --- | --- |
| From | ``` func CTTypesetterCreateWithAttributedStringAndOptions(_ string: CFAttributedString!, _ options: CFDictionary!) -> CTTypesetter! ``` |
| To | ``` func CTTypesetterCreateWithAttributedStringAndOptions(_ string: CFAttributedString, _ options: CFDictionary?) -> CTTypesetter ``` |

Modified [CTTypesetterSuggestClusterBreak(_: CTTypesetter, _: CFIndex, _: Double) -> CFIndex](https://developer.apple.com/documentation/coretext/1508669-cttypesettersuggestclusterbreak)

|  | Declaration |
| --- | --- |
| From | ``` func CTTypesetterSuggestClusterBreak(_ typesetter: CTTypesetter!, _ startIndex: CFIndex, _ width: Double) -> CFIndex ``` |
| To | ``` func CTTypesetterSuggestClusterBreak(_ typesetter: CTTypesetter, _ startIndex: CFIndex, _ width: Double) -> CFIndex ``` |

Modified [CTTypesetterSuggestClusterBreakWithOffset(_: CTTypesetter, _: CFIndex, _: Double, _: Double) -> CFIndex](https://developer.apple.com/documentation/coretext/1511119-cttypesettersuggestclusterbreakw)

|  | Declaration |
| --- | --- |
| From | ``` func CTTypesetterSuggestClusterBreakWithOffset(_ typesetter: CTTypesetter!, _ startIndex: CFIndex, _ width: Double, _ offset: Double) -> CFIndex ``` |
| To | ``` func CTTypesetterSuggestClusterBreakWithOffset(_ typesetter: CTTypesetter, _ startIndex: CFIndex, _ width: Double, _ offset: Double) -> CFIndex ``` |

Modified [CTTypesetterSuggestLineBreak(_: CTTypesetter, _: CFIndex, _: Double) -> CFIndex](https://developer.apple.com/documentation/coretext/1510080-cttypesettersuggestlinebreak)

|  | Declaration |
| --- | --- |
| From | ``` func CTTypesetterSuggestLineBreak(_ typesetter: CTTypesetter!, _ startIndex: CFIndex, _ width: Double) -> CFIndex ``` |
| To | ``` func CTTypesetterSuggestLineBreak(_ typesetter: CTTypesetter, _ startIndex: CFIndex, _ width: Double) -> CFIndex ``` |

Modified [CTTypesetterSuggestLineBreakWithOffset(_: CTTypesetter, _: CFIndex, _: Double, _: Double) -> CFIndex](https://developer.apple.com/documentation/coretext/1508862-cttypesettersuggestlinebreakwith)

|  | Declaration |
| --- | --- |
| From | ``` func CTTypesetterSuggestLineBreakWithOffset(_ typesetter: CTTypesetter!, _ startIndex: CFIndex, _ width: Double, _ offset: Double) -> CFIndex ``` |
| To | ``` func CTTypesetterSuggestLineBreakWithOffset(_ typesetter: CTTypesetter, _ startIndex: CFIndex, _ width: Double, _ offset: Double) -> CFIndex ``` |

Modified [kCTBaselineClassAttributeName](https://developer.apple.com/documentation/coretext/kctbaselineclassattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineClassAttributeName: CFString! ``` |
| To | ``` let kCTBaselineClassAttributeName: CFString ``` |

Modified [kCTBaselineClassHanging](https://developer.apple.com/documentation/coretext/kctbaselineclasshanging)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineClassHanging: CFString! ``` |
| To | ``` let kCTBaselineClassHanging: CFString ``` |

Modified [kCTBaselineClassIdeographicCentered](https://developer.apple.com/documentation/coretext/kctbaselineclassideographiccentered)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineClassIdeographicCentered: CFString! ``` |
| To | ``` let kCTBaselineClassIdeographicCentered: CFString ``` |

Modified [kCTBaselineClassIdeographicHigh](https://developer.apple.com/documentation/coretext/kctbaselineclassideographichigh)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineClassIdeographicHigh: CFString! ``` |
| To | ``` let kCTBaselineClassIdeographicHigh: CFString ``` |

Modified [kCTBaselineClassIdeographicLow](https://developer.apple.com/documentation/coretext/kctbaselineclassideographiclow)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineClassIdeographicLow: CFString! ``` |
| To | ``` let kCTBaselineClassIdeographicLow: CFString ``` |

Modified [kCTBaselineClassMath](https://developer.apple.com/documentation/coretext/kctbaselineclassmath)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineClassMath: CFString! ``` |
| To | ``` let kCTBaselineClassMath: CFString ``` |

Modified [kCTBaselineClassRoman](https://developer.apple.com/documentation/coretext/kctbaselineclassroman)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineClassRoman: CFString! ``` |
| To | ``` let kCTBaselineClassRoman: CFString ``` |

Modified [kCTBaselineInfoAttributeName](https://developer.apple.com/documentation/coretext/kctbaselineinfoattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineInfoAttributeName: CFString! ``` |
| To | ``` let kCTBaselineInfoAttributeName: CFString ``` |

Modified [kCTBaselineOriginalFont](https://developer.apple.com/documentation/coretext/kctbaselineoriginalfont)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineOriginalFont: CFString! ``` |
| To | ``` let kCTBaselineOriginalFont: CFString ``` |

Modified [kCTBaselineReferenceFont](https://developer.apple.com/documentation/coretext/kctbaselinereferencefont)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineReferenceFont: CFString! ``` |
| To | ``` let kCTBaselineReferenceFont: CFString ``` |

Modified [kCTBaselineReferenceInfoAttributeName](https://developer.apple.com/documentation/coretext/kctbaselinereferenceinfoattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTBaselineReferenceInfoAttributeName: CFString! ``` |
| To | ``` let kCTBaselineReferenceInfoAttributeName: CFString ``` |

Modified [kCTCharacterShapeAttributeName](https://developer.apple.com/documentation/coretext/kctcharactershapeattributename)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCTCharacterShapeAttributeName: CFString! ``` | -- |
| To | ``` let kCTCharacterShapeAttributeName: CFString ``` | iOS 9.0 |

Modified [kCTFontAttributeName](https://developer.apple.com/documentation/coretext/kctfontattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontAttributeName: CFString! ``` |
| To | ``` let kCTFontAttributeName: CFString ``` |

Modified [kCTFontBaselineAdjustAttribute](https://developer.apple.com/documentation/coretext/kctfontbaselineadjustattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontBaselineAdjustAttribute: CFString! ``` |
| To | ``` let kCTFontBaselineAdjustAttribute: CFString ``` |

Modified [kCTFontCascadeListAttribute](https://developer.apple.com/documentation/coretext/kctfontcascadelistattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontCascadeListAttribute: CFString! ``` |
| To | ``` let kCTFontCascadeListAttribute: CFString ``` |

Modified [kCTFontCharacterSetAttribute](https://developer.apple.com/documentation/coretext/kctfontcharactersetattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontCharacterSetAttribute: CFString! ``` |
| To | ``` let kCTFontCharacterSetAttribute: CFString ``` |

Modified [kCTFontCollectionRemoveDuplicatesOption](https://developer.apple.com/documentation/coretext/kctfontcollectionremoveduplicatesoption)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontCollectionRemoveDuplicatesOption: CFString! ``` |
| To | ``` let kCTFontCollectionRemoveDuplicatesOption: CFString ``` |

Modified [kCTFontCopyrightNameKey](https://developer.apple.com/documentation/coretext/kctfontcopyrightnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontCopyrightNameKey: CFString! ``` |
| To | ``` let kCTFontCopyrightNameKey: CFString ``` |

Modified [kCTFontDescriptionNameKey](https://developer.apple.com/documentation/coretext/kctfontdescriptionnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptionNameKey: CFString! ``` |
| To | ``` let kCTFontDescriptionNameKey: CFString ``` |

Modified [kCTFontDescriptorMatchingCurrentAssetSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingcurrentassetsize)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptorMatchingCurrentAssetSize: CFString! ``` |
| To | ``` let kCTFontDescriptorMatchingCurrentAssetSize: CFString ``` |

Modified [kCTFontDescriptorMatchingDescriptors](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptorMatchingDescriptors: CFString! ``` |
| To | ``` let kCTFontDescriptorMatchingDescriptors: CFString ``` |

Modified [kCTFontDescriptorMatchingError](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingerror)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptorMatchingError: CFString! ``` |
| To | ``` let kCTFontDescriptorMatchingError: CFString ``` |

Modified [kCTFontDescriptorMatchingPercentage](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingpercentage)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptorMatchingPercentage: CFString! ``` |
| To | ``` let kCTFontDescriptorMatchingPercentage: CFString ``` |

Modified [kCTFontDescriptorMatchingResult](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingresult)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptorMatchingResult: CFString! ``` |
| To | ``` let kCTFontDescriptorMatchingResult: CFString ``` |

Modified [kCTFontDescriptorMatchingSourceDescriptor](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingsourcedescriptor)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptorMatchingSourceDescriptor: CFString! ``` |
| To | ``` let kCTFontDescriptorMatchingSourceDescriptor: CFString ``` |

Modified [kCTFontDescriptorMatchingTotalAssetSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingtotalassetsize)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptorMatchingTotalAssetSize: CFString! ``` |
| To | ``` let kCTFontDescriptorMatchingTotalAssetSize: CFString ``` |

Modified [kCTFontDescriptorMatchingTotalDownloadedSize](https://developer.apple.com/documentation/coretext/kctfontdescriptormatchingtotaldownloadedsize)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDescriptorMatchingTotalDownloadedSize: CFString! ``` |
| To | ``` let kCTFontDescriptorMatchingTotalDownloadedSize: CFString ``` |

Modified [kCTFontDesignerNameKey](https://developer.apple.com/documentation/coretext/kctfontdesignernamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDesignerNameKey: CFString! ``` |
| To | ``` let kCTFontDesignerNameKey: CFString ``` |

Modified [kCTFontDesignerURLNameKey](https://developer.apple.com/documentation/coretext/kctfontdesignerurlnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDesignerURLNameKey: CFString! ``` |
| To | ``` let kCTFontDesignerURLNameKey: CFString ``` |

Modified [kCTFontDisplayNameAttribute](https://developer.apple.com/documentation/coretext/kctfontdisplaynameattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDisplayNameAttribute: CFString! ``` |
| To | ``` let kCTFontDisplayNameAttribute: CFString ``` |

Modified [kCTFontDownloadableAttribute](https://developer.apple.com/documentation/coretext/kctfontdownloadableattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDownloadableAttribute: CFString! ``` |
| To | ``` let kCTFontDownloadableAttribute: CFString ``` |

Modified [kCTFontDownloadedAttribute](https://developer.apple.com/documentation/coretext/kctfontdownloadedattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontDownloadedAttribute: CFString! ``` |
| To | ``` let kCTFontDownloadedAttribute: CFString ``` |

Modified [kCTFontEnabledAttribute](https://developer.apple.com/documentation/coretext/kctfontenabledattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontEnabledAttribute: CFString! ``` |
| To | ``` let kCTFontEnabledAttribute: CFString ``` |

Modified [kCTFontFamilyNameAttribute](https://developer.apple.com/documentation/coretext/kctfontfamilynameattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFamilyNameAttribute: CFString! ``` |
| To | ``` let kCTFontFamilyNameAttribute: CFString ``` |

Modified [kCTFontFamilyNameKey](https://developer.apple.com/documentation/coretext/kctfontfamilynamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFamilyNameKey: CFString! ``` |
| To | ``` let kCTFontFamilyNameKey: CFString ``` |

Modified [kCTFontFeaturesAttribute](https://developer.apple.com/documentation/coretext/kctfontfeaturesattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeaturesAttribute: CFString! ``` |
| To | ``` let kCTFontFeaturesAttribute: CFString ``` |

Modified [kCTFontFeatureSelectorDefaultKey](https://developer.apple.com/documentation/coretext/kctfontfeatureselectordefaultkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureSelectorDefaultKey: CFString! ``` |
| To | ``` let kCTFontFeatureSelectorDefaultKey: CFString ``` |

Modified [kCTFontFeatureSelectorIdentifierKey](https://developer.apple.com/documentation/coretext/kctfontfeatureselectoridentifierkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureSelectorIdentifierKey: CFString! ``` |
| To | ``` let kCTFontFeatureSelectorIdentifierKey: CFString ``` |

Modified [kCTFontFeatureSelectorNameKey](https://developer.apple.com/documentation/coretext/kctfontfeatureselectornamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureSelectorNameKey: CFString! ``` |
| To | ``` let kCTFontFeatureSelectorNameKey: CFString ``` |

Modified [kCTFontFeatureSelectorSettingKey](https://developer.apple.com/documentation/coretext/kctfontfeatureselectorsettingkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureSelectorSettingKey: CFString! ``` |
| To | ``` let kCTFontFeatureSelectorSettingKey: CFString ``` |

Modified [kCTFontFeatureSettingsAttribute](https://developer.apple.com/documentation/coretext/kctfontfeaturesettingsattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureSettingsAttribute: CFString! ``` |
| To | ``` let kCTFontFeatureSettingsAttribute: CFString ``` |

Modified [kCTFontFeatureTypeExclusiveKey](https://developer.apple.com/documentation/coretext/kctfontfeaturetypeexclusivekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureTypeExclusiveKey: CFString! ``` |
| To | ``` let kCTFontFeatureTypeExclusiveKey: CFString ``` |

Modified [kCTFontFeatureTypeIdentifierKey](https://developer.apple.com/documentation/coretext/kctfontfeaturetypeidentifierkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureTypeIdentifierKey: CFString! ``` |
| To | ``` let kCTFontFeatureTypeIdentifierKey: CFString ``` |

Modified [kCTFontFeatureTypeNameKey](https://developer.apple.com/documentation/coretext/kctfontfeaturetypenamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureTypeNameKey: CFString! ``` |
| To | ``` let kCTFontFeatureTypeNameKey: CFString ``` |

Modified [kCTFontFeatureTypeSelectorsKey](https://developer.apple.com/documentation/coretext/kctfontfeaturetypeselectorskey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFeatureTypeSelectorsKey: CFString! ``` |
| To | ``` let kCTFontFeatureTypeSelectorsKey: CFString ``` |

Modified [kCTFontFixedAdvanceAttribute](https://developer.apple.com/documentation/coretext/kctfontfixedadvanceattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFixedAdvanceAttribute: CFString! ``` |
| To | ``` let kCTFontFixedAdvanceAttribute: CFString ``` |

Modified [kCTFontFormatAttribute](https://developer.apple.com/documentation/coretext/kctfontformatattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFormatAttribute: CFString! ``` |
| To | ``` let kCTFontFormatAttribute: CFString ``` |

Modified [kCTFontFullNameKey](https://developer.apple.com/documentation/coretext/kctfontfullnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontFullNameKey: CFString! ``` |
| To | ``` let kCTFontFullNameKey: CFString ``` |

Modified [kCTFontLanguagesAttribute](https://developer.apple.com/documentation/coretext/kctfontlanguagesattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontLanguagesAttribute: CFString! ``` |
| To | ``` let kCTFontLanguagesAttribute: CFString ``` |

Modified [kCTFontLicenseNameKey](https://developer.apple.com/documentation/coretext/kctfontlicensenamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontLicenseNameKey: CFString! ``` |
| To | ``` let kCTFontLicenseNameKey: CFString ``` |

Modified [kCTFontLicenseURLNameKey](https://developer.apple.com/documentation/coretext/kctfontlicenseurlnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontLicenseURLNameKey: CFString! ``` |
| To | ``` let kCTFontLicenseURLNameKey: CFString ``` |

Modified [kCTFontMacintoshEncodingsAttribute](https://developer.apple.com/documentation/coretext/kctfontmacintoshencodingsattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontMacintoshEncodingsAttribute: CFString! ``` |
| To | ``` let kCTFontMacintoshEncodingsAttribute: CFString ``` |

Modified [kCTFontManagerErrorDomain](https://developer.apple.com/documentation/coretext/kctfontmanagererrordomain)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontManagerErrorDomain: CFString! ``` |
| To | ``` let kCTFontManagerErrorDomain: CFString ``` |

Modified [kCTFontManagerErrorFontURLsKey](https://developer.apple.com/documentation/coretext/kctfontmanagererrorfonturlskey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontManagerErrorFontURLsKey: CFString! ``` |
| To | ``` let kCTFontManagerErrorFontURLsKey: CFString ``` |

Modified [kCTFontManagerRegisteredFontsChangedNotification](https://developer.apple.com/documentation/coretext/kctfontmanagerregisteredfontschangednotification)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontManagerRegisteredFontsChangedNotification: CFString! ``` |
| To | ``` let kCTFontManagerRegisteredFontsChangedNotification: CFString ``` |

Modified [kCTFontManufacturerNameKey](https://developer.apple.com/documentation/coretext/kctfontmanufacturernamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontManufacturerNameKey: CFString! ``` |
| To | ``` let kCTFontManufacturerNameKey: CFString ``` |

Modified [kCTFontMatrixAttribute](https://developer.apple.com/documentation/coretext/kctfontmatrixattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontMatrixAttribute: CFString! ``` |
| To | ``` let kCTFontMatrixAttribute: CFString ``` |

Modified [kCTFontNameAttribute](https://developer.apple.com/documentation/coretext/kctfontnameattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontNameAttribute: CFString! ``` |
| To | ``` let kCTFontNameAttribute: CFString ``` |

Modified [kCTFontOpenTypeFeatureTag](https://developer.apple.com/documentation/coretext/kctfontopentypefeaturetag)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontOpenTypeFeatureTag: CFString! ``` |
| To | ``` let kCTFontOpenTypeFeatureTag: CFString ``` |

Modified [kCTFontOpenTypeFeatureValue](https://developer.apple.com/documentation/coretext/kctfontopentypefeaturevalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontOpenTypeFeatureValue: CFString! ``` |
| To | ``` let kCTFontOpenTypeFeatureValue: CFString ``` |

Modified [kCTFontOrientationAttribute](https://developer.apple.com/documentation/coretext/kctfontorientationattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontOrientationAttribute: CFString! ``` |
| To | ``` let kCTFontOrientationAttribute: CFString ``` |

Modified [kCTFontPostScriptCIDNameKey](https://developer.apple.com/documentation/coretext/kctfontpostscriptcidnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontPostScriptCIDNameKey: CFString! ``` |
| To | ``` let kCTFontPostScriptCIDNameKey: CFString ``` |

Modified [kCTFontPostScriptNameKey](https://developer.apple.com/documentation/coretext/kctfontpostscriptnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontPostScriptNameKey: CFString! ``` |
| To | ``` let kCTFontPostScriptNameKey: CFString ``` |

Modified [kCTFontPriorityAttribute](https://developer.apple.com/documentation/coretext/kctfontpriorityattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontPriorityAttribute: CFString! ``` |
| To | ``` let kCTFontPriorityAttribute: CFString ``` |

Modified [kCTFontRegistrationScopeAttribute](https://developer.apple.com/documentation/coretext/kctfontregistrationscopeattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontRegistrationScopeAttribute: CFString! ``` |
| To | ``` let kCTFontRegistrationScopeAttribute: CFString ``` |

Modified [kCTFontSampleTextNameKey](https://developer.apple.com/documentation/coretext/kctfontsampletextnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontSampleTextNameKey: CFString! ``` |
| To | ``` let kCTFontSampleTextNameKey: CFString ``` |

Modified [kCTFontSizeAttribute](https://developer.apple.com/documentation/coretext/kctfontsizeattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontSizeAttribute: CFString! ``` |
| To | ``` let kCTFontSizeAttribute: CFString ``` |

Modified [kCTFontSlantTrait](https://developer.apple.com/documentation/coretext/kctfontslanttrait)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontSlantTrait: CFString! ``` |
| To | ``` let kCTFontSlantTrait: CFString ``` |

Modified [kCTFontStyleNameAttribute](https://developer.apple.com/documentation/coretext/kctfontstylenameattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontStyleNameAttribute: CFString! ``` |
| To | ``` let kCTFontStyleNameAttribute: CFString ``` |

Modified [kCTFontStyleNameKey](https://developer.apple.com/documentation/coretext/kctfontstylenamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontStyleNameKey: CFString! ``` |
| To | ``` let kCTFontStyleNameKey: CFString ``` |

Modified [kCTFontSubFamilyNameKey](https://developer.apple.com/documentation/coretext/kctfontsubfamilynamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontSubFamilyNameKey: CFString! ``` |
| To | ``` let kCTFontSubFamilyNameKey: CFString ``` |

Modified [kCTFontSymbolicTrait](https://developer.apple.com/documentation/coretext/kctfontsymbolictrait)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontSymbolicTrait: CFString! ``` |
| To | ``` let kCTFontSymbolicTrait: CFString ``` |

Modified [kCTFontTrademarkNameKey](https://developer.apple.com/documentation/coretext/kctfonttrademarknamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontTrademarkNameKey: CFString! ``` |
| To | ``` let kCTFontTrademarkNameKey: CFString ``` |

Modified [kCTFontTraitsAttribute](https://developer.apple.com/documentation/coretext/kctfonttraitsattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontTraitsAttribute: CFString! ``` |
| To | ``` let kCTFontTraitsAttribute: CFString ``` |

Modified [kCTFontUniqueNameKey](https://developer.apple.com/documentation/coretext/kctfontuniquenamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontUniqueNameKey: CFString! ``` |
| To | ``` let kCTFontUniqueNameKey: CFString ``` |

Modified [kCTFontURLAttribute](https://developer.apple.com/documentation/coretext/kctfonturlattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontURLAttribute: CFString! ``` |
| To | ``` let kCTFontURLAttribute: CFString ``` |

Modified [kCTFontVariationAttribute](https://developer.apple.com/documentation/coretext/kctfontvariationattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontVariationAttribute: CFString! ``` |
| To | ``` let kCTFontVariationAttribute: CFString ``` |

Modified [kCTFontVariationAxisDefaultValueKey](https://developer.apple.com/documentation/coretext/kctfontvariationaxisdefaultvaluekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontVariationAxisDefaultValueKey: CFString! ``` |
| To | ``` let kCTFontVariationAxisDefaultValueKey: CFString ``` |

Modified [kCTFontVariationAxisIdentifierKey](https://developer.apple.com/documentation/coretext/kctfontvariationaxisidentifierkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontVariationAxisIdentifierKey: CFString! ``` |
| To | ``` let kCTFontVariationAxisIdentifierKey: CFString ``` |

Modified [kCTFontVariationAxisMaximumValueKey](https://developer.apple.com/documentation/coretext/kctfontvariationaxismaximumvaluekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontVariationAxisMaximumValueKey: CFString! ``` |
| To | ``` let kCTFontVariationAxisMaximumValueKey: CFString ``` |

Modified [kCTFontVariationAxisMinimumValueKey](https://developer.apple.com/documentation/coretext/kctfontvariationaxisminimumvaluekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontVariationAxisMinimumValueKey: CFString! ``` |
| To | ``` let kCTFontVariationAxisMinimumValueKey: CFString ``` |

Modified [kCTFontVariationAxisNameKey](https://developer.apple.com/documentation/coretext/kctfontvariationaxisnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontVariationAxisNameKey: CFString! ``` |
| To | ``` let kCTFontVariationAxisNameKey: CFString ``` |

Modified [kCTFontVendorURLNameKey](https://developer.apple.com/documentation/coretext/kctfontvendorurlnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontVendorURLNameKey: CFString! ``` |
| To | ``` let kCTFontVendorURLNameKey: CFString ``` |

Modified [kCTFontVersionNameKey](https://developer.apple.com/documentation/coretext/kctfontversionnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontVersionNameKey: CFString! ``` |
| To | ``` let kCTFontVersionNameKey: CFString ``` |

Modified [kCTFontWeightTrait](https://developer.apple.com/documentation/coretext/kctfontweighttrait)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontWeightTrait: CFString! ``` |
| To | ``` let kCTFontWeightTrait: CFString ``` |

Modified [kCTFontWidthTrait](https://developer.apple.com/documentation/coretext/kctfontwidthtrait)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFontWidthTrait: CFString! ``` |
| To | ``` let kCTFontWidthTrait: CFString ``` |

Modified [kCTForegroundColorAttributeName](https://developer.apple.com/documentation/coretext/kctforegroundcolorattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTForegroundColorAttributeName: CFString! ``` |
| To | ``` let kCTForegroundColorAttributeName: CFString ``` |

Modified [kCTForegroundColorFromContextAttributeName](https://developer.apple.com/documentation/coretext/kctforegroundcolorfromcontextattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTForegroundColorFromContextAttributeName: CFString! ``` |
| To | ``` let kCTForegroundColorFromContextAttributeName: CFString ``` |

Modified [kCTFrameClippingPathsAttributeName](https://developer.apple.com/documentation/coretext/kctframeclippingpathsattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFrameClippingPathsAttributeName: CFString! ``` |
| To | ``` let kCTFrameClippingPathsAttributeName: CFString ``` |

Modified [kCTFramePathClippingPathAttributeName](https://developer.apple.com/documentation/coretext/kctframepathclippingpathattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFramePathClippingPathAttributeName: CFString! ``` |
| To | ``` let kCTFramePathClippingPathAttributeName: CFString ``` |

Modified [kCTFramePathFillRuleAttributeName](https://developer.apple.com/documentation/coretext/kctframepathfillruleattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFramePathFillRuleAttributeName: CFString! ``` |
| To | ``` let kCTFramePathFillRuleAttributeName: CFString ``` |

Modified [kCTFramePathWidthAttributeName](https://developer.apple.com/documentation/coretext/kctframepathwidthattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFramePathWidthAttributeName: CFString! ``` |
| To | ``` let kCTFramePathWidthAttributeName: CFString ``` |

Modified [kCTFrameProgressionAttributeName](https://developer.apple.com/documentation/coretext/kctframeprogressionattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTFrameProgressionAttributeName: CFString! ``` |
| To | ``` let kCTFrameProgressionAttributeName: CFString ``` |

Modified [kCTGlyphInfoAttributeName](https://developer.apple.com/documentation/coretext/kctglyphinfoattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTGlyphInfoAttributeName: CFString! ``` |
| To | ``` let kCTGlyphInfoAttributeName: CFString ``` |

Modified [kCTKernAttributeName](https://developer.apple.com/documentation/coretext/kctkernattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTKernAttributeName: CFString! ``` |
| To | ``` let kCTKernAttributeName: CFString ``` |

Modified [kCTLanguageAttributeName](https://developer.apple.com/documentation/coretext/kctlanguageattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTLanguageAttributeName: CFString! ``` |
| To | ``` let kCTLanguageAttributeName: CFString ``` |

Modified [kCTLigatureAttributeName](https://developer.apple.com/documentation/coretext/kctligatureattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTLigatureAttributeName: CFString! ``` |
| To | ``` let kCTLigatureAttributeName: CFString ``` |

Modified [kCTParagraphStyleAttributeName](https://developer.apple.com/documentation/coretext/kctparagraphstyleattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTParagraphStyleAttributeName: CFString! ``` |
| To | ``` let kCTParagraphStyleAttributeName: CFString ``` |

Modified [kCTRubyAnnotationAttributeName](https://developer.apple.com/documentation/coretext/kctrubyannotationattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTRubyAnnotationAttributeName: CFString! ``` |
| To | ``` let kCTRubyAnnotationAttributeName: CFString ``` |

Modified [kCTRunDelegateAttributeName](https://developer.apple.com/documentation/coretext/kctrundelegateattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTRunDelegateAttributeName: CFString! ``` |
| To | ``` let kCTRunDelegateAttributeName: CFString ``` |

Modified [kCTStrokeColorAttributeName](https://developer.apple.com/documentation/coretext/kctstrokecolorattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTStrokeColorAttributeName: CFString! ``` |
| To | ``` let kCTStrokeColorAttributeName: CFString ``` |

Modified [kCTStrokeWidthAttributeName](https://developer.apple.com/documentation/coretext/kctstrokewidthattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTStrokeWidthAttributeName: CFString! ``` |
| To | ``` let kCTStrokeWidthAttributeName: CFString ``` |

Modified [kCTSuperscriptAttributeName](https://developer.apple.com/documentation/coretext/kctsuperscriptattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTSuperscriptAttributeName: CFString! ``` |
| To | ``` let kCTSuperscriptAttributeName: CFString ``` |

Modified [kCTTabColumnTerminatorsAttributeName](https://developer.apple.com/documentation/coretext/kcttabcolumnterminatorsattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTTabColumnTerminatorsAttributeName: CFString! ``` |
| To | ``` let kCTTabColumnTerminatorsAttributeName: CFString ``` |

Modified [kCTTypesetterOptionForcedEmbeddingLevel](https://developer.apple.com/documentation/coretext/kcttypesetteroptionforcedembeddinglevel)

|  | Declaration |
| --- | --- |
| From | ``` let kCTTypesetterOptionForcedEmbeddingLevel: CFString! ``` |
| To | ``` let kCTTypesetterOptionForcedEmbeddingLevel: CFString ``` |

Modified [kCTUnderlineColorAttributeName](https://developer.apple.com/documentation/coretext/kctunderlinecolorattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTUnderlineColorAttributeName: CFString! ``` |
| To | ``` let kCTUnderlineColorAttributeName: CFString ``` |

Modified [kCTUnderlineStyleAttributeName](https://developer.apple.com/documentation/coretext/kctunderlinestyleattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTUnderlineStyleAttributeName: CFString! ``` |
| To | ``` let kCTUnderlineStyleAttributeName: CFString ``` |

Modified [kCTVerticalFormsAttributeName](https://developer.apple.com/documentation/coretext/kctverticalformsattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTVerticalFormsAttributeName: CFString! ``` |
| To | ``` let kCTVerticalFormsAttributeName: CFString ``` |

Modified [kCTWritingDirectionAttributeName](https://developer.apple.com/documentation/coretext/kctwritingdirectionattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kCTWritingDirectionAttributeName: CFString! ``` |
| To | ``` let kCTWritingDirectionAttributeName: CFString ``` |

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
