---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/ApplicationServices.html
archived_at: '2026-07-18T02:50:56.724604Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# ApplicationServices Changes for Swift

### ApplicationServices

Removed ATSFontQuerySourceContext.init(version: UInt32, refCon: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!)Removed ATSUBackgroundData.init(backgroundUPP: RedrawBackgroundUPP!)Removed ATSUGlyphInfo.init(glyphID: GlyphID, reserved: UInt16, layoutFlags: UInt32, charIndex: UniCharArrayOffset, style: ATSUStyle, deltaY: Float32, idealX: Float32, screenX: Int16, caretX: Int16)Removed ATSUGlyphInfoArray.init(layout: ATSUTextLayout, numGlyphs: Int, glyphs: (ATSUGlyphInfo))Removed ATSULayoutOperationOverrideSpecifier.init(operationSelector: ATSULayoutOperationSelector, overrideUPP: ATSUDirectLayoutOperationOverrideUPP!)Removed [AXMenuItemModifiers.None](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifiernone)Removed [BitMap.init(baseAddr: Ptr, rowBytes: Int16, bounds: Rect)](https://developer.apple.com/documentation/applicationservices/bitmap/1464073-init)Removed [CMDeviceInfo.init(dataVersion: UInt32, deviceClass: CMDeviceClass, deviceID: CMDeviceID, deviceScope: CMDeviceScope, deviceState: CMDeviceState, defaultProfileID: CMDeviceProfileID, deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, profileCount: UInt32, reserved: UInt32)](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo/1461251-init)Removed CQDProcs.init(textProc: QDTextUPP!, lineProc: QDLineUPP!, rectProc: QDRectUPP!, rRectProc: QDRRectUPP!, ovalProc: QDOvalUPP!, arcProc: QDArcUPP!, polyProc: QDPolyUPP!, rgnProc: QDRgnUPP!, bitsProc: QDBitsUPP!, commentProc: QDCommentUPP!, txMeasProc: QDTxMeasUPP!, getPicProc: QDGetPicUPP!, putPicProc: QDPutPicUPP!, opcodeProc: QDOpcodeUPP!, newProc1: UniversalProcPtr!, glyphsProc: QDStdGlyphsUPP!, printerStatusProc: QDPrinterStatusUPP!, newProc4: UniversalProcPtr!, newProc5: UniversalProcPtr!, newProc6: UniversalProcPtr!)Removed [GDevice.init(gdRefNum: Int16, gdID: Int16, gdType: Int16, gdITable: Handle, gdResPref: Int16, gdSearchProc: Handle, gdCompProc: Handle, gdFlags: Int16, gdPMap: PixMapHandle, gdRefCon: Int32, gdNextGD: GDHandle, gdRect: Rect, gdMode: Int32, gdCCBytes: Int16, gdCCDepth: Int16, gdCCXData: Handle, gdCCXMask: Handle, gdExt: Handle)](https://developer.apple.com/documentation/applicationservices/gdevice/1458837-init)Removed HomographDicInfoRec.init(dictionaryID: DCMDictionaryID, uniqueID: DCMUniqueID)Removed [LAMorphemeRec.init(sourceTextLength: UInt32, sourceTextPtr: LogicalAddress, morphemeTextLength: UInt32, morphemeTextPtr: LogicalAddress, partOfSpeech: UInt32)](https://developer.apple.com/documentation/applicationservices/lamorphemerec/1462691-init)Removed [LaunchParamBlockRec.init(reserved1: UInt32, reserved2: UInt16, launchBlockID: UInt16, launchEPBLength: UInt32, launchFileFlags: UInt16, launchControlFlags: LaunchFlags, launchAppRef: FSRefPtr, launchProcessSN: ProcessSerialNumber, launchPreferredSize: UInt32, launchMinimumSize: UInt32, launchAvailableSize: UInt32, launchAppParameters: AppParametersPtr)](https://developer.apple.com/documentation/applicationservices/launchparamblockrec/1459112-init)Removed [PixMap.init(baseAddr: Ptr, rowBytes: Int16, bounds: Rect, pmVersion: Int16, packType: Int16, packSize: Int32, hRes: Fixed, vRes: Fixed, pixelType: Int16, pixelSize: Int16, cmpCount: Int16, cmpSize: Int16, pixelFormat: OSType, pmTable: CTabHandle, pmExt: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/applicationservices/pixmap/1461182-init)Removed [PixPat.init(patType: Int16, patMap: PixMapHandle, patData: Handle, patXData: Handle, patXValid: Int16, patXMap: Handle, pat1Data: Pattern)](https://developer.apple.com/documentation/applicationservices/pixpat/1460972-init)Removed [ProcessInfoExtendedRec.init(processInfoLength: UInt32, processName: StringPtr, processNumber: ProcessSerialNumber, processType: UInt32, processSignature: OSType, processMode: UInt32, processLocation: Ptr, processSize: UInt32, processFreeMem: UInt32, processLauncher: ProcessSerialNumber, processLaunchDate: UInt32, processActiveTime: UInt32, processAppRef: FSRefPtr, processTempMemTotal: UInt32, processPurgeableTempMemTotal: UInt32)](https://developer.apple.com/documentation/applicationservices/processinfoextendedrec/1462532-init)Removed [ProcessInfoRec.init(processInfoLength: UInt32, processName: StringPtr, processNumber: ProcessSerialNumber, processType: UInt32, processSignature: OSType, processMode: UInt32, processLocation: Ptr, processSize: UInt32, processFreeMem: UInt32, processLauncher: ProcessSerialNumber, processLaunchDate: UInt32, processActiveTime: UInt32, processAppRef: FSRefPtr)](https://developer.apple.com/documentation/applicationservices/processinforec/1463048-init)Removed [VDGammaRecord.init(csGTable: Ptr)](https://developer.apple.com/documentation/applicationservices/vdgammarecord/1464585-init)Removed [kPasteboardClientIsOwner](https://developer.apple.com/documentation/applicationservices/pasteboardsyncflags/kpasteboardclientisowner)Removed [kPasteboardFlavorNoFlags](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavornoflags)Removed [kPasteboardFlavorNotSaved](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavornotsaved)Removed [kPasteboardFlavorPromised](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/1464646-promised)Removed [kPasteboardFlavorRequestOnly](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/1463690-requestonly)Removed [kPasteboardFlavorSenderOnly](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/1462180-senderonly)Removed [kPasteboardFlavorSenderTranslated](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavorsendertranslated)Removed [kPasteboardFlavorSystemTranslated](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavorsystemtranslated)Removed [kPasteboardModified](https://developer.apple.com/documentation/applicationservices/pasteboardsyncflags/1458804-modified)Removed [kPasteboardStandardLocationTrash](https://developer.apple.com/documentation/applicationservices/pasteboardstandardlocation/trash)Removed [kPasteboardStandardLocationUnknown](https://developer.apple.com/documentation/applicationservices/pasteboardstandardlocation/kpasteboardstandardlocationunknown)Removed [PasteboardFlavorFlags](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags)Removed [PasteboardStandardLocation](https://developer.apple.com/documentation/applicationservices/pasteboardstandardlocation)Removed [PasteboardSyncFlags](https://developer.apple.com/documentation/applicationservices/pasteboardsyncflags)Added [ATSFontQuerySourceContext.init(version: UInt32, refCon: UnsafeMutableRawPointer!, retain: CoreFoundation.CFAllocatorRetainCallBack!, release: CoreFoundation.CFAllocatorReleaseCallBack!)](https://developer.apple.com/documentation/applicationservices/atsfontquerysourcecontext/1778162-init)Added [ATSUBackgroundData.init(backgroundUPP: ApplicationServices.RedrawBackgroundUPP!)](https://developer.apple.com/documentation/applicationservices/atsubackgrounddata/1778161-init)Added [ATSUGlyphInfo.init(glyphID: GlyphID, reserved: UInt16, layoutFlags: UInt32, charIndex: UniCharArrayOffset, style: ATSUStyle!, deltaY: Float32, idealX: Float32, screenX: Int16, caretX: Int16)](https://developer.apple.com/documentation/applicationservices/atsuglyphinfo/1690597-init)Added [ATSUGlyphInfoArray.init(layout: ATSUTextLayout!, numGlyphs: Int, glyphs: (ATSUGlyphInfo))](https://developer.apple.com/documentation/applicationservices/atsuglyphinfoarray/1690599-init)Added [ATSULayoutOperationOverrideSpecifier.init(operationSelector: ATSULayoutOperationSelector, overrideUPP: ApplicationServices.ATSUDirectLayoutOperationOverrideUPP!)](https://developer.apple.com/documentation/applicationservices/atsulayoutoperationoverridespecifier/1778160-init)Added [BitMap.init(baseAddr: Ptr!, rowBytes: Int16, bounds: Rect)](https://developer.apple.com/documentation/applicationservices/bitmap/1464073-init)Added [CMDeviceInfo.init(dataVersion: UInt32, deviceClass: CMDeviceClass, deviceID: UInt32, deviceScope: CMDeviceScope, deviceState: UInt32, defaultProfileID: UInt32, deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, profileCount: UInt32, reserved: UInt32)](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo/1461251-init)Added [CQDProcs.init(textProc: ApplicationServices.QDTextUPP!, lineProc: ApplicationServices.QDLineUPP!, rectProc: ApplicationServices.QDRectUPP!, rRectProc: ApplicationServices.QDRRectUPP!, ovalProc: ApplicationServices.QDOvalUPP!, arcProc: ApplicationServices.QDArcUPP!, polyProc: ApplicationServices.QDPolyUPP!, rgnProc: ApplicationServices.QDRgnUPP!, bitsProc: ApplicationServices.QDBitsUPP!, commentProc: ApplicationServices.QDCommentUPP!, txMeasProc: ApplicationServices.QDTxMeasUPP!, getPicProc: ApplicationServices.QDGetPicUPP!, putPicProc: ApplicationServices.QDPutPicUPP!, opcodeProc: ApplicationServices.QDOpcodeUPP!, newProc1: Darwin.UniversalProcPtr!, glyphsProc: ApplicationServices.QDStdGlyphsUPP!, printerStatusProc: ApplicationServices.QDPrinterStatusUPP!, newProc4: Darwin.UniversalProcPtr!, newProc5: Darwin.UniversalProcPtr!, newProc6: Darwin.UniversalProcPtr!)](https://developer.apple.com/documentation/applicationservices/cqdprocs/1778159-init)Added [GDevice.init(gdRefNum: Int16, gdID: Int16, gdType: Int16, gdITable: Handle!, gdResPref: Int16, gdSearchProc: Handle!, gdCompProc: Handle!, gdFlags: Int16, gdPMap: PixMapHandle!, gdRefCon: Int32, gdNextGD: GDHandle!, gdRect: Rect, gdMode: Int32, gdCCBytes: Int16, gdCCDepth: Int16, gdCCXData: Handle!, gdCCXMask: Handle!, gdExt: Handle!)](https://developer.apple.com/documentation/applicationservices/gdevice/1458837-init)Added [HomographDicInfoRec.init(dictionaryID: DCMDictionaryID!, uniqueID: DCMUniqueID)](https://developer.apple.com/documentation/applicationservices/homographdicinforec/1690601-init)Added [LAMorphemeRec.init(sourceTextLength: UInt32, sourceTextPtr: LogicalAddress!, morphemeTextLength: UInt32, morphemeTextPtr: LogicalAddress!, partOfSpeech: UInt32)](https://developer.apple.com/documentation/applicationservices/lamorphemerec/1462691-init)Added [LaunchParamBlockRec.init(reserved1: UInt32, reserved2: UInt16, launchBlockID: UInt16, launchEPBLength: UInt32, launchFileFlags: UInt16, launchControlFlags: LaunchFlags, launchAppRef: FSRefPtr!, launchProcessSN: ProcessSerialNumber, launchPreferredSize: UInt32, launchMinimumSize: UInt32, launchAvailableSize: UInt32, launchAppParameters: AppParametersPtr!)](https://developer.apple.com/documentation/applicationservices/launchparamblockrec/1459112-init)Added [PasteboardFlavorFlags [struct]](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags)Added [PasteboardFlavorFlags.init(rawValue: OptionBits)](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/1644092-init)Added [PasteboardFlavorFlags.notSaved](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/1461870-notsaved)Added [PasteboardFlavorFlags.promised](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavorpromised)Added [PasteboardFlavorFlags.requestOnly](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavorrequestonly)Added [PasteboardFlavorFlags.senderOnly](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavorsenderonly)Added [PasteboardFlavorFlags.senderTranslated](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavorsendertranslated)Added [PasteboardFlavorFlags.systemTranslated](https://developer.apple.com/documentation/applicationservices/pasteboardflavorflags/kpasteboardflavorsystemtranslated)Added [PasteboardStandardLocation [enum]](https://developer.apple.com/documentation/applicationservices/pasteboardstandardlocation)Added [PasteboardStandardLocation.trash](https://developer.apple.com/documentation/applicationservices/pasteboardstandardlocation/kpasteboardstandardlocationtrash)Added [PasteboardStandardLocation.unknown](https://developer.apple.com/documentation/applicationservices/pasteboardstandardlocation/unknown)Added [PasteboardSyncFlags [struct]](https://developer.apple.com/documentation/applicationservices/pasteboardsyncflags)Added [PasteboardSyncFlags.clientIsOwner](https://developer.apple.com/documentation/applicationservices/pasteboardsyncflags/kpasteboardclientisowner)Added [PasteboardSyncFlags.init(rawValue: OptionBits)](https://developer.apple.com/documentation/applicationservices/pasteboardsyncflags/1644060-init)Added [PasteboardSyncFlags.modified](https://developer.apple.com/documentation/applicationservices/pasteboardsyncflags/kpasteboardmodified)Added [PixMap.init(baseAddr: Ptr!, rowBytes: Int16, bounds: Rect, pmVersion: Int16, packType: Int16, packSize: Int32, hRes: Fixed, vRes: Fixed, pixelType: Int16, pixelSize: Int16, cmpCount: Int16, cmpSize: Int16, pixelFormat: OSType, pmTable: CTabHandle!, pmExt: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/applicationservices/pixmap/1461182-init)Added [PixPat.init(patType: Int16, patMap: PixMapHandle!, patData: Handle!, patXData: Handle!, patXValid: Int16, patXMap: Handle!, pat1Data: Pattern)](https://developer.apple.com/documentation/applicationservices/pixpat/1460972-init)Added [ProcessInfoExtendedRec.init(processInfoLength: UInt32, processName: StringPtr!, processNumber: ProcessSerialNumber, processType: UInt32, processSignature: OSType, processMode: UInt32, processLocation: Ptr!, processSize: UInt32, processFreeMem: UInt32, processLauncher: ProcessSerialNumber, processLaunchDate: UInt32, processActiveTime: UInt32, processAppRef: FSRefPtr!, processTempMemTotal: UInt32, processPurgeableTempMemTotal: UInt32)](https://developer.apple.com/documentation/applicationservices/processinfoextendedrec/1462532-init)Added [ProcessInfoRec.init(processInfoLength: UInt32, processName: StringPtr!, processNumber: ProcessSerialNumber, processType: UInt32, processSignature: OSType, processMode: UInt32, processLocation: Ptr!, processSize: UInt32, processFreeMem: UInt32, processLauncher: ProcessSerialNumber, processLaunchDate: UInt32, processActiveTime: UInt32, processAppRef: FSRefPtr!)](https://developer.apple.com/documentation/applicationservices/processinforec/1463048-init)Added [VDGammaRecord.init(csGTable: Ptr!)](https://developer.apple.com/documentation/applicationservices/vdgammarecord/1464585-init)Added [kATSUCenterAlignment](https://developer.apple.com/documentation/applicationservices/katsucenteralignment)Added [kATSUEndAlignment](https://developer.apple.com/documentation/applicationservices/katsuendalignment)Added [kATSUFullJustification](https://developer.apple.com/documentation/applicationservices/katsufulljustification)Added [kATSUNoJustification](https://developer.apple.com/documentation/applicationservices/katsunojustification)Added [kATSUStartAlignment](https://developer.apple.com/documentation/applicationservices/katsustartalignment)Added kColorSyncConvertUseExtendedRangeModified [ATSFontFilter [struct]](https://developer.apple.com/documentation/applicationservices/atsfontfilter)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFontFilter {     struct __Unnamed_union_filter {         var generationFilter: ATSGeneration         var fontFamilyFilter: ATSFontFamilyRef         var fontFamilyApplierFunctionFilter: ATSFontFamilyApplierFunction!         var fontApplierFunctionFilter: ATSFontApplierFunction!         var fontFileRefFilter: UnsafePointer<FSRef>         init(generationFilter generationFilter: ATSGeneration)         init(fontFamilyFilter fontFamilyFilter: ATSFontFamilyRef)         init(fontFamilyApplierFunctionFilter fontFamilyApplierFunctionFilter: ATSFontFamilyApplierFunction!)         init(fontApplierFunctionFilter fontApplierFunctionFilter: ATSFontApplierFunction!)         init(fontFileRefFilter fontFileRefFilter: UnsafePointer<FSRef>)         init()     }     var version: UInt32     var filterSelector: ATSFontFilterSelector     var filter: ATSFontFilter.__Unnamed_union_filter     init()     init(version version: UInt32, filterSelector filterSelector: ATSFontFilterSelector, filter filter: ATSFontFilter.__Unnamed_union_filter) } ``` |
| To | ``` struct ATSFontFilter {     struct __Unnamed_union_filter {         var generationFilter: ATSGeneration         var fontFamilyFilter: ATSFontFamilyRef         var fontFamilyApplierFunctionFilter: ApplicationServices.ATSFontFamilyApplierFunction!         var fontApplierFunctionFilter: ApplicationServices.ATSFontApplierFunction!         var fontFileRefFilter: UnsafePointer<FSRef>!         init(generationFilter generationFilter: ATSGeneration)         init(fontFamilyFilter fontFamilyFilter: ATSFontFamilyRef)         init(fontFamilyApplierFunctionFilter fontFamilyApplierFunctionFilter: ApplicationServices.ATSFontFamilyApplierFunction!)         init(fontApplierFunctionFilter fontApplierFunctionFilter: ApplicationServices.ATSFontApplierFunction!)         init(fontFileRefFilter fontFileRefFilter: UnsafePointer<FSRef>!)         init()     }     var version: UInt32     var filterSelector: ATSFontFilterSelector     var filter: ATSFontFilter.__Unnamed_union_filter     init()     init(version version: UInt32, filterSelector filterSelector: ATSFontFilterSelector, filter filter: ATSFontFilter.__Unnamed_union_filter) } ``` |

Modified [ATSFontQuerySourceContext [struct]](https://developer.apple.com/documentation/applicationservices/atsfontquerysourcecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFontQuerySourceContext {     var version: UInt32     var refCon: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack!     var release: CFAllocatorReleaseCallBack!     init()     init(version version: UInt32, refCon refCon: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack!, release release: CFAllocatorReleaseCallBack!) } ``` |
| To | ``` struct ATSFontQuerySourceContext {     var version: UInt32     var refCon: UnsafeMutableRawPointer!     var retain: CoreFoundation.CFAllocatorRetainCallBack!     var release: CoreFoundation.CFAllocatorReleaseCallBack!     init()     init(version version: UInt32, refCon refCon: UnsafeMutableRawPointer!, retain retain: CoreFoundation.CFAllocatorRetainCallBack!, release release: CoreFoundation.CFAllocatorReleaseCallBack!) } ``` |

Modified [ATSFontQuerySourceContext.refCon](https://developer.apple.com/documentation/applicationservices/atsfontquerysourcecontext/1461013-refcon)

|  | Declaration |
| --- | --- |
| From | ``` var refCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var refCon: UnsafeMutableRawPointer! ``` |

Modified [ATSFontQuerySourceContext.release](https://developer.apple.com/documentation/applicationservices/atsfontquerysourcecontext/1460736-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack! ``` |
| To | ``` var release: CoreFoundation.CFAllocatorReleaseCallBack! ``` |

Modified [ATSFontQuerySourceContext.retain](https://developer.apple.com/documentation/applicationservices/atsfontquerysourcecontext/1463355-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack! ``` |
| To | ``` var retain: CoreFoundation.CFAllocatorRetainCallBack! ``` |

Modified [ATSFSSpec [struct]](https://developer.apple.com/documentation/applicationservices/atsfsspec)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFSSpec {     var vRefNum: FSVolumeRefNum     var parID: Int32     var name: StrFileName     init()     init(vRefNum vRefNum: FSVolumeRefNum, parID parID: Int32, name name: StrFileName) } ``` |
| To | ``` struct ATSFSSpec {     var vRefNum: FSVolumeRefNum     var parID: Int32     var name: Darwin.StrFileName     init()     init(vRefNum vRefNum: FSVolumeRefNum, parID parID: Int32, name name: Darwin.StrFileName) } ``` |

Modified [ATSFSSpec.init(vRefNum: FSVolumeRefNum, parID: Int32, name: Darwin.StrFileName)](https://developer.apple.com/documentation/applicationservices/atsfsspec/1463783-init)

|  | Declaration |
| --- | --- |
| From | ``` init(vRefNum vRefNum: FSVolumeRefNum, parID parID: Int32, name name: StrFileName) ``` |
| To | ``` init(vRefNum vRefNum: FSVolumeRefNum, parID parID: Int32, name name: Darwin.StrFileName) ``` |

Modified [ATSFSSpec.name](https://developer.apple.com/documentation/applicationservices/atsfsspec/1460126-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: StrFileName ``` |
| To | ``` var name: Darwin.StrFileName ``` |

Modified [ATSUBackgroundData [struct]](https://developer.apple.com/documentation/applicationservices/1452350-atsubackgrounddata)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUBackgroundData {     var backgroundColor: ATSUBackgroundColor     var backgroundUPP: RedrawBackgroundUPP!     init(backgroundColor backgroundColor: ATSUBackgroundColor)     init(backgroundUPP backgroundUPP: RedrawBackgroundUPP!)     init() } ``` |
| To | ``` struct ATSUBackgroundData {     var backgroundColor: ATSUBackgroundColor     var backgroundUPP: ApplicationServices.RedrawBackgroundUPP!     init(backgroundColor backgroundColor: ATSUBackgroundColor)     init(backgroundUPP backgroundUPP: ApplicationServices.RedrawBackgroundUPP!)     init() } ``` |

Modified [ATSUBackgroundData.backgroundUPP](https://developer.apple.com/documentation/applicationservices/1452350-atsubackgrounddata/1452266-backgroundupp)

|  | Declaration |
| --- | --- |
| From | ``` var backgroundUPP: RedrawBackgroundUPP! ``` |
| To | ``` var backgroundUPP: ApplicationServices.RedrawBackgroundUPP! ``` |

Modified [ATSUGlyphInfo [struct]](https://developer.apple.com/documentation/applicationservices/atsuglyphinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUGlyphInfo {     var glyphID: GlyphID     var reserved: UInt16     var layoutFlags: UInt32     var charIndex: UniCharArrayOffset     var style: ATSUStyle     var deltaY: Float32     var idealX: Float32     var screenX: Int16     var caretX: Int16     init()     init(glyphID glyphID: GlyphID, reserved reserved: UInt16, layoutFlags layoutFlags: UInt32, charIndex charIndex: UniCharArrayOffset, style style: ATSUStyle, deltaY deltaY: Float32, idealX idealX: Float32, screenX screenX: Int16, caretX caretX: Int16) } ``` |
| To | ``` struct ATSUGlyphInfo {     var glyphID: GlyphID     var reserved: UInt16     var layoutFlags: UInt32     var charIndex: UniCharArrayOffset     var style: ATSUStyle!     var deltaY: Float32     var idealX: Float32     var screenX: Int16     var caretX: Int16     init()     init(glyphID glyphID: GlyphID, reserved reserved: UInt16, layoutFlags layoutFlags: UInt32, charIndex charIndex: UniCharArrayOffset, style style: ATSUStyle!, deltaY deltaY: Float32, idealX idealX: Float32, screenX screenX: Int16, caretX caretX: Int16) } ``` |

Modified [ATSUGlyphInfo.style](https://developer.apple.com/documentation/applicationservices/atsuglyphinfo/1452143-style)

|  | Declaration |
| --- | --- |
| From | ``` var style: ATSUStyle ``` |
| To | ``` var style: ATSUStyle! ``` |

Modified [ATSUGlyphInfoArray [struct]](https://developer.apple.com/documentation/applicationservices/atsuglyphinfoarray)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUGlyphInfoArray {     var layout: ATSUTextLayout     var numGlyphs: Int     var glyphs: (ATSUGlyphInfo)     init()     init(layout layout: ATSUTextLayout, numGlyphs numGlyphs: Int, glyphs glyphs: (ATSUGlyphInfo)) } ``` |
| To | ``` struct ATSUGlyphInfoArray {     var layout: ATSUTextLayout!     var numGlyphs: Int     var glyphs: (ATSUGlyphInfo)     init()     init(layout layout: ATSUTextLayout!, numGlyphs numGlyphs: Int, glyphs glyphs: (ATSUGlyphInfo)) } ``` |

Modified [ATSUGlyphInfoArray.layout](https://developer.apple.com/documentation/applicationservices/atsuglyphinfoarray/1452037-layout)

|  | Declaration |
| --- | --- |
| From | ``` var layout: ATSUTextLayout ``` |
| To | ``` var layout: ATSUTextLayout! ``` |

Modified [ATSULayoutOperationOverrideSpecifier [struct]](https://developer.apple.com/documentation/applicationservices/atsulayoutoperationoverridespecifier)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSULayoutOperationOverrideSpecifier {     var operationSelector: ATSULayoutOperationSelector     var overrideUPP: ATSUDirectLayoutOperationOverrideUPP!     init()     init(operationSelector operationSelector: ATSULayoutOperationSelector, overrideUPP overrideUPP: ATSUDirectLayoutOperationOverrideUPP!) } ``` |
| To | ``` struct ATSULayoutOperationOverrideSpecifier {     var operationSelector: ATSULayoutOperationSelector     var overrideUPP: ApplicationServices.ATSUDirectLayoutOperationOverrideUPP!     init()     init(operationSelector operationSelector: ATSULayoutOperationSelector, overrideUPP overrideUPP: ApplicationServices.ATSUDirectLayoutOperationOverrideUPP!) } ``` |

Modified [ATSULayoutOperationOverrideSpecifier.overrideUPP](https://developer.apple.com/documentation/applicationservices/atsulayoutoperationoverridespecifier/1463665-overrideupp)

|  | Declaration |
| --- | --- |
| From | ``` var overrideUPP: ATSUDirectLayoutOperationOverrideUPP! ``` |
| To | ``` var overrideUPP: ApplicationServices.ATSUDirectLayoutOperationOverrideUPP! ``` |

Modified [AXCopyMultipleAttributeOptions [struct]](https://developer.apple.com/documentation/applicationservices/axcopymultipleattributeoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AXCopyMultipleAttributeOptions : OptionSetType {     init(rawValue rawValue: UInt32)     static var StopOnError: AXCopyMultipleAttributeOptions { get } } ``` | OptionSetType |
| To | ``` struct AXCopyMultipleAttributeOptions : OptionSet {     init(rawValue rawValue: UInt32)     static var stopOnError: AXCopyMultipleAttributeOptions { get }     func intersect(_ other: AXCopyMultipleAttributeOptions) -> AXCopyMultipleAttributeOptions     func exclusiveOr(_ other: AXCopyMultipleAttributeOptions) -> AXCopyMultipleAttributeOptions     mutating func unionInPlace(_ other: AXCopyMultipleAttributeOptions)     mutating func intersectInPlace(_ other: AXCopyMultipleAttributeOptions)     mutating func exclusiveOrInPlace(_ other: AXCopyMultipleAttributeOptions)     func isSubsetOf(_ other: AXCopyMultipleAttributeOptions) -> Bool     func isDisjointWith(_ other: AXCopyMultipleAttributeOptions) -> Bool     func isSupersetOf(_ other: AXCopyMultipleAttributeOptions) -> Bool     mutating func subtractInPlace(_ other: AXCopyMultipleAttributeOptions)     func isStrictSupersetOf(_ other: AXCopyMultipleAttributeOptions) -> Bool     func isStrictSubsetOf(_ other: AXCopyMultipleAttributeOptions) -> Bool } extension AXCopyMultipleAttributeOptions {     func union(_ other: AXCopyMultipleAttributeOptions) -> AXCopyMultipleAttributeOptions     func intersection(_ other: AXCopyMultipleAttributeOptions) -> AXCopyMultipleAttributeOptions     func symmetricDifference(_ other: AXCopyMultipleAttributeOptions) -> AXCopyMultipleAttributeOptions } extension AXCopyMultipleAttributeOptions {     func contains(_ member: AXCopyMultipleAttributeOptions) -> Bool     mutating func insert(_ newMember: AXCopyMultipleAttributeOptions) -> (inserted: Bool, memberAfterInsert: AXCopyMultipleAttributeOptions)     mutating func remove(_ member: AXCopyMultipleAttributeOptions) -> AXCopyMultipleAttributeOptions?     mutating func update(with newMember: AXCopyMultipleAttributeOptions) -> AXCopyMultipleAttributeOptions? } extension AXCopyMultipleAttributeOptions {     convenience init()     mutating func formUnion(_ other: AXCopyMultipleAttributeOptions)     mutating func formIntersection(_ other: AXCopyMultipleAttributeOptions)     mutating func formSymmetricDifference(_ other: AXCopyMultipleAttributeOptions) } extension AXCopyMultipleAttributeOptions {     convenience init<S : Sequence where S.Iterator.Element == AXCopyMultipleAttributeOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AXCopyMultipleAttributeOptions...)     mutating func subtract(_ other: AXCopyMultipleAttributeOptions)     func isSubset(of other: AXCopyMultipleAttributeOptions) -> Bool     func isSuperset(of other: AXCopyMultipleAttributeOptions) -> Bool     func isDisjoint(with other: AXCopyMultipleAttributeOptions) -> Bool     func subtracting(_ other: AXCopyMultipleAttributeOptions) -> AXCopyMultipleAttributeOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AXCopyMultipleAttributeOptions) -> Bool     func isStrictSubset(of other: AXCopyMultipleAttributeOptions) -> Bool } ``` | OptionSet |

Modified [AXCopyMultipleAttributeOptions.stopOnError](https://developer.apple.com/documentation/applicationservices/axcopymultipleattributeoptions/1460788-stoponerror)

|  | Declaration |
| --- | --- |
| From | ``` static var StopOnError: AXCopyMultipleAttributeOptions { get } ``` |
| To | ``` static var stopOnError: AXCopyMultipleAttributeOptions { get } ``` |

Modified [AXError [enum]](https://developer.apple.com/documentation/applicationservices/axerror)

|  | Declaration |
| --- | --- |
| From | ``` enum AXError : Int32 {     case Success     case Failure     case IllegalArgument     case InvalidUIElement     case InvalidUIElementObserver     case CannotComplete     case AttributeUnsupported     case ActionUnsupported     case NotificationUnsupported     case NotImplemented     case NotificationAlreadyRegistered     case NotificationNotRegistered     case APIDisabled     case NoValue     case ParameterizedAttributeUnsupported     case NotEnoughPrecision } ``` |
| To | ``` enum AXError : Int32 {     case success     case failure     case illegalArgument     case invalidUIElement     case invalidUIElementObserver     case cannotComplete     case attributeUnsupported     case actionUnsupported     case notificationUnsupported     case notImplemented     case notificationAlreadyRegistered     case notificationNotRegistered     case apiDisabled     case noValue     case parameterizedAttributeUnsupported     case notEnoughPrecision } ``` |

Modified [AXError.actionUnsupported](https://developer.apple.com/documentation/applicationservices/axerror/kaxerroractionunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case ActionUnsupported ``` |
| To | ``` case actionUnsupported ``` |

Modified [AXError.apiDisabled](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorapidisabled)

|  | Declaration |
| --- | --- |
| From | ``` case APIDisabled ``` |
| To | ``` case apiDisabled ``` |

Modified [AXError.attributeUnsupported](https://developer.apple.com/documentation/applicationservices/axerror/attributeunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case AttributeUnsupported ``` |
| To | ``` case attributeUnsupported ``` |

Modified [AXError.cannotComplete](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorcannotcomplete)

|  | Declaration |
| --- | --- |
| From | ``` case CannotComplete ``` |
| To | ``` case cannotComplete ``` |

Modified [AXError.failure](https://developer.apple.com/documentation/applicationservices/axerror/failure)

|  | Declaration |
| --- | --- |
| From | ``` case Failure ``` |
| To | ``` case failure ``` |

Modified [AXError.illegalArgument](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorillegalargument)

|  | Declaration |
| --- | --- |
| From | ``` case IllegalArgument ``` |
| To | ``` case illegalArgument ``` |

Modified [AXError.invalidUIElement](https://developer.apple.com/documentation/applicationservices/axerror/invaliduielement)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidUIElement ``` |
| To | ``` case invalidUIElement ``` |

Modified [AXError.invalidUIElementObserver](https://developer.apple.com/documentation/applicationservices/axerror/invaliduielementobserver)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidUIElementObserver ``` |
| To | ``` case invalidUIElementObserver ``` |

Modified [AXError.notEnoughPrecision](https://developer.apple.com/documentation/applicationservices/axerror/notenoughprecision)

|  | Declaration |
| --- | --- |
| From | ``` case NotEnoughPrecision ``` |
| To | ``` case notEnoughPrecision ``` |

Modified [AXError.notificationAlreadyRegistered](https://developer.apple.com/documentation/applicationservices/axerror/notificationalreadyregistered)

|  | Declaration |
| --- | --- |
| From | ``` case NotificationAlreadyRegistered ``` |
| To | ``` case notificationAlreadyRegistered ``` |

Modified [AXError.notificationNotRegistered](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrornotificationnotregistered)

|  | Declaration |
| --- | --- |
| From | ``` case NotificationNotRegistered ``` |
| To | ``` case notificationNotRegistered ``` |

Modified [AXError.notificationUnsupported](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrornotificationunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case NotificationUnsupported ``` |
| To | ``` case notificationUnsupported ``` |

Modified [AXError.notImplemented](https://developer.apple.com/documentation/applicationservices/axerror/notimplemented)

|  | Declaration |
| --- | --- |
| From | ``` case NotImplemented ``` |
| To | ``` case notImplemented ``` |

Modified [AXError.noValue](https://developer.apple.com/documentation/applicationservices/axerror/novalue)

|  | Declaration |
| --- | --- |
| From | ``` case NoValue ``` |
| To | ``` case noValue ``` |

Modified [AXError.parameterizedAttributeUnsupported](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorparameterizedattributeunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case ParameterizedAttributeUnsupported ``` |
| To | ``` case parameterizedAttributeUnsupported ``` |

Modified [AXError.success](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorsuccess)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [AXMenuItemModifiers [struct]](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AXMenuItemModifiers : OptionSetType {     init(rawValue rawValue: UInt32)     static var None: AXMenuItemModifiers { get }     static var Shift: AXMenuItemModifiers { get }     static var Option: AXMenuItemModifiers { get }     static var Control: AXMenuItemModifiers { get }     static var NoCommand: AXMenuItemModifiers { get } } ``` | OptionSetType |
| To | ``` struct AXMenuItemModifiers : OptionSet {     init(rawValue rawValue: UInt32)     static var none: AXMenuItemModifiers { get }     static var shift: AXMenuItemModifiers { get }     static var option: AXMenuItemModifiers { get }     static var control: AXMenuItemModifiers { get }     static var noCommand: AXMenuItemModifiers { get }     func intersect(_ other: AXMenuItemModifiers) -> AXMenuItemModifiers     func exclusiveOr(_ other: AXMenuItemModifiers) -> AXMenuItemModifiers     mutating func unionInPlace(_ other: AXMenuItemModifiers)     mutating func intersectInPlace(_ other: AXMenuItemModifiers)     mutating func exclusiveOrInPlace(_ other: AXMenuItemModifiers)     func isSubsetOf(_ other: AXMenuItemModifiers) -> Bool     func isDisjointWith(_ other: AXMenuItemModifiers) -> Bool     func isSupersetOf(_ other: AXMenuItemModifiers) -> Bool     mutating func subtractInPlace(_ other: AXMenuItemModifiers)     func isStrictSupersetOf(_ other: AXMenuItemModifiers) -> Bool     func isStrictSubsetOf(_ other: AXMenuItemModifiers) -> Bool } extension AXMenuItemModifiers {     func union(_ other: AXMenuItemModifiers) -> AXMenuItemModifiers     func intersection(_ other: AXMenuItemModifiers) -> AXMenuItemModifiers     func symmetricDifference(_ other: AXMenuItemModifiers) -> AXMenuItemModifiers } extension AXMenuItemModifiers {     func contains(_ member: AXMenuItemModifiers) -> Bool     mutating func insert(_ newMember: AXMenuItemModifiers) -> (inserted: Bool, memberAfterInsert: AXMenuItemModifiers)     mutating func remove(_ member: AXMenuItemModifiers) -> AXMenuItemModifiers?     mutating func update(with newMember: AXMenuItemModifiers) -> AXMenuItemModifiers? } extension AXMenuItemModifiers {     convenience init()     mutating func formUnion(_ other: AXMenuItemModifiers)     mutating func formIntersection(_ other: AXMenuItemModifiers)     mutating func formSymmetricDifference(_ other: AXMenuItemModifiers) } extension AXMenuItemModifiers {     convenience init<S : Sequence where S.Iterator.Element == AXMenuItemModifiers>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AXMenuItemModifiers...)     mutating func subtract(_ other: AXMenuItemModifiers)     func isSubset(of other: AXMenuItemModifiers) -> Bool     func isSuperset(of other: AXMenuItemModifiers) -> Bool     func isDisjoint(with other: AXMenuItemModifiers) -> Bool     func subtracting(_ other: AXMenuItemModifiers) -> AXMenuItemModifiers     var isEmpty: Bool { get }     func isStrictSuperset(of other: AXMenuItemModifiers) -> Bool     func isStrictSubset(of other: AXMenuItemModifiers) -> Bool } ``` | OptionSet |

Modified [AXMenuItemModifiers.control](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/1464333-control)

|  | Declaration |
| --- | --- |
| From | ``` static var Control: AXMenuItemModifiers { get } ``` |
| To | ``` static var control: AXMenuItemModifiers { get } ``` |

Modified [AXMenuItemModifiers.noCommand](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifiernocommand)

|  | Declaration |
| --- | --- |
| From | ``` static var NoCommand: AXMenuItemModifiers { get } ``` |
| To | ``` static var noCommand: AXMenuItemModifiers { get } ``` |

Modified [AXMenuItemModifiers.option](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifieroption)

|  | Declaration |
| --- | --- |
| From | ``` static var Option: AXMenuItemModifiers { get } ``` |
| To | ``` static var option: AXMenuItemModifiers { get } ``` |

Modified [AXMenuItemModifiers.shift](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifiershift)

|  | Declaration |
| --- | --- |
| From | ``` static var Shift: AXMenuItemModifiers { get } ``` |
| To | ``` static var shift: AXMenuItemModifiers { get } ``` |

Modified [AXPriority [enum]](https://developer.apple.com/documentation/applicationservices/axpriority)

|  | Declaration |
| --- | --- |
| From | ``` enum AXPriority : CFIndex {     case Low     case Medium     case High } ``` |
| To | ``` enum AXPriority : CFIndex {     case low     case medium     case high } ``` |

Modified [AXPriority.high](https://developer.apple.com/documentation/applicationservices/axpriority/kaxpriorityhigh)

|  | Declaration |
| --- | --- |
| From | ``` case High ``` |
| To | ``` case high ``` |

Modified [AXPriority.low](https://developer.apple.com/documentation/applicationservices/axpriority/low)

|  | Declaration |
| --- | --- |
| From | ``` case Low ``` |
| To | ``` case low ``` |

Modified [AXPriority.medium](https://developer.apple.com/documentation/applicationservices/axpriority/medium)

|  | Declaration |
| --- | --- |
| From | ``` case Medium ``` |
| To | ``` case medium ``` |

Modified [AXUnderlineStyle [enum]](https://developer.apple.com/documentation/applicationservices/axunderlinestyle)

|  | Declaration |
| --- | --- |
| From | ``` enum AXUnderlineStyle : UInt32 {     case None     case Single     case Thick     case Double } ``` |
| To | ``` enum AXUnderlineStyle : UInt32 {     case none     case single     case thick     case double } ``` |

Modified [AXUnderlineStyle.double](https://developer.apple.com/documentation/applicationservices/axunderlinestyle/kaxunderlinestyledouble)

|  | Declaration |
| --- | --- |
| From | ``` case Double ``` |
| To | ``` case double ``` |

Modified [AXUnderlineStyle.none](https://developer.apple.com/documentation/applicationservices/axunderlinestyle/kaxunderlinestylenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [AXUnderlineStyle.single](https://developer.apple.com/documentation/applicationservices/axunderlinestyle/kaxunderlinestylesingle)

|  | Declaration |
| --- | --- |
| From | ``` case Single ``` |
| To | ``` case single ``` |

Modified [AXUnderlineStyle.thick](https://developer.apple.com/documentation/applicationservices/axunderlinestyle/thick)

|  | Declaration |
| --- | --- |
| From | ``` case Thick ``` |
| To | ``` case thick ``` |

Modified [AXValueType [enum]](https://developer.apple.com/documentation/applicationservices/axvaluetype)

|  | Declaration |
| --- | --- |
| From | ``` enum AXValueType : UInt32 {     case CGPoint     case CGSize     case CGRect     case CFRange     case AXError     case Illegal } ``` |
| To | ``` enum AXValueType : UInt32 {     case cgPoint     case cgSize     case cgRect     case cfRange     case axError     case illegal } ``` |

Modified [AXValueType.axError](https://developer.apple.com/documentation/applicationservices/axvaluetype/axerror)

|  | Declaration |
| --- | --- |
| From | ``` case AXError ``` |
| To | ``` case axError ``` |

Modified [AXValueType.cfRange](https://developer.apple.com/documentation/applicationservices/axvaluetype/cfrange)

|  | Declaration |
| --- | --- |
| From | ``` case CFRange ``` |
| To | ``` case cfRange ``` |

Modified [AXValueType.cgPoint](https://developer.apple.com/documentation/applicationservices/axvaluetype/cgpoint)

|  | Declaration |
| --- | --- |
| From | ``` case CGPoint ``` |
| To | ``` case cgPoint ``` |

Modified [AXValueType.cgRect](https://developer.apple.com/documentation/applicationservices/axvaluetype/cgrect)

|  | Declaration |
| --- | --- |
| From | ``` case CGRect ``` |
| To | ``` case cgRect ``` |

Modified [AXValueType.cgSize](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvaluetypecgsize)

|  | Declaration |
| --- | --- |
| From | ``` case CGSize ``` |
| To | ``` case cgSize ``` |

Modified [AXValueType.illegal](https://developer.apple.com/documentation/applicationservices/axvaluetype/illegal)

|  | Declaration |
| --- | --- |
| From | ``` case Illegal ``` |
| To | ``` case illegal ``` |

Modified [BitMap [struct]](https://developer.apple.com/documentation/applicationservices/bitmap)

|  | Declaration |
| --- | --- |
| From | ``` struct BitMap {     var baseAddr: Ptr     var rowBytes: Int16     var bounds: Rect     init()     init(baseAddr baseAddr: Ptr, rowBytes rowBytes: Int16, bounds bounds: Rect) } ``` |
| To | ``` struct BitMap {     var baseAddr: Ptr!     var rowBytes: Int16     var bounds: Rect     init()     init(baseAddr baseAddr: Ptr!, rowBytes rowBytes: Int16, bounds bounds: Rect) } ``` |

Modified [BitMap.baseAddr](https://developer.apple.com/documentation/applicationservices/bitmap/1459306-baseaddr)

|  | Declaration |
| --- | --- |
| From | ``` var baseAddr: Ptr ``` |
| To | ``` var baseAddr: Ptr! ``` |

Modified [CMDeviceInfo [struct]](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct CMDeviceInfo {     var dataVersion: UInt32     var deviceClass: CMDeviceClass     var deviceID: CMDeviceID     var deviceScope: CMDeviceScope     var deviceState: CMDeviceState     var defaultProfileID: CMDeviceProfileID     var deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>     var profileCount: UInt32     var reserved: UInt32     init()     init(dataVersion dataVersion: UInt32, deviceClass deviceClass: CMDeviceClass, deviceID deviceID: CMDeviceID, deviceScope deviceScope: CMDeviceScope, deviceState deviceState: CMDeviceState, defaultProfileID defaultProfileID: CMDeviceProfileID, deviceName deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, profileCount profileCount: UInt32, reserved reserved: UInt32) } ``` |
| To | ``` struct CMDeviceInfo {     var dataVersion: UInt32     var deviceClass: CMDeviceClass     var deviceID: UInt32     var deviceScope: CMDeviceScope     var deviceState: UInt32     var defaultProfileID: UInt32     var deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!     var profileCount: UInt32     var reserved: UInt32     init()     init(dataVersion dataVersion: UInt32, deviceClass deviceClass: CMDeviceClass, deviceID deviceID: UInt32, deviceScope deviceScope: CMDeviceScope, deviceState deviceState: UInt32, defaultProfileID defaultProfileID: UInt32, deviceName deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, profileCount profileCount: UInt32, reserved reserved: UInt32) } ``` |

Modified [CMDeviceInfo.defaultProfileID](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo/1461755-defaultprofileid)

|  | Declaration |
| --- | --- |
| From | ``` var defaultProfileID: CMDeviceProfileID ``` |
| To | ``` var defaultProfileID: UInt32 ``` |

Modified [CMDeviceInfo.deviceID](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo/1458888-deviceid)

|  | Declaration |
| --- | --- |
| From | ``` var deviceID: CMDeviceID ``` |
| To | ``` var deviceID: UInt32 ``` |

Modified [CMDeviceInfo.deviceName](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo/1460441-devicename)

|  | Declaration |
| --- | --- |
| From | ``` var deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?> ``` |
| To | ``` var deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>! ``` |

Modified [CMDeviceInfo.deviceState](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo/1460889-devicestate)

|  | Declaration |
| --- | --- |
| From | ``` var deviceState: CMDeviceState ``` |
| To | ``` var deviceState: UInt32 ``` |

Modified [CQDProcs [struct]](https://developer.apple.com/documentation/applicationservices/cqdprocs)

|  | Declaration |
| --- | --- |
| From | ``` struct CQDProcs {     var textProc: QDTextUPP!     var lineProc: QDLineUPP!     var rectProc: QDRectUPP!     var rRectProc: QDRRectUPP!     var ovalProc: QDOvalUPP!     var arcProc: QDArcUPP!     var polyProc: QDPolyUPP!     var rgnProc: QDRgnUPP!     var bitsProc: QDBitsUPP!     var commentProc: QDCommentUPP!     var txMeasProc: QDTxMeasUPP!     var getPicProc: QDGetPicUPP!     var putPicProc: QDPutPicUPP!     var opcodeProc: QDOpcodeUPP!     var newProc1: UniversalProcPtr!     var glyphsProc: QDStdGlyphsUPP!     var printerStatusProc: QDPrinterStatusUPP!     var newProc4: UniversalProcPtr!     var newProc5: UniversalProcPtr!     var newProc6: UniversalProcPtr!     init()     init(textProc textProc: QDTextUPP!, lineProc lineProc: QDLineUPP!, rectProc rectProc: QDRectUPP!, rRectProc rRectProc: QDRRectUPP!, ovalProc ovalProc: QDOvalUPP!, arcProc arcProc: QDArcUPP!, polyProc polyProc: QDPolyUPP!, rgnProc rgnProc: QDRgnUPP!, bitsProc bitsProc: QDBitsUPP!, commentProc commentProc: QDCommentUPP!, txMeasProc txMeasProc: QDTxMeasUPP!, getPicProc getPicProc: QDGetPicUPP!, putPicProc putPicProc: QDPutPicUPP!, opcodeProc opcodeProc: QDOpcodeUPP!, newProc1 newProc1: UniversalProcPtr!, glyphsProc glyphsProc: QDStdGlyphsUPP!, printerStatusProc printerStatusProc: QDPrinterStatusUPP!, newProc4 newProc4: UniversalProcPtr!, newProc5 newProc5: UniversalProcPtr!, newProc6 newProc6: UniversalProcPtr!) } ``` |
| To | ``` struct CQDProcs {     var textProc: ApplicationServices.QDTextUPP!     var lineProc: ApplicationServices.QDLineUPP!     var rectProc: ApplicationServices.QDRectUPP!     var rRectProc: ApplicationServices.QDRRectUPP!     var ovalProc: ApplicationServices.QDOvalUPP!     var arcProc: ApplicationServices.QDArcUPP!     var polyProc: ApplicationServices.QDPolyUPP!     var rgnProc: ApplicationServices.QDRgnUPP!     var bitsProc: ApplicationServices.QDBitsUPP!     var commentProc: ApplicationServices.QDCommentUPP!     var txMeasProc: ApplicationServices.QDTxMeasUPP!     var getPicProc: ApplicationServices.QDGetPicUPP!     var putPicProc: ApplicationServices.QDPutPicUPP!     var opcodeProc: ApplicationServices.QDOpcodeUPP!     var newProc1: Darwin.UniversalProcPtr!     var glyphsProc: ApplicationServices.QDStdGlyphsUPP!     var printerStatusProc: ApplicationServices.QDPrinterStatusUPP!     var newProc4: Darwin.UniversalProcPtr!     var newProc5: Darwin.UniversalProcPtr!     var newProc6: Darwin.UniversalProcPtr!     init()     init(textProc textProc: ApplicationServices.QDTextUPP!, lineProc lineProc: ApplicationServices.QDLineUPP!, rectProc rectProc: ApplicationServices.QDRectUPP!, rRectProc rRectProc: ApplicationServices.QDRRectUPP!, ovalProc ovalProc: ApplicationServices.QDOvalUPP!, arcProc arcProc: ApplicationServices.QDArcUPP!, polyProc polyProc: ApplicationServices.QDPolyUPP!, rgnProc rgnProc: ApplicationServices.QDRgnUPP!, bitsProc bitsProc: ApplicationServices.QDBitsUPP!, commentProc commentProc: ApplicationServices.QDCommentUPP!, txMeasProc txMeasProc: ApplicationServices.QDTxMeasUPP!, getPicProc getPicProc: ApplicationServices.QDGetPicUPP!, putPicProc putPicProc: ApplicationServices.QDPutPicUPP!, opcodeProc opcodeProc: ApplicationServices.QDOpcodeUPP!, newProc1 newProc1: Darwin.UniversalProcPtr!, glyphsProc glyphsProc: ApplicationServices.QDStdGlyphsUPP!, printerStatusProc printerStatusProc: ApplicationServices.QDPrinterStatusUPP!, newProc4 newProc4: Darwin.UniversalProcPtr!, newProc5 newProc5: Darwin.UniversalProcPtr!, newProc6 newProc6: Darwin.UniversalProcPtr!) } ``` |

Modified [CQDProcs.arcProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1462707-arcproc)

|  | Declaration |
| --- | --- |
| From | ``` var arcProc: QDArcUPP! ``` |
| To | ``` var arcProc: ApplicationServices.QDArcUPP! ``` |

Modified [CQDProcs.bitsProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1463001-bitsproc)

|  | Declaration |
| --- | --- |
| From | ``` var bitsProc: QDBitsUPP! ``` |
| To | ``` var bitsProc: ApplicationServices.QDBitsUPP! ``` |

Modified [CQDProcs.commentProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1463288-commentproc)

|  | Declaration |
| --- | --- |
| From | ``` var commentProc: QDCommentUPP! ``` |
| To | ``` var commentProc: ApplicationServices.QDCommentUPP! ``` |

Modified [CQDProcs.getPicProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1462475-getpicproc)

|  | Declaration |
| --- | --- |
| From | ``` var getPicProc: QDGetPicUPP! ``` |
| To | ``` var getPicProc: ApplicationServices.QDGetPicUPP! ``` |

Modified [CQDProcs.glyphsProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1459000-glyphsproc)

|  | Declaration |
| --- | --- |
| From | ``` var glyphsProc: QDStdGlyphsUPP! ``` |
| To | ``` var glyphsProc: ApplicationServices.QDStdGlyphsUPP! ``` |

Modified [CQDProcs.lineProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1463885-lineproc)

|  | Declaration |
| --- | --- |
| From | ``` var lineProc: QDLineUPP! ``` |
| To | ``` var lineProc: ApplicationServices.QDLineUPP! ``` |

Modified [CQDProcs.newProc1](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461234-newproc1)

|  | Declaration |
| --- | --- |
| From | ``` var newProc1: UniversalProcPtr! ``` |
| To | ``` var newProc1: Darwin.UniversalProcPtr! ``` |

Modified [CQDProcs.newProc4](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461037-newproc4)

|  | Declaration |
| --- | --- |
| From | ``` var newProc4: UniversalProcPtr! ``` |
| To | ``` var newProc4: Darwin.UniversalProcPtr! ``` |

Modified [CQDProcs.newProc5](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461848-newproc5)

|  | Declaration |
| --- | --- |
| From | ``` var newProc5: UniversalProcPtr! ``` |
| To | ``` var newProc5: Darwin.UniversalProcPtr! ``` |

Modified [CQDProcs.newProc6](https://developer.apple.com/documentation/applicationservices/cqdprocs/1459877-newproc6)

|  | Declaration |
| --- | --- |
| From | ``` var newProc6: UniversalProcPtr! ``` |
| To | ``` var newProc6: Darwin.UniversalProcPtr! ``` |

Modified [CQDProcs.opcodeProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1459207-opcodeproc)

|  | Declaration |
| --- | --- |
| From | ``` var opcodeProc: QDOpcodeUPP! ``` |
| To | ``` var opcodeProc: ApplicationServices.QDOpcodeUPP! ``` |

Modified [CQDProcs.ovalProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1462138-ovalproc)

|  | Declaration |
| --- | --- |
| From | ``` var ovalProc: QDOvalUPP! ``` |
| To | ``` var ovalProc: ApplicationServices.QDOvalUPP! ``` |

Modified [CQDProcs.polyProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461442-polyproc)

|  | Declaration |
| --- | --- |
| From | ``` var polyProc: QDPolyUPP! ``` |
| To | ``` var polyProc: ApplicationServices.QDPolyUPP! ``` |

Modified [CQDProcs.printerStatusProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1464531-printerstatusproc)

|  | Declaration |
| --- | --- |
| From | ``` var printerStatusProc: QDPrinterStatusUPP! ``` |
| To | ``` var printerStatusProc: ApplicationServices.QDPrinterStatusUPP! ``` |

Modified [CQDProcs.putPicProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461526-putpicproc)

|  | Declaration |
| --- | --- |
| From | ``` var putPicProc: QDPutPicUPP! ``` |
| To | ``` var putPicProc: ApplicationServices.QDPutPicUPP! ``` |

Modified [CQDProcs.rectProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1464519-rectproc)

|  | Declaration |
| --- | --- |
| From | ``` var rectProc: QDRectUPP! ``` |
| To | ``` var rectProc: ApplicationServices.QDRectUPP! ``` |

Modified [CQDProcs.rgnProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1463631-rgnproc)

|  | Declaration |
| --- | --- |
| From | ``` var rgnProc: QDRgnUPP! ``` |
| To | ``` var rgnProc: ApplicationServices.QDRgnUPP! ``` |

Modified [CQDProcs.rRectProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1461880-rrectproc)

|  | Declaration |
| --- | --- |
| From | ``` var rRectProc: QDRRectUPP! ``` |
| To | ``` var rRectProc: ApplicationServices.QDRRectUPP! ``` |

Modified [CQDProcs.textProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1460192-textproc)

|  | Declaration |
| --- | --- |
| From | ``` var textProc: QDTextUPP! ``` |
| To | ``` var textProc: ApplicationServices.QDTextUPP! ``` |

Modified [CQDProcs.txMeasProc](https://developer.apple.com/documentation/applicationservices/cqdprocs/1464721-txmeasproc)

|  | Declaration |
| --- | --- |
| From | ``` var txMeasProc: QDTxMeasUPP! ``` |
| To | ``` var txMeasProc: ApplicationServices.QDTxMeasUPP! ``` |

Modified [DCMDictionaryHeader [struct]](https://developer.apple.com/documentation/applicationservices/dcmdictionaryheader)

|  | Declaration |
| --- | --- |
| From | ``` struct DCMDictionaryHeader {     var headerSignature: FourCharCode     var headerVersion: UInt32     var headerSize: UInt32     var accessMethod: Str63     init()     init(headerSignature headerSignature: FourCharCode, headerVersion headerVersion: UInt32, headerSize headerSize: UInt32, accessMethod accessMethod: Str63) } ``` |
| To | ``` struct DCMDictionaryHeader {     var headerSignature: FourCharCode     var headerVersion: UInt32     var headerSize: UInt32     var accessMethod: Darwin.Str63     init()     init(headerSignature headerSignature: FourCharCode, headerVersion headerVersion: UInt32, headerSize headerSize: UInt32, accessMethod accessMethod: Darwin.Str63) } ``` |

Modified [DCMDictionaryHeader.accessMethod](https://developer.apple.com/documentation/applicationservices/dcmdictionaryheader/1409021-accessmethod)

|  | Declaration |
| --- | --- |
| From | ``` var accessMethod: Str63 ``` |
| To | ``` var accessMethod: Darwin.Str63 ``` |

Modified [DCMDictionaryHeader.init(headerSignature: FourCharCode, headerVersion: UInt32, headerSize: UInt32, accessMethod: Darwin.Str63)](https://developer.apple.com/documentation/applicationservices/dcmdictionaryheader/1459129-init)

|  | Declaration |
| --- | --- |
| From | ``` init(headerSignature headerSignature: FourCharCode, headerVersion headerVersion: UInt32, headerSize headerSize: UInt32, accessMethod accessMethod: Str63) ``` |
| To | ``` init(headerSignature headerSignature: FourCharCode, headerVersion headerVersion: UInt32, headerSize headerSize: UInt32, accessMethod accessMethod: Darwin.Str63) ``` |

Modified [FMFilter [struct]](https://developer.apple.com/documentation/applicationservices/fmfilter)

|  | Declaration |
| --- | --- |
| From | ``` struct FMFilter {     struct __Unnamed_union_filter {         var fontTechnologyFilter: FourCharCode         var fontContainerFilter: ATSFSSpec         var generationFilter: FMGeneration         var fontFamilyCallbackFilter: FMFontFamilyCallbackFilterUPP!         var fontCallbackFilter: FMFontCallbackFilterUPP!         var fontDirectoryFilter: FMFontDirectoryFilter         var fontFileRefFilter: UnsafePointer<FSRef>         init(fontTechnologyFilter fontTechnologyFilter: FourCharCode)         init(fontContainerFilter fontContainerFilter: ATSFSSpec)         init(generationFilter generationFilter: FMGeneration)         init(fontFamilyCallbackFilter fontFamilyCallbackFilter: FMFontFamilyCallbackFilterUPP!)         init(fontCallbackFilter fontCallbackFilter: FMFontCallbackFilterUPP!)         init(fontDirectoryFilter fontDirectoryFilter: FMFontDirectoryFilter)         init(fontFileRefFilter fontFileRefFilter: UnsafePointer<FSRef>)         init()     }     var format: UInt32     var selector: FMFilterSelector     var filter: FMFilter.__Unnamed_union_filter     init()     init(format format: UInt32, selector selector: FMFilterSelector, filter filter: FMFilter.__Unnamed_union_filter) } ``` |
| To | ``` struct FMFilter {     struct __Unnamed_union_filter {         var fontTechnologyFilter: FourCharCode         var fontContainerFilter: ATSFSSpec         var generationFilter: FMGeneration         var fontFamilyCallbackFilter: ApplicationServices.FMFontFamilyCallbackFilterUPP!         var fontCallbackFilter: ApplicationServices.FMFontCallbackFilterUPP!         var fontDirectoryFilter: FMFontDirectoryFilter         var fontFileRefFilter: UnsafePointer<FSRef>!         init(fontTechnologyFilter fontTechnologyFilter: FourCharCode)         init(fontContainerFilter fontContainerFilter: ATSFSSpec)         init(generationFilter generationFilter: FMGeneration)         init(fontFamilyCallbackFilter fontFamilyCallbackFilter: ApplicationServices.FMFontFamilyCallbackFilterUPP!)         init(fontCallbackFilter fontCallbackFilter: ApplicationServices.FMFontCallbackFilterUPP!)         init(fontDirectoryFilter fontDirectoryFilter: FMFontDirectoryFilter)         init(fontFileRefFilter fontFileRefFilter: UnsafePointer<FSRef>!)         init()     }     var format: UInt32     var selector: FMFilterSelector     var filter: FMFilter.__Unnamed_union_filter     init()     init(format format: UInt32, selector selector: FMFilterSelector, filter filter: FMFilter.__Unnamed_union_filter) } ``` |

Modified [GDevice [struct]](https://developer.apple.com/documentation/applicationservices/gdevice)

|  | Declaration |
| --- | --- |
| From | ``` struct GDevice {     var gdRefNum: Int16     var gdID: Int16     var gdType: Int16     var gdITable: Handle     var gdResPref: Int16     var gdSearchProc: Handle     var gdCompProc: Handle     var gdFlags: Int16     var gdPMap: PixMapHandle     var gdRefCon: Int32     var gdNextGD: GDHandle     var gdRect: Rect     var gdMode: Int32     var gdCCBytes: Int16     var gdCCDepth: Int16     var gdCCXData: Handle     var gdCCXMask: Handle     var gdExt: Handle     init()     init(gdRefNum gdRefNum: Int16, gdID gdID: Int16, gdType gdType: Int16, gdITable gdITable: Handle, gdResPref gdResPref: Int16, gdSearchProc gdSearchProc: Handle, gdCompProc gdCompProc: Handle, gdFlags gdFlags: Int16, gdPMap gdPMap: PixMapHandle, gdRefCon gdRefCon: Int32, gdNextGD gdNextGD: GDHandle, gdRect gdRect: Rect, gdMode gdMode: Int32, gdCCBytes gdCCBytes: Int16, gdCCDepth gdCCDepth: Int16, gdCCXData gdCCXData: Handle, gdCCXMask gdCCXMask: Handle, gdExt gdExt: Handle) } ``` |
| To | ``` struct GDevice {     var gdRefNum: Int16     var gdID: Int16     var gdType: Int16     var gdITable: Handle!     var gdResPref: Int16     var gdSearchProc: Handle!     var gdCompProc: Handle!     var gdFlags: Int16     var gdPMap: PixMapHandle!     var gdRefCon: Int32     var gdNextGD: GDHandle!     var gdRect: Rect     var gdMode: Int32     var gdCCBytes: Int16     var gdCCDepth: Int16     var gdCCXData: Handle!     var gdCCXMask: Handle!     var gdExt: Handle!     init()     init(gdRefNum gdRefNum: Int16, gdID gdID: Int16, gdType gdType: Int16, gdITable gdITable: Handle!, gdResPref gdResPref: Int16, gdSearchProc gdSearchProc: Handle!, gdCompProc gdCompProc: Handle!, gdFlags gdFlags: Int16, gdPMap gdPMap: PixMapHandle!, gdRefCon gdRefCon: Int32, gdNextGD gdNextGD: GDHandle!, gdRect gdRect: Rect, gdMode gdMode: Int32, gdCCBytes gdCCBytes: Int16, gdCCDepth gdCCDepth: Int16, gdCCXData gdCCXData: Handle!, gdCCXMask gdCCXMask: Handle!, gdExt gdExt: Handle!) } ``` |

Modified [GDevice.gdCCXData](https://developer.apple.com/documentation/applicationservices/gdevice/1459010-gdccxdata)

|  | Declaration |
| --- | --- |
| From | ``` var gdCCXData: Handle ``` |
| To | ``` var gdCCXData: Handle! ``` |

Modified [GDevice.gdCCXMask](https://developer.apple.com/documentation/applicationservices/gdevice/1459120-gdccxmask)

|  | Declaration |
| --- | --- |
| From | ``` var gdCCXMask: Handle ``` |
| To | ``` var gdCCXMask: Handle! ``` |

Modified [GDevice.gdCompProc](https://developer.apple.com/documentation/applicationservices/gdevice/1459239-gdcompproc)

|  | Declaration |
| --- | --- |
| From | ``` var gdCompProc: Handle ``` |
| To | ``` var gdCompProc: Handle! ``` |

Modified [GDevice.gdExt](https://developer.apple.com/documentation/applicationservices/gdevice/1459670-gdext)

|  | Declaration |
| --- | --- |
| From | ``` var gdExt: Handle ``` |
| To | ``` var gdExt: Handle! ``` |

Modified [GDevice.gdITable](https://developer.apple.com/documentation/applicationservices/gdevice/1458907-gditable)

|  | Declaration |
| --- | --- |
| From | ``` var gdITable: Handle ``` |
| To | ``` var gdITable: Handle! ``` |

Modified [GDevice.gdNextGD](https://developer.apple.com/documentation/applicationservices/gdevice/1458799-gdnextgd)

|  | Declaration |
| --- | --- |
| From | ``` var gdNextGD: GDHandle ``` |
| To | ``` var gdNextGD: GDHandle! ``` |

Modified [GDevice.gdPMap](https://developer.apple.com/documentation/applicationservices/gdevice/1459113-gdpmap)

|  | Declaration |
| --- | --- |
| From | ``` var gdPMap: PixMapHandle ``` |
| To | ``` var gdPMap: PixMapHandle! ``` |

Modified [GDevice.gdSearchProc](https://developer.apple.com/documentation/applicationservices/gdevice/1462338-gdsearchproc)

|  | Declaration |
| --- | --- |
| From | ``` var gdSearchProc: Handle ``` |
| To | ``` var gdSearchProc: Handle! ``` |

Modified [HomographDicInfoRec [struct]](https://developer.apple.com/documentation/applicationservices/homographdicinforec)

|  | Declaration |
| --- | --- |
| From | ``` struct HomographDicInfoRec {     var dictionaryID: DCMDictionaryID     var uniqueID: DCMUniqueID     init()     init(dictionaryID dictionaryID: DCMDictionaryID, uniqueID uniqueID: DCMUniqueID) } ``` |
| To | ``` struct HomographDicInfoRec {     var dictionaryID: DCMDictionaryID!     var uniqueID: DCMUniqueID     init()     init(dictionaryID dictionaryID: DCMDictionaryID!, uniqueID uniqueID: DCMUniqueID) } ``` |

Modified [HomographDicInfoRec.dictionaryID](https://developer.apple.com/documentation/applicationservices/homographdicinforec/1459237-dictionaryid)

|  | Declaration |
| --- | --- |
| From | ``` var dictionaryID: DCMDictionaryID ``` |
| To | ``` var dictionaryID: DCMDictionaryID! ``` |

Modified [ICAppSpec [struct]](https://developer.apple.com/documentation/applicationservices/icappspec)

|  | Declaration |
| --- | --- |
| From | ``` struct ICAppSpec {     var fCreator: OSType     var name: Str63     init()     init(fCreator fCreator: OSType, name name: Str63) } ``` |
| To | ``` struct ICAppSpec {     var fCreator: OSType     var name: Darwin.Str63     init()     init(fCreator fCreator: OSType, name name: Darwin.Str63) } ``` |

Modified [ICAppSpec.init(fCreator: OSType, name: Darwin.Str63)](https://developer.apple.com/documentation/applicationservices/icappspec/1459250-init)

|  | Declaration |
| --- | --- |
| From | ``` init(fCreator fCreator: OSType, name name: Str63) ``` |
| To | ``` init(fCreator fCreator: OSType, name name: Darwin.Str63) ``` |

Modified [ICAppSpec.name](https://developer.apple.com/documentation/applicationservices/icappspec/1461948-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: Str63 ``` |
| To | ``` var name: Darwin.Str63 ``` |

Modified [ICFileSpec [struct]](https://developer.apple.com/documentation/applicationservices/icfilespec)

|  | Declaration |
| --- | --- |
| From | ``` struct ICFileSpec {     var volName: Str31     var volCreationDate: Int32     var fss: FSSpec     var alias: AliasRecord     init()     init(volName volName: Str31, volCreationDate volCreationDate: Int32, fss fss: FSSpec, alias alias: AliasRecord) } ``` |
| To | ``` struct ICFileSpec {     var volName: Darwin.Str31     var volCreationDate: Int32     var fss: FSSpec     var alias: AliasRecord     init()     init(volName volName: Darwin.Str31, volCreationDate volCreationDate: Int32, fss fss: FSSpec, alias alias: AliasRecord) } ``` |

Modified [ICFileSpec.init(volName: Darwin.Str31, volCreationDate: Int32, fss: FSSpec, alias: AliasRecord)](https://developer.apple.com/documentation/applicationservices/icfilespec/1460097-init)

|  | Declaration |
| --- | --- |
| From | ``` init(volName volName: Str31, volCreationDate volCreationDate: Int32, fss fss: FSSpec, alias alias: AliasRecord) ``` |
| To | ``` init(volName volName: Darwin.Str31, volCreationDate volCreationDate: Int32, fss fss: FSSpec, alias alias: AliasRecord) ``` |

Modified [ICFileSpec.volName](https://developer.apple.com/documentation/applicationservices/icfilespec/1462535-volname)

|  | Declaration |
| --- | --- |
| From | ``` var volName: Str31 ``` |
| To | ``` var volName: Darwin.Str31 ``` |

Modified [ICFontRecord [struct]](https://developer.apple.com/documentation/applicationservices/icfontrecord)

|  | Declaration |
| --- | --- |
| From | ``` struct ICFontRecord {     var size: Int16     var face: Style     var pad: Int8     var font: Str255     init()     init(size size: Int16, face face: Style, pad pad: Int8, font font: Str255) } ``` |
| To | ``` struct ICFontRecord {     var size: Int16     var face: Style     var pad: Int8     var font: Darwin.Str255     init()     init(size size: Int16, face face: Style, pad pad: Int8, font font: Darwin.Str255) } ``` |

Modified [ICFontRecord.font](https://developer.apple.com/documentation/applicationservices/icfontrecord/1463495-font)

|  | Declaration |
| --- | --- |
| From | ``` var font: Str255 ``` |
| To | ``` var font: Darwin.Str255 ``` |

Modified [ICFontRecord.init(size: Int16, face: Style, pad: Int8, font: Darwin.Str255)](https://developer.apple.com/documentation/applicationservices/icfontrecord/1458842-init)

|  | Declaration |
| --- | --- |
| From | ``` init(size size: Int16, face face: Style, pad pad: Int8, font font: Str255) ``` |
| To | ``` init(size size: Int16, face face: Style, pad pad: Int8, font font: Darwin.Str255) ``` |

Modified [ICMapEntry [struct]](https://developer.apple.com/documentation/applicationservices/icmapentry)

|  | Declaration |
| --- | --- |
| From | ``` struct ICMapEntry {     var totalLength: Int16     var fixedLength: ICFixedLength     var version: Int16     var fileType: OSType     var fileCreator: OSType     var postCreator: OSType     var flags: ICMapEntryFlags     var `extension`: Str255     var creatorAppName: Str255     var postAppName: Str255     var MIMEType: Str255     var entryName: Str255     init()     init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, extension extension: Str255, creatorAppName creatorAppName: Str255, postAppName postAppName: Str255, MIMEType MIMEType: Str255, entryName entryName: Str255) } ``` |
| To | ``` struct ICMapEntry {     var totalLength: Int16     var fixedLength: ICFixedLength     var version: Int16     var fileType: OSType     var fileCreator: OSType     var postCreator: OSType     var flags: ICMapEntryFlags     var `extension`: Darwin.Str255     var creatorAppName: Darwin.Str255     var postAppName: Darwin.Str255     var MIMEType: Darwin.Str255     var entryName: Darwin.Str255     init()     init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, extension extension: Darwin.Str255, creatorAppName creatorAppName: Darwin.Str255, postAppName postAppName: Darwin.Str255, MIMEType MIMEType: Darwin.Str255, entryName entryName: Darwin.Str255) } ``` |

Modified [ICMapEntry.creatorAppName](https://developer.apple.com/documentation/applicationservices/icmapentry/1463557-creatorappname)

|  | Declaration |
| --- | --- |
| From | ``` var creatorAppName: Str255 ``` |
| To | ``` var creatorAppName: Darwin.Str255 ``` |

Modified [ICMapEntry.entryName](https://developer.apple.com/documentation/applicationservices/icmapentry/1463382-entryname)

|  | Declaration |
| --- | --- |
| From | ``` var entryName: Str255 ``` |
| To | ``` var entryName: Darwin.Str255 ``` |

Modified [ICMapEntry.extension](https://developer.apple.com/documentation/applicationservices/icmapentry/1459990-extension)

|  | Declaration |
| --- | --- |
| From | ``` var `extension`: Str255 ``` |
| To | ``` var `extension`: Darwin.Str255 ``` |

Modified [ICMapEntry.init(totalLength: Int16, fixedLength: ICFixedLength, version: Int16, fileType: OSType, fileCreator: OSType, postCreator: OSType, flags: ICMapEntryFlags, extension: Darwin.Str255, creatorAppName: Darwin.Str255, postAppName: Darwin.Str255, MIMEType: Darwin.Str255, entryName: Darwin.Str255)](https://developer.apple.com/documentation/applicationservices/icmapentry/1463249-init)

|  | Declaration |
| --- | --- |
| From | ``` init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, extension extension: Str255, creatorAppName creatorAppName: Str255, postAppName postAppName: Str255, MIMEType MIMEType: Str255, entryName entryName: Str255) ``` |
| To | ``` init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, extension extension: Darwin.Str255, creatorAppName creatorAppName: Darwin.Str255, postAppName postAppName: Darwin.Str255, MIMEType MIMEType: Darwin.Str255, entryName entryName: Darwin.Str255) ``` |

Modified [ICMapEntry.MIMEType](https://developer.apple.com/documentation/applicationservices/icmapentry/1462908-mimetype)

|  | Declaration |
| --- | --- |
| From | ``` var MIMEType: Str255 ``` |
| To | ``` var MIMEType: Darwin.Str255 ``` |

Modified [ICMapEntry.postAppName](https://developer.apple.com/documentation/applicationservices/icmapentry/1464312-postappname)

|  | Declaration |
| --- | --- |
| From | ``` var postAppName: Str255 ``` |
| To | ``` var postAppName: Darwin.Str255 ``` |

Modified [ICServiceEntry [struct]](https://developer.apple.com/documentation/applicationservices/icserviceentry)

|  | Declaration |
| --- | --- |
| From | ``` struct ICServiceEntry {     var name: Str255     var port: Int16     var flags: ICServiceEntryFlags     init()     init(name name: Str255, port port: Int16, flags flags: ICServiceEntryFlags) } ``` |
| To | ``` struct ICServiceEntry {     var name: Darwin.Str255     var port: Int16     var flags: ICServiceEntryFlags     init()     init(name name: Darwin.Str255, port port: Int16, flags flags: ICServiceEntryFlags) } ``` |

Modified [ICServiceEntry.init(name: Darwin.Str255, port: Int16, flags: ICServiceEntryFlags)](https://developer.apple.com/documentation/applicationservices/icserviceentry/1459244-init)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: Str255, port port: Int16, flags flags: ICServiceEntryFlags) ``` |
| To | ``` init(name name: Darwin.Str255, port port: Int16, flags flags: ICServiceEntryFlags) ``` |

Modified [ICServiceEntry.name](https://developer.apple.com/documentation/applicationservices/icserviceentry/1460135-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: Str255 ``` |
| To | ``` var name: Darwin.Str255 ``` |

Modified [LAMorphemeRec [struct]](https://developer.apple.com/documentation/applicationservices/lamorphemerec)

|  | Declaration |
| --- | --- |
| From | ``` struct LAMorphemeRec {     var sourceTextLength: UInt32     var sourceTextPtr: LogicalAddress     var morphemeTextLength: UInt32     var morphemeTextPtr: LogicalAddress     var partOfSpeech: UInt32     init()     init(sourceTextLength sourceTextLength: UInt32, sourceTextPtr sourceTextPtr: LogicalAddress, morphemeTextLength morphemeTextLength: UInt32, morphemeTextPtr morphemeTextPtr: LogicalAddress, partOfSpeech partOfSpeech: UInt32) } ``` |
| To | ``` struct LAMorphemeRec {     var sourceTextLength: UInt32     var sourceTextPtr: LogicalAddress!     var morphemeTextLength: UInt32     var morphemeTextPtr: LogicalAddress!     var partOfSpeech: UInt32     init()     init(sourceTextLength sourceTextLength: UInt32, sourceTextPtr sourceTextPtr: LogicalAddress!, morphemeTextLength morphemeTextLength: UInt32, morphemeTextPtr morphemeTextPtr: LogicalAddress!, partOfSpeech partOfSpeech: UInt32) } ``` |

Modified [LAMorphemeRec.morphemeTextPtr](https://developer.apple.com/documentation/applicationservices/lamorphemerec/1462432-morphemetextptr)

|  | Declaration |
| --- | --- |
| From | ``` var morphemeTextPtr: LogicalAddress ``` |
| To | ``` var morphemeTextPtr: LogicalAddress! ``` |

Modified [LAMorphemeRec.sourceTextPtr](https://developer.apple.com/documentation/applicationservices/lamorphemerec/1462602-sourcetextptr)

|  | Declaration |
| --- | --- |
| From | ``` var sourceTextPtr: LogicalAddress ``` |
| To | ``` var sourceTextPtr: LogicalAddress! ``` |

Modified [LaunchParamBlockRec [struct]](https://developer.apple.com/documentation/applicationservices/launchparamblockrec)

|  | Declaration |
| --- | --- |
| From | ``` struct LaunchParamBlockRec {     var reserved1: UInt32     var reserved2: UInt16     var launchBlockID: UInt16     var launchEPBLength: UInt32     var launchFileFlags: UInt16     var launchControlFlags: LaunchFlags     var launchAppRef: FSRefPtr     var launchProcessSN: ProcessSerialNumber     var launchPreferredSize: UInt32     var launchMinimumSize: UInt32     var launchAvailableSize: UInt32     var launchAppParameters: AppParametersPtr     init()     init(reserved1 reserved1: UInt32, reserved2 reserved2: UInt16, launchBlockID launchBlockID: UInt16, launchEPBLength launchEPBLength: UInt32, launchFileFlags launchFileFlags: UInt16, launchControlFlags launchControlFlags: LaunchFlags, launchAppRef launchAppRef: FSRefPtr, launchProcessSN launchProcessSN: ProcessSerialNumber, launchPreferredSize launchPreferredSize: UInt32, launchMinimumSize launchMinimumSize: UInt32, launchAvailableSize launchAvailableSize: UInt32, launchAppParameters launchAppParameters: AppParametersPtr) } ``` |
| To | ``` struct LaunchParamBlockRec {     var reserved1: UInt32     var reserved2: UInt16     var launchBlockID: UInt16     var launchEPBLength: UInt32     var launchFileFlags: UInt16     var launchControlFlags: LaunchFlags     var launchAppRef: FSRefPtr!     var launchProcessSN: ProcessSerialNumber     var launchPreferredSize: UInt32     var launchMinimumSize: UInt32     var launchAvailableSize: UInt32     var launchAppParameters: AppParametersPtr!     init()     init(reserved1 reserved1: UInt32, reserved2 reserved2: UInt16, launchBlockID launchBlockID: UInt16, launchEPBLength launchEPBLength: UInt32, launchFileFlags launchFileFlags: UInt16, launchControlFlags launchControlFlags: LaunchFlags, launchAppRef launchAppRef: FSRefPtr!, launchProcessSN launchProcessSN: ProcessSerialNumber, launchPreferredSize launchPreferredSize: UInt32, launchMinimumSize launchMinimumSize: UInt32, launchAvailableSize launchAvailableSize: UInt32, launchAppParameters launchAppParameters: AppParametersPtr!) } ``` |

Modified [LaunchParamBlockRec.launchAppParameters](https://developer.apple.com/documentation/applicationservices/launchparamblockrec/1459942-launchappparameters)

|  | Declaration |
| --- | --- |
| From | ``` var launchAppParameters: AppParametersPtr ``` |
| To | ``` var launchAppParameters: AppParametersPtr! ``` |

Modified [LaunchParamBlockRec.launchAppRef](https://developer.apple.com/documentation/applicationservices/launchparamblockrec/1460856-launchappref)

|  | Declaration |
| --- | --- |
| From | ``` var launchAppRef: FSRefPtr ``` |
| To | ``` var launchAppRef: FSRefPtr! ``` |

Modified [NameTable [struct]](https://developer.apple.com/documentation/applicationservices/nametable)

|  | Declaration |
| --- | --- |
| From | ``` struct NameTable {     var stringCount: Int16     var baseFontName: Str255     init()     init(stringCount stringCount: Int16, baseFontName baseFontName: Str255) } ``` |
| To | ``` struct NameTable {     var stringCount: Int16     var baseFontName: Darwin.Str255     init()     init(stringCount stringCount: Int16, baseFontName baseFontName: Darwin.Str255) } ``` |

Modified [NameTable.baseFontName](https://developer.apple.com/documentation/applicationservices/nametable/1463733-basefontname)

|  | Declaration |
| --- | --- |
| From | ``` var baseFontName: Str255 ``` |
| To | ``` var baseFontName: Darwin.Str255 ``` |

Modified [NameTable.init(stringCount: Int16, baseFontName: Darwin.Str255)](https://developer.apple.com/documentation/applicationservices/nametable/1462387-init)

|  | Declaration |
| --- | --- |
| From | ``` init(stringCount stringCount: Int16, baseFontName baseFontName: Str255) ``` |
| To | ``` init(stringCount stringCount: Int16, baseFontName baseFontName: Darwin.Str255) ``` |

Modified [PhonemeInfo [struct]](https://developer.apple.com/documentation/applicationservices/phonemeinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct PhonemeInfo {     var opcode: Int16     var phStr: Str15     var exampleStr: Str31     var hiliteStart: Int16     var hiliteEnd: Int16     init()     init(opcode opcode: Int16, phStr phStr: Str15, exampleStr exampleStr: Str31, hiliteStart hiliteStart: Int16, hiliteEnd hiliteEnd: Int16) } ``` |
| To | ``` struct PhonemeInfo {     var opcode: Int16     var phStr: Darwin.Str15     var exampleStr: Darwin.Str31     var hiliteStart: Int16     var hiliteEnd: Int16     init()     init(opcode opcode: Int16, phStr phStr: Darwin.Str15, exampleStr exampleStr: Darwin.Str31, hiliteStart hiliteStart: Int16, hiliteEnd hiliteEnd: Int16) } ``` |

Modified [PhonemeInfo.exampleStr](https://developer.apple.com/documentation/applicationservices/phonemeinfo/1460341-examplestr)

|  | Declaration |
| --- | --- |
| From | ``` var exampleStr: Str31 ``` |
| To | ``` var exampleStr: Darwin.Str31 ``` |

Modified [PhonemeInfo.init(opcode: Int16, phStr: Darwin.Str15, exampleStr: Darwin.Str31, hiliteStart: Int16, hiliteEnd: Int16)](https://developer.apple.com/documentation/applicationservices/phonemeinfo/1459158-init)

|  | Declaration |
| --- | --- |
| From | ``` init(opcode opcode: Int16, phStr phStr: Str15, exampleStr exampleStr: Str31, hiliteStart hiliteStart: Int16, hiliteEnd hiliteEnd: Int16) ``` |
| To | ``` init(opcode opcode: Int16, phStr phStr: Darwin.Str15, exampleStr exampleStr: Darwin.Str31, hiliteStart hiliteStart: Int16, hiliteEnd hiliteEnd: Int16) ``` |

Modified [PhonemeInfo.phStr](https://developer.apple.com/documentation/applicationservices/phonemeinfo/1461253-phstr)

|  | Declaration |
| --- | --- |
| From | ``` var phStr: Str15 ``` |
| To | ``` var phStr: Darwin.Str15 ``` |

Modified [PixMap [struct]](https://developer.apple.com/documentation/applicationservices/pixmap)

|  | Declaration |
| --- | --- |
| From | ``` struct PixMap {     var baseAddr: Ptr     var rowBytes: Int16     var bounds: Rect     var pmVersion: Int16     var packType: Int16     var packSize: Int32     var hRes: Fixed     var vRes: Fixed     var pixelType: Int16     var pixelSize: Int16     var cmpCount: Int16     var cmpSize: Int16     var pixelFormat: OSType     var pmTable: CTabHandle     var pmExt: UnsafeMutablePointer<Void>     init()     init(baseAddr baseAddr: Ptr, rowBytes rowBytes: Int16, bounds bounds: Rect, pmVersion pmVersion: Int16, packType packType: Int16, packSize packSize: Int32, hRes hRes: Fixed, vRes vRes: Fixed, pixelType pixelType: Int16, pixelSize pixelSize: Int16, cmpCount cmpCount: Int16, cmpSize cmpSize: Int16, pixelFormat pixelFormat: OSType, pmTable pmTable: CTabHandle, pmExt pmExt: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct PixMap {     var baseAddr: Ptr!     var rowBytes: Int16     var bounds: Rect     var pmVersion: Int16     var packType: Int16     var packSize: Int32     var hRes: Fixed     var vRes: Fixed     var pixelType: Int16     var pixelSize: Int16     var cmpCount: Int16     var cmpSize: Int16     var pixelFormat: OSType     var pmTable: CTabHandle!     var pmExt: UnsafeMutableRawPointer!     init()     init(baseAddr baseAddr: Ptr!, rowBytes rowBytes: Int16, bounds bounds: Rect, pmVersion pmVersion: Int16, packType packType: Int16, packSize packSize: Int32, hRes hRes: Fixed, vRes vRes: Fixed, pixelType pixelType: Int16, pixelSize pixelSize: Int16, cmpCount cmpCount: Int16, cmpSize cmpSize: Int16, pixelFormat pixelFormat: OSType, pmTable pmTable: CTabHandle!, pmExt pmExt: UnsafeMutableRawPointer!) } ``` |

Modified [PixMap.baseAddr](https://developer.apple.com/documentation/applicationservices/pixmap/1459096-baseaddr)

|  | Declaration |
| --- | --- |
| From | ``` var baseAddr: Ptr ``` |
| To | ``` var baseAddr: Ptr! ``` |

Modified [PixMap.pmExt](https://developer.apple.com/documentation/applicationservices/pixmap/1462255-pmext)

|  | Declaration |
| --- | --- |
| From | ``` var pmExt: UnsafeMutablePointer<Void> ``` |
| To | ``` var pmExt: UnsafeMutableRawPointer! ``` |

Modified [PixMap.pmTable](https://developer.apple.com/documentation/applicationservices/pixmap/1459634-pmtable)

|  | Declaration |
| --- | --- |
| From | ``` var pmTable: CTabHandle ``` |
| To | ``` var pmTable: CTabHandle! ``` |

Modified [PixPat [struct]](https://developer.apple.com/documentation/applicationservices/pixpat)

|  | Declaration |
| --- | --- |
| From | ``` struct PixPat {     var patType: Int16     var patMap: PixMapHandle     var patData: Handle     var patXData: Handle     var patXValid: Int16     var patXMap: Handle     var pat1Data: Pattern     init()     init(patType patType: Int16, patMap patMap: PixMapHandle, patData patData: Handle, patXData patXData: Handle, patXValid patXValid: Int16, patXMap patXMap: Handle, pat1Data pat1Data: Pattern) } ``` |
| To | ``` struct PixPat {     var patType: Int16     var patMap: PixMapHandle!     var patData: Handle!     var patXData: Handle!     var patXValid: Int16     var patXMap: Handle!     var pat1Data: Pattern     init()     init(patType patType: Int16, patMap patMap: PixMapHandle!, patData patData: Handle!, patXData patXData: Handle!, patXValid patXValid: Int16, patXMap patXMap: Handle!, pat1Data pat1Data: Pattern) } ``` |

Modified [PixPat.patData](https://developer.apple.com/documentation/applicationservices/pixpat/1459829-patdata)

|  | Declaration |
| --- | --- |
| From | ``` var patData: Handle ``` |
| To | ``` var patData: Handle! ``` |

Modified [PixPat.patMap](https://developer.apple.com/documentation/applicationservices/pixpat/1464638-patmap)

|  | Declaration |
| --- | --- |
| From | ``` var patMap: PixMapHandle ``` |
| To | ``` var patMap: PixMapHandle! ``` |

Modified [PixPat.patXData](https://developer.apple.com/documentation/applicationservices/pixpat/1459286-patxdata)

|  | Declaration |
| --- | --- |
| From | ``` var patXData: Handle ``` |
| To | ``` var patXData: Handle! ``` |

Modified [PixPat.patXMap](https://developer.apple.com/documentation/applicationservices/pixpat/1463879-patxmap)

|  | Declaration |
| --- | --- |
| From | ``` var patXMap: Handle ``` |
| To | ``` var patXMap: Handle! ``` |

Modified [PMLanguageInfo [struct]](https://developer.apple.com/documentation/applicationservices/pmlanguageinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct PMLanguageInfo {     var level: Str32     var version: Str32     var release: Str32     init()     init(level level: Str32, version version: Str32, release release: Str32) } ``` |
| To | ``` struct PMLanguageInfo {     var level: Darwin.Str32     var version: Darwin.Str32     var release: Darwin.Str32     init()     init(level level: Darwin.Str32, version version: Darwin.Str32, release release: Darwin.Str32) } ``` |

Modified [PMLanguageInfo.init(level: Darwin.Str32, version: Darwin.Str32, release: Darwin.Str32)](https://developer.apple.com/documentation/applicationservices/pmlanguageinfo/1464084-init)

|  | Declaration |
| --- | --- |
| From | ``` init(level level: Str32, version version: Str32, release release: Str32) ``` |
| To | ``` init(level level: Darwin.Str32, version version: Darwin.Str32, release release: Darwin.Str32) ``` |

Modified [PMLanguageInfo.level](https://developer.apple.com/documentation/applicationservices/pmlanguageinfo/1459988-level)

|  | Declaration |
| --- | --- |
| From | ``` var level: Str32 ``` |
| To | ``` var level: Darwin.Str32 ``` |

Modified [PMLanguageInfo.release](https://developer.apple.com/documentation/applicationservices/pmlanguageinfo/1459131-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: Str32 ``` |
| To | ``` var release: Darwin.Str32 ``` |

Modified [PMLanguageInfo.version](https://developer.apple.com/documentation/applicationservices/pmlanguageinfo/1459038-version)

|  | Declaration |
| --- | --- |
| From | ``` var version: Str32 ``` |
| To | ``` var version: Darwin.Str32 ``` |

Modified [ProcessInfoExtendedRec [struct]](https://developer.apple.com/documentation/applicationservices/processinfoextendedrec)

|  | Declaration |
| --- | --- |
| From | ``` struct ProcessInfoExtendedRec {     var processInfoLength: UInt32     var processName: StringPtr     var processNumber: ProcessSerialNumber     var processType: UInt32     var processSignature: OSType     var processMode: UInt32     var processLocation: Ptr     var processSize: UInt32     var processFreeMem: UInt32     var processLauncher: ProcessSerialNumber     var processLaunchDate: UInt32     var processActiveTime: UInt32     var processAppRef: FSRefPtr     var processTempMemTotal: UInt32     var processPurgeableTempMemTotal: UInt32     init()     init(processInfoLength processInfoLength: UInt32, processName processName: StringPtr, processNumber processNumber: ProcessSerialNumber, processType processType: UInt32, processSignature processSignature: OSType, processMode processMode: UInt32, processLocation processLocation: Ptr, processSize processSize: UInt32, processFreeMem processFreeMem: UInt32, processLauncher processLauncher: ProcessSerialNumber, processLaunchDate processLaunchDate: UInt32, processActiveTime processActiveTime: UInt32, processAppRef processAppRef: FSRefPtr, processTempMemTotal processTempMemTotal: UInt32, processPurgeableTempMemTotal processPurgeableTempMemTotal: UInt32) } ``` |
| To | ``` struct ProcessInfoExtendedRec {     var processInfoLength: UInt32     var processName: StringPtr!     var processNumber: ProcessSerialNumber     var processType: UInt32     var processSignature: OSType     var processMode: UInt32     var processLocation: Ptr!     var processSize: UInt32     var processFreeMem: UInt32     var processLauncher: ProcessSerialNumber     var processLaunchDate: UInt32     var processActiveTime: UInt32     var processAppRef: FSRefPtr!     var processTempMemTotal: UInt32     var processPurgeableTempMemTotal: UInt32     init()     init(processInfoLength processInfoLength: UInt32, processName processName: StringPtr!, processNumber processNumber: ProcessSerialNumber, processType processType: UInt32, processSignature processSignature: OSType, processMode processMode: UInt32, processLocation processLocation: Ptr!, processSize processSize: UInt32, processFreeMem processFreeMem: UInt32, processLauncher processLauncher: ProcessSerialNumber, processLaunchDate processLaunchDate: UInt32, processActiveTime processActiveTime: UInt32, processAppRef processAppRef: FSRefPtr!, processTempMemTotal processTempMemTotal: UInt32, processPurgeableTempMemTotal processPurgeableTempMemTotal: UInt32) } ``` |

Modified [ProcessInfoExtendedRec.processAppRef](https://developer.apple.com/documentation/applicationservices/processinfoextendedrec/1464388-processappref)

|  | Declaration |
| --- | --- |
| From | ``` var processAppRef: FSRefPtr ``` |
| To | ``` var processAppRef: FSRefPtr! ``` |

Modified [ProcessInfoExtendedRec.processLocation](https://developer.apple.com/documentation/applicationservices/processinfoextendedrec/1463684-processlocation)

|  | Declaration |
| --- | --- |
| From | ``` var processLocation: Ptr ``` |
| To | ``` var processLocation: Ptr! ``` |

Modified [ProcessInfoExtendedRec.processName](https://developer.apple.com/documentation/applicationservices/processinfoextendedrec/1462598-processname)

|  | Declaration |
| --- | --- |
| From | ``` var processName: StringPtr ``` |
| To | ``` var processName: StringPtr! ``` |

Modified [ProcessInfoRec [struct]](https://developer.apple.com/documentation/applicationservices/processinforec)

|  | Declaration |
| --- | --- |
| From | ``` struct ProcessInfoRec {     var processInfoLength: UInt32     var processName: StringPtr     var processNumber: ProcessSerialNumber     var processType: UInt32     var processSignature: OSType     var processMode: UInt32     var processLocation: Ptr     var processSize: UInt32     var processFreeMem: UInt32     var processLauncher: ProcessSerialNumber     var processLaunchDate: UInt32     var processActiveTime: UInt32     var processAppRef: FSRefPtr     init()     init(processInfoLength processInfoLength: UInt32, processName processName: StringPtr, processNumber processNumber: ProcessSerialNumber, processType processType: UInt32, processSignature processSignature: OSType, processMode processMode: UInt32, processLocation processLocation: Ptr, processSize processSize: UInt32, processFreeMem processFreeMem: UInt32, processLauncher processLauncher: ProcessSerialNumber, processLaunchDate processLaunchDate: UInt32, processActiveTime processActiveTime: UInt32, processAppRef processAppRef: FSRefPtr) } ``` |
| To | ``` struct ProcessInfoRec {     var processInfoLength: UInt32     var processName: StringPtr!     var processNumber: ProcessSerialNumber     var processType: UInt32     var processSignature: OSType     var processMode: UInt32     var processLocation: Ptr!     var processSize: UInt32     var processFreeMem: UInt32     var processLauncher: ProcessSerialNumber     var processLaunchDate: UInt32     var processActiveTime: UInt32     var processAppRef: FSRefPtr!     init()     init(processInfoLength processInfoLength: UInt32, processName processName: StringPtr!, processNumber processNumber: ProcessSerialNumber, processType processType: UInt32, processSignature processSignature: OSType, processMode processMode: UInt32, processLocation processLocation: Ptr!, processSize processSize: UInt32, processFreeMem processFreeMem: UInt32, processLauncher processLauncher: ProcessSerialNumber, processLaunchDate processLaunchDate: UInt32, processActiveTime processActiveTime: UInt32, processAppRef processAppRef: FSRefPtr!) } ``` |

Modified [ProcessInfoRec.processAppRef](https://developer.apple.com/documentation/applicationservices/processinforec/1461921-processappref)

|  | Declaration |
| --- | --- |
| From | ``` var processAppRef: FSRefPtr ``` |
| To | ``` var processAppRef: FSRefPtr! ``` |

Modified [ProcessInfoRec.processLocation](https://developer.apple.com/documentation/applicationservices/processinforec/1462868-processlocation)

|  | Declaration |
| --- | --- |
| From | ``` var processLocation: Ptr ``` |
| To | ``` var processLocation: Ptr! ``` |

Modified [ProcessInfoRec.processName](https://developer.apple.com/documentation/applicationservices/processinforec/1462097-processname)

|  | Declaration |
| --- | --- |
| From | ``` var processName: StringPtr ``` |
| To | ``` var processName: StringPtr! ``` |

Modified [VDGammaRecord [struct]](https://developer.apple.com/documentation/applicationservices/vdgammarecord)

|  | Declaration |
| --- | --- |
| From | ``` struct VDGammaRecord {     var csGTable: Ptr     init()     init(csGTable csGTable: Ptr) } ``` |
| To | ``` struct VDGammaRecord {     var csGTable: Ptr!     init()     init(csGTable csGTable: Ptr!) } ``` |

Modified [VDGammaRecord.csGTable](https://developer.apple.com/documentation/applicationservices/vdgammarecord/1458775-csgtable)

|  | Declaration |
| --- | --- |
| From | ``` var csGTable: Ptr ``` |
| To | ``` var csGTable: Ptr! ``` |

Modified [VoiceDescription [struct]](https://developer.apple.com/documentation/applicationservices/voicedescription)

|  | Declaration |
| --- | --- |
| From | ``` struct VoiceDescription {     var length: Int32     var voice: VoiceSpec     var version: Int32     var name: Str63     var comment: Str255     var gender: Int16     var age: Int16     var script: Int16     var language: Int16     var region: Int16     var reserved: (Int32, Int32, Int32, Int32)     init()     init(length length: Int32, voice voice: VoiceSpec, version version: Int32, name name: Str63, comment comment: Str255, gender gender: Int16, age age: Int16, script script: Int16, language language: Int16, region region: Int16, reserved reserved: (Int32, Int32, Int32, Int32)) } ``` |
| To | ``` struct VoiceDescription {     var length: Int32     var voice: VoiceSpec     var version: Int32     var name: Darwin.Str63     var comment: Darwin.Str255     var gender: Int16     var age: Int16     var script: Int16     var language: Int16     var region: Int16     var reserved: (Int32, Int32, Int32, Int32)     init()     init(length length: Int32, voice voice: VoiceSpec, version version: Int32, name name: Darwin.Str63, comment comment: Darwin.Str255, gender gender: Int16, age age: Int16, script script: Int16, language language: Int16, region region: Int16, reserved reserved: (Int32, Int32, Int32, Int32)) } ``` |

Modified [VoiceDescription.comment](https://developer.apple.com/documentation/applicationservices/voicedescription/1461098-comment)

|  | Declaration |
| --- | --- |
| From | ``` var comment: Str255 ``` |
| To | ``` var comment: Darwin.Str255 ``` |

Modified [VoiceDescription.init(length: Int32, voice: VoiceSpec, version: Int32, name: Darwin.Str63, comment: Darwin.Str255, gender: Int16, age: Int16, script: Int16, language: Int16, region: Int16, reserved: (Int32, Int32, Int32, Int32))](https://developer.apple.com/documentation/applicationservices/voicedescription/1463154-init)

|  | Declaration |
| --- | --- |
| From | ``` init(length length: Int32, voice voice: VoiceSpec, version version: Int32, name name: Str63, comment comment: Str255, gender gender: Int16, age age: Int16, script script: Int16, language language: Int16, region region: Int16, reserved reserved: (Int32, Int32, Int32, Int32)) ``` |
| To | ``` init(length length: Int32, voice voice: VoiceSpec, version version: Int32, name name: Darwin.Str63, comment comment: Darwin.Str255, gender gender: Int16, age age: Int16, script script: Int16, language language: Int16, region region: Int16, reserved reserved: (Int32, Int32, Int32, Int32)) ``` |

Modified [VoiceDescription.name](https://developer.apple.com/documentation/applicationservices/voicedescription/1459756-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: Str63 ``` |
| To | ``` var name: Darwin.Str63 ``` |

Modified [ATSCubicClosePathProcPtr](https://developer.apple.com/documentation/applicationservices/atscubicclosepathprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicClosePathProcPtr = (UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSCubicClosePathProcPtr = (UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSCubicClosePathUPP](https://developer.apple.com/documentation/applicationservices/atscubicclosepathupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicClosePathUPP = ATSCubicClosePathProcPtr ``` |
| To | ``` typealias ATSCubicClosePathUPP = ApplicationServices.ATSCubicClosePathProcPtr ``` |

Modified [ATSCubicCurveToProcPtr](https://developer.apple.com/documentation/applicationservices/atscubiccurvetoprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicCurveToProcPtr = (UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSCubicCurveToProcPtr = (UnsafePointer<Float32Point>?, UnsafePointer<Float32Point>?, UnsafePointer<Float32Point>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSCubicCurveToUPP](https://developer.apple.com/documentation/applicationservices/atscubiccurvetoupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicCurveToUPP = ATSCubicCurveToProcPtr ``` |
| To | ``` typealias ATSCubicCurveToUPP = ApplicationServices.ATSCubicCurveToProcPtr ``` |

Modified [ATSCubicLineToProcPtr](https://developer.apple.com/documentation/applicationservices/atscubiclinetoprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicLineToProcPtr = (UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSCubicLineToProcPtr = (UnsafePointer<Float32Point>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSCubicLineToUPP](https://developer.apple.com/documentation/applicationservices/atscubiclinetoupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicLineToUPP = ATSCubicLineToProcPtr ``` |
| To | ``` typealias ATSCubicLineToUPP = ApplicationServices.ATSCubicLineToProcPtr ``` |

Modified [ATSCubicMoveToProcPtr](https://developer.apple.com/documentation/applicationservices/atscubicmovetoprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicMoveToProcPtr = (UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSCubicMoveToProcPtr = (UnsafePointer<Float32Point>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSCubicMoveToUPP](https://developer.apple.com/documentation/applicationservices/atscubicmovetoupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicMoveToUPP = ATSCubicMoveToProcPtr ``` |
| To | ``` typealias ATSCubicMoveToUPP = ApplicationServices.ATSCubicMoveToProcPtr ``` |

Modified [ATSFontApplierFunction](https://developer.apple.com/documentation/applicationservices/atsfontapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontApplierFunction = (ATSFontRef, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSFontApplierFunction = (ATSFontRef, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSFontFamilyApplierFunction](https://developer.apple.com/documentation/applicationservices/atsfontfamilyapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontFamilyApplierFunction = (ATSFontFamilyRef, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSFontFamilyApplierFunction = (ATSFontFamilyRef, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSFontFamilyIterator](https://developer.apple.com/documentation/applicationservices/atsfontfamilyiterator)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontFamilyIterator = COpaquePointer ``` |
| To | ``` typealias ATSFontFamilyIterator = OpaquePointer ``` |

Modified [ATSFontIterator](https://developer.apple.com/documentation/applicationservices/atsfontiterator)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontIterator = COpaquePointer ``` |
| To | ``` typealias ATSFontIterator = OpaquePointer ``` |

Modified [ATSFontNotificationInfoRef](https://developer.apple.com/documentation/applicationservices/atsfontnotificationinforef)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontNotificationInfoRef = COpaquePointer ``` |
| To | ``` typealias ATSFontNotificationInfoRef = OpaquePointer ``` |

Modified [ATSFontNotificationRef](https://developer.apple.com/documentation/applicationservices/atsfontnotificationref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontNotificationRef = COpaquePointer ``` |
| To | ``` typealias ATSFontNotificationRef = OpaquePointer ``` |

Modified [ATSFontQueryCallback](https://developer.apple.com/documentation/applicationservices/atsfontquerycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontQueryCallback = (ATSFontQueryMessageID, CFPropertyList!, UnsafeMutablePointer<Void>) -> Unmanaged<CFPropertyList>! ``` |
| To | ``` typealias ATSFontQueryCallback = (ATSFontQueryMessageID, CFPropertyList?, UnsafeMutableRawPointer?) -> Unmanaged<CFPropertyList>? ``` |

Modified [ATSNotificationCallback](https://developer.apple.com/documentation/applicationservices/atsnotificationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSNotificationCallback = (ATSFontNotificationInfoRef, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias ATSNotificationCallback = (ATSFontNotificationInfoRef?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [ATSQuadraticClosePathProcPtr](https://developer.apple.com/documentation/applicationservices/atsquadraticclosepathprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticClosePathProcPtr = (UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSQuadraticClosePathProcPtr = (UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSQuadraticClosePathUPP](https://developer.apple.com/documentation/applicationservices/atsquadraticclosepathupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticClosePathUPP = ATSQuadraticClosePathProcPtr ``` |
| To | ``` typealias ATSQuadraticClosePathUPP = ApplicationServices.ATSQuadraticClosePathProcPtr ``` |

Modified [ATSQuadraticCurveProcPtr](https://developer.apple.com/documentation/applicationservices/atsquadraticcurveprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticCurveProcPtr = (UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSQuadraticCurveProcPtr = (UnsafePointer<Float32Point>?, UnsafePointer<Float32Point>?, UnsafePointer<Float32Point>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSQuadraticCurveUPP](https://developer.apple.com/documentation/applicationservices/atsquadraticcurveupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticCurveUPP = ATSQuadraticCurveProcPtr ``` |
| To | ``` typealias ATSQuadraticCurveUPP = ApplicationServices.ATSQuadraticCurveProcPtr ``` |

Modified [ATSQuadraticLineProcPtr](https://developer.apple.com/documentation/applicationservices/atsquadraticlineprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticLineProcPtr = (UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSQuadraticLineProcPtr = (UnsafePointer<Float32Point>?, UnsafePointer<Float32Point>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSQuadraticLineUPP](https://developer.apple.com/documentation/applicationservices/atsquadraticlineupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticLineUPP = ATSQuadraticLineProcPtr ``` |
| To | ``` typealias ATSQuadraticLineUPP = ApplicationServices.ATSQuadraticLineProcPtr ``` |

Modified [ATSQuadraticNewPathProcPtr](https://developer.apple.com/documentation/applicationservices/atsquadraticnewpathprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticNewPathProcPtr = (UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias ATSQuadraticNewPathProcPtr = (UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [ATSQuadraticNewPathUPP](https://developer.apple.com/documentation/applicationservices/atsquadraticnewpathupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticNewPathUPP = ATSQuadraticNewPathProcPtr ``` |
| To | ``` typealias ATSQuadraticNewPathUPP = ApplicationServices.ATSQuadraticNewPathProcPtr ``` |

Modified [ATSUAttributeValuePtr](https://developer.apple.com/documentation/applicationservices/atsuattributevalueptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUAttributeValuePtr = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias ATSUAttributeValuePtr = UnsafeMutableRawPointer ``` |

Modified [ATSUDirectLayoutOperationOverrideProcPtr](https://developer.apple.com/documentation/applicationservices/atsudirectlayoutoperationoverrideprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUDirectLayoutOperationOverrideProcPtr = (ATSULayoutOperationSelector, ATSULineRef, URefCon, UnsafeMutablePointer<Void>, UnsafeMutablePointer<ATSULayoutOperationCallbackStatus>) -> OSStatus ``` |
| To | ``` typealias ATSUDirectLayoutOperationOverrideProcPtr = (ATSULayoutOperationSelector, ATSULineRef?, URefCon?, UnsafeMutableRawPointer?, UnsafeMutablePointer<ATSULayoutOperationCallbackStatus>?) -> OSStatus ``` |

Modified [ATSUDirectLayoutOperationOverrideUPP](https://developer.apple.com/documentation/applicationservices/atsudirectlayoutoperationoverrideupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUDirectLayoutOperationOverrideUPP = ATSUDirectLayoutOperationOverrideProcPtr ``` |
| To | ``` typealias ATSUDirectLayoutOperationOverrideUPP = ApplicationServices.ATSUDirectLayoutOperationOverrideProcPtr ``` |

Modified [ATSUFontFallbacks](https://developer.apple.com/documentation/applicationservices/atsufontfallbacks)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUFontFallbacks = COpaquePointer ``` |
| To | ``` typealias ATSUFontFallbacks = OpaquePointer ``` |

Modified [ATSULineRef](https://developer.apple.com/documentation/applicationservices/atsulineref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSULineRef = COpaquePointer ``` |
| To | ``` typealias ATSULineRef = OpaquePointer ``` |

Modified [ATSUStyle](https://developer.apple.com/documentation/applicationservices/atsustyle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUStyle = COpaquePointer ``` |
| To | ``` typealias ATSUStyle = OpaquePointer ``` |

Modified [ATSUStyleSettingRef](https://developer.apple.com/documentation/applicationservices/atsustylesettingref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUStyleSettingRef = COpaquePointer ``` |
| To | ``` typealias ATSUStyleSettingRef = OpaquePointer ``` |

Modified [ATSUTextLayout](https://developer.apple.com/documentation/applicationservices/atsutextlayout)

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUTextLayout = COpaquePointer ``` |
| To | ``` typealias ATSUTextLayout = OpaquePointer ``` |

Modified [AXObserverAddNotification(_: AXObserver, _: AXUIElement, _: CFString, _: UnsafeMutableRawPointer?) -> AXError](https://developer.apple.com/documentation/applicationservices/1462089-axobserveraddnotification)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverAddNotification(_ observer: AXObserver, _ element: AXUIElement, _ notification: CFString, _ refcon: UnsafeMutablePointer<Void>) -> AXError ``` |
| To | ``` func AXObserverAddNotification(_ observer: AXObserver, _ element: AXUIElement, _ notification: CFString, _ refcon: UnsafeMutableRawPointer?) -> AXError ``` |

Modified [AXObserverCallback](https://developer.apple.com/documentation/applicationservices/axobservercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AXObserverCallback = (AXObserver, AXUIElement, CFString, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias AXObserverCallback = (AXObserver, AXUIElement, CFString, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [AXObserverCallbackWithInfo](https://developer.apple.com/documentation/applicationservices/axobservercallbackwithinfo)

|  | Declaration |
| --- | --- |
| From | ``` typealias AXObserverCallbackWithInfo = (AXObserver, AXUIElement, CFString, CFDictionary, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias AXObserverCallbackWithInfo = (AXObserver, AXUIElement, CFString, CFDictionary, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [AXObserverCreate(_: pid_t, _: ApplicationServices.AXObserverCallback, _: UnsafeMutablePointer<AXObserver?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1460133-axobservercreate)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverCreate(_ application: pid_t, _ callback: AXObserverCallback, _ outObserver: UnsafeMutablePointer<AXObserver?>) -> AXError ``` |
| To | ``` func AXObserverCreate(_ application: pid_t, _ callback: ApplicationServices.AXObserverCallback, _ outObserver: UnsafeMutablePointer<AXObserver?>) -> AXError ``` |

Modified [AXObserverCreateWithInfoCallback(_: pid_t, _: ApplicationServices.AXObserverCallbackWithInfo, _: UnsafeMutablePointer<AXObserver?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1460610-axobservercreatewithinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverCreateWithInfoCallback(_ application: pid_t, _ callback: AXObserverCallbackWithInfo, _ outObserver: UnsafeMutablePointer<AXObserver?>) -> AXError ``` |
| To | ``` func AXObserverCreateWithInfoCallback(_ application: pid_t, _ callback: ApplicationServices.AXObserverCallbackWithInfo, _ outObserver: UnsafeMutablePointer<AXObserver?>) -> AXError ``` |

Modified [AXObserverGetRunLoopSource(_: AXObserver) -> CFRunLoopSource](https://developer.apple.com/documentation/applicationservices/1459139-axobservergetrunloopsource)

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverGetRunLoopSource(_ observer: AXObserver) -> Unmanaged<CFRunLoopSource> ``` |
| To | ``` func AXObserverGetRunLoopSource(_ observer: AXObserver) -> CFRunLoopSource ``` |

Modified [AXUIElementCopyAttributeValue(_: AXUIElement, _: CFString, _: UnsafeMutablePointer<CFTypeRef?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1462085-axuielementcopyattributevalue)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyAttributeValue(_ element: AXUIElement, _ attribute: CFString, _ value: UnsafeMutablePointer<AnyObject?>) -> AXError ``` |
| To | ``` func AXUIElementCopyAttributeValue(_ element: AXUIElement, _ attribute: CFString, _ value: UnsafeMutablePointer<CFTypeRef?>) -> AXError ``` |

Modified [AXUIElementCopyParameterizedAttributeValue(_: AXUIElement, _: CFString, _: CFTypeRef, _: UnsafeMutablePointer<CFTypeRef?>) -> AXError](https://developer.apple.com/documentation/applicationservices/1461203-axuielementcopyparameterizedattr)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyParameterizedAttributeValue(_ element: AXUIElement, _ parameterizedAttribute: CFString, _ parameter: AnyObject, _ result: UnsafeMutablePointer<AnyObject?>) -> AXError ``` |
| To | ``` func AXUIElementCopyParameterizedAttributeValue(_ element: AXUIElement, _ parameterizedAttribute: CFString, _ parameter: CFTypeRef, _ result: UnsafeMutablePointer<CFTypeRef?>) -> AXError ``` |

Modified [AXUIElementCreateApplication(_: pid_t) -> AXUIElement](https://developer.apple.com/documentation/applicationservices/1459374-axuielementcreateapplication)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCreateApplication(_ pid: pid_t) -> Unmanaged<AXUIElement> ``` |
| To | ``` func AXUIElementCreateApplication(_ pid: pid_t) -> AXUIElement ``` |

Modified [AXUIElementCreateSystemWide() -> AXUIElement](https://developer.apple.com/documentation/applicationservices/1462095-axuielementcreatesystemwide)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCreateSystemWide() -> Unmanaged<AXUIElement> ``` |
| To | ``` func AXUIElementCreateSystemWide() -> AXUIElement ``` |

Modified [AXUIElementSetAttributeValue(_: AXUIElement, _: CFString, _: CFTypeRef) -> AXError](https://developer.apple.com/documentation/applicationservices/1460434-axuielementsetattributevalue)

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementSetAttributeValue(_ element: AXUIElement, _ attribute: CFString, _ value: AnyObject) -> AXError ``` |
| To | ``` func AXUIElementSetAttributeValue(_ element: AXUIElement, _ attribute: CFString, _ value: CFTypeRef) -> AXError ``` |

Modified [AXValueCreate(_: AXValueType, _: UnsafeRawPointer) -> AXValue?](https://developer.apple.com/documentation/applicationservices/1459351-axvaluecreate)

|  | Declaration |
| --- | --- |
| From | ``` func AXValueCreate(_ theType: AXValueType, _ valuePtr: UnsafePointer<Void>) -> Unmanaged<AXValue>? ``` |
| To | ``` func AXValueCreate(_ theType: AXValueType, _ valuePtr: UnsafeRawPointer) -> AXValue? ``` |

Modified [AXValueGetValue(_: AXValue, _: AXValueType, _: UnsafeMutableRawPointer) -> Bool](https://developer.apple.com/documentation/applicationservices/1462933-axvaluegetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func AXValueGetValue(_ value: AXValue, _ theType: AXValueType, _ valuePtr: UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` func AXValueGetValue(_ value: AXValue, _ theType: AXValueType, _ valuePtr: UnsafeMutableRawPointer) -> Bool ``` |

Modified [BitMapHandle](https://developer.apple.com/documentation/applicationservices/bitmaphandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias BitMapHandle = UnsafeMutablePointer<BitMapPtr> ``` |
| To | ``` typealias BitMapHandle = UnsafeMutablePointer<BitMapPtr?> ``` |

Modified [CMFlattenProcPtr](https://developer.apple.com/documentation/applicationservices/cmflattenprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMFlattenProcPtr = (Int32, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSErr ``` |
| To | ``` typealias CMFlattenProcPtr = (Int32, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSErr ``` |

Modified [CMFlattenUPP](https://developer.apple.com/documentation/applicationservices/cmflattenupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMFlattenUPP = CMFlattenProcPtr ``` |
| To | ``` typealias CMFlattenUPP = ApplicationServices.CMFlattenProcPtr ``` |

Modified [CMMApplyTransformProc](https://developer.apple.com/documentation/colorsync/cmmapplytransformproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMApplyTransformProc = (ColorSyncTransform!, Int, Int, Int, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, ColorSyncDataDepth, ColorSyncDataLayout, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary!) -> Bool ``` |
| To | ``` typealias CMMApplyTransformProc = (ColorSyncTransform?, Int, Int, Int, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, ColorSyncDataDepth, ColorSyncDataLayout, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool ``` |

Modified [CMMCreateTransformPropertyProc](https://developer.apple.com/documentation/colorsync/cmmcreatetransformpropertyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMCreateTransformPropertyProc = (ColorSyncTransform!, AnyObject!, CFDictionary!) -> Unmanaged<AnyObject>! ``` |
| To | ``` typealias CMMCreateTransformPropertyProc = (ColorSyncTransform?, CFTypeRef?, CFDictionary?) -> Unmanaged<CFTypeRef>? ``` |

Modified [CMMInitializeLinkProfileProc](https://developer.apple.com/documentation/colorsync/cmminitializelinkprofileproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMInitializeLinkProfileProc = (ColorSyncMutableProfile!, CFArray!, CFDictionary!) -> Bool ``` |
| To | ``` typealias CMMInitializeLinkProfileProc = (ColorSyncMutableProfile?, CFArray?, CFDictionary?) -> Bool ``` |

Modified [CMMInitializeTransformProc](https://developer.apple.com/documentation/colorsync/cmminitializetransformproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMInitializeTransformProc = (ColorSyncTransform!, CFArray!, CFDictionary!) -> Bool ``` |
| To | ``` typealias CMMInitializeTransformProc = (ColorSyncTransform?, CFArray?, CFDictionary?) -> Bool ``` |

Modified [ColorComplementProcPtr](https://developer.apple.com/documentation/applicationservices/colorcomplementprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorComplementProcPtr = (UnsafeMutablePointer<RGBColor>) -> DarwinBoolean ``` |
| To | ``` typealias ColorComplementProcPtr = (UnsafeMutablePointer<RGBColor>?) -> DarwinBoolean ``` |

Modified [ColorComplementUPP](https://developer.apple.com/documentation/applicationservices/colorcomplementupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorComplementUPP = ColorComplementProcPtr ``` |
| To | ``` typealias ColorComplementUPP = ApplicationServices.ColorComplementProcPtr ``` |

Modified [ColorSearchProcPtr](https://developer.apple.com/documentation/applicationservices/colorsearchprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSearchProcPtr = (UnsafeMutablePointer<RGBColor>, UnsafeMutablePointer<Int>) -> DarwinBoolean ``` |
| To | ``` typealias ColorSearchProcPtr = (UnsafeMutablePointer<RGBColor>?, UnsafeMutablePointer<Int>?) -> DarwinBoolean ``` |

Modified [ColorSearchUPP](https://developer.apple.com/documentation/applicationservices/colorsearchupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSearchUPP = ColorSearchProcPtr ``` |
| To | ``` typealias ColorSearchUPP = ApplicationServices.ColorSearchProcPtr ``` |

Modified [ColorSyncCMMIterateCallback](https://developer.apple.com/documentation/colorsync/colorsynccmmiteratecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncCMMIterateCallback = (ColorSyncCMM!, UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` typealias ColorSyncCMMIterateCallback = (ColorSyncCMM?, UnsafeMutableRawPointer?) -> Bool ``` |

Modified [ColorSyncDeviceProfileIterateCallback](https://developer.apple.com/documentation/colorsync/colorsyncdeviceprofileiteratecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncDeviceProfileIterateCallback = (CFDictionary!, UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` typealias ColorSyncDeviceProfileIterateCallback = (CFDictionary?, UnsafeMutableRawPointer?) -> Bool ``` |

Modified [ColorSyncIterateDeviceProfiles(_: ApplicationServices.ColorSyncDeviceProfileIterateCallback!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/colorsync/1460141-colorsynciteratedeviceprofiles)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateDeviceProfiles(_ callBack: ColorSyncDeviceProfileIterateCallback!, _ userInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ColorSyncIterateDeviceProfiles(_ callBack: ApplicationServices.ColorSyncDeviceProfileIterateCallback!, _ userInfo: UnsafeMutableRawPointer!) ``` |

Modified [ColorSyncIterateInstalledCMMs(_: ApplicationServices.ColorSyncCMMIterateCallback!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/colorsync/1462477-colorsynciterateinstalledcmms)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateInstalledCMMs(_ callBack: ColorSyncCMMIterateCallback!, _ userInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ColorSyncIterateInstalledCMMs(_ callBack: ApplicationServices.ColorSyncCMMIterateCallback!, _ userInfo: UnsafeMutableRawPointer!) ``` |

Modified [ColorSyncIterateInstalledProfiles(_: ApplicationServices.ColorSyncProfileIterateCallback!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!)](https://developer.apple.com/documentation/colorsync/1463359-colorsynciterateinstalledprofile)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateInstalledProfiles(_ callBack: ColorSyncProfileIterateCallback!, _ seed: UnsafeMutablePointer<UInt32>, _ userInfo: UnsafeMutablePointer<Void>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) ``` |
| To | ``` func ColorSyncIterateInstalledProfiles(_ callBack: ApplicationServices.ColorSyncProfileIterateCallback!, _ seed: UnsafeMutablePointer<UInt32>!, _ userInfo: UnsafeMutableRawPointer!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) ``` |

Modified [ColorSyncProfileCopyData(_: ColorSyncProfile!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/colorsync/1461594-colorsyncprofilecopydata)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileCopyData(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func ColorSyncProfileCopyData(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>! ``` |

Modified [ColorSyncProfileCreate(_: CFData!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ColorSyncProfile>!](https://developer.apple.com/documentation/colorsync/1462094-colorsyncprofilecreate)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileCreate(_ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ColorSyncProfile>! ``` |
| To | ``` func ColorSyncProfileCreate(_ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ColorSyncProfile>! ``` |

Modified [ColorSyncProfileCreateDeviceProfile(_: CFString!, _: CFUUID!, _: CFTypeRef!) -> Unmanaged<ColorSyncProfile>!](https://developer.apple.com/documentation/colorsync/1463374-colorsyncprofilecreatedeviceprof)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileCreateDeviceProfile(_ deviceClass: CFString!, _ deviceID: CFUUID!, _ profileID: AnyObject!) -> Unmanaged<ColorSyncProfile>! ``` |
| To | ``` func ColorSyncProfileCreateDeviceProfile(_ deviceClass: CFString!, _ deviceID: CFUUID!, _ profileID: CFTypeRef!) -> Unmanaged<ColorSyncProfile>! ``` |

Modified [ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_: ColorSyncProfile!, _: UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/colorsync/1463186-colorsyncprofilecreatedisplaytra)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_ profile: ColorSyncProfile!, _ nSamplesPerChannel: UnsafeMutablePointer<Int>) -> Unmanaged<CFData>! ``` |
| To | ``` func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_ profile: ColorSyncProfile!, _ nSamplesPerChannel: UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>! ``` |

Modified [ColorSyncProfileCreateWithURL(_: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ColorSyncProfile>!](https://developer.apple.com/documentation/colorsync/1458999-colorsyncprofilecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileCreateWithURL(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ColorSyncProfile>! ``` |
| To | ``` func ColorSyncProfileCreateWithURL(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ColorSyncProfile>! ``` |

Modified [ColorSyncProfileEstimateGamma(_: ColorSyncProfile!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Float](https://developer.apple.com/documentation/colorsync/1464019-colorsyncprofileestimategamma)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileEstimateGamma(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Float ``` |
| To | ``` func ColorSyncProfileEstimateGamma(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Float ``` |

Modified [ColorSyncProfileEstimateGammaWithDisplayID(_: Int32, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Float](https://developer.apple.com/documentation/colorsync/1461168-colorsyncprofileestimategammawit)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileEstimateGammaWithDisplayID(_ displayID: Int32, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Float ``` |
| To | ``` func ColorSyncProfileEstimateGammaWithDisplayID(_ displayID: Int32, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Float ``` |

Modified [ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_: ColorSyncProfile!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!) -> Bool](https://developer.apple.com/documentation/colorsync/1459197-colorsyncprofilegetdisplaytransf)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_ profile: ColorSyncProfile!, _ redMin: UnsafeMutablePointer<Float>, _ redMax: UnsafeMutablePointer<Float>, _ redGamma: UnsafeMutablePointer<Float>, _ greenMin: UnsafeMutablePointer<Float>, _ greenMax: UnsafeMutablePointer<Float>, _ greenGamma: UnsafeMutablePointer<Float>, _ blueMin: UnsafeMutablePointer<Float>, _ blueMax: UnsafeMutablePointer<Float>, _ blueGamma: UnsafeMutablePointer<Float>) -> Bool ``` |
| To | ``` func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_ profile: ColorSyncProfile!, _ redMin: UnsafeMutablePointer<Float>!, _ redMax: UnsafeMutablePointer<Float>!, _ redGamma: UnsafeMutablePointer<Float>!, _ greenMin: UnsafeMutablePointer<Float>!, _ greenMax: UnsafeMutablePointer<Float>!, _ greenGamma: UnsafeMutablePointer<Float>!, _ blueMin: UnsafeMutablePointer<Float>!, _ blueMax: UnsafeMutablePointer<Float>!, _ blueGamma: UnsafeMutablePointer<Float>!) -> Bool ``` |

Modified [ColorSyncProfileGetURL(_: ColorSyncProfile!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](https://developer.apple.com/documentation/colorsync/1464063-colorsyncprofilegeturl)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileGetURL(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func ColorSyncProfileGetURL(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>! ``` |

Modified [ColorSyncProfileInstall(_: ColorSyncProfile!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/colorsync/1463116-colorsyncprofileinstall)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileInstall(_ profile: ColorSyncProfile!, _ domain: CFString!, _ subpath: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ColorSyncProfileInstall(_ profile: ColorSyncProfile!, _ domain: CFString!, _ subpath: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ColorSyncProfileIterateCallback](https://developer.apple.com/documentation/colorsync/colorsyncprofileiteratecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncProfileIterateCallback = (CFDictionary!, UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` typealias ColorSyncProfileIterateCallback = (CFDictionary?, UnsafeMutableRawPointer?) -> Bool ``` |

Modified [ColorSyncProfileUninstall(_: ColorSyncProfile!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/colorsync/1458805-colorsyncprofileuninstall)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileUninstall(_ profile: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ColorSyncProfileUninstall(_ profile: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ColorSyncProfileVerify(_: ColorSyncProfile!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/colorsync/1459719-colorsyncprofileverify)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileVerify(_ prof: ColorSyncProfile!, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>, _ warnings: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ColorSyncProfileVerify(_ prof: ColorSyncProfile!, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>!, _ warnings: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ColorSyncTransformConvert(_: ColorSyncTransform!, _: Int, _: Int, _: UnsafeMutableRawPointer!, _: ColorSyncDataDepth, _: ColorSyncDataLayout, _: Int, _: UnsafeRawPointer!, _: ColorSyncDataDepth, _: ColorSyncDataLayout, _: Int, _: CFDictionary!) -> Bool](https://developer.apple.com/documentation/colorsync/1459813-colorsynctransformconvert)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncTransformConvert(_ transform: ColorSyncTransform!, _ width: Int, _ height: Int, _ dst: UnsafeMutablePointer<Void>, _ dstDepth: ColorSyncDataDepth, _ dstLayout: ColorSyncDataLayout, _ dstBytesPerRow: Int, _ src: UnsafePointer<Void>, _ srcDepth: ColorSyncDataDepth, _ srcLayout: ColorSyncDataLayout, _ srcBytesPerRow: Int, _ options: CFDictionary!) -> Bool ``` |
| To | ``` func ColorSyncTransformConvert(_ transform: ColorSyncTransform!, _ width: Int, _ height: Int, _ dst: UnsafeMutableRawPointer!, _ dstDepth: ColorSyncDataDepth, _ dstLayout: ColorSyncDataLayout, _ dstBytesPerRow: Int, _ src: UnsafeRawPointer!, _ srcDepth: ColorSyncDataDepth, _ srcLayout: ColorSyncDataLayout, _ srcBytesPerRow: Int, _ options: CFDictionary!) -> Bool ``` |

Modified [ColorSyncTransformCopyProperty(_: ColorSyncTransform!, _: CFTypeRef!, _: CFDictionary!) -> Unmanaged<CFTypeRef>!](https://developer.apple.com/documentation/colorsync/1462866-colorsynctransformcopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncTransformCopyProperty(_ transform: ColorSyncTransform!, _ key: AnyObject!, _ options: CFDictionary!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func ColorSyncTransformCopyProperty(_ transform: ColorSyncTransform!, _ key: CFTypeRef!, _ options: CFDictionary!) -> Unmanaged<CFTypeRef>! ``` |

Modified [ColorSyncTransformSetProperty(_: ColorSyncTransform!, _: CFTypeRef!, _: CFTypeRef!)](https://developer.apple.com/documentation/colorsync/1458899-colorsynctransformsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncTransformSetProperty(_ transform: ColorSyncTransform!, _ key: AnyObject!, _ property: AnyObject!) ``` |
| To | ``` func ColorSyncTransformSetProperty(_ transform: ColorSyncTransform!, _ key: CFTypeRef!, _ property: CFTypeRef!) ``` |

Modified [ConstATSUAttributeValuePtr](https://developer.apple.com/documentation/applicationservices/constatsuattributevalueptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias ConstATSUAttributeValuePtr = UnsafePointer<Void> ``` |
| To | ``` typealias ConstATSUAttributeValuePtr = UnsafeRawPointer ``` |

Modified [CopySpeechProperty(_: SpeechChannel, _: CFString, _: UnsafeMutablePointer<CFTypeRef?>) -> OSErr](https://developer.apple.com/documentation/applicationservices/1459075-copyspeechproperty)

|  | Declaration |
| --- | --- |
| From | ``` func CopySpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: UnsafeMutablePointer<AnyObject?>) -> OSErr ``` |
| To | ``` func CopySpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: UnsafeMutablePointer<CFTypeRef?>) -> OSErr ``` |

Modified CTabHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias CTabHandle = UnsafeMutablePointer<CTabPtr> ``` |
| To | ``` typealias CTabHandle = UnsafeMutablePointer<CTabPtr?> ``` |

Modified [DCMFoundRecordIterator](https://developer.apple.com/documentation/applicationservices/dcmfoundrecorditerator)

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMFoundRecordIterator = COpaquePointer ``` |
| To | ``` typealias DCMFoundRecordIterator = OpaquePointer ``` |

Modified [DCMObjectID](https://developer.apple.com/documentation/applicationservices/dcmobjectid)

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMObjectID = COpaquePointer ``` |
| To | ``` typealias DCMObjectID = OpaquePointer ``` |

Modified [DCMObjectIterator](https://developer.apple.com/documentation/applicationservices/dcmobjectiterator)

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMObjectIterator = COpaquePointer ``` |
| To | ``` typealias DCMObjectIterator = OpaquePointer ``` |

Modified [DCMObjectRef](https://developer.apple.com/documentation/applicationservices/dcmobjectref)

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMObjectRef = COpaquePointer ``` |
| To | ``` typealias DCMObjectRef = OpaquePointer ``` |

Modified [DCMProgressFilterUPP](https://developer.apple.com/documentation/applicationservices/dcmprogressfilterupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMProgressFilterUPP = DCMProgressFilterProcPtr ``` |
| To | ``` typealias DCMProgressFilterUPP = ApplicationServices.DCMProgressFilterProcPtr ``` |

Modified DialogPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DialogPtr = COpaquePointer ``` |
| To | ``` typealias DialogPtr = OpaquePointer ``` |

Modified [DisposeIconActionUPP(_: ApplicationServices.IconActionUPP!)](https://developer.apple.com/documentation/applicationservices/1461028-disposeiconactionupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeIconActionUPP(_ userUPP: IconActionUPP!) ``` |
| To | ``` func DisposeIconActionUPP(_ userUPP: ApplicationServices.IconActionUPP!) ``` |

Modified [DisposeIconGetterUPP(_: ApplicationServices.IconGetterUPP!)](https://developer.apple.com/documentation/applicationservices/1461061-disposeicongetterupp)

|  | Declaration |
| --- | --- |
| From | ``` func DisposeIconGetterUPP(_ userUPP: IconGetterUPP!) ``` |
| To | ``` func DisposeIconGetterUPP(_ userUPP: ApplicationServices.IconGetterUPP!) ``` |

Modified [DragGrayRgnProcPtr](https://developer.apple.com/documentation/applicationservices/draggrayrgnprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias DragGrayRgnProcPtr = () -> Void ``` |
| To | ``` typealias DragGrayRgnProcPtr = () -> Swift.Void ``` |

Modified [DragGrayRgnUPP](https://developer.apple.com/documentation/applicationservices/draggrayrgnupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias DragGrayRgnUPP = DragGrayRgnProcPtr ``` |
| To | ``` typealias DragGrayRgnUPP = ApplicationServices.DragGrayRgnProcPtr ``` |

Modified [FMFontCallbackFilterProcPtr](https://developer.apple.com/documentation/applicationservices/fmfontcallbackfilterprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias FMFontCallbackFilterProcPtr = (FMFont, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias FMFontCallbackFilterProcPtr = (FMFont, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [FMFontCallbackFilterUPP](https://developer.apple.com/documentation/applicationservices/fmfontcallbackfilterupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias FMFontCallbackFilterUPP = FMFontCallbackFilterProcPtr ``` |
| To | ``` typealias FMFontCallbackFilterUPP = ApplicationServices.FMFontCallbackFilterProcPtr ``` |

Modified [FMFontFamilyCallbackFilterProcPtr](https://developer.apple.com/documentation/applicationservices/fmfontfamilycallbackfilterprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias FMFontFamilyCallbackFilterProcPtr = (FMFontFamily, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias FMFontFamilyCallbackFilterProcPtr = (FMFontFamily, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [FMFontFamilyCallbackFilterUPP](https://developer.apple.com/documentation/applicationservices/fmfontfamilycallbackfilterupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias FMFontFamilyCallbackFilterUPP = FMFontFamilyCallbackFilterProcPtr ``` |
| To | ``` typealias FMFontFamilyCallbackFilterUPP = ApplicationServices.FMFontFamilyCallbackFilterProcPtr ``` |

Modified [FontRecHdl](https://developer.apple.com/documentation/applicationservices/fontrechdl)

|  | Declaration |
| --- | --- |
| From | ``` typealias FontRecHdl = UnsafeMutablePointer<FontRecPtr> ``` |
| To | ``` typealias FontRecHdl = UnsafeMutablePointer<FontRecPtr?> ``` |

Modified GDHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias GDHandle = UnsafeMutablePointer<GDPtr> ``` |
| To | ``` typealias GDHandle = UnsafeMutablePointer<GDPtr?> ``` |

Modified [GetIconFamilyData(_: IconFamilyHandle!, _: OSType, _: Handle!) -> OSErr](https://developer.apple.com/documentation/applicationservices/1462743-geticonfamilydata)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconFamilyData(_ iconFamily: IconFamilyHandle, _ iconType: OSType, _ h: Handle) -> OSErr ``` |
| To | ``` func GetIconFamilyData(_ iconFamily: IconFamilyHandle!, _ iconType: OSType, _ h: Handle!) -> OSErr ``` |

Modified [GetIconRefVariant(_: IconRef!, _: OSType, _: UnsafeMutablePointer<IconTransformType>!) -> IconRef!](https://developer.apple.com/documentation/applicationservices/1463088-geticonrefvariant)

|  | Declaration |
| --- | --- |
| From | ``` func GetIconRefVariant(_ inIconRef: IconRef, _ inVariant: OSType, _ outTransform: UnsafeMutablePointer<IconTransformType>) -> IconRef ``` |
| To | ``` func GetIconRefVariant(_ inIconRef: IconRef!, _ inVariant: OSType, _ outTransform: UnsafeMutablePointer<IconTransformType>!) -> IconRef! ``` |

Modified [GetVoiceDescription(_: UnsafePointer<VoiceSpec>?, _: UnsafeMutablePointer<VoiceDescription>?, _: Int) -> OSErr](https://developer.apple.com/documentation/applicationservices/1463940-getvoicedescription)

|  | Declaration |
| --- | --- |
| From | ``` func GetVoiceDescription(_ voice: UnsafePointer<VoiceSpec>, _ info: UnsafeMutablePointer<VoiceDescription>, _ infoLength: Int) -> OSErr ``` |
| To | ``` func GetVoiceDescription(_ voice: UnsafePointer<VoiceSpec>?, _ info: UnsafeMutablePointer<VoiceDescription>?, _ infoLength: Int) -> OSErr ``` |

Modified [GetVoiceInfo(_: UnsafePointer<VoiceSpec>?, _: OSType, _: UnsafeMutableRawPointer) -> OSErr](https://developer.apple.com/documentation/applicationservices/1461410-getvoiceinfo)

|  | Declaration |
| --- | --- |
| From | ``` func GetVoiceInfo(_ voice: UnsafePointer<VoiceSpec>, _ selector: OSType, _ voiceInfo: UnsafeMutablePointer<Void>) -> OSErr ``` |
| To | ``` func GetVoiceInfo(_ voice: UnsafePointer<VoiceSpec>?, _ selector: OSType, _ voiceInfo: UnsafeMutableRawPointer) -> OSErr ``` |

Modified GrafPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias GrafPtr = COpaquePointer ``` |
| To | ``` typealias GrafPtr = OpaquePointer ``` |

Modified [HIShapeContainsPoint(_: HIShape!, _: UnsafePointer<CGPoint>!) -> Bool](https://developer.apple.com/documentation/applicationservices/1464704-hishapecontainspoint)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeContainsPoint(_ inShape: HIShape!, _ inPoint: UnsafePointer<CGPoint>) -> Bool ``` |
| To | ``` func HIShapeContainsPoint(_ inShape: HIShape!, _ inPoint: UnsafePointer<CGPoint>!) -> Bool ``` |

Modified [HIShapeCreateMutableWithRect(_: UnsafePointer<CGRect>!) -> Unmanaged<HIMutableShape>!](https://developer.apple.com/documentation/applicationservices/1459532-hishapecreatemutablewithrect)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeCreateMutableWithRect(_ inRect: UnsafePointer<CGRect>) -> Unmanaged<HIMutableShape>! ``` |
| To | ``` func HIShapeCreateMutableWithRect(_ inRect: UnsafePointer<CGRect>!) -> Unmanaged<HIMutableShape>! ``` |

Modified [HIShapeCreateWithQDRgn(_: RgnHandle!) -> Unmanaged<HIShape>!](https://developer.apple.com/documentation/applicationservices/1464296-hishapecreatewithqdrgn)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeCreateWithQDRgn(_ inRgn: RgnHandle) -> Unmanaged<HIShape>! ``` |
| To | ``` func HIShapeCreateWithQDRgn(_ inRgn: RgnHandle!) -> Unmanaged<HIShape>! ``` |

Modified [HIShapeCreateWithRect(_: UnsafePointer<CGRect>!) -> Unmanaged<HIShape>!](https://developer.apple.com/documentation/applicationservices/1460650-hishapecreatewithrect)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeCreateWithRect(_ inRect: UnsafePointer<CGRect>) -> Unmanaged<HIShape>! ``` |
| To | ``` func HIShapeCreateWithRect(_ inRect: UnsafePointer<CGRect>!) -> Unmanaged<HIShape>! ``` |

Modified [HIShapeEnumerate(_: HIShape!, _: OptionBits, _: ApplicationServices.HIShapeEnumerateProcPtr!, _: UnsafeMutableRawPointer!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459161-hishapeenumerate)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeEnumerate(_ inShape: HIShape!, _ inOptions: OptionBits, _ inProc: HIShapeEnumerateProcPtr!, _ inRefcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func HIShapeEnumerate(_ inShape: HIShape!, _ inOptions: OptionBits, _ inProc: ApplicationServices.HIShapeEnumerateProcPtr!, _ inRefcon: UnsafeMutableRawPointer!) -> OSStatus ``` |

Modified [HIShapeEnumerateProcPtr](https://developer.apple.com/documentation/applicationservices/hishapeenumerateprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias HIShapeEnumerateProcPtr = (Int32, HIShape!, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias HIShapeEnumerateProcPtr = (Int32, HIShape?, UnsafePointer<CGRect>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [HIShapeGetAsQDRgn(_: HIShape!, _: RgnHandle!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464369-hishapegetasqdrgn)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeGetAsQDRgn(_ inShape: HIShape!, _ outRgn: RgnHandle) -> OSStatus ``` |
| To | ``` func HIShapeGetAsQDRgn(_ inShape: HIShape!, _ outRgn: RgnHandle!) -> OSStatus ``` |

Modified [HIShapeGetBounds(_: HIShape!, _: UnsafeMutablePointer<CGRect>!) -> UnsafeMutablePointer<CGRect>!](https://developer.apple.com/documentation/applicationservices/1460255-hishapegetbounds)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeGetBounds(_ inShape: HIShape!, _ outRect: UnsafeMutablePointer<CGRect>) -> UnsafeMutablePointer<CGRect> ``` |
| To | ``` func HIShapeGetBounds(_ inShape: HIShape!, _ outRect: UnsafeMutablePointer<CGRect>!) -> UnsafeMutablePointer<CGRect>! ``` |

Modified [HIShapeIntersectsRect(_: HIShape!, _: UnsafePointer<CGRect>!) -> Bool](https://developer.apple.com/documentation/applicationservices/1459614-hishapeintersectsrect)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeIntersectsRect(_ inShape: HIShape!, _ inRect: UnsafePointer<CGRect>) -> Bool ``` |
| To | ``` func HIShapeIntersectsRect(_ inShape: HIShape!, _ inRect: UnsafePointer<CGRect>!) -> Bool ``` |

Modified [HIShapeUnionWithRect(_: HIMutableShape!, _: UnsafePointer<CGRect>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462757-hishapeunionwithrect)

|  | Declaration |
| --- | --- |
| From | ``` func HIShapeUnionWithRect(_ inShape: HIMutableShape!, _ inRect: UnsafePointer<CGRect>) -> OSStatus ``` |
| To | ``` func HIShapeUnionWithRect(_ inShape: HIMutableShape!, _ inRect: UnsafePointer<CGRect>!) -> OSStatus ``` |

Modified [ICAppSpecHandle](https://developer.apple.com/documentation/applicationservices/icappspechandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICAppSpecHandle = UnsafeMutablePointer<ICAppSpecPtr> ``` |
| To | ``` typealias ICAppSpecHandle = UnsafeMutablePointer<ICAppSpecPtr?> ``` |

Modified [ICAppSpecListHandle](https://developer.apple.com/documentation/applicationservices/icappspeclisthandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICAppSpecListHandle = UnsafeMutablePointer<ICAppSpecListPtr> ``` |
| To | ``` typealias ICAppSpecListHandle = UnsafeMutablePointer<ICAppSpecListPtr?> ``` |

Modified [ICCharTableHandle](https://developer.apple.com/documentation/applicationservices/icchartablehandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICCharTableHandle = UnsafeMutablePointer<ICCharTablePtr> ``` |
| To | ``` typealias ICCharTableHandle = UnsafeMutablePointer<ICCharTablePtr?> ``` |

Modified [ICFileSpecHandle](https://developer.apple.com/documentation/applicationservices/icfilespechandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICFileSpecHandle = UnsafeMutablePointer<ICFileSpecPtr> ``` |
| To | ``` typealias ICFileSpecHandle = UnsafeMutablePointer<ICFileSpecPtr?> ``` |

Modified [ICFontRecordHandle](https://developer.apple.com/documentation/applicationservices/icfontrecordhandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICFontRecordHandle = UnsafeMutablePointer<ICFontRecordPtr> ``` |
| To | ``` typealias ICFontRecordHandle = UnsafeMutablePointer<ICFontRecordPtr?> ``` |

Modified [ICInstance](https://developer.apple.com/documentation/applicationservices/icinstance)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICInstance = COpaquePointer ``` |
| To | ``` typealias ICInstance = OpaquePointer ``` |

Modified [ICMapEntryHandle](https://developer.apple.com/documentation/applicationservices/icmapentryhandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICMapEntryHandle = UnsafeMutablePointer<ICMapEntryPtr> ``` |
| To | ``` typealias ICMapEntryHandle = UnsafeMutablePointer<ICMapEntryPtr?> ``` |

Modified [IconActionProcPtr](https://developer.apple.com/documentation/applicationservices/iconactionprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias IconActionProcPtr = (ResType, UnsafeMutablePointer<Handle>, UnsafeMutablePointer<Void>) -> OSErr ``` |
| To | ``` typealias IconActionProcPtr = (ResType, UnsafeMutablePointer<Handle?>?, UnsafeMutableRawPointer?) -> OSErr ``` |

Modified [IconActionUPP](https://developer.apple.com/documentation/applicationservices/iconactionupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias IconActionUPP = IconActionProcPtr ``` |
| To | ``` typealias IconActionUPP = ApplicationServices.IconActionProcPtr ``` |

Modified [IconGetterProcPtr](https://developer.apple.com/documentation/applicationservices/icongetterprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias IconGetterProcPtr = (ResType, UnsafeMutablePointer<Void>) -> Handle ``` |
| To | ``` typealias IconGetterProcPtr = (ResType, UnsafeMutableRawPointer?) -> Handle? ``` |

Modified [IconGetterUPP](https://developer.apple.com/documentation/applicationservices/icongetterupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias IconGetterUPP = IconGetterProcPtr ``` |
| To | ``` typealias IconGetterUPP = ApplicationServices.IconGetterProcPtr ``` |

Modified [IconRefContainsCGPoint(_: UnsafePointer<CGPoint>!, _: UnsafePointer<CGRect>!, _: IconAlignmentType, _: IconServicesUsageFlags, _: IconRef!) -> Bool](https://developer.apple.com/documentation/applicationservices/1461049-iconrefcontainscgpoint)

|  | Declaration |
| --- | --- |
| From | ``` func IconRefContainsCGPoint(_ testPt: UnsafePointer<CGPoint>, _ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Bool ``` |
| To | ``` func IconRefContainsCGPoint(_ testPt: UnsafePointer<CGPoint>!, _ iconRect: UnsafePointer<CGRect>!, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef!) -> Bool ``` |

Modified [IconRefIntersectsCGRect(_: UnsafePointer<CGRect>!, _: UnsafePointer<CGRect>!, _: IconAlignmentType, _: IconServicesUsageFlags, _: IconRef!) -> Bool](https://developer.apple.com/documentation/applicationservices/1462553-iconrefintersectscgrect)

|  | Declaration |
| --- | --- |
| From | ``` func IconRefIntersectsCGRect(_ testRect: UnsafePointer<CGRect>, _ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Bool ``` |
| To | ``` func IconRefIntersectsCGRect(_ testRect: UnsafePointer<CGRect>!, _ iconRect: UnsafePointer<CGRect>!, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef!) -> Bool ``` |

Modified [IconRefToHIShape(_: UnsafePointer<CGRect>!, _: IconAlignmentType, _: IconServicesUsageFlags, _: IconRef!) -> Unmanaged<HIShape>!](https://developer.apple.com/documentation/applicationservices/1464005-iconreftohishape)

|  | Declaration |
| --- | --- |
| From | ``` func IconRefToHIShape(_ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Unmanaged<HIShape>! ``` |
| To | ``` func IconRefToHIShape(_ iconRect: UnsafePointer<CGRect>!, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef!) -> Unmanaged<HIShape>! ``` |

Modified [IconRefToIconFamily(_: IconRef!, _: IconSelectorValue, _: UnsafeMutablePointer<IconFamilyHandle?>!) -> OSErr](https://developer.apple.com/documentation/applicationservices/1459977-iconreftoiconfamily)

|  | Declaration |
| --- | --- |
| From | ``` func IconRefToIconFamily(_ theIconRef: IconRef, _ whichIcons: IconSelectorValue, _ iconFamily: UnsafeMutablePointer<IconFamilyHandle>) -> OSErr ``` |
| To | ``` func IconRefToIconFamily(_ theIconRef: IconRef!, _ whichIcons: IconSelectorValue, _ iconFamily: UnsafeMutablePointer<IconFamilyHandle?>!) -> OSErr ``` |

Modified [ICServiceEntryHandle](https://developer.apple.com/documentation/applicationservices/icserviceentryhandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICServiceEntryHandle = UnsafeMutablePointer<ICServiceEntryPtr> ``` |
| To | ``` typealias ICServiceEntryHandle = UnsafeMutablePointer<ICServiceEntryPtr?> ``` |

Modified [ICServicesHandle](https://developer.apple.com/documentation/applicationservices/icserviceshandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias ICServicesHandle = UnsafeMutablePointer<ICServicesPtr> ``` |
| To | ``` typealias ICServicesHandle = UnsafeMutablePointer<ICServicesPtr?> ``` |

Modified [InvokeIconActionUPP(_: ResType, _: UnsafeMutablePointer<Handle?>!, _: UnsafeMutableRawPointer!, _: ApplicationServices.IconActionUPP!) -> OSErr](https://developer.apple.com/documentation/applicationservices/1464116-invokeiconactionupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeIconActionUPP(_ theType: ResType, _ theIcon: UnsafeMutablePointer<Handle>, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: IconActionUPP!) -> OSErr ``` |
| To | ``` func InvokeIconActionUPP(_ theType: ResType, _ theIcon: UnsafeMutablePointer<Handle?>!, _ yourDataPtr: UnsafeMutableRawPointer!, _ userUPP: ApplicationServices.IconActionUPP!) -> OSErr ``` |

Modified [InvokeIconGetterUPP(_: ResType, _: UnsafeMutableRawPointer!, _: ApplicationServices.IconGetterUPP!) -> Handle!](https://developer.apple.com/documentation/applicationservices/1460976-invokeicongetterupp)

|  | Declaration |
| --- | --- |
| From | ``` func InvokeIconGetterUPP(_ theType: ResType, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: IconGetterUPP!) -> Handle ``` |
| To | ``` func InvokeIconGetterUPP(_ theType: ResType, _ yourDataPtr: UnsafeMutableRawPointer!, _ userUPP: ApplicationServices.IconGetterUPP!) -> Handle! ``` |

Modified [IsIconRefMaskEmpty(_: IconRef!) -> Bool](https://developer.apple.com/documentation/applicationservices/1464419-isiconrefmaskempty)

|  | Declaration |
| --- | --- |
| From | ``` func IsIconRefMaskEmpty(_ iconRef: IconRef) -> Bool ``` |
| To | ``` func IsIconRefMaskEmpty(_ iconRef: IconRef!) -> Bool ``` |

Modified [LAContextRef](https://developer.apple.com/documentation/applicationservices/lacontextref)

|  | Declaration |
| --- | --- |
| From | ``` typealias LAContextRef = COpaquePointer ``` |
| To | ``` typealias LAContextRef = OpaquePointer ``` |

Modified [LAEnvironmentRef](https://developer.apple.com/documentation/applicationservices/laenvironmentref)

|  | Declaration |
| --- | --- |
| From | ``` typealias LAEnvironmentRef = COpaquePointer ``` |
| To | ``` typealias LAEnvironmentRef = OpaquePointer ``` |

Modified [NewIconActionUPP(_: ApplicationServices.IconActionProcPtr!) -> ApplicationServices.IconActionUPP!](https://developer.apple.com/documentation/applicationservices/1462738-newiconactionupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewIconActionUPP(_ userRoutine: IconActionProcPtr!) -> IconActionUPP! ``` |
| To | ``` func NewIconActionUPP(_ userRoutine: ApplicationServices.IconActionProcPtr!) -> ApplicationServices.IconActionUPP! ``` |

Modified [NewIconGetterUPP(_: ApplicationServices.IconGetterProcPtr!) -> ApplicationServices.IconGetterUPP!](https://developer.apple.com/documentation/applicationservices/1458777-newicongetterupp)

|  | Declaration |
| --- | --- |
| From | ``` func NewIconGetterUPP(_ userRoutine: IconGetterProcPtr!) -> IconGetterUPP! ``` |
| To | ``` func NewIconGetterUPP(_ userRoutine: ApplicationServices.IconGetterProcPtr!) -> ApplicationServices.IconGetterUPP! ``` |

Modified [NewSpeechChannel(_: UnsafeMutablePointer<VoiceSpec>?, _: UnsafeMutablePointer<SpeechChannel?>) -> OSErr](https://developer.apple.com/documentation/applicationservices/1461367-newspeechchannel)

|  | Declaration |
| --- | --- |
| From | ``` func NewSpeechChannel(_ voice: UnsafeMutablePointer<VoiceSpec>, _ chan: UnsafeMutablePointer<SpeechChannel>) -> OSErr ``` |
| To | ``` func NewSpeechChannel(_ voice: UnsafeMutablePointer<VoiceSpec>?, _ chan: UnsafeMutablePointer<SpeechChannel?>) -> OSErr ``` |

Modified [PasteboardClear(_: Pasteboard) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460800-pasteboardclear)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardClear(_ inPasteboard: Pasteboard!) -> OSStatus ``` |
| To | ``` func PasteboardClear(_ inPasteboard: Pasteboard) -> OSStatus ``` |

Modified [PasteboardCopyItemFlavorData(_: Pasteboard, _: PasteboardItemID, _: CFString, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1458917-pasteboardcopyitemflavordata)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardCopyItemFlavorData(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ inFlavorType: CFString!, _ outData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func PasteboardCopyItemFlavorData(_ inPasteboard: Pasteboard, _ inItem: PasteboardItemID, _ inFlavorType: CFString, _ outData: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [PasteboardCopyItemFlavors(_: Pasteboard, _: PasteboardItemID, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460005-pasteboardcopyitemflavors)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardCopyItemFlavors(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ outFlavorTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func PasteboardCopyItemFlavors(_ inPasteboard: Pasteboard, _ inItem: PasteboardItemID, _ outFlavorTypes: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [PasteboardCopyName(_: Pasteboard, _: UnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459455-pasteboardcopyname)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardCopyName(_ inPasteboard: Pasteboard!, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func PasteboardCopyName(_ inPasteboard: Pasteboard, _ outName: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [PasteboardCopyPasteLocation(_: Pasteboard, _: UnsafeMutablePointer<CFURL?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462546-pasteboardcopypastelocation)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardCopyPasteLocation(_ inPasteboard: Pasteboard!, _ outPasteLocation: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func PasteboardCopyPasteLocation(_ inPasteboard: Pasteboard, _ outPasteLocation: UnsafeMutablePointer<CFURL?>) -> OSStatus ``` |

Modified [PasteboardCreate(_: CFString?, _: UnsafeMutablePointer<Pasteboard?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461248-pasteboardcreate)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardCreate(_ inName: CFString!, _ outPasteboard: UnsafeMutablePointer<Unmanaged<Pasteboard>?>) -> OSStatus ``` |
| To | ``` func PasteboardCreate(_ inName: CFString?, _ outPasteboard: UnsafeMutablePointer<Pasteboard?>) -> OSStatus ``` |

Modified [PasteboardGetItemCount(_: Pasteboard, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459551-pasteboardgetitemcount)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardGetItemCount(_ inPasteboard: Pasteboard!, _ outItemCount: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func PasteboardGetItemCount(_ inPasteboard: Pasteboard, _ outItemCount: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [PasteboardGetItemFlavorFlags(_: Pasteboard, _: PasteboardItemID, _: CFString, _: UnsafeMutablePointer<PasteboardFlavorFlags>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459353-pasteboardgetitemflavorflags)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardGetItemFlavorFlags(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ inFlavorType: CFString!, _ outFlags: UnsafeMutablePointer<PasteboardFlavorFlags>) -> OSStatus ``` |
| To | ``` func PasteboardGetItemFlavorFlags(_ inPasteboard: Pasteboard, _ inItem: PasteboardItemID, _ inFlavorType: CFString, _ outFlags: UnsafeMutablePointer<PasteboardFlavorFlags>) -> OSStatus ``` |

Modified [PasteboardGetItemIdentifier(_: Pasteboard, _: CFIndex, _: UnsafeMutablePointer<PasteboardItemID?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463412-pasteboardgetitemidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardGetItemIdentifier(_ inPasteboard: Pasteboard!, _ inIndex: CFIndex, _ outItem: UnsafeMutablePointer<PasteboardItemID>) -> OSStatus ``` |
| To | ``` func PasteboardGetItemIdentifier(_ inPasteboard: Pasteboard, _ inIndex: CFIndex, _ outItem: UnsafeMutablePointer<PasteboardItemID?>) -> OSStatus ``` |

Modified [PasteboardItemID](https://developer.apple.com/documentation/applicationservices/pasteboarditemid)

|  | Declaration |
| --- | --- |
| From | ``` typealias PasteboardItemID = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias PasteboardItemID = UnsafeMutableRawPointer ``` |

Modified [PasteboardPromiseKeeperProcPtr](https://developer.apple.com/documentation/applicationservices/pasteboardpromisekeeperprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias PasteboardPromiseKeeperProcPtr = (Pasteboard!, PasteboardItemID, CFString!, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias PasteboardPromiseKeeperProcPtr = (Pasteboard, PasteboardItemID, CFString, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [PasteboardPutItemFlavor(_: Pasteboard, _: PasteboardItemID, _: CFString, _: CFData?, _: PasteboardFlavorFlags) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463184-pasteboardputitemflavor)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardPutItemFlavor(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ inFlavorType: CFString!, _ inData: CFData!, _ inFlags: PasteboardFlavorFlags) -> OSStatus ``` |
| To | ``` func PasteboardPutItemFlavor(_ inPasteboard: Pasteboard, _ inItem: PasteboardItemID, _ inFlavorType: CFString, _ inData: CFData?, _ inFlags: PasteboardFlavorFlags) -> OSStatus ``` |

Modified [PasteboardResolvePromises(_: Pasteboard) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460816-pasteboardresolvepromises)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardResolvePromises(_ inPasteboard: Pasteboard!) -> OSStatus ``` |
| To | ``` func PasteboardResolvePromises(_ inPasteboard: Pasteboard) -> OSStatus ``` |

Modified [PasteboardSetPasteLocation(_: Pasteboard, _: CFURL) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460572-pasteboardsetpastelocation)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardSetPasteLocation(_ inPasteboard: Pasteboard!, _ inPasteLocation: CFURL!) -> OSStatus ``` |
| To | ``` func PasteboardSetPasteLocation(_ inPasteboard: Pasteboard, _ inPasteLocation: CFURL) -> OSStatus ``` |

Modified [PasteboardSetPromiseKeeper(_: Pasteboard, _: ApplicationServices.PasteboardPromiseKeeperProcPtr, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463604-pasteboardsetpromisekeeper)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardSetPromiseKeeper(_ inPasteboard: Pasteboard!, _ inPromiseKeeper: PasteboardPromiseKeeperProcPtr!, _ inContext: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func PasteboardSetPromiseKeeper(_ inPasteboard: Pasteboard, _ inPromiseKeeper: ApplicationServices.PasteboardPromiseKeeperProcPtr, _ inContext: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [PasteboardSynchronize(_: Pasteboard) -> PasteboardSyncFlags](https://developer.apple.com/documentation/applicationservices/1459590-pasteboardsynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func PasteboardSynchronize(_ inPasteboard: Pasteboard!) -> PasteboardSyncFlags ``` |
| To | ``` func PasteboardSynchronize(_ inPasteboard: Pasteboard) -> PasteboardSyncFlags ``` |

Modified [PatHandle](https://developer.apple.com/documentation/applicationservices/pathandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias PatHandle = UnsafeMutablePointer<PatPtr> ``` |
| To | ``` typealias PatHandle = UnsafeMutablePointer<PatPtr?> ``` |

Modified PicHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias PicHandle = UnsafeMutablePointer<PicPtr> ``` |
| To | ``` typealias PicHandle = UnsafeMutablePointer<PicPtr?> ``` |

Modified PixMapHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias PixMapHandle = UnsafeMutablePointer<PixMapPtr> ``` |
| To | ``` typealias PixMapHandle = UnsafeMutablePointer<PixMapPtr?> ``` |

Modified [PixPatHandle](https://developer.apple.com/documentation/applicationservices/pixpathandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias PixPatHandle = UnsafeMutablePointer<PixPatPtr> ``` |
| To | ``` typealias PixPatHandle = UnsafeMutablePointer<PixPatPtr?> ``` |

Modified [PlotIconRefInContext(_: CGContext!, _: UnsafePointer<CGRect>!, _: IconAlignmentType, _: IconTransformType, _: UnsafePointer<RGBColor>!, _: PlotIconRefFlags, _: IconRef!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463721-ploticonrefincontext)

|  | Declaration |
| --- | --- |
| From | ``` func PlotIconRefInContext(_ inContext: CGContext!, _ inRect: UnsafePointer<CGRect>, _ inAlign: IconAlignmentType, _ inTransform: IconTransformType, _ inLabelColor: UnsafePointer<RGBColor>, _ inFlags: PlotIconRefFlags, _ inIconRef: IconRef) -> OSStatus ``` |
| To | ``` func PlotIconRefInContext(_ inContext: CGContext!, _ inRect: UnsafePointer<CGRect>!, _ inAlign: IconAlignmentType, _ inTransform: IconTransformType, _ inLabelColor: UnsafePointer<RGBColor>!, _ inFlags: PlotIconRefFlags, _ inIconRef: IconRef!) -> OSStatus ``` |

Modified [PMGetPageFormatExtendedData(_: PMPageFormat, _: OSType, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464455-pmgetpageformatextendeddata)

|  | Declaration |
| --- | --- |
| From | ``` func PMGetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UnsafeMutablePointer<UInt32>, _ extendedData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func PMGetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UnsafeMutablePointer<UInt32>?, _ extendedData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [PMObject](https://developer.apple.com/documentation/applicationservices/pmobject)

|  | Declaration |
| --- | --- |
| From | ``` typealias PMObject = UnsafePointer<Void> ``` |
| To | ``` typealias PMObject = UnsafeRawPointer ``` |

Modified [PMPageFormat](https://developer.apple.com/documentation/applicationservices/pmpageformat)

|  | Declaration |
| --- | --- |
| From | ``` typealias PMPageFormat = COpaquePointer ``` |
| To | ``` typealias PMPageFormat = OpaquePointer ``` |

Modified [PMPageFormatCreateDataRepresentation(_: PMPageFormat, _: UnsafeMutablePointer<Unmanaged<CFData>>, _: PMDataFormat) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464227-pmpageformatcreatedatarepresenta)

|  | Declaration |
| --- | --- |
| From | ``` func PMPageFormatCreateDataRepresentation(_ pageFormat: PMPageFormat, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>, _ format: PMDataFormat) -> OSStatus ``` |
| To | ``` func PMPageFormatCreateDataRepresentation(_ pageFormat: PMPageFormat, _ data: UnsafeMutablePointer<Unmanaged<CFData>>, _ format: PMDataFormat) -> OSStatus ``` |

Modified [PMPaper](https://developer.apple.com/documentation/applicationservices/pmpaper)

|  | Declaration |
| --- | --- |
| From | ``` typealias PMPaper = COpaquePointer ``` |
| To | ``` typealias PMPaper = OpaquePointer ``` |

Modified [PMPaperCreateCustom(_: PMPrinter?, _: CFString?, _: CFString?, _: Double, _: Double, _: UnsafePointer<PMPaperMargins>, _: UnsafeMutablePointer<PMPaper?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459322-pmpapercreatecustom)

|  | Declaration |
| --- | --- |
| From | ``` func PMPaperCreateCustom(_ printer: PMPrinter, _ id: CFString?, _ name: CFString?, _ width: Double, _ height: Double, _ margins: UnsafePointer<PMPaperMargins>, _ paperP: UnsafeMutablePointer<PMPaper>) -> OSStatus ``` |
| To | ``` func PMPaperCreateCustom(_ printer: PMPrinter?, _ id: CFString?, _ name: CFString?, _ width: Double, _ height: Double, _ margins: UnsafePointer<PMPaperMargins>, _ paperP: UnsafeMutablePointer<PMPaper?>) -> OSStatus ``` |

Modified [PMPaperGetID(_: PMPaper, _: UnsafeMutablePointer<Unmanaged<CFString>>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462910-pmpapergetid)

|  | Declaration |
| --- | --- |
| From | ``` func PMPaperGetID(_ paper: PMPaper, _ paperID: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func PMPaperGetID(_ paper: PMPaper, _ paperID: UnsafeMutablePointer<Unmanaged<CFString>>) -> OSStatus ``` |

Modified [PMPreset](https://developer.apple.com/documentation/applicationservices/pmpreset)

|  | Declaration |
| --- | --- |
| From | ``` typealias PMPreset = COpaquePointer ``` |
| To | ``` typealias PMPreset = OpaquePointer ``` |

Modified [PMPrinter](https://developer.apple.com/documentation/applicationservices/pmprinter)

|  | Declaration |
| --- | --- |
| From | ``` typealias PMPrinter = COpaquePointer ``` |
| To | ``` typealias PMPrinter = OpaquePointer ``` |

Modified [PMPrinterCopyHostName(_: PMPrinter, _: UnsafeMutablePointer<Unmanaged<CFString>>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462076-pmprintercopyhostname)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterCopyHostName(_ printer: PMPrinter, _ hostNameP: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func PMPrinterCopyHostName(_ printer: PMPrinter, _ hostNameP: UnsafeMutablePointer<Unmanaged<CFString>>) -> OSStatus ``` |

Modified [PMPrinterCopyState(_: PMPrinter, _: UnsafeMutablePointer<Unmanaged<CFDictionary>>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460381-pmprintercopystate)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterCopyState(_ printer: PMPrinter, _ stateDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func PMPrinterCopyState(_ printer: PMPrinter, _ stateDict: UnsafeMutablePointer<Unmanaged<CFDictionary>>) -> OSStatus ``` |

Modified [PMPrinterCreateFromPrinterID(_: CFString) -> PMPrinter?](https://developer.apple.com/documentation/applicationservices/1461363-pmprintercreatefromprinterid)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterCreateFromPrinterID(_ printerID: CFString) -> PMPrinter ``` |
| To | ``` func PMPrinterCreateFromPrinterID(_ printerID: CFString) -> PMPrinter? ``` |

Modified [PMPrinterGetCommInfo(_: PMPrinter, _: UnsafeMutablePointer<DarwinBoolean>?, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461069-pmprintergetcomminfo)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetCommInfo(_ printer: PMPrinter, _ supportsControlCharRangeP: UnsafeMutablePointer<DarwinBoolean>, _ supportsEightBitP: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func PMPrinterGetCommInfo(_ printer: PMPrinter, _ supportsControlCharRangeP: UnsafeMutablePointer<DarwinBoolean>?, _ supportsEightBitP: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [PMPrinterGetMimeTypes(_: PMPrinter, _: PMPrintSettings?, _: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460125-pmprintergetmimetypes)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetMimeTypes(_ printer: PMPrinter, _ settings: PMPrintSettings, _ mimeTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func PMPrinterGetMimeTypes(_ printer: PMPrinter, _ settings: PMPrintSettings?, _ mimeTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified [PMPrinterPrintWithFile(_: PMPrinter, _: PMPrintSettings, _: PMPageFormat?, _: CFString?, _: CFURL) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464600-pmprinterprintwithfile)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterPrintWithFile(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString?, _ fileURL: CFURL) -> OSStatus ``` |
| To | ``` func PMPrinterPrintWithFile(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat?, _ mimeType: CFString?, _ fileURL: CFURL) -> OSStatus ``` |

Modified [PMPrinterPrintWithProvider(_: PMPrinter, _: PMPrintSettings, _: PMPageFormat?, _: CFString, _: CGDataProvider) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461110-pmprinterprintwithprovider)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterPrintWithProvider(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString, _ provider: CGDataProvider) -> OSStatus ``` |
| To | ``` func PMPrinterPrintWithProvider(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat?, _ mimeType: CFString, _ provider: CGDataProvider) -> OSStatus ``` |

Modified [PMPrinterWritePostScriptToURL(_: PMPrinter, _: PMPrintSettings, _: PMPageFormat?, _: CFString?, _: CFURL, _: CFURL) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459729-pmprinterwritepostscripttourl)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterWritePostScriptToURL(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat, _ mimeType: CFString?, _ sourceFileURL: CFURL, _ destinationFileURL: CFURL) -> OSStatus ``` |
| To | ``` func PMPrinterWritePostScriptToURL(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat?, _ mimeType: CFString?, _ sourceFileURL: CFURL, _ destinationFileURL: CFURL) -> OSStatus ``` |

Modified [PMPrintSession](https://developer.apple.com/documentation/applicationservices/pmprintsession)

|  | Declaration |
| --- | --- |
| From | ``` typealias PMPrintSession = COpaquePointer ``` |
| To | ``` typealias PMPrintSession = OpaquePointer ``` |

Modified [PMPrintSettings](https://developer.apple.com/documentation/applicationservices/pmprintsettings)

|  | Declaration |
| --- | --- |
| From | ``` typealias PMPrintSettings = COpaquePointer ``` |
| To | ``` typealias PMPrintSettings = OpaquePointer ``` |

Modified [PMPrintSettingsCreateDataRepresentation(_: PMPrintSettings, _: UnsafeMutablePointer<Unmanaged<CFData>>, _: PMDataFormat) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464570-pmprintsettingscreatedatareprese)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsCreateDataRepresentation(_ printSettings: PMPrintSettings, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>, _ format: PMDataFormat) -> OSStatus ``` |
| To | ``` func PMPrintSettingsCreateDataRepresentation(_ printSettings: PMPrintSettings, _ data: UnsafeMutablePointer<Unmanaged<CFData>>, _ format: PMDataFormat) -> OSStatus ``` |

Modified [PMPrintSettingsGetValue(_: PMPrintSettings, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460602-pmprintsettingsgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsGetValue(_ printSettings: PMPrintSettings, _ key: CFString, _ value: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func PMPrintSettingsGetValue(_ printSettings: PMPrintSettings, _ key: CFString, _ value: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus ``` |

Modified [PMPrintSettingsSetValue(_: PMPrintSettings, _: CFString, _: CFTypeRef?, _: Bool) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461697-pmprintsettingssetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsSetValue(_ printSettings: PMPrintSettings, _ key: CFString, _ value: AnyObject?, _ locked: Bool) -> OSStatus ``` |
| To | ``` func PMPrintSettingsSetValue(_ printSettings: PMPrintSettings, _ key: CFString, _ value: CFTypeRef?, _ locked: Bool) -> OSStatus ``` |

Modified [PMPrintSettingsToOptions(_: PMPrintSettings, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459069-pmprintsettingstooptions)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsToOptions(_ settings: PMPrintSettings, _ options: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |
| To | ``` func PMPrintSettingsToOptions(_ settings: PMPrintSettings, _ options: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>) -> OSStatus ``` |

Modified [PMPrintSettingsToOptionsWithPrinterAndPageFormat(_: PMPrintSettings, _: PMPrinter, _: PMPageFormat?, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459435-pmprintsettingstooptionswithprin)

|  | Declaration |
| --- | --- |
| From | ``` func PMPrintSettingsToOptionsWithPrinterAndPageFormat(_ settings: PMPrintSettings, _ printer: PMPrinter, _ pageFormat: PMPageFormat, _ options: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |
| To | ``` func PMPrintSettingsToOptionsWithPrinterAndPageFormat(_ settings: PMPrintSettings, _ printer: PMPrinter, _ pageFormat: PMPageFormat?, _ options: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>) -> OSStatus ``` |

Modified [PMRelease(_: PMObject?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461402-pmrelease)

|  | Declaration |
| --- | --- |
| From | ``` func PMRelease(_ object: PMObject) -> OSStatus ``` |
| To | ``` func PMRelease(_ object: PMObject?) -> OSStatus ``` |

Modified [PMRetain(_: PMObject?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460190-pmretain)

|  | Declaration |
| --- | --- |
| From | ``` func PMRetain(_ object: PMObject) -> OSStatus ``` |
| To | ``` func PMRetain(_ object: PMObject?) -> OSStatus ``` |

Modified [PMServer](https://developer.apple.com/documentation/applicationservices/pmserver)

|  | Declaration |
| --- | --- |
| From | ``` typealias PMServer = COpaquePointer ``` |
| To | ``` typealias PMServer = OpaquePointer ``` |

Modified [PMServerCreatePrinterList(_: PMServer?, _: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459953-pmservercreateprinterlist)

|  | Declaration |
| --- | --- |
| From | ``` func PMServerCreatePrinterList(_ server: PMServer, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func PMServerCreatePrinterList(_ server: PMServer?, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified [PMServerLaunchPrinterBrowser(_: PMServer?, _: CFDictionary?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460175-pmserverlaunchprinterbrowser)

|  | Declaration |
| --- | --- |
| From | ``` func PMServerLaunchPrinterBrowser(_ server: PMServer, _ options: CFDictionary?) -> OSStatus ``` |
| To | ``` func PMServerLaunchPrinterBrowser(_ server: PMServer?, _ options: CFDictionary?) -> OSStatus ``` |

Modified [PMSessionBeginPageNoDialog(_: PMPrintSession, _: PMPageFormat?, _: UnsafePointer<PMRect>?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463416-pmsessionbeginpagenodialog)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionBeginPageNoDialog(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ pageFrame: UnsafePointer<PMRect>) -> OSStatus ``` |
| To | ``` func PMSessionBeginPageNoDialog(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat?, _ pageFrame: UnsafePointer<PMRect>?) -> OSStatus ``` |

Modified [PMSessionCreatePageFormatList(_: PMPrintSession, _: PMPrinter?, _: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463985-pmsessioncreatepageformatlist)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionCreatePageFormatList(_ printSession: PMPrintSession, _ printer: PMPrinter, _ pageFormatList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func PMSessionCreatePageFormatList(_ printSession: PMPrintSession, _ printer: PMPrinter?, _ pageFormatList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified [PMSessionCreatePrinterList(_: PMPrintSession, _: UnsafeMutablePointer<Unmanaged<CFArray>>, _: UnsafeMutablePointer<CFIndex>?, _: UnsafeMutablePointer<PMPrinter>?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460119-pmsessioncreateprinterlist)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionCreatePrinterList(_ printSession: PMPrintSession, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ currentIndex: UnsafeMutablePointer<CFIndex>, _ currentPrinter: UnsafeMutablePointer<PMPrinter>) -> OSStatus ``` |
| To | ``` func PMSessionCreatePrinterList(_ printSession: PMPrintSession, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>>, _ currentIndex: UnsafeMutablePointer<CFIndex>?, _ currentPrinter: UnsafeMutablePointer<PMPrinter>?) -> OSStatus ``` |

Modified [PMSessionGetDataFromSession(_: PMPrintSession, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462964-pmsessiongetdatafromsession)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionGetDataFromSession(_ printSession: PMPrintSession, _ key: CFString, _ data: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func PMSessionGetDataFromSession(_ printSession: PMPrintSession, _ key: CFString, _ data: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>) -> OSStatus ``` |

Modified [PMSessionSetDataInSession(_: PMPrintSession, _: CFString, _: CFTypeRef) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1461902-pmsessionsetdatainsession)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionSetDataInSession(_ printSession: PMPrintSession, _ key: CFString, _ data: AnyObject) -> OSStatus ``` |
| To | ``` func PMSessionSetDataInSession(_ printSession: PMPrintSession, _ key: CFString, _ data: CFTypeRef) -> OSStatus ``` |

Modified [PMSessionValidatePageFormat(_: PMPrintSession, _: PMPageFormat, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459090-pmsessionvalidatepageformat)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionValidatePageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ changed: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func PMSessionValidatePageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ changed: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [PMSessionValidatePrintSettings(_: PMPrintSession, _: PMPrintSettings, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1458994-pmsessionvalidateprintsettings)

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionValidatePrintSettings(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ changed: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func PMSessionValidatePrintSettings(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ changed: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [PMSetPageFormatExtendedData(_: PMPageFormat, _: OSType, _: UInt32, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463464-pmsetpageformatextendeddata)

|  | Declaration |
| --- | --- |
| From | ``` func PMSetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UInt32, _ extendedData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func PMSetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UInt32, _ extendedData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [PMWorkflowSubmitPDFWithOptions(_: CFURL, _: CFString?, _: UnsafePointer<Int8>?, _: CFURL) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1463747-pmworkflowsubmitpdfwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func PMWorkflowSubmitPDFWithOptions(_ workflowItem: CFURL, _ title: CFString?, _ options: UnsafePointer<Int8>, _ pdfFile: CFURL) -> OSStatus ``` |
| To | ``` func PMWorkflowSubmitPDFWithOptions(_ workflowItem: CFURL, _ title: CFString?, _ options: UnsafePointer<Int8>?, _ pdfFile: CFURL) -> OSStatus ``` |

Modified [PolyHandle](https://developer.apple.com/documentation/applicationservices/polyhandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias PolyHandle = UnsafeMutablePointer<PolyPtr> ``` |
| To | ``` typealias PolyHandle = UnsafeMutablePointer<PolyPtr?> ``` |

Modified [QDArcProcPtr](https://developer.apple.com/documentation/applicationservices/qdarcprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDArcProcPtr = (GrafVerb, UnsafePointer<Rect>, Int16, Int16) -> Void ``` |
| To | ``` typealias QDArcProcPtr = (GrafVerb, UnsafePointer<Rect>?, Int16, Int16) -> Swift.Void ``` |

Modified [QDArcUPP](https://developer.apple.com/documentation/applicationservices/qdarcupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDArcUPP = QDArcProcPtr ``` |
| To | ``` typealias QDArcUPP = ApplicationServices.QDArcProcPtr ``` |

Modified [QDBitsProcPtr](https://developer.apple.com/documentation/applicationservices/qdbitsprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDBitsProcPtr = (UnsafePointer<BitMap>, UnsafePointer<Rect>, UnsafePointer<Rect>, Int16, RgnHandle) -> Void ``` |
| To | ``` typealias QDBitsProcPtr = (UnsafePointer<BitMap>?, UnsafePointer<Rect>?, UnsafePointer<Rect>?, Int16, RgnHandle?) -> Swift.Void ``` |

Modified [QDBitsUPP](https://developer.apple.com/documentation/applicationservices/qdbitsupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDBitsUPP = QDBitsProcPtr ``` |
| To | ``` typealias QDBitsUPP = ApplicationServices.QDBitsProcPtr ``` |

Modified [QDCommentProcPtr](https://developer.apple.com/documentation/applicationservices/qdcommentprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDCommentProcPtr = (Int16, Int16, Handle) -> Void ``` |
| To | ``` typealias QDCommentProcPtr = (Int16, Int16, Handle?) -> Swift.Void ``` |

Modified [QDCommentUPP](https://developer.apple.com/documentation/applicationservices/qdcommentupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDCommentUPP = QDCommentProcPtr ``` |
| To | ``` typealias QDCommentUPP = ApplicationServices.QDCommentProcPtr ``` |

Modified [QDGetPicProcPtr](https://developer.apple.com/documentation/applicationservices/qdgetpicprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDGetPicProcPtr = (UnsafeMutablePointer<Void>, Int16) -> Void ``` |
| To | ``` typealias QDGetPicProcPtr = (UnsafeMutableRawPointer?, Int16) -> Swift.Void ``` |

Modified [QDGetPicUPP](https://developer.apple.com/documentation/applicationservices/qdgetpicupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDGetPicUPP = QDGetPicProcPtr ``` |
| To | ``` typealias QDGetPicUPP = ApplicationServices.QDGetPicProcPtr ``` |

Modified [QDJShieldCursorProcPtr](https://developer.apple.com/documentation/applicationservices/qdjshieldcursorprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDJShieldCursorProcPtr = (Int16, Int16, Int16, Int16) -> Void ``` |
| To | ``` typealias QDJShieldCursorProcPtr = (Int16, Int16, Int16, Int16) -> Swift.Void ``` |

Modified [QDJShieldCursorUPP](https://developer.apple.com/documentation/applicationservices/qdjshieldcursorupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDJShieldCursorUPP = QDJShieldCursorProcPtr ``` |
| To | ``` typealias QDJShieldCursorUPP = ApplicationServices.QDJShieldCursorProcPtr ``` |

Modified [QDLineProcPtr](https://developer.apple.com/documentation/applicationservices/qdlineprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDLineProcPtr = (Point) -> Void ``` |
| To | ``` typealias QDLineProcPtr = (Point) -> Swift.Void ``` |

Modified [QDLineUPP](https://developer.apple.com/documentation/applicationservices/qdlineupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDLineUPP = QDLineProcPtr ``` |
| To | ``` typealias QDLineUPP = ApplicationServices.QDLineProcPtr ``` |

Modified [QDOpcodeProcPtr](https://developer.apple.com/documentation/applicationservices/qdopcodeprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDOpcodeProcPtr = (UnsafePointer<Rect>, UnsafePointer<Rect>, UInt16, Int16) -> Void ``` |
| To | ``` typealias QDOpcodeProcPtr = (UnsafePointer<Rect>?, UnsafePointer<Rect>?, UInt16, Int16) -> Swift.Void ``` |

Modified [QDOpcodeUPP](https://developer.apple.com/documentation/applicationservices/qdopcodeupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDOpcodeUPP = QDOpcodeProcPtr ``` |
| To | ``` typealias QDOpcodeUPP = ApplicationServices.QDOpcodeProcPtr ``` |

Modified [QDOvalProcPtr](https://developer.apple.com/documentation/applicationservices/qdovalprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDOvalProcPtr = (GrafVerb, UnsafePointer<Rect>) -> Void ``` |
| To | ``` typealias QDOvalProcPtr = (GrafVerb, UnsafePointer<Rect>?) -> Swift.Void ``` |

Modified [QDOvalUPP](https://developer.apple.com/documentation/applicationservices/qdovalupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDOvalUPP = QDOvalProcPtr ``` |
| To | ``` typealias QDOvalUPP = ApplicationServices.QDOvalProcPtr ``` |

Modified [QDPolyProcPtr](https://developer.apple.com/documentation/applicationservices/qdpolyprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPolyProcPtr = (GrafVerb, PolyHandle) -> Void ``` |
| To | ``` typealias QDPolyProcPtr = (GrafVerb, PolyHandle?) -> Swift.Void ``` |

Modified [QDPolyUPP](https://developer.apple.com/documentation/applicationservices/qdpolyupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPolyUPP = QDPolyProcPtr ``` |
| To | ``` typealias QDPolyUPP = ApplicationServices.QDPolyProcPtr ``` |

Modified [QDPrinterStatusProcPtr](https://developer.apple.com/documentation/applicationservices/qdprinterstatusprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPrinterStatusProcPtr = (PrinterStatusOpcode, CGrafPtr, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias QDPrinterStatusProcPtr = (PrinterStatusOpcode, CGrafPtr?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [QDPrinterStatusUPP](https://developer.apple.com/documentation/applicationservices/qdprinterstatusupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPrinterStatusUPP = QDPrinterStatusProcPtr ``` |
| To | ``` typealias QDPrinterStatusUPP = ApplicationServices.QDPrinterStatusProcPtr ``` |

Modified [QDPutPicProcPtr](https://developer.apple.com/documentation/applicationservices/qdputpicprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPutPicProcPtr = (UnsafePointer<Void>, Int16) -> Void ``` |
| To | ``` typealias QDPutPicProcPtr = (UnsafeRawPointer?, Int16) -> Swift.Void ``` |

Modified [QDPutPicUPP](https://developer.apple.com/documentation/applicationservices/qdputpicupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPutPicUPP = QDPutPicProcPtr ``` |
| To | ``` typealias QDPutPicUPP = ApplicationServices.QDPutPicProcPtr ``` |

Modified [QDRectProcPtr](https://developer.apple.com/documentation/applicationservices/qdrectprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRectProcPtr = (GrafVerb, UnsafePointer<Rect>) -> Void ``` |
| To | ``` typealias QDRectProcPtr = (GrafVerb, UnsafePointer<Rect>?) -> Swift.Void ``` |

Modified [QDRectUPP](https://developer.apple.com/documentation/applicationservices/qdrectupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRectUPP = QDRectProcPtr ``` |
| To | ``` typealias QDRectUPP = ApplicationServices.QDRectProcPtr ``` |

Modified [QDRgnProcPtr](https://developer.apple.com/documentation/applicationservices/qdrgnprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRgnProcPtr = (GrafVerb, RgnHandle) -> Void ``` |
| To | ``` typealias QDRgnProcPtr = (GrafVerb, RgnHandle?) -> Swift.Void ``` |

Modified [QDRgnUPP](https://developer.apple.com/documentation/applicationservices/qdrgnupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRgnUPP = QDRgnProcPtr ``` |
| To | ``` typealias QDRgnUPP = ApplicationServices.QDRgnProcPtr ``` |

Modified [QDRRectProcPtr](https://developer.apple.com/documentation/applicationservices/qdrrectprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRRectProcPtr = (GrafVerb, UnsafePointer<Rect>, Int16, Int16) -> Void ``` |
| To | ``` typealias QDRRectProcPtr = (GrafVerb, UnsafePointer<Rect>?, Int16, Int16) -> Swift.Void ``` |

Modified [QDRRectUPP](https://developer.apple.com/documentation/applicationservices/qdrrectupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRRectUPP = QDRRectProcPtr ``` |
| To | ``` typealias QDRRectUPP = ApplicationServices.QDRRectProcPtr ``` |

Modified [QDStdGlyphsProcPtr](https://developer.apple.com/documentation/applicationservices/qdstdglyphsprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDStdGlyphsProcPtr = (UnsafeMutablePointer<Void>, Int) -> OSStatus ``` |
| To | ``` typealias QDStdGlyphsProcPtr = (UnsafeMutableRawPointer?, Int) -> OSStatus ``` |

Modified [QDStdGlyphsUPP](https://developer.apple.com/documentation/applicationservices/qdstdglyphsupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDStdGlyphsUPP = QDStdGlyphsProcPtr ``` |
| To | ``` typealias QDStdGlyphsUPP = ApplicationServices.QDStdGlyphsProcPtr ``` |

Modified [QDTextProcPtr](https://developer.apple.com/documentation/applicationservices/qdtextprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDTextProcPtr = (Int16, UnsafePointer<Void>, Point, Point) -> Void ``` |
| To | ``` typealias QDTextProcPtr = (Int16, UnsafeRawPointer?, Point, Point) -> Swift.Void ``` |

Modified [QDTextUPP](https://developer.apple.com/documentation/applicationservices/qdtextupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDTextUPP = QDTextProcPtr ``` |
| To | ``` typealias QDTextUPP = ApplicationServices.QDTextProcPtr ``` |

Modified [QDTxMeasProcPtr](https://developer.apple.com/documentation/applicationservices/qdtxmeasprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDTxMeasProcPtr = (Int16, UnsafePointer<Void>, UnsafeMutablePointer<Point>, UnsafeMutablePointer<Point>, UnsafeMutablePointer<FontInfo>) -> Int16 ``` |
| To | ``` typealias QDTxMeasProcPtr = (Int16, UnsafeRawPointer?, UnsafeMutablePointer<Point>?, UnsafeMutablePointer<Point>?, UnsafeMutablePointer<FontInfo>?) -> Int16 ``` |

Modified [QDTxMeasUPP](https://developer.apple.com/documentation/applicationservices/qdtxmeasupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias QDTxMeasUPP = QDTxMeasProcPtr ``` |
| To | ``` typealias QDTxMeasUPP = ApplicationServices.QDTxMeasProcPtr ``` |

Modified [RedrawBackgroundProcPtr](https://developer.apple.com/documentation/applicationservices/redrawbackgroundprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias RedrawBackgroundProcPtr = (ATSUTextLayout, UniCharArrayOffset, Int, UnsafeMutablePointer<ATSTrapezoid>, Int) -> DarwinBoolean ``` |
| To | ``` typealias RedrawBackgroundProcPtr = (ATSUTextLayout?, UniCharArrayOffset, Int, UnsafeMutablePointer<ATSTrapezoid>?, Int) -> DarwinBoolean ``` |

Modified [RedrawBackgroundUPP](https://developer.apple.com/documentation/applicationservices/redrawbackgroundupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias RedrawBackgroundUPP = RedrawBackgroundProcPtr ``` |
| To | ``` typealias RedrawBackgroundUPP = ApplicationServices.RedrawBackgroundProcPtr ``` |

Modified [RegionToRectsProcPtr](https://developer.apple.com/documentation/applicationservices/regiontorectsprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias RegionToRectsProcPtr = (UInt16, RgnHandle, UnsafePointer<Rect>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias RegionToRectsProcPtr = (UInt16, RgnHandle?, UnsafePointer<Rect>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [RegionToRectsUPP](https://developer.apple.com/documentation/applicationservices/regiontorectsupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias RegionToRectsUPP = RegionToRectsProcPtr ``` |
| To | ``` typealias RegionToRectsUPP = ApplicationServices.RegionToRectsProcPtr ``` |

Modified RgnHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias RgnHandle = COpaquePointer ``` |
| To | ``` typealias RgnHandle = OpaquePointer ``` |

Modified [SetIconFamilyData(_: IconFamilyHandle!, _: OSType, _: Handle!) -> OSErr](https://developer.apple.com/documentation/applicationservices/1462050-seticonfamilydata)

|  | Declaration |
| --- | --- |
| From | ``` func SetIconFamilyData(_ iconFamily: IconFamilyHandle, _ iconType: OSType, _ h: Handle) -> OSErr ``` |
| To | ``` func SetIconFamilyData(_ iconFamily: IconFamilyHandle!, _ iconType: OSType, _ h: Handle!) -> OSErr ``` |

Modified [SetSpeechProperty(_: SpeechChannel, _: CFString, _: CFTypeRef?) -> OSErr](https://developer.apple.com/documentation/applicationservices/1459256-setspeechproperty)

|  | Declaration |
| --- | --- |
| From | ``` func SetSpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: AnyObject?) -> OSErr ``` |
| To | ``` func SetSpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: CFTypeRef?) -> OSErr ``` |

Modified [SizeResourceRecHandle](https://developer.apple.com/documentation/applicationservices/sizeresourcerechandle)

|  | Declaration |
| --- | --- |
| From | ``` typealias SizeResourceRecHandle = UnsafeMutablePointer<SizeResourceRecPtr> ``` |
| To | ``` typealias SizeResourceRecHandle = UnsafeMutablePointer<SizeResourceRecPtr?> ``` |

Modified [SpeechDoneProcPtr](https://developer.apple.com/documentation/applicationservices/speechdoneprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechDoneProcPtr = (SpeechChannel, SRefCon) -> Void ``` |
| To | ``` typealias SpeechDoneProcPtr = (SpeechChannel, SRefCon) -> Swift.Void ``` |

Modified [SpeechDoneUPP](https://developer.apple.com/documentation/applicationservices/speechdoneupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechDoneUPP = SpeechDoneProcPtr ``` |
| To | ``` typealias SpeechDoneUPP = ApplicationServices.SpeechDoneProcPtr ``` |

Modified [SpeechErrorCFProcPtr](https://developer.apple.com/documentation/applicationservices/speecherrorcfprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechErrorCFProcPtr = (SpeechChannel, SRefCon, CFError) -> Void ``` |
| To | ``` typealias SpeechErrorCFProcPtr = (SpeechChannel, SRefCon, CFError) -> Swift.Void ``` |

Modified [SpeechErrorProcPtr](https://developer.apple.com/documentation/applicationservices/speecherrorprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechErrorProcPtr = (SpeechChannel, SRefCon, OSErr, Int) -> Void ``` |
| To | ``` typealias SpeechErrorProcPtr = (SpeechChannel, SRefCon, OSErr, Int) -> Swift.Void ``` |

Modified [SpeechErrorUPP](https://developer.apple.com/documentation/applicationservices/speecherrorupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechErrorUPP = SpeechErrorProcPtr ``` |
| To | ``` typealias SpeechErrorUPP = ApplicationServices.SpeechErrorProcPtr ``` |

Modified [SpeechPhonemeProcPtr](https://developer.apple.com/documentation/applicationservices/speechphonemeprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechPhonemeProcPtr = (SpeechChannel, SRefCon, Int16) -> Void ``` |
| To | ``` typealias SpeechPhonemeProcPtr = (SpeechChannel, SRefCon, Int16) -> Swift.Void ``` |

Modified [SpeechPhonemeUPP](https://developer.apple.com/documentation/applicationservices/speechphonemeupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechPhonemeUPP = SpeechPhonemeProcPtr ``` |
| To | ``` typealias SpeechPhonemeUPP = ApplicationServices.SpeechPhonemeProcPtr ``` |

Modified [SpeechSyncProcPtr](https://developer.apple.com/documentation/applicationservices/speechsyncprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechSyncProcPtr = (SpeechChannel, SRefCon, OSType) -> Void ``` |
| To | ``` typealias SpeechSyncProcPtr = (SpeechChannel, SRefCon, OSType) -> Swift.Void ``` |

Modified [SpeechSyncUPP](https://developer.apple.com/documentation/applicationservices/speechsyncupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechSyncUPP = SpeechSyncProcPtr ``` |
| To | ``` typealias SpeechSyncUPP = ApplicationServices.SpeechSyncProcPtr ``` |

Modified [SpeechTextDoneProcPtr](https://developer.apple.com/documentation/applicationservices/speechtextdoneprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechTextDoneProcPtr = (SpeechChannel, SRefCon, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<Int32>) -> Void ``` |
| To | ``` typealias SpeechTextDoneProcPtr = (SpeechChannel, SRefCon, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<Int32>) -> Swift.Void ``` |

Modified [SpeechTextDoneUPP](https://developer.apple.com/documentation/applicationservices/speechtextdoneupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechTextDoneUPP = SpeechTextDoneProcPtr ``` |
| To | ``` typealias SpeechTextDoneUPP = ApplicationServices.SpeechTextDoneProcPtr ``` |

Modified [SpeechWordCFProcPtr](https://developer.apple.com/documentation/applicationservices/speechwordcfprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechWordCFProcPtr = (SpeechChannel, SRefCon, CFString, CFRange) -> Void ``` |
| To | ``` typealias SpeechWordCFProcPtr = (SpeechChannel, SRefCon, CFString, CFRange) -> Swift.Void ``` |

Modified [SpeechWordProcPtr](https://developer.apple.com/documentation/applicationservices/speechwordprocptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechWordProcPtr = (SpeechChannel, SRefCon, UInt, UInt16) -> Void ``` |
| To | ``` typealias SpeechWordProcPtr = (SpeechChannel, SRefCon, UInt, UInt16) -> Swift.Void ``` |

Modified [SpeechWordUPP](https://developer.apple.com/documentation/applicationservices/speechwordupp)

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechWordUPP = SpeechWordProcPtr ``` |
| To | ``` typealias SpeechWordUPP = ApplicationServices.SpeechWordProcPtr ``` |

Modified [TransformProcessType(_: UnsafePointer<ProcessSerialNumber>!, _: ProcessApplicationTransformState) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1462420-transformprocesstype)

|  | Declaration |
| --- | --- |
| From | ``` func TransformProcessType(_ psn: UnsafePointer<ProcessSerialNumber>, _ transformState: ProcessApplicationTransformState) -> OSStatus ``` |
| To | ``` func TransformProcessType(_ psn: UnsafePointer<ProcessSerialNumber>!, _ transformState: ProcessApplicationTransformState) -> OSStatus ``` |

Modified [TranslationCopyDestinationType(_: Translation!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459620-translationcopydestinationtype)

|  | Declaration |
| --- | --- |
| From | ``` func TranslationCopyDestinationType(_ inTranslation: Translation!, _ outDestinationType: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func TranslationCopyDestinationType(_ inTranslation: Translation!, _ outDestinationType: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus ``` |

Modified [TranslationCopySourceType(_: Translation!, _: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459344-translationcopysourcetype)

|  | Declaration |
| --- | --- |
| From | ``` func TranslationCopySourceType(_ inTranslation: Translation!, _ outSourceType: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func TranslationCopySourceType(_ inTranslation: Translation!, _ outSourceType: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus ``` |

Modified [TranslationCreate(_: CFString!, _: CFString!, _: TranslationFlags, _: UnsafeMutablePointer<Unmanaged<Translation>?>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459231-translationcreate)

|  | Declaration |
| --- | --- |
| From | ``` func TranslationCreate(_ inSourceType: CFString!, _ inDestinationType: CFString!, _ inTranslationFlags: TranslationFlags, _ outTranslation: UnsafeMutablePointer<Unmanaged<Translation>?>) -> OSStatus ``` |
| To | ``` func TranslationCreate(_ inSourceType: CFString!, _ inDestinationType: CFString!, _ inTranslationFlags: TranslationFlags, _ outTranslation: UnsafeMutablePointer<Unmanaged<Translation>?>!) -> OSStatus ``` |

Modified [TranslationCreateWithSourceArray(_: CFArray!, _: TranslationFlags, _: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464306-translationcreatewithsourcearray)

|  | Declaration |
| --- | --- |
| From | ``` func TranslationCreateWithSourceArray(_ inSourceTypes: CFArray!, _ inTranslationFlags: TranslationFlags, _ outDestinationTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outTranslations: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func TranslationCreateWithSourceArray(_ inSourceTypes: CFArray!, _ inTranslationFlags: TranslationFlags, _ outDestinationTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _ outTranslations: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!) -> OSStatus ``` |

Modified [TranslationGetTranslationFlags(_: Translation!, _: UnsafeMutablePointer<TranslationFlags>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1459307-translationgettranslationflags)

|  | Declaration |
| --- | --- |
| From | ``` func TranslationGetTranslationFlags(_ inTranslation: Translation!, _ outTranslationFlags: UnsafeMutablePointer<TranslationFlags>) -> OSStatus ``` |
| To | ``` func TranslationGetTranslationFlags(_ inTranslation: Translation!, _ outTranslationFlags: UnsafeMutablePointer<TranslationFlags>!) -> OSStatus ``` |

Modified [TranslationPerformForData(_: Translation!, _: CFData!, _: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460828-translationperformfordata)

|  | Declaration |
| --- | --- |
| From | ``` func TranslationPerformForData(_ inTranslation: Translation!, _ inSourceData: CFData!, _ outDestinationData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func TranslationPerformForData(_ inTranslation: Translation!, _ inSourceData: CFData!, _ outDestinationData: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> OSStatus ``` |

Modified [TranslationPerformForFile(_: Translation!, _: UnsafePointer<FSRef>!, _: UnsafePointer<FSRef>!, _: CFString!, _: UnsafeMutablePointer<FSRef>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1464541-translationperformforfile)

|  | Declaration |
| --- | --- |
| From | ``` func TranslationPerformForFile(_ inTranslation: Translation!, _ inSourceFile: UnsafePointer<FSRef>, _ inDestinationDirectory: UnsafePointer<FSRef>, _ inDestinationName: CFString!, _ outTranslatedFile: UnsafeMutablePointer<FSRef>) -> OSStatus ``` |
| To | ``` func TranslationPerformForFile(_ inTranslation: Translation!, _ inSourceFile: UnsafePointer<FSRef>!, _ inDestinationDirectory: UnsafePointer<FSRef>!, _ inDestinationName: CFString!, _ outTranslatedFile: UnsafeMutablePointer<FSRef>!) -> OSStatus ``` |

Modified [TranslationPerformForURL(_: Translation!, _: CFURL!, _: CFURL!, _: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1460118-translationperformforurl)

|  | Declaration |
| --- | --- |
| From | ``` func TranslationPerformForURL(_ inTranslation: Translation!, _ inSourceURL: CFURL!, _ inDestinationURL: CFURL!, _ outTranslatedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func TranslationPerformForURL(_ inTranslation: Translation!, _ inSourceURL: CFURL!, _ inDestinationURL: CFURL!, _ outTranslatedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>!) -> OSStatus ``` |

Modified [UAZoomChangeFocus(_: UnsafePointer<CGRect>!, _: UnsafePointer<CGRect>!, _: UAZoomChangeFocusType) -> OSStatus](https://developer.apple.com/documentation/applicationservices/1458830-uazoomchangefocus)

|  | Declaration |
| --- | --- |
| From | ``` func UAZoomChangeFocus(_ inRect: UnsafePointer<CGRect>, _ inHighlightRect: UnsafePointer<CGRect>, _ inType: UAZoomChangeFocusType) -> OSStatus ``` |
| To | ``` func UAZoomChangeFocus(_ inRect: UnsafePointer<CGRect>!, _ inHighlightRect: UnsafePointer<CGRect>!, _ inType: UAZoomChangeFocusType) -> OSStatus ``` |

Modified WindowPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias WindowPtr = COpaquePointer ``` |
| To | ``` typealias WindowPtr = OpaquePointer ``` |

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
