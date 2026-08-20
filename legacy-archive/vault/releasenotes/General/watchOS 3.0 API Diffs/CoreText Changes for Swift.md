---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Swift/CoreText.html
archived_at: '2026-07-18T02:58:20.808261Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# CoreText Changes for Swift

### CoreText

Removed [CTFontOptions.Default](https://developer.apple.com/documentation/coretext/ctfontoptions/kctfontoptionsdefault)Removed [CTFontStylisticClass.ClassUnknown](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassunknown)Removed [CTFontStylisticClass.UnknownClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontunknownclass)Removed [CTFontTableOptions.noOptions](https://developer.apple.com/documentation/coretext/ctfonttableoptions/kctfonttableoptionnooptions)Removed [CTRunStatus.NoStatus](https://developer.apple.com/documentation/coretext/ctrunstatus/kctrunstatusnostatus)Removed [CTUnderlineStyle.None](https://developer.apple.com/documentation/coretext/ctunderlinestyle/kctunderlinestylenone)Removed KerxIndexArrayHeader.glyphCountRemoved KerxIndexArrayHeader.init(glyphCount: UInt16, kernValueCount: UInt16, leftClassCount: UInt16, rightClassCount: UInt16, flags: UInt16, kernValue: (Int16), leftClass: (UInt16), rightClass: (UInt16), kernIndex: (UInt16))Removed KerxIndexArrayHeader.kernIndexRemoved KerxIndexArrayHeader.kernValueRemoved KerxIndexArrayHeader.kernValueCountRemoved KerxIndexArrayHeader.leftClassRemoved KerxIndexArrayHeader.leftClassCountRemoved KerxIndexArrayHeader.rightClassRemoved KerxIndexArrayHeader.rightClassCountRemoved KerxSubtableHeader.init(length: UInt32, stInfo: KerxSubtableCoverage, tupleIndex: UInt32, fsHeader: KerxFormatSpecificHeader)Removed KerxSubtableHeader.tupleIndexAdded KerxIndexArrayHeader.columnCountAdded KerxIndexArrayHeader.columnIndexTableOffsetAdded KerxIndexArrayHeader.init(flags: UInt32, rowCount: UInt16, columnCount: UInt16, rowIndexTableOffset: UInt32, columnIndexTableOffset: UInt32, kerningArrayOffset: UInt32, kerningVectorOffset: UInt32)Added KerxIndexArrayHeader.kerningArrayOffsetAdded KerxIndexArrayHeader.kerningVectorOffsetAdded KerxIndexArrayHeader.rowCountAdded KerxIndexArrayHeader.rowIndexTableOffsetAdded KerxSubtableHeader.init(length: UInt32, stInfo: KerxSubtableCoverage, tupleCount: UInt32, fsHeader: KerxFormatSpecificHeader)Added KerxSubtableHeader.tupleCountAdded SFNTLookupFormatSpecificHeader.init(vector: SFNTLookupVectorHeader)Added SFNTLookupFormatSpecificHeader.vectorAdded [SFNTLookupVectorHeader [struct]](https://developer.apple.com/documentation/coretext/sfntlookupvectorheader)Added [SFNTLookupVectorHeader.count](https://developer.apple.com/documentation/coretext/sfntlookupvectorheader/1642011-count)Added [SFNTLookupVectorHeader.firstGlyph](https://developer.apple.com/documentation/coretext/sfntlookupvectorheader/1642005-firstglyph)Added [SFNTLookupVectorHeader.init()](https://developer.apple.com/documentation/coretext/sfntlookupvectorheader/1642030-init)Added [SFNTLookupVectorHeader.init(valueSize: UInt16, firstGlyph: UInt16, count: UInt16, values: (UInt8))](https://developer.apple.com/documentation/coretext/sfntlookupvectorheader/1642009-init)Added [SFNTLookupVectorHeader.values](https://developer.apple.com/documentation/coretext/sfntlookupvectorheader/1642004-values)Added [SFNTLookupVectorHeader.valueSize](https://developer.apple.com/documentation/coretext/sfntlookupvectorheader/1642012-valuesize)Added [CTFontManagerCopyAvailableFontFamilyNames() -> CFArray](https://developer.apple.com/documentation/coretext/1499494-ctfontmanagercopyavailablefontfa)Added [CTFontManagerCopyAvailablePostScriptNames() -> CFArray](https://developer.apple.com/documentation/coretext/1499516-ctfontmanagercopyavailablepostsc)Added [CTRubyAnnotationCreateWithAttributes(_: CTRubyAlignment, _: CTRubyOverhang, _: CTRubyPosition, _: CFString, _: CFDictionary) -> CTRubyAnnotation](https://developer.apple.com/documentation/coretext/1642000-ctrubyannotationcreatewithattrib)Added [kCTBackgroundColorAttributeName](https://developer.apple.com/documentation/coretext/kctbackgroundcolorattributename)Added [kCTHorizontalInVerticalFormsAttributeName](https://developer.apple.com/documentation/coretext/kcthorizontalinverticalformsattributename)Added [kCTRubyAnnotationScaleToFitAttributeName](https://developer.apple.com/documentation/coretext/kctrubyannotationscaletofitattributename)Added [kCTRubyAnnotationSizeFactorAttributeName](https://developer.apple.com/documentation/coretext/kctrubyannotationsizefactorattributename)Added [kCTVersionNumber10_12](https://developer.apple.com/documentation/coretext/kctversionnumber10_12)Added [kKERXValuesAreLong](https://developer.apple.com/documentation/coretext/1643710-anonymous/kkerxvaluesarelong)Added kSFNTLookupVectorModified [CTCharacterCollection [enum]](https://developer.apple.com/documentation/coretext/ctcharactercollection)

|  | Declaration |
| --- | --- |
| From | ``` enum CTCharacterCollection : UInt16 {     case IdentityMapping     case AdobeCNS1     case AdobeGB1     case AdobeJapan1     case AdobeJapan2     case AdobeKorea1     static var kCTIdentityMappingCharacterCollection: CTCharacterCollection { get }     static var kCTAdobeCNS1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeGB1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeJapan1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeJapan2CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeKorea1CharacterCollection: CTCharacterCollection { get } } ``` |
| To | ``` enum CTCharacterCollection : UInt16 {     case identityMapping     case adobeCNS1     case adobeGB1     case adobeJapan1     case adobeJapan2     case adobeKorea1     static var kCTIdentityMappingCharacterCollection: CTCharacterCollection { get }     static var kCTAdobeCNS1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeGB1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeJapan1CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeJapan2CharacterCollection: CTCharacterCollection { get }     static var kCTAdobeKorea1CharacterCollection: CTCharacterCollection { get } } ``` |

Modified [CTCharacterCollection.adobeCNS1](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctcharactercollectionadobecns1)

|  | Declaration |
| --- | --- |
| From | ``` case AdobeCNS1 ``` |
| To | ``` case adobeCNS1 ``` |

Modified [CTCharacterCollection.adobeGB1](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctcharactercollectionadobegb1)

|  | Declaration |
| --- | --- |
| From | ``` case AdobeGB1 ``` |
| To | ``` case adobeGB1 ``` |

Modified [CTCharacterCollection.adobeJapan1](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobejapan1)

|  | Declaration |
| --- | --- |
| From | ``` case AdobeJapan1 ``` |
| To | ``` case adobeJapan1 ``` |

Modified [CTCharacterCollection.adobeJapan2](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobejapan2)

|  | Declaration |
| --- | --- |
| From | ``` case AdobeJapan2 ``` |
| To | ``` case adobeJapan2 ``` |

Modified [CTCharacterCollection.adobeKorea1](https://developer.apple.com/documentation/coretext/ctcharactercollection/adobekorea1)

|  | Declaration |
| --- | --- |
| From | ``` case AdobeKorea1 ``` |
| To | ``` case adobeKorea1 ``` |

Modified [CTCharacterCollection.identityMapping](https://developer.apple.com/documentation/coretext/ctcharactercollection/kctcharactercollectionidentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` case IdentityMapping ``` |
| To | ``` case identityMapping ``` |

Modified [CTFontDescriptorMatchingState [enum]](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFontDescriptorMatchingState : UInt32 {     case DidBegin     case DidFinish     case WillBeginQuerying     case Stalled     case WillBeginDownloading     case Downloading     case DidFinishDownloading     case DidMatch     case DidFailWithError } ``` |
| To | ``` enum CTFontDescriptorMatchingState : UInt32 {     case didBegin     case didFinish     case willBeginQuerying     case stalled     case willBeginDownloading     case downloading     case didFinishDownloading     case didMatch     case didFailWithError } ``` |

Modified [CTFontDescriptorMatchingState.didBegin](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/didbegin)

|  | Declaration |
| --- | --- |
| From | ``` case DidBegin ``` |
| To | ``` case didBegin ``` |

Modified [CTFontDescriptorMatchingState.didFailWithError](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfailwitherror)

|  | Declaration |
| --- | --- |
| From | ``` case DidFailWithError ``` |
| To | ``` case didFailWithError ``` |

Modified [CTFontDescriptorMatchingState.didFinish](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfinish)

|  | Declaration |
| --- | --- |
| From | ``` case DidFinish ``` |
| To | ``` case didFinish ``` |

Modified [CTFontDescriptorMatchingState.didFinishDownloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidfinishdownloading)

|  | Declaration |
| --- | --- |
| From | ``` case DidFinishDownloading ``` |
| To | ``` case didFinishDownloading ``` |

Modified [CTFontDescriptorMatchingState.didMatch](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingdidmatch)

|  | Declaration |
| --- | --- |
| From | ``` case DidMatch ``` |
| To | ``` case didMatch ``` |

Modified [CTFontDescriptorMatchingState.downloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/downloading)

|  | Declaration |
| --- | --- |
| From | ``` case Downloading ``` |
| To | ``` case downloading ``` |

Modified [CTFontDescriptorMatchingState.stalled](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingstalled)

|  | Declaration |
| --- | --- |
| From | ``` case Stalled ``` |
| To | ``` case stalled ``` |

Modified [CTFontDescriptorMatchingState.willBeginDownloading](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingwillbegindownloading)

|  | Declaration |
| --- | --- |
| From | ``` case WillBeginDownloading ``` |
| To | ``` case willBeginDownloading ``` |

Modified [CTFontDescriptorMatchingState.willBeginQuerying](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/kctfontdescriptormatchingwillbeginquerying)

|  | Declaration |
| --- | --- |
| From | ``` case WillBeginQuerying ``` |
| To | ``` case willBeginQuerying ``` |

Modified [CTFontFormat [enum]](https://developer.apple.com/documentation/coretext/ctfontformat)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFontFormat : UInt32 {     case Unrecognized     case OpenTypePostScript     case OpenTypeTrueType     case TrueType     case PostScript     case Bitmap } ``` |
| To | ``` enum CTFontFormat : UInt32 {     case unrecognized     case openTypePostScript     case openTypeTrueType     case trueType     case postScript     case bitmap } ``` |

Modified [CTFontFormat.bitmap](https://developer.apple.com/documentation/coretext/ctfontformat/kctfontformatbitmap)

|  | Declaration |
| --- | --- |
| From | ``` case Bitmap ``` |
| To | ``` case bitmap ``` |

Modified [CTFontFormat.openTypePostScript](https://developer.apple.com/documentation/coretext/ctfontformat/kctfontformatopentypepostscript)

|  | Declaration |
| --- | --- |
| From | ``` case OpenTypePostScript ``` |
| To | ``` case openTypePostScript ``` |

Modified [CTFontFormat.openTypeTrueType](https://developer.apple.com/documentation/coretext/ctfontformat/kctfontformatopentypetruetype)

|  | Declaration |
| --- | --- |
| From | ``` case OpenTypeTrueType ``` |
| To | ``` case openTypeTrueType ``` |

Modified [CTFontFormat.postScript](https://developer.apple.com/documentation/coretext/ctfontformat/kctfontformatpostscript)

|  | Declaration |
| --- | --- |
| From | ``` case PostScript ``` |
| To | ``` case postScript ``` |

Modified [CTFontFormat.trueType](https://developer.apple.com/documentation/coretext/ctfontformat/kctfontformattruetype)

|  | Declaration |
| --- | --- |
| From | ``` case TrueType ``` |
| To | ``` case trueType ``` |

Modified [CTFontFormat.unrecognized](https://developer.apple.com/documentation/coretext/ctfontformat/unrecognized)

|  | Declaration |
| --- | --- |
| From | ``` case Unrecognized ``` |
| To | ``` case unrecognized ``` |

Modified [CTFontManagerAutoActivationSetting [enum]](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFontManagerAutoActivationSetting : UInt32 {     case Default     case Disabled     case Enabled     case PromptUser } ``` |
| To | ``` enum CTFontManagerAutoActivationSetting : UInt32 {     case `default`     case disabled     case enabled     case promptUser } ``` |

Modified [CTFontManagerAutoActivationSetting.default](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting/default)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [CTFontManagerAutoActivationSetting.disabled](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting/disabled)

|  | Declaration |
| --- | --- |
| From | ``` case Disabled ``` |
| To | ``` case disabled ``` |

Modified [CTFontManagerAutoActivationSetting.enabled](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting/kctfontmanagerautoactivationenabled)

|  | Declaration |
| --- | --- |
| From | ``` case Enabled ``` |
| To | ``` case enabled ``` |

Modified [CTFontManagerAutoActivationSetting.promptUser](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting/promptuser)

|  | Declaration |
| --- | --- |
| From | ``` case PromptUser ``` |
| To | ``` case promptUser ``` |

Modified [CTFontManagerError [enum]](https://developer.apple.com/documentation/coretext/ctfontmanagererror)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFontManagerError : CFIndex {     case FileNotFound     case InsufficientPermissions     case UnrecognizedFormat     case InvalidFontData     case AlreadyRegistered     case NotRegistered     case InUse     case SystemRequired } ``` |
| To | ``` enum CTFontManagerError : CFIndex {     case fileNotFound     case insufficientPermissions     case unrecognizedFormat     case invalidFontData     case alreadyRegistered     case notRegistered     case inUse     case systemRequired } ``` |

Modified [CTFontManagerError.alreadyRegistered](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererroralreadyregistered)

|  | Declaration |
| --- | --- |
| From | ``` case AlreadyRegistered ``` |
| To | ``` case alreadyRegistered ``` |

Modified [CTFontManagerError.fileNotFound](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererrorfilenotfound)

|  | Declaration |
| --- | --- |
| From | ``` case FileNotFound ``` |
| To | ``` case fileNotFound ``` |

Modified [CTFontManagerError.insufficientPermissions](https://developer.apple.com/documentation/coretext/ctfontmanagererror/insufficientpermissions)

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientPermissions ``` |
| To | ``` case insufficientPermissions ``` |

Modified [CTFontManagerError.inUse](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererrorinuse)

|  | Declaration |
| --- | --- |
| From | ``` case InUse ``` |
| To | ``` case inUse ``` |

Modified [CTFontManagerError.invalidFontData](https://developer.apple.com/documentation/coretext/ctfontmanagererror/invalidfontdata)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidFontData ``` |
| To | ``` case invalidFontData ``` |

Modified [CTFontManagerError.notRegistered](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererrornotregistered)

|  | Declaration |
| --- | --- |
| From | ``` case NotRegistered ``` |
| To | ``` case notRegistered ``` |

Modified [CTFontManagerError.systemRequired](https://developer.apple.com/documentation/coretext/ctfontmanagererror/systemrequired)

|  | Declaration |
| --- | --- |
| From | ``` case SystemRequired ``` |
| To | ``` case systemRequired ``` |

Modified [CTFontManagerError.unrecognizedFormat](https://developer.apple.com/documentation/coretext/ctfontmanagererror/unrecognizedformat)

|  | Declaration |
| --- | --- |
| From | ``` case UnrecognizedFormat ``` |
| To | ``` case unrecognizedFormat ``` |

Modified [CTFontManagerScope [enum]](https://developer.apple.com/documentation/coretext/ctfontmanagerscope)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFontManagerScope : UInt32 {     case None     case Process     case User     case Session } ``` |
| To | ``` enum CTFontManagerScope : UInt32 {     case none     case process     case user     case session } ``` |

Modified [CTFontManagerScope.none](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/kctfontmanagerscopenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CTFontManagerScope.process](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/process)

|  | Declaration |
| --- | --- |
| From | ``` case Process ``` |
| To | ``` case process ``` |

Modified [CTFontManagerScope.session](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/session)

|  | Declaration |
| --- | --- |
| From | ``` case Session ``` |
| To | ``` case session ``` |

Modified [CTFontManagerScope.user](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/user)

|  | Declaration |
| --- | --- |
| From | ``` case User ``` |
| To | ``` case user ``` |

Modified [CTFontOptions [struct]](https://developer.apple.com/documentation/coretext/ctfontoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var Default: CTFontOptions { get }     static var PreventAutoActivation: CTFontOptions { get }     static var PreferSystemFont: CTFontOptions { get } } ``` | OptionSetType |
| To | ``` struct CTFontOptions : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var `default`: CTFontOptions { get }     static var preventAutoActivation: CTFontOptions { get }     static var preferSystemFont: CTFontOptions { get }     func intersect(_ other: CTFontOptions) -> CTFontOptions     func exclusiveOr(_ other: CTFontOptions) -> CTFontOptions     mutating func unionInPlace(_ other: CTFontOptions)     mutating func intersectInPlace(_ other: CTFontOptions)     mutating func exclusiveOrInPlace(_ other: CTFontOptions)     func isSubsetOf(_ other: CTFontOptions) -> Bool     func isDisjointWith(_ other: CTFontOptions) -> Bool     func isSupersetOf(_ other: CTFontOptions) -> Bool     mutating func subtractInPlace(_ other: CTFontOptions)     func isStrictSupersetOf(_ other: CTFontOptions) -> Bool     func isStrictSubsetOf(_ other: CTFontOptions) -> Bool } extension CTFontOptions {     func union(_ other: CTFontOptions) -> CTFontOptions     func intersection(_ other: CTFontOptions) -> CTFontOptions     func symmetricDifference(_ other: CTFontOptions) -> CTFontOptions } extension CTFontOptions {     func contains(_ member: CTFontOptions) -> Bool     mutating func insert(_ newMember: CTFontOptions) -> (inserted: Bool, memberAfterInsert: CTFontOptions)     mutating func remove(_ member: CTFontOptions) -> CTFontOptions?     mutating func update(with newMember: CTFontOptions) -> CTFontOptions? } extension CTFontOptions {     convenience init()     mutating func formUnion(_ other: CTFontOptions)     mutating func formIntersection(_ other: CTFontOptions)     mutating func formSymmetricDifference(_ other: CTFontOptions) } extension CTFontOptions {     convenience init<S : Sequence where S.Iterator.Element == CTFontOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CTFontOptions...)     mutating func subtract(_ other: CTFontOptions)     func isSubset(of other: CTFontOptions) -> Bool     func isSuperset(of other: CTFontOptions) -> Bool     func isDisjoint(with other: CTFontOptions) -> Bool     func subtracting(_ other: CTFontOptions) -> CTFontOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CTFontOptions) -> Bool     func isStrictSubset(of other: CTFontOptions) -> Bool } ``` | OptionSet |

Modified [CTFontOptions.preferSystemFont](https://developer.apple.com/documentation/coretext/ctfontoptions/kctfontoptionsprefersystemfont)

|  | Declaration |
| --- | --- |
| From | ``` static var PreferSystemFont: CTFontOptions { get } ``` |
| To | ``` static var preferSystemFont: CTFontOptions { get } ``` |

Modified [CTFontOptions.preventAutoActivation](https://developer.apple.com/documentation/coretext/ctfontoptions/kctfontoptionspreventautoactivation)

|  | Declaration |
| --- | --- |
| From | ``` static var PreventAutoActivation: CTFontOptions { get } ``` |
| To | ``` static var preventAutoActivation: CTFontOptions { get } ``` |

Modified [CTFontOrientation [enum]](https://developer.apple.com/documentation/coretext/ctfontorientation)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFontOrientation : UInt32 {     case Default     case Horizontal     case Vertical     static var kCTFontDefaultOrientation: CTFontOrientation { get }     static var kCTFontHorizontalOrientation: CTFontOrientation { get }     static var kCTFontVerticalOrientation: CTFontOrientation { get } } ``` |
| To | ``` enum CTFontOrientation : UInt32 {     case `default`     case horizontal     case vertical     static var kCTFontDefaultOrientation: CTFontOrientation { get }     static var kCTFontHorizontalOrientation: CTFontOrientation { get }     static var kCTFontVerticalOrientation: CTFontOrientation { get } } ``` |

Modified [CTFontOrientation.default](https://developer.apple.com/documentation/coretext/ctfontorientation/default)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [CTFontOrientation.horizontal](https://developer.apple.com/documentation/coretext/ctfontorientation/horizontal)

|  | Declaration |
| --- | --- |
| From | ``` case Horizontal ``` |
| To | ``` case horizontal ``` |

Modified [CTFontOrientation.vertical](https://developer.apple.com/documentation/coretext/ctfontorientation/vertical)

|  | Declaration |
| --- | --- |
| From | ``` case Vertical ``` |
| To | ``` case vertical ``` |

Modified [CTFontStylisticClass [struct]](https://developer.apple.com/documentation/coretext/ctfontstylisticclass)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontStylisticClass : OptionSetType {     init(rawValue rawValue: UInt32)     static var ClassUnknown: CTFontStylisticClass { get }     static var ClassOldStyleSerifs: CTFontStylisticClass { get }     static var ClassTransitionalSerifs: CTFontStylisticClass { get }     static var ClassModernSerifs: CTFontStylisticClass { get }     static var ClassClarendonSerifs: CTFontStylisticClass { get }     static var ClassSlabSerifs: CTFontStylisticClass { get }     static var ClassFreeformSerifs: CTFontStylisticClass { get }     static var ClassSansSerif: CTFontStylisticClass { get }     static var ClassOrnamentals: CTFontStylisticClass { get }     static var ClassScripts: CTFontStylisticClass { get }     static var ClassSymbolic: CTFontStylisticClass { get }     static var UnknownClass: CTFontStylisticClass { get }     static var OldStyleSerifsClass: CTFontStylisticClass { get }     static var TransitionalSerifsClass: CTFontStylisticClass { get }     static var ModernSerifsClass: CTFontStylisticClass { get }     static var ClarendonSerifsClass: CTFontStylisticClass { get }     static var SlabSerifsClass: CTFontStylisticClass { get }     static var FreeformSerifsClass: CTFontStylisticClass { get }     static var SansSerifClass: CTFontStylisticClass { get }     static var OrnamentalsClass: CTFontStylisticClass { get }     static var ScriptsClass: CTFontStylisticClass { get }     static var SymbolicClass: CTFontStylisticClass { get } } ``` | OptionSetType |
| To | ``` struct CTFontStylisticClass : OptionSet {     init(rawValue rawValue: UInt32)     static var classUnknown: CTFontStylisticClass { get }     static var classOldStyleSerifs: CTFontStylisticClass { get }     static var classTransitionalSerifs: CTFontStylisticClass { get }     static var classModernSerifs: CTFontStylisticClass { get }     static var classClarendonSerifs: CTFontStylisticClass { get }     static var classSlabSerifs: CTFontStylisticClass { get }     static var classFreeformSerifs: CTFontStylisticClass { get }     static var classSansSerif: CTFontStylisticClass { get }     static var classOrnamentals: CTFontStylisticClass { get }     static var classScripts: CTFontStylisticClass { get }     static var classSymbolic: CTFontStylisticClass { get }     static var unknownClass: CTFontStylisticClass { get }     static var oldStyleSerifsClass: CTFontStylisticClass { get }     static var transitionalSerifsClass: CTFontStylisticClass { get }     static var modernSerifsClass: CTFontStylisticClass { get }     static var clarendonSerifsClass: CTFontStylisticClass { get }     static var slabSerifsClass: CTFontStylisticClass { get }     static var freeformSerifsClass: CTFontStylisticClass { get }     static var sansSerifClass: CTFontStylisticClass { get }     static var ornamentalsClass: CTFontStylisticClass { get }     static var scriptsClass: CTFontStylisticClass { get }     static var symbolicClass: CTFontStylisticClass { get }     func intersect(_ other: CTFontStylisticClass) -> CTFontStylisticClass     func exclusiveOr(_ other: CTFontStylisticClass) -> CTFontStylisticClass     mutating func unionInPlace(_ other: CTFontStylisticClass)     mutating func intersectInPlace(_ other: CTFontStylisticClass)     mutating func exclusiveOrInPlace(_ other: CTFontStylisticClass)     func isSubsetOf(_ other: CTFontStylisticClass) -> Bool     func isDisjointWith(_ other: CTFontStylisticClass) -> Bool     func isSupersetOf(_ other: CTFontStylisticClass) -> Bool     mutating func subtractInPlace(_ other: CTFontStylisticClass)     func isStrictSupersetOf(_ other: CTFontStylisticClass) -> Bool     func isStrictSubsetOf(_ other: CTFontStylisticClass) -> Bool } extension CTFontStylisticClass {     func union(_ other: CTFontStylisticClass) -> CTFontStylisticClass     func intersection(_ other: CTFontStylisticClass) -> CTFontStylisticClass     func symmetricDifference(_ other: CTFontStylisticClass) -> CTFontStylisticClass } extension CTFontStylisticClass {     func contains(_ member: CTFontStylisticClass) -> Bool     mutating func insert(_ newMember: CTFontStylisticClass) -> (inserted: Bool, memberAfterInsert: CTFontStylisticClass)     mutating func remove(_ member: CTFontStylisticClass) -> CTFontStylisticClass?     mutating func update(with newMember: CTFontStylisticClass) -> CTFontStylisticClass? } extension CTFontStylisticClass {     convenience init()     mutating func formUnion(_ other: CTFontStylisticClass)     mutating func formIntersection(_ other: CTFontStylisticClass)     mutating func formSymmetricDifference(_ other: CTFontStylisticClass) } extension CTFontStylisticClass {     convenience init<S : Sequence where S.Iterator.Element == CTFontStylisticClass>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CTFontStylisticClass...)     mutating func subtract(_ other: CTFontStylisticClass)     func isSubset(of other: CTFontStylisticClass) -> Bool     func isSuperset(of other: CTFontStylisticClass) -> Bool     func isDisjoint(with other: CTFontStylisticClass) -> Bool     func subtracting(_ other: CTFontStylisticClass) -> CTFontStylisticClass     var isEmpty: Bool { get }     func isStrictSuperset(of other: CTFontStylisticClass) -> Bool     func isStrictSubset(of other: CTFontStylisticClass) -> Bool } ``` | OptionSet |

Modified [CTFontStylisticClass.clarendonSerifsClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1509420-clarendonserifsclass)

|  | Declaration |
| --- | --- |
| From | ``` static var ClarendonSerifsClass: CTFontStylisticClass { get } ``` |
| To | ``` static var clarendonSerifsClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classClarendonSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassclarendonserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassClarendonSerifs: CTFontStylisticClass { get } ``` |
| To | ``` static var classClarendonSerifs: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classFreeformSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1511041-classfreeformserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassFreeformSerifs: CTFontStylisticClass { get } ``` |
| To | ``` static var classFreeformSerifs: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classModernSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassmodernserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassModernSerifs: CTFontStylisticClass { get } ``` |
| To | ``` static var classModernSerifs: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classOldStyleSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassoldstyleserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassOldStyleSerifs: CTFontStylisticClass { get } ``` |
| To | ``` static var classOldStyleSerifs: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classOrnamentals](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1508975-classornamentals)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassOrnamentals: CTFontStylisticClass { get } ``` |
| To | ``` static var classOrnamentals: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classSansSerif](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1509781-classsansserif)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassSansSerif: CTFontStylisticClass { get } ``` |
| To | ``` static var classSansSerif: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classScripts](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontclassscripts)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassScripts: CTFontStylisticClass { get } ``` |
| To | ``` static var classScripts: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classSlabSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1508763-classslabserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassSlabSerifs: CTFontStylisticClass { get } ``` |
| To | ``` static var classSlabSerifs: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classSymbolic](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1509404-classsymbolic)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassSymbolic: CTFontStylisticClass { get } ``` |
| To | ``` static var classSymbolic: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.classTransitionalSerifs](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1509272-classtransitionalserifs)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassTransitionalSerifs: CTFontStylisticClass { get } ``` |
| To | ``` static var classTransitionalSerifs: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.freeformSerifsClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1510777-freeformserifsclass)

|  | Declaration |
| --- | --- |
| From | ``` static var FreeformSerifsClass: CTFontStylisticClass { get } ``` |
| To | ``` static var freeformSerifsClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.modernSerifsClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1510940-modernserifsclass)

|  | Declaration |
| --- | --- |
| From | ``` static var ModernSerifsClass: CTFontStylisticClass { get } ``` |
| To | ``` static var modernSerifsClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.oldStyleSerifsClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1510660-oldstyleserifsclass)

|  | Declaration |
| --- | --- |
| From | ``` static var OldStyleSerifsClass: CTFontStylisticClass { get } ``` |
| To | ``` static var oldStyleSerifsClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.ornamentalsClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1509778-ornamentalsclass)

|  | Declaration |
| --- | --- |
| From | ``` static var OrnamentalsClass: CTFontStylisticClass { get } ``` |
| To | ``` static var ornamentalsClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.sansSerifClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontsansserifclass)

|  | Declaration |
| --- | --- |
| From | ``` static var SansSerifClass: CTFontStylisticClass { get } ``` |
| To | ``` static var sansSerifClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.scriptsClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontscriptsclass)

|  | Declaration |
| --- | --- |
| From | ``` static var ScriptsClass: CTFontStylisticClass { get } ``` |
| To | ``` static var scriptsClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.slabSerifsClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/1510990-slabserifsclass)

|  | Declaration |
| --- | --- |
| From | ``` static var SlabSerifsClass: CTFontStylisticClass { get } ``` |
| To | ``` static var slabSerifsClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.symbolicClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfontsymbolicclass)

|  | Declaration |
| --- | --- |
| From | ``` static var SymbolicClass: CTFontStylisticClass { get } ``` |
| To | ``` static var symbolicClass: CTFontStylisticClass { get } ``` |

Modified [CTFontStylisticClass.transitionalSerifsClass](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/kctfonttransitionalserifsclass)

|  | Declaration |
| --- | --- |
| From | ``` static var TransitionalSerifsClass: CTFontStylisticClass { get } ``` |
| To | ``` static var transitionalSerifsClass: CTFontStylisticClass { get } ``` |

Modified [CTFontSymbolicTraits [struct]](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontSymbolicTraits : OptionSetType {     init(rawValue rawValue: UInt32)     static var TraitItalic: CTFontSymbolicTraits { get }     static var TraitBold: CTFontSymbolicTraits { get }     static var TraitExpanded: CTFontSymbolicTraits { get }     static var TraitCondensed: CTFontSymbolicTraits { get }     static var TraitMonoSpace: CTFontSymbolicTraits { get }     static var TraitVertical: CTFontSymbolicTraits { get }     static var TraitUIOptimized: CTFontSymbolicTraits { get }     static var TraitColorGlyphs: CTFontSymbolicTraits { get }     static var TraitComposite: CTFontSymbolicTraits { get }     static var TraitClassMask: CTFontSymbolicTraits { get }     static var ItalicTrait: CTFontSymbolicTraits { get }     static var BoldTrait: CTFontSymbolicTraits { get }     static var ExpandedTrait: CTFontSymbolicTraits { get }     static var CondensedTrait: CTFontSymbolicTraits { get }     static var MonoSpaceTrait: CTFontSymbolicTraits { get }     static var VerticalTrait: CTFontSymbolicTraits { get }     static var UIOptimizedTrait: CTFontSymbolicTraits { get }     static var ColorGlyphsTrait: CTFontSymbolicTraits { get }     static var CompositeTrait: CTFontSymbolicTraits { get }     static var ClassMaskTrait: CTFontSymbolicTraits { get } } ``` | OptionSetType |
| To | ``` struct CTFontSymbolicTraits : OptionSet {     init(rawValue rawValue: UInt32)     static var traitItalic: CTFontSymbolicTraits { get }     static var traitBold: CTFontSymbolicTraits { get }     static var traitExpanded: CTFontSymbolicTraits { get }     static var traitCondensed: CTFontSymbolicTraits { get }     static var traitMonoSpace: CTFontSymbolicTraits { get }     static var traitVertical: CTFontSymbolicTraits { get }     static var traitUIOptimized: CTFontSymbolicTraits { get }     static var traitColorGlyphs: CTFontSymbolicTraits { get }     static var traitComposite: CTFontSymbolicTraits { get }     static var traitClassMask: CTFontSymbolicTraits { get }     static var italicTrait: CTFontSymbolicTraits { get }     static var boldTrait: CTFontSymbolicTraits { get }     static var expandedTrait: CTFontSymbolicTraits { get }     static var condensedTrait: CTFontSymbolicTraits { get }     static var monoSpaceTrait: CTFontSymbolicTraits { get }     static var verticalTrait: CTFontSymbolicTraits { get }     static var uiOptimizedTrait: CTFontSymbolicTraits { get }     static var colorGlyphsTrait: CTFontSymbolicTraits { get }     static var compositeTrait: CTFontSymbolicTraits { get }     static var classMaskTrait: CTFontSymbolicTraits { get }     func intersect(_ other: CTFontSymbolicTraits) -> CTFontSymbolicTraits     func exclusiveOr(_ other: CTFontSymbolicTraits) -> CTFontSymbolicTraits     mutating func unionInPlace(_ other: CTFontSymbolicTraits)     mutating func intersectInPlace(_ other: CTFontSymbolicTraits)     mutating func exclusiveOrInPlace(_ other: CTFontSymbolicTraits)     func isSubsetOf(_ other: CTFontSymbolicTraits) -> Bool     func isDisjointWith(_ other: CTFontSymbolicTraits) -> Bool     func isSupersetOf(_ other: CTFontSymbolicTraits) -> Bool     mutating func subtractInPlace(_ other: CTFontSymbolicTraits)     func isStrictSupersetOf(_ other: CTFontSymbolicTraits) -> Bool     func isStrictSubsetOf(_ other: CTFontSymbolicTraits) -> Bool } extension CTFontSymbolicTraits {     func union(_ other: CTFontSymbolicTraits) -> CTFontSymbolicTraits     func intersection(_ other: CTFontSymbolicTraits) -> CTFontSymbolicTraits     func symmetricDifference(_ other: CTFontSymbolicTraits) -> CTFontSymbolicTraits } extension CTFontSymbolicTraits {     func contains(_ member: CTFontSymbolicTraits) -> Bool     mutating func insert(_ newMember: CTFontSymbolicTraits) -> (inserted: Bool, memberAfterInsert: CTFontSymbolicTraits)     mutating func remove(_ member: CTFontSymbolicTraits) -> CTFontSymbolicTraits?     mutating func update(with newMember: CTFontSymbolicTraits) -> CTFontSymbolicTraits? } extension CTFontSymbolicTraits {     convenience init()     mutating func formUnion(_ other: CTFontSymbolicTraits)     mutating func formIntersection(_ other: CTFontSymbolicTraits)     mutating func formSymmetricDifference(_ other: CTFontSymbolicTraits) } extension CTFontSymbolicTraits {     convenience init<S : Sequence where S.Iterator.Element == CTFontSymbolicTraits>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CTFontSymbolicTraits...)     mutating func subtract(_ other: CTFontSymbolicTraits)     func isSubset(of other: CTFontSymbolicTraits) -> Bool     func isSuperset(of other: CTFontSymbolicTraits) -> Bool     func isDisjoint(with other: CTFontSymbolicTraits) -> Bool     func subtracting(_ other: CTFontSymbolicTraits) -> CTFontSymbolicTraits     var isEmpty: Bool { get }     func isStrictSuperset(of other: CTFontSymbolicTraits) -> Bool     func isStrictSubset(of other: CTFontSymbolicTraits) -> Bool } ``` | OptionSet |

Modified [CTFontSymbolicTraits.boldTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfontboldtrait)

|  | Declaration |
| --- | --- |
| From | ``` static var BoldTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var boldTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.classMaskTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509032-classmasktrait)

|  | Declaration |
| --- | --- |
| From | ``` static var ClassMaskTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var classMaskTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.colorGlyphsTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfontcolorglyphstrait)

|  | Declaration |
| --- | --- |
| From | ``` static var ColorGlyphsTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var colorGlyphsTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.compositeTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509332-compositetrait)

|  | Declaration |
| --- | --- |
| From | ``` static var CompositeTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var compositeTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.condensedTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509352-condensedtrait)

|  | Declaration |
| --- | --- |
| From | ``` static var CondensedTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var condensedTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.expandedTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509941-expandedtrait)

|  | Declaration |
| --- | --- |
| From | ``` static var ExpandedTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var expandedTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.italicTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1508736-italictrait)

|  | Declaration |
| --- | --- |
| From | ``` static var ItalicTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var italicTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.monoSpaceTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfontmonospacetrait)

|  | Declaration |
| --- | --- |
| From | ``` static var MonoSpaceTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var monoSpaceTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitBold](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraitbold)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitBold: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitBold: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitClassMask](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509187-traitclassmask)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitClassMask: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitClassMask: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitColorGlyphs](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraitcolorglyphs)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitColorGlyphs: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitColorGlyphs: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitComposite](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraitcomposite)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitComposite: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitComposite: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitCondensed](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1510865-traitcondensed)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitCondensed: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitCondensed: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitExpanded](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1510447-traitexpanded)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitExpanded: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitExpanded: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitItalic](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1509535-traititalic)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitItalic: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitItalic: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitMonoSpace](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraitmonospace)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitMonoSpace: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitMonoSpace: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitUIOptimized](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraituioptimized)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitUIOptimized: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitUIOptimized: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.traitVertical](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfonttraitvertical)

|  | Declaration |
| --- | --- |
| From | ``` static var TraitVertical: CTFontSymbolicTraits { get } ``` |
| To | ``` static var traitVertical: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.uiOptimizedTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/kctfontuioptimizedtrait)

|  | Declaration |
| --- | --- |
| From | ``` static var UIOptimizedTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var uiOptimizedTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontSymbolicTraits.verticalTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1511338-verticaltrait)

|  | Declaration |
| --- | --- |
| From | ``` static var VerticalTrait: CTFontSymbolicTraits { get } ``` |
| To | ``` static var verticalTrait: CTFontSymbolicTraits { get } ``` |

Modified [CTFontTableOptions [struct]](https://developer.apple.com/documentation/coretext/ctfonttableoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontTableOptions : OptionSetType {     init(rawValue rawValue: UInt32)     static var NoOptions: CTFontTableOptions { get }     static var ExcludeSynthetic: CTFontTableOptions { get } } ``` | OptionSetType |
| To | ``` struct CTFontTableOptions : OptionSet {     init(rawValue rawValue: UInt32)     static var noOptions: CTFontTableOptions { get }     static var excludeSynthetic: CTFontTableOptions { get }     func intersect(_ other: CTFontTableOptions) -> CTFontTableOptions     func exclusiveOr(_ other: CTFontTableOptions) -> CTFontTableOptions     mutating func unionInPlace(_ other: CTFontTableOptions)     mutating func intersectInPlace(_ other: CTFontTableOptions)     mutating func exclusiveOrInPlace(_ other: CTFontTableOptions)     func isSubsetOf(_ other: CTFontTableOptions) -> Bool     func isDisjointWith(_ other: CTFontTableOptions) -> Bool     func isSupersetOf(_ other: CTFontTableOptions) -> Bool     mutating func subtractInPlace(_ other: CTFontTableOptions)     func isStrictSupersetOf(_ other: CTFontTableOptions) -> Bool     func isStrictSubsetOf(_ other: CTFontTableOptions) -> Bool } extension CTFontTableOptions {     func union(_ other: CTFontTableOptions) -> CTFontTableOptions     func intersection(_ other: CTFontTableOptions) -> CTFontTableOptions     func symmetricDifference(_ other: CTFontTableOptions) -> CTFontTableOptions } extension CTFontTableOptions {     func contains(_ member: CTFontTableOptions) -> Bool     mutating func insert(_ newMember: CTFontTableOptions) -> (inserted: Bool, memberAfterInsert: CTFontTableOptions)     mutating func remove(_ member: CTFontTableOptions) -> CTFontTableOptions?     mutating func update(with newMember: CTFontTableOptions) -> CTFontTableOptions? } extension CTFontTableOptions {     convenience init()     mutating func formUnion(_ other: CTFontTableOptions)     mutating func formIntersection(_ other: CTFontTableOptions)     mutating func formSymmetricDifference(_ other: CTFontTableOptions) } extension CTFontTableOptions {     convenience init<S : Sequence where S.Iterator.Element == CTFontTableOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CTFontTableOptions...)     mutating func subtract(_ other: CTFontTableOptions)     func isSubset(of other: CTFontTableOptions) -> Bool     func isSuperset(of other: CTFontTableOptions) -> Bool     func isDisjoint(with other: CTFontTableOptions) -> Bool     func subtracting(_ other: CTFontTableOptions) -> CTFontTableOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CTFontTableOptions) -> Bool     func isStrictSubset(of other: CTFontTableOptions) -> Bool } ``` | OptionSet |

Modified [CTFontTableOptions.excludeSynthetic](https://developer.apple.com/documentation/coretext/ctfonttableoptions/kctfonttableoptionexcludesynthetic)

|  | Declaration |
| --- | --- |
| From | ``` static var ExcludeSynthetic: CTFontTableOptions { get } ``` |
| To | ``` static var excludeSynthetic: CTFontTableOptions { get } ``` |

Modified [CTFontUIFontType [enum]](https://developer.apple.com/documentation/coretext/ctfontuifonttype)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFontUIFontType : UInt32 {     case None     case User     case UserFixedPitch     case System     case EmphasizedSystem     case SmallSystem     case SmallEmphasizedSystem     case MiniSystem     case MiniEmphasizedSystem     case Views     case Application     case Label     case MenuTitle     case MenuItem     case MenuItemMark     case MenuItemCmdKey     case WindowTitle     case PushButton     case UtilityWindowTitle     case AlertHeader     case SystemDetail     case EmphasizedSystemDetail     case Toolbar     case SmallToolbar     case Message     case Palette     case ToolTip     case ControlContent     static var kCTFontNoFontType: CTFontUIFontType { get }     static var kCTFontUserFontType: CTFontUIFontType { get }     static var kCTFontUserFixedPitchFontType: CTFontUIFontType { get }     static var kCTFontSystemFontType: CTFontUIFontType { get }     static var kCTFontEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontSmallSystemFontType: CTFontUIFontType { get }     static var kCTFontSmallEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontMiniSystemFontType: CTFontUIFontType { get }     static var kCTFontMiniEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontViewsFontType: CTFontUIFontType { get }     static var kCTFontApplicationFontType: CTFontUIFontType { get }     static var kCTFontLabelFontType: CTFontUIFontType { get }     static var kCTFontMenuTitleFontType: CTFontUIFontType { get }     static var kCTFontMenuItemFontType: CTFontUIFontType { get }     static var kCTFontMenuItemMarkFontType: CTFontUIFontType { get }     static var kCTFontMenuItemCmdKeyFontType: CTFontUIFontType { get }     static var kCTFontWindowTitleFontType: CTFontUIFontType { get }     static var kCTFontPushButtonFontType: CTFontUIFontType { get }     static var kCTFontUtilityWindowTitleFontType: CTFontUIFontType { get }     static var kCTFontAlertHeaderFontType: CTFontUIFontType { get }     static var kCTFontSystemDetailFontType: CTFontUIFontType { get }     static var kCTFontEmphasizedSystemDetailFontType: CTFontUIFontType { get }     static var kCTFontToolbarFontType: CTFontUIFontType { get }     static var kCTFontSmallToolbarFontType: CTFontUIFontType { get }     static var kCTFontMessageFontType: CTFontUIFontType { get }     static var kCTFontPaletteFontType: CTFontUIFontType { get }     static var kCTFontToolTipFontType: CTFontUIFontType { get }     static var kCTFontControlContentFontType: CTFontUIFontType { get } } ``` |
| To | ``` enum CTFontUIFontType : UInt32 {     case none     case user     case userFixedPitch     case system     case emphasizedSystem     case smallSystem     case smallEmphasizedSystem     case miniSystem     case miniEmphasizedSystem     case views     case application     case label     case menuTitle     case menuItem     case menuItemMark     case menuItemCmdKey     case windowTitle     case pushButton     case utilityWindowTitle     case alertHeader     case systemDetail     case emphasizedSystemDetail     case toolbar     case smallToolbar     case message     case palette     case toolTip     case controlContent     static var kCTFontNoFontType: CTFontUIFontType { get }     static var kCTFontUserFontType: CTFontUIFontType { get }     static var kCTFontUserFixedPitchFontType: CTFontUIFontType { get }     static var kCTFontSystemFontType: CTFontUIFontType { get }     static var kCTFontEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontSmallSystemFontType: CTFontUIFontType { get }     static var kCTFontSmallEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontMiniSystemFontType: CTFontUIFontType { get }     static var kCTFontMiniEmphasizedSystemFontType: CTFontUIFontType { get }     static var kCTFontViewsFontType: CTFontUIFontType { get }     static var kCTFontApplicationFontType: CTFontUIFontType { get }     static var kCTFontLabelFontType: CTFontUIFontType { get }     static var kCTFontMenuTitleFontType: CTFontUIFontType { get }     static var kCTFontMenuItemFontType: CTFontUIFontType { get }     static var kCTFontMenuItemMarkFontType: CTFontUIFontType { get }     static var kCTFontMenuItemCmdKeyFontType: CTFontUIFontType { get }     static var kCTFontWindowTitleFontType: CTFontUIFontType { get }     static var kCTFontPushButtonFontType: CTFontUIFontType { get }     static var kCTFontUtilityWindowTitleFontType: CTFontUIFontType { get }     static var kCTFontAlertHeaderFontType: CTFontUIFontType { get }     static var kCTFontSystemDetailFontType: CTFontUIFontType { get }     static var kCTFontEmphasizedSystemDetailFontType: CTFontUIFontType { get }     static var kCTFontToolbarFontType: CTFontUIFontType { get }     static var kCTFontSmallToolbarFontType: CTFontUIFontType { get }     static var kCTFontMessageFontType: CTFontUIFontType { get }     static var kCTFontPaletteFontType: CTFontUIFontType { get }     static var kCTFontToolTipFontType: CTFontUIFontType { get }     static var kCTFontControlContentFontType: CTFontUIFontType { get } } ``` |

Modified [CTFontUIFontType.alertHeader](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontalertheader)

|  | Declaration |
| --- | --- |
| From | ``` case AlertHeader ``` |
| To | ``` case alertHeader ``` |

Modified [CTFontUIFontType.application](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontapplication)

|  | Declaration |
| --- | --- |
| From | ``` case Application ``` |
| To | ``` case application ``` |

Modified [CTFontUIFontType.controlContent](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontcontrolcontent)

|  | Declaration |
| --- | --- |
| From | ``` case ControlContent ``` |
| To | ``` case controlContent ``` |

Modified [CTFontUIFontType.emphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/emphasizedsystem)

|  | Declaration |
| --- | --- |
| From | ``` case EmphasizedSystem ``` |
| To | ``` case emphasizedSystem ``` |

Modified [CTFontUIFontType.emphasizedSystemDetail](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontemphasizedsystemdetail)

|  | Declaration |
| --- | --- |
| From | ``` case EmphasizedSystemDetail ``` |
| To | ``` case emphasizedSystemDetail ``` |

Modified [CTFontUIFontType.label](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontlabel)

|  | Declaration |
| --- | --- |
| From | ``` case Label ``` |
| To | ``` case label ``` |

Modified [CTFontUIFontType.menuItem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/menuitem)

|  | Declaration |
| --- | --- |
| From | ``` case MenuItem ``` |
| To | ``` case menuItem ``` |

Modified [CTFontUIFontType.menuItemCmdKey](https://developer.apple.com/documentation/coretext/ctfontuifonttype/menuitemcmdkey)

|  | Declaration |
| --- | --- |
| From | ``` case MenuItemCmdKey ``` |
| To | ``` case menuItemCmdKey ``` |

Modified [CTFontUIFontType.menuItemMark](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontmenuitemmark)

|  | Declaration |
| --- | --- |
| From | ``` case MenuItemMark ``` |
| To | ``` case menuItemMark ``` |

Modified [CTFontUIFontType.menuTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontmenutitle)

|  | Declaration |
| --- | --- |
| From | ``` case MenuTitle ``` |
| To | ``` case menuTitle ``` |

Modified [CTFontUIFontType.message](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontmessage)

|  | Declaration |
| --- | --- |
| From | ``` case Message ``` |
| To | ``` case message ``` |

Modified [CTFontUIFontType.miniEmphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontminiemphasizedsystem)

|  | Declaration |
| --- | --- |
| From | ``` case MiniEmphasizedSystem ``` |
| To | ``` case miniEmphasizedSystem ``` |

Modified [CTFontUIFontType.miniSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/minisystem)

|  | Declaration |
| --- | --- |
| From | ``` case MiniSystem ``` |
| To | ``` case miniSystem ``` |

Modified [CTFontUIFontType.none](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CTFontUIFontType.palette](https://developer.apple.com/documentation/coretext/ctfontuifonttype/palette)

|  | Declaration |
| --- | --- |
| From | ``` case Palette ``` |
| To | ``` case palette ``` |

Modified [CTFontUIFontType.pushButton](https://developer.apple.com/documentation/coretext/ctfontuifonttype/pushbutton)

|  | Declaration |
| --- | --- |
| From | ``` case PushButton ``` |
| To | ``` case pushButton ``` |

Modified [CTFontUIFontType.smallEmphasizedSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/smallemphasizedsystem)

|  | Declaration |
| --- | --- |
| From | ``` case SmallEmphasizedSystem ``` |
| To | ``` case smallEmphasizedSystem ``` |

Modified [CTFontUIFontType.smallSystem](https://developer.apple.com/documentation/coretext/ctfontuifonttype/smallsystem)

|  | Declaration |
| --- | --- |
| From | ``` case SmallSystem ``` |
| To | ``` case smallSystem ``` |

Modified [CTFontUIFontType.smallToolbar](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsmalltoolbar)

|  | Declaration |
| --- | --- |
| From | ``` case SmallToolbar ``` |
| To | ``` case smallToolbar ``` |

Modified [CTFontUIFontType.system](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsystem)

|  | Declaration |
| --- | --- |
| From | ``` case System ``` |
| To | ``` case system ``` |

Modified [CTFontUIFontType.systemDetail](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifontsystemdetail)

|  | Declaration |
| --- | --- |
| From | ``` case SystemDetail ``` |
| To | ``` case systemDetail ``` |

Modified [CTFontUIFontType.toolbar](https://developer.apple.com/documentation/coretext/ctfontuifonttype/toolbar)

|  | Declaration |
| --- | --- |
| From | ``` case Toolbar ``` |
| To | ``` case toolbar ``` |

Modified [CTFontUIFontType.toolTip](https://developer.apple.com/documentation/coretext/ctfontuifonttype/kctfontuifonttooltip)

|  | Declaration |
| --- | --- |
| From | ``` case ToolTip ``` |
| To | ``` case toolTip ``` |

Modified [CTFontUIFontType.user](https://developer.apple.com/documentation/coretext/ctfontuifonttype/user)

|  | Declaration |
| --- | --- |
| From | ``` case User ``` |
| To | ``` case user ``` |

Modified [CTFontUIFontType.userFixedPitch](https://developer.apple.com/documentation/coretext/ctfontuifonttype/userfixedpitch)

|  | Declaration |
| --- | --- |
| From | ``` case UserFixedPitch ``` |
| To | ``` case userFixedPitch ``` |

Modified [CTFontUIFontType.utilityWindowTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/utilitywindowtitle)

|  | Declaration |
| --- | --- |
| From | ``` case UtilityWindowTitle ``` |
| To | ``` case utilityWindowTitle ``` |

Modified [CTFontUIFontType.views](https://developer.apple.com/documentation/coretext/ctfontuifonttype/views)

|  | Declaration |
| --- | --- |
| From | ``` case Views ``` |
| To | ``` case views ``` |

Modified [CTFontUIFontType.windowTitle](https://developer.apple.com/documentation/coretext/ctfontuifonttype/windowtitle)

|  | Declaration |
| --- | --- |
| From | ``` case WindowTitle ``` |
| To | ``` case windowTitle ``` |

Modified [CTFramePathFillRule [enum]](https://developer.apple.com/documentation/coretext/ctframepathfillrule)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFramePathFillRule : UInt32 {     case EvenOdd     case WindingNumber } ``` |
| To | ``` enum CTFramePathFillRule : UInt32 {     case evenOdd     case windingNumber } ``` |

Modified [CTFramePathFillRule.evenOdd](https://developer.apple.com/documentation/coretext/ctframepathfillrule/kctframepathfillevenodd)

|  | Declaration |
| --- | --- |
| From | ``` case EvenOdd ``` |
| To | ``` case evenOdd ``` |

Modified [CTFramePathFillRule.windingNumber](https://developer.apple.com/documentation/coretext/ctframepathfillrule/windingnumber)

|  | Declaration |
| --- | --- |
| From | ``` case WindingNumber ``` |
| To | ``` case windingNumber ``` |

Modified [CTFrameProgression [enum]](https://developer.apple.com/documentation/coretext/ctframeprogression)

|  | Declaration |
| --- | --- |
| From | ``` enum CTFrameProgression : UInt32 {     case TopToBottom     case RightToLeft     case LeftToRight } ``` |
| To | ``` enum CTFrameProgression : UInt32 {     case topToBottom     case rightToLeft     case leftToRight } ``` |

Modified [CTFrameProgression.leftToRight](https://developer.apple.com/documentation/coretext/ctframeprogression/lefttoright)

|  | Declaration |
| --- | --- |
| From | ``` case LeftToRight ``` |
| To | ``` case leftToRight ``` |

Modified [CTFrameProgression.rightToLeft](https://developer.apple.com/documentation/coretext/ctframeprogression/righttoleft)

|  | Declaration |
| --- | --- |
| From | ``` case RightToLeft ``` |
| To | ``` case rightToLeft ``` |

Modified [CTFrameProgression.topToBottom](https://developer.apple.com/documentation/coretext/ctframeprogression/kctframeprogressiontoptobottom)

|  | Declaration |
| --- | --- |
| From | ``` case TopToBottom ``` |
| To | ``` case topToBottom ``` |

Modified [CTLineBoundsOptions [struct]](https://developer.apple.com/documentation/coretext/ctlineboundsoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTLineBoundsOptions : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var ExcludeTypographicLeading: CTLineBoundsOptions { get }     static var ExcludeTypographicShifts: CTLineBoundsOptions { get }     static var UseHangingPunctuation: CTLineBoundsOptions { get }     static var UseGlyphPathBounds: CTLineBoundsOptions { get }     static var UseOpticalBounds: CTLineBoundsOptions { get }     static var IncludeLanguageExtents: CTLineBoundsOptions { get } } ``` | OptionSetType |
| To | ``` struct CTLineBoundsOptions : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var excludeTypographicLeading: CTLineBoundsOptions { get }     static var excludeTypographicShifts: CTLineBoundsOptions { get }     static var useHangingPunctuation: CTLineBoundsOptions { get }     static var useGlyphPathBounds: CTLineBoundsOptions { get }     static var useOpticalBounds: CTLineBoundsOptions { get }     static var includeLanguageExtents: CTLineBoundsOptions { get }     func intersect(_ other: CTLineBoundsOptions) -> CTLineBoundsOptions     func exclusiveOr(_ other: CTLineBoundsOptions) -> CTLineBoundsOptions     mutating func unionInPlace(_ other: CTLineBoundsOptions)     mutating func intersectInPlace(_ other: CTLineBoundsOptions)     mutating func exclusiveOrInPlace(_ other: CTLineBoundsOptions)     func isSubsetOf(_ other: CTLineBoundsOptions) -> Bool     func isDisjointWith(_ other: CTLineBoundsOptions) -> Bool     func isSupersetOf(_ other: CTLineBoundsOptions) -> Bool     mutating func subtractInPlace(_ other: CTLineBoundsOptions)     func isStrictSupersetOf(_ other: CTLineBoundsOptions) -> Bool     func isStrictSubsetOf(_ other: CTLineBoundsOptions) -> Bool } extension CTLineBoundsOptions {     func union(_ other: CTLineBoundsOptions) -> CTLineBoundsOptions     func intersection(_ other: CTLineBoundsOptions) -> CTLineBoundsOptions     func symmetricDifference(_ other: CTLineBoundsOptions) -> CTLineBoundsOptions } extension CTLineBoundsOptions {     func contains(_ member: CTLineBoundsOptions) -> Bool     mutating func insert(_ newMember: CTLineBoundsOptions) -> (inserted: Bool, memberAfterInsert: CTLineBoundsOptions)     mutating func remove(_ member: CTLineBoundsOptions) -> CTLineBoundsOptions?     mutating func update(with newMember: CTLineBoundsOptions) -> CTLineBoundsOptions? } extension CTLineBoundsOptions {     convenience init()     mutating func formUnion(_ other: CTLineBoundsOptions)     mutating func formIntersection(_ other: CTLineBoundsOptions)     mutating func formSymmetricDifference(_ other: CTLineBoundsOptions) } extension CTLineBoundsOptions {     convenience init<S : Sequence where S.Iterator.Element == CTLineBoundsOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CTLineBoundsOptions...)     mutating func subtract(_ other: CTLineBoundsOptions)     func isSubset(of other: CTLineBoundsOptions) -> Bool     func isSuperset(of other: CTLineBoundsOptions) -> Bool     func isDisjoint(with other: CTLineBoundsOptions) -> Bool     func subtracting(_ other: CTLineBoundsOptions) -> CTLineBoundsOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CTLineBoundsOptions) -> Bool     func isStrictSubset(of other: CTLineBoundsOptions) -> Bool } ``` | OptionSet |

Modified [CTLineBoundsOptions.excludeTypographicLeading](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/1511034-excludetypographicleading)

|  | Declaration |
| --- | --- |
| From | ``` static var ExcludeTypographicLeading: CTLineBoundsOptions { get } ``` |
| To | ``` static var excludeTypographicLeading: CTLineBoundsOptions { get } ``` |

Modified [CTLineBoundsOptions.excludeTypographicShifts](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/1508724-excludetypographicshifts)

|  | Declaration |
| --- | --- |
| From | ``` static var ExcludeTypographicShifts: CTLineBoundsOptions { get } ``` |
| To | ``` static var excludeTypographicShifts: CTLineBoundsOptions { get } ``` |

Modified [CTLineBoundsOptions.includeLanguageExtents](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/kctlineboundsincludelanguageextents)

|  | Declaration |
| --- | --- |
| From | ``` static var IncludeLanguageExtents: CTLineBoundsOptions { get } ``` |
| To | ``` static var includeLanguageExtents: CTLineBoundsOptions { get } ``` |

Modified [CTLineBoundsOptions.useGlyphPathBounds](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/1510976-useglyphpathbounds)

|  | Declaration |
| --- | --- |
| From | ``` static var UseGlyphPathBounds: CTLineBoundsOptions { get } ``` |
| To | ``` static var useGlyphPathBounds: CTLineBoundsOptions { get } ``` |

Modified [CTLineBoundsOptions.useHangingPunctuation](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/1508952-usehangingpunctuation)

|  | Declaration |
| --- | --- |
| From | ``` static var UseHangingPunctuation: CTLineBoundsOptions { get } ``` |
| To | ``` static var useHangingPunctuation: CTLineBoundsOptions { get } ``` |

Modified [CTLineBoundsOptions.useOpticalBounds](https://developer.apple.com/documentation/coretext/ctlineboundsoptions/kctlineboundsuseopticalbounds)

|  | Declaration |
| --- | --- |
| From | ``` static var UseOpticalBounds: CTLineBoundsOptions { get } ``` |
| To | ``` static var useOpticalBounds: CTLineBoundsOptions { get } ``` |

Modified [CTLineBreakMode [enum]](https://developer.apple.com/documentation/coretext/ctlinebreakmode)

|  | Declaration |
| --- | --- |
| From | ``` enum CTLineBreakMode : UInt8 {     case ByWordWrapping     case ByCharWrapping     case ByClipping     case ByTruncatingHead     case ByTruncatingTail     case ByTruncatingMiddle } ``` |
| To | ``` enum CTLineBreakMode : UInt8 {     case byWordWrapping     case byCharWrapping     case byClipping     case byTruncatingHead     case byTruncatingTail     case byTruncatingMiddle } ``` |

Modified [CTLineBreakMode.byCharWrapping](https://developer.apple.com/documentation/coretext/ctlinebreakmode/kctlinebreakbycharwrapping)

|  | Declaration |
| --- | --- |
| From | ``` case ByCharWrapping ``` |
| To | ``` case byCharWrapping ``` |

Modified [CTLineBreakMode.byClipping](https://developer.apple.com/documentation/coretext/ctlinebreakmode/kctlinebreakbyclipping)

|  | Declaration |
| --- | --- |
| From | ``` case ByClipping ``` |
| To | ``` case byClipping ``` |

Modified [CTLineBreakMode.byTruncatingHead](https://developer.apple.com/documentation/coretext/ctlinebreakmode/bytruncatinghead)

|  | Declaration |
| --- | --- |
| From | ``` case ByTruncatingHead ``` |
| To | ``` case byTruncatingHead ``` |

Modified [CTLineBreakMode.byTruncatingMiddle](https://developer.apple.com/documentation/coretext/ctlinebreakmode/bytruncatingmiddle)

|  | Declaration |
| --- | --- |
| From | ``` case ByTruncatingMiddle ``` |
| To | ``` case byTruncatingMiddle ``` |

Modified [CTLineBreakMode.byTruncatingTail](https://developer.apple.com/documentation/coretext/ctlinebreakmode/bytruncatingtail)

|  | Declaration |
| --- | --- |
| From | ``` case ByTruncatingTail ``` |
| To | ``` case byTruncatingTail ``` |

Modified [CTLineBreakMode.byWordWrapping](https://developer.apple.com/documentation/coretext/ctlinebreakmode/bywordwrapping)

|  | Declaration |
| --- | --- |
| From | ``` case ByWordWrapping ``` |
| To | ``` case byWordWrapping ``` |

Modified [CTLineTruncationType [enum]](https://developer.apple.com/documentation/coretext/ctlinetruncationtype)

|  | Declaration |
| --- | --- |
| From | ``` enum CTLineTruncationType : UInt32 {     case Start     case End     case Middle } ``` |
| To | ``` enum CTLineTruncationType : UInt32 {     case start     case end     case middle } ``` |

Modified [CTLineTruncationType.end](https://developer.apple.com/documentation/coretext/ctlinetruncationtype/end)

|  | Declaration |
| --- | --- |
| From | ``` case End ``` |
| To | ``` case end ``` |

Modified [CTLineTruncationType.middle](https://developer.apple.com/documentation/coretext/ctlinetruncationtype/middle)

|  | Declaration |
| --- | --- |
| From | ``` case Middle ``` |
| To | ``` case middle ``` |

Modified [CTLineTruncationType.start](https://developer.apple.com/documentation/coretext/ctlinetruncationtype/kctlinetruncationstart)

|  | Declaration |
| --- | --- |
| From | ``` case Start ``` |
| To | ``` case start ``` |

Modified [CTParagraphStyleSetting [struct]](https://developer.apple.com/documentation/coretext/ctparagraphstylesetting)

|  | Declaration |
| --- | --- |
| From | ``` struct CTParagraphStyleSetting {     var spec: CTParagraphStyleSpecifier     var valueSize: Int     var value: UnsafePointer<Void> } ``` |
| To | ``` struct CTParagraphStyleSetting {     var spec: CTParagraphStyleSpecifier     var valueSize: Int     var value: UnsafeRawPointer } ``` |

Modified [CTParagraphStyleSetting.value](https://developer.apple.com/documentation/coretext/ctparagraphstylesetting/1496100-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: UnsafePointer<Void> ``` |
| To | ``` var value: UnsafeRawPointer ``` |

Modified [CTParagraphStyleSpecifier [enum]](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier)

|  | Declaration |
| --- | --- |
| From | ``` enum CTParagraphStyleSpecifier : UInt32 {     case Alignment     case FirstLineHeadIndent     case HeadIndent     case TailIndent     case TabStops     case DefaultTabInterval     case LineBreakMode     case LineHeightMultiple     case MaximumLineHeight     case MinimumLineHeight     case LineSpacing     case ParagraphSpacing     case ParagraphSpacingBefore     case BaseWritingDirection     case MaximumLineSpacing     case MinimumLineSpacing     case LineSpacingAdjustment     case LineBoundsOptions     case Count } ``` |
| To | ``` enum CTParagraphStyleSpecifier : UInt32 {     case alignment     case firstLineHeadIndent     case headIndent     case tailIndent     case tabStops     case defaultTabInterval     case lineBreakMode     case lineHeightMultiple     case maximumLineHeight     case minimumLineHeight     case lineSpacing     case paragraphSpacing     case paragraphSpacingBefore     case baseWritingDirection     case maximumLineSpacing     case minimumLineSpacing     case lineSpacingAdjustment     case lineBoundsOptions     case count } ``` |

Modified [CTParagraphStyleSpecifier.alignment](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifieralignment)

|  | Declaration |
| --- | --- |
| From | ``` case Alignment ``` |
| To | ``` case alignment ``` |

Modified [CTParagraphStyleSpecifier.baseWritingDirection](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/basewritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` case BaseWritingDirection ``` |
| To | ``` case baseWritingDirection ``` |

Modified [CTParagraphStyleSpecifier.count](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/count)

|  | Declaration |
| --- | --- |
| From | ``` case Count ``` |
| To | ``` case count ``` |

Modified [CTParagraphStyleSpecifier.defaultTabInterval](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/defaulttabinterval)

|  | Declaration |
| --- | --- |
| From | ``` case DefaultTabInterval ``` |
| To | ``` case defaultTabInterval ``` |

Modified [CTParagraphStyleSpecifier.firstLineHeadIndent](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierfirstlineheadindent)

|  | Declaration |
| --- | --- |
| From | ``` case FirstLineHeadIndent ``` |
| To | ``` case firstLineHeadIndent ``` |

Modified [CTParagraphStyleSpecifier.headIndent](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/headindent)

|  | Declaration |
| --- | --- |
| From | ``` case HeadIndent ``` |
| To | ``` case headIndent ``` |

Modified [CTParagraphStyleSpecifier.lineBoundsOptions](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierlineboundsoptions)

|  | Declaration |
| --- | --- |
| From | ``` case LineBoundsOptions ``` |
| To | ``` case lineBoundsOptions ``` |

Modified [CTParagraphStyleSpecifier.lineBreakMode](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/linebreakmode)

|  | Declaration |
| --- | --- |
| From | ``` case LineBreakMode ``` |
| To | ``` case lineBreakMode ``` |

Modified [CTParagraphStyleSpecifier.lineHeightMultiple](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierlineheightmultiple)

|  | Declaration |
| --- | --- |
| From | ``` case LineHeightMultiple ``` |
| To | ``` case lineHeightMultiple ``` |

Modified [CTParagraphStyleSpecifier.lineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierlinespacing)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` case LineSpacing ``` | watchOS 2.2 | -- |
| To | ``` case lineSpacing ``` | watchOS 2.0 | watchOS 2.0 |

Modified [CTParagraphStyleSpecifier.lineSpacingAdjustment](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/linespacingadjustment)

|  | Declaration |
| --- | --- |
| From | ``` case LineSpacingAdjustment ``` |
| To | ``` case lineSpacingAdjustment ``` |

Modified [CTParagraphStyleSpecifier.maximumLineHeight](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/maximumlineheight)

|  | Declaration |
| --- | --- |
| From | ``` case MaximumLineHeight ``` |
| To | ``` case maximumLineHeight ``` |

Modified [CTParagraphStyleSpecifier.maximumLineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/maximumlinespacing)

|  | Declaration |
| --- | --- |
| From | ``` case MaximumLineSpacing ``` |
| To | ``` case maximumLineSpacing ``` |

Modified [CTParagraphStyleSpecifier.minimumLineHeight](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierminimumlineheight)

|  | Declaration |
| --- | --- |
| From | ``` case MinimumLineHeight ``` |
| To | ``` case minimumLineHeight ``` |

Modified [CTParagraphStyleSpecifier.minimumLineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/minimumlinespacing)

|  | Declaration |
| --- | --- |
| From | ``` case MinimumLineSpacing ``` |
| To | ``` case minimumLineSpacing ``` |

Modified [CTParagraphStyleSpecifier.paragraphSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierparagraphspacing)

|  | Declaration |
| --- | --- |
| From | ``` case ParagraphSpacing ``` |
| To | ``` case paragraphSpacing ``` |

Modified [CTParagraphStyleSpecifier.paragraphSpacingBefore](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierparagraphspacingbefore)

|  | Declaration |
| --- | --- |
| From | ``` case ParagraphSpacingBefore ``` |
| To | ``` case paragraphSpacingBefore ``` |

Modified [CTParagraphStyleSpecifier.tabStops](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/tabstops)

|  | Declaration |
| --- | --- |
| From | ``` case TabStops ``` |
| To | ``` case tabStops ``` |

Modified [CTParagraphStyleSpecifier.tailIndent](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/tailindent)

|  | Declaration |
| --- | --- |
| From | ``` case TailIndent ``` |
| To | ``` case tailIndent ``` |

Modified [CTRubyAlignment [enum]](https://developer.apple.com/documentation/coretext/ctrubyalignment)

|  | Declaration |
| --- | --- |
| From | ``` enum CTRubyAlignment : UInt8 {     case Invalid     case Auto     case Start     case Center     case End     case DistributeLetter     case DistributeSpace     case LineEdge } ``` |
| To | ``` enum CTRubyAlignment : UInt8 {     case invalid     case auto     case start     case center     case end     case distributeLetter     case distributeSpace     case lineEdge } ``` |

Modified [CTRubyAlignment.auto](https://developer.apple.com/documentation/coretext/ctrubyalignment/auto)

|  | Declaration |
| --- | --- |
| From | ``` case Auto ``` |
| To | ``` case auto ``` |

Modified [CTRubyAlignment.center](https://developer.apple.com/documentation/coretext/ctrubyalignment/kctrubyalignmentcenter)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [CTRubyAlignment.distributeLetter](https://developer.apple.com/documentation/coretext/ctrubyalignment/distributeletter)

|  | Declaration |
| --- | --- |
| From | ``` case DistributeLetter ``` |
| To | ``` case distributeLetter ``` |

Modified [CTRubyAlignment.distributeSpace](https://developer.apple.com/documentation/coretext/ctrubyalignment/kctrubyalignmentdistributespace)

|  | Declaration |
| --- | --- |
| From | ``` case DistributeSpace ``` |
| To | ``` case distributeSpace ``` |

Modified [CTRubyAlignment.end](https://developer.apple.com/documentation/coretext/ctrubyalignment/kctrubyalignmentend)

|  | Declaration |
| --- | --- |
| From | ``` case End ``` |
| To | ``` case end ``` |

Modified [CTRubyAlignment.invalid](https://developer.apple.com/documentation/coretext/ctrubyalignment/kctrubyalignmentinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [CTRubyAlignment.lineEdge](https://developer.apple.com/documentation/coretext/ctrubyalignment/lineedge)

|  | Declaration |
| --- | --- |
| From | ``` case LineEdge ``` |
| To | ``` case lineEdge ``` |

Modified [CTRubyAlignment.start](https://developer.apple.com/documentation/coretext/ctrubyalignment/kctrubyalignmentstart)

|  | Declaration |
| --- | --- |
| From | ``` case Start ``` |
| To | ``` case start ``` |

Modified [CTRubyOverhang [enum]](https://developer.apple.com/documentation/coretext/ctrubyoverhang)

|  | Declaration |
| --- | --- |
| From | ``` enum CTRubyOverhang : UInt8 {     case Invalid     case Auto     case Start     case End     case None } ``` |
| To | ``` enum CTRubyOverhang : UInt8 {     case invalid     case auto     case start     case end     case none } ``` |

Modified [CTRubyOverhang.auto](https://developer.apple.com/documentation/coretext/ctrubyoverhang/auto)

|  | Declaration |
| --- | --- |
| From | ``` case Auto ``` |
| To | ``` case auto ``` |

Modified [CTRubyOverhang.end](https://developer.apple.com/documentation/coretext/ctrubyoverhang/end)

|  | Declaration |
| --- | --- |
| From | ``` case End ``` |
| To | ``` case end ``` |

Modified [CTRubyOverhang.invalid](https://developer.apple.com/documentation/coretext/ctrubyoverhang/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [CTRubyOverhang.none](https://developer.apple.com/documentation/coretext/ctrubyoverhang/kctrubyoverhangnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CTRubyOverhang.start](https://developer.apple.com/documentation/coretext/ctrubyoverhang/start)

|  | Declaration |
| --- | --- |
| From | ``` case Start ``` |
| To | ``` case start ``` |

Modified [CTRubyPosition [enum]](https://developer.apple.com/documentation/coretext/ctrubyposition)

|  | Declaration |
| --- | --- |
| From | ``` enum CTRubyPosition : UInt8 {     case Before     case After     case InterCharacter     case Inline     case Count } ``` |
| To | ``` enum CTRubyPosition : UInt8 {     case before     case after     case interCharacter     case inline     case count } ``` |

Modified [CTRubyPosition.after](https://developer.apple.com/documentation/coretext/ctrubyposition/kctrubypositionafter)

|  | Declaration |
| --- | --- |
| From | ``` case After ``` |
| To | ``` case after ``` |

Modified [CTRubyPosition.before](https://developer.apple.com/documentation/coretext/ctrubyposition/kctrubypositionbefore)

|  | Declaration |
| --- | --- |
| From | ``` case Before ``` |
| To | ``` case before ``` |

Modified [CTRubyPosition.count](https://developer.apple.com/documentation/coretext/ctrubyposition/kctrubypositioncount)

|  | Declaration |
| --- | --- |
| From | ``` case Count ``` |
| To | ``` case count ``` |

Modified [CTRubyPosition.inline](https://developer.apple.com/documentation/coretext/ctrubyposition/kctrubypositioninline)

|  | Declaration |
| --- | --- |
| From | ``` case Inline ``` |
| To | ``` case inline ``` |

Modified [CTRubyPosition.interCharacter](https://developer.apple.com/documentation/coretext/ctrubyposition/kctrubypositionintercharacter)

|  | Declaration |
| --- | --- |
| From | ``` case InterCharacter ``` |
| To | ``` case interCharacter ``` |

Modified [CTRunDelegateCallbacks [struct]](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CTRunDelegateCallbacks {     var version: CFIndex     var dealloc: CTRunDelegateDeallocateCallback     var getAscent: CTRunDelegateGetAscentCallback     var getDescent: CTRunDelegateGetDescentCallback     var getWidth: CTRunDelegateGetWidthCallback } ``` |
| To | ``` struct CTRunDelegateCallbacks {     var version: CFIndex     var dealloc: CoreText.CTRunDelegateDeallocateCallback     var getAscent: CoreText.CTRunDelegateGetAscentCallback     var getDescent: CoreText.CTRunDelegateGetDescentCallback     var getWidth: CoreText.CTRunDelegateGetWidthCallback } ``` |

Modified [CTRunDelegateCallbacks.dealloc](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks/1498170-dealloc)

|  | Declaration |
| --- | --- |
| From | ``` var dealloc: CTRunDelegateDeallocateCallback ``` |
| To | ``` var dealloc: CoreText.CTRunDelegateDeallocateCallback ``` |

Modified [CTRunDelegateCallbacks.getAscent](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks/1498178-getascent)

|  | Declaration |
| --- | --- |
| From | ``` var getAscent: CTRunDelegateGetAscentCallback ``` |
| To | ``` var getAscent: CoreText.CTRunDelegateGetAscentCallback ``` |

Modified [CTRunDelegateCallbacks.getDescent](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks/1498173-getdescent)

|  | Declaration |
| --- | --- |
| From | ``` var getDescent: CTRunDelegateGetDescentCallback ``` |
| To | ``` var getDescent: CoreText.CTRunDelegateGetDescentCallback ``` |

Modified [CTRunDelegateCallbacks.getWidth](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks/1498164-getwidth)

|  | Declaration |
| --- | --- |
| From | ``` var getWidth: CTRunDelegateGetWidthCallback ``` |
| To | ``` var getWidth: CoreText.CTRunDelegateGetWidthCallback ``` |

Modified [CTRunStatus [struct]](https://developer.apple.com/documentation/coretext/ctrunstatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTRunStatus : OptionSetType {     init(rawValue rawValue: UInt32)     static var NoStatus: CTRunStatus { get }     static var RightToLeft: CTRunStatus { get }     static var NonMonotonic: CTRunStatus { get }     static var HasNonIdentityMatrix: CTRunStatus { get } } ``` | OptionSetType |
| To | ``` struct CTRunStatus : OptionSet {     init(rawValue rawValue: UInt32)     static var noStatus: CTRunStatus { get }     static var rightToLeft: CTRunStatus { get }     static var nonMonotonic: CTRunStatus { get }     static var hasNonIdentityMatrix: CTRunStatus { get }     func intersect(_ other: CTRunStatus) -> CTRunStatus     func exclusiveOr(_ other: CTRunStatus) -> CTRunStatus     mutating func unionInPlace(_ other: CTRunStatus)     mutating func intersectInPlace(_ other: CTRunStatus)     mutating func exclusiveOrInPlace(_ other: CTRunStatus)     func isSubsetOf(_ other: CTRunStatus) -> Bool     func isDisjointWith(_ other: CTRunStatus) -> Bool     func isSupersetOf(_ other: CTRunStatus) -> Bool     mutating func subtractInPlace(_ other: CTRunStatus)     func isStrictSupersetOf(_ other: CTRunStatus) -> Bool     func isStrictSubsetOf(_ other: CTRunStatus) -> Bool } extension CTRunStatus {     func union(_ other: CTRunStatus) -> CTRunStatus     func intersection(_ other: CTRunStatus) -> CTRunStatus     func symmetricDifference(_ other: CTRunStatus) -> CTRunStatus } extension CTRunStatus {     func contains(_ member: CTRunStatus) -> Bool     mutating func insert(_ newMember: CTRunStatus) -> (inserted: Bool, memberAfterInsert: CTRunStatus)     mutating func remove(_ member: CTRunStatus) -> CTRunStatus?     mutating func update(with newMember: CTRunStatus) -> CTRunStatus? } extension CTRunStatus {     convenience init()     mutating func formUnion(_ other: CTRunStatus)     mutating func formIntersection(_ other: CTRunStatus)     mutating func formSymmetricDifference(_ other: CTRunStatus) } extension CTRunStatus {     convenience init<S : Sequence where S.Iterator.Element == CTRunStatus>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CTRunStatus...)     mutating func subtract(_ other: CTRunStatus)     func isSubset(of other: CTRunStatus) -> Bool     func isSuperset(of other: CTRunStatus) -> Bool     func isDisjoint(with other: CTRunStatus) -> Bool     func subtracting(_ other: CTRunStatus) -> CTRunStatus     var isEmpty: Bool { get }     func isStrictSuperset(of other: CTRunStatus) -> Bool     func isStrictSubset(of other: CTRunStatus) -> Bool } ``` | OptionSet |

Modified [CTRunStatus.hasNonIdentityMatrix](https://developer.apple.com/documentation/coretext/ctrunstatus/kctrunstatushasnonidentitymatrix)

|  | Declaration |
| --- | --- |
| From | ``` static var HasNonIdentityMatrix: CTRunStatus { get } ``` |
| To | ``` static var hasNonIdentityMatrix: CTRunStatus { get } ``` |

Modified [CTRunStatus.nonMonotonic](https://developer.apple.com/documentation/coretext/ctrunstatus/kctrunstatusnonmonotonic)

|  | Declaration |
| --- | --- |
| From | ``` static var NonMonotonic: CTRunStatus { get } ``` |
| To | ``` static var nonMonotonic: CTRunStatus { get } ``` |

Modified [CTRunStatus.rightToLeft](https://developer.apple.com/documentation/coretext/ctrunstatus/kctrunstatusrighttoleft)

|  | Declaration |
| --- | --- |
| From | ``` static var RightToLeft: CTRunStatus { get } ``` |
| To | ``` static var rightToLeft: CTRunStatus { get } ``` |

Modified [CTTextAlignment [enum]](https://developer.apple.com/documentation/coretext/cttextalignment)

|  | Declaration |
| --- | --- |
| From | ``` enum CTTextAlignment : UInt8 {     case Left     case Right     case Center     case Justified     case Natural     static var kCTLeftTextAlignment: CTTextAlignment { get }     static var kCTRightTextAlignment: CTTextAlignment { get }     static var kCTCenterTextAlignment: CTTextAlignment { get }     static var kCTJustifiedTextAlignment: CTTextAlignment { get }     static var kCTNaturalTextAlignment: CTTextAlignment { get } } ``` |
| To | ``` enum CTTextAlignment : UInt8 {     case left     case right     case center     case justified     case natural     static var kCTLeftTextAlignment: CTTextAlignment { get }     static var kCTRightTextAlignment: CTTextAlignment { get }     static var kCTCenterTextAlignment: CTTextAlignment { get }     static var kCTJustifiedTextAlignment: CTTextAlignment { get }     static var kCTNaturalTextAlignment: CTTextAlignment { get } } ``` |

Modified [CTTextAlignment.center](https://developer.apple.com/documentation/coretext/cttextalignment/center)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [CTTextAlignment.justified](https://developer.apple.com/documentation/coretext/cttextalignment/justified)

|  | Declaration |
| --- | --- |
| From | ``` case Justified ``` |
| To | ``` case justified ``` |

Modified [CTTextAlignment.left](https://developer.apple.com/documentation/coretext/cttextalignment/kcttextalignmentleft)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [CTTextAlignment.natural](https://developer.apple.com/documentation/coretext/cttextalignment/kcttextalignmentnatural)

|  | Declaration |
| --- | --- |
| From | ``` case Natural ``` |
| To | ``` case natural ``` |

Modified [CTTextAlignment.right](https://developer.apple.com/documentation/coretext/cttextalignment/right)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [CTUnderlineStyle [struct]](https://developer.apple.com/documentation/coretext/ctunderlinestyle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTUnderlineStyle : OptionSetType {     init(rawValue rawValue: Int32)     static var None: CTUnderlineStyle { get }     static var Single: CTUnderlineStyle { get }     static var Thick: CTUnderlineStyle { get }     static var Double: CTUnderlineStyle { get } } ``` | OptionSetType |
| To | ``` struct CTUnderlineStyle : OptionSet {     init(rawValue rawValue: Int32)     static var none: CTUnderlineStyle { get }     static var single: CTUnderlineStyle { get }     static var thick: CTUnderlineStyle { get }     static var double: CTUnderlineStyle { get }     func intersect(_ other: CTUnderlineStyle) -> CTUnderlineStyle     func exclusiveOr(_ other: CTUnderlineStyle) -> CTUnderlineStyle     mutating func unionInPlace(_ other: CTUnderlineStyle)     mutating func intersectInPlace(_ other: CTUnderlineStyle)     mutating func exclusiveOrInPlace(_ other: CTUnderlineStyle)     func isSubsetOf(_ other: CTUnderlineStyle) -> Bool     func isDisjointWith(_ other: CTUnderlineStyle) -> Bool     func isSupersetOf(_ other: CTUnderlineStyle) -> Bool     mutating func subtractInPlace(_ other: CTUnderlineStyle)     func isStrictSupersetOf(_ other: CTUnderlineStyle) -> Bool     func isStrictSubsetOf(_ other: CTUnderlineStyle) -> Bool } extension CTUnderlineStyle {     func union(_ other: CTUnderlineStyle) -> CTUnderlineStyle     func intersection(_ other: CTUnderlineStyle) -> CTUnderlineStyle     func symmetricDifference(_ other: CTUnderlineStyle) -> CTUnderlineStyle } extension CTUnderlineStyle {     func contains(_ member: CTUnderlineStyle) -> Bool     mutating func insert(_ newMember: CTUnderlineStyle) -> (inserted: Bool, memberAfterInsert: CTUnderlineStyle)     mutating func remove(_ member: CTUnderlineStyle) -> CTUnderlineStyle?     mutating func update(with newMember: CTUnderlineStyle) -> CTUnderlineStyle? } extension CTUnderlineStyle {     convenience init()     mutating func formUnion(_ other: CTUnderlineStyle)     mutating func formIntersection(_ other: CTUnderlineStyle)     mutating func formSymmetricDifference(_ other: CTUnderlineStyle) } extension CTUnderlineStyle {     convenience init<S : Sequence where S.Iterator.Element == CTUnderlineStyle>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CTUnderlineStyle...)     mutating func subtract(_ other: CTUnderlineStyle)     func isSubset(of other: CTUnderlineStyle) -> Bool     func isSuperset(of other: CTUnderlineStyle) -> Bool     func isDisjoint(with other: CTUnderlineStyle) -> Bool     func subtracting(_ other: CTUnderlineStyle) -> CTUnderlineStyle     var isEmpty: Bool { get }     func isStrictSuperset(of other: CTUnderlineStyle) -> Bool     func isStrictSubset(of other: CTUnderlineStyle) -> Bool } ``` | OptionSet |

Modified [CTUnderlineStyle.double](https://developer.apple.com/documentation/coretext/ctunderlinestyle/1510983-double)

|  | Declaration |
| --- | --- |
| From | ``` static var Double: CTUnderlineStyle { get } ``` |
| To | ``` static var double: CTUnderlineStyle { get } ``` |

Modified [CTUnderlineStyle.single](https://developer.apple.com/documentation/coretext/ctunderlinestyle/kctunderlinestylesingle)

|  | Declaration |
| --- | --- |
| From | ``` static var Single: CTUnderlineStyle { get } ``` |
| To | ``` static var single: CTUnderlineStyle { get } ``` |

Modified [CTUnderlineStyle.thick](https://developer.apple.com/documentation/coretext/ctunderlinestyle/1509580-thick)

|  | Declaration |
| --- | --- |
| From | ``` static var Thick: CTUnderlineStyle { get } ``` |
| To | ``` static var thick: CTUnderlineStyle { get } ``` |

Modified [CTUnderlineStyleModifiers [struct]](https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTUnderlineStyleModifiers : OptionSetType {     init(rawValue rawValue: Int32)     static var PatternSolid: CTUnderlineStyleModifiers { get }     static var PatternDot: CTUnderlineStyleModifiers { get }     static var PatternDash: CTUnderlineStyleModifiers { get }     static var PatternDashDot: CTUnderlineStyleModifiers { get }     static var PatternDashDotDot: CTUnderlineStyleModifiers { get } } ``` | OptionSetType |
| To | ``` struct CTUnderlineStyleModifiers : OptionSet {     init(rawValue rawValue: Int32)     static var patternSolid: CTUnderlineStyleModifiers { get }     static var patternDot: CTUnderlineStyleModifiers { get }     static var patternDash: CTUnderlineStyleModifiers { get }     static var patternDashDot: CTUnderlineStyleModifiers { get }     static var patternDashDotDot: CTUnderlineStyleModifiers { get }     func intersect(_ other: CTUnderlineStyleModifiers) -> CTUnderlineStyleModifiers     func exclusiveOr(_ other: CTUnderlineStyleModifiers) -> CTUnderlineStyleModifiers     mutating func unionInPlace(_ other: CTUnderlineStyleModifiers)     mutating func intersectInPlace(_ other: CTUnderlineStyleModifiers)     mutating func exclusiveOrInPlace(_ other: CTUnderlineStyleModifiers)     func isSubsetOf(_ other: CTUnderlineStyleModifiers) -> Bool     func isDisjointWith(_ other: CTUnderlineStyleModifiers) -> Bool     func isSupersetOf(_ other: CTUnderlineStyleModifiers) -> Bool     mutating func subtractInPlace(_ other: CTUnderlineStyleModifiers)     func isStrictSupersetOf(_ other: CTUnderlineStyleModifiers) -> Bool     func isStrictSubsetOf(_ other: CTUnderlineStyleModifiers) -> Bool } extension CTUnderlineStyleModifiers {     func union(_ other: CTUnderlineStyleModifiers) -> CTUnderlineStyleModifiers     func intersection(_ other: CTUnderlineStyleModifiers) -> CTUnderlineStyleModifiers     func symmetricDifference(_ other: CTUnderlineStyleModifiers) -> CTUnderlineStyleModifiers } extension CTUnderlineStyleModifiers {     func contains(_ member: CTUnderlineStyleModifiers) -> Bool     mutating func insert(_ newMember: CTUnderlineStyleModifiers) -> (inserted: Bool, memberAfterInsert: CTUnderlineStyleModifiers)     mutating func remove(_ member: CTUnderlineStyleModifiers) -> CTUnderlineStyleModifiers?     mutating func update(with newMember: CTUnderlineStyleModifiers) -> CTUnderlineStyleModifiers? } extension CTUnderlineStyleModifiers {     convenience init()     mutating func formUnion(_ other: CTUnderlineStyleModifiers)     mutating func formIntersection(_ other: CTUnderlineStyleModifiers)     mutating func formSymmetricDifference(_ other: CTUnderlineStyleModifiers) } extension CTUnderlineStyleModifiers {     convenience init<S : Sequence where S.Iterator.Element == CTUnderlineStyleModifiers>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CTUnderlineStyleModifiers...)     mutating func subtract(_ other: CTUnderlineStyleModifiers)     func isSubset(of other: CTUnderlineStyleModifiers) -> Bool     func isSuperset(of other: CTUnderlineStyleModifiers) -> Bool     func isDisjoint(with other: CTUnderlineStyleModifiers) -> Bool     func subtracting(_ other: CTUnderlineStyleModifiers) -> CTUnderlineStyleModifiers     var isEmpty: Bool { get }     func isStrictSuperset(of other: CTUnderlineStyleModifiers) -> Bool     func isStrictSubset(of other: CTUnderlineStyleModifiers) -> Bool } ``` | OptionSet |

Modified [CTUnderlineStyleModifiers.patternDash](https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers/1511467-patterndash)

|  | Declaration |
| --- | --- |
| From | ``` static var PatternDash: CTUnderlineStyleModifiers { get } ``` |
| To | ``` static var patternDash: CTUnderlineStyleModifiers { get } ``` |

Modified [CTUnderlineStyleModifiers.patternDashDot](https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers/kctunderlinepatterndashdot)

|  | Declaration |
| --- | --- |
| From | ``` static var PatternDashDot: CTUnderlineStyleModifiers { get } ``` |
| To | ``` static var patternDashDot: CTUnderlineStyleModifiers { get } ``` |

Modified [CTUnderlineStyleModifiers.patternDashDotDot](https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers/1508940-patterndashdotdot)

|  | Declaration |
| --- | --- |
| From | ``` static var PatternDashDotDot: CTUnderlineStyleModifiers { get } ``` |
| To | ``` static var patternDashDotDot: CTUnderlineStyleModifiers { get } ``` |

Modified [CTUnderlineStyleModifiers.patternDot](https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers/1509626-patterndot)

|  | Declaration |
| --- | --- |
| From | ``` static var PatternDot: CTUnderlineStyleModifiers { get } ``` |
| To | ``` static var patternDot: CTUnderlineStyleModifiers { get } ``` |

Modified [CTUnderlineStyleModifiers.patternSolid](https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers/kctunderlinepatternsolid)

|  | Declaration |
| --- | --- |
| From | ``` static var PatternSolid: CTUnderlineStyleModifiers { get } ``` |
| To | ``` static var patternSolid: CTUnderlineStyleModifiers { get } ``` |

Modified [CTWritingDirection [enum]](https://developer.apple.com/documentation/coretext/ctwritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` enum CTWritingDirection : Int8 {     case Natural     case LeftToRight     case RightToLeft } ``` |
| To | ``` enum CTWritingDirection : Int8 {     case natural     case leftToRight     case rightToLeft } ``` |

Modified [CTWritingDirection.leftToRight](https://developer.apple.com/documentation/coretext/ctwritingdirection/kctwritingdirectionlefttoright)

|  | Declaration |
| --- | --- |
| From | ``` case LeftToRight ``` |
| To | ``` case leftToRight ``` |

Modified [CTWritingDirection.natural](https://developer.apple.com/documentation/coretext/ctwritingdirection/kctwritingdirectionnatural)

|  | Declaration |
| --- | --- |
| From | ``` case Natural ``` |
| To | ``` case natural ``` |

Modified [CTWritingDirection.rightToLeft](https://developer.apple.com/documentation/coretext/ctwritingdirection/righttoleft)

|  | Declaration |
| --- | --- |
| From | ``` case RightToLeft ``` |
| To | ``` case rightToLeft ``` |

Modified KerxIndexArrayHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxIndexArrayHeader {     var glyphCount: UInt16     var kernValueCount: UInt16     var leftClassCount: UInt16     var rightClassCount: UInt16     var flags: UInt16     var kernValue: (Int16)     var leftClass: (UInt16)     var rightClass: (UInt16)     var kernIndex: (UInt16)     init()     init(glyphCount glyphCount: UInt16, kernValueCount kernValueCount: UInt16, leftClassCount leftClassCount: UInt16, rightClassCount rightClassCount: UInt16, flags flags: UInt16, kernValue kernValue: (Int16), leftClass leftClass: (UInt16), rightClass rightClass: (UInt16), kernIndex kernIndex: (UInt16)) } ``` |
| To | ``` struct KerxIndexArrayHeader {     var flags: UInt32     var rowCount: UInt16     var columnCount: UInt16     var rowIndexTableOffset: UInt32     var columnIndexTableOffset: UInt32     var kerningArrayOffset: UInt32     var kerningVectorOffset: UInt32     init()     init(flags flags: UInt32, rowCount rowCount: UInt16, columnCount columnCount: UInt16, rowIndexTableOffset rowIndexTableOffset: UInt32, columnIndexTableOffset columnIndexTableOffset: UInt32, kerningArrayOffset kerningArrayOffset: UInt32, kerningVectorOffset kerningVectorOffset: UInt32) } ``` |

Modified KerxIndexArrayHeader.flags

|  | Declaration |
| --- | --- |
| From | ``` var flags: UInt16 ``` |
| To | ``` var flags: UInt32 ``` |

Modified KerxSubtableHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxSubtableHeader {     var length: UInt32     var stInfo: KerxSubtableCoverage     var tupleIndex: UInt32     var fsHeader: KerxFormatSpecificHeader     init()     init(length length: UInt32, stInfo stInfo: KerxSubtableCoverage, tupleIndex tupleIndex: UInt32, fsHeader fsHeader: KerxFormatSpecificHeader) } ``` |
| To | ``` struct KerxSubtableHeader {     var length: UInt32     var stInfo: KerxSubtableCoverage     var tupleCount: UInt32     var fsHeader: KerxFormatSpecificHeader     init()     init(length length: UInt32, stInfo stInfo: KerxSubtableCoverage, tupleCount tupleCount: UInt32, fsHeader fsHeader: KerxFormatSpecificHeader) } ``` |

Modified SFNTLookupFormatSpecificHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupFormatSpecificHeader {     var theArray: SFNTLookupArrayHeader     var segment: SFNTLookupSegmentHeader     var single: SFNTLookupSingleHeader     var trimmedArray: SFNTLookupTrimmedArrayHeader     init(theArray theArray: SFNTLookupArrayHeader)     init(segment segment: SFNTLookupSegmentHeader)     init(single single: SFNTLookupSingleHeader)     init(trimmedArray trimmedArray: SFNTLookupTrimmedArrayHeader)     init() } ``` |
| To | ``` struct SFNTLookupFormatSpecificHeader {     var theArray: SFNTLookupArrayHeader     var segment: SFNTLookupSegmentHeader     var single: SFNTLookupSingleHeader     var trimmedArray: SFNTLookupTrimmedArrayHeader     var vector: SFNTLookupVectorHeader     init(theArray theArray: SFNTLookupArrayHeader)     init(segment segment: SFNTLookupSegmentHeader)     init(single single: SFNTLookupSingleHeader)     init(trimmedArray trimmedArray: SFNTLookupTrimmedArrayHeader)     init(vector vector: SFNTLookupVectorHeader)     init() } ``` |

Modified [CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_: CTFontCollection, _: CoreText.CTFontCollectionSortDescriptorsCallback?, _: UnsafeMutableRawPointer?) -> CFArray?](https://developer.apple.com/documentation/coretext/1510434-ctfontcollectioncreatematchingfo)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_ collection: CTFontCollection, _ sortCallback: CTFontCollectionSortDescriptorsCallback?, _ refCon: UnsafeMutablePointer<Void>) -> CFArray? ``` |
| To | ``` func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_ collection: CTFontCollection, _ sortCallback: CoreText.CTFontCollectionSortDescriptorsCallback?, _ refCon: UnsafeMutableRawPointer?) -> CFArray? ``` |

Modified [CTFontCollectionSortDescriptorsCallback](https://developer.apple.com/documentation/coretext/ctfontcollectionsortdescriptorscallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTFontCollectionSortDescriptorsCallback = (CTFontDescriptor, CTFontDescriptor, UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |
| To | ``` typealias CTFontCollectionSortDescriptorsCallback = (CTFontDescriptor, CTFontDescriptor, UnsafeMutableRawPointer) -> CFComparisonResult ``` |

Modified [CTFontCopyAttribute(_: CTFont, _: CFString) -> CFTypeRef?](https://developer.apple.com/documentation/coretext/1508984-ctfontcopyattribute)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyAttribute(_ font: CTFont, _ attribute: CFString) -> AnyObject? ``` |
| To | ``` func CTFontCopyAttribute(_ font: CTFont, _ attribute: CFString) -> CFTypeRef? ``` |

Modified [CTFontCopyGraphicsFont(_: CTFont, _: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont](https://developer.apple.com/documentation/coretext/1508712-ctfontcopygraphicsfont)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyGraphicsFont(_ font: CTFont, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> CGFont ``` |
| To | ``` func CTFontCopyGraphicsFont(_ font: CTFont, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>?) -> CGFont ``` |

Modified [CTFontCopyLocalizedName(_: CTFont, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?](https://developer.apple.com/documentation/coretext/1510714-ctfontcopylocalizedname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCopyLocalizedName(_ font: CTFont, _ nameKey: CFString, _ actualLanguage: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFString? ``` |
| To | ``` func CTFontCopyLocalizedName(_ font: CTFont, _ nameKey: CFString, _ actualLanguage: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString? ``` |

Modified [CTFontCreateCopyWithAttributes(_: CTFont, _: CGFloat, _: UnsafePointer<CGAffineTransform>?, _: CTFontDescriptor?) -> CTFont](https://developer.apple.com/documentation/coretext/1511225-ctfontcreatecopywithattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateCopyWithAttributes(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor?) -> CTFont ``` |
| To | ``` func CTFontCreateCopyWithAttributes(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ attributes: CTFontDescriptor?) -> CTFont ``` |

Modified [CTFontCreateCopyWithFamily(_: CTFont, _: CGFloat, _: UnsafePointer<CGAffineTransform>?, _: CFString) -> CTFont?](https://developer.apple.com/documentation/coretext/1510945-ctfontcreatecopywithfamily)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateCopyWithFamily(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ family: CFString) -> CTFont? ``` |
| To | ``` func CTFontCreateCopyWithFamily(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ family: CFString) -> CTFont? ``` |

Modified [CTFontCreateCopyWithSymbolicTraits(_: CTFont, _: CGFloat, _: UnsafePointer<CGAffineTransform>?, _: CTFontSymbolicTraits, _: CTFontSymbolicTraits) -> CTFont?](https://developer.apple.com/documentation/coretext/1511394-ctfontcreatecopywithsymbolictrai)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateCopyWithSymbolicTraits(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFont? ``` |
| To | ``` func CTFontCreateCopyWithSymbolicTraits(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFont? ``` |

Modified [CTFontCreatePathForGlyph(_: CTFont, _: CGGlyph, _: UnsafePointer<CGAffineTransform>?) -> CGPath?](https://developer.apple.com/documentation/coretext/1510921-ctfontcreatepathforglyph)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreatePathForGlyph(_ font: CTFont, _ glyph: CGGlyph, _ matrix: UnsafePointer<CGAffineTransform>) -> CGPath? ``` |
| To | ``` func CTFontCreatePathForGlyph(_ font: CTFont, _ glyph: CGGlyph, _ matrix: UnsafePointer<CGAffineTransform>?) -> CGPath? ``` |

Modified [CTFontCreateWithFontDescriptor(_: CTFontDescriptor, _: CGFloat, _: UnsafePointer<CGAffineTransform>?) -> CTFont](https://developer.apple.com/documentation/coretext/1509056-ctfontcreatewithfontdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithFontDescriptor(_ descriptor: CTFontDescriptor, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>) -> CTFont ``` |
| To | ``` func CTFontCreateWithFontDescriptor(_ descriptor: CTFontDescriptor, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?) -> CTFont ``` |

Modified [CTFontCreateWithFontDescriptorAndOptions(_: CTFontDescriptor, _: CGFloat, _: UnsafePointer<CGAffineTransform>?, _: CTFontOptions) -> CTFont](https://developer.apple.com/documentation/coretext/1510463-ctfontcreatewithfontdescriptoran)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithFontDescriptorAndOptions(_ descriptor: CTFontDescriptor, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont ``` |
| To | ``` func CTFontCreateWithFontDescriptorAndOptions(_ descriptor: CTFontDescriptor, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ options: CTFontOptions) -> CTFont ``` |

Modified [CTFontCreateWithGraphicsFont(_: CGFont, _: CGFloat, _: UnsafePointer<CGAffineTransform>?, _: CTFontDescriptor?) -> CTFont](https://developer.apple.com/documentation/coretext/1508745-ctfontcreatewithgraphicsfont)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithGraphicsFont(_ graphicsFont: CGFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor?) -> CTFont ``` |
| To | ``` func CTFontCreateWithGraphicsFont(_ graphicsFont: CGFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ attributes: CTFontDescriptor?) -> CTFont ``` |

Modified [CTFontCreateWithName(_: CFString?, _: CGFloat, _: UnsafePointer<CGAffineTransform>?) -> CTFont](https://developer.apple.com/documentation/coretext/1509153-ctfontcreatewithname)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithName(_ name: CFString?, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>) -> CTFont ``` |
| To | ``` func CTFontCreateWithName(_ name: CFString?, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?) -> CTFont ``` |

Modified [CTFontCreateWithNameAndOptions(_: CFString, _: CGFloat, _: UnsafePointer<CGAffineTransform>?, _: CTFontOptions) -> CTFont](https://developer.apple.com/documentation/coretext/1508624-ctfontcreatewithnameandoptions)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontCreateWithNameAndOptions(_ name: CFString, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont ``` |
| To | ``` func CTFontCreateWithNameAndOptions(_ name: CFString, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ options: CTFontOptions) -> CTFont ``` |

Modified [CTFontDescriptorCopyAttribute(_: CTFontDescriptor, _: CFString) -> CFTypeRef?](https://developer.apple.com/documentation/coretext/1510346-ctfontdescriptorcopyattribute)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCopyAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString) -> AnyObject? ``` |
| To | ``` func CTFontDescriptorCopyAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString) -> CFTypeRef? ``` |

Modified [CTFontDescriptorCopyLocalizedAttribute(_: CTFontDescriptor, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFTypeRef?](https://developer.apple.com/documentation/coretext/1509510-ctfontdescriptorcopylocalizedatt)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorCopyLocalizedAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString, _ language: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject? ``` |
| To | ``` func CTFontDescriptorCopyLocalizedAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString, _ language: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFTypeRef? ``` |

Modified [CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_: CFArray, _: CFSet?, _: CoreText.CTFontDescriptorProgressHandler) -> Bool](https://developer.apple.com/documentation/coretext/1511433-ctfontdescriptormatchfontdescrip)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_ descriptors: CFArray, _ mandatoryAttributes: CFSet?, _ progressBlock: CTFontDescriptorProgressHandler) -> Bool ``` |
| To | ``` func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_ descriptors: CFArray, _ mandatoryAttributes: CFSet?, _ progressBlock: CoreText.CTFontDescriptorProgressHandler) -> Bool ``` |

Modified [CTFontDrawGlyphs(_: CTFont, _: UnsafePointer<CGGlyph>!, _: UnsafePointer<CGPoint>!, _: Int, _: CGContext)](https://developer.apple.com/documentation/coretext/1509850-ctfontdrawglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontDrawGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int, _ context: CGContext) ``` |
| To | ``` func CTFontDrawGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>!, _ positions: UnsafePointer<CGPoint>!, _ count: Int, _ context: CGContext) ``` |

Modified [CTFontGetAdvancesForGlyphs(_: CTFont, _: CTFontOrientation, _: UnsafePointer<CGGlyph>!, _: UnsafeMutablePointer<CGSize>?, _: CFIndex) -> Double](https://developer.apple.com/documentation/coretext/1511265-ctfontgetadvancesforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetAdvancesForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ advances: UnsafeMutablePointer<CGSize>, _ count: CFIndex) -> Double ``` |
| To | ``` func CTFontGetAdvancesForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>!, _ advances: UnsafeMutablePointer<CGSize>?, _ count: CFIndex) -> Double ``` |

Modified [CTFontGetBoundingRectsForGlyphs(_: CTFont, _: CTFontOrientation, _: UnsafePointer<CGGlyph>!, _: UnsafeMutablePointer<CGRect>?, _: CFIndex) -> CGRect](https://developer.apple.com/documentation/coretext/1509419-ctfontgetboundingrectsforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetBoundingRectsForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>, _ count: CFIndex) -> CGRect ``` |
| To | ``` func CTFontGetBoundingRectsForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>!, _ boundingRects: UnsafeMutablePointer<CGRect>?, _ count: CFIndex) -> CGRect ``` |

Modified [CTFontGetGlyphsForCharacters(_: CTFont, _: UnsafePointer<UniChar>!, _: UnsafeMutablePointer<CGGlyph>!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/coretext/1510813-ctfontgetglyphsforcharacters)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetGlyphsForCharacters(_ font: CTFont, _ characters: UnsafePointer<UniChar>, _ glyphs: UnsafeMutablePointer<CGGlyph>, _ count: CFIndex) -> Bool ``` |
| To | ``` func CTFontGetGlyphsForCharacters(_ font: CTFont, _ characters: UnsafePointer<UniChar>!, _ glyphs: UnsafeMutablePointer<CGGlyph>!, _ count: CFIndex) -> Bool ``` |

Modified [CTFontGetLigatureCaretPositions(_: CTFont, _: CGGlyph, _: UnsafeMutablePointer<CGFloat>?, _: CFIndex) -> CFIndex](https://developer.apple.com/documentation/coretext/1508820-ctfontgetligaturecaretpositions)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetLigatureCaretPositions(_ font: CTFont, _ glyph: CGGlyph, _ positions: UnsafeMutablePointer<CGFloat>, _ maxPositions: CFIndex) -> CFIndex ``` |
| To | ``` func CTFontGetLigatureCaretPositions(_ font: CTFont, _ glyph: CGGlyph, _ positions: UnsafeMutablePointer<CGFloat>?, _ maxPositions: CFIndex) -> CFIndex ``` |

Modified [CTFontGetOpticalBoundsForGlyphs(_: CTFont, _: UnsafePointer<CGGlyph>!, _: UnsafeMutablePointer<CGRect>?, _: CFIndex, _: CFOptionFlags) -> CGRect](https://developer.apple.com/documentation/coretext/1510531-ctfontgetopticalboundsforglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetOpticalBoundsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>, _ count: CFIndex, _ options: CFOptionFlags) -> CGRect ``` |
| To | ``` func CTFontGetOpticalBoundsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>!, _ boundingRects: UnsafeMutablePointer<CGRect>?, _ count: CFIndex, _ options: CFOptionFlags) -> CGRect ``` |

Modified [CTFontGetVerticalTranslationsForGlyphs(_: CTFont, _: UnsafePointer<CGGlyph>!, _: UnsafeMutablePointer<CGSize>!, _: CFIndex)](https://developer.apple.com/documentation/coretext/1511102-ctfontgetverticaltranslationsfor)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontGetVerticalTranslationsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ translations: UnsafeMutablePointer<CGSize>, _ count: CFIndex) ``` |
| To | ``` func CTFontGetVerticalTranslationsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>!, _ translations: UnsafeMutablePointer<CGSize>!, _ count: CFIndex) ``` |

Modified [CTFontManagerRegisterFontsForURL(_: CFURL, _: CTFontManagerScope, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/coretext/1499468-ctfontmanagerregisterfontsforurl)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerRegisterFontsForURL(_ fontURL: CFURL, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CTFontManagerRegisterFontsForURL(_ fontURL: CFURL, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool ``` |

Modified [CTFontManagerRegisterFontsForURLs(_: CFArray, _: CTFontManagerScope, _: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool](https://developer.apple.com/documentation/coretext/1499470-ctfontmanagerregisterfontsforurl)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerRegisterFontsForURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool ``` |
| To | ``` func CTFontManagerRegisterFontsForURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool ``` |

Modified [CTFontManagerRegisterGraphicsFont(_: CGFont, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/coretext/1499499-ctfontmanagerregistergraphicsfon)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerRegisterGraphicsFont(_ font: CGFont, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CTFontManagerRegisterGraphicsFont(_ font: CGFont, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool ``` |

Modified [CTFontManagerUnregisterFontsForURL(_: CFURL, _: CTFontManagerScope, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/coretext/1499496-ctfontmanagerunregisterfontsforu)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerUnregisterFontsForURL(_ fontURL: CFURL, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CTFontManagerUnregisterFontsForURL(_ fontURL: CFURL, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool ``` |

Modified [CTFontManagerUnregisterFontsForURLs(_: CFArray, _: CTFontManagerScope, _: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool](https://developer.apple.com/documentation/coretext/1499477-ctfontmanagerunregisterfontsforu)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerUnregisterFontsForURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool ``` |
| To | ``` func CTFontManagerUnregisterFontsForURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool ``` |

Modified [CTFontManagerUnregisterGraphicsFont(_: CGFont, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/coretext/1499472-ctfontmanagerunregistergraphicsf)

|  | Declaration |
| --- | --- |
| From | ``` func CTFontManagerUnregisterGraphicsFont(_ font: CGFont, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CTFontManagerUnregisterGraphicsFont(_ font: CGFont, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool ``` |

Modified [CTFrameGetLineOrigins(_: CTFrame, _: CFRange, _: UnsafeMutablePointer<CGPoint>!)](https://developer.apple.com/documentation/coretext/1510610-ctframegetlineorigins)

|  | Declaration |
| --- | --- |
| From | ``` func CTFrameGetLineOrigins(_ frame: CTFrame, _ range: CFRange, _ origins: UnsafeMutablePointer<CGPoint>) ``` |
| To | ``` func CTFrameGetLineOrigins(_ frame: CTFrame, _ range: CFRange, _ origins: UnsafeMutablePointer<CGPoint>!) ``` |

Modified [CTFramesetterSuggestFrameSizeWithConstraints(_: CTFramesetter, _: CFRange, _: CFDictionary?, _: CGSize, _: UnsafeMutablePointer<CFRange>?) -> CGSize](https://developer.apple.com/documentation/coretext/1478566-ctframesettersuggestframesizewit)

|  | Declaration |
| --- | --- |
| From | ``` func CTFramesetterSuggestFrameSizeWithConstraints(_ framesetter: CTFramesetter, _ stringRange: CFRange, _ frameAttributes: CFDictionary?, _ constraints: CGSize, _ fitRange: UnsafeMutablePointer<CFRange>) -> CGSize ``` |
| To | ``` func CTFramesetterSuggestFrameSizeWithConstraints(_ framesetter: CTFramesetter, _ stringRange: CFRange, _ frameAttributes: CFDictionary?, _ constraints: CGSize, _ fitRange: UnsafeMutablePointer<CFRange>?) -> CGSize ``` |

Modified [CTLineEnumerateCaretOffsets(_: CTLine, _: (Double, CFIndex, Bool, UnsafeMutablePointer<Bool>) -> Swift.Void)](https://developer.apple.com/documentation/coretext/1508685-ctlineenumeratecaretoffsets)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineEnumerateCaretOffsets(_ line: CTLine, _ block: (Double, CFIndex, Bool, UnsafeMutablePointer<Bool>) -> Void) ``` |
| To | ``` func CTLineEnumerateCaretOffsets(_ line: CTLine, _ block: @escaping (Double, CFIndex, Bool, UnsafeMutablePointer<Bool>) -> Swift.Void) ``` |

Modified [CTLineGetOffsetForStringIndex(_: CTLine, _: CFIndex, _: UnsafeMutablePointer<CGFloat>?) -> CGFloat](https://developer.apple.com/documentation/coretext/1509629-ctlinegetoffsetforstringindex)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetOffsetForStringIndex(_ line: CTLine, _ charIndex: CFIndex, _ secondaryOffset: UnsafeMutablePointer<CGFloat>) -> CGFloat ``` |
| To | ``` func CTLineGetOffsetForStringIndex(_ line: CTLine, _ charIndex: CFIndex, _ secondaryOffset: UnsafeMutablePointer<CGFloat>?) -> CGFloat ``` |

Modified [CTLineGetTypographicBounds(_: CTLine, _: UnsafeMutablePointer<CGFloat>?, _: UnsafeMutablePointer<CGFloat>?, _: UnsafeMutablePointer<CGFloat>?) -> Double](https://developer.apple.com/documentation/coretext/1510360-ctlinegettypographicbounds)

|  | Declaration |
| --- | --- |
| From | ``` func CTLineGetTypographicBounds(_ line: CTLine, _ ascent: UnsafeMutablePointer<CGFloat>, _ descent: UnsafeMutablePointer<CGFloat>, _ leading: UnsafeMutablePointer<CGFloat>) -> Double ``` |
| To | ``` func CTLineGetTypographicBounds(_ line: CTLine, _ ascent: UnsafeMutablePointer<CGFloat>?, _ descent: UnsafeMutablePointer<CGFloat>?, _ leading: UnsafeMutablePointer<CGFloat>?) -> Double ``` |

Modified [CTParagraphStyleCreate(_: UnsafePointer<CTParagraphStyleSetting>?, _: Int) -> CTParagraphStyle](https://developer.apple.com/documentation/coretext/1496164-ctparagraphstylecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CTParagraphStyleCreate(_ settings: UnsafePointer<CTParagraphStyleSetting>, _ settingCount: Int) -> CTParagraphStyle ``` |
| To | ``` func CTParagraphStyleCreate(_ settings: UnsafePointer<CTParagraphStyleSetting>?, _ settingCount: Int) -> CTParagraphStyle ``` |

Modified [CTParagraphStyleGetValueForSpecifier(_: CTParagraphStyle, _: CTParagraphStyleSpecifier, _: Int, _: UnsafeMutableRawPointer) -> Bool](https://developer.apple.com/documentation/coretext/1496169-ctparagraphstylegetvalueforspeci)

|  | Declaration |
| --- | --- |
| From | ``` func CTParagraphStyleGetValueForSpecifier(_ paragraphStyle: CTParagraphStyle, _ spec: CTParagraphStyleSpecifier, _ valueBufferSize: Int, _ valueBuffer: UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` func CTParagraphStyleGetValueForSpecifier(_ paragraphStyle: CTParagraphStyle, _ spec: CTParagraphStyleSpecifier, _ valueBufferSize: Int, _ valueBuffer: UnsafeMutableRawPointer) -> Bool ``` |

Modified [CTRubyAnnotationCreate(_: CTRubyAlignment, _: CTRubyOverhang, _: CGFloat, _: UnsafeMutablePointer<Unmanaged<CFString>>!) -> CTRubyAnnotation](https://developer.apple.com/documentation/coretext/1510191-ctrubyannotationcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CTRubyAnnotationCreate(_ alignment: CTRubyAlignment, _ overhang: CTRubyOverhang, _ sizeFactor: CGFloat, _ text: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CTRubyAnnotation ``` |
| To | ``` func CTRubyAnnotationCreate(_ alignment: CTRubyAlignment, _ overhang: CTRubyOverhang, _ sizeFactor: CGFloat, _ text: UnsafeMutablePointer<Unmanaged<CFString>>!) -> CTRubyAnnotation ``` |

Modified [CTRunDelegateCreate(_: UnsafePointer<CTRunDelegateCallbacks>, _: UnsafeMutableRawPointer?) -> CTRunDelegate?](https://developer.apple.com/documentation/coretext/1498167-ctrundelegatecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunDelegateCreate(_ callbacks: UnsafePointer<CTRunDelegateCallbacks>, _ refCon: UnsafeMutablePointer<Void>) -> CTRunDelegate? ``` |
| To | ``` func CTRunDelegateCreate(_ callbacks: UnsafePointer<CTRunDelegateCallbacks>, _ refCon: UnsafeMutableRawPointer?) -> CTRunDelegate? ``` |

Modified [CTRunDelegateDeallocateCallback](https://developer.apple.com/documentation/coretext/ctrundelegatedeallocatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateDeallocateCallback = (UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CTRunDelegateDeallocateCallback = (UnsafeMutableRawPointer) -> Swift.Void ``` |

Modified [CTRunDelegateGetAscentCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetascentcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetAscentCallback = (UnsafeMutablePointer<Void>) -> CGFloat ``` |
| To | ``` typealias CTRunDelegateGetAscentCallback = (UnsafeMutableRawPointer) -> CGFloat ``` |

Modified [CTRunDelegateGetDescentCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetdescentcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetDescentCallback = (UnsafeMutablePointer<Void>) -> CGFloat ``` |
| To | ``` typealias CTRunDelegateGetDescentCallback = (UnsafeMutableRawPointer) -> CGFloat ``` |

Modified [CTRunDelegateGetRefCon(_: CTRunDelegate) -> UnsafeMutableRawPointer](https://developer.apple.com/documentation/coretext/1498169-ctrundelegategetrefcon)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunDelegateGetRefCon(_ runDelegate: CTRunDelegate) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CTRunDelegateGetRefCon(_ runDelegate: CTRunDelegate) -> UnsafeMutableRawPointer ``` |

Modified [CTRunDelegateGetWidthCallback](https://developer.apple.com/documentation/coretext/ctrundelegategetwidthcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetWidthCallback = (UnsafeMutablePointer<Void>) -> CGFloat ``` |
| To | ``` typealias CTRunDelegateGetWidthCallback = (UnsafeMutableRawPointer) -> CGFloat ``` |

Modified [CTRunGetAdvances(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CGSize>!)](https://developer.apple.com/documentation/coretext/1510488-ctrungetadvances)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetAdvances(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGSize>) ``` |
| To | ``` func CTRunGetAdvances(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGSize>!) ``` |

Modified [CTRunGetAdvancesPtr(_: CTRun) -> UnsafePointer<CGSize>?](https://developer.apple.com/documentation/coretext/1508625-ctrungetadvancesptr)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetAdvancesPtr(_ run: CTRun) -> UnsafePointer<CGSize> ``` |
| To | ``` func CTRunGetAdvancesPtr(_ run: CTRun) -> UnsafePointer<CGSize>? ``` |

Modified [CTRunGetGlyphs(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CGGlyph>!)](https://developer.apple.com/documentation/coretext/1509249-ctrungetglyphs)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetGlyphs(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGGlyph>) ``` |
| To | ``` func CTRunGetGlyphs(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGGlyph>!) ``` |

Modified [CTRunGetGlyphsPtr(_: CTRun) -> UnsafePointer<CGGlyph>?](https://developer.apple.com/documentation/coretext/1509952-ctrungetglyphsptr)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetGlyphsPtr(_ run: CTRun) -> UnsafePointer<CGGlyph> ``` |
| To | ``` func CTRunGetGlyphsPtr(_ run: CTRun) -> UnsafePointer<CGGlyph>? ``` |

Modified [CTRunGetPositions(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CGPoint>!)](https://developer.apple.com/documentation/coretext/1508678-ctrungetpositions)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetPositions(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGPoint>) ``` |
| To | ``` func CTRunGetPositions(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGPoint>!) ``` |

Modified [CTRunGetPositionsPtr(_: CTRun) -> UnsafePointer<CGPoint>?](https://developer.apple.com/documentation/coretext/1510044-ctrungetpositionsptr)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetPositionsPtr(_ run: CTRun) -> UnsafePointer<CGPoint> ``` |
| To | ``` func CTRunGetPositionsPtr(_ run: CTRun) -> UnsafePointer<CGPoint>? ``` |

Modified [CTRunGetStringIndices(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CFIndex>!)](https://developer.apple.com/documentation/coretext/1511382-ctrungetstringindices)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetStringIndices(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CFIndex>) ``` |
| To | ``` func CTRunGetStringIndices(_ run: CTRun, _ range: CFRange, _ buffer: UnsafeMutablePointer<CFIndex>!) ``` |

Modified [CTRunGetStringIndicesPtr(_: CTRun) -> UnsafePointer<CFIndex>?](https://developer.apple.com/documentation/coretext/1510605-ctrungetstringindicesptr)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetStringIndicesPtr(_ run: CTRun) -> UnsafePointer<CFIndex> ``` |
| To | ``` func CTRunGetStringIndicesPtr(_ run: CTRun) -> UnsafePointer<CFIndex>? ``` |

Modified [CTRunGetTypographicBounds(_: CTRun, _: CFRange, _: UnsafeMutablePointer<CGFloat>?, _: UnsafeMutablePointer<CGFloat>?, _: UnsafeMutablePointer<CGFloat>?) -> Double](https://developer.apple.com/documentation/coretext/1510569-ctrungettypographicbounds)

|  | Declaration |
| --- | --- |
| From | ``` func CTRunGetTypographicBounds(_ run: CTRun, _ range: CFRange, _ ascent: UnsafeMutablePointer<CGFloat>, _ descent: UnsafeMutablePointer<CGFloat>, _ leading: UnsafeMutablePointer<CGFloat>) -> Double ``` |
| To | ``` func CTRunGetTypographicBounds(_ run: CTRun, _ range: CFRange, _ ascent: UnsafeMutablePointer<CGFloat>?, _ descent: UnsafeMutablePointer<CGFloat>?, _ leading: UnsafeMutablePointer<CGFloat>?) -> Double ``` |

Modified KernTableHeaderHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias KernTableHeaderHandle = UnsafeMutablePointer<KernTableHeaderPtr> ``` |
| To | ``` typealias KernTableHeaderHandle = UnsafeMutablePointer<KernTableHeaderPtr?> ``` |

Modified KerxTableHeaderHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias KerxTableHeaderHandle = UnsafeMutablePointer<KerxTableHeaderPtr> ``` |
| To | ``` typealias KerxTableHeaderHandle = UnsafeMutablePointer<KerxTableHeaderPtr?> ``` |

Modified SFNTLookupTableHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias SFNTLookupTableHandle = UnsafeMutablePointer<SFNTLookupTablePtr> ``` |
| To | ``` typealias SFNTLookupTableHandle = UnsafeMutablePointer<SFNTLookupTablePtr?> ``` |

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
