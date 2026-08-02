---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/ApplicationServices.html
archived_at: '2026-07-18T02:53:18.675750Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ApplicationServices Changes for Swift

### ApplicationServices

Removed ATSFontFilterSelector.valueRemoved ATSFontNotifyAction.valueRemoved ATSFontNotifyOption.valueRemoved ATSFontQueryMessageID.valueRemoved ATSFontQuerySourceContext.init(version: UInt32, refCon: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack)Removed ATSULayoutOperationOverrideSpecifier.init(operationSelector: ATSULayoutOperationSelector, overrideUPP: ATSUDirectLayoutOperationOverrideUPP)Removed AXValueType [struct]Removed AXValueType.init(_: UInt32)Removed AXValueType.valueRemoved CMFloatBitmapFlags.valueRemoved ColorSyncAlphaInfo.valueRemoved ColorSyncDataDepth.valueRemoved CQDProcs.init(textProc: QDTextUPP, lineProc: QDLineUPP, rectProc: QDRectUPP, rRectProc: QDRRectUPP, ovalProc: QDOvalUPP, arcProc: QDArcUPP, polyProc: QDPolyUPP, rgnProc: QDRgnUPP, bitsProc: QDBitsUPP, commentProc: QDCommentUPP, txMeasProc: QDTxMeasUPP, getPicProc: QDGetPicUPP, putPicProc: QDPutPicUPP, opcodeProc: QDOpcodeUPP, newProc1: UniversalProcPtr, glyphsProc: QDStdGlyphsUPP, printerStatusProc: QDPrinterStatusUPP, newProc4: UniversalProcPtr, newProc5: UniversalProcPtr, newProc6: UniversalProcPtr)Removed FMInput.init(family: Int16, size: Int16, face: Style, needBits: Boolean, device: Int16, numer: Point, denom: Point)Removed PMDataFormat.valueRemoved PMPageToPaperMappingType.valueRemoved SpeechStatusInfo.init(outputBusy: Boolean, outputPaused: Boolean, inputBytesLeft: Int, phonemeCode: Int16)Removed AXCopyMultipleAttributeOptionsRemoved AXErrorRemoved AXMenuItemModifiersRemoved AXUnderlineStyleRemoved cmTextureRGBtoRGBX16Removed cmTextureRGBtoRGBX8Removed cmTextureRGBtoRGBXFloat32Removed [DisposeCMBitmapCallBackUPP(_: CMBitmapCallBackUPP)](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805300-disposecmbitmapcallbackupp)Removed [DisposeCMConcatCallBackUPP(_: CMConcatCallBackUPP)](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805310-disposecmconcatcallbackupp)Removed [DisposeCMFlattenUPP(_: CMFlattenUPP)](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805318-disposecmflattenupp)Removed [DisposeCMMIterateUPP(_: CMMIterateUPP)](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805323-disposecmmiterateupp)Removed [DisposeCMProfileIterateUPP(_: CMProfileIterateUPP)](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805341-disposecmprofileiterateupp)Removed [InvokeCMBitmapCallBackUPP(_: Int32, _: UnsafeMutablePointer<Void>, _: CMBitmapCallBackUPP) -> Boolean](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805303-invokecmbitmapcallbackupp)Removed [InvokeCMConcatCallBackUPP(_: Int32, _: UnsafeMutablePointer<Void>, _: CMConcatCallBackUPP) -> Boolean](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805312-invokecmconcatcallbackupp)Removed [InvokeCMFlattenUPP(_: Int32, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<Void>, _: CMFlattenUPP) -> OSErr](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805320-invokecmflattenupp)Removed [InvokeCMMIterateUPP(_: UnsafeMutablePointer<CMMInfo>, _: UnsafeMutablePointer<Void>, _: CMMIterateUPP) -> OSErr](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805325-invokecmmiterateupp)Removed [InvokeCMProfileIterateUPP(_: UnsafeMutablePointer<CMProfileIterateData>, _: UnsafeMutablePointer<Void>, _: CMProfileIterateUPP) -> OSErr](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805343-invokecmprofileiterateupp)Removed kAXCopyMultipleAttributeOptionStopOnErrorRemoved kAXErrorActionUnsupportedRemoved kAXErrorAPIDisabledRemoved kAXErrorAttributeUnsupportedRemoved kAXErrorCannotCompleteRemoved kAXErrorFailureRemoved kAXErrorIllegalArgumentRemoved kAXErrorInvalidUIElementRemoved kAXErrorInvalidUIElementObserverRemoved kAXErrorNotEnoughPrecisionRemoved kAXErrorNotificationAlreadyRegisteredRemoved kAXErrorNotificationNotRegisteredRemoved kAXErrorNotificationUnsupportedRemoved kAXErrorNotImplementedRemoved kAXErrorNoValueRemoved kAXErrorParameterizedAttributeUnsupportedRemoved kAXErrorSuccessRemoved kAXMenuItemModifierControlRemoved kAXMenuItemModifierNoCommandRemoved kAXMenuItemModifierNoneRemoved kAXMenuItemModifierOptionRemoved kAXMenuItemModifierShiftRemoved kAXUnderlineStyleDoubleRemoved kAXUnderlineStyleNoneRemoved kAXUnderlineStyleSingleRemoved kAXUnderlineStyleThickRemoved [NewCMBitmapCallBackUPP(_: CMBitmapCallBackProcPtr) -> CMBitmapCallBackUPP](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805297-newcmbitmapcallbackupp)Removed [NewCMConcatCallBackUPP(_: CMConcatCallBackProcPtr) -> CMConcatCallBackUPP](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805306-newcmconcatcallbackupp)Removed [NewCMFlattenUPP(_: CMFlattenProcPtr) -> CMFlattenUPP](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805315-newcmflattenupp)Removed [NewCMMIterateUPP(_: CMMIterateProcPtr) -> CMMIterateUPP](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805322-newcmmiterateupp)Removed [NewCMProfileIterateUPP(_: CMProfileIterateProcPtr) -> CMProfileIterateUPP](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805339-newcmprofileiterateupp)Added ATSFontFilterSelector.init(rawValue: UInt32)Added ATSFontFilterSelector.rawValueAdded ATSFontNotifyAction.init(rawValue: UInt32)Added ATSFontNotifyAction.rawValueAdded ATSFontNotifyOption.init(rawValue: UInt32)Added ATSFontNotifyOption.rawValueAdded ATSFontQueryMessageID.init(rawValue: UInt32)Added ATSFontQueryMessageID.rawValueAdded ATSFontQuerySourceContext.init(version: UInt32, refCon: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!)Added ATSULayoutOperationOverrideSpecifier.init(operationSelector: ATSULayoutOperationSelector, overrideUPP: ATSUDirectLayoutOperationOverrideUPP!)Added [AXCopyMultipleAttributeOptions [struct]](https://developer.apple.com/documentation/applicationservices/axcopymultipleattributeoptions)Added AXCopyMultipleAttributeOptions.init(rawValue: UInt32)Added [AXCopyMultipleAttributeOptions.StopOnError](https://developer.apple.com/documentation/applicationservices/axcopymultipleattributeoptions/1460788-stoponerror)Added [AXError [enum]](https://developer.apple.com/documentation/applicationservices/axerror)Added [AXError.ActionUnsupported](https://developer.apple.com/documentation/applicationservices/axerror/kaxerroractionunsupported)Added [AXError.APIDisabled](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorapidisabled)Added [AXError.AttributeUnsupported](https://developer.apple.com/documentation/applicationservices/axerror/attributeunsupported)Added [AXError.CannotComplete](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorcannotcomplete)Added [AXError.Failure](https://developer.apple.com/documentation/applicationservices/axerror/failure)Added [AXError.IllegalArgument](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorillegalargument)Added [AXError.InvalidUIElement](https://developer.apple.com/documentation/applicationservices/axerror/invaliduielement)Added [AXError.InvalidUIElementObserver](https://developer.apple.com/documentation/applicationservices/axerror/invaliduielementobserver)Added [AXError.NotEnoughPrecision](https://developer.apple.com/documentation/applicationservices/axerror/notenoughprecision)Added [AXError.NotificationAlreadyRegistered](https://developer.apple.com/documentation/applicationservices/axerror/notificationalreadyregistered)Added [AXError.NotificationNotRegistered](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrornotificationnotregistered)Added [AXError.NotificationUnsupported](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrornotificationunsupported)Added [AXError.NotImplemented](https://developer.apple.com/documentation/applicationservices/axerror/notimplemented)Added [AXError.NoValue](https://developer.apple.com/documentation/applicationservices/axerror/novalue)Added [AXError.ParameterizedAttributeUnsupported](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorparameterizedattributeunsupported)Added [AXError.Success](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorsuccess)Added [AXMenuItemModifiers [struct]](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers)Added [AXMenuItemModifiers.Control](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/1464333-control)Added AXMenuItemModifiers.init(rawValue: UInt32)Added [AXMenuItemModifiers.NoCommand](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifiernocommand)Added [AXMenuItemModifiers.None](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifiernone)Added [AXMenuItemModifiers.Option](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifieroption)Added [AXMenuItemModifiers.Shift](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifiershift)Added [AXUnderlineStyle [enum]](https://developer.apple.com/documentation/applicationservices/axunderlinestyle)Added [AXUnderlineStyle.Double](https://developer.apple.com/documentation/applicationservices/axunderlinestyle/kaxunderlinestyledouble)Added [AXUnderlineStyle.None](https://developer.apple.com/documentation/applicationservices/axunderlinestyle/kaxunderlinestylenone)Added [AXUnderlineStyle.Single](https://developer.apple.com/documentation/applicationservices/axunderlinestyle/kaxunderlinestylesingle)Added [AXUnderlineStyle.Thick](https://developer.apple.com/documentation/applicationservices/axunderlinestyle/thick)Added [AXValueType [enum]](https://developer.apple.com/documentation/applicationservices/axvaluetype)Added [AXValueType.AXError](https://developer.apple.com/documentation/applicationservices/axvaluetype/axerror)Added [AXValueType.CFRange](https://developer.apple.com/documentation/applicationservices/axvaluetype/cfrange)Added [AXValueType.CGPoint](https://developer.apple.com/documentation/applicationservices/axvaluetype/cgpoint)Added [AXValueType.CGRect](https://developer.apple.com/documentation/applicationservices/axvaluetype/cgrect)Added [AXValueType.CGSize](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvaluetypecgsize)Added [AXValueType.Illegal](https://developer.apple.com/documentation/applicationservices/axvaluetype/illegal)Added CMFloatBitmapFlags.init(rawValue: UInt32)Added CMFloatBitmapFlags.rawValueAdded ColorSyncAlphaInfo.init(rawValue: UInt32)Added ColorSyncAlphaInfo.rawValueAdded ColorSyncDataDepth.init(rawValue: UInt32)Added ColorSyncDataDepth.rawValueAdded CQDProcs.init(textProc: QDTextUPP!, lineProc: QDLineUPP!, rectProc: QDRectUPP!, rRectProc: QDRRectUPP!, ovalProc: QDOvalUPP!, arcProc: QDArcUPP!, polyProc: QDPolyUPP!, rgnProc: QDRgnUPP!, bitsProc: QDBitsUPP!, commentProc: QDCommentUPP!, txMeasProc: QDTxMeasUPP!, getPicProc: QDGetPicUPP!, putPicProc: QDPutPicUPP!, opcodeProc: QDOpcodeUPP!, newProc1: UniversalProcPtr!, glyphsProc: QDStdGlyphsUPP!, printerStatusProc: QDPrinterStatusUPP!, newProc4: UniversalProcPtr!, newProc5: UniversalProcPtr!, newProc6: UniversalProcPtr!)Added FMInput.init(family: Int16, size: Int16, face: Style, needBits: DarwinBoolean, device: Int16, numer: Point, denom: Point)Added ICMapEntry.init(totalLength: Int16, fixedLength: ICFixedLength, version: Int16, fileType: OSType, fileCreator: OSType, postCreator: OSType, flags: ICMapEntryFlags, extension: Str255, creatorAppName: Str255, postAppName: Str255, MIMEType: Str255, entryName: Str255)Added PMDataFormat.init(rawValue: UInt32)Added PMDataFormat.rawValueAdded PMPageToPaperMappingType.init(rawValue: UInt32)Added PMPageToPaperMappingType.rawValueAdded SpeechStatusInfo.init(outputBusy: DarwinBoolean, outputPaused: DarwinBoolean, inputBytesLeft: Int, phonemeCode: Int16)Added [COLORSYNC_PROFILE_INSTALL_ENTITLEMENT](https://developer.apple.com/documentation/colorsync/colorsync_profile_install_entitlement)Added [ColorSyncProfileInstall(_: ColorSyncProfile!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/colorsync/1463116-colorsyncprofileinstall)Added [ColorSyncProfileUninstall(_: ColorSyncProfile!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/colorsync/1458805-colorsyncprofileuninstall)Added [kAXListItemIndexTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxlistitemindextextattribute)Added [kAXListItemLevelTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxlistitemleveltextattribute)Added [kAXListItemPrefixTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxlistitemprefixtextattribute)Added [kColorSync10BitInteger](https://developer.apple.com/documentation/colorsync/colorsyncdatadepth/kcolorsync10bitinteger)Added [kColorSyncACESCGLinearProfile](https://developer.apple.com/documentation/colorsync/kcolorsyncacescglinearprofile)Added [kColorSyncITUR2020Profile](https://developer.apple.com/documentation/colorsync/kcolorsyncitur2020profile)Added [kColorSyncITUR709Profile](https://developer.apple.com/documentation/colorsync/kcolorsyncitur709profile)Added [kColorSyncProfileComputerDomain](https://developer.apple.com/documentation/colorsync/kcolorsyncprofilecomputerdomain)Added [kColorSyncProfileUserDomain](https://developer.apple.com/documentation/colorsync/kcolorsyncprofileuserdomain)Added [kColorSyncROMMRGBProfile](https://developer.apple.com/documentation/colorsync/kcolorsyncrommrgbprofile)Added [kColorSyncTransformCodeFragmentType](https://developer.apple.com/documentation/colorsync/kcolorsynctransformcodefragmenttype)Modified [ATSFontFilterSelector [struct]](https://developer.apple.com/documentation/applicationservices/atsfontfilterselector)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ATSFontFilterSelector {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ATSFontFilterSelector : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ATSFontNotifyAction [struct]](https://developer.apple.com/documentation/applicationservices/atsfontnotifyaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ATSFontNotifyAction {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ATSFontNotifyAction : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ATSFontNotifyOption [struct]](https://developer.apple.com/documentation/applicationservices/atsfontnotifyoption)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ATSFontNotifyOption {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ATSFontNotifyOption : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ATSFontQueryMessageID [struct]](https://developer.apple.com/documentation/applicationservices/atsfontquerymessageid)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ATSFontQueryMessageID {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ATSFontQueryMessageID : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ATSFontQuerySourceContext [struct]](https://developer.apple.com/documentation/applicationservices/atsfontquerysourcecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFontQuerySourceContext {     var version: UInt32     var refCon: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     init()     init(version version: UInt32, refCon refCon: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack) } ``` |
| To | ``` struct ATSFontQuerySourceContext {     var version: UInt32     var refCon: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack!     var release: CFAllocatorReleaseCallBack!     init()     init(version version: UInt32, refCon refCon: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack!, release release: CFAllocatorReleaseCallBack!) } ``` |

Modified [ATSFontQuerySourceContext.release](https://developer.apple.com/documentation/applicationservices/atsfontquerysourcecontext/1460736-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack ``` |
| To | ``` var release: CFAllocatorReleaseCallBack! ``` |

Modified [ATSFontQuerySourceContext.retain](https://developer.apple.com/documentation/applicationservices/atsfontquerysourcecontext/1463355-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack ``` |
| To | ``` var retain: CFAllocatorRetainCallBack! ``` |

Modified [ATSULayoutOperationOverrideSpecifier [struct]](https://developer.apple.com/documentation/applicationservices/atsulayoutoperationoverridespecifier)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSULayoutOperationOverrideSpecifier {     var operationSelector: ATSULayoutOperationSelector     var overrideUPP: ATSUDirectLayoutOperationOverrideUPP     init()     init(operationSelector operationSelector: ATSULayoutOperationSelector, overrideUPP overrideUPP: ATSUDirectLayoutOperationOverrideUPP) } ``` |
| To | ``` struct ATSULayoutOperationOverrideSpecifier {     var operationSelector: ATSULayoutOperationSelector     var overrideUPP: ATSUDirectLayoutOperationOverrideUPP!     init()     init(operationSelector operationSelector: ATSULayoutOperationSelector, overrideUPP overrideUPP: ATSUDirectLayoutOperationOverrideUPP!) } ``` |

Modified [ATSULayoutOperationOverrideSpecifier.overrideUPP](https://developer.apple.com/documentation/applicationservices/atsulayoutoperationoverridespecifier/1463665-overrideupp)

|  | Declaration |
| --- | --- |
| From | ``` var overrideUPP: ATSUDirectLayoutOperationOverrideUPP ``` |
| To | ``` var overrideUPP: ATSUDirectLayoutOperationOverrideUPP! ``` |

Modified [CMFloatBitmapFlags [struct]](https://developer.apple.com/documentation/applicationservices/cmfloatbitmapflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMFloatBitmapFlags {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CMFloatBitmapFlags : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ColorSyncAlphaInfo [struct]](https://developer.apple.com/documentation/colorsync/colorsyncalphainfo)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ColorSyncAlphaInfo {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ColorSyncAlphaInfo : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ColorSyncDataDepth [struct]](https://developer.apple.com/documentation/colorsync/colorsyncdatadepth)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ColorSyncDataDepth {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ColorSyncDataDepth : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [CQDProcs [struct]](https://developer.apple.com/documentation/applicationservices/cqdprocs)

|  | Declaration |
| --- | --- |
| From | ``` struct CQDProcs {     var textProc: QDTextUPP     var lineProc: QDLineUPP     var rectProc: QDRectUPP     var rRectProc: QDRRectUPP     var ovalProc: QDOvalUPP     var arcProc: QDArcUPP     var polyProc: QDPolyUPP     var rgnProc: QDRgnUPP     var bitsProc: QDBitsUPP     var commentProc: QDCommentUPP     var txMeasProc: QDTxMeasUPP     var getPicProc: QDGetPicUPP     var putPicProc: QDPutPicUPP     var opcodeProc: QDOpcodeUPP     var newProc1: UniversalProcPtr     var glyphsProc: QDStdGlyphsUPP     var printerStatusProc: QDPrinterStatusUPP     var newProc4: UniversalProcPtr     var newProc5: UniversalProcPtr     var newProc6: UniversalProcPtr     init()     init(textProc textProc: QDTextUPP, lineProc lineProc: QDLineUPP, rectProc rectProc: QDRectUPP, rRectProc rRectProc: QDRRectUPP, ovalProc ovalProc: QDOvalUPP, arcProc arcProc: QDArcUPP, polyProc polyProc: QDPolyUPP, rgnProc rgnProc: QDRgnUPP, bitsProc bitsProc: QDBitsUPP, commentProc commentProc: QDCommentUPP, txMeasProc txMeasProc: QDTxMeasUPP, getPicProc getPicProc: QDGetPicUPP, putPicProc putPicProc: QDPutPicUPP, opcodeProc opcodeProc: QDOpcodeUPP, newProc1 newProc1: UniversalProcPtr, glyphsProc glyphsProc: QDStdGlyphsUPP, printerStatusProc printerStatusProc: QDPrinterStatusUPP, newProc4 newProc4: UniversalProcPtr, newProc5 newProc5: UniversalProcPtr, newProc6 newProc6: UniversalProcPtr) } ``` |
| To | ``` struct CQDProcs {     var textProc: QDTextUPP!     var lineProc: QDLineUPP!     var rectProc: QDRectUPP!     var rRectProc: QDRRectUPP!     var ovalProc: QDOvalUPP!     var arcProc: QDArcUPP!     var polyProc: QDPolyUPP!     var rgnProc: QDRgnUPP!     var bitsProc: QDBitsUPP!     var commentProc: QDCommentUPP!     var txMeasProc: QDTxMeasUPP!     var getPicProc: QDGetPicUPP!     var putPicProc: QDPutPicUPP!     var opcodeProc: QDOpcodeUPP!     var newProc1: UniversalProcPtr!     var glyphsProc: QDStdGlyphsUPP!     var printerStatusProc: QDPrinterStatusUPP!     var newProc4: UniversalProcPtr!     var newProc5: UniversalProcPtr!     var newProc6: UniversalProcPtr!     init()     init(textProc textProc: QDTextUPP!, lineProc lineProc: QDLineUPP!, rectProc rectProc: QDRectUPP!, rRectProc rRectProc: QDRRectUPP!, ovalProc ovalProc: QDOvalUPP!, arcProc arcProc: QDArcUPP!, polyProc polyProc: QDPolyUPP!, rgnProc rgnProc: QDRgnUPP!, bitsProc bitsProc: QDBitsUPP!, commentProc commentProc: QDCommentUPP!, txMeasProc txMeasProc: QDTxMeasUPP!, getPicProc getPicProc: QDGetPicUPP!, putPicProc putPicProc: QDPutPicUPP!, opcodeProc opcodeProc: QDOpcodeUPP!, newProc1 newProc1: UniversalProcPtr!, glyphsProc glyphsProc: QDStdGlyphsUPP!, printerStatusProc printerStatusProc: QDPrinterStatusUPP!, newProc4 newProc4: UniversalProcPtr!, newProc5 newProc5: UniversalProcPtr!, newProc6 newProc6: UniversalProcPtr!) } ``` |

Modified [CQDProcs.arcProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1462707-arcproc)

|  | Declaration |
| --- | --- |
| From | ``` var arcProc: QDArcUPP ``` |
| To | ``` var arcProc: QDArcUPP! ``` |

Modified [CQDProcs.bitsProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1463001-bitsproc)

|  | Declaration |
| --- | --- |
| From | ``` var bitsProc: QDBitsUPP ``` |
| To | ``` var bitsProc: QDBitsUPP! ``` |

Modified [CQDProcs.commentProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1463288-commentproc)

|  | Declaration |
| --- | --- |
| From | ``` var commentProc: QDCommentUPP ``` |
| To | ``` var commentProc: QDCommentUPP! ``` |

Modified [CQDProcs.getPicProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1462475-getpicproc)

|  | Declaration |
| --- | --- |
| From | ``` var getPicProc: QDGetPicUPP ``` |
| To | ``` var getPicProc: QDGetPicUPP! ``` |

Modified [CQDProcs.glyphsProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1459000-glyphsproc)

|  | Declaration |
| --- | --- |
| From | ``` var glyphsProc: QDStdGlyphsUPP ``` |
| To | ``` var glyphsProc: QDStdGlyphsUPP! ``` |

Modified [CQDProcs.lineProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1463885-lineproc)

|  | Declaration |
| --- | --- |
| From | ``` var lineProc: QDLineUPP ``` |
| To | ``` var lineProc: QDLineUPP! ``` |

Modified [CQDProcs.newProc1](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461234-newproc1)

|  | Declaration |
| --- | --- |
| From | ``` var newProc1: UniversalProcPtr ``` |
| To | ``` var newProc1: UniversalProcPtr! ``` |

Modified [CQDProcs.newProc4](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461037-newproc4)

|  | Declaration |
| --- | --- |
| From | ``` var newProc4: UniversalProcPtr ``` |
| To | ``` var newProc4: UniversalProcPtr! ``` |

Modified [CQDProcs.newProc5](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461848-newproc5)

|  | Declaration |
| --- | --- |
| From | ``` var newProc5: UniversalProcPtr ``` |
| To | ``` var newProc5: UniversalProcPtr! ``` |

Modified [CQDProcs.newProc6](https://developer.apple.com/documentation/applicationservices/cqdprocs/1459877-newproc6)

|  | Declaration |
| --- | --- |
| From | ``` var newProc6: UniversalProcPtr ``` |
| To | ``` var newProc6: UniversalProcPtr! ``` |

Modified [CQDProcs.opcodeProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1459207-opcodeproc)

|  | Declaration |
| --- | --- |
| From | ``` var opcodeProc: QDOpcodeUPP ``` |
| To | ``` var opcodeProc: QDOpcodeUPP! ``` |

Modified [CQDProcs.ovalProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1462138-ovalproc)

|  | Declaration |
| --- | --- |
| From | ``` var ovalProc: QDOvalUPP ``` |
| To | ``` var ovalProc: QDOvalUPP! ``` |

Modified [CQDProcs.polyProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461442-polyproc)

|  | Declaration |
| --- | --- |
| From | ``` var polyProc: QDPolyUPP ``` |
| To | ``` var polyProc: QDPolyUPP! ``` |

Modified [CQDProcs.printerStatusProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1464531-printerstatusproc)

|  | Declaration |
| --- | --- |
| From | ``` var printerStatusProc: QDPrinterStatusUPP ``` |
| To | ``` var printerStatusProc: QDPrinterStatusUPP! ``` |

Modified [CQDProcs.putPicProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461526-putpicproc)

|  | Declaration |
| --- | --- |
| From | ``` var putPicProc: QDPutPicUPP ``` |
| To | ``` var putPicProc: QDPutPicUPP! ``` |

Modified [CQDProcs.rectProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1464519-rectproc)

|  | Declaration |
| --- | --- |
| From | ``` var rectProc: QDRectUPP ``` |
| To | ``` var rectProc: QDRectUPP! ``` |

Modified [CQDProcs.rgnProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1463631-rgnproc)

|  | Declaration |
| --- | --- |
| From | ``` var rgnProc: QDRgnUPP ``` |
| To | ``` var rgnProc: QDRgnUPP! ``` |

Modified [CQDProcs.rRectProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461880-rrectproc)

|  | Declaration |
| --- | --- |
| From | ``` var rRectProc: QDRRectUPP ``` |
| To | ``` var rRectProc: QDRRectUPP! ``` |

Modified [CQDProcs.textProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1460192-textproc)

|  | Declaration |
| --- | --- |
| From | ``` var textProc: QDTextUPP ``` |
| To | ``` var textProc: QDTextUPP! ``` |

Modified [CQDProcs.txMeasProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1464721-txmeasproc)

|  | Declaration |
| --- | --- |
| From | ``` var txMeasProc: QDTxMeasUPP ``` |
| To | ``` var txMeasProc: QDTxMeasUPP! ``` |

Modified [FMInput [struct]](https://developer.apple.com/documentation/applicationservices/fminput)

|  | Declaration |
| --- | --- |
| From | ``` struct FMInput {     var family: Int16     var size: Int16     var face: Style     var needBits: Boolean     var device: Int16     var numer: Point     var denom: Point     init()     init(family family: Int16, size size: Int16, face face: Style, needBits needBits: Boolean, device device: Int16, numer numer: Point, denom denom: Point) } ``` |
| To | ``` struct FMInput {     var family: Int16     var size: Int16     var face: Style     var needBits: DarwinBoolean     var device: Int16     var numer: Point     var denom: Point     init()     init(family family: Int16, size size: Int16, face face: Style, needBits needBits: DarwinBoolean, device device: Int16, numer numer: Point, denom denom: Point) } ``` |

Modified [FMInput.needBits](https://developer.apple.com/documentation/applicationservices/fminput/1464683-needbits)

|  | Declaration |
| --- | --- |
| From | ``` var needBits: Boolean ``` |
| To | ``` var needBits: DarwinBoolean ``` |

Modified [ICCharTable [struct]](https://developer.apple.com/documentation/applicationservices/icchartable)

|  | Declaration |
| --- | --- |
| From | ``` struct ICCharTable {     var netToMac: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var macToNet: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(netToMac netToMac: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), macToNet macToNet: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |
| To | ``` struct ICCharTable {     var netToMac: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var macToNet: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(netToMac netToMac: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), macToNet macToNet: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified [PMDataFormat [struct]](https://developer.apple.com/documentation/applicationservices/pmdataformat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PMDataFormat {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct PMDataFormat : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [PMPageToPaperMappingType [struct]](https://developer.apple.com/documentation/applicationservices/pmpagetopapermappingtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PMPageToPaperMappingType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct PMPageToPaperMappingType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [SpeechStatusInfo [struct]](https://developer.apple.com/documentation/applicationservices/speechstatusinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct SpeechStatusInfo {     var outputBusy: Boolean     var outputPaused: Boolean     var inputBytesLeft: Int     var phonemeCode: Int16     init()     init(outputBusy outputBusy: Boolean, outputPaused outputPaused: Boolean, inputBytesLeft inputBytesLeft: Int, phonemeCode phonemeCode: Int16) } ``` |
| To | ``` struct SpeechStatusInfo {     var outputBusy: DarwinBoolean     var outputPaused: DarwinBoolean     var inputBytesLeft: Int     var phonemeCode: Int16     init()     init(outputBusy outputBusy: DarwinBoolean, outputPaused outputPaused: DarwinBoolean, inputBytesLeft inputBytesLeft: Int, phonemeCode phonemeCode: Int16) } ``` |

Modified [SpeechStatusInfo.outputBusy](https://developer.apple.com/documentation/applicationservices/speechstatusinfo/1459111-outputbusy)

|  | Declaration |
| --- | --- |
| From | ``` var outputBusy: Boolean ``` |
| To | ``` var outputBusy: DarwinBoolean ``` |

Modified [SpeechStatusInfo.outputPaused](https://developer.apple.com/documentation/applicationservices/speechstatusinfo/1460606-outputpaused)

|  | Declaration |
| --- | --- |
| From | ``` var outputPaused: Boolean ``` |
| To | ``` var outputPaused: DarwinBoolean ``` |

Modified [ATSCubicClosePathProcPtr](https://developer.apple.com/documentation/applicationservices/atscubicclosepathprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicClosePathProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSCubicClosePathProcPtr = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSCubicCurveToProcPtr](https://developer.apple.com/documentation/applicationservices/atscubiccurvetoprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicCurveToProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSCubicCurveToProcPtr = (UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSCubicLineToProcPtr](https://developer.apple.com/documentation/applicationservices/atscubiclinetoprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicLineToProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSCubicLineToProcPtr = (UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSCubicMoveToProcPtr](https://developer.apple.com/documentation/applicationservices/atscubicmovetoprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicMoveToProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSCubicMoveToProcPtr = (UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSFontApplierFunction](https://developer.apple.com/documentation/applicationservices/atsfontapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontApplierFunction = CFunctionPointer<((ATSFontRef, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSFontApplierFunction = (ATSFontRef, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSFontFamilyApplierFunction](https://developer.apple.com/documentation/applicationservices/atsfontfamilyapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontFamilyApplierFunction = CFunctionPointer<((ATSFontFamilyRef, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSFontFamilyApplierFunction = (ATSFontFamilyRef, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSFontQueryCallback](https://developer.apple.com/documentation/applicationservices/atsfontquerycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontQueryCallback = CFunctionPointer<((ATSFontQueryMessageID, CFPropertyList!, UnsafeMutablePointer<Void>) -> Unmanaged<CFPropertyList>!)> ``` |
| To | ``` typealias ATSFontQueryCallback = (ATSFontQueryMessageID, CFPropertyList!, UnsafeMutablePointer<Void>) -> Unmanaged<CFPropertyList>! ``` |

Modified [ATSNotificationCallback](https://developer.apple.com/documentation/applicationservices/atsnotificationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSNotificationCallback = CFunctionPointer<((ATSFontNotificationInfoRef, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias ATSNotificationCallback = (ATSFontNotificationInfoRef, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [ATSQuadraticClosePathProcPtr](https://developer.apple.com/documentation/applicationservices/atsquadraticclosepathprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticClosePathProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSQuadraticClosePathProcPtr = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSQuadraticCurveProcPtr](https://developer.apple.com/documentation/applicationservices/atsquadraticcurveprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticCurveProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSQuadraticCurveProcPtr = (UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSQuadraticLineProcPtr](https://developer.apple.com/documentation/applicationservices/atsquadraticlineprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticLineProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSQuadraticLineProcPtr = (UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSQuadraticNewPathProcPtr](https://developer.apple.com/documentation/applicationservices/atsquadraticnewpathprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticNewPathProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias ATSQuadraticNewPathProcPtr = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [ATSUDirectLayoutOperationOverrideProcPtr](https://developer.apple.com/documentation/applicationservices/atsudirectlayoutoperationoverrideprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUDirectLayoutOperationOverrideProcPtr = CFunctionPointer<((ATSULayoutOperationSelector, ATSULineRef, URefCon, UnsafeMutablePointer<Void>, UnsafeMutablePointer<ATSULayoutOperationCallbackStatus>) -> OSStatus)> ``` |
| To | ``` typealias ATSUDirectLayoutOperationOverrideProcPtr = (ATSULayoutOperationSelector, ATSULineRef, URefCon, UnsafeMutablePointer<Void>, UnsafeMutablePointer<ATSULayoutOperationCallbackStatus>) -> OSStatus ``` |

Modified [AXIsProcessTrusted() -> Bool](https://developer.apple.com/documentation/applicationservices/1460720-axisprocesstrusted)

|  | Declaration |
| --- | --- |
| From | ``` func AXIsProcessTrusted() -> Boolean ``` |
| To | ``` func AXIsProcessTrusted() -> Bool ``` |

Modified [AXIsProcessTrustedWithOptions(_: CFDictionary?) -> Bool](https://developer.apple.com/documentation/applicationservices/1459186-axisprocesstrustedwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func AXIsProcessTrustedWithOptions(_ options: CFDictionary!) -> Boolean ``` |
| To | ``` func AXIsProcessTrustedWithOptions(_ options: CFDictionary?) -> Bool ``` |

Modified [AXObserverAddNotification(_: AXObserver, _: AXUIElement, _: CFString, _: UnsafeMutablePointer<Void>) -> AXError](https://developer.apple.com/documentation/applicationservices/1462089-axobserveraddnotification)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverAddNotification(_ observer: AXObserver!, _ element: AXUIElement!, _ notification: CFString!, _ refcon: UnsafeMutablePointer<Void>) -> AXError ``` |
| To | ``` func AXObserverAddNotification(_ observer: AXObserver, _ element: AXUIElement, _ notification: CFString, _ refcon: UnsafeMutablePointer<Void>) -> AXError ``` |

Modified [AXObserverCallback](https://developer.apple.com/documentation/applicationservices/axobservercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AXObserverCallback = CFunctionPointer<((AXObserver!, AXUIElement!, CFString!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias AXObserverCallback = (AXObserver, AXUIElement, CFString, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [AXObserverCallbackWithInfo](https://developer.apple.com/documentation/applicationservices/axobservercallbackwithinfo)

|  | Declaration |
| --- | --- |
| From | ``` typealias AXObserverCallbackWithInfo = CFunctionPointer<((AXObserver!, AXUIElement!, CFString!, CFDictionary!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias AXObserverCallbackWithInfo = (AXObserver, AXUIElement, CFString, CFDictionary, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [AXObserverCreate(_: pid_t, _: AXObserverCallback, _: UnsafeMutablePointer<AXObserver?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1460133-axobservercreate)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverCreate(_ application: pid_t, _ callback: AXObserverCallback, _ outObserver: UnsafeMutablePointer<Unmanaged<AXObserver>?>) -> AXError ``` |
| To | ``` func AXObserverCreate(_ application: pid_t, _ callback: AXObserverCallback, _ outObserver: UnsafeMutablePointer<AXObserver?>) -> AXError ``` |

Modified [AXObserverCreateWithInfoCallback(_: pid_t, _: AXObserverCallbackWithInfo, _: UnsafeMutablePointer<AXObserver?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1460610-axobservercreatewithinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverCreateWithInfoCallback(_ application: pid_t, _ callback: AXObserverCallbackWithInfo, _ outObserver: UnsafeMutablePointer<Unmanaged<AXObserver>?>) -> AXError ``` |
| To | ``` func AXObserverCreateWithInfoCallback(_ application: pid_t, _ callback: AXObserverCallbackWithInfo, _ outObserver: UnsafeMutablePointer<AXObserver?>) -> AXError ``` |

Modified [AXObserverGetRunLoopSource(_: AXObserver) -> Unmanaged<CFRunLoopSource>](https://developer.apple.com/documentation/applicationservices/1459139-axobservergetrunloopsource)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverGetRunLoopSource(_ observer: AXObserver!) -> Unmanaged<CFRunLoopSource>! ``` |
| To | ``` func AXObserverGetRunLoopSource(_ observer: AXObserver) -> Unmanaged<CFRunLoopSource> ``` |

Modified [AXObserverRemoveNotification(_: AXObserver, _: AXUIElement, _: CFString) -> AXError](https://developer.apple.com/documentation/applicationservices/1462066-axobserverremovenotification)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverRemoveNotification(_ observer: AXObserver!, _ element: AXUIElement!, _ notification: CFString!) -> AXError ``` |
| To | ``` func AXObserverRemoveNotification(_ observer: AXObserver, _ element: AXUIElement, _ notification: CFString) -> AXError ``` |

Modified [AXUIElementCopyActionDescription(_: AXUIElement, _: CFString, _: UnsafeMutablePointer<CFString?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1462075-axuielementcopyactiondescription)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyActionDescription(_ element: AXUIElement!, _ action: CFString!, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyActionDescription(_ element: AXUIElement, _ action: CFString, _ description: UnsafeMutablePointer<CFString?>) -> AXError ``` |

Modified [AXUIElementCopyActionNames(_: AXUIElement, _: UnsafeMutablePointer<CFArray?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1462053-axuielementcopyactionnames)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyActionNames(_ element: AXUIElement!, _ names: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyActionNames(_ element: AXUIElement, _ names: UnsafeMutablePointer<CFArray?>) -> AXError ``` |

Modified [AXUIElementCopyAttributeNames(_: AXUIElement, _: UnsafeMutablePointer<CFArray?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1459475-axuielementcopyattributenames)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyAttributeNames(_ element: AXUIElement!, _ names: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyAttributeNames(_ element: AXUIElement, _ names: UnsafeMutablePointer<CFArray?>) -> AXError ``` |

Modified [AXUIElementCopyAttributeValue(_: AXUIElement, _: CFString, _: UnsafeMutablePointer<AnyObject?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1462085-axuielementcopyattributevalue)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyAttributeValue(_ element: AXUIElement!, _ attribute: CFString!, _ value: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyAttributeValue(_ element: AXUIElement, _ attribute: CFString, _ value: UnsafeMutablePointer<AnyObject?>) -> AXError ``` |

Modified [AXUIElementCopyAttributeValues(_: AXUIElement, _: CFString, _: CFIndex, _: CFIndex, _: UnsafeMutablePointer<CFArray?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1462060-axuielementcopyattributevalues)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyAttributeValues(_ element: AXUIElement!, _ attribute: CFString!, _ index: CFIndex, _ maxValues: CFIndex, _ values: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyAttributeValues(_ element: AXUIElement, _ attribute: CFString, _ index: CFIndex, _ maxValues: CFIndex, _ values: UnsafeMutablePointer<CFArray?>) -> AXError ``` |

Modified [AXUIElementCopyElementAtPosition(_: AXUIElement, _: Float, _: Float, _: UnsafeMutablePointer<AXUIElement?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1462077-axuielementcopyelementatposition)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyElementAtPosition(_ application: AXUIElement!, _ x: Float, _ y: Float, _ element: UnsafeMutablePointer<Unmanaged<AXUIElement>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyElementAtPosition(_ application: AXUIElement, _ x: Float, _ y: Float, _ element: UnsafeMutablePointer<AXUIElement?>) -> AXError ``` |

Modified [AXUIElementCopyMultipleAttributeValues(_: AXUIElement, _: CFArray, _: AXCopyMultipleAttributeOptions, _: UnsafeMutablePointer<CFArray?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1462051-axuielementcopymultipleattribute)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyMultipleAttributeValues(_ element: AXUIElement!, _ attributes: CFArray!, _ options: AXCopyMultipleAttributeOptions, _ values: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyMultipleAttributeValues(_ element: AXUIElement, _ attributes: CFArray, _ options: AXCopyMultipleAttributeOptions, _ values: UnsafeMutablePointer<CFArray?>) -> AXError ``` |

Modified [AXUIElementCopyParameterizedAttributeNames(_: AXUIElement, _: UnsafeMutablePointer<CFArray?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1458783-axuielementcopyparameterizedattr)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyParameterizedAttributeNames(_ element: AXUIElement!, _ names: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyParameterizedAttributeNames(_ element: AXUIElement, _ names: UnsafeMutablePointer<CFArray?>) -> AXError ``` |

Modified [AXUIElementCopyParameterizedAttributeValue(_: AXUIElement, _: CFString, _: AnyObject, _: UnsafeMutablePointer<AnyObject?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1461203-axuielementcopyparameterizedattr)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyParameterizedAttributeValue(_ element: AXUIElement!, _ parameterizedAttribute: CFString!, _ parameter: AnyObject!, _ result: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyParameterizedAttributeValue(_ element: AXUIElement, _ parameterizedAttribute: CFString, _ parameter: AnyObject, _ result: UnsafeMutablePointer<AnyObject?>) -> AXError ``` |

Modified [AXUIElementCreateApplication(_: pid_t) -> Unmanaged<AXUIElement>](https://developer.apple.com/documentation/applicationservices/1459374-axuielementcreateapplication)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCreateApplication(_ pid: pid_t) -> Unmanaged<AXUIElement>! ``` |
| To | ``` func AXUIElementCreateApplication(_ pid: pid_t) -> Unmanaged<AXUIElement> ``` |

Modified [AXUIElementCreateSystemWide() -> Unmanaged<AXUIElement>](https://developer.apple.com/documentation/applicationservices/1462095-axuielementcreatesystemwide)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCreateSystemWide() -> Unmanaged<AXUIElement>! ``` |
| To | ``` func AXUIElementCreateSystemWide() -> Unmanaged<AXUIElement> ``` |

Modified [AXUIElementGetAttributeValueCount(_: AXUIElement, _: CFString, _: UnsafeMutablePointer<CFIndex>) -> AXError](https://developer.apple.com/documentation/applicationservices/1459066-axuielementgetattributevaluecoun)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementGetAttributeValueCount(_ element: AXUIElement!, _ attribute: CFString!, _ count: UnsafeMutablePointer<CFIndex>) -> AXError ``` |
| To | ``` func AXUIElementGetAttributeValueCount(_ element: AXUIElement, _ attribute: CFString, _ count: UnsafeMutablePointer<CFIndex>) -> AXError ``` |

Modified [AXUIElementGetPid(_: AXUIElement, _: UnsafeMutablePointer<pid_t>) -> AXError](https://developer.apple.com/documentation/applicationservices/1460337-axuielementgetpid)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementGetPid(_ element: AXUIElement!, _ pid: UnsafeMutablePointer<pid_t>) -> AXError ``` |
| To | ``` func AXUIElementGetPid(_ element: AXUIElement, _ pid: UnsafeMutablePointer<pid_t>) -> AXError ``` |

Modified [AXUIElementIsAttributeSettable(_: AXUIElement, _: CFString, _: UnsafeMutablePointer<DarwinBoolean>) -> AXError](https://developer.apple.com/documentation/applicationservices/1459972-axuielementisattributesettable)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementIsAttributeSettable(_ element: AXUIElement!, _ attribute: CFString!, _ settable: UnsafeMutablePointer<Boolean>) -> AXError ``` |
| To | ``` func AXUIElementIsAttributeSettable(_ element: AXUIElement, _ attribute: CFString, _ settable: UnsafeMutablePointer<DarwinBoolean>) -> AXError ``` |

Modified [AXUIElementPerformAction(_: AXUIElement, _: CFString) -> AXError](https://developer.apple.com/documentation/applicationservices/1462091-axuielementperformaction)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementPerformAction(_ element: AXUIElement!, _ action: CFString!) -> AXError ``` |
| To | ``` func AXUIElementPerformAction(_ element: AXUIElement, _ action: CFString) -> AXError ``` |

Modified [AXUIElementSetAttributeValue(_: AXUIElement, _: CFString, _: AnyObject) -> AXError](https://developer.apple.com/documentation/applicationservices/1460434-axuielementsetattributevalue)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementSetAttributeValue(_ element: AXUIElement!, _ attribute: CFString!, _ value: AnyObject!) -> AXError ``` |
| To | ``` func AXUIElementSetAttributeValue(_ element: AXUIElement, _ attribute: CFString, _ value: AnyObject) -> AXError ``` |

Modified [AXUIElementSetMessagingTimeout(_: AXUIElement, _: Float) -> AXError](https://developer.apple.com/documentation/applicationservices/1459345-axuielementsetmessagingtimeout)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementSetMessagingTimeout(_ element: AXUIElement!, _ timeoutInSeconds: Float) -> AXError ``` |
| To | ``` func AXUIElementSetMessagingTimeout(_ element: AXUIElement, _ timeoutInSeconds: Float) -> AXError ``` |

Modified [AXValueCreate(_: AXValueType, _: UnsafePointer<Void>) -> Unmanaged<AXValue>?](https://developer.apple.com/documentation/applicationservices/1459351-axvaluecreate)

|  | Declaration |
| --- | --- |
| From | ``` func AXValueCreate(_ theType: AXValueType, _ valuePtr: UnsafePointer<Void>) -> Unmanaged<AXValue>! ``` |
| To | ``` func AXValueCreate(_ theType: AXValueType, _ valuePtr: UnsafePointer<Void>) -> Unmanaged<AXValue>? ``` |

Modified [AXValueGetType(_: AXValue) -> AXValueType](https://developer.apple.com/documentation/applicationservices/1460911-axvaluegettype)

|  | Declaration |
| --- | --- |
| From | ``` func AXValueGetType(_ value: AXValue!) -> AXValueType ``` |
| To | ``` func AXValueGetType(_ value: AXValue) -> AXValueType ``` |

Modified [AXValueGetValue(_: AXValue, _: AXValueType, _: UnsafeMutablePointer<Void>) -> Bool](https://developer.apple.com/documentation/applicationservices/1462933-axvaluegetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func AXValueGetValue(_ value: AXValue!, _ theType: AXValueType, _ valuePtr: UnsafeMutablePointer<Void>) -> Boolean ``` |
| To | ``` func AXValueGetValue(_ value: AXValue, _ theType: AXValueType, _ valuePtr: UnsafeMutablePointer<Void>) -> Bool ``` |

Modified [CMFlattenProcPtr](https://developer.apple.com/documentation/applicationservices/cmflattenprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMFlattenProcPtr = CFunctionPointer<((Int32, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSErr)> ``` |
| To | ``` typealias CMFlattenProcPtr = (Int32, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSErr ``` |

Modified [CMMApplyTransformProc](https://developer.apple.com/documentation/colorsync/cmmapplytransformproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMApplyTransformProc = CFunctionPointer<((ColorSyncTransform!, Int, Int, Int, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, ColorSyncDataDepth, ColorSyncDataLayout, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary!) -> Bool)> ``` |
| To | ``` typealias CMMApplyTransformProc = (ColorSyncTransform!, Int, Int, Int, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, ColorSyncDataDepth, ColorSyncDataLayout, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary!) -> Bool ``` |

Modified [CMMCreateTransformPropertyProc](https://developer.apple.com/documentation/colorsync/cmmcreatetransformpropertyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMCreateTransformPropertyProc = CFunctionPointer<((ColorSyncTransform!, AnyObject!, CFDictionary!) -> Unmanaged<AnyObject>!)> ``` |
| To | ``` typealias CMMCreateTransformPropertyProc = (ColorSyncTransform!, AnyObject!, CFDictionary!) -> Unmanaged<AnyObject>! ``` |

Modified [CMMInitializeLinkProfileProc](https://developer.apple.com/documentation/colorsync/cmminitializelinkprofileproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMInitializeLinkProfileProc = CFunctionPointer<((ColorSyncMutableProfile!, CFArray!, CFDictionary!) -> Bool)> ``` |
| To | ``` typealias CMMInitializeLinkProfileProc = (ColorSyncMutableProfile!, CFArray!, CFDictionary!) -> Bool ``` |

Modified [CMMInitializeTransformProc](https://developer.apple.com/documentation/colorsync/cmminitializetransformproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMInitializeTransformProc = CFunctionPointer<((ColorSyncTransform!, CFArray!, CFDictionary!) -> Bool)> ``` |
| To | ``` typealias CMMInitializeTransformProc = (ColorSyncTransform!, CFArray!, CFDictionary!) -> Bool ``` |

Modified [ColorComplementProcPtr](https://developer.apple.com/documentation/applicationservices/colorcomplementprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorComplementProcPtr = CFunctionPointer<((UnsafeMutablePointer<RGBColor>) -> Boolean)> ``` |
| To | ``` typealias ColorComplementProcPtr = (UnsafeMutablePointer<RGBColor>) -> DarwinBoolean ``` |

Modified [ColorSearchProcPtr](https://developer.apple.com/documentation/applicationservices/colorsearchprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSearchProcPtr = CFunctionPointer<((UnsafeMutablePointer<RGBColor>, UnsafeMutablePointer<Int>) -> Boolean)> ``` |
| To | ``` typealias ColorSearchProcPtr = (UnsafeMutablePointer<RGBColor>, UnsafeMutablePointer<Int>) -> DarwinBoolean ``` |

Modified [ColorSyncCMMIterateCallback](https://developer.apple.com/documentation/colorsync/colorsynccmmiteratecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncCMMIterateCallback = CFunctionPointer<((ColorSyncCMM!, UnsafeMutablePointer<Void>) -> Bool)> ``` |
| To | ``` typealias ColorSyncCMMIterateCallback = (ColorSyncCMM!, UnsafeMutablePointer<Void>) -> Bool ``` |

Modified [ColorSyncDeviceProfileIterateCallback](https://developer.apple.com/documentation/colorsync/colorsyncdeviceprofileiteratecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncDeviceProfileIterateCallback = CFunctionPointer<((CFDictionary!, UnsafeMutablePointer<Void>) -> Bool)> ``` |
| To | ``` typealias ColorSyncDeviceProfileIterateCallback = (CFDictionary!, UnsafeMutablePointer<Void>) -> Bool ``` |

Modified [ColorSyncIterateDeviceProfiles(_: ColorSyncDeviceProfileIterateCallback!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/colorsync/1460141-colorsynciteratedeviceprofiles)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateDeviceProfiles(_ callBack: ColorSyncDeviceProfileIterateCallback, _ userInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ColorSyncIterateDeviceProfiles(_ callBack: ColorSyncDeviceProfileIterateCallback!, _ userInfo: UnsafeMutablePointer<Void>) ``` |

Modified [ColorSyncIterateInstalledCMMs(_: ColorSyncCMMIterateCallback!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/colorsync/1462477-colorsynciterateinstalledcmms)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateInstalledCMMs(_ callBack: ColorSyncCMMIterateCallback, _ userInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ColorSyncIterateInstalledCMMs(_ callBack: ColorSyncCMMIterateCallback!, _ userInfo: UnsafeMutablePointer<Void>) ``` |

Modified [ColorSyncIterateInstalledProfiles(_: ColorSyncProfileIterateCallback!, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<Unmanaged<CFError>?>)](https://developer.apple.com/documentation/colorsync/1463359-colorsynciterateinstalledprofile)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateInstalledProfiles(_ callBack: ColorSyncProfileIterateCallback, _ seed: UnsafeMutablePointer<UInt32>, _ userInfo: UnsafeMutablePointer<Void>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) ``` |
| To | ``` func ColorSyncIterateInstalledProfiles(_ callBack: ColorSyncProfileIterateCallback!, _ seed: UnsafeMutablePointer<UInt32>, _ userInfo: UnsafeMutablePointer<Void>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) ``` |

Modified [ColorSyncProfileIterateCallback](https://developer.apple.com/documentation/colorsync/colorsyncprofileiteratecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncProfileIterateCallback = CFunctionPointer<((CFDictionary!, UnsafeMutablePointer<Void>) -> Bool)> ``` |
| To | ``` typealias ColorSyncProfileIterateCallback = (CFDictionary!, UnsafeMutablePointer<Void>) -> Bool ``` |

Modified [CopyPhonemesFromText(_: SpeechChannel, _: CFString, _: UnsafeMutablePointer<CFString?>) -> OSErr](https://developer.apple.com/documentation/applicationservices/1460918-copyphonemesfromtext)

|  | Declaration |
| --- | --- |
| From | ``` func CopyPhonemesFromText(_ chan: SpeechChannel, _ text: CFString!, _ phonemes: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSErr ``` |
| To | ``` func CopyPhonemesFromText(_ chan: SpeechChannel, _ text: CFString, _ phonemes: UnsafeMutablePointer<CFString?>) -> OSErr ``` |

Modified [CopySpeechProperty(_: SpeechChannel, _: CFString, _: UnsafeMutablePointer<AnyObject?>) -> OSErr](https://developer.apple.com/documentation/applicationservices/1459075-copyspeechproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CopySpeechProperty(_ chan: SpeechChannel, _ property: CFString!, _ object: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSErr ``` |
| To | ``` func CopySpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: UnsafeMutablePointer<AnyObject?>) -> OSErr ``` |

Modified [DCMProgressFilterProcPtr](https://developer.apple.com/documentation/applicationservices/dcmprogressfilterprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMProgressFilterProcPtr = CFunctionPointer<((Boolean, UInt16, UInt32) -> Boolean)> ``` |
| To | ``` typealias DCMProgressFilterProcPtr = (DarwinBoolean, UInt16, UInt32) -> DarwinBoolean ``` |

Modified [DisposeIconActionUPP(_: IconActionUPP!)](https://developer.apple.com/documentation/applicationservices/1461028-disposeiconactionupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeIconActionUPP(_ userUPP: IconActionUPP) ``` |
| To | ``` func DisposeIconActionUPP(_ userUPP: IconActionUPP!) ``` |

Modified [DisposeIconGetterUPP(_: IconGetterUPP!)](https://developer.apple.com/documentation/applicationservices/1461061-disposeicongetterupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeIconGetterUPP(_ userUPP: IconGetterUPP) ``` |
| To | ``` func DisposeIconGetterUPP(_ userUPP: IconGetterUPP!) ``` |

Modified [DragGrayRgnProcPtr](https://developer.apple.com/documentation/applicationservices/draggrayrgnprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias DragGrayRgnProcPtr = CFunctionPointer<(() -> Void)> ``` |
| To | ``` typealias DragGrayRgnProcPtr = () -> Void ``` |

Modified [FMFontCallbackFilterProcPtr](https://developer.apple.com/documentation/applicationservices/fmfontcallbackfilterprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias FMFontCallbackFilterProcPtr = CFunctionPointer<((FMFont, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias FMFontCallbackFilterProcPtr = (FMFont, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [FMFontFamilyCallbackFilterProcPtr](https://developer.apple.com/documentation/applicationservices/fmfontfamilycallbackfilterprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias FMFontFamilyCallbackFilterProcPtr = CFunctionPointer<((FMFontFamily, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias FMFontFamilyCallbackFilterProcPtr = (FMFontFamily, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [HIShapeContainsPoint(_: HIShape!, _: UnsafePointer<CGPoint>) -> Bool](https://developer.apple.com/documentation/applicationservices/1464704-hishapecontainspoint)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeContainsPoint(_ inShape: HIShape!, _ inPoint: UnsafePointer<CGPoint>) -> Boolean ``` |
| To | ``` func HIShapeContainsPoint(_ inShape: HIShape!, _ inPoint: UnsafePointer<CGPoint>) -> Bool ``` |

Modified [HIShapeEnumerate(_: HIShape!, _: OptionBits, _: HIShapeEnumerateProcPtr!, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459161-hishapeenumerate)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeEnumerate(_ inShape: HIShape!, _ inOptions: OptionBits, _ inProc: HIShapeEnumerateProcPtr, _ inRefcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func HIShapeEnumerate(_ inShape: HIShape!, _ inOptions: OptionBits, _ inProc: HIShapeEnumerateProcPtr!, _ inRefcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [HIShapeEnumerateProcPtr](https://developer.apple.com/documentation/applicationservices/hishapeenumerateprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias HIShapeEnumerateProcPtr = CFunctionPointer<((Int32, HIShape!, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias HIShapeEnumerateProcPtr = (Int32, HIShape!, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [HIShapeIntersectsRect(_: HIShape!, _: UnsafePointer<CGRect>) -> Bool](https://developer.apple.com/documentation/applicationservices/1459614-hishapeintersectsrect)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeIntersectsRect(_ inShape: HIShape!, _ inRect: UnsafePointer<CGRect>) -> Boolean ``` |
| To | ``` func HIShapeIntersectsRect(_ inShape: HIShape!, _ inRect: UnsafePointer<CGRect>) -> Bool ``` |

Modified [HIShapeIsEmpty(_: HIShape!) -> Bool](https://developer.apple.com/documentation/applicationservices/1461878-hishapeisempty)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeIsEmpty(_ inShape: HIShape!) -> Boolean ``` |
| To | ``` func HIShapeIsEmpty(_ inShape: HIShape!) -> Bool ``` |

Modified [HIShapeIsRectangular(_: HIShape!) -> Bool](https://developer.apple.com/documentation/applicationservices/1461292-hishapeisrectangular)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeIsRectangular(_ inShape: HIShape!) -> Boolean ``` |
| To | ``` func HIShapeIsRectangular(_ inShape: HIShape!) -> Bool ``` |

Modified [IconActionProcPtr](https://developer.apple.com/documentation/applicationservices/iconactionprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias IconActionProcPtr = CFunctionPointer<((ResType, UnsafeMutablePointer<Handle>, UnsafeMutablePointer<Void>) -> OSErr)> ``` |
| To | ``` typealias IconActionProcPtr = (ResType, UnsafeMutablePointer<Handle>, UnsafeMutablePointer<Void>) -> OSErr ``` |

Modified [IconGetterProcPtr](https://developer.apple.com/documentation/applicationservices/icongetterprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias IconGetterProcPtr = CFunctionPointer<((ResType, UnsafeMutablePointer<Void>) -> Handle)> ``` |
| To | ``` typealias IconGetterProcPtr = (ResType, UnsafeMutablePointer<Void>) -> Handle ``` |

Modified [IconRefContainsCGPoint(_: UnsafePointer<CGPoint>, _: UnsafePointer<CGRect>, _: IconAlignmentType, _: IconServicesUsageFlags, _: IconRef) -> Bool](https://developer.apple.com/documentation/applicationservices/1461049-iconrefcontainscgpoint)

|  | Declaration |
| --- | --- |
| From | ``` func IconRefContainsCGPoint(_ testPt: UnsafePointer<CGPoint>, _ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Boolean ``` |
| To | ``` func IconRefContainsCGPoint(_ testPt: UnsafePointer<CGPoint>, _ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Bool ``` |

Modified [IconRefIntersectsCGRect(_: UnsafePointer<CGRect>, _: UnsafePointer<CGRect>, _: IconAlignmentType, _: IconServicesUsageFlags, _: IconRef) -> Bool](https://developer.apple.com/documentation/applicationservices/1462553-iconrefintersectscgrect)

|  | Declaration |
| --- | --- |
| From | ``` func IconRefIntersectsCGRect(_ testRect: UnsafePointer<CGRect>, _ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Boolean ``` |
| To | ``` func IconRefIntersectsCGRect(_ testRect: UnsafePointer<CGRect>, _ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Bool ``` |

Modified [InvokeIconActionUPP(_: ResType, _: UnsafeMutablePointer<Handle>, _: UnsafeMutablePointer<Void>, _: IconActionUPP!) -> OSErr](https://developer.apple.com/documentation/applicationservices/1464116-invokeiconactionupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeIconActionUPP(_ theType: ResType, _ theIcon: UnsafeMutablePointer<Handle>, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: IconActionUPP) -> OSErr ``` |
| To | ``` func InvokeIconActionUPP(_ theType: ResType, _ theIcon: UnsafeMutablePointer<Handle>, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: IconActionUPP!) -> OSErr ``` |

Modified [InvokeIconGetterUPP(_: ResType, _: UnsafeMutablePointer<Void>, _: IconGetterUPP!) -> Handle](https://developer.apple.com/documentation/applicationservices/1460976-invokeicongetterupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeIconGetterUPP(_ theType: ResType, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: IconGetterUPP) -> Handle ``` |
| To | ``` func InvokeIconGetterUPP(_ theType: ResType, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: IconGetterUPP!) -> Handle ``` |

Modified [IsIconRefMaskEmpty(_: IconRef) -> Bool](https://developer.apple.com/documentation/applicationservices/1464419-isiconrefmaskempty)

|  | Declaration |
| --- | --- |
| From | ``` func IsIconRefMaskEmpty(_ iconRef: IconRef) -> Boolean ``` |
| To | ``` func IsIconRefMaskEmpty(_ iconRef: IconRef) -> Bool ``` |

Modified [kAudioUnitProperty_SpeechChannel](https://developer.apple.com/documentation/applicationservices/1552263-audio_unit_constants/kaudiounitproperty_speechchannel)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SpeechChannel: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SpeechChannel: UInt32 { get } ``` |

Modified [kAudioUnitProperty_Voice](https://developer.apple.com/documentation/applicationservices/kaudiounitproperty_voice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_Voice: Int { get } ``` |
| To | ``` var kAudioUnitProperty_Voice: UInt32 { get } ``` |

Modified [kAudioUnitSubType_SpeechSynthesis](https://developer.apple.com/documentation/applicationservices/kaudiounitsubtype_speechsynthesis)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_SpeechSynthesis: Int { get } ``` |
| To | ``` var kAudioUnitSubType_SpeechSynthesis: UInt32 { get } ``` |

Modified [kAXAttachmentTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxattachmenttextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXAttachmentTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXAttachmentTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXAutocorrectedTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxautocorrectedtextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXAutocorrectedTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXAutocorrectedTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXBackgroundColorTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxbackgroundcolortextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXBackgroundColorTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXBackgroundColorTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXFontFamilyKey](https://developer.apple.com/documentation/applicationservices/kaxfontfamilykey)

|  | Declaration |
| --- | --- |
| From | ``` var kAXFontFamilyKey: Unmanaged<CFString>! ``` |
| To | ``` var kAXFontFamilyKey: Unmanaged<CFString> ``` |

Modified [kAXFontNameKey](https://developer.apple.com/documentation/applicationservices/kaxfontnamekey)

|  | Declaration |
| --- | --- |
| From | ``` var kAXFontNameKey: Unmanaged<CFString>! ``` |
| To | ``` var kAXFontNameKey: Unmanaged<CFString> ``` |

Modified [kAXFontSizeKey](https://developer.apple.com/documentation/applicationservices/kaxfontsizekey)

|  | Declaration |
| --- | --- |
| From | ``` var kAXFontSizeKey: Unmanaged<CFString>! ``` |
| To | ``` var kAXFontSizeKey: Unmanaged<CFString> ``` |

Modified [kAXFontTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxfonttextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXFontTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXFontTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXForegoundColorTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxforegoundcolortextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXForegoundColorTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXForegoundColorTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXForegroundColorTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxforegroundcolortextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXForegroundColorTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXForegroundColorTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXLinkTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxlinktextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXLinkTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXLinkTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXMarkedMisspelledTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxmarkedmisspelledtextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXMarkedMisspelledTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXMarkedMisspelledTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXMisspelledTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxmisspelledtextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXMisspelledTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXMisspelledTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXNaturalLanguageTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxnaturallanguagetextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXNaturalLanguageTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXNaturalLanguageTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXReplacementStringTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxreplacementstringtextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXReplacementStringTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXReplacementStringTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXShadowTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxshadowtextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXShadowTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXShadowTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXStrikethroughColorTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxstrikethroughcolortextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXStrikethroughColorTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXStrikethroughColorTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXStrikethroughTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxstrikethroughtextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXStrikethroughTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXStrikethroughTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXSuperscriptTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxsuperscripttextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXSuperscriptTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXSuperscriptTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXTrustedCheckOptionPrompt](https://developer.apple.com/documentation/applicationservices/kaxtrustedcheckoptionprompt)

|  | Declaration |
| --- | --- |
| From | ``` var kAXTrustedCheckOptionPrompt: Unmanaged<CFString>! ``` |
| To | ``` var kAXTrustedCheckOptionPrompt: Unmanaged<CFString> ``` |

Modified [kAXUnderlineColorTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxunderlinecolortextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXUnderlineColorTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXUnderlineColorTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXUnderlineTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxunderlinetextattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kAXUnderlineTextAttribute: Unmanaged<CFString>! ``` |
| To | ``` var kAXUnderlineTextAttribute: Unmanaged<CFString> ``` |

Modified [kAXValueAXErrorType](https://developer.apple.com/documentation/applicationservices/kaxvalueaxerrortype)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kAXValueAXErrorType: AXValueType { get } ``` | OS X 10.10 |
| To | ``` let kAXValueAXErrorType: UInt32 ``` | OS X 10.11 |

Modified [kAXValueCFRangeType](https://developer.apple.com/documentation/applicationservices/kaxvaluecfrangetype)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kAXValueCFRangeType: AXValueType { get } ``` | OS X 10.10 |
| To | ``` let kAXValueCFRangeType: UInt32 ``` | OS X 10.11 |

Modified [kAXValueCGPointType](https://developer.apple.com/documentation/applicationservices/kaxvaluecgpointtype)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kAXValueCGPointType: AXValueType { get } ``` | OS X 10.10 |
| To | ``` let kAXValueCGPointType: UInt32 ``` | OS X 10.11 |

Modified [kAXValueCGRectType](https://developer.apple.com/documentation/applicationservices/kaxvaluecgrecttype)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kAXValueCGRectType: AXValueType { get } ``` | OS X 10.10 |
| To | ``` let kAXValueCGRectType: UInt32 ``` | OS X 10.11 |

Modified [kAXValueCGSizeType](https://developer.apple.com/documentation/applicationservices/kaxvaluecgsizetype)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kAXValueCGSizeType: AXValueType { get } ``` | OS X 10.10 |
| To | ``` let kAXValueCGSizeType: UInt32 ``` | OS X 10.11 |

Modified [kAXValueIllegalType](https://developer.apple.com/documentation/applicationservices/kaxvalueillegaltype)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kAXValueIllegalType: AXValueType { get } ``` | OS X 10.10 |
| To | ``` let kAXValueIllegalType: UInt32 ``` | OS X 10.11 |

Modified [kAXVisibleNameKey](https://developer.apple.com/documentation/applicationservices/kaxvisiblenamekey)

|  | Declaration |
| --- | --- |
| From | ``` var kAXVisibleNameKey: Unmanaged<CFString>! ``` |
| To | ``` var kAXVisibleNameKey: Unmanaged<CFString> ``` |

Modified [kEndOfSentence](https://developer.apple.com/documentation/applicationservices/kendofsentence)

|  | Declaration |
| --- | --- |
| From | ``` var kEndOfSentence: Int { get } ``` |
| To | ``` var kEndOfSentence: Int32 { get } ``` |

Modified [kEndOfWord](https://developer.apple.com/documentation/applicationservices/1552264-stop_speech_locations/kendofword)

|  | Declaration |
| --- | --- |
| From | ``` var kEndOfWord: Int { get } ``` |
| To | ``` var kEndOfWord: Int32 { get } ``` |

Modified [kFemale](https://developer.apple.com/documentation/applicationservices/1552246-gender_constants/kfemale)

|  | Declaration |
| --- | --- |
| From | ``` var kFemale: Int { get } ``` |
| To | ``` var kFemale: Int16 { get } ``` |

Modified [kImmediate](https://developer.apple.com/documentation/applicationservices/1552264-stop_speech_locations/kimmediate)

|  | Declaration |
| --- | --- |
| From | ``` var kImmediate: Int { get } ``` |
| To | ``` var kImmediate: Int32 { get } ``` |

Modified [kMale](https://developer.apple.com/documentation/applicationservices/kmale)

|  | Declaration |
| --- | --- |
| From | ``` var kMale: Int { get } ``` |
| To | ``` var kMale: Int16 { get } ``` |

Modified [kNeuter](https://developer.apple.com/documentation/applicationservices/1552246-gender_constants/kneuter)

|  | Declaration |
| --- | --- |
| From | ``` var kNeuter: Int { get } ``` |
| To | ``` var kNeuter: Int16 { get } ``` |

Modified [kNoEndingProsody](https://developer.apple.com/documentation/applicationservices/knoendingprosody)

|  | Declaration |
| --- | --- |
| From | ``` var kNoEndingProsody: Int { get } ``` |
| To | ``` var kNoEndingProsody: Int32 { get } ``` |

Modified [kNoSpeechInterrupt](https://developer.apple.com/documentation/applicationservices/knospeechinterrupt)

|  | Declaration |
| --- | --- |
| From | ``` var kNoSpeechInterrupt: Int { get } ``` |
| To | ``` var kNoSpeechInterrupt: Int32 { get } ``` |

Modified [kPreflightThenPause](https://developer.apple.com/documentation/applicationservices/1552213-control_flags_constants/kpreflightthenpause)

|  | Declaration |
| --- | --- |
| From | ``` var kPreflightThenPause: Int { get } ``` |
| To | ``` var kPreflightThenPause: Int32 { get } ``` |

Modified [kSpeechAudioGraphProperty](https://developer.apple.com/documentation/applicationservices/kspeechaudiographproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechAudioGraphProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechAudioGraphProperty: CFString ``` |

Modified [kSpeechAudioOutputFormatProperty](https://developer.apple.com/documentation/applicationservices/kspeechaudiooutputformatproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechAudioOutputFormatProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechAudioOutputFormatProperty: CFString ``` |

Modified [kSpeechAudioUnitProperty](https://developer.apple.com/documentation/applicationservices/kspeechaudiounitproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechAudioUnitProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechAudioUnitProperty: CFString ``` |

Modified [kSpeechCharacterModeProperty](https://developer.apple.com/documentation/applicationservices/kspeechcharactermodeproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechCharacterModeProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechCharacterModeProperty: CFString ``` |

Modified [kSpeechCommandDelimiterProperty](https://developer.apple.com/documentation/applicationservices/kspeechcommanddelimiterproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechCommandDelimiterProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechCommandDelimiterProperty: CFString ``` |

Modified [kSpeechCommandPrefix](https://developer.apple.com/documentation/applicationservices/kspeechcommandprefix)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechCommandPrefix: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechCommandPrefix: CFString ``` |

Modified [kSpeechCommandSuffix](https://developer.apple.com/documentation/applicationservices/kspeechcommandsuffix)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechCommandSuffix: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechCommandSuffix: CFString ``` |

Modified [kSpeechCurrentVoiceProperty](https://developer.apple.com/documentation/applicationservices/kspeechcurrentvoiceproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechCurrentVoiceProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechCurrentVoiceProperty: CFString ``` |

Modified [kSpeechDictionaryAbbreviations](https://developer.apple.com/documentation/applicationservices/kspeechdictionaryabbreviations)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechDictionaryAbbreviations: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechDictionaryAbbreviations: CFString ``` |

Modified [kSpeechDictionaryEntryPhonemes](https://developer.apple.com/documentation/applicationservices/kspeechdictionaryentryphonemes)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechDictionaryEntryPhonemes: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechDictionaryEntryPhonemes: CFString ``` |

Modified [kSpeechDictionaryEntrySpelling](https://developer.apple.com/documentation/applicationservices/kspeechdictionaryentryspelling)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechDictionaryEntrySpelling: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechDictionaryEntrySpelling: CFString ``` |

Modified [kSpeechDictionaryLocaleIdentifier](https://developer.apple.com/documentation/applicationservices/kspeechdictionarylocaleidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechDictionaryLocaleIdentifier: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechDictionaryLocaleIdentifier: CFString ``` |

Modified [kSpeechDictionaryModificationDate](https://developer.apple.com/documentation/applicationservices/kspeechdictionarymodificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechDictionaryModificationDate: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechDictionaryModificationDate: CFString ``` |

Modified [kSpeechDictionaryPronunciations](https://developer.apple.com/documentation/applicationservices/kspeechdictionarypronunciations)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechDictionaryPronunciations: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechDictionaryPronunciations: CFString ``` |

Modified [kSpeechErrorCallbackCharacterOffset](https://developer.apple.com/documentation/applicationservices/kspeecherrorcallbackcharacteroffset)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorCallbackCharacterOffset: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorCallbackCharacterOffset: CFString ``` |

Modified [kSpeechErrorCallbackSpokenString](https://developer.apple.com/documentation/applicationservices/kspeecherrorcallbackspokenstring)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorCallbackSpokenString: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorCallbackSpokenString: CFString ``` |

Modified [kSpeechErrorCFCallBack](https://developer.apple.com/documentation/applicationservices/kspeecherrorcfcallback)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorCFCallBack: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorCFCallBack: CFString ``` |

Modified [kSpeechErrorCount](https://developer.apple.com/documentation/applicationservices/kspeecherrorcount)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorCount: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorCount: CFString ``` |

Modified [kSpeechErrorNewest](https://developer.apple.com/documentation/applicationservices/kspeecherrornewest)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorNewest: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorNewest: CFString ``` |

Modified [kSpeechErrorNewestCharacterOffset](https://developer.apple.com/documentation/applicationservices/kspeecherrornewestcharacteroffset)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorNewestCharacterOffset: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorNewestCharacterOffset: CFString ``` |

Modified [kSpeechErrorOldest](https://developer.apple.com/documentation/applicationservices/kspeecherroroldest)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorOldest: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorOldest: CFString ``` |

Modified [kSpeechErrorOldestCharacterOffset](https://developer.apple.com/documentation/applicationservices/kspeecherroroldestcharacteroffset)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorOldestCharacterOffset: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorOldestCharacterOffset: CFString ``` |

Modified [kSpeechErrorsProperty](https://developer.apple.com/documentation/applicationservices/kspeecherrorsproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechErrorsProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechErrorsProperty: CFString ``` |

Modified [kSpeechGenerateTune](https://developer.apple.com/documentation/applicationservices/1552233-phoneme_generation_options/kspeechgeneratetune)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechGenerateTune: Int { get } ``` |
| To | ``` var kSpeechGenerateTune: Int32 { get } ``` |

Modified [kSpeechInputModeProperty](https://developer.apple.com/documentation/applicationservices/kspeechinputmodeproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechInputModeProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechInputModeProperty: CFString ``` |

Modified [kSpeechModeLiteral](https://developer.apple.com/documentation/applicationservices/kspeechmodeliteral)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechModeLiteral: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechModeLiteral: CFString ``` |

Modified [kSpeechModeNormal](https://developer.apple.com/documentation/applicationservices/kspeechmodenormal)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechModeNormal: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechModeNormal: CFString ``` |

Modified [kSpeechModePhoneme](https://developer.apple.com/documentation/applicationservices/kspeechmodephoneme)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechModePhoneme: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechModePhoneme: CFString ``` |

Modified [kSpeechModeText](https://developer.apple.com/documentation/applicationservices/kspeechmodetext)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechModeText: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechModeText: CFString ``` |

Modified [kSpeechModeTune](https://developer.apple.com/documentation/applicationservices/kspeechmodetune)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechModeTune: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechModeTune: CFString ``` |

Modified [kSpeechNoEndingProsody](https://developer.apple.com/documentation/applicationservices/kspeechnoendingprosody)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechNoEndingProsody: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechNoEndingProsody: CFString ``` |

Modified [kSpeechNoSpeechInterrupt](https://developer.apple.com/documentation/applicationservices/kspeechnospeechinterrupt)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechNoSpeechInterrupt: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechNoSpeechInterrupt: CFString ``` |

Modified [kSpeechNumberModeProperty](https://developer.apple.com/documentation/applicationservices/kspeechnumbermodeproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechNumberModeProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechNumberModeProperty: CFString ``` |

Modified [kSpeechOutputChannelMapProperty](https://developer.apple.com/documentation/applicationservices/kspeechoutputchannelmapproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechOutputChannelMapProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechOutputChannelMapProperty: CFString ``` |

Modified [kSpeechOutputToAudioDeviceProperty](https://developer.apple.com/documentation/applicationservices/kspeechoutputtoaudiodeviceproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechOutputToAudioDeviceProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechOutputToAudioDeviceProperty: CFString ``` |

Modified [kSpeechOutputToExtAudioFileProperty](https://developer.apple.com/documentation/applicationservices/kspeechoutputtoextaudiofileproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechOutputToExtAudioFileProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechOutputToExtAudioFileProperty: CFString ``` |

Modified [kSpeechOutputToFileDescriptorProperty](https://developer.apple.com/documentation/applicationservices/kspeechoutputtofiledescriptorproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechOutputToFileDescriptorProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechOutputToFileDescriptorProperty: CFString ``` |

Modified [kSpeechOutputToFileURLProperty](https://developer.apple.com/documentation/applicationservices/kspeechoutputtofileurlproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechOutputToFileURLProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechOutputToFileURLProperty: CFString ``` |

Modified [kSpeechPhonemeCallBack](https://developer.apple.com/documentation/applicationservices/kspeechphonemecallback)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPhonemeCallBack: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPhonemeCallBack: CFString ``` |

Modified [kSpeechPhonemeInfoExample](https://developer.apple.com/documentation/applicationservices/kspeechphonemeinfoexample)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPhonemeInfoExample: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPhonemeInfoExample: CFString ``` |

Modified [kSpeechPhonemeInfoHiliteEnd](https://developer.apple.com/documentation/applicationservices/kspeechphonemeinfohiliteend)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPhonemeInfoHiliteEnd: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPhonemeInfoHiliteEnd: CFString ``` |

Modified [kSpeechPhonemeInfoHiliteStart](https://developer.apple.com/documentation/applicationservices/kspeechphonemeinfohilitestart)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPhonemeInfoHiliteStart: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPhonemeInfoHiliteStart: CFString ``` |

Modified [kSpeechPhonemeInfoOpcode](https://developer.apple.com/documentation/applicationservices/kspeechphonemeinfoopcode)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPhonemeInfoOpcode: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPhonemeInfoOpcode: CFString ``` |

Modified [kSpeechPhonemeInfoSymbol](https://developer.apple.com/documentation/applicationservices/kspeechphonemeinfosymbol)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPhonemeInfoSymbol: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPhonemeInfoSymbol: CFString ``` |

Modified [kSpeechPhonemeOptionsProperty](https://developer.apple.com/documentation/applicationservices/kspeechphonemeoptionsproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPhonemeOptionsProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPhonemeOptionsProperty: CFString ``` |

Modified [kSpeechPhonemeSymbolsProperty](https://developer.apple.com/documentation/applicationservices/kspeechphonemesymbolsproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPhonemeSymbolsProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPhonemeSymbolsProperty: CFString ``` |

Modified [kSpeechPitchBaseProperty](https://developer.apple.com/documentation/applicationservices/kspeechpitchbaseproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPitchBaseProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPitchBaseProperty: CFString ``` |

Modified [kSpeechPitchModProperty](https://developer.apple.com/documentation/applicationservices/kspeechpitchmodproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPitchModProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPitchModProperty: CFString ``` |

Modified [kSpeechPreflightThenPause](https://developer.apple.com/documentation/applicationservices/kspeechpreflightthenpause)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechPreflightThenPause: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechPreflightThenPause: CFString ``` |

Modified [kSpeechRateProperty](https://developer.apple.com/documentation/applicationservices/kspeechrateproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechRateProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechRateProperty: CFString ``` |

Modified [kSpeechRecentSyncProperty](https://developer.apple.com/documentation/applicationservices/kspeechrecentsyncproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechRecentSyncProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechRecentSyncProperty: CFString ``` |

Modified [kSpeechRefConProperty](https://developer.apple.com/documentation/applicationservices/kspeechrefconproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechRefConProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechRefConProperty: CFString ``` |

Modified [kSpeechRelativeDuration](https://developer.apple.com/documentation/applicationservices/kspeechrelativeduration)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechRelativeDuration: Int { get } ``` |
| To | ``` var kSpeechRelativeDuration: Int32 { get } ``` |

Modified [kSpeechRelativePitch](https://developer.apple.com/documentation/applicationservices/kspeechrelativepitch)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechRelativePitch: Int { get } ``` |
| To | ``` var kSpeechRelativePitch: Int32 { get } ``` |

Modified [kSpeechResetProperty](https://developer.apple.com/documentation/applicationservices/kspeechresetproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechResetProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechResetProperty: CFString ``` |

Modified [kSpeechShowSyllables](https://developer.apple.com/documentation/applicationservices/1552233-phoneme_generation_options/kspeechshowsyllables)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechShowSyllables: Int { get } ``` |
| To | ``` var kSpeechShowSyllables: Int32 { get } ``` |

Modified [kSpeechSpeechDoneCallBack](https://developer.apple.com/documentation/applicationservices/kspeechspeechdonecallback)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechSpeechDoneCallBack: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechSpeechDoneCallBack: CFString ``` |

Modified [kSpeechStatusNumberOfCharactersLeft](https://developer.apple.com/documentation/applicationservices/kspeechstatusnumberofcharactersleft)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechStatusNumberOfCharactersLeft: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechStatusNumberOfCharactersLeft: CFString ``` |

Modified [kSpeechStatusOutputBusy](https://developer.apple.com/documentation/applicationservices/kspeechstatusoutputbusy)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechStatusOutputBusy: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechStatusOutputBusy: CFString ``` |

Modified [kSpeechStatusOutputPaused](https://developer.apple.com/documentation/applicationservices/kspeechstatusoutputpaused)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechStatusOutputPaused: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechStatusOutputPaused: CFString ``` |

Modified [kSpeechStatusPhonemeCode](https://developer.apple.com/documentation/applicationservices/kspeechstatusphonemecode)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechStatusPhonemeCode: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechStatusPhonemeCode: CFString ``` |

Modified [kSpeechStatusProperty](https://developer.apple.com/documentation/applicationservices/kspeechstatusproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechStatusProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechStatusProperty: CFString ``` |

Modified [kSpeechSyncCallBack](https://developer.apple.com/documentation/applicationservices/kspeechsynccallback)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechSyncCallBack: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechSyncCallBack: CFString ``` |

Modified [kSpeechSynthesizerInfoIdentifier](https://developer.apple.com/documentation/applicationservices/kspeechsynthesizerinfoidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechSynthesizerInfoIdentifier: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechSynthesizerInfoIdentifier: CFString ``` |

Modified [kSpeechSynthesizerInfoManufacturer](https://developer.apple.com/documentation/applicationservices/kspeechsynthesizerinfomanufacturer)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechSynthesizerInfoManufacturer: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechSynthesizerInfoManufacturer: CFString ``` |

Modified [kSpeechSynthesizerInfoProperty](https://developer.apple.com/documentation/applicationservices/kspeechsynthesizerinfoproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechSynthesizerInfoProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechSynthesizerInfoProperty: CFString ``` |

Modified [kSpeechSynthesizerInfoVersion](https://developer.apple.com/documentation/applicationservices/kspeechsynthesizerinfoversion)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechSynthesizerInfoVersion: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechSynthesizerInfoVersion: CFString ``` |

Modified [kSpeechSynthExtensionProperty](https://developer.apple.com/documentation/applicationservices/kspeechsynthextensionproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechSynthExtensionProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechSynthExtensionProperty: CFString ``` |

Modified [kSpeechTextDoneCallBack](https://developer.apple.com/documentation/applicationservices/kspeechtextdonecallback)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechTextDoneCallBack: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechTextDoneCallBack: CFString ``` |

Modified [kSpeechVoiceCreator](https://developer.apple.com/documentation/applicationservices/kspeechvoicecreator)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechVoiceCreator: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechVoiceCreator: CFString ``` |

Modified [kSpeechVoiceID](https://developer.apple.com/documentation/applicationservices/kspeechvoiceid)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechVoiceID: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechVoiceID: CFString ``` |

Modified [kSpeechVolumeProperty](https://developer.apple.com/documentation/applicationservices/kspeechvolumeproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechVolumeProperty: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechVolumeProperty: CFString ``` |

Modified [kSpeechWordCFCallBack](https://developer.apple.com/documentation/applicationservices/kspeechwordcfcallback)

|  | Declaration |
| --- | --- |
| From | ``` var kSpeechWordCFCallBack: Unmanaged<CFString>! ``` |
| To | ``` let kSpeechWordCFCallBack: CFString ``` |

Modified [kTextToSpeechSynthType](https://developer.apple.com/documentation/applicationservices/ktexttospeechsynthtype)

|  | Declaration |
| --- | --- |
| From | ``` var kTextToSpeechSynthType: Int { get } ``` |
| To | ``` var kTextToSpeechSynthType: OSType { get } ``` |

Modified [kTextToSpeechVoiceBundleType](https://developer.apple.com/documentation/applicationservices/1552231-speech_synthesis_manager_operati/ktexttospeechvoicebundletype)

|  | Declaration |
| --- | --- |
| From | ``` var kTextToSpeechVoiceBundleType: Int { get } ``` |
| To | ``` var kTextToSpeechVoiceBundleType: OSType { get } ``` |

Modified [kTextToSpeechVoiceFileType](https://developer.apple.com/documentation/applicationservices/ktexttospeechvoicefiletype)

|  | Declaration |
| --- | --- |
| From | ``` var kTextToSpeechVoiceFileType: Int { get } ``` |
| To | ``` var kTextToSpeechVoiceFileType: OSType { get } ``` |

Modified [kTextToSpeechVoiceType](https://developer.apple.com/documentation/applicationservices/1552231-speech_synthesis_manager_operati/ktexttospeechvoicetype)

|  | Declaration |
| --- | --- |
| From | ``` var kTextToSpeechVoiceType: Int { get } ``` |
| To | ``` var kTextToSpeechVoiceType: OSType { get } ``` |

Modified [modeLiteral](https://developer.apple.com/documentation/applicationservices/modeliteral)

|  | Declaration |
| --- | --- |
| From | ``` var modeLiteral: Int { get } ``` |
| To | ``` var modeLiteral: OSType { get } ``` |

Modified [modeNormal](https://developer.apple.com/documentation/applicationservices/modenormal)

|  | Declaration |
| --- | --- |
| From | ``` var modeNormal: Int { get } ``` |
| To | ``` var modeNormal: OSType { get } ``` |

Modified [modePhonemes](https://developer.apple.com/documentation/applicationservices/1552256-speech_channel_modes/modephonemes)

|  | Declaration |
| --- | --- |
| From | ``` var modePhonemes: Int { get } ``` |
| To | ``` var modePhonemes: OSType { get } ``` |

Modified [modeText](https://developer.apple.com/documentation/applicationservices/1552256-speech_channel_modes/modetext)

|  | Declaration |
| --- | --- |
| From | ``` var modeText: Int { get } ``` |
| To | ``` var modeText: OSType { get } ``` |

Modified [modeTune](https://developer.apple.com/documentation/applicationservices/modetune)

|  | Declaration |
| --- | --- |
| From | ``` var modeTune: Int { get } ``` |
| To | ``` var modeTune: OSType { get } ``` |

Modified [NewIconActionUPP(_: IconActionProcPtr!) -> IconActionUPP!](https://developer.apple.com/documentation/applicationservices/1462738-newiconactionupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewIconActionUPP(_ userRoutine: IconActionProcPtr) -> IconActionUPP ``` |
| To | ``` func NewIconActionUPP(_ userRoutine: IconActionProcPtr!) -> IconActionUPP! ``` |

Modified [NewIconGetterUPP(_: IconGetterProcPtr!) -> IconGetterUPP!](https://developer.apple.com/documentation/applicationservices/1458777-newicongetterupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewIconGetterUPP(_ userRoutine: IconGetterProcPtr) -> IconGetterUPP ``` |
| To | ``` func NewIconGetterUPP(_ userRoutine: IconGetterProcPtr!) -> IconGetterUPP! ``` |

Modified [PasteboardPromiseKeeperProcPtr](https://developer.apple.com/documentation/applicationservices/pasteboardpromisekeeperprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias PasteboardPromiseKeeperProcPtr = CFunctionPointer<((Pasteboard!, PasteboardItemID, CFString!, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias PasteboardPromiseKeeperProcPtr = (Pasteboard!, PasteboardItemID, CFString!, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [PasteboardSetPromiseKeeper(_: Pasteboard!, _: PasteboardPromiseKeeperProcPtr!, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463604-pasteboardsetpromisekeeper)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardSetPromiseKeeper(_ inPasteboard: Pasteboard!, _ inPromiseKeeper: PasteboardPromiseKeeperProcPtr, _ inContext: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func PasteboardSetPromiseKeeper(_ inPasteboard: Pasteboard!, _ inPromiseKeeper: PasteboardPromiseKeeperProcPtr!, _ inContext: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [PMCGImageCreateWithEPSDataProvider(_: CGDataProvider?, _: CGImage) -> Unmanaged<CGImage>?](https://developer.apple.com/documentation/applicationservices/1462361-pmcgimagecreatewithepsdataprovid)

|  | Declaration |
| --- | --- |
| From | ``` func PMCGImageCreateWithEPSDataProvider(_ epsDataProvider: CGDataProvider!, _ epsPreview: CGImage!) -> Unmanaged<CGImage>! ``` |
| To | ``` func PMCGImageCreateWithEPSDataProvider(_ epsDataProvider: CGDataProvider?, _ epsPreview: CGImage) -> Unmanaged<CGImage>? ``` |

Modified [PMCopyLocalizedPPD(_: CFURL, _: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459690-pmcopylocalizedppd)

|  | Declaration |
| --- | --- |
| From | ``` func PMCopyLocalizedPPD(_ ppd: CFURL!, _ localizedPPD: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func PMCopyLocalizedPPD(_ ppd: CFURL, _ localizedPPD: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |

Modified [PMCopyPPDData(_: CFURL, _: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460345-pmcopyppddata)

|  | Declaration |
| --- | --- |
| From | ``` func PMCopyPPDData(_ ppd: CFURL!, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func PMCopyPPDData(_ ppd: CFURL, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified [PMGetCollate(_: PMPrintSettings, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464492-pmgetcollate)

|  | Declaration |
| --- | --- |
| From | ``` func PMGetCollate(_ printSettings: PMPrintSettings, _ collate: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func PMGetCollate(_ printSettings: PMPrintSettings, _ collate: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [PMPageFormatCreateWithDataRepresentation(_: CFData, _: UnsafeMutablePointer<PMPageFormat>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462876-pmpageformatcreatewithdatarepres)

|  | Declaration |
| --- | --- |
| From | ``` func PMPageFormatCreateWithDataRepresentation(_ data: CFData!, _ pageFormat: UnsafeMutablePointer<PMPageFormat>) -> OSStatus ``` |
| To | ``` func PMPageFormatCreateWithDataRepresentation(_ data: CFData, _ pageFormat: UnsafeMutablePointer<PMPageFormat>) -> OSStatus ``` |

Modified [PMPaperCreateCustom(_: PMPrinter, _: CFString?, _: CFString?, _: Double, _: Double, _: UnsafePointer<PMPaperMargins>, _: UnsafeMutablePointer<PMPaper>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459322-pmpapercreatecustom)

|  | Declaration |
| --- | --- |
| From | ``` func PMPaperCreateCustom(_ printer: PMPrinter, _ id: CFString!, _ name: CFString!, _ width: Double, _ height: Double, _ margins: UnsafePointer<PMPaperMargins>, _ paperP: UnsafeMutablePointer<PMPaper>) -> OSStatus ``` |
| To | ``` func PMPaperCreateCustom(_ printer: PMPrinter, _ id: CFString?, _ name: CFString?, _ width: Double, _ height: Double, _ margins: UnsafePointer<PMPaperMargins>, _ paperP: UnsafeMutablePointer<PMPaper>) -> OSStatus ``` |

Modified [PMPaperIsCustom(_: PMPaper) -> Bool](https://developer.apple.com/documentation/applicationservices/1459526-pmpaperiscustom)

|  | Declaration |
| --- | --- |
| From | ``` func PMPaperIsCustom(_ paper: PMPaper) -> Boolean ``` |
| To | ``` func PMPaperIsCustom(_ paper: PMPaper) -> Bool ``` |

Modified [PMPrinterCopyDescriptionURL(_: PMPrinter, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459187-pmprintercopydescriptionurl)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterCopyDescriptionURL(_ printer: PMPrinter, _ descriptionType: CFString!, _ fileURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func PMPrinterCopyDescriptionURL(_ printer: PMPrinter, _ descriptionType: CFString, _ fileURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |

Modified [PMPrinterCreateFromPrinterID(_: CFString) -> PMPrinter](https://developer.apple.com/documentation/applicationservices/1461363-pmprintercreatefromprinterid)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterCreateFromPrinterID(_ printerID: CFString!) -> PMPrinter ``` |
| To | ``` func PMPrinterCreateFromPrinterID(_ printerID: CFString) -> PMPrinter ``` |

Modified [PMPrinterGetCommInfo(_: PMPrinter, _: UnsafeMutablePointer<DarwinBoolean>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461069-pmprintergetcomminfo)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetCommInfo(_ printer: PMPrinter, _ supportsControlCharRangeP: UnsafeMutablePointer<Boolean>, _ supportsEightBitP: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func PMPrinterGetCommInfo(_ printer: PMPrinter, _ supportsControlCharRangeP: UnsafeMutablePointer<DarwinBoolean>, _ supportsEightBitP: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [PMPrinterGetID(_: PMPrinter) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/applicationservices/1459606-pmprintergetid)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetID(_ printer: PMPrinter) -> Unmanaged<CFString>! ``` |
| To | ``` func PMPrinterGetID(_ printer: PMPrinter) -> Unmanaged<CFString>? ``` |

Modified [PMPrinterGetLocation(_: PMPrinter) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/applicationservices/1461467-pmprintergetlocation)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetLocation(_ printer: PMPrinter) -> Unmanaged<CFString>! ``` |
| To | ``` func PMPrinterGetLocation(_ printer: PMPrinter) -> Unmanaged<CFString>? ``` |

Modified [PMPrinterGetName(_: PMPrinter) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/applicationservices/1459018-pmprintergetname)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetName(_ printer: PMPrinter) -> Unmanaged<CFString>! ``` |
| To | ``` func PMPrinterGetName(_ printer: PMPrinter) -> Unmanaged<CFString>? ``` |

Modified [PMPrinterIsDefault(_: PMPrinter) -> Bool](https://developer.apple.com/documentation/applicationservices/1459030-pmprinterisdefault)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterIsDefault(_ printer: PMPrinter) -> Boolean ``` |
| To | ``` func PMPrinterIsDefault(_ printer: PMPrinter) -> Bool ``` |

Modified [PMPrinterIsFavorite(_: PMPrinter) -> Bool](https://developer.apple.com/documentation/applicationservices/1462074-pmprinterisfavorite)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterIsFavorite(_ printer: PMPrinter) -> Boolean ``` |
| To | ``` func PMPrinterIsFavorite(_ printer: PMPrinter) -> Bool ``` |

Modified [PMPrinterIsPostScriptCapable(_: PMPrinter) -> Bool](https://developer.apple.com/documentation/applicationservices/1464168-pmprinterispostscriptcapable)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterIsPostScriptCapable(_ printer: PMPrinter) -> Boolean ``` |
| To | ``` func PMPrinterIsPostScriptCapable(_ printer: PMPrinter) -> Bool ``` |

Modified [PMPrinterIsPostScriptPrinter(_: PMPrinter, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462257-pmprinterispostscriptprinter)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterIsPostScriptPrinter(_ printer: PMPrinter, _ isPSPrinter: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func PMPrinterIsPostScriptPrinter(_ printer: PMPrinter, _ isPSPrinter: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [PMPrinterIsRemote(_: PMPrinter, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461377-pmprinterisremote)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterIsRemote(_ printer: PMPrinter, _ isRemoteP: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func PMPrinterIsRemote(_ printer: PMPrinter, _ isRemoteP: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [PMPrinterPrintWithFile(_: PMPrinter, _: PMPrintSettings, _: PMPageFormat, _: CFString?, _: CFURL) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464600-pmprinterprintwithfile)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterPrintWithFile(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString!, _ fileURL: CFURL!) -> OSStatus ``` |
| To | ``` func PMPrinterPrintWithFile(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString?, _ fileURL: CFURL) -> OSStatus ``` |

Modified [PMPrinterPrintWithProvider(_: PMPrinter, _: PMPrintSettings, _: PMPageFormat, _: CFString, _: CGDataProvider) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461110-pmprinterprintwithprovider)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterPrintWithProvider(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString!, _ provider: CGDataProvider!) -> OSStatus ``` |
| To | ``` func PMPrinterPrintWithProvider(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString, _ provider: CGDataProvider) -> OSStatus ``` |

Modified [PMPrinterSendCommand(_: PMPrinter, _: CFString, _: CFString?, _: CFDictionary?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463872-pmprintersendcommand)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterSendCommand(_ printer: PMPrinter, _ commandString: CFString!, _ jobTitle: CFString!, _ options: CFDictionary!) -> OSStatus ``` |
| To | ``` func PMPrinterSendCommand(_ printer: PMPrinter, _ commandString: CFString, _ jobTitle: CFString?, _ options: CFDictionary?) -> OSStatus ``` |

Modified [PMPrinterWritePostScriptToURL(_: PMPrinter, _: PMPrintSettings, _: PMPageFormat, _: CFString?, _: CFURL, _: CFURL) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459729-pmprinterwritepostscripttourl)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterWritePostScriptToURL(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString!, _ sourceFileURL: CFURL!, _ destinationFileURL: CFURL!) -> OSStatus ``` |
| To | ``` func PMPrinterWritePostScriptToURL(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString?, _ sourceFileURL: CFURL, _ destinationFileURL: CFURL) -> OSStatus ``` |

Modified [PMPrintSettingsCreateWithDataRepresentation(_: CFData, _: UnsafeMutablePointer<PMPrintSettings>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462203-pmprintsettingscreatewithdatarep)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsCreateWithDataRepresentation(_ data: CFData!, _ printSettings: UnsafeMutablePointer<PMPrintSettings>) -> OSStatus ``` |
| To | ``` func PMPrintSettingsCreateWithDataRepresentation(_ data: CFData, _ printSettings: UnsafeMutablePointer<PMPrintSettings>) -> OSStatus ``` |

Modified [PMPrintSettingsGetValue(_: PMPrintSettings, _: CFString, _: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460602-pmprintsettingsgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsGetValue(_ printSettings: PMPrintSettings, _ key: CFString!, _ value: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func PMPrintSettingsGetValue(_ printSettings: PMPrintSettings, _ key: CFString, _ value: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |

Modified [PMPrintSettingsSetJobName(_: PMPrintSettings, _: CFString) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460149-pmprintsettingssetjobname)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsSetJobName(_ printSettings: PMPrintSettings, _ name: CFString!) -> OSStatus ``` |
| To | ``` func PMPrintSettingsSetJobName(_ printSettings: PMPrintSettings, _ name: CFString) -> OSStatus ``` |

Modified [PMPrintSettingsSetValue(_: PMPrintSettings, _: CFString, _: AnyObject?, _: Bool) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461697-pmprintsettingssetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsSetValue(_ printSettings: PMPrintSettings, _ key: CFString!, _ value: AnyObject!, _ locked: Boolean) -> OSStatus ``` |
| To | ``` func PMPrintSettingsSetValue(_ printSettings: PMPrintSettings, _ key: CFString, _ value: AnyObject?, _ locked: Bool) -> OSStatus ``` |

Modified [PMServerLaunchPrinterBrowser(_: PMServer, _: CFDictionary?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460175-pmserverlaunchprinterbrowser)

|  | Declaration |
| --- | --- |
| From | ``` func PMServerLaunchPrinterBrowser(_ server: PMServer, _ options: CFDictionary!) -> OSStatus ``` |
| To | ``` func PMServerLaunchPrinterBrowser(_ server: PMServer, _ options: CFDictionary?) -> OSStatus ``` |

Modified [PMSessionGetDataFromSession(_: PMPrintSession, _: CFString, _: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462964-pmsessiongetdatafromsession)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionGetDataFromSession(_ printSession: PMPrintSession, _ key: CFString!, _ data: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func PMSessionGetDataFromSession(_ printSession: PMPrintSession, _ key: CFString, _ data: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |

Modified [PMSessionSetDataInSession(_: PMPrintSession, _: CFString, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461902-pmsessionsetdatainsession)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionSetDataInSession(_ printSession: PMPrintSession, _ key: CFString!, _ data: AnyObject!) -> OSStatus ``` |
| To | ``` func PMSessionSetDataInSession(_ printSession: PMPrintSession, _ key: CFString, _ data: AnyObject) -> OSStatus ``` |

Modified [PMSessionSetDestination(_: PMPrintSession, _: PMPrintSettings, _: PMDestinationType, _: CFString?, _: CFURL?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459855-pmsessionsetdestination)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionSetDestination(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destType: PMDestinationType, _ destFormat: CFString!, _ destLocation: CFURL!) -> OSStatus ``` |
| To | ``` func PMSessionSetDestination(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destType: PMDestinationType, _ destFormat: CFString?, _ destLocation: CFURL?) -> OSStatus ``` |

Modified [PMSessionValidatePageFormat(_: PMPrintSession, _: PMPageFormat, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459090-pmsessionvalidatepageformat)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionValidatePageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ result: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func PMSessionValidatePageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ changed: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [PMSessionValidatePrintSettings(_: PMPrintSession, _: PMPrintSettings, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1458994-pmsessionvalidateprintsettings)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionValidatePrintSettings(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ result: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func PMSessionValidatePrintSettings(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ changed: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [PMSetCollate(_: PMPrintSettings, _: Bool) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463223-pmsetcollate)

|  | Declaration |
| --- | --- |
| From | ``` func PMSetCollate(_ printSettings: PMPrintSettings, _ collate: Boolean) -> OSStatus ``` |
| To | ``` func PMSetCollate(_ printSettings: PMPrintSettings, _ collate: Bool) -> OSStatus ``` |

Modified [PMSetCopies(_: PMPrintSettings, _: UInt32, _: Bool) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463804-pmsetcopies)

|  | Declaration |
| --- | --- |
| From | ``` func PMSetCopies(_ printSettings: PMPrintSettings, _ copies: UInt32, _ lock: Boolean) -> OSStatus ``` |
| To | ``` func PMSetCopies(_ printSettings: PMPrintSettings, _ copies: UInt32, _ lock: Bool) -> OSStatus ``` |

Modified [PMSetFirstPage(_: PMPrintSettings, _: UInt32, _: Bool) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461519-pmsetfirstpage)

|  | Declaration |
| --- | --- |
| From | ``` func PMSetFirstPage(_ printSettings: PMPrintSettings, _ first: UInt32, _ lock: Boolean) -> OSStatus ``` |
| To | ``` func PMSetFirstPage(_ printSettings: PMPrintSettings, _ first: UInt32, _ lock: Bool) -> OSStatus ``` |

Modified [PMSetLastPage(_: PMPrintSettings, _: UInt32, _: Bool) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463595-pmsetlastpage)

|  | Declaration |
| --- | --- |
| From | ``` func PMSetLastPage(_ printSettings: PMPrintSettings, _ last: UInt32, _ lock: Boolean) -> OSStatus ``` |
| To | ``` func PMSetLastPage(_ printSettings: PMPrintSettings, _ last: UInt32, _ lock: Bool) -> OSStatus ``` |

Modified [PMSetOrientation(_: PMPageFormat, _: PMOrientation, _: Bool) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459016-pmsetorientation)

|  | Declaration |
| --- | --- |
| From | ``` func PMSetOrientation(_ pageFormat: PMPageFormat, _ orientation: PMOrientation, _ lock: Boolean) -> OSStatus ``` |
| To | ``` func PMSetOrientation(_ pageFormat: PMPageFormat, _ orientation: PMOrientation, _ lock: Bool) -> OSStatus ``` |

Modified [PMWorkflowSubmitPDFWithOptions(_: CFURL, _: CFString?, _: UnsafePointer<Int8>, _: CFURL) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463747-pmworkflowsubmitpdfwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func PMWorkflowSubmitPDFWithOptions(_ workflowItem: CFURL!, _ title: CFString!, _ options: UnsafePointer<Int8>, _ pdfFile: CFURL!) -> OSStatus ``` |
| To | ``` func PMWorkflowSubmitPDFWithOptions(_ workflowItem: CFURL, _ title: CFString?, _ options: UnsafePointer<Int8>, _ pdfFile: CFURL) -> OSStatus ``` |

Modified [PMWorkflowSubmitPDFWithSettings(_: CFURL, _: PMPrintSettings, _: CFURL) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1458874-pmworkflowsubmitpdfwithsettings)

|  | Declaration |
| --- | --- |
| From | ``` func PMWorkflowSubmitPDFWithSettings(_ workflowItem: CFURL!, _ settings: PMPrintSettings, _ pdfFile: CFURL!) -> OSStatus ``` |
| To | ``` func PMWorkflowSubmitPDFWithSettings(_ workflowItem: CFURL, _ settings: PMPrintSettings, _ pdfFile: CFURL) -> OSStatus ``` |

Modified [QDArcProcPtr](https://developer.apple.com/documentation/applicationservices/qdarcprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDArcProcPtr = CFunctionPointer<((GrafVerb, UnsafePointer<Rect>, Int16, Int16) -> Void)> ``` |
| To | ``` typealias QDArcProcPtr = (GrafVerb, UnsafePointer<Rect>, Int16, Int16) -> Void ``` |

Modified [QDBitsProcPtr](https://developer.apple.com/documentation/applicationservices/qdbitsprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDBitsProcPtr = CFunctionPointer<((UnsafePointer<BitMap>, UnsafePointer<Rect>, UnsafePointer<Rect>, Int16, RgnHandle) -> Void)> ``` |
| To | ``` typealias QDBitsProcPtr = (UnsafePointer<BitMap>, UnsafePointer<Rect>, UnsafePointer<Rect>, Int16, RgnHandle) -> Void ``` |

Modified [QDCommentProcPtr](https://developer.apple.com/documentation/applicationservices/qdcommentprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDCommentProcPtr = CFunctionPointer<((Int16, Int16, Handle) -> Void)> ``` |
| To | ``` typealias QDCommentProcPtr = (Int16, Int16, Handle) -> Void ``` |

Modified [QDGetPicProcPtr](https://developer.apple.com/documentation/applicationservices/qdgetpicprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDGetPicProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>, Int16) -> Void)> ``` |
| To | ``` typealias QDGetPicProcPtr = (UnsafeMutablePointer<Void>, Int16) -> Void ``` |

Modified [QDJShieldCursorProcPtr](https://developer.apple.com/documentation/applicationservices/qdjshieldcursorprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDJShieldCursorProcPtr = CFunctionPointer<((Int16, Int16, Int16, Int16) -> Void)> ``` |
| To | ``` typealias QDJShieldCursorProcPtr = (Int16, Int16, Int16, Int16) -> Void ``` |

Modified [QDLineProcPtr](https://developer.apple.com/documentation/applicationservices/qdlineprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDLineProcPtr = CFunctionPointer<((Point) -> Void)> ``` |
| To | ``` typealias QDLineProcPtr = (Point) -> Void ``` |

Modified [QDOpcodeProcPtr](https://developer.apple.com/documentation/applicationservices/qdopcodeprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDOpcodeProcPtr = CFunctionPointer<((UnsafePointer<Rect>, UnsafePointer<Rect>, UInt16, Int16) -> Void)> ``` |
| To | ``` typealias QDOpcodeProcPtr = (UnsafePointer<Rect>, UnsafePointer<Rect>, UInt16, Int16) -> Void ``` |

Modified [QDOvalProcPtr](https://developer.apple.com/documentation/applicationservices/qdovalprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDOvalProcPtr = CFunctionPointer<((GrafVerb, UnsafePointer<Rect>) -> Void)> ``` |
| To | ``` typealias QDOvalProcPtr = (GrafVerb, UnsafePointer<Rect>) -> Void ``` |

Modified [QDPolyProcPtr](https://developer.apple.com/documentation/applicationservices/qdpolyprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPolyProcPtr = CFunctionPointer<((GrafVerb, PolyHandle) -> Void)> ``` |
| To | ``` typealias QDPolyProcPtr = (GrafVerb, PolyHandle) -> Void ``` |

Modified [QDPrinterStatusProcPtr](https://developer.apple.com/documentation/applicationservices/qdprinterstatusprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPrinterStatusProcPtr = CFunctionPointer<((PrinterStatusOpcode, CGrafPtr, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias QDPrinterStatusProcPtr = (PrinterStatusOpcode, CGrafPtr, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [QDPutPicProcPtr](https://developer.apple.com/documentation/applicationservices/qdputpicprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPutPicProcPtr = CFunctionPointer<((UnsafePointer<Void>, Int16) -> Void)> ``` |
| To | ``` typealias QDPutPicProcPtr = (UnsafePointer<Void>, Int16) -> Void ``` |

Modified [QDRectProcPtr](https://developer.apple.com/documentation/applicationservices/qdrectprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRectProcPtr = CFunctionPointer<((GrafVerb, UnsafePointer<Rect>) -> Void)> ``` |
| To | ``` typealias QDRectProcPtr = (GrafVerb, UnsafePointer<Rect>) -> Void ``` |

Modified [QDRgnProcPtr](https://developer.apple.com/documentation/applicationservices/qdrgnprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRgnProcPtr = CFunctionPointer<((GrafVerb, RgnHandle) -> Void)> ``` |
| To | ``` typealias QDRgnProcPtr = (GrafVerb, RgnHandle) -> Void ``` |

Modified [QDRRectProcPtr](https://developer.apple.com/documentation/applicationservices/qdrrectprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRRectProcPtr = CFunctionPointer<((GrafVerb, UnsafePointer<Rect>, Int16, Int16) -> Void)> ``` |
| To | ``` typealias QDRRectProcPtr = (GrafVerb, UnsafePointer<Rect>, Int16, Int16) -> Void ``` |

Modified [QDStdGlyphsProcPtr](https://developer.apple.com/documentation/applicationservices/qdstdglyphsprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDStdGlyphsProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> OSStatus)> ``` |
| To | ``` typealias QDStdGlyphsProcPtr = (UnsafeMutablePointer<Void>, Int) -> OSStatus ``` |

Modified [QDTextProcPtr](https://developer.apple.com/documentation/applicationservices/qdtextprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDTextProcPtr = CFunctionPointer<((Int16, UnsafePointer<Void>, Point, Point) -> Void)> ``` |
| To | ``` typealias QDTextProcPtr = (Int16, UnsafePointer<Void>, Point, Point) -> Void ``` |

Modified [QDTxMeasProcPtr](https://developer.apple.com/documentation/applicationservices/qdtxmeasprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDTxMeasProcPtr = CFunctionPointer<((Int16, UnsafePointer<Void>, UnsafeMutablePointer<Point>, UnsafeMutablePointer<Point>, UnsafeMutablePointer<FontInfo>) -> Int16)> ``` |
| To | ``` typealias QDTxMeasProcPtr = (Int16, UnsafePointer<Void>, UnsafeMutablePointer<Point>, UnsafeMutablePointer<Point>, UnsafeMutablePointer<FontInfo>) -> Int16 ``` |

Modified [RedrawBackgroundProcPtr](https://developer.apple.com/documentation/applicationservices/redrawbackgroundprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias RedrawBackgroundProcPtr = CFunctionPointer<((ATSUTextLayout, UniCharArrayOffset, Int, UnsafeMutablePointer<ATSTrapezoid>, Int) -> Boolean)> ``` |
| To | ``` typealias RedrawBackgroundProcPtr = (ATSUTextLayout, UniCharArrayOffset, Int, UnsafeMutablePointer<ATSTrapezoid>, Int) -> DarwinBoolean ``` |

Modified [RegionToRectsProcPtr](https://developer.apple.com/documentation/applicationservices/regiontorectsprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias RegionToRectsProcPtr = CFunctionPointer<((UInt16, RgnHandle, UnsafePointer<Rect>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias RegionToRectsProcPtr = (UInt16, RgnHandle, UnsafePointer<Rect>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [SetSpeechProperty(_: SpeechChannel, _: CFString, _: AnyObject?) -> OSErr](https://developer.apple.com/documentation/applicationservices/1459256-setspeechproperty)

|  | Declaration |
| --- | --- |
| From | ``` func SetSpeechProperty(_ chan: SpeechChannel, _ property: CFString!, _ object: AnyObject!) -> OSErr ``` |
| To | ``` func SetSpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: AnyObject?) -> OSErr ``` |

Modified [soCharacterMode](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/socharactermode)

|  | Declaration |
| --- | --- |
| From | ``` var soCharacterMode: Int { get } ``` |
| To | ``` var soCharacterMode: OSType { get } ``` |

Modified [soCommandDelimiter](https://developer.apple.com/documentation/applicationservices/socommanddelimiter)

|  | Declaration |
| --- | --- |
| From | ``` var soCommandDelimiter: Int { get } ``` |
| To | ``` var soCommandDelimiter: OSType { get } ``` |

Modified [soCurrentA5](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/socurrenta5)

|  | Declaration |
| --- | --- |
| From | ``` var soCurrentA5: Int { get } ``` |
| To | ``` var soCurrentA5: OSType { get } ``` |

Modified [soCurrentVoice](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/socurrentvoice)

|  | Declaration |
| --- | --- |
| From | ``` var soCurrentVoice: Int { get } ``` |
| To | ``` var soCurrentVoice: OSType { get } ``` |

Modified [soErrorCallBack](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/soerrorcallback)

|  | Declaration |
| --- | --- |
| From | ``` var soErrorCallBack: Int { get } ``` |
| To | ``` var soErrorCallBack: OSType { get } ``` |

Modified [soErrors](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/soerrors)

|  | Declaration |
| --- | --- |
| From | ``` var soErrors: Int { get } ``` |
| To | ``` var soErrors: OSType { get } ``` |

Modified [soInputMode](https://developer.apple.com/documentation/applicationservices/soinputmode)

|  | Declaration |
| --- | --- |
| From | ``` var soInputMode: Int { get } ``` |
| To | ``` var soInputMode: OSType { get } ``` |

Modified [soNumberMode](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sonumbermode)

|  | Declaration |
| --- | --- |
| From | ``` var soNumberMode: Int { get } ``` |
| To | ``` var soNumberMode: OSType { get } ``` |

Modified [soOutputToAudioDevice](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sooutputtoaudiodevice)

|  | Declaration |
| --- | --- |
| From | ``` var soOutputToAudioDevice: Int { get } ``` |
| To | ``` var soOutputToAudioDevice: OSType { get } ``` |

Modified [soOutputToExtAudioFile](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sooutputtoextaudiofile)

|  | Declaration |
| --- | --- |
| From | ``` var soOutputToExtAudioFile: Int { get } ``` |
| To | ``` var soOutputToExtAudioFile: OSType { get } ``` |

Modified [soOutputToFileWithCFURL](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sooutputtofilewithcfurl)

|  | Declaration |
| --- | --- |
| From | ``` var soOutputToFileWithCFURL: Int { get } ``` |
| To | ``` var soOutputToFileWithCFURL: OSType { get } ``` |

Modified [soPhonemeCallBack](https://developer.apple.com/documentation/applicationservices/sophonemecallback)

|  | Declaration |
| --- | --- |
| From | ``` var soPhonemeCallBack: Int { get } ``` |
| To | ``` var soPhonemeCallBack: OSType { get } ``` |

Modified [soPhonemeOptions](https://developer.apple.com/documentation/applicationservices/sophonemeoptions)

|  | Declaration |
| --- | --- |
| From | ``` var soPhonemeOptions: Int { get } ``` |
| To | ``` var soPhonemeOptions: OSType { get } ``` |

Modified [soPhonemeSymbols](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sophonemesymbols)

|  | Declaration |
| --- | --- |
| From | ``` var soPhonemeSymbols: Int { get } ``` |
| To | ``` var soPhonemeSymbols: OSType { get } ``` |

Modified [soPitchBase](https://developer.apple.com/documentation/applicationservices/sopitchbase)

|  | Declaration |
| --- | --- |
| From | ``` var soPitchBase: Int { get } ``` |
| To | ``` var soPitchBase: OSType { get } ``` |

Modified [soPitchMod](https://developer.apple.com/documentation/applicationservices/sopitchmod)

|  | Declaration |
| --- | --- |
| From | ``` var soPitchMod: Int { get } ``` |
| To | ``` var soPitchMod: OSType { get } ``` |

Modified [soRate](https://developer.apple.com/documentation/applicationservices/sorate)

|  | Declaration |
| --- | --- |
| From | ``` var soRate: Int { get } ``` |
| To | ``` var soRate: OSType { get } ``` |

Modified [soRecentSync](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sorecentsync)

|  | Declaration |
| --- | --- |
| From | ``` var soRecentSync: Int { get } ``` |
| To | ``` var soRecentSync: OSType { get } ``` |

Modified [soRefCon](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sorefcon)

|  | Declaration |
| --- | --- |
| From | ``` var soRefCon: Int { get } ``` |
| To | ``` var soRefCon: OSType { get } ``` |

Modified [soReset](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/soreset)

|  | Declaration |
| --- | --- |
| From | ``` var soReset: Int { get } ``` |
| To | ``` var soReset: OSType { get } ``` |

Modified [soSoundOutput](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sosoundoutput)

|  | Declaration |
| --- | --- |
| From | ``` var soSoundOutput: Int { get } ``` |
| To | ``` var soSoundOutput: OSType { get } ``` |

Modified [soSpeechDoneCallBack](https://developer.apple.com/documentation/applicationservices/sospeechdonecallback)

|  | Declaration |
| --- | --- |
| From | ``` var soSpeechDoneCallBack: Int { get } ``` |
| To | ``` var soSpeechDoneCallBack: OSType { get } ``` |

Modified [soStatus](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sostatus)

|  | Declaration |
| --- | --- |
| From | ``` var soStatus: Int { get } ``` |
| To | ``` var soStatus: OSType { get } ``` |

Modified [soSyncCallBack](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sosynccallback)

|  | Declaration |
| --- | --- |
| From | ``` var soSyncCallBack: Int { get } ``` |
| To | ``` var soSyncCallBack: OSType { get } ``` |

Modified [soSynthExtension](https://developer.apple.com/documentation/applicationservices/sosynthextension)

|  | Declaration |
| --- | --- |
| From | ``` var soSynthExtension: Int { get } ``` |
| To | ``` var soSynthExtension: OSType { get } ``` |

Modified [soSynthType](https://developer.apple.com/documentation/applicationservices/1552228-speech_channel_information_const/sosynthtype)

|  | Declaration |
| --- | --- |
| From | ``` var soSynthType: Int { get } ``` |
| To | ``` var soSynthType: OSType { get } ``` |

Modified [soTextDoneCallBack](https://developer.apple.com/documentation/applicationservices/sotextdonecallback)

|  | Declaration |
| --- | --- |
| From | ``` var soTextDoneCallBack: Int { get } ``` |
| To | ``` var soTextDoneCallBack: OSType { get } ``` |

Modified [soVoiceDescription](https://developer.apple.com/documentation/applicationservices/1552254-voice_information_selectors/sovoicedescription)

|  | Declaration |
| --- | --- |
| From | ``` var soVoiceDescription: Int { get } ``` |
| To | ``` var soVoiceDescription: OSType { get } ``` |

Modified [soVoiceFile](https://developer.apple.com/documentation/applicationservices/1552254-voice_information_selectors/sovoicefile)

|  | Declaration |
| --- | --- |
| From | ``` var soVoiceFile: Int { get } ``` |
| To | ``` var soVoiceFile: OSType { get } ``` |

Modified [soVolume](https://developer.apple.com/documentation/applicationservices/sovolume)

|  | Declaration |
| --- | --- |
| From | ``` var soVolume: Int { get } ``` |
| To | ``` var soVolume: OSType { get } ``` |

Modified [soWordCallBack](https://developer.apple.com/documentation/applicationservices/sowordcallback)

|  | Declaration |
| --- | --- |
| From | ``` var soWordCallBack: Int { get } ``` |
| To | ``` var soWordCallBack: OSType { get } ``` |

Modified [SpeakCFString(_: SpeechChannel, _: CFString, _: CFDictionary?) -> OSErr](https://developer.apple.com/documentation/applicationservices/1461621-speakcfstring)

|  | Declaration |
| --- | --- |
| From | ``` func SpeakCFString(_ chan: SpeechChannel, _ aString: CFString!, _ options: CFDictionary!) -> OSErr ``` |
| To | ``` func SpeakCFString(_ chan: SpeechChannel, _ aString: CFString, _ options: CFDictionary?) -> OSErr ``` |

Modified [SpeechDoneProcPtr](https://developer.apple.com/documentation/applicationservices/speechdoneprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechDoneProcPtr = CFunctionPointer<((SpeechChannel, SRefCon) -> Void)> ``` |
| To | ``` typealias SpeechDoneProcPtr = (SpeechChannel, SRefCon) -> Void ``` |

Modified [SpeechErrorCFProcPtr](https://developer.apple.com/documentation/applicationservices/speecherrorcfprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechErrorCFProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, CFError!) -> Void)> ``` |
| To | ``` typealias SpeechErrorCFProcPtr = (SpeechChannel, SRefCon, CFError) -> Void ``` |

Modified [SpeechErrorProcPtr](https://developer.apple.com/documentation/applicationservices/speecherrorprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechErrorProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, OSErr, Int) -> Void)> ``` |
| To | ``` typealias SpeechErrorProcPtr = (SpeechChannel, SRefCon, OSErr, Int) -> Void ``` |

Modified [SpeechPhonemeProcPtr](https://developer.apple.com/documentation/applicationservices/speechphonemeprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechPhonemeProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, Int16) -> Void)> ``` |
| To | ``` typealias SpeechPhonemeProcPtr = (SpeechChannel, SRefCon, Int16) -> Void ``` |

Modified [SpeechSyncProcPtr](https://developer.apple.com/documentation/applicationservices/speechsyncprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechSyncProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, OSType) -> Void)> ``` |
| To | ``` typealias SpeechSyncProcPtr = (SpeechChannel, SRefCon, OSType) -> Void ``` |

Modified [SpeechSynthesisRegisterModuleURL(_: CFURL) -> OSErr](https://developer.apple.com/documentation/applicationservices/1459624-speechsynthesisregistermoduleurl)

|  | Declaration |
| --- | --- |
| From | ``` func SpeechSynthesisRegisterModuleURL(_ url: CFURL!) -> OSErr ``` |
| To | ``` func SpeechSynthesisRegisterModuleURL(_ url: CFURL) -> OSErr ``` |

Modified [SpeechSynthesisUnregisterModuleURL(_: CFURL) -> OSErr](https://developer.apple.com/documentation/applicationservices/1462511-speechsynthesisunregistermoduleu)

|  | Declaration |
| --- | --- |
| From | ``` func SpeechSynthesisUnregisterModuleURL(_ url: CFURL!) -> OSErr ``` |
| To | ``` func SpeechSynthesisUnregisterModuleURL(_ url: CFURL) -> OSErr ``` |

Modified [SpeechTextDoneProcPtr](https://developer.apple.com/documentation/applicationservices/speechtextdoneprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechTextDoneProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<Int32>) -> Void)> ``` |
| To | ``` typealias SpeechTextDoneProcPtr = (SpeechChannel, SRefCon, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<Int32>) -> Void ``` |

Modified [SpeechWordCFProcPtr](https://developer.apple.com/documentation/applicationservices/speechwordcfprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechWordCFProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, CFString!, CFRange) -> Void)> ``` |
| To | ``` typealias SpeechWordCFProcPtr = (SpeechChannel, SRefCon, CFString, CFRange) -> Void ``` |

Modified [SpeechWordProcPtr](https://developer.apple.com/documentation/applicationservices/speechwordprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechWordProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, UInt, UInt16) -> Void)> ``` |
| To | ``` typealias SpeechWordProcPtr = (SpeechChannel, SRefCon, UInt, UInt16) -> Void ``` |

Modified [UAZoomEnabled() -> Bool](https://developer.apple.com/documentation/applicationservices/1462288-uazoomenabled)

|  | Declaration |
| --- | --- |
| From | ``` func UAZoomEnabled() -> Boolean ``` |
| To | ``` func UAZoomEnabled() -> Bool ``` |

Modified [UseSpeechDictionary(_: SpeechChannel, _: CFDictionary) -> OSErr](https://developer.apple.com/documentation/applicationservices/1463688-usespeechdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func UseSpeechDictionary(_ chan: SpeechChannel, _ speechDictionary: CFDictionary!) -> OSErr ``` |
| To | ``` func UseSpeechDictionary(_ chan: SpeechChannel, _ speechDictionary: CFDictionary) -> OSErr ``` |

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
