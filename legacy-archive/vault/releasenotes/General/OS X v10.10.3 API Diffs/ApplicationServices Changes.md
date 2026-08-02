---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/ApplicationServices.html
archived_at: '2026-07-18T02:52:04.782440Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# ApplicationServices Changes

## ApplicationServices

Removed ATSFONTREF_DEFINEDAdded ATSFSSpec.init()Added ATSFSSpec.init(vRefNum: FSVolumeRefNum, parID: Int32, name: StrFileName)Added ATSFlatDataFontNameDataHeader.init()Added ATSFlatDataFontNameDataHeader.init(nameSpecifierType: ATSFlatDataFontSpeciferType, nameSpecifierSize: UInt32)Added ATSFlatDataFontSpecRawNameData.init()Added ATSFlatDataFontSpecRawNameData.init(fontNameType: FontNameCode, fontNamePlatform: FontPlatformCode, fontNameScript: FontScriptCode, fontNameLanguage: FontLanguageCode, fontNameLength: UInt32)Added ATSFlatDataFontSpecRawNameDataHeader.init()Added ATSFlatDataFontSpecRawNameDataHeader.init(numberOfFlattenedNames: UInt32, nameDataArray:(ATSFlatDataFontSpecRawNameData))Added ATSFlatDataLayoutControlsDataHeader.init()Added ATSFlatDataLayoutControlsDataHeader.init(numberOfLayoutControls: UInt32, controlArray:(ATSUAttributeInfo))Added ATSFlatDataLineInfoData.init()Added ATSFlatDataLineInfoData.init(lineLength: UInt32, numberOfLineControls: UInt32)Added ATSFlatDataLineInfoHeader.init()Added ATSFlatDataLineInfoHeader.init(numberOfLines: UInt32, lineInfoArray:(ATSFlatDataLineInfoData))Added ATSFlatDataMainHeaderBlock.init()Added ATSFlatDataMainHeaderBlock.init(version: UInt32, sizeOfDataBlock: UInt32, offsetToTextLayouts: UInt32, offsetToStyleRuns: UInt32, offsetToStyleList: UInt32)Added ATSFlatDataStyleListFeatureData.init()Added ATSFlatDataStyleListFeatureData.init(theFeatureType: ATSUFontFeatureType, theFeatureSelector: ATSUFontFeatureSelector)Added ATSFlatDataStyleListHeader.init()Added ATSFlatDataStyleListHeader.init(numberOfStyles: UInt32, styleDataArray:(ATSFlatDataStyleListStyleDataHeader))Added ATSFlatDataStyleListStyleDataHeader.init()Added ATSFlatDataStyleListStyleDataHeader.init(sizeOfStyleInfo: UInt32, numberOfSetAttributes: UInt32, numberOfSetFeatures: UInt32, numberOfSetVariations: UInt32)Added ATSFlatDataStyleListVariationData.init()Added ATSFlatDataStyleListVariationData.init(theVariationAxis: ATSUFontVariationAxis, theVariationValue: ATSUFontVariationValue)Added ATSFlatDataStyleRunDataHeader.init()Added ATSFlatDataStyleRunDataHeader.init(numberOfStyleRuns: UInt32, styleRunArray:(ATSUStyleRunInfo))Added ATSFlatDataTextLayoutDataHeader.init()Added ATSFlatDataTextLayoutDataHeader.init(sizeOfLayoutData: UInt32, textLayoutLength: UInt32, offsetToLayoutControls: UInt32, offsetToLineInfo: UInt32)Added ATSFlatDataTextLayoutHeader.init()Added ATSFlatDataTextLayoutHeader.init(numFlattenedTextLayouts: UInt32, flattenedTextLayouts:(ATSFlatDataTextLayoutDataHeader))Added ATSFontFilter.init()Added ATSFontMetrics.init()Added ATSFontMetrics.init(version: UInt32, ascent: CGFloat, descent: CGFloat, leading: CGFloat, avgAdvanceWidth: CGFloat, maxAdvanceWidth: CGFloat, minLeftSideBearing: CGFloat, minRightSideBearing: CGFloat, stemWidth: CGFloat, stemHeight: CGFloat, capHeight: CGFloat, xHeight: CGFloat, italicAngle: CGFloat, underlinePosition: CGFloat, underlineThickness: CGFloat)Added ATSFontQuerySourceContext.init()Added ATSFontQuerySourceContext.init(version: UInt32, refCon: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack)Added ATSGlyphIdealMetrics.init()Added ATSGlyphIdealMetrics.init(advance: ATSPoint, sideBearing: ATSPoint, otherSideBearing: ATSPoint)Added ATSGlyphScreenMetrics.init()Added ATSGlyphScreenMetrics.init(deviceAdvance: ATSPoint, topLeft: ATSPoint, height: UInt32, width: UInt32, sideBearing: ATSPoint, otherSideBearing: ATSPoint)Added ATSJustWidthDeltaEntryOverride.init()Added ATSJustWidthDeltaEntryOverride.init(beforeGrowLimit: Fixed, beforeShrinkLimit: Fixed, afterGrowLimit: Fixed, afterShrinkLimit: Fixed, growFlags: JustificationFlags, shrinkFlags: JustificationFlags)Added ATSLayoutRecord.init()Added ATSLayoutRecord.init(glyphID: ATSGlyphRef, flags: ATSGlyphInfoFlags, originalOffset: Int, realPos: Fixed)Added ATSTrapezoid.init()Added ATSTrapezoid.init(upperLeft: FixedPoint, upperRight: FixedPoint, lowerRight: FixedPoint, lowerLeft: FixedPoint)Added ATSUAttributeInfo.init()Added ATSUAttributeInfo.init(fTag: ATSUAttributeTag, fValueSize: Int)Added ATSUBackgroundData [struct]Added ATSUBackgroundData.init()Added ATSUCaret.init()Added ATSUCaret.init(fX: Fixed, fY: Fixed, fDeltaX: Fixed, fDeltaY: Fixed)Added ATSUCurvePath.init()Added ATSUCurvePath.init(vectors: UInt32, controlBits:(UInt32), vector:(ATSPoint))Added ATSUCurvePaths.init()Added ATSUCurvePaths.init(contours: UInt32, contour:(ATSUCurvePath))Added ATSUGlyphInfo.init()Added ATSUGlyphInfo.init(glyphID: GlyphID, reserved: UInt16, layoutFlags: UInt32, charIndex: UniCharArrayOffset, style: ATSUStyle, deltaY: Float32, idealX: Float32, screenX: Int16, caretX: Int16)Added ATSUGlyphInfoArray.init()Added ATSUGlyphInfoArray.init(layout: ATSUTextLayout, numGlyphs: Int, glyphs:(ATSUGlyphInfo))Added ATSUGlyphSelector.init()Added ATSUGlyphSelector.init(collection: GlyphCollection, glyphID: GlyphID)Added ATSULayoutOperationOverrideSpecifier.init()Added ATSULayoutOperationOverrideSpecifier.init(operationSelector: ATSULayoutOperationSelector, overrideUPP: ATSUDirectLayoutOperationOverrideUPP)Added ATSURGBAlphaColor.init()Added ATSURGBAlphaColor.init(red: Float, green: Float, blue: Float, alpha: Float)Added ATSUStyleRunInfo.init()Added ATSUStyleRunInfo.init(runLength: UInt32, styleObjectIndex: UInt32)Added ATSUTab.init()Added ATSUTab.init(tabPosition: ATSUTextMeasurement, tabType: ATSUTabType)Added ATSUUnhighlightData.init()Added ATSUUnhighlightData.init(dataType: ATSUBackgroundDataType, unhighlightData: ATSUBackgroundData)Added ATSUUnhighlightData.unhighlightDataAdded AppParameters.init()Added AsscEntry.init()Added AsscEntry.init(fontSize: Int16, fontStyle: Int16, fontID: Int16)Added BitMap.init()Added BitMap.init(baseAddr: Ptr, rowBytes: Int16, bounds: Rect)Added CM2Profile.init()Added CM2Profile.init(header: CM2Header, tagTable: CMTagElemTable, elemData:(Int8))Added CMDeviceInfo.init()Added CMDeviceInfo.init(dataVersion: UInt32, deviceClass: CMDeviceClass, deviceID: CMDeviceID, deviceScope: CMDeviceScope, deviceState: CMDeviceState, defaultProfileID: CMDeviceProfileID, deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, profileCount: UInt32, reserved: UInt32)Added CMDeviceProfileArray.init()Added CMDeviceProfileArray.init(profileCount: UInt32, profiles:(CMDeviceProfileInfo))Added CMDeviceScope.init()Added CMDeviceScope.init(deviceUser: Unmanaged<CFString>!, deviceHost: Unmanaged<CFString>!)Added CMMultiFunctLutType.init()Added CMMultiFunctLutType.init(typeDescriptor: OSType, reserved: UInt32, inputChannels: UInt8, outputChannels: UInt8, reserved2: UInt16, offsetBcurves: UInt32, offsetMatrix: UInt32, offsetMcurves: UInt32, offsetCLUT: UInt32, offsetAcurves: UInt32, data:(UInt8))Added CMXYZColor.init()Added CMXYZColor.init(X: CMXYZComponent, Y: CMXYZComponent, Z: CMXYZComponent)Added CQDProcs.init()Added CQDProcs.init(textProc: QDTextUPP, lineProc: QDLineUPP, rectProc: QDRectUPP, rRectProc: QDRRectUPP, ovalProc: QDOvalUPP, arcProc: QDArcUPP, polyProc: QDPolyUPP, rgnProc: QDRgnUPP, bitsProc: QDBitsUPP, commentProc: QDCommentUPP, txMeasProc: QDTxMeasUPP, getPicProc: QDGetPicUPP, putPicProc: QDPutPicUPP, opcodeProc: QDOpcodeUPP, newProc1: UniversalProcPtr, glyphsProc: QDStdGlyphsUPP, printerStatusProc: QDPrinterStatusUPP, newProc4: UniversalProcPtr, newProc5: UniversalProcPtr, newProc6: UniversalProcPtr)Added ColorSpec.init()Added ColorSpec.init(value: Int16, rgb: RGBColor)Added ColorSyncMD5.init()Added ColorSyncMD5.init(digest: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added ColorTable.init()Added ColorTable.init(ctSeed: Int32, ctFlags: Int16, ctSize: Int16, ctTable: CSpecArray)Added DCMDictionaryHeader.init()Added DCMDictionaryHeader.init(headerSignature: FourCharCode, headerVersion: UInt32, headerSize: UInt32, accessMethod: Str63)Added DelimiterInfo.init()Added DelimiterInfo.init(startDelimiter: (UInt8, UInt8), endDelimiter:(UInt8, UInt8))Added FMFilter.init()Added FMFontDirectoryFilter.init()Added FMFontDirectoryFilter.init(fontFolderDomain: Int16, reserved:(UInt32, UInt32))Added FMFontFamilyInstance.init()Added FMFontFamilyInstance.init(fontFamily: FMFontFamily, fontStyle: FMFontStyle)Added FMFontFamilyInstanceIterator.init()Added FMFontFamilyInstanceIterator.init(reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added FMFontFamilyIterator.init()Added FMFontFamilyIterator.init(reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added FMFontIterator.init()Added FMFontIterator.init(reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added FMInput.init()Added FMInput.init(family: Int16, size: Int16, face: Style, needBits: Boolean, device: Int16, numer: Point, denom: Point)Added FamRec.init()Added FamRec.init(ffFlags: Int16, ffFamID: Int16, ffFirstChar: Int16, ffLastChar: Int16, ffAscent: Int16, ffDescent: Int16, ffLeading: Int16, ffWidMax: Int16, ffWTabOff: Int32, ffKernOff: Int32, ffStylOff: Int32, ffProperty:(Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16), ffIntl:(Int16, Int16), ffVersion: Int16)Added FontAssoc.init()Added FontAssoc.init(numAssoc: Int16)Added FontInfo.init()Added FontInfo.init(ascent: Int16, descent: Int16, widMax: Int16, leading: Int16)Added FontRec.init()Added FontRec.init(fontType: Int16, firstChar: Int16, lastChar: Int16, widMax: Int16, kernMax: Int16, nDescent: Int16, fRectWidth: Int16, fRectHeight: Int16, owTLoc: UInt16, ascent: Int16, descent: Int16, leading: Int16, rowWords: Int16)Added GDevice.init()Added GDevice.init(gdRefNum: Int16, gdID: Int16, gdType: Int16, gdITable: Handle, gdResPref: Int16, gdSearchProc: Handle, gdCompProc: Handle, gdFlags: Int16, gdPMap: PixMapHandle, gdRefCon: Int32, gdNextGD: GDHandle, gdRect: Rect, gdMode: Int32, gdCCBytes: Int16, gdCCDepth: Int16, gdCCXData: Handle, gdCCXMask: Handle, gdExt: Handle)Added GrafPort.init()Added GrafPort.init(whatever: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16))Added HomographDicInfoRec.init()Added HomographDicInfoRec.init(dictionaryID: DCMDictionaryID, uniqueID: DCMUniqueID)Added ICAppSpec.init()Added ICAppSpec.init(fCreator: OSType, name: Str63)Added ICAppSpecList.init()Added ICAppSpecList.init(numberOfItems: Int16, appSpecs:(ICAppSpec))Added ICCharTable.init()Added ICCharTable.init(netToMac: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), macToNet:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added ICFileSpec.init()Added ICFileSpec.init(volName: Str31, volCreationDate: Int32, fss: FSSpec, alias: AliasRecord)Added ICFontRecord.init()Added ICFontRecord.init(size: Int16, face: Style, pad: Int8, font: Str255)Added ICMapEntry.init()Added ICMapEntry.init(totalLength: Int16, fixedLength: ICFixedLength, version: Int16, fileType: OSType, fileCreator: OSType, postCreator: OSType, flags: ICMapEntryFlags, extension: Str255, creatorAppName: Str255, postAppName: Str255, MIMEType: Str255, entryName: Str255)Added ICServiceEntry.init()Added ICServiceEntry.init(name: Str255, port: Int16, flags: ICServiceEntryFlags)Added ICServices.init()Added ICServices.init(count: Int16, services:(ICServiceEntry))Added KernEntry.init()Added KernEntry.init(kernStyle: Int16, kernLength: Int16)Added KernPair.init()Added KernPair.init(kernFirst: Int8, kernSecond: Int8, kernWidth: Int16)Added KernTable.init()Added KernTable.init(numKerns: Int16)Added LAMorphemeRec.init()Added LAMorphemeRec.init(sourceTextLength: UInt32, sourceTextPtr: LogicalAddress, morphemeTextLength: UInt32, morphemeTextPtr: LogicalAddress, partOfSpeech: UInt32)Added LAMorphemesArray.init()Added LAMorphemesArray.init(morphemesCount: Int, processedTextLength: UInt32, morphemesTextLength: UInt32, morphemes:(LAMorphemeRec))Added LaunchParamBlockRec.init()Added LaunchParamBlockRec.init(reserved1: UInt32, reserved2: UInt16, launchBlockID: UInt16, launchEPBLength: UInt32, launchFileFlags: UInt16, launchControlFlags: LaunchFlags, launchAppRef: FSRefPtr, launchProcessSN: ProcessSerialNumber, launchPreferredSize: UInt32, launchMinimumSize: UInt32, launchAvailableSize: UInt32, launchAppParameters: AppParametersPtr)Added MacPolygon.init()Added MacPolygon.init(polySize: Int16, polyBBox: Rect, polyPoints:(Point))Added MorphemeTextRange.init()Added MorphemeTextRange.init(sourceOffset: UInt32, length: UInt32)Added NameTable.init()Added NameTable.init(stringCount: Int16, baseFontName: Str255)Added OpenCPicParams.init()Added OpenCPicParams.init(srcRect: Rect, hRes: Fixed, vRes: Fixed, version: Int16, reserved1: Int16, reserved2: Int32)Added PMLanguageInfo.init()Added PMLanguageInfo.init(level: Str32, version: Str32, release: Str32)Added PMRect.init()Added PMRect.init(top: Double, left: Double, bottom: Double, right: Double)Added PMResolution.init()Added PMResolution.init(hRes: Double, vRes: Double)Added Pattern.init()Added Pattern.init(pat: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added PhonemeDescriptor.init()Added PhonemeDescriptor.init(phonemeCount: Int16, thePhonemes:(PhonemeInfo))Added PhonemeInfo.init()Added PhonemeInfo.init(opcode: Int16, phStr: Str15, exampleStr: Str31, hiliteStart: Int16, hiliteEnd: Int16)Added Picture.init()Added Picture.init(picSize: Int16, picFrame: Rect)Added PixMap.init()Added PixMap.init(baseAddr: Ptr, rowBytes: Int16, bounds: Rect, pmVersion: Int16, packType: Int16, packSize: Int32, hRes: Fixed, vRes: Fixed, pixelType: Int16, pixelSize: Int16, cmpCount: Int16, cmpSize: Int16, pixelFormat: OSType, pmTable: CTabHandle, pmExt: UnsafeMutablePointer<Void>)Added PixPat.init()Added PixPat.init(patType: Int16, patMap: PixMapHandle, patData: Handle, patXData: Handle, patXValid: Int16, patXMap: Handle, pat1Data: Pattern)Added ProcessInfoExtendedRec.init()Added ProcessInfoExtendedRec.init(processInfoLength: UInt32, processName: StringPtr, processNumber: ProcessSerialNumber, processType: UInt32, processSignature: OSType, processMode: UInt32, processLocation: Ptr, processSize: UInt32, processFreeMem: UInt32, processLauncher: ProcessSerialNumber, processLaunchDate: UInt32, processActiveTime: UInt32, processAppRef: FSRefPtr, processTempMemTotal: UInt32, processPurgeableTempMemTotal: UInt32)Added ProcessInfoRec.init()Added ProcessInfoRec.init(processInfoLength: UInt32, processName: StringPtr, processNumber: ProcessSerialNumber, processType: UInt32, processSignature: OSType, processMode: UInt32, processLocation: Ptr, processSize: UInt32, processFreeMem: UInt32, processLauncher: ProcessSerialNumber, processLaunchDate: UInt32, processActiveTime: UInt32, processAppRef: FSRefPtr)Added RGBColor.init()Added RGBColor.init(red: UInt16, green: UInt16, blue: UInt16)Added SizeResourceRec.init()Added SizeResourceRec.init(flags: UInt16, preferredHeapSize: UInt32, minimumHeapSize: UInt32)Added SpeechChannelRecord.init()Added SpeechChannelRecord.init(data: (Int))Added SpeechErrorInfo.init()Added SpeechErrorInfo.init(count: Int16, oldest: OSErr, oldPos: Int, newest: OSErr, newPos: Int)Added SpeechStatusInfo.init()Added SpeechStatusInfo.init(outputBusy: Boolean, outputPaused: Boolean, inputBytesLeft: Int, phonemeCode: Int16)Added SpeechVersionInfo.init()Added SpeechVersionInfo.init(synthType: OSType, synthSubType: OSType, synthManufacturer: OSType, synthFlags: Int32, synthVersion: NumVersion)Added SpeechXtndData.init()Added SpeechXtndData.init(synthCreator: OSType, synthData:(UInt8, UInt8))Added StyleTable.init()Added StyleTable.init(fontClass: Int16, offset: Int32, reserved: Int32, indexes:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added VDGammaRecord.init()Added VDGammaRecord.init(csGTable: Ptr)Added VoiceDescription.init()Added VoiceDescription.init(length: Int32, voice: VoiceSpec, version: Int32, name: Str63, comment: Str255, gender: Int16, age: Int16, script: Int16, language: Int16, region: Int16, reserved:(Int32, Int32, Int32, Int32))Added VoiceFileInfo.init()Added VoiceFileInfo.init(fileSpec: FSSpec, resID: Int16)Added VoiceSpec.init()Added VoiceSpec.init(creator: OSType, id: OSType)Added kATSFontNameTableBytesAdded kATSFontNameTableCodeAdded kATSFontNameTableLanguageAdded kATSFontNameTablePlatformAdded kATSFontNameTableScriptAdded kATSQueryClientPIDAdded kATSQueryFontNameAdded kATSQueryFontNameTableEntriesAdded kATSQueryFontPostScriptNameAdded kATSQueryQDFamilyNameAdded kAXAMPMFieldAttributeAdded kAXAllowedValuesAttributeAdded kAXAlternateUIVisibleAttributeAdded kAXAnnouncementKeyAdded kAXAnnouncementRequestedNotificationAdded kAXApplicationActivatedNotificationAdded kAXApplicationDeactivatedNotificationAdded kAXApplicationDockItemSubroleAdded kAXApplicationHiddenNotificationAdded kAXApplicationRoleAdded kAXApplicationShownNotificationAdded kAXAscendingSortDirectionValueAdded kAXAttributedStringForRangeParameterizedAttributeAdded kAXBoundsForRangeParameterizedAttributeAdded kAXBrowserRoleAdded kAXBusyIndicatorRoleAdded kAXButtonRoleAdded kAXCancelActionAdded kAXCancelButtonAttributeAdded kAXCellForColumnAndRowParameterizedAttributeAdded kAXCellRoleAdded kAXCheckBoxRoleAdded kAXChildrenAttributeAdded kAXClearButtonAttributeAdded kAXCloseButtonAttributeAdded kAXCloseButtonSubroleAdded kAXColorWellRoleAdded kAXColumnCountAttributeAdded kAXColumnHeaderUIElementsAttributeAdded kAXColumnIndexRangeAttributeAdded kAXColumnRoleAdded kAXColumnTitleAttributeAdded kAXColumnTitlesAttributeAdded kAXColumnsAttributeAdded kAXComboBoxRoleAdded kAXConfirmActionAdded kAXContentListSubroleAdded kAXContentsAttributeAdded kAXCreatedNotificationAdded kAXCriticalValueAttributeAdded kAXDateFieldRoleAdded kAXDayFieldAttributeAdded kAXDecrementActionAdded kAXDecrementArrowSubroleAdded kAXDecrementButtonAttributeAdded kAXDecrementPageSubroleAdded kAXDefaultButtonAttributeAdded kAXDefinitionListSubroleAdded kAXDescendingSortDirectionValueAdded kAXDescriptionAdded kAXDescriptionAttributeAdded kAXDescriptionListSubroleAdded kAXDialogSubroleAdded kAXDisclosedByRowAttributeAdded kAXDisclosedRowsAttributeAdded kAXDisclosingAttributeAdded kAXDisclosureLevelAttributeAdded kAXDisclosureTriangleRoleAdded kAXDockExtraDockItemSubroleAdded kAXDockItemRoleAdded kAXDocumentAttributeAdded kAXDocumentDockItemSubroleAdded kAXDrawerCreatedNotificationAdded kAXDrawerRoleAdded kAXEditedAttributeAdded kAXElementBusyAttributeAdded kAXElementBusyChangedNotificationAdded kAXEnabledAttributeAdded kAXExpandedAttributeAdded kAXExtrasMenuBarAttributeAdded kAXFilenameAttributeAdded kAXFloatingWindowSubroleAdded kAXFocusedApplicationAttributeAdded kAXFocusedAttributeAdded kAXFocusedUIElementAttributeAdded kAXFocusedUIElementChangedNotificationAdded kAXFocusedWindowAttributeAdded kAXFocusedWindowChangedNotificationAdded kAXFolderDockItemSubroleAdded kAXFrontmostAttributeAdded kAXFullScreenButtonAttributeAdded kAXFullScreenButtonSubroleAdded kAXGridRoleAdded kAXGroupRoleAdded kAXGrowAreaAttributeAdded kAXGrowAreaRoleAdded kAXHandleRoleAdded kAXHandlesAttributeAdded kAXHeaderAttributeAdded kAXHelpAttributeAdded kAXHelpTagCreatedNotificationAdded kAXHelpTagRoleAdded kAXHiddenAttributeAdded kAXHorizontalOrientationValueAdded kAXHorizontalScrollBarAttributeAdded kAXHorizontalUnitDescriptionAttributeAdded kAXHorizontalUnitsAttributeAdded kAXHourFieldAttributeAdded kAXIdentifierAttributeAdded kAXImageRoleAdded kAXIncrementActionAdded kAXIncrementArrowSubroleAdded kAXIncrementButtonAttributeAdded kAXIncrementPageSubroleAdded kAXIncrementorAttributeAdded kAXIncrementorRoleAdded kAXIndexAttributeAdded kAXInsertionPointLineNumberAttributeAdded kAXIsApplicationRunningAttributeAdded kAXIsEditableAttributeAdded kAXLabelUIElementsAttributeAdded kAXLabelValueAttributeAdded kAXLayoutAreaRoleAdded kAXLayoutChangedNotificationAdded kAXLayoutItemRoleAdded kAXLayoutPointForScreenPointParameterizedAttributeAdded kAXLayoutSizeForScreenSizeParameterizedAttributeAdded kAXLevelIndicatorRoleAdded kAXLineForIndexParameterizedAttributeAdded kAXLinkedUIElementsAttributeAdded kAXListRoleAdded kAXMainAttributeAdded kAXMainWindowAttributeAdded kAXMainWindowChangedNotificationAdded kAXMarkerTypeAttributeAdded kAXMarkerTypeDescriptionAttributeAdded kAXMarkerUIElementsAttributeAdded kAXMatteContentUIElementAttributeAdded kAXMatteHoleAttributeAdded kAXMatteRoleAdded kAXMaxValueAttributeAdded kAXMenuBarAttributeAdded kAXMenuBarItemRoleAdded kAXMenuBarRoleAdded kAXMenuButtonRoleAdded kAXMenuClosedNotificationAdded kAXMenuItemCmdCharAttributeAdded kAXMenuItemCmdGlyphAttributeAdded kAXMenuItemCmdModifiersAttributeAdded kAXMenuItemCmdVirtualKeyAttributeAdded kAXMenuItemMarkCharAttributeAdded kAXMenuItemPrimaryUIElementAttributeAdded kAXMenuItemRoleAdded kAXMenuItemSelectedNotificationAdded kAXMenuOpenedNotificationAdded kAXMenuRoleAdded kAXMinValueAttributeAdded kAXMinimizeButtonAttributeAdded kAXMinimizeButtonSubroleAdded kAXMinimizedAttributeAdded kAXMinimizedWindowDockItemSubroleAdded kAXMinuteFieldAttributeAdded kAXModalAttributeAdded kAXMonthFieldAttributeAdded kAXMovedNotificationAdded kAXNextContentsAttributeAdded kAXNumberOfCharactersAttributeAdded kAXOrderedByRowAttributeAdded kAXOrientationAttributeAdded kAXOutlineRoleAdded kAXOutlineRowSubroleAdded kAXOverflowButtonAttributeAdded kAXParentAttributeAdded kAXPickActionAdded kAXPlaceholderValueAttributeAdded kAXPopUpButtonRoleAdded kAXPopoverRoleAdded kAXPositionAttributeAdded kAXPressActionAdded kAXPreviousContentsAttributeAdded kAXPriorityKeyAdded kAXProcessSwitcherListSubroleAdded kAXProgressIndicatorRoleAdded kAXProxyAttributeAdded kAXRTFForRangeParameterizedAttributeAdded kAXRadioButtonRoleAdded kAXRadioGroupRoleAdded kAXRaiseActionAdded kAXRangeForIndexParameterizedAttributeAdded kAXRangeForLineParameterizedAttributeAdded kAXRangeForPositionParameterizedAttributeAdded kAXRatingIndicatorSubroleAdded kAXRelevanceIndicatorRoleAdded kAXResizedNotificationAdded kAXRoleAttributeAdded kAXRoleDescriptionAttributeAdded kAXRowCollapsedNotificationAdded kAXRowCountAttributeAdded kAXRowCountChangedNotificationAdded kAXRowExpandedNotificationAdded kAXRowHeaderUIElementsAttributeAdded kAXRowIndexRangeAttributeAdded kAXRowRoleAdded kAXRowsAttributeAdded kAXRulerMarkerRoleAdded kAXRulerRoleAdded kAXScreenPointForLayoutPointParameterizedAttributeAdded kAXScreenSizeForLayoutSizeParameterizedAttributeAdded kAXScrollAreaRoleAdded kAXScrollBarRoleAdded kAXSearchButtonAttributeAdded kAXSearchFieldSubroleAdded kAXSecondFieldAttributeAdded kAXSecureTextFieldSubroleAdded kAXSelectedAttributeAdded kAXSelectedCellsAttributeAdded kAXSelectedCellsChangedNotificationAdded kAXSelectedChildrenAttributeAdded kAXSelectedChildrenChangedNotificationAdded kAXSelectedChildrenMovedNotificationAdded kAXSelectedColumnsAttributeAdded kAXSelectedColumnsChangedNotificationAdded kAXSelectedRowsAttributeAdded kAXSelectedRowsChangedNotificationAdded kAXSelectedTextAttributeAdded kAXSelectedTextChangedNotificationAdded kAXSelectedTextRangeAttributeAdded kAXSelectedTextRangesAttributeAdded kAXSeparatorDockItemSubroleAdded kAXServesAsTitleForUIElementsAttributeAdded kAXSharedCharacterRangeAttributeAdded kAXSharedFocusElementsAttributeAdded kAXSharedTextUIElementsAttributeAdded kAXSheetCreatedNotificationAdded kAXSheetRoleAdded kAXShowAlternateUIActionAdded kAXShowDefaultUIActionAdded kAXShowMenuActionAdded kAXShownMenuUIElementAttributeAdded kAXSizeAttributeAdded kAXSliderRoleAdded kAXSortButtonSubroleAdded kAXSortDirectionAttributeAdded kAXSplitGroupRoleAdded kAXSplitterRoleAdded kAXSplittersAttributeAdded kAXStandardWindowSubroleAdded kAXStaticTextRoleAdded kAXStringForRangeParameterizedAttributeAdded kAXStyleRangeForIndexParameterizedAttributeAdded kAXSubroleAttributeAdded kAXSwitchSubroleAdded kAXSystemDialogSubroleAdded kAXSystemFloatingWindowSubroleAdded kAXSystemWideRoleAdded kAXTabGroupRoleAdded kAXTableRoleAdded kAXTableRowSubroleAdded kAXTabsAttributeAdded kAXTextAreaRoleAdded kAXTextAttributeAdded kAXTextFieldRoleAdded kAXTimeFieldRoleAdded kAXTimelineSubroleAdded kAXTitleAttributeAdded kAXTitleChangedNotificationAdded kAXTitleUIElementAttributeAdded kAXToggleSubroleAdded kAXToolbarButtonAttributeAdded kAXToolbarButtonSubroleAdded kAXToolbarRoleAdded kAXTopLevelUIElementAttributeAdded kAXTrashDockItemSubroleAdded kAXUIElementDestroyedNotificationAdded kAXUIElementsKeyAdded kAXURLAttributeAdded kAXURLDockItemSubroleAdded kAXUnitDescriptionAttributeAdded kAXUnitsAttributeAdded kAXUnitsChangedNotificationAdded kAXUnknownOrientationValueAdded kAXUnknownRoleAdded kAXUnknownSortDirectionValueAdded kAXUnknownSubroleAdded kAXValueAttributeAdded kAXValueChangedNotificationAdded kAXValueDescriptionAttributeAdded kAXValueIncrementAttributeAdded kAXValueIndicatorRoleAdded kAXValueWrapsAttributeAdded kAXVerticalOrientationValueAdded kAXVerticalScrollBarAttributeAdded kAXVerticalUnitDescriptionAttributeAdded kAXVerticalUnitsAttributeAdded kAXVisibleCellsAttributeAdded kAXVisibleCharacterRangeAttributeAdded kAXVisibleChildrenAttributeAdded kAXVisibleColumnsAttributeAdded kAXVisibleRowsAttributeAdded kAXVisibleTextAttributeAdded kAXWarningValueAttributeAdded kAXWindowAttributeAdded kAXWindowCreatedNotificationAdded kAXWindowDeminiaturizedNotificationAdded kAXWindowMiniaturizedNotificationAdded kAXWindowMovedNotificationAdded kAXWindowResizedNotificationAdded kAXWindowRoleAdded kAXWindowsAttributeAdded kAXYearFieldAttributeAdded kAXZoomButtonAttributeAdded kAXZoomButtonSubroleAdded kCMDefaultDeviceNotificationAdded kCMDefaultDeviceProfileNotificationAdded kCMDeviceOfflineNotificationAdded kCMDeviceOnlineNotificationAdded kCMDeviceProfilesNotificationAdded kCMDeviceRegisteredNotificationAdded kCMDeviceStateNotificationAdded kCMDeviceUnregisteredNotificationAdded kCMDisplayDeviceProfilesNotificationAdded kCMPrefsChangedNotificationAdded kPDFWorkflowDisplayNameKeyAdded kPDFWorkflowItemURLKeyAdded kPDFWorkflowItemsKeyAdded kPMDocumentFormatDefaultAdded kPMDocumentFormatPDFAdded kPMDocumentFormatPostScriptAdded kPMGraphicsContextCoreGraphicsAdded kPMGraphicsContextDefaultAdded kPMPPDDescriptionTypeAdded kPMPresetGraphicsTypeAllAdded kPMPresetGraphicsTypeGeneralAdded kPMPresetGraphicsTypeKeyAdded kPMPresetGraphicsTypeNoneAdded kPMPresetGraphicsTypePhotoAdded kPMPrintSelectionTitleKeyAdded kPasteboardClipboardAdded kPasteboardFindAdded kPasteboardTypeFilePromiseContentAdded kPasteboardTypeFileURLPromiseModified ATSFSSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFSSpec {     var vRefNum: FSVolumeRefNum     var parID: Int32     var name: StrFileName } ``` |
| To | ``` struct ATSFSSpec {     var vRefNum: FSVolumeRefNum     var parID: Int32     var name: StrFileName     init()     init(vRefNum vRefNum: FSVolumeRefNum, parID parID: Int32, name name: StrFileName) } ``` |

Modified ATSFlatDataFontNameDataHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataFontNameDataHeader {     var nameSpecifierType: ATSFlatDataFontSpeciferType     var nameSpecifierSize: UInt32 } ``` |
| To | ``` struct ATSFlatDataFontNameDataHeader {     var nameSpecifierType: ATSFlatDataFontSpeciferType     var nameSpecifierSize: UInt32     init()     init(nameSpecifierType nameSpecifierType: ATSFlatDataFontSpeciferType, nameSpecifierSize nameSpecifierSize: UInt32) } ``` |

Modified ATSFlatDataFontSpecRawNameData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataFontSpecRawNameData {     var fontNameType: FontNameCode     var fontNamePlatform: FontPlatformCode     var fontNameScript: FontScriptCode     var fontNameLanguage: FontLanguageCode     var fontNameLength: UInt32 } ``` |
| To | ``` struct ATSFlatDataFontSpecRawNameData {     var fontNameType: FontNameCode     var fontNamePlatform: FontPlatformCode     var fontNameScript: FontScriptCode     var fontNameLanguage: FontLanguageCode     var fontNameLength: UInt32     init()     init(fontNameType fontNameType: FontNameCode, fontNamePlatform fontNamePlatform: FontPlatformCode, fontNameScript fontNameScript: FontScriptCode, fontNameLanguage fontNameLanguage: FontLanguageCode, fontNameLength fontNameLength: UInt32) } ``` |

Modified ATSFlatDataFontSpecRawNameDataHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataFontSpecRawNameDataHeader {     var numberOfFlattenedNames: UInt32     var nameDataArray: (ATSFlatDataFontSpecRawNameData) } ``` |
| To | ``` struct ATSFlatDataFontSpecRawNameDataHeader {     var numberOfFlattenedNames: UInt32     var nameDataArray: (ATSFlatDataFontSpecRawNameData)     init()     init(numberOfFlattenedNames numberOfFlattenedNames: UInt32, nameDataArray nameDataArray: (ATSFlatDataFontSpecRawNameData)) } ``` |

Modified ATSFlatDataLayoutControlsDataHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataLayoutControlsDataHeader {     var numberOfLayoutControls: UInt32     var controlArray: (ATSUAttributeInfo) } ``` |
| To | ``` struct ATSFlatDataLayoutControlsDataHeader {     var numberOfLayoutControls: UInt32     var controlArray: (ATSUAttributeInfo)     init()     init(numberOfLayoutControls numberOfLayoutControls: UInt32, controlArray controlArray: (ATSUAttributeInfo)) } ``` |

Modified ATSFlatDataLineInfoData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataLineInfoData {     var lineLength: UInt32     var numberOfLineControls: UInt32 } ``` |
| To | ``` struct ATSFlatDataLineInfoData {     var lineLength: UInt32     var numberOfLineControls: UInt32     init()     init(lineLength lineLength: UInt32, numberOfLineControls numberOfLineControls: UInt32) } ``` |

Modified ATSFlatDataLineInfoHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataLineInfoHeader {     var numberOfLines: UInt32     var lineInfoArray: (ATSFlatDataLineInfoData) } ``` |
| To | ``` struct ATSFlatDataLineInfoHeader {     var numberOfLines: UInt32     var lineInfoArray: (ATSFlatDataLineInfoData)     init()     init(numberOfLines numberOfLines: UInt32, lineInfoArray lineInfoArray: (ATSFlatDataLineInfoData)) } ``` |

Modified ATSFlatDataMainHeaderBlock [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataMainHeaderBlock {     var version: UInt32     var sizeOfDataBlock: UInt32     var offsetToTextLayouts: UInt32     var offsetToStyleRuns: UInt32     var offsetToStyleList: UInt32 } ``` |
| To | ``` struct ATSFlatDataMainHeaderBlock {     var version: UInt32     var sizeOfDataBlock: UInt32     var offsetToTextLayouts: UInt32     var offsetToStyleRuns: UInt32     var offsetToStyleList: UInt32     init()     init(version version: UInt32, sizeOfDataBlock sizeOfDataBlock: UInt32, offsetToTextLayouts offsetToTextLayouts: UInt32, offsetToStyleRuns offsetToStyleRuns: UInt32, offsetToStyleList offsetToStyleList: UInt32) } ``` |

Modified ATSFlatDataStyleListFeatureData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataStyleListFeatureData {     var theFeatureType: ATSUFontFeatureType     var theFeatureSelector: ATSUFontFeatureSelector } ``` |
| To | ``` struct ATSFlatDataStyleListFeatureData {     var theFeatureType: ATSUFontFeatureType     var theFeatureSelector: ATSUFontFeatureSelector     init()     init(theFeatureType theFeatureType: ATSUFontFeatureType, theFeatureSelector theFeatureSelector: ATSUFontFeatureSelector) } ``` |

Modified ATSFlatDataStyleListHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataStyleListHeader {     var numberOfStyles: UInt32     var styleDataArray: (ATSFlatDataStyleListStyleDataHeader) } ``` |
| To | ``` struct ATSFlatDataStyleListHeader {     var numberOfStyles: UInt32     var styleDataArray: (ATSFlatDataStyleListStyleDataHeader)     init()     init(numberOfStyles numberOfStyles: UInt32, styleDataArray styleDataArray: (ATSFlatDataStyleListStyleDataHeader)) } ``` |

Modified ATSFlatDataStyleListStyleDataHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataStyleListStyleDataHeader {     var sizeOfStyleInfo: UInt32     var numberOfSetAttributes: UInt32     var numberOfSetFeatures: UInt32     var numberOfSetVariations: UInt32 } ``` |
| To | ``` struct ATSFlatDataStyleListStyleDataHeader {     var sizeOfStyleInfo: UInt32     var numberOfSetAttributes: UInt32     var numberOfSetFeatures: UInt32     var numberOfSetVariations: UInt32     init()     init(sizeOfStyleInfo sizeOfStyleInfo: UInt32, numberOfSetAttributes numberOfSetAttributes: UInt32, numberOfSetFeatures numberOfSetFeatures: UInt32, numberOfSetVariations numberOfSetVariations: UInt32) } ``` |

Modified ATSFlatDataStyleListVariationData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataStyleListVariationData {     var theVariationAxis: ATSUFontVariationAxis     var theVariationValue: ATSUFontVariationValue } ``` |
| To | ``` struct ATSFlatDataStyleListVariationData {     var theVariationAxis: ATSUFontVariationAxis     var theVariationValue: ATSUFontVariationValue     init()     init(theVariationAxis theVariationAxis: ATSUFontVariationAxis, theVariationValue theVariationValue: ATSUFontVariationValue) } ``` |

Modified ATSFlatDataStyleRunDataHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataStyleRunDataHeader {     var numberOfStyleRuns: UInt32     var styleRunArray: (ATSUStyleRunInfo) } ``` |
| To | ``` struct ATSFlatDataStyleRunDataHeader {     var numberOfStyleRuns: UInt32     var styleRunArray: (ATSUStyleRunInfo)     init()     init(numberOfStyleRuns numberOfStyleRuns: UInt32, styleRunArray styleRunArray: (ATSUStyleRunInfo)) } ``` |

Modified ATSFlatDataTextLayoutDataHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataTextLayoutDataHeader {     var sizeOfLayoutData: UInt32     var textLayoutLength: UInt32     var offsetToLayoutControls: UInt32     var offsetToLineInfo: UInt32 } ``` |
| To | ``` struct ATSFlatDataTextLayoutDataHeader {     var sizeOfLayoutData: UInt32     var textLayoutLength: UInt32     var offsetToLayoutControls: UInt32     var offsetToLineInfo: UInt32     init()     init(sizeOfLayoutData sizeOfLayoutData: UInt32, textLayoutLength textLayoutLength: UInt32, offsetToLayoutControls offsetToLayoutControls: UInt32, offsetToLineInfo offsetToLineInfo: UInt32) } ``` |

Modified ATSFlatDataTextLayoutHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFlatDataTextLayoutHeader {     var numFlattenedTextLayouts: UInt32     var flattenedTextLayouts: (ATSFlatDataTextLayoutDataHeader) } ``` |
| To | ``` struct ATSFlatDataTextLayoutHeader {     var numFlattenedTextLayouts: UInt32     var flattenedTextLayouts: (ATSFlatDataTextLayoutDataHeader)     init()     init(numFlattenedTextLayouts numFlattenedTextLayouts: UInt32, flattenedTextLayouts flattenedTextLayouts: (ATSFlatDataTextLayoutDataHeader)) } ``` |

Modified ATSFontFilter [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFontFilter {     var version: UInt32     var filterSelector: ATSFontFilterSelector } ``` |
| To | ``` struct ATSFontFilter {     var version: UInt32     var filterSelector: ATSFontFilterSelector     init() } ``` |

Modified ATSFontMetrics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFontMetrics {     var version: UInt32     var ascent: CGFloat     var descent: CGFloat     var leading: CGFloat     var avgAdvanceWidth: CGFloat     var maxAdvanceWidth: CGFloat     var minLeftSideBearing: CGFloat     var minRightSideBearing: CGFloat     var stemWidth: CGFloat     var stemHeight: CGFloat     var capHeight: CGFloat     var xHeight: CGFloat     var italicAngle: CGFloat     var underlinePosition: CGFloat     var underlineThickness: CGFloat } ``` |
| To | ``` struct ATSFontMetrics {     var version: UInt32     var ascent: CGFloat     var descent: CGFloat     var leading: CGFloat     var avgAdvanceWidth: CGFloat     var maxAdvanceWidth: CGFloat     var minLeftSideBearing: CGFloat     var minRightSideBearing: CGFloat     var stemWidth: CGFloat     var stemHeight: CGFloat     var capHeight: CGFloat     var xHeight: CGFloat     var italicAngle: CGFloat     var underlinePosition: CGFloat     var underlineThickness: CGFloat     init()     init(version version: UInt32, ascent ascent: CGFloat, descent descent: CGFloat, leading leading: CGFloat, avgAdvanceWidth avgAdvanceWidth: CGFloat, maxAdvanceWidth maxAdvanceWidth: CGFloat, minLeftSideBearing minLeftSideBearing: CGFloat, minRightSideBearing minRightSideBearing: CGFloat, stemWidth stemWidth: CGFloat, stemHeight stemHeight: CGFloat, capHeight capHeight: CGFloat, xHeight xHeight: CGFloat, italicAngle italicAngle: CGFloat, underlinePosition underlinePosition: CGFloat, underlineThickness underlineThickness: CGFloat) } ``` |

Modified ATSFontQuerySourceContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFontQuerySourceContext {     var version: UInt32     var refCon: UnsafePointer<()>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack } ``` |
| To | ``` struct ATSFontQuerySourceContext {     var version: UInt32     var refCon: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     init()     init(version version: UInt32, refCon refCon: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack) } ``` |

Modified ATSFontQuerySourceContext.refCon

|  | Declaration |
| --- | --- |
| From | ``` var refCon: UnsafePointer<()> ``` |
| To | ``` var refCon: UnsafeMutablePointer<Void> ``` |

Modified ATSGlyphIdealMetrics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSGlyphIdealMetrics {     var advance: ATSPoint     var sideBearing: ATSPoint     var otherSideBearing: ATSPoint } ``` |
| To | ``` struct ATSGlyphIdealMetrics {     var advance: ATSPoint     var sideBearing: ATSPoint     var otherSideBearing: ATSPoint     init()     init(advance advance: ATSPoint, sideBearing sideBearing: ATSPoint, otherSideBearing otherSideBearing: ATSPoint) } ``` |

Modified ATSGlyphScreenMetrics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSGlyphScreenMetrics {     var deviceAdvance: ATSPoint     var topLeft: ATSPoint     var height: UInt32     var width: UInt32     var sideBearing: ATSPoint     var otherSideBearing: ATSPoint } ``` |
| To | ``` struct ATSGlyphScreenMetrics {     var deviceAdvance: ATSPoint     var topLeft: ATSPoint     var height: UInt32     var width: UInt32     var sideBearing: ATSPoint     var otherSideBearing: ATSPoint     init()     init(deviceAdvance deviceAdvance: ATSPoint, topLeft topLeft: ATSPoint, height height: UInt32, width width: UInt32, sideBearing sideBearing: ATSPoint, otherSideBearing otherSideBearing: ATSPoint) } ``` |

Modified ATSJustWidthDeltaEntryOverride [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSJustWidthDeltaEntryOverride {     var beforeGrowLimit: Fixed     var beforeShrinkLimit: Fixed     var afterGrowLimit: Fixed     var afterShrinkLimit: Fixed     var growFlags: JustificationFlags     var shrinkFlags: JustificationFlags } ``` |
| To | ``` struct ATSJustWidthDeltaEntryOverride {     var beforeGrowLimit: Fixed     var beforeShrinkLimit: Fixed     var afterGrowLimit: Fixed     var afterShrinkLimit: Fixed     var growFlags: JustificationFlags     var shrinkFlags: JustificationFlags     init()     init(beforeGrowLimit beforeGrowLimit: Fixed, beforeShrinkLimit beforeShrinkLimit: Fixed, afterGrowLimit afterGrowLimit: Fixed, afterShrinkLimit afterShrinkLimit: Fixed, growFlags growFlags: JustificationFlags, shrinkFlags shrinkFlags: JustificationFlags) } ``` |

Modified ATSLayoutRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSLayoutRecord {     var glyphID: ATSGlyphRef     var flags: ATSGlyphInfoFlags     var originalOffset: ByteCount     var realPos: Fixed } ``` |
| To | ``` struct ATSLayoutRecord {     var glyphID: ATSGlyphRef     var flags: ATSGlyphInfoFlags     var originalOffset: Int     var realPos: Fixed     init()     init(glyphID glyphID: ATSGlyphRef, flags flags: ATSGlyphInfoFlags, originalOffset originalOffset: Int, realPos realPos: Fixed) } ``` |

Modified ATSLayoutRecord.originalOffset

|  | Declaration |
| --- | --- |
| From | ``` var originalOffset: ByteCount ``` |
| To | ``` var originalOffset: Int ``` |

Modified ATSTrapezoid [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSTrapezoid {     var upperLeft: FixedPoint     var upperRight: FixedPoint     var lowerRight: FixedPoint     var lowerLeft: FixedPoint } ``` |
| To | ``` struct ATSTrapezoid {     var upperLeft: FixedPoint     var upperRight: FixedPoint     var lowerRight: FixedPoint     var lowerLeft: FixedPoint     init()     init(upperLeft upperLeft: FixedPoint, upperRight upperRight: FixedPoint, lowerRight lowerRight: FixedPoint, lowerLeft lowerLeft: FixedPoint) } ``` |

Modified ATSUAttributeInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUAttributeInfo {     var fTag: ATSUAttributeTag     var fValueSize: ByteCount } ``` |
| To | ``` struct ATSUAttributeInfo {     var fTag: ATSUAttributeTag     var fValueSize: Int     init()     init(fTag fTag: ATSUAttributeTag, fValueSize fValueSize: Int) } ``` |

Modified ATSUAttributeInfo.fValueSize

|  | Declaration |
| --- | --- |
| From | ``` var fValueSize: ByteCount ``` |
| To | ``` var fValueSize: Int ``` |

Modified ATSUCaret [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUCaret {     var fX: Fixed     var fY: Fixed     var fDeltaX: Fixed     var fDeltaY: Fixed } ``` |
| To | ``` struct ATSUCaret {     var fX: Fixed     var fY: Fixed     var fDeltaX: Fixed     var fDeltaY: Fixed     init()     init(fX fX: Fixed, fY fY: Fixed, fDeltaX fDeltaX: Fixed, fDeltaY fDeltaY: Fixed) } ``` |

Modified ATSUCurvePath [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUCurvePath {     var vectors: UInt32     var controlBits: (UInt32)     var vector: (ATSPoint) } ``` |
| To | ``` struct ATSUCurvePath {     var vectors: UInt32     var controlBits: (UInt32)     var vector: (ATSPoint)     init()     init(vectors vectors: UInt32, controlBits controlBits: (UInt32), vector vector: (ATSPoint)) } ``` |

Modified ATSUCurvePaths [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUCurvePaths {     var contours: UInt32     var contour: (ATSUCurvePath) } ``` |
| To | ``` struct ATSUCurvePaths {     var contours: UInt32     var contour: (ATSUCurvePath)     init()     init(contours contours: UInt32, contour contour: (ATSUCurvePath)) } ``` |

Modified ATSUGlyphInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUGlyphInfo {     var glyphID: GlyphID     var reserved: UInt16     var layoutFlags: UInt32     var charIndex: UniCharArrayOffset     var style: ATSUStyle     var deltaY: Float32     var idealX: Float32     var screenX: Int16     var caretX: Int16 } ``` |
| To | ``` struct ATSUGlyphInfo {     var glyphID: GlyphID     var reserved: UInt16     var layoutFlags: UInt32     var charIndex: UniCharArrayOffset     var style: ATSUStyle     var deltaY: Float32     var idealX: Float32     var screenX: Int16     var caretX: Int16     init()     init(glyphID glyphID: GlyphID, reserved reserved: UInt16, layoutFlags layoutFlags: UInt32, charIndex charIndex: UniCharArrayOffset, style style: ATSUStyle, deltaY deltaY: Float32, idealX idealX: Float32, screenX screenX: Int16, caretX caretX: Int16) } ``` |

Modified ATSUGlyphInfoArray [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUGlyphInfoArray {     var layout: ATSUTextLayout     var numGlyphs: ItemCount     var glyphs: (ATSUGlyphInfo) } ``` |
| To | ``` struct ATSUGlyphInfoArray {     var layout: ATSUTextLayout     var numGlyphs: Int     var glyphs: (ATSUGlyphInfo)     init()     init(layout layout: ATSUTextLayout, numGlyphs numGlyphs: Int, glyphs glyphs: (ATSUGlyphInfo)) } ``` |

Modified ATSUGlyphInfoArray.numGlyphs

|  | Declaration |
| --- | --- |
| From | ``` var numGlyphs: ItemCount ``` |
| To | ``` var numGlyphs: Int ``` |

Modified ATSUGlyphSelector [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUGlyphSelector {     var collection: GlyphCollection     var glyphID: GlyphID } ``` |
| To | ``` struct ATSUGlyphSelector {     var collection: GlyphCollection     var glyphID: GlyphID     init()     init(collection collection: GlyphCollection, glyphID glyphID: GlyphID) } ``` |

Modified ATSULayoutOperationOverrideSpecifier [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSULayoutOperationOverrideSpecifier {     var operationSelector: ATSULayoutOperationSelector     var overrideUPP: ATSUDirectLayoutOperationOverrideUPP } ``` |
| To | ``` struct ATSULayoutOperationOverrideSpecifier {     var operationSelector: ATSULayoutOperationSelector     var overrideUPP: ATSUDirectLayoutOperationOverrideUPP     init()     init(operationSelector operationSelector: ATSULayoutOperationSelector, overrideUPP overrideUPP: ATSUDirectLayoutOperationOverrideUPP) } ``` |

Modified ATSURGBAlphaColor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSURGBAlphaColor {     var red: Float     var green: Float     var blue: Float     var alpha: Float } ``` |
| To | ``` struct ATSURGBAlphaColor {     var red: Float     var green: Float     var blue: Float     var alpha: Float     init()     init(red red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } ``` |

Modified ATSUStyleRunInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUStyleRunInfo {     var runLength: UInt32     var styleObjectIndex: UInt32 } ``` |
| To | ``` struct ATSUStyleRunInfo {     var runLength: UInt32     var styleObjectIndex: UInt32     init()     init(runLength runLength: UInt32, styleObjectIndex styleObjectIndex: UInt32) } ``` |

Modified ATSUTab [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUTab {     var tabPosition: ATSUTextMeasurement     var tabType: ATSUTabType } ``` |
| To | ``` struct ATSUTab {     var tabPosition: ATSUTextMeasurement     var tabType: ATSUTabType     init()     init(tabPosition tabPosition: ATSUTextMeasurement, tabType tabType: ATSUTabType) } ``` |

Modified ATSUUnhighlightData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ATSUUnhighlightData {     var dataType: ATSUBackgroundDataType } ``` |
| To | ``` struct ATSUUnhighlightData {     var dataType: ATSUBackgroundDataType     var unhighlightData: ATSUBackgroundData     init()     init(dataType dataType: ATSUBackgroundDataType, unhighlightData unhighlightData: ATSUBackgroundData) } ``` |

Modified AXPriority [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AppParameters [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AppParameters {     var eventRefCon: UInt32     var messageLength: UInt32 } ``` |
| To | ``` struct AppParameters {     var eventRefCon: UInt32     var messageLength: UInt32     init() } ``` |

Modified AsscEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AsscEntry {     var fontSize: Int16     var fontStyle: Int16     var fontID: Int16 } ``` |
| To | ``` struct AsscEntry {     var fontSize: Int16     var fontStyle: Int16     var fontID: Int16     init()     init(fontSize fontSize: Int16, fontStyle fontStyle: Int16, fontID fontID: Int16) } ``` |

Modified BitMap [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BitMap {     var baseAddr: Ptr     var rowBytes: Int16     var bounds: Rect } ``` |
| To | ``` struct BitMap {     var baseAddr: Ptr     var rowBytes: Int16     var bounds: Rect     init()     init(baseAddr baseAddr: Ptr, rowBytes rowBytes: Int16, bounds bounds: Rect) } ``` |

Modified CM2Profile [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CM2Profile {     var header: CM2Header     var tagTable: CMTagElemTable     var elemData: (Int8) } ``` |
| To | ``` struct CM2Profile {     var header: CM2Header     var tagTable: CMTagElemTable     var elemData: (Int8)     init()     init(header header: CM2Header, tagTable tagTable: CMTagElemTable, elemData elemData: (Int8)) } ``` |

Modified CMDeviceInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMDeviceInfo {     var dataVersion: UInt32     var deviceClass: CMDeviceClass     var deviceID: CMDeviceID     var deviceScope: CMDeviceScope     var deviceState: CMDeviceState     var defaultProfileID: CMDeviceProfileID     var deviceName: UnsafePointer<Unmanaged<CFDictionary>?>     var profileCount: UInt32     var reserved: UInt32 } ``` |
| To | ``` struct CMDeviceInfo {     var dataVersion: UInt32     var deviceClass: CMDeviceClass     var deviceID: CMDeviceID     var deviceScope: CMDeviceScope     var deviceState: CMDeviceState     var defaultProfileID: CMDeviceProfileID     var deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>     var profileCount: UInt32     var reserved: UInt32     init()     init(dataVersion dataVersion: UInt32, deviceClass deviceClass: CMDeviceClass, deviceID deviceID: CMDeviceID, deviceScope deviceScope: CMDeviceScope, deviceState deviceState: CMDeviceState, defaultProfileID defaultProfileID: CMDeviceProfileID, deviceName deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, profileCount profileCount: UInt32, reserved reserved: UInt32) } ``` |

Modified CMDeviceInfo.deviceName

|  | Declaration |
| --- | --- |
| From | ``` var deviceName: UnsafePointer<Unmanaged<CFDictionary>?> ``` |
| To | ``` var deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?> ``` |

Modified CMDeviceProfileArray [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMDeviceProfileArray {     var profileCount: UInt32     var profiles: (CMDeviceProfileInfo) } ``` |
| To | ``` struct CMDeviceProfileArray {     var profileCount: UInt32     var profiles: (CMDeviceProfileInfo)     init()     init(profileCount profileCount: UInt32, profiles profiles: (CMDeviceProfileInfo)) } ``` |

Modified CMDeviceScope [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMDeviceScope {     var deviceUser: Unmanaged<CFString>!     var deviceHost: Unmanaged<CFString>! } ``` |
| To | ``` struct CMDeviceScope {     var deviceUser: Unmanaged<CFString>!     var deviceHost: Unmanaged<CFString>!     init()     init(deviceUser deviceUser: Unmanaged<CFString>!, deviceHost deviceHost: Unmanaged<CFString>!) } ``` |

Modified CMMultiFunctLutType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMMultiFunctLutType {     var typeDescriptor: OSType     var reserved: UInt32     var inputChannels: UInt8     var outputChannels: UInt8     var reserved2: UInt16     var offsetBcurves: UInt32     var offsetMatrix: UInt32     var offsetMcurves: UInt32     var offsetCLUT: UInt32     var offsetAcurves: UInt32     var data: (UInt8) } ``` |
| To | ``` struct CMMultiFunctLutType {     var typeDescriptor: OSType     var reserved: UInt32     var inputChannels: UInt8     var outputChannels: UInt8     var reserved2: UInt16     var offsetBcurves: UInt32     var offsetMatrix: UInt32     var offsetMcurves: UInt32     var offsetCLUT: UInt32     var offsetAcurves: UInt32     var data: (UInt8)     init()     init(typeDescriptor typeDescriptor: OSType, reserved reserved: UInt32, inputChannels inputChannels: UInt8, outputChannels outputChannels: UInt8, reserved2 reserved2: UInt16, offsetBcurves offsetBcurves: UInt32, offsetMatrix offsetMatrix: UInt32, offsetMcurves offsetMcurves: UInt32, offsetCLUT offsetCLUT: UInt32, offsetAcurves offsetAcurves: UInt32, data data: (UInt8)) } ``` |

Modified CMXYZColor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMXYZColor {     var X: CMXYZComponent     var Y: CMXYZComponent     var Z: CMXYZComponent } ``` |
| To | ``` struct CMXYZColor {     var X: CMXYZComponent     var Y: CMXYZComponent     var Z: CMXYZComponent     init()     init(X X: CMXYZComponent, Y Y: CMXYZComponent, Z Z: CMXYZComponent) } ``` |

Modified CQDProcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CQDProcs {     var textProc: QDTextUPP     var lineProc: QDLineUPP     var rectProc: QDRectUPP     var rRectProc: QDRRectUPP     var ovalProc: QDOvalUPP     var arcProc: QDArcUPP     var polyProc: QDPolyUPP     var rgnProc: QDRgnUPP     var bitsProc: QDBitsUPP     var commentProc: QDCommentUPP     var txMeasProc: QDTxMeasUPP     var getPicProc: QDGetPicUPP     var putPicProc: QDPutPicUPP     var opcodeProc: QDOpcodeUPP     var newProc1: UniversalProcPtr     var glyphsProc: QDStdGlyphsUPP     var printerStatusProc: QDPrinterStatusUPP     var newProc4: UniversalProcPtr     var newProc5: UniversalProcPtr     var newProc6: UniversalProcPtr } ``` |
| To | ``` struct CQDProcs {     var textProc: QDTextUPP     var lineProc: QDLineUPP     var rectProc: QDRectUPP     var rRectProc: QDRRectUPP     var ovalProc: QDOvalUPP     var arcProc: QDArcUPP     var polyProc: QDPolyUPP     var rgnProc: QDRgnUPP     var bitsProc: QDBitsUPP     var commentProc: QDCommentUPP     var txMeasProc: QDTxMeasUPP     var getPicProc: QDGetPicUPP     var putPicProc: QDPutPicUPP     var opcodeProc: QDOpcodeUPP     var newProc1: UniversalProcPtr     var glyphsProc: QDStdGlyphsUPP     var printerStatusProc: QDPrinterStatusUPP     var newProc4: UniversalProcPtr     var newProc5: UniversalProcPtr     var newProc6: UniversalProcPtr     init()     init(textProc textProc: QDTextUPP, lineProc lineProc: QDLineUPP, rectProc rectProc: QDRectUPP, rRectProc rRectProc: QDRRectUPP, ovalProc ovalProc: QDOvalUPP, arcProc arcProc: QDArcUPP, polyProc polyProc: QDPolyUPP, rgnProc rgnProc: QDRgnUPP, bitsProc bitsProc: QDBitsUPP, commentProc commentProc: QDCommentUPP, txMeasProc txMeasProc: QDTxMeasUPP, getPicProc getPicProc: QDGetPicUPP, putPicProc putPicProc: QDPutPicUPP, opcodeProc opcodeProc: QDOpcodeUPP, newProc1 newProc1: UniversalProcPtr, glyphsProc glyphsProc: QDStdGlyphsUPP, printerStatusProc printerStatusProc: QDPrinterStatusUPP, newProc4 newProc4: UniversalProcPtr, newProc5 newProc5: UniversalProcPtr, newProc6 newProc6: UniversalProcPtr) } ``` |

Modified ColorSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ColorSpec {     var value: Int16     var rgb: RGBColor } ``` |
| To | ``` struct ColorSpec {     var value: Int16     var rgb: RGBColor     init()     init(value value: Int16, rgb rgb: RGBColor) } ``` |

Modified ColorSyncMD5 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ColorSyncMD5 {     var digest: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct ColorSyncMD5 {     var digest: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(digest digest: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified ColorTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ColorTable {     var ctSeed: Int32     var ctFlags: Int16     var ctSize: Int16     var ctTable: CSpecArray } ``` |
| To | ``` struct ColorTable {     var ctSeed: Int32     var ctFlags: Int16     var ctSize: Int16     var ctTable: CSpecArray     init()     init(ctSeed ctSeed: Int32, ctFlags ctFlags: Int16, ctSize ctSize: Int16, ctTable ctTable: CSpecArray) } ``` |

Modified DCMDictionaryHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DCMDictionaryHeader {     var headerSignature: FourCharCode     var headerVersion: UInt32     var headerSize: UInt32     var accessMethod: Str63 } ``` |
| To | ``` struct DCMDictionaryHeader {     var headerSignature: FourCharCode     var headerVersion: UInt32     var headerSize: UInt32     var accessMethod: Str63     init()     init(headerSignature headerSignature: FourCharCode, headerVersion headerVersion: UInt32, headerSize headerSize: UInt32, accessMethod accessMethod: Str63) } ``` |

Modified DelimiterInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DelimiterInfo {     var startDelimiter: (Byte, Byte)     var endDelimiter: (Byte, Byte) } ``` |
| To | ``` struct DelimiterInfo {     var startDelimiter: (UInt8, UInt8)     var endDelimiter: (UInt8, UInt8)     init()     init(startDelimiter startDelimiter: (UInt8, UInt8), endDelimiter endDelimiter: (UInt8, UInt8)) } ``` |

Modified DelimiterInfo.endDelimiter

|  | Declaration |
| --- | --- |
| From | ``` var endDelimiter: (Byte, Byte) ``` |
| To | ``` var endDelimiter: (UInt8, UInt8) ``` |

Modified DelimiterInfo.startDelimiter

|  | Declaration |
| --- | --- |
| From | ``` var startDelimiter: (Byte, Byte) ``` |
| To | ``` var startDelimiter: (UInt8, UInt8) ``` |

Modified FMFilter [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FMFilter {     var format: UInt32     var selector: FMFilterSelector } ``` |
| To | ``` struct FMFilter {     var format: UInt32     var selector: FMFilterSelector     init() } ``` |

Modified FMFontDirectoryFilter [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FMFontDirectoryFilter {     var fontFolderDomain: Int16     var reserved: (UInt32, UInt32) } ``` |
| To | ``` struct FMFontDirectoryFilter {     var fontFolderDomain: Int16     var reserved: (UInt32, UInt32)     init()     init(fontFolderDomain fontFolderDomain: Int16, reserved reserved: (UInt32, UInt32)) } ``` |

Modified FMFontFamilyInstance [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FMFontFamilyInstance {     var fontFamily: FMFontFamily     var fontStyle: FMFontStyle } ``` |
| To | ``` struct FMFontFamilyInstance {     var fontFamily: FMFontFamily     var fontStyle: FMFontStyle     init()     init(fontFamily fontFamily: FMFontFamily, fontStyle fontStyle: FMFontStyle) } ``` |

Modified FMFontFamilyInstanceIterator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FMFontFamilyInstanceIterator {     var reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct FMFontFamilyInstanceIterator {     var reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(reserved reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified FMFontFamilyIterator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FMFontFamilyIterator {     var reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct FMFontFamilyIterator {     var reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(reserved reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified FMFontIterator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FMFontIterator {     var reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct FMFontIterator {     var reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(reserved reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified FMInput [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FMInput {     var family: Int16     var size: Int16     var face: Style     var needBits: Boolean     var device: Int16     var numer: Point     var denom: Point } ``` |
| To | ``` struct FMInput {     var family: Int16     var size: Int16     var face: Style     var needBits: Boolean     var device: Int16     var numer: Point     var denom: Point     init()     init(family family: Int16, size size: Int16, face face: Style, needBits needBits: Boolean, device device: Int16, numer numer: Point, denom denom: Point) } ``` |

Modified FamRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FamRec {     var ffFlags: Int16     var ffFamID: Int16     var ffFirstChar: Int16     var ffLastChar: Int16     var ffAscent: Int16     var ffDescent: Int16     var ffLeading: Int16     var ffWidMax: Int16     var ffWTabOff: Int32     var ffKernOff: Int32     var ffStylOff: Int32     var ffProperty: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     var ffIntl: (Int16, Int16)     var ffVersion: Int16 } ``` |
| To | ``` struct FamRec {     var ffFlags: Int16     var ffFamID: Int16     var ffFirstChar: Int16     var ffLastChar: Int16     var ffAscent: Int16     var ffDescent: Int16     var ffLeading: Int16     var ffWidMax: Int16     var ffWTabOff: Int32     var ffKernOff: Int32     var ffStylOff: Int32     var ffProperty: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     var ffIntl: (Int16, Int16)     var ffVersion: Int16     init()     init(ffFlags ffFlags: Int16, ffFamID ffFamID: Int16, ffFirstChar ffFirstChar: Int16, ffLastChar ffLastChar: Int16, ffAscent ffAscent: Int16, ffDescent ffDescent: Int16, ffLeading ffLeading: Int16, ffWidMax ffWidMax: Int16, ffWTabOff ffWTabOff: Int32, ffKernOff ffKernOff: Int32, ffStylOff ffStylOff: Int32, ffProperty ffProperty: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16), ffIntl ffIntl: (Int16, Int16), ffVersion ffVersion: Int16) } ``` |

Modified FontAssoc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FontAssoc {     var numAssoc: Int16 } ``` |
| To | ``` struct FontAssoc {     var numAssoc: Int16     init()     init(numAssoc numAssoc: Int16) } ``` |

Modified FontInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FontInfo {     var ascent: Int16     var descent: Int16     var widMax: Int16     var leading: Int16 } ``` |
| To | ``` struct FontInfo {     var ascent: Int16     var descent: Int16     var widMax: Int16     var leading: Int16     init()     init(ascent ascent: Int16, descent descent: Int16, widMax widMax: Int16, leading leading: Int16) } ``` |

Modified FontRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FontRec {     var fontType: Int16     var firstChar: Int16     var lastChar: Int16     var widMax: Int16     var kernMax: Int16     var nDescent: Int16     var fRectWidth: Int16     var fRectHeight: Int16     var owTLoc: UInt16     var ascent: Int16     var descent: Int16     var leading: Int16     var rowWords: Int16 } ``` |
| To | ``` struct FontRec {     var fontType: Int16     var firstChar: Int16     var lastChar: Int16     var widMax: Int16     var kernMax: Int16     var nDescent: Int16     var fRectWidth: Int16     var fRectHeight: Int16     var owTLoc: UInt16     var ascent: Int16     var descent: Int16     var leading: Int16     var rowWords: Int16     init()     init(fontType fontType: Int16, firstChar firstChar: Int16, lastChar lastChar: Int16, widMax widMax: Int16, kernMax kernMax: Int16, nDescent nDescent: Int16, fRectWidth fRectWidth: Int16, fRectHeight fRectHeight: Int16, owTLoc owTLoc: UInt16, ascent ascent: Int16, descent descent: Int16, leading leading: Int16, rowWords rowWords: Int16) } ``` |

Modified GDevice [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GDevice {     var gdRefNum: Int16     var gdID: Int16     var gdType: Int16     var gdITable: Handle     var gdResPref: Int16     var gdSearchProc: Handle     var gdCompProc: Handle     var gdFlags: Int16     var gdPMap: PixMapHandle     var gdRefCon: Int32     var gdNextGD: GDHandle     var gdRect: Rect     var gdMode: Int32     var gdCCBytes: Int16     var gdCCDepth: Int16     var gdCCXData: Handle     var gdCCXMask: Handle     var gdExt: Handle } ``` |
| To | ``` struct GDevice {     var gdRefNum: Int16     var gdID: Int16     var gdType: Int16     var gdITable: Handle     var gdResPref: Int16     var gdSearchProc: Handle     var gdCompProc: Handle     var gdFlags: Int16     var gdPMap: PixMapHandle     var gdRefCon: Int32     var gdNextGD: GDHandle     var gdRect: Rect     var gdMode: Int32     var gdCCBytes: Int16     var gdCCDepth: Int16     var gdCCXData: Handle     var gdCCXMask: Handle     var gdExt: Handle     init()     init(gdRefNum gdRefNum: Int16, gdID gdID: Int16, gdType gdType: Int16, gdITable gdITable: Handle, gdResPref gdResPref: Int16, gdSearchProc gdSearchProc: Handle, gdCompProc gdCompProc: Handle, gdFlags gdFlags: Int16, gdPMap gdPMap: PixMapHandle, gdRefCon gdRefCon: Int32, gdNextGD gdNextGD: GDHandle, gdRect gdRect: Rect, gdMode gdMode: Int32, gdCCBytes gdCCBytes: Int16, gdCCDepth gdCCDepth: Int16, gdCCXData gdCCXData: Handle, gdCCXMask gdCCXMask: Handle, gdExt gdExt: Handle) } ``` |

Modified GrafPort [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GrafPort {     var whatever: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16) } ``` |
| To | ``` struct GrafPort {     var whatever: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     init()     init(whatever whatever: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)) } ``` |

Modified HomographDicInfoRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HomographDicInfoRec {     var dictionaryID: DCMDictionaryID     var uniqueID: DCMUniqueID } ``` |
| To | ``` struct HomographDicInfoRec {     var dictionaryID: DCMDictionaryID     var uniqueID: DCMUniqueID     init()     init(dictionaryID dictionaryID: DCMDictionaryID, uniqueID uniqueID: DCMUniqueID) } ``` |

Modified ICAppSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAppSpec {     var fCreator: OSType     var name: Str63 } ``` |
| To | ``` struct ICAppSpec {     var fCreator: OSType     var name: Str63     init()     init(fCreator fCreator: OSType, name name: Str63) } ``` |

Modified ICAppSpecList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICAppSpecList {     var numberOfItems: Int16     var appSpecs: (ICAppSpec) } ``` |
| To | ``` struct ICAppSpecList {     var numberOfItems: Int16     var appSpecs: (ICAppSpec)     init()     init(numberOfItems numberOfItems: Int16, appSpecs appSpecs: (ICAppSpec)) } ``` |

Modified ICCharTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICCharTable {     var netToMac: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var macToNet: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ```  ``` |

Modified ICFileSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICFileSpec {     var volName: Str31     var volCreationDate: Int32     var fss: FSSpec     var alias: AliasRecord } ``` |
| To | ``` struct ICFileSpec {     var volName: Str31     var volCreationDate: Int32     var fss: FSSpec     var alias: AliasRecord     init()     init(volName volName: Str31, volCreationDate volCreationDate: Int32, fss fss: FSSpec, alias alias: AliasRecord) } ``` |

Modified ICFontRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICFontRecord {     var size: Int16     var face: Style     var pad: Int8     var font: Str255 } ``` |
| To | ``` struct ICFontRecord {     var size: Int16     var face: Style     var pad: Int8     var font: Str255     init()     init(size size: Int16, face face: Style, pad pad: Int8, font font: Str255) } ``` |

Modified ICMapEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICMapEntry {     var totalLength: Int16     var fixedLength: ICFixedLength     var version: Int16     var fileType: OSType     var fileCreator: OSType     var postCreator: OSType     var flags: ICMapEntryFlags     var `extension`: Str255     var creatorAppName: Str255     var postAppName: Str255     var MIMEType: Str255     var entryName: Str255 } ``` |
| To | ``` struct ICMapEntry {     var totalLength: Int16     var fixedLength: ICFixedLength     var version: Int16     var fileType: OSType     var fileCreator: OSType     var postCreator: OSType     var flags: ICMapEntryFlags     var `extension`: Str255     var creatorAppName: Str255     var postAppName: Str255     var MIMEType: Str255     var entryName: Str255     init()     init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, `extension` `extension`: Str255, creatorAppName creatorAppName: Str255, postAppName postAppName: Str255, MIMEType MIMEType: Str255, entryName entryName: Str255) } ``` |

Modified ICServiceEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICServiceEntry {     var name: Str255     var port: Int16     var flags: ICServiceEntryFlags } ``` |
| To | ``` struct ICServiceEntry {     var name: Str255     var port: Int16     var flags: ICServiceEntryFlags     init()     init(name name: Str255, port port: Int16, flags flags: ICServiceEntryFlags) } ``` |

Modified ICServices [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ICServices {     var count: Int16     var services: (ICServiceEntry) } ``` |
| To | ``` struct ICServices {     var count: Int16     var services: (ICServiceEntry)     init()     init(count count: Int16, services services: (ICServiceEntry)) } ``` |

Modified KernEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernEntry {     var kernStyle: Int16     var kernLength: Int16 } ``` |
| To | ``` struct KernEntry {     var kernStyle: Int16     var kernLength: Int16     init()     init(kernStyle kernStyle: Int16, kernLength kernLength: Int16) } ``` |

Modified KernPair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernPair {     var kernFirst: Int8     var kernSecond: Int8     var kernWidth: Int16 } ``` |
| To | ``` struct KernPair {     var kernFirst: Int8     var kernSecond: Int8     var kernWidth: Int16     init()     init(kernFirst kernFirst: Int8, kernSecond kernSecond: Int8, kernWidth kernWidth: Int16) } ``` |

Modified KernTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernTable {     var numKerns: Int16 } ``` |
| To | ``` struct KernTable {     var numKerns: Int16     init()     init(numKerns numKerns: Int16) } ``` |

Modified LAMorphemeRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LAMorphemeRec {     var sourceTextLength: UInt32     var sourceTextPtr: LogicalAddress     var morphemeTextLength: UInt32     var morphemeTextPtr: LogicalAddress     var partOfSpeech: UInt32 } ``` |
| To | ``` struct LAMorphemeRec {     var sourceTextLength: UInt32     var sourceTextPtr: LogicalAddress     var morphemeTextLength: UInt32     var morphemeTextPtr: LogicalAddress     var partOfSpeech: UInt32     init()     init(sourceTextLength sourceTextLength: UInt32, sourceTextPtr sourceTextPtr: LogicalAddress, morphemeTextLength morphemeTextLength: UInt32, morphemeTextPtr morphemeTextPtr: LogicalAddress, partOfSpeech partOfSpeech: UInt32) } ``` |

Modified LAMorphemesArray [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LAMorphemesArray {     var morphemesCount: ItemCount     var processedTextLength: UInt32     var morphemesTextLength: UInt32     var morphemes: (LAMorphemeRec) } ``` |
| To | ``` struct LAMorphemesArray {     var morphemesCount: Int     var processedTextLength: UInt32     var morphemesTextLength: UInt32     var morphemes: (LAMorphemeRec)     init()     init(morphemesCount morphemesCount: Int, processedTextLength processedTextLength: UInt32, morphemesTextLength morphemesTextLength: UInt32, morphemes morphemes: (LAMorphemeRec)) } ``` |

Modified LAMorphemesArray.morphemesCount

|  | Declaration |
| --- | --- |
| From | ``` var morphemesCount: ItemCount ``` |
| To | ``` var morphemesCount: Int ``` |

Modified LaunchParamBlockRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LaunchParamBlockRec {     var reserved1: UInt32     var reserved2: UInt16     var launchBlockID: UInt16     var launchEPBLength: UInt32     var launchFileFlags: UInt16     var launchControlFlags: LaunchFlags     var launchAppRef: FSRefPtr     var launchProcessSN: ProcessSerialNumber     var launchPreferredSize: UInt32     var launchMinimumSize: UInt32     var launchAvailableSize: UInt32     var launchAppParameters: AppParametersPtr } ``` |
| To | ``` struct LaunchParamBlockRec {     var reserved1: UInt32     var reserved2: UInt16     var launchBlockID: UInt16     var launchEPBLength: UInt32     var launchFileFlags: UInt16     var launchControlFlags: LaunchFlags     var launchAppRef: FSRefPtr     var launchProcessSN: ProcessSerialNumber     var launchPreferredSize: UInt32     var launchMinimumSize: UInt32     var launchAvailableSize: UInt32     var launchAppParameters: AppParametersPtr     init()     init(reserved1 reserved1: UInt32, reserved2 reserved2: UInt16, launchBlockID launchBlockID: UInt16, launchEPBLength launchEPBLength: UInt32, launchFileFlags launchFileFlags: UInt16, launchControlFlags launchControlFlags: LaunchFlags, launchAppRef launchAppRef: FSRefPtr, launchProcessSN launchProcessSN: ProcessSerialNumber, launchPreferredSize launchPreferredSize: UInt32, launchMinimumSize launchMinimumSize: UInt32, launchAvailableSize launchAvailableSize: UInt32, launchAppParameters launchAppParameters: AppParametersPtr) } ``` |

Modified MacPolygon [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MacPolygon {     var polySize: Int16     var polyBBox: Rect     var polyPoints: (Point) } ``` |
| To | ``` struct MacPolygon {     var polySize: Int16     var polyBBox: Rect     var polyPoints: (Point)     init()     init(polySize polySize: Int16, polyBBox polyBBox: Rect, polyPoints polyPoints: (Point)) } ``` |

Modified MorphemeTextRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorphemeTextRange {     var sourceOffset: UInt32     var length: UInt32 } ``` |
| To | ``` struct MorphemeTextRange {     var sourceOffset: UInt32     var length: UInt32     init()     init(sourceOffset sourceOffset: UInt32, length length: UInt32) } ``` |

Modified NameTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NameTable {     var stringCount: Int16     var baseFontName: Str255 } ``` |
| To | ``` struct NameTable {     var stringCount: Int16     var baseFontName: Str255     init()     init(stringCount stringCount: Int16, baseFontName baseFontName: Str255) } ``` |

Modified OpenCPicParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OpenCPicParams {     var srcRect: Rect     var hRes: Fixed     var vRes: Fixed     var version: Int16     var reserved1: Int16     var reserved2: Int32 } ``` |
| To | ``` struct OpenCPicParams {     var srcRect: Rect     var hRes: Fixed     var vRes: Fixed     var version: Int16     var reserved1: Int16     var reserved2: Int32     init()     init(srcRect srcRect: Rect, hRes hRes: Fixed, vRes vRes: Fixed, version version: Int16, reserved1 reserved1: Int16, reserved2 reserved2: Int32) } ``` |

Modified PMLanguageInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PMLanguageInfo {     var level: Str32     var version: Str32     var release: Str32 } ``` |
| To | ``` struct PMLanguageInfo {     var level: Str32     var version: Str32     var release: Str32     init()     init(level level: Str32, version version: Str32, release release: Str32) } ``` |

Modified PMRect [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PMRect {     var top: Double     var left: Double     var bottom: Double     var right: Double } ``` |
| To | ``` struct PMRect {     var top: Double     var left: Double     var bottom: Double     var right: Double     init()     init(top top: Double, left left: Double, bottom bottom: Double, right right: Double) } ``` |

Modified PMResolution [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PMResolution {     var hRes: Double     var vRes: Double } ``` |
| To | ``` struct PMResolution {     var hRes: Double     var vRes: Double     init()     init(hRes hRes: Double, vRes vRes: Double) } ``` |

Modified Pattern [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Pattern {     var pat: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct Pattern {     var pat: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(pat pat: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified PhonemeDescriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PhonemeDescriptor {     var phonemeCount: Int16     var thePhonemes: (PhonemeInfo) } ``` |
| To | ``` struct PhonemeDescriptor {     var phonemeCount: Int16     var thePhonemes: (PhonemeInfo)     init()     init(phonemeCount phonemeCount: Int16, thePhonemes thePhonemes: (PhonemeInfo)) } ``` |

Modified PhonemeInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PhonemeInfo {     var opcode: Int16     var phStr: Str15     var exampleStr: Str31     var hiliteStart: Int16     var hiliteEnd: Int16 } ``` |
| To | ``` struct PhonemeInfo {     var opcode: Int16     var phStr: Str15     var exampleStr: Str31     var hiliteStart: Int16     var hiliteEnd: Int16     init()     init(opcode opcode: Int16, phStr phStr: Str15, exampleStr exampleStr: Str31, hiliteStart hiliteStart: Int16, hiliteEnd hiliteEnd: Int16) } ``` |

Modified Picture [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Picture {     var picSize: Int16     var picFrame: Rect } ``` |
| To | ``` struct Picture {     var picSize: Int16     var picFrame: Rect     init()     init(picSize picSize: Int16, picFrame picFrame: Rect) } ``` |

Modified PixMap [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PixMap {     var baseAddr: Ptr     var rowBytes: Int16     var bounds: Rect     var pmVersion: Int16     var packType: Int16     var packSize: Int32     var hRes: Fixed     var vRes: Fixed     var pixelType: Int16     var pixelSize: Int16     var cmpCount: Int16     var cmpSize: Int16     var pixelFormat: OSType     var pmTable: CTabHandle     var pmExt: UnsafePointer<()> } ``` |
| To | ``` struct PixMap {     var baseAddr: Ptr     var rowBytes: Int16     var bounds: Rect     var pmVersion: Int16     var packType: Int16     var packSize: Int32     var hRes: Fixed     var vRes: Fixed     var pixelType: Int16     var pixelSize: Int16     var cmpCount: Int16     var cmpSize: Int16     var pixelFormat: OSType     var pmTable: CTabHandle     var pmExt: UnsafeMutablePointer<Void>     init()     init(baseAddr baseAddr: Ptr, rowBytes rowBytes: Int16, bounds bounds: Rect, pmVersion pmVersion: Int16, packType packType: Int16, packSize packSize: Int32, hRes hRes: Fixed, vRes vRes: Fixed, pixelType pixelType: Int16, pixelSize pixelSize: Int16, cmpCount cmpCount: Int16, cmpSize cmpSize: Int16, pixelFormat pixelFormat: OSType, pmTable pmTable: CTabHandle, pmExt pmExt: UnsafeMutablePointer<Void>) } ``` |

Modified PixMap.pmExt

|  | Declaration |
| --- | --- |
| From | ``` var pmExt: UnsafePointer<()> ``` |
| To | ``` var pmExt: UnsafeMutablePointer<Void> ``` |

Modified PixPat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PixPat {     var patType: Int16     var patMap: PixMapHandle     var patData: Handle     var patXData: Handle     var patXValid: Int16     var patXMap: Handle     var pat1Data: Pattern } ``` |
| To | ``` struct PixPat {     var patType: Int16     var patMap: PixMapHandle     var patData: Handle     var patXData: Handle     var patXValid: Int16     var patXMap: Handle     var pat1Data: Pattern     init()     init(patType patType: Int16, patMap patMap: PixMapHandle, patData patData: Handle, patXData patXData: Handle, patXValid patXValid: Int16, patXMap patXMap: Handle, pat1Data pat1Data: Pattern) } ``` |

Modified ProcessInfoExtendedRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ProcessInfoExtendedRec {     var processInfoLength: UInt32     var processName: StringPtr     var processNumber: ProcessSerialNumber     var processType: UInt32     var processSignature: OSType     var processMode: UInt32     var processLocation: Ptr     var processSize: UInt32     var processFreeMem: UInt32     var processLauncher: ProcessSerialNumber     var processLaunchDate: UInt32     var processActiveTime: UInt32     var processAppRef: FSRefPtr     var processTempMemTotal: UInt32     var processPurgeableTempMemTotal: UInt32 } ``` |
| To | ``` struct ProcessInfoExtendedRec {     var processInfoLength: UInt32     var processName: StringPtr     var processNumber: ProcessSerialNumber     var processType: UInt32     var processSignature: OSType     var processMode: UInt32     var processLocation: Ptr     var processSize: UInt32     var processFreeMem: UInt32     var processLauncher: ProcessSerialNumber     var processLaunchDate: UInt32     var processActiveTime: UInt32     var processAppRef: FSRefPtr     var processTempMemTotal: UInt32     var processPurgeableTempMemTotal: UInt32     init()     init(processInfoLength processInfoLength: UInt32, processName processName: StringPtr, processNumber processNumber: ProcessSerialNumber, processType processType: UInt32, processSignature processSignature: OSType, processMode processMode: UInt32, processLocation processLocation: Ptr, processSize processSize: UInt32, processFreeMem processFreeMem: UInt32, processLauncher processLauncher: ProcessSerialNumber, processLaunchDate processLaunchDate: UInt32, processActiveTime processActiveTime: UInt32, processAppRef processAppRef: FSRefPtr, processTempMemTotal processTempMemTotal: UInt32, processPurgeableTempMemTotal processPurgeableTempMemTotal: UInt32) } ``` |

Modified ProcessInfoRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ProcessInfoRec {     var processInfoLength: UInt32     var processName: StringPtr     var processNumber: ProcessSerialNumber     var processType: UInt32     var processSignature: OSType     var processMode: UInt32     var processLocation: Ptr     var processSize: UInt32     var processFreeMem: UInt32     var processLauncher: ProcessSerialNumber     var processLaunchDate: UInt32     var processActiveTime: UInt32     var processAppRef: FSRefPtr } ``` |
| To | ``` struct ProcessInfoRec {     var processInfoLength: UInt32     var processName: StringPtr     var processNumber: ProcessSerialNumber     var processType: UInt32     var processSignature: OSType     var processMode: UInt32     var processLocation: Ptr     var processSize: UInt32     var processFreeMem: UInt32     var processLauncher: ProcessSerialNumber     var processLaunchDate: UInt32     var processActiveTime: UInt32     var processAppRef: FSRefPtr     init()     init(processInfoLength processInfoLength: UInt32, processName processName: StringPtr, processNumber processNumber: ProcessSerialNumber, processType processType: UInt32, processSignature processSignature: OSType, processMode processMode: UInt32, processLocation processLocation: Ptr, processSize processSize: UInt32, processFreeMem processFreeMem: UInt32, processLauncher processLauncher: ProcessSerialNumber, processLaunchDate processLaunchDate: UInt32, processActiveTime processActiveTime: UInt32, processAppRef processAppRef: FSRefPtr) } ``` |

Modified RGBColor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct RGBColor {     var red: UInt16     var green: UInt16     var blue: UInt16 } ``` |
| To | ``` struct RGBColor {     var red: UInt16     var green: UInt16     var blue: UInt16     init()     init(red red: UInt16, green green: UInt16, blue blue: UInt16) } ``` |

Modified SizeResourceRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SizeResourceRec {     var flags: UInt16     var preferredHeapSize: UInt32     var minimumHeapSize: UInt32 } ``` |
| To | ``` struct SizeResourceRec {     var flags: UInt16     var preferredHeapSize: UInt32     var minimumHeapSize: UInt32     init()     init(flags flags: UInt16, preferredHeapSize preferredHeapSize: UInt32, minimumHeapSize minimumHeapSize: UInt32) } ``` |

Modified SpeechChannelRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SpeechChannelRecord {     var data: (Int) } ``` |
| To | ``` struct SpeechChannelRecord {     var data: (Int)     init()     init(data data: (Int)) } ``` |

Modified SpeechErrorInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SpeechErrorInfo {     var count: Int16     var oldest: OSErr     var oldPos: Int     var newest: OSErr     var newPos: Int } ``` |
| To | ``` struct SpeechErrorInfo {     var count: Int16     var oldest: OSErr     var oldPos: Int     var newest: OSErr     var newPos: Int     init()     init(count count: Int16, oldest oldest: OSErr, oldPos oldPos: Int, newest newest: OSErr, newPos newPos: Int) } ``` |

Modified SpeechStatusInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SpeechStatusInfo {     var outputBusy: Boolean     var outputPaused: Boolean     var inputBytesLeft: Int     var phonemeCode: Int16 } ``` |
| To | ``` struct SpeechStatusInfo {     var outputBusy: Boolean     var outputPaused: Boolean     var inputBytesLeft: Int     var phonemeCode: Int16     init()     init(outputBusy outputBusy: Boolean, outputPaused outputPaused: Boolean, inputBytesLeft inputBytesLeft: Int, phonemeCode phonemeCode: Int16) } ``` |

Modified SpeechVersionInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SpeechVersionInfo {     var synthType: OSType     var synthSubType: OSType     var synthManufacturer: OSType     var synthFlags: Int32     var synthVersion: NumVersion } ``` |
| To | ``` struct SpeechVersionInfo {     var synthType: OSType     var synthSubType: OSType     var synthManufacturer: OSType     var synthFlags: Int32     var synthVersion: NumVersion     init()     init(synthType synthType: OSType, synthSubType synthSubType: OSType, synthManufacturer synthManufacturer: OSType, synthFlags synthFlags: Int32, synthVersion synthVersion: NumVersion) } ``` |

Modified SpeechXtndData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SpeechXtndData {     var synthCreator: OSType     var synthData: (Byte, Byte) } ``` |
| To | ``` struct SpeechXtndData {     var synthCreator: OSType     var synthData: (UInt8, UInt8)     init()     init(synthCreator synthCreator: OSType, synthData synthData: (UInt8, UInt8)) } ``` |

Modified SpeechXtndData.synthData

|  | Declaration |
| --- | --- |
| From | ``` var synthData: (Byte, Byte) ``` |
| To | ``` var synthData: (UInt8, UInt8) ``` |

Modified StyleTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct StyleTable {     var fontClass: Int16     var offset: Int32     var reserved: Int32     var indexes: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct StyleTable {     var fontClass: Int16     var offset: Int32     var reserved: Int32     var indexes: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(fontClass fontClass: Int16, offset offset: Int32, reserved reserved: Int32, indexes indexes: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified VDGammaRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VDGammaRecord {     var csGTable: Ptr } ``` |
| To | ``` struct VDGammaRecord {     var csGTable: Ptr     init()     init(csGTable csGTable: Ptr) } ``` |

Modified VoiceDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VoiceDescription {     var length: Int32     var voice: VoiceSpec     var version: Int32     var name: Str63     var comment: Str255     var gender: Int16     var age: Int16     var script: Int16     var language: Int16     var region: Int16     var reserved: (Int32, Int32, Int32, Int32) } ``` |
| To | ``` struct VoiceDescription {     var length: Int32     var voice: VoiceSpec     var version: Int32     var name: Str63     var comment: Str255     var gender: Int16     var age: Int16     var script: Int16     var language: Int16     var region: Int16     var reserved: (Int32, Int32, Int32, Int32)     init()     init(length length: Int32, voice voice: VoiceSpec, version version: Int32, name name: Str63, comment comment: Str255, gender gender: Int16, age age: Int16, script script: Int16, language language: Int16, region region: Int16, reserved reserved: (Int32, Int32, Int32, Int32)) } ``` |

Modified VoiceFileInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VoiceFileInfo {     var fileSpec: FSSpec     var resID: Int16 } ``` |
| To | ``` struct VoiceFileInfo {     var fileSpec: FSSpec     var resID: Int16     init()     init(fileSpec fileSpec: FSSpec, resID resID: Int16) } ``` |

Modified VoiceSpec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VoiceSpec {     var creator: OSType     var id: OSType } ``` |
| To | ``` struct VoiceSpec {     var creator: OSType     var id: OSType     init()     init(creator creator: OSType, id id: OSType) } ``` |

Modified ATSCubicClosePathProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicClosePathProcPtr = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSCubicClosePathProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSCubicCurveToProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicCurveToProcPtr = CFunctionPointer<((ConstUnsafePointer<Float32Point>, ConstUnsafePointer<Float32Point>, ConstUnsafePointer<Float32Point>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSCubicCurveToProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSCubicLineToProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicLineToProcPtr = CFunctionPointer<((ConstUnsafePointer<Float32Point>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSCubicLineToProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSCubicMoveToProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSCubicMoveToProcPtr = CFunctionPointer<((ConstUnsafePointer<Float32Point>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSCubicMoveToProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSFontApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontApplierFunction = CFunctionPointer<((ATSFontRef, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSFontApplierFunction = CFunctionPointer<((ATSFontRef, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSFontFamilyApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontFamilyApplierFunction = CFunctionPointer<((ATSFontFamilyRef, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSFontFamilyApplierFunction = CFunctionPointer<((ATSFontFamilyRef, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSFontNotificationInfoRef

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontNotificationInfoRef = ATSFontNotificationInfo ``` |
| To | ``` typealias ATSFontNotificationInfoRef = COpaquePointer ``` |

Modified ATSFontNotificationRef

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontNotificationRef = ATSFontNotification ``` |
| To | ``` typealias ATSFontNotificationRef = COpaquePointer ``` |

Modified ATSFontQueryCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSFontQueryCallback = CFunctionPointer<((ATSFontQueryMessageID, CFPropertyListRef!, UnsafePointer<()>) -> Unmanaged<CFPropertyListRef>!)> ``` |
| To | ``` typealias ATSFontQueryCallback = CFunctionPointer<((ATSFontQueryMessageID, CFPropertyList!, UnsafeMutablePointer<Void>) -> Unmanaged<CFPropertyList>!)> ``` |

Modified ATSNotificationCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSNotificationCallback = CFunctionPointer<((ATSFontNotificationInfo!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias ATSNotificationCallback = CFunctionPointer<((ATSFontNotificationInfoRef, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified ATSQuadraticClosePathProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticClosePathProcPtr = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSQuadraticClosePathProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSQuadraticCurveProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticCurveProcPtr = CFunctionPointer<((ConstUnsafePointer<Float32Point>, ConstUnsafePointer<Float32Point>, ConstUnsafePointer<Float32Point>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSQuadraticCurveProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSQuadraticLineProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticLineProcPtr = CFunctionPointer<((ConstUnsafePointer<Float32Point>, ConstUnsafePointer<Float32Point>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSQuadraticLineProcPtr = CFunctionPointer<((UnsafePointer<Float32Point>, UnsafePointer<Float32Point>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSQuadraticNewPathProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSQuadraticNewPathProcPtr = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ATSQuadraticNewPathProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ATSUAttributeValuePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUAttributeValuePtr = UnsafePointer<()> ``` |
| To | ``` typealias ATSUAttributeValuePtr = UnsafeMutablePointer<Void> ``` |

Modified ATSUDirectLayoutOperationOverrideProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUDirectLayoutOperationOverrideProcPtr = CFunctionPointer<((ATSULayoutOperationSelector, ATSULine!, URefCon, UnsafePointer<()>, UnsafePointer<ATSULayoutOperationCallbackStatus>) -> OSStatus)> ``` |
| To | ``` typealias ATSUDirectLayoutOperationOverrideProcPtr = CFunctionPointer<((ATSULayoutOperationSelector, ATSULineRef, URefCon, UnsafeMutablePointer<Void>, UnsafeMutablePointer<ATSULayoutOperationCallbackStatus>) -> OSStatus)> ``` |

Modified ATSULineRef

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSULineRef = ATSULine ``` |
| To | ``` typealias ATSULineRef = COpaquePointer ``` |

Modified ATSUStyleSettingRef

|  | Declaration |
| --- | --- |
| From | ``` typealias ATSUStyleSettingRef = ATSUStyleSetting ``` |
| To | ``` typealias ATSUStyleSettingRef = COpaquePointer ``` |

Modified AXIsProcessTrusted() -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified AXIsProcessTrustedWithOptions(CFDictionary!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AXObserverAddNotification(AXObserver!, AXUIElement!, CFString!, UnsafeMutablePointer<Void>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverAddNotification(_ observer: AXObserver!, _ element: AXUIElement!, _ notification: CFString!, _ refcon: UnsafePointer<()>) -> AXError ``` |
| To | ``` func AXObserverAddNotification(_ observer: AXObserver!, _ element: AXUIElement!, _ notification: CFString!, _ refcon: UnsafeMutablePointer<Void>) -> AXError ``` |

Modified AXObserverCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AXObserverCallback = CFunctionPointer<((AXObserver!, AXUIElement!, CFString!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias AXObserverCallback = CFunctionPointer<((AXObserver!, AXUIElement!, CFString!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified AXObserverCallbackWithInfo

|  | Declaration |
| --- | --- |
| From | ``` typealias AXObserverCallbackWithInfo = CFunctionPointer<((AXObserver!, AXUIElement!, CFString!, CFDictionary!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias AXObserverCallbackWithInfo = CFunctionPointer<((AXObserver!, AXUIElement!, CFString!, CFDictionary!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified AXObserverCreate(pid_t, AXObserverCallback, UnsafeMutablePointer<Unmanaged<AXObserver>?>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverCreate(_ application: pid_t, _ callback: AXObserverCallback, _ outObserver: UnsafePointer<Unmanaged<AXObserver>?>) -> AXError ``` |
| To | ``` func AXObserverCreate(_ application: pid_t, _ callback: AXObserverCallback, _ outObserver: UnsafeMutablePointer<Unmanaged<AXObserver>?>) -> AXError ``` |

Modified AXObserverCreateWithInfoCallback(pid_t, AXObserverCallbackWithInfo, UnsafeMutablePointer<Unmanaged<AXObserver>?>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXObserverCreateWithInfoCallback(_ application: pid_t, _ callback: AXObserverCallbackWithInfo, _ outObserver: UnsafePointer<Unmanaged<AXObserver>?>) -> AXError ``` |
| To | ``` func AXObserverCreateWithInfoCallback(_ application: pid_t, _ callback: AXObserverCallbackWithInfo, _ outObserver: UnsafeMutablePointer<Unmanaged<AXObserver>?>) -> AXError ``` |

Modified AXUIElementCopyActionDescription(AXUIElement!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyActionDescription(_ element: AXUIElement!, _ action: CFString!, _ description: UnsafePointer<Unmanaged<CFString>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyActionDescription(_ element: AXUIElement!, _ action: CFString!, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AXError ``` |

Modified AXUIElementCopyActionNames(AXUIElement!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyActionNames(_ element: AXUIElement!, _ names: UnsafePointer<Unmanaged<CFArray>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyActionNames(_ element: AXUIElement!, _ names: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` |

Modified AXUIElementCopyAttributeNames(AXUIElement!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyAttributeNames(_ element: AXUIElement!, _ names: UnsafePointer<Unmanaged<CFArray>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyAttributeNames(_ element: AXUIElement!, _ names: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` |

Modified AXUIElementCopyAttributeValue(AXUIElement!, CFString!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyAttributeValue(_ element: AXUIElement!, _ attribute: CFString!, _ value: UnsafePointer<Unmanaged<AnyObject>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyAttributeValue(_ element: AXUIElement!, _ attribute: CFString!, _ value: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> AXError ``` |

Modified AXUIElementCopyAttributeValues(AXUIElement!, CFString!, CFIndex, CFIndex, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyAttributeValues(_ element: AXUIElement!, _ attribute: CFString!, _ index: CFIndex, _ maxValues: CFIndex, _ values: UnsafePointer<Unmanaged<CFArray>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyAttributeValues(_ element: AXUIElement!, _ attribute: CFString!, _ index: CFIndex, _ maxValues: CFIndex, _ values: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` |

Modified AXUIElementCopyElementAtPosition(AXUIElement!, Float, Float, UnsafeMutablePointer<Unmanaged<AXUIElement>?>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementCopyElementAtPosition(_ application: AXUIElement!, _ x: Float, _ y: Float, _ element: UnsafePointer<Unmanaged<AXUIElement>?>) -> AXError ``` |
| To | ``` func AXUIElementCopyElementAtPosition(_ application: AXUIElement!, _ x: Float, _ y: Float, _ element: UnsafeMutablePointer<Unmanaged<AXUIElement>?>) -> AXError ``` |

Modified AXUIElementCopyMultipleAttributeValues(AXUIElement!, CFArray!, AXCopyMultipleAttributeOptions, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AXUIElementCopyMultipleAttributeValues(_ element: AXUIElement!, _ attributes: CFArray!, _ options: AXCopyMultipleAttributeOptions, _ values: UnsafePointer<Unmanaged<CFArray>?>) -> AXError ``` | OS X 10.10 |
| To | ``` func AXUIElementCopyMultipleAttributeValues(_ element: AXUIElement!, _ attributes: CFArray!, _ options: AXCopyMultipleAttributeOptions, _ values: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` | OS X 10.4 |

Modified AXUIElementCopyParameterizedAttributeNames(AXUIElement!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AXUIElementCopyParameterizedAttributeNames(_ element: AXUIElement!, _ names: UnsafePointer<Unmanaged<CFArray>?>) -> AXError ``` | OS X 10.10 |
| To | ``` func AXUIElementCopyParameterizedAttributeNames(_ element: AXUIElement!, _ names: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> AXError ``` | OS X 10.3 |

Modified AXUIElementCopyParameterizedAttributeValue(AXUIElement!, CFString!, AnyObject!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> AXError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AXUIElementCopyParameterizedAttributeValue(_ element: AXUIElement!, _ parameterizedAttribute: CFString!, _ parameter: AnyObject!, _ result: UnsafePointer<Unmanaged<AnyObject>?>) -> AXError ``` | OS X 10.10 |
| To | ``` func AXUIElementCopyParameterizedAttributeValue(_ element: AXUIElement!, _ parameterizedAttribute: CFString!, _ parameter: AnyObject!, _ result: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> AXError ``` | OS X 10.3 |

Modified AXUIElementGetAttributeValueCount(AXUIElement!, CFString!, UnsafeMutablePointer<CFIndex>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementGetAttributeValueCount(_ element: AXUIElement!, _ attribute: CFString!, _ count: UnsafePointer<CFIndex>) -> AXError ``` |
| To | ``` func AXUIElementGetAttributeValueCount(_ element: AXUIElement!, _ attribute: CFString!, _ count: UnsafeMutablePointer<CFIndex>) -> AXError ``` |

Modified AXUIElementGetPid(AXUIElement!, UnsafeMutablePointer<pid_t>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementGetPid(_ element: AXUIElement!, _ pid: UnsafePointer<pid_t>) -> AXError ``` |
| To | ``` func AXUIElementGetPid(_ element: AXUIElement!, _ pid: UnsafeMutablePointer<pid_t>) -> AXError ``` |

Modified AXUIElementIsAttributeSettable(AXUIElement!, CFString!, UnsafeMutablePointer<Boolean>) -> AXError

|  | Declaration |
| --- | --- |
| From | ``` func AXUIElementIsAttributeSettable(_ element: AXUIElement!, _ attribute: CFString!, _ settable: UnsafePointer<Boolean>) -> AXError ``` |
| To | ``` func AXUIElementIsAttributeSettable(_ element: AXUIElement!, _ attribute: CFString!, _ settable: UnsafeMutablePointer<Boolean>) -> AXError ``` |

Modified AXUIElementSetMessagingTimeout(AXUIElement!, Float) -> AXError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified AXValueCreate(AXValueType, UnsafePointer<Void>) -> Unmanaged<AXValue>!

|  | Declaration |
| --- | --- |
| From | ``` func AXValueCreate(_ theType: AXValueType, _ valuePtr: ConstUnsafePointer<()>) -> Unmanaged<AXValue>! ``` |
| To | ``` func AXValueCreate(_ theType: AXValueType, _ valuePtr: UnsafePointer<Void>) -> Unmanaged<AXValue>! ``` |

Modified AXValueGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified AXValueGetValue(AXValue!, AXValueType, UnsafeMutablePointer<Void>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func AXValueGetValue(_ value: AXValue!, _ theType: AXValueType, _ valuePtr: UnsafePointer<()>) -> Boolean ``` |
| To | ``` func AXValueGetValue(_ value: AXValue!, _ theType: AXValueType, _ valuePtr: UnsafeMutablePointer<Void>) -> Boolean ``` |

Modified AppParametersPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias AppParametersPtr = UnsafePointer<AppParameters> ``` |
| To | ``` typealias AppParametersPtr = UnsafeMutablePointer<AppParameters> ``` |

Modified BitMapHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias BitMapHandle = UnsafePointer<BitMapPtr> ``` |
| To | ``` typealias BitMapHandle = UnsafeMutablePointer<BitMapPtr> ``` |

Modified BitMapPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias BitMapPtr = UnsafePointer<BitMap> ``` |
| To | ``` typealias BitMapPtr = UnsafeMutablePointer<BitMap> ``` |

Modified CM2ProfilePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CM2ProfilePtr = UnsafePointer<CM2Profile> ``` |
| To | ``` typealias CM2ProfilePtr = UnsafeMutablePointer<CM2Profile> ``` |

Modified CMFlattenProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CMFlattenProcPtr = CFunctionPointer<((Int32, UnsafePointer<Int>, UnsafePointer<()>, UnsafePointer<()>) -> OSErr)> ``` |
| To | ``` typealias CMFlattenProcPtr = CFunctionPointer<((Int32, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSErr)> ``` |

Modified CMMApplyTransformProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMApplyTransformProc = CFunctionPointer<((ColorSyncTransform!, UInt, UInt, UInt, UnsafePointer<UnsafePointer<()>>, ColorSyncDataDepth, ColorSyncDataLayout, UInt, UInt, UnsafePointer<ConstUnsafePointer<()>>, ColorSyncDataDepth, ColorSyncDataLayout, UInt, CFDictionary!) -> Bool)> ``` |
| To | ``` typealias CMMApplyTransformProc = CFunctionPointer<((ColorSyncTransform!, Int, Int, Int, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, ColorSyncDataDepth, ColorSyncDataLayout, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary!) -> Bool)> ``` |

Modified CQDProcsPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CQDProcsPtr = UnsafePointer<CQDProcs> ``` |
| To | ``` typealias CQDProcsPtr = UnsafeMutablePointer<CQDProcs> ``` |

Modified CTabHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias CTabHandle = UnsafePointer<CTabPtr> ``` |
| To | ``` typealias CTabHandle = UnsafeMutablePointer<CTabPtr> ``` |

Modified CTabPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias CTabPtr = UnsafePointer<ColorTable> ``` |
| To | ``` typealias CTabPtr = UnsafeMutablePointer<ColorTable> ``` |

Modified ColorComplementProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorComplementProcPtr = CFunctionPointer<((UnsafePointer<RGBColor>) -> Boolean)> ``` |
| To | ``` typealias ColorComplementProcPtr = CFunctionPointer<((UnsafeMutablePointer<RGBColor>) -> Boolean)> ``` |

Modified ColorSearchProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSearchProcPtr = CFunctionPointer<((UnsafePointer<RGBColor>, UnsafePointer<Int>) -> Boolean)> ``` |
| To | ``` typealias ColorSearchProcPtr = CFunctionPointer<((UnsafeMutablePointer<RGBColor>, UnsafeMutablePointer<Int>) -> Boolean)> ``` |

Modified ColorSpecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSpecPtr = UnsafePointer<ColorSpec> ``` |
| To | ``` typealias ColorSpecPtr = UnsafeMutablePointer<ColorSpec> ``` |

Modified ColorSyncCMMIterateCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncCMMIterateCallback = CFunctionPointer<((ColorSyncCMM!, UnsafePointer<()>) -> Bool)> ``` |
| To | ``` typealias ColorSyncCMMIterateCallback = CFunctionPointer<((ColorSyncCMM!, UnsafeMutablePointer<Void>) -> Bool)> ``` |

Modified ColorSyncDeviceProfileIterateCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncDeviceProfileIterateCallback = CFunctionPointer<((CFDictionary!, UnsafePointer<()>) -> Bool)> ``` |
| To | ``` typealias ColorSyncDeviceProfileIterateCallback = CFunctionPointer<((CFDictionary!, UnsafeMutablePointer<Void>) -> Bool)> ``` |

Modified ColorSyncIterateDeviceProfiles(ColorSyncDeviceProfileIterateCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateDeviceProfiles(_ callBack: ColorSyncDeviceProfileIterateCallback, _ userInfo: UnsafePointer<()>) ``` |
| To | ``` func ColorSyncIterateDeviceProfiles(_ callBack: ColorSyncDeviceProfileIterateCallback, _ userInfo: UnsafeMutablePointer<Void>) ``` |

Modified ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback, UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateInstalledCMMs(_ callBack: ColorSyncCMMIterateCallback, _ userInfo: UnsafePointer<()>) ``` |
| To | ``` func ColorSyncIterateInstalledCMMs(_ callBack: ColorSyncCMMIterateCallback, _ userInfo: UnsafeMutablePointer<Void>) ``` |

Modified ColorSyncIterateInstalledProfiles(ColorSyncProfileIterateCallback, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<CFError>?>)

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncIterateInstalledProfiles(_ callBack: ColorSyncProfileIterateCallback, _ seed: UnsafePointer<UInt32>, _ userInfo: UnsafePointer<()>, _ error: UnsafePointer<Unmanaged<CFError>?>) ``` |
| To | ``` func ColorSyncIterateInstalledProfiles(_ callBack: ColorSyncProfileIterateCallback, _ seed: UnsafeMutablePointer<UInt32>, _ userInfo: UnsafeMutablePointer<Void>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) ``` |

Modified ColorSyncProfileCopyData(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileCopyData(_ prof: ColorSyncProfile!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func ColorSyncProfileCopyData(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |

Modified ColorSyncProfileCreate(CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ColorSyncProfile>!

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileCreate(_ data: CFData!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ColorSyncProfile>! ``` |
| To | ``` func ColorSyncProfileCreate(_ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ColorSyncProfile>! ``` |

Modified ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_ profile: ColorSyncProfile!, _ nSamplesPerChannel: UnsafePointer<UInt>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(_ profile: ColorSyncProfile!, _ nSamplesPerChannel: UnsafeMutablePointer<Int>) -> Unmanaged<CFData>! ``` | OS X 10.10.3 |

Modified ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ColorSyncProfile>!

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileCreateWithURL(_ url: CFURL!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<ColorSyncProfile>! ``` |
| To | ``` func ColorSyncProfileCreateWithURL(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ColorSyncProfile>! ``` |

Modified ColorSyncProfileEstimateGamma(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileEstimateGamma(_ prof: ColorSyncProfile!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Float ``` |
| To | ``` func ColorSyncProfileEstimateGamma(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Float ``` |

Modified ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileEstimateGammaWithDisplayID(_ displayID: Int32, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Float ``` |
| To | ``` func ColorSyncProfileEstimateGammaWithDisplayID(_ displayID: Int32, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Float ``` |

Modified ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_ profile: ColorSyncProfile!, _ redMin: UnsafePointer<Float>, _ redMax: UnsafePointer<Float>, _ redGamma: UnsafePointer<Float>, _ greenMin: UnsafePointer<Float>, _ greenMax: UnsafePointer<Float>, _ greenGamma: UnsafePointer<Float>, _ blueMin: UnsafePointer<Float>, _ blueMax: UnsafePointer<Float>, _ blueGamma: UnsafePointer<Float>) -> Bool ``` |
| To | ``` func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_ profile: ColorSyncProfile!, _ redMin: UnsafeMutablePointer<Float>, _ redMax: UnsafeMutablePointer<Float>, _ redGamma: UnsafeMutablePointer<Float>, _ greenMin: UnsafeMutablePointer<Float>, _ greenMax: UnsafeMutablePointer<Float>, _ greenGamma: UnsafeMutablePointer<Float>, _ blueMin: UnsafeMutablePointer<Float>, _ blueMax: UnsafeMutablePointer<Float>, _ blueGamma: UnsafeMutablePointer<Float>) -> Bool ``` |

Modified ColorSyncProfileGetURL(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>!

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileGetURL(_ prof: ColorSyncProfile!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |
| To | ``` func ColorSyncProfileGetURL(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFURL>! ``` |

Modified ColorSyncProfileIterateCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias ColorSyncProfileIterateCallback = CFunctionPointer<((CFDictionary!, UnsafePointer<()>) -> Bool)> ``` |
| To | ``` typealias ColorSyncProfileIterateCallback = CFunctionPointer<((CFDictionary!, UnsafeMutablePointer<Void>) -> Bool)> ``` |

Modified ColorSyncProfileVerify(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ColorSyncProfileVerify(_ prof: ColorSyncProfile!, _ errors: UnsafePointer<Unmanaged<CFError>?>, _ warnings: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ColorSyncProfileVerify(_ prof: ColorSyncProfile!, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>, _ warnings: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified ColorSyncTransformConvert(ColorSyncTransform!, Int, Int, UnsafeMutablePointer<Void>, ColorSyncDataDepth, ColorSyncDataLayout, Int, UnsafePointer<Void>, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary!) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ColorSyncTransformConvert(_ transform: ColorSyncTransform!, _ width: UInt, _ height: UInt, _ dst: UnsafePointer<()>, _ dstDepth: ColorSyncDataDepth, _ dstLayout: ColorSyncDataLayout, _ dstBytesPerRow: UInt, _ src: ConstUnsafePointer<()>, _ srcDepth: ColorSyncDataDepth, _ srcLayout: ColorSyncDataLayout, _ srcBytesPerRow: UInt, _ options: CFDictionary!) -> Bool ``` | OS X 10.10 |
| To | ``` func ColorSyncTransformConvert(_ transform: ColorSyncTransform!, _ width: Int, _ height: Int, _ dst: UnsafeMutablePointer<Void>, _ dstDepth: ColorSyncDataDepth, _ dstLayout: ColorSyncDataLayout, _ dstBytesPerRow: Int, _ src: UnsafePointer<Void>, _ srcDepth: ColorSyncDataDepth, _ srcLayout: ColorSyncDataLayout, _ srcBytesPerRow: Int, _ options: CFDictionary!) -> Bool ``` | OS X 10.10.3 |

Modified ConstATSUAttributeValuePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ConstATSUAttributeValuePtr = ConstUnsafePointer<()> ``` |
| To | ``` typealias ConstATSUAttributeValuePtr = UnsafePointer<Void> ``` |

Modified CopyPhonemesFromText(SpeechChannel, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSErr

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopyPhonemesFromText(_ chan: SpeechChannel, _ text: CFString!, _ phonemes: UnsafePointer<Unmanaged<CFString>?>) -> OSErr ``` | OS X 10.10 |
| To | ``` func CopyPhonemesFromText(_ chan: SpeechChannel, _ text: CFString!, _ phonemes: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSErr ``` | OS X 10.5 |

Modified CopySpeechProperty(SpeechChannel, CFString!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSErr

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopySpeechProperty(_ chan: SpeechChannel, _ property: CFString!, _ object: UnsafePointer<Unmanaged<AnyObject>?>) -> OSErr ``` | OS X 10.10 |
| To | ``` func CopySpeechProperty(_ chan: SpeechChannel, _ property: CFString!, _ object: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSErr ``` | OS X 10.5 |

Modified CountVoices(UnsafeMutablePointer<Int16>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func CountVoices(_ numVoices: UnsafePointer<Int16>) -> OSErr ``` |
| To | ``` func CountVoices(_ numVoices: UnsafeMutablePointer<Int16>) -> OSErr ``` |

Modified DCMDictionaryRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMDictionaryRef = DCMDictionary ``` |
| To | ``` typealias DCMDictionaryRef = DCMObjectRef ``` |

Modified DCMDictionaryStreamRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMDictionaryStreamRef = DCMDictionaryStream ``` |
| To | ``` typealias DCMDictionaryStreamRef = DCMObjectRef ``` |

Modified DCMObjectRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DCMObjectRef = DCMObject ``` |
| To | ``` typealias DCMObjectRef = COpaquePointer ``` |

Modified FMFontCallbackFilterProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FMFontCallbackFilterProcPtr = CFunctionPointer<((FMFont, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias FMFontCallbackFilterProcPtr = CFunctionPointer<((FMFont, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified FMFontFamilyCallbackFilterProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FMFontFamilyCallbackFilterProcPtr = CFunctionPointer<((FMFontFamily, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias FMFontFamilyCallbackFilterProcPtr = CFunctionPointer<((FMFontFamily, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified FontRecHdl

|  | Declaration |
| --- | --- |
| From | ``` typealias FontRecHdl = UnsafePointer<FontRecPtr> ``` |
| To | ``` typealias FontRecHdl = UnsafeMutablePointer<FontRecPtr> ``` |

Modified FontRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias FontRecPtr = UnsafePointer<FontRec> ``` |
| To | ``` typealias FontRecPtr = UnsafeMutablePointer<FontRec> ``` |

Modified GDHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias GDHandle = UnsafePointer<GDPtr> ``` |
| To | ``` typealias GDHandle = UnsafeMutablePointer<GDPtr> ``` |

Modified GDPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias GDPtr = UnsafePointer<GDevice> ``` |
| To | ``` typealias GDPtr = UnsafeMutablePointer<GDevice> ``` |

Modified GetIconRefVariant(IconRef, OSType, UnsafeMutablePointer<IconTransformType>) -> IconRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GetIconRefVariant(_ inIconRef: Icon!, _ inVariant: OSType, _ outTransform: UnsafePointer<IconTransformType>) -> Unmanaged<Icon>! ``` | OS X 10.10 |
| To | ``` func GetIconRefVariant(_ inIconRef: IconRef, _ inVariant: OSType, _ outTransform: UnsafeMutablePointer<IconTransformType>) -> IconRef ``` | OS X 10.10.3 |

Modified GetIndVoice(Int16, UnsafeMutablePointer<VoiceSpec>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func GetIndVoice(_ index: Int16, _ voice: UnsafePointer<VoiceSpec>) -> OSErr ``` |
| To | ``` func GetIndVoice(_ index: Int16, _ voice: UnsafeMutablePointer<VoiceSpec>) -> OSErr ``` |

Modified GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func GetSpeechPitch(_ chan: SpeechChannel, _ pitch: UnsafePointer<Fixed>) -> OSErr ``` |
| To | ``` func GetSpeechPitch(_ chan: SpeechChannel, _ pitch: UnsafeMutablePointer<Fixed>) -> OSErr ``` |

Modified GetSpeechRate(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func GetSpeechRate(_ chan: SpeechChannel, _ rate: UnsafePointer<Fixed>) -> OSErr ``` |
| To | ``` func GetSpeechRate(_ chan: SpeechChannel, _ rate: UnsafeMutablePointer<Fixed>) -> OSErr ``` |

Modified GetVoiceDescription(UnsafePointer<VoiceSpec>, UnsafeMutablePointer<VoiceDescription>, Int) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func GetVoiceDescription(_ voice: ConstUnsafePointer<VoiceSpec>, _ info: UnsafePointer<VoiceDescription>, _ infoLength: Int) -> OSErr ``` |
| To | ``` func GetVoiceDescription(_ voice: UnsafePointer<VoiceSpec>, _ info: UnsafeMutablePointer<VoiceDescription>, _ infoLength: Int) -> OSErr ``` |

Modified GetVoiceInfo(UnsafePointer<VoiceSpec>, OSType, UnsafeMutablePointer<Void>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func GetVoiceInfo(_ voice: ConstUnsafePointer<VoiceSpec>, _ selector: OSType, _ voiceInfo: UnsafePointer<()>) -> OSErr ``` |
| To | ``` func GetVoiceInfo(_ voice: UnsafePointer<VoiceSpec>, _ selector: OSType, _ voiceInfo: UnsafeMutablePointer<Void>) -> OSErr ``` |

Modified HIShapeContainsPoint(HIShape!, UnsafePointer<CGPoint>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIShapeContainsPoint(_ inShape: HIShape!, _ inPoint: ConstUnsafePointer<CGPoint>) -> Boolean ``` | OS X 10.10 |
| To | ``` func HIShapeContainsPoint(_ inShape: HIShape!, _ inPoint: UnsafePointer<CGPoint>) -> Boolean ``` | OS X 10.2 |

Modified HIShapeCreateCopy(HIShape!) -> Unmanaged<HIShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeCreateDifference(HIShape!, HIShape!) -> Unmanaged<HIShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeCreateEmpty() -> Unmanaged<HIShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified HIShapeCreateIntersection(HIShape!, HIShape!) -> Unmanaged<HIShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeCreateMutable() -> Unmanaged<HIMutableShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeCreateMutableCopy(HIShape!) -> Unmanaged<HIMutableShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeCreateMutableWithRect(UnsafePointer<CGRect>) -> Unmanaged<HIMutableShape>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIShapeCreateMutableWithRect(_ inRect: ConstUnsafePointer<CGRect>) -> Unmanaged<HIMutableShape>! ``` | OS X 10.10 |
| To | ``` func HIShapeCreateMutableWithRect(_ inRect: UnsafePointer<CGRect>) -> Unmanaged<HIMutableShape>! ``` | OS X 10.5 |

Modified HIShapeCreateUnion(HIShape!, HIShape!) -> Unmanaged<HIShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeCreateWithQDRgn(RgnHandle) -> Unmanaged<HIShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeCreateWithRect(UnsafePointer<CGRect>) -> Unmanaged<HIShape>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIShapeCreateWithRect(_ inRect: ConstUnsafePointer<CGRect>) -> Unmanaged<HIShape>! ``` | OS X 10.10 |
| To | ``` func HIShapeCreateWithRect(_ inRect: UnsafePointer<CGRect>) -> Unmanaged<HIShape>! ``` | OS X 10.2 |

Modified HIShapeCreateXor(HIShape!, HIShape!) -> Unmanaged<HIShape>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified HIShapeDifference(HIShape!, HIShape!, HIMutableShape!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeEnumerate(HIShape!, OptionBits, HIShapeEnumerateProcPtr, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIShapeEnumerate(_ inShape: HIShape!, _ inOptions: OptionBits, _ inProc: HIShapeEnumerateProcPtr, _ inRefcon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIShapeEnumerate(_ inShape: HIShape!, _ inOptions: OptionBits, _ inProc: HIShapeEnumerateProcPtr, _ inRefcon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified HIShapeEnumerateProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias HIShapeEnumerateProcPtr = CFunctionPointer<((Int32, HIShape!, ConstUnsafePointer<CGRect>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias HIShapeEnumerateProcPtr = CFunctionPointer<((Int32, HIShape!, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified HIShapeGetAsQDRgn(HIShape!, RgnHandle) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeGetBounds(HIShape!, UnsafeMutablePointer<CGRect>) -> UnsafeMutablePointer<CGRect>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIShapeGetBounds(_ inShape: HIShape!, _ outRect: UnsafePointer<CGRect>) -> UnsafePointer<CGRect> ``` | OS X 10.10 |
| To | ``` func HIShapeGetBounds(_ inShape: HIShape!, _ outRect: UnsafeMutablePointer<CGRect>) -> UnsafeMutablePointer<CGRect> ``` | OS X 10.2 |

Modified HIShapeGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeInset(HIMutableShape!, CGFloat, CGFloat) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified HIShapeIntersect(HIShape!, HIShape!, HIMutableShape!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeIntersectsRect(HIShape!, UnsafePointer<CGRect>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIShapeIntersectsRect(_ inShape: HIShape!, _ inRect: ConstUnsafePointer<CGRect>) -> Boolean ``` | OS X 10.10 |
| To | ``` func HIShapeIntersectsRect(_ inShape: HIShape!, _ inRect: UnsafePointer<CGRect>) -> Boolean ``` | OS X 10.4 |

Modified HIShapeIsEmpty(HIShape!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeIsRectangular(HIShape!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeOffset(HIMutableShape!, CGFloat, CGFloat) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeReplacePathInCGContext(HIShape!, CGContext!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeSetEmpty(HIMutableShape!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeSetWithShape(HIMutableShape!, HIShape!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified HIShapeUnion(HIShape!, HIShape!, HIMutableShape!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified HIShapeUnionWithRect(HIMutableShape!, UnsafePointer<CGRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func HIShapeUnionWithRect(_ inShape: HIMutableShape!, _ inRect: ConstUnsafePointer<CGRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func HIShapeUnionWithRect(_ inShape: HIMutableShape!, _ inRect: UnsafePointer<CGRect>) -> OSStatus ``` | OS X 10.5 |

Modified HIShapeXor(HIShape!, HIShape!, HIMutableShape!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified ICAppSpecHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ICAppSpecHandle = UnsafePointer<ICAppSpecPtr> ``` |
| To | ``` typealias ICAppSpecHandle = UnsafeMutablePointer<ICAppSpecPtr> ``` |

Modified ICAppSpecListHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ICAppSpecListHandle = UnsafePointer<ICAppSpecListPtr> ``` |
| To | ``` typealias ICAppSpecListHandle = UnsafeMutablePointer<ICAppSpecListPtr> ``` |

Modified ICAppSpecListPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICAppSpecListPtr = UnsafePointer<ICAppSpecList> ``` |
| To | ``` typealias ICAppSpecListPtr = UnsafeMutablePointer<ICAppSpecList> ``` |

Modified ICAppSpecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICAppSpecPtr = UnsafePointer<ICAppSpec> ``` |
| To | ``` typealias ICAppSpecPtr = UnsafeMutablePointer<ICAppSpec> ``` |

Modified ICCharTableHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ICCharTableHandle = UnsafePointer<ICCharTablePtr> ``` |
| To | ``` typealias ICCharTableHandle = UnsafeMutablePointer<ICCharTablePtr> ``` |

Modified ICCharTablePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICCharTablePtr = UnsafePointer<ICCharTable> ``` |
| To | ``` typealias ICCharTablePtr = UnsafeMutablePointer<ICCharTable> ``` |

Modified ICFileSpecHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ICFileSpecHandle = UnsafePointer<ICFileSpecPtr> ``` |
| To | ``` typealias ICFileSpecHandle = UnsafeMutablePointer<ICFileSpecPtr> ``` |

Modified ICFileSpecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICFileSpecPtr = UnsafePointer<ICFileSpec> ``` |
| To | ``` typealias ICFileSpecPtr = UnsafeMutablePointer<ICFileSpec> ``` |

Modified ICFontRecordHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ICFontRecordHandle = UnsafePointer<ICFontRecordPtr> ``` |
| To | ``` typealias ICFontRecordHandle = UnsafeMutablePointer<ICFontRecordPtr> ``` |

Modified ICFontRecordPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICFontRecordPtr = UnsafePointer<ICFontRecord> ``` |
| To | ``` typealias ICFontRecordPtr = UnsafeMutablePointer<ICFontRecord> ``` |

Modified ICMapEntryHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ICMapEntryHandle = UnsafePointer<ICMapEntryPtr> ``` |
| To | ``` typealias ICMapEntryHandle = UnsafeMutablePointer<ICMapEntryPtr> ``` |

Modified ICMapEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICMapEntryPtr = UnsafePointer<ICMapEntry> ``` |
| To | ``` typealias ICMapEntryPtr = UnsafeMutablePointer<ICMapEntry> ``` |

Modified ICProfileIDPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICProfileIDPtr = UnsafePointer<ICProfileID> ``` |
| To | ``` typealias ICProfileIDPtr = UnsafeMutablePointer<ICProfileID> ``` |

Modified ICServiceEntryHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ICServiceEntryHandle = UnsafePointer<ICServiceEntryPtr> ``` |
| To | ``` typealias ICServiceEntryHandle = UnsafeMutablePointer<ICServiceEntryPtr> ``` |

Modified ICServiceEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICServiceEntryPtr = UnsafePointer<ICServiceEntry> ``` |
| To | ``` typealias ICServiceEntryPtr = UnsafeMutablePointer<ICServiceEntry> ``` |

Modified ICServicesHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ICServicesHandle = UnsafePointer<ICServicesPtr> ``` |
| To | ``` typealias ICServicesHandle = UnsafeMutablePointer<ICServicesPtr> ``` |

Modified ICServicesPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ICServicesPtr = UnsafePointer<ICServices> ``` |
| To | ``` typealias ICServicesPtr = UnsafeMutablePointer<ICServices> ``` |

Modified IconActionProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias IconActionProcPtr = CFunctionPointer<((ResType, UnsafePointer<Handle>, UnsafePointer<()>) -> OSErr)> ``` |
| To | ``` typealias IconActionProcPtr = CFunctionPointer<((ResType, UnsafeMutablePointer<Handle>, UnsafeMutablePointer<Void>) -> OSErr)> ``` |

Modified IconGetterProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias IconGetterProcPtr = CFunctionPointer<((ResType, UnsafePointer<()>) -> Handle)> ``` |
| To | ``` typealias IconGetterProcPtr = CFunctionPointer<((ResType, UnsafeMutablePointer<Void>) -> Handle)> ``` |

Modified IconRefContainsCGPoint(UnsafePointer<CGPoint>, UnsafePointer<CGRect>, IconAlignmentType, IconServicesUsageFlags, IconRef) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IconRefContainsCGPoint(_ testPt: ConstUnsafePointer<CGPoint>, _ iconRect: ConstUnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: Icon!) -> Boolean ``` | OS X 10.10 |
| To | ``` func IconRefContainsCGPoint(_ testPt: UnsafePointer<CGPoint>, _ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Boolean ``` | OS X 10.5 |

Modified IconRefIntersectsCGRect(UnsafePointer<CGRect>, UnsafePointer<CGRect>, IconAlignmentType, IconServicesUsageFlags, IconRef) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IconRefIntersectsCGRect(_ testRect: ConstUnsafePointer<CGRect>, _ iconRect: ConstUnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: Icon!) -> Boolean ``` | OS X 10.10 |
| To | ``` func IconRefIntersectsCGRect(_ testRect: UnsafePointer<CGRect>, _ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Boolean ``` | OS X 10.5 |

Modified IconRefToHIShape(UnsafePointer<CGRect>, IconAlignmentType, IconServicesUsageFlags, IconRef) -> Unmanaged<HIShape>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IconRefToHIShape(_ iconRect: ConstUnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: Icon!) -> Unmanaged<HIShape>! ``` | OS X 10.10 |
| To | ``` func IconRefToHIShape(_ iconRect: UnsafePointer<CGRect>, _ align: IconAlignmentType, _ iconServicesUsageFlags: IconServicesUsageFlags, _ theIconRef: IconRef) -> Unmanaged<HIShape>! ``` | OS X 10.5 |

Modified IconRefToIconFamily(IconRef, IconSelectorValue, UnsafeMutablePointer<IconFamilyHandle>) -> OSErr

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IconRefToIconFamily(_ theIconRef: Icon!, _ whichIcons: IconSelectorValue, _ iconFamily: UnsafePointer<IconFamilyHandle>) -> OSErr ``` | OS X 10.10 |
| To | ``` func IconRefToIconFamily(_ theIconRef: IconRef, _ whichIcons: IconSelectorValue, _ iconFamily: UnsafeMutablePointer<IconFamilyHandle>) -> OSErr ``` | OS X 10.10.3 |

Modified InvokeCMBitmapCallBackUPP(Int32, UnsafeMutablePointer<Void>, CMBitmapCallBackUPP) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func InvokeCMBitmapCallBackUPP(_ progress: Int32, _ refCon: UnsafePointer<()>, _ userUPP: CMBitmapCallBackUPP) -> Boolean ``` |
| To | ``` func InvokeCMBitmapCallBackUPP(_ progress: Int32, _ refCon: UnsafeMutablePointer<Void>, _ userUPP: CMBitmapCallBackUPP) -> Boolean ``` |

Modified InvokeCMConcatCallBackUPP(Int32, UnsafeMutablePointer<Void>, CMConcatCallBackUPP) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func InvokeCMConcatCallBackUPP(_ progress: Int32, _ refCon: UnsafePointer<()>, _ userUPP: CMConcatCallBackUPP) -> Boolean ``` |
| To | ``` func InvokeCMConcatCallBackUPP(_ progress: Int32, _ refCon: UnsafeMutablePointer<Void>, _ userUPP: CMConcatCallBackUPP) -> Boolean ``` |

Modified InvokeCMFlattenUPP(Int32, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, CMFlattenUPP) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func InvokeCMFlattenUPP(_ command: Int32, _ size: UnsafePointer<Int>, _ data: UnsafePointer<()>, _ refCon: UnsafePointer<()>, _ userUPP: CMFlattenUPP) -> OSErr ``` |
| To | ``` func InvokeCMFlattenUPP(_ command: Int32, _ size: UnsafeMutablePointer<Int>, _ data: UnsafeMutablePointer<Void>, _ refCon: UnsafeMutablePointer<Void>, _ userUPP: CMFlattenUPP) -> OSErr ``` |

Modified InvokeCMMIterateUPP(UnsafeMutablePointer<CMMInfo>, UnsafeMutablePointer<Void>, CMMIterateUPP) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func InvokeCMMIterateUPP(_ iterateData: UnsafePointer<CMMInfo>, _ refCon: UnsafePointer<()>, _ userUPP: CMMIterateUPP) -> OSErr ``` |
| To | ``` func InvokeCMMIterateUPP(_ iterateData: UnsafeMutablePointer<CMMInfo>, _ refCon: UnsafeMutablePointer<Void>, _ userUPP: CMMIterateUPP) -> OSErr ``` |

Modified InvokeCMProfileIterateUPP(UnsafeMutablePointer<CMProfileIterateData>, UnsafeMutablePointer<Void>, CMProfileIterateUPP) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func InvokeCMProfileIterateUPP(_ iterateData: UnsafePointer<CMProfileIterateData>, _ refCon: UnsafePointer<()>, _ userUPP: CMProfileIterateUPP) -> OSErr ``` |
| To | ``` func InvokeCMProfileIterateUPP(_ iterateData: UnsafeMutablePointer<CMProfileIterateData>, _ refCon: UnsafeMutablePointer<Void>, _ userUPP: CMProfileIterateUPP) -> OSErr ``` |

Modified InvokeIconActionUPP(ResType, UnsafeMutablePointer<Handle>, UnsafeMutablePointer<Void>, IconActionUPP) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func InvokeIconActionUPP(_ theType: ResType, _ theIcon: UnsafePointer<Handle>, _ yourDataPtr: UnsafePointer<()>, _ userUPP: IconActionUPP) -> OSErr ``` |
| To | ``` func InvokeIconActionUPP(_ theType: ResType, _ theIcon: UnsafeMutablePointer<Handle>, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: IconActionUPP) -> OSErr ``` |

Modified InvokeIconGetterUPP(ResType, UnsafeMutablePointer<Void>, IconGetterUPP) -> Handle

|  | Declaration |
| --- | --- |
| From | ``` func InvokeIconGetterUPP(_ theType: ResType, _ yourDataPtr: UnsafePointer<()>, _ userUPP: IconGetterUPP) -> Handle ``` |
| To | ``` func InvokeIconGetterUPP(_ theType: ResType, _ yourDataPtr: UnsafeMutablePointer<Void>, _ userUPP: IconGetterUPP) -> Handle ``` |

Modified IsIconRefMaskEmpty(IconRef) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func IsIconRefMaskEmpty(_ iconRef: Icon!) -> Boolean ``` | OS X 10.10 |
| To | ``` func IsIconRefMaskEmpty(_ iconRef: IconRef) -> Boolean ``` | OS X 10.10.3 |

Modified LAContextRef

|  | Declaration |
| --- | --- |
| From | ``` typealias LAContextRef = LAContext ``` |
| To | ``` typealias LAContextRef = COpaquePointer ``` |

Modified LAEnvironmentRef

|  | Declaration |
| --- | --- |
| From | ``` typealias LAEnvironmentRef = LAEnvironment ``` |
| To | ``` typealias LAEnvironmentRef = COpaquePointer ``` |

Modified LAMorphemesArrayPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias LAMorphemesArrayPtr = UnsafePointer<LAMorphemesArray> ``` |
| To | ``` typealias LAMorphemesArrayPtr = UnsafeMutablePointer<LAMorphemesArray> ``` |

Modified LaunchPBPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias LaunchPBPtr = UnsafePointer<LaunchParamBlockRec> ``` |
| To | ``` typealias LaunchPBPtr = UnsafeMutablePointer<LaunchParamBlockRec> ``` |

Modified MakeVoiceSpec(OSType, OSType, UnsafeMutablePointer<VoiceSpec>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func MakeVoiceSpec(_ creator: OSType, _ id: OSType, _ voice: UnsafePointer<VoiceSpec>) -> OSErr ``` |
| To | ``` func MakeVoiceSpec(_ creator: OSType, _ id: OSType, _ voice: UnsafeMutablePointer<VoiceSpec>) -> OSErr ``` |

Modified NewSpeechChannel(UnsafeMutablePointer<VoiceSpec>, UnsafeMutablePointer<SpeechChannel>) -> OSErr

|  | Declaration |
| --- | --- |
| From | ``` func NewSpeechChannel(_ voice: UnsafePointer<VoiceSpec>, _ chan: UnsafePointer<SpeechChannel>) -> OSErr ``` |
| To | ``` func NewSpeechChannel(_ voice: UnsafeMutablePointer<VoiceSpec>, _ chan: UnsafeMutablePointer<SpeechChannel>) -> OSErr ``` |

Modified PMCGImageCreateWithEPSDataProvider(CGDataProvider!, CGImage!) -> Unmanaged<CGImage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified PMCopyAvailablePPDs(PMPPDDomain, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMCopyAvailablePPDs(_ domain: PMPPDDomain, _ ppds: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMCopyAvailablePPDs(_ domain: PMPPDDomain, _ ppds: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMCopyLocalizedPPD(CFURL!, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMCopyLocalizedPPD(_ ppd: CFURL!, _ localizedPPD: UnsafePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMCopyLocalizedPPD(_ ppd: CFURL!, _ localizedPPD: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMCopyPPDData(CFURL!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMCopyPPDData(_ ppd: CFURL!, _ data: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMCopyPPDData(_ ppd: CFURL!, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMCreateGenericPrinter(UnsafeMutablePointer<PMPrinter>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMCreateGenericPrinter(_ printer: UnsafePointer<PMPrinter>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMCreateGenericPrinter(_ printer: UnsafeMutablePointer<PMPrinter>) -> OSStatus ``` | OS X 10.5 |

Modified PMCreatePageFormat(UnsafeMutablePointer<PMPageFormat>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMCreatePageFormat(_ pageFormat: UnsafePointer<PMPageFormat>) -> OSStatus ``` |
| To | ``` func PMCreatePageFormat(_ pageFormat: UnsafeMutablePointer<PMPageFormat>) -> OSStatus ``` |

Modified PMCreatePageFormatWithPMPaper(UnsafeMutablePointer<PMPageFormat>, PMPaper) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMCreatePageFormatWithPMPaper(_ pageFormat: UnsafePointer<PMPageFormat>, _ paper: PMPaper) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMCreatePageFormatWithPMPaper(_ pageFormat: UnsafeMutablePointer<PMPageFormat>, _ paper: PMPaper) -> OSStatus ``` | OS X 10.3 |

Modified PMCreatePrintSettings(UnsafeMutablePointer<PMPrintSettings>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMCreatePrintSettings(_ printSettings: UnsafePointer<PMPrintSettings>) -> OSStatus ``` |
| To | ``` func PMCreatePrintSettings(_ printSettings: UnsafeMutablePointer<PMPrintSettings>) -> OSStatus ``` |

Modified PMCreateSession(UnsafeMutablePointer<PMPrintSession>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMCreateSession(_ printSession: UnsafePointer<PMPrintSession>) -> OSStatus ``` |
| To | ``` func PMCreateSession(_ printSession: UnsafeMutablePointer<PMPrintSession>) -> OSStatus ``` |

Modified PMGetAdjustedPageRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetAdjustedPageRect(_ pageFormat: PMPageFormat, _ pageRect: UnsafePointer<PMRect>) -> OSStatus ``` |
| To | ``` func PMGetAdjustedPageRect(_ pageFormat: PMPageFormat, _ pageRect: UnsafeMutablePointer<PMRect>) -> OSStatus ``` |

Modified PMGetAdjustedPaperRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetAdjustedPaperRect(_ pageFormat: PMPageFormat, _ paperRect: UnsafePointer<PMRect>) -> OSStatus ``` |
| To | ``` func PMGetAdjustedPaperRect(_ pageFormat: PMPageFormat, _ paperRect: UnsafeMutablePointer<PMRect>) -> OSStatus ``` |

Modified PMGetCollate(PMPrintSettings, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMGetCollate(_ printSettings: PMPrintSettings, _ collate: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMGetCollate(_ printSettings: PMPrintSettings, _ collate: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.2 |

Modified PMGetCopies(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetCopies(_ printSettings: PMPrintSettings, _ copies: UnsafePointer<UInt32>) -> OSStatus ``` |
| To | ``` func PMGetCopies(_ printSettings: PMPrintSettings, _ copies: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified PMGetDuplex(PMPrintSettings, UnsafeMutablePointer<PMDuplexMode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMGetDuplex(_ printSettings: PMPrintSettings, _ duplexSetting: UnsafePointer<PMDuplexMode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMGetDuplex(_ printSettings: PMPrintSettings, _ duplexSetting: UnsafeMutablePointer<PMDuplexMode>) -> OSStatus ``` | OS X 10.4 |

Modified PMGetFirstPage(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetFirstPage(_ printSettings: PMPrintSettings, _ first: UnsafePointer<UInt32>) -> OSStatus ``` |
| To | ``` func PMGetFirstPage(_ printSettings: PMPrintSettings, _ first: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified PMGetLastPage(PMPrintSettings, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetLastPage(_ printSettings: PMPrintSettings, _ last: UnsafePointer<UInt32>) -> OSStatus ``` |
| To | ``` func PMGetLastPage(_ printSettings: PMPrintSettings, _ last: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified PMGetOrientation(PMPageFormat, UnsafeMutablePointer<PMOrientation>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetOrientation(_ pageFormat: PMPageFormat, _ orientation: UnsafePointer<PMOrientation>) -> OSStatus ``` |
| To | ``` func PMGetOrientation(_ pageFormat: PMPageFormat, _ orientation: UnsafeMutablePointer<PMOrientation>) -> OSStatus ``` |

Modified PMGetPageFormatExtendedData(PMPageFormat, OSType, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UnsafePointer<UInt32>, _ extendedData: UnsafePointer<()>) -> OSStatus ``` |
| To | ``` func PMGetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UnsafeMutablePointer<UInt32>, _ extendedData: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified PMGetPageFormatPaper(PMPageFormat, UnsafeMutablePointer<PMPaper>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMGetPageFormatPaper(_ format: PMPageFormat, _ paper: UnsafePointer<PMPaper>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMGetPageFormatPaper(_ format: PMPageFormat, _ paper: UnsafeMutablePointer<PMPaper>) -> OSStatus ``` | OS X 10.3 |

Modified PMGetPageRange(PMPrintSettings, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetPageRange(_ printSettings: PMPrintSettings, _ minPage: UnsafePointer<UInt32>, _ maxPage: UnsafePointer<UInt32>) -> OSStatus ``` |
| To | ``` func PMGetPageRange(_ printSettings: PMPrintSettings, _ minPage: UnsafeMutablePointer<UInt32>, _ maxPage: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified PMGetScale(PMPageFormat, UnsafeMutablePointer<Double>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetScale(_ pageFormat: PMPageFormat, _ scale: UnsafePointer<Double>) -> OSStatus ``` |
| To | ``` func PMGetScale(_ pageFormat: PMPageFormat, _ scale: UnsafeMutablePointer<Double>) -> OSStatus ``` |

Modified PMGetUnadjustedPageRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetUnadjustedPageRect(_ pageFormat: PMPageFormat, _ pageRect: UnsafePointer<PMRect>) -> OSStatus ``` |
| To | ``` func PMGetUnadjustedPageRect(_ pageFormat: PMPageFormat, _ pageRect: UnsafeMutablePointer<PMRect>) -> OSStatus ``` |

Modified PMGetUnadjustedPaperRect(PMPageFormat, UnsafeMutablePointer<PMRect>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMGetUnadjustedPaperRect(_ pageFormat: PMPageFormat, _ paperRect: UnsafePointer<PMRect>) -> OSStatus ``` |
| To | ``` func PMGetUnadjustedPaperRect(_ pageFormat: PMPageFormat, _ paperRect: UnsafeMutablePointer<PMRect>) -> OSStatus ``` |

Modified PMObject

|  | Declaration |
| --- | --- |
| From | ``` typealias PMObject = ConstUnsafePointer<()> ``` |
| To | ``` typealias PMObject = UnsafePointer<Void> ``` |

Modified PMPageFormatCreateDataRepresentation(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPageFormatCreateDataRepresentation(_ pageFormat: PMPageFormat, _ data: UnsafePointer<Unmanaged<CFData>?>, _ format: PMDataFormat) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPageFormatCreateDataRepresentation(_ pageFormat: PMPageFormat, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>, _ format: PMDataFormat) -> OSStatus ``` | OS X 10.5 |

Modified PMPageFormatCreateWithDataRepresentation(CFData!, UnsafeMutablePointer<PMPageFormat>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPageFormatCreateWithDataRepresentation(_ data: CFData!, _ pageFormat: UnsafePointer<PMPageFormat>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPageFormatCreateWithDataRepresentation(_ data: CFData!, _ pageFormat: UnsafeMutablePointer<PMPageFormat>) -> OSStatus ``` | OS X 10.5 |

Modified PMPageFormatGetPrinterID(PMPageFormat, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPageFormatGetPrinterID(_ pageFormat: PMPageFormat, _ printerID: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPageFormatGetPrinterID(_ pageFormat: PMPageFormat, _ printerID: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.5 |

Modified PMPaperCreateCustom(PMPrinter, CFString!, CFString!, Double, Double, UnsafePointer<PMPaperMargins>, UnsafeMutablePointer<PMPaper>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPaperCreateCustom(_ printer: PMPrinter, _ id: CFString!, _ name: CFString!, _ width: Double, _ height: Double, _ margins: ConstUnsafePointer<PMPaperMargins>, _ paperP: UnsafePointer<PMPaper>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPaperCreateCustom(_ printer: PMPrinter, _ id: CFString!, _ name: CFString!, _ width: Double, _ height: Double, _ margins: UnsafePointer<PMPaperMargins>, _ paperP: UnsafeMutablePointer<PMPaper>) -> OSStatus ``` | OS X 10.5 |

Modified PMPaperCreateLocalizedName(PMPaper, PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPaperCreateLocalizedName(_ paper: PMPaper, _ printer: PMPrinter, _ paperName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPaperCreateLocalizedName(_ paper: PMPaper, _ printer: PMPrinter, _ paperName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.5 |

Modified PMPaperGetHeight(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPaperGetHeight(_ paper: PMPaper, _ paperHeight: UnsafePointer<Double>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPaperGetHeight(_ paper: PMPaper, _ paperHeight: UnsafeMutablePointer<Double>) -> OSStatus ``` | OS X 10.3 |

Modified PMPaperGetID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPaperGetID(_ paper: PMPaper, _ paperID: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPaperGetID(_ paper: PMPaper, _ paperID: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMPaperGetMargins(PMPaper, UnsafeMutablePointer<PMPaperMargins>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPaperGetMargins(_ paper: PMPaper, _ paperMargins: UnsafePointer<PMPaperMargins>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPaperGetMargins(_ paper: PMPaper, _ paperMargins: UnsafeMutablePointer<PMPaperMargins>) -> OSStatus ``` | OS X 10.3 |

Modified PMPaperGetPPDPaperName(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPaperGetPPDPaperName(_ paper: PMPaper, _ paperName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPaperGetPPDPaperName(_ paper: PMPaper, _ paperName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.5 |

Modified PMPaperGetPrinterID(PMPaper, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPaperGetPrinterID(_ paper: PMPaper, _ printerID: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPaperGetPrinterID(_ paper: PMPaper, _ printerID: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.5 |

Modified PMPaperGetWidth(PMPaper, UnsafeMutablePointer<Double>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPaperGetWidth(_ paper: PMPaper, _ paperWidth: UnsafePointer<Double>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPaperGetWidth(_ paper: PMPaper, _ paperWidth: UnsafeMutablePointer<Double>) -> OSStatus ``` | OS X 10.3 |

Modified PMPaperIsCustom(PMPaper) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified PMPresetCopyName(PMPreset, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPresetCopyName(_ preset: PMPreset, _ name: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPresetCopyName(_ preset: PMPreset, _ name: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMPresetCreatePrintSettings(PMPreset, PMPrintSession, UnsafeMutablePointer<PMPrintSettings>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPresetCreatePrintSettings(_ preset: PMPreset, _ session: PMPrintSession, _ printSettings: UnsafePointer<PMPrintSettings>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPresetCreatePrintSettings(_ preset: PMPreset, _ session: PMPrintSession, _ printSettings: UnsafeMutablePointer<PMPrintSettings>) -> OSStatus ``` | OS X 10.3 |

Modified PMPresetGetAttributes(PMPreset, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPresetGetAttributes(_ preset: PMPreset, _ attributes: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPresetGetAttributes(_ preset: PMPreset, _ attributes: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMPrintSettingsCopyAsDictionary(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrintSettingsCopyAsDictionary(_ printSettings: PMPrintSettings, _ settingsDictionary: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrintSettingsCopyAsDictionary(_ printSettings: PMPrintSettings, _ settingsDictionary: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.5 |

Modified PMPrintSettingsCopyKeys(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrintSettingsCopyKeys(_ printSettings: PMPrintSettings, _ settingsKeys: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrintSettingsCopyKeys(_ printSettings: PMPrintSettings, _ settingsKeys: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified PMPrintSettingsCreateDataRepresentation(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFData>?>, PMDataFormat) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrintSettingsCreateDataRepresentation(_ printSettings: PMPrintSettings, _ data: UnsafePointer<Unmanaged<CFData>?>, _ format: PMDataFormat) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrintSettingsCreateDataRepresentation(_ printSettings: PMPrintSettings, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>, _ format: PMDataFormat) -> OSStatus ``` | OS X 10.5 |

Modified PMPrintSettingsCreateWithDataRepresentation(CFData!, UnsafeMutablePointer<PMPrintSettings>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrintSettingsCreateWithDataRepresentation(_ data: CFData!, _ printSettings: UnsafePointer<PMPrintSettings>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrintSettingsCreateWithDataRepresentation(_ data: CFData!, _ printSettings: UnsafeMutablePointer<PMPrintSettings>) -> OSStatus ``` | OS X 10.5 |

Modified PMPrintSettingsGetJobName(PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrintSettingsGetJobName(_ printSettings: PMPrintSettings, _ name: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrintSettingsGetJobName(_ printSettings: PMPrintSettings, _ name: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.4 |

Modified PMPrintSettingsGetValue(PMPrintSettings, CFString!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrintSettingsGetValue(_ printSettings: PMPrintSettings, _ key: CFString!, _ value: UnsafePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrintSettingsGetValue(_ printSettings: PMPrintSettings, _ key: CFString!, _ value: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` | OS X 10.4 |

Modified PMPrintSettingsSetJobName(PMPrintSettings, CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified PMPrintSettingsSetValue(PMPrintSettings, CFString!, AnyObject!, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified PMPrintSettingsToOptions(PMPrintSettings, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrintSettingsToOptions(_ settings: PMPrintSettings, _ options: UnsafePointer<UnsafePointer<Int8>>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrintSettingsToOptions(_ settings: PMPrintSettings, _ options: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` | OS X 10.3 |

Modified PMPrintSettingsToOptionsWithPrinterAndPageFormat(PMPrintSettings, PMPrinter, PMPageFormat, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrintSettingsToOptionsWithPrinterAndPageFormat(_ settings: PMPrintSettings, _ printer: PMPrinter, _ pageFormat: PMPageFormat, _ options: UnsafePointer<UnsafePointer<Int8>>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrintSettingsToOptionsWithPrinterAndPageFormat(_ settings: PMPrintSettings, _ printer: PMPrinter, _ pageFormat: PMPageFormat, _ options: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` | OS X 10.5 |

Modified PMPrinterCopyDescriptionURL(PMPrinter, CFString!, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterCopyDescriptionURL(_ printer: PMPrinter, _ descriptionType: CFString!, _ fileURL: UnsafePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterCopyDescriptionURL(_ printer: PMPrinter, _ descriptionType: CFString!, _ fileURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.4 |

Modified PMPrinterCopyDeviceURI(PMPrinter, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterCopyDeviceURI(_ printer: PMPrinter, _ deviceURI: UnsafePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterCopyDeviceURI(_ printer: PMPrinter, _ deviceURI: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.4 |

Modified PMPrinterCopyHostName(PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterCopyHostName(_ printer: PMPrinter, _ hostNameP: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterCopyHostName(_ printer: PMPrinter, _ hostNameP: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMPrinterCopyPresets(PMPrinter, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterCopyPresets(_ printer: PMPrinter, _ presetList: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterCopyPresets(_ printer: PMPrinter, _ presetList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMPrinterCopyState(PMPrinter, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterCopyState(_ printer: PMPrinter, _ stateDict: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterCopyState(_ printer: PMPrinter, _ stateDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.6 |

Modified PMPrinterCreateFromPrinterID(CFString!) -> PMPrinter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified PMPrinterGetCommInfo(PMPrinter, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterGetCommInfo(_ printer: PMPrinter, _ supportsControlCharRangeP: UnsafePointer<Boolean>, _ supportsEightBitP: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterGetCommInfo(_ printer: PMPrinter, _ supportsControlCharRangeP: UnsafeMutablePointer<Boolean>, _ supportsEightBitP: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified PMPrinterGetDriverCreator(PMPrinter, UnsafeMutablePointer<OSType>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetDriverCreator(_ printer: PMPrinter, _ creator: UnsafePointer<OSType>) -> OSStatus ``` |
| To | ``` func PMPrinterGetDriverCreator(_ printer: PMPrinter, _ creator: UnsafeMutablePointer<OSType>) -> OSStatus ``` |

Modified PMPrinterGetDriverReleaseInfo(PMPrinter, UnsafeMutablePointer<VersRec>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetDriverReleaseInfo(_ printer: PMPrinter, _ release: UnsafePointer<VersRec>) -> OSStatus ``` |
| To | ``` func PMPrinterGetDriverReleaseInfo(_ printer: PMPrinter, _ release: UnsafeMutablePointer<VersRec>) -> OSStatus ``` |

Modified PMPrinterGetID(PMPrinter) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified PMPrinterGetIndexedPrinterResolution(PMPrinter, UInt32, UnsafeMutablePointer<PMResolution>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetIndexedPrinterResolution(_ printer: PMPrinter, _ index: UInt32, _ resolutionP: UnsafePointer<PMResolution>) -> OSStatus ``` |
| To | ``` func PMPrinterGetIndexedPrinterResolution(_ printer: PMPrinter, _ index: UInt32, _ resolutionP: UnsafeMutablePointer<PMResolution>) -> OSStatus ``` |

Modified PMPrinterGetLanguageInfo(PMPrinter, UnsafeMutablePointer<PMLanguageInfo>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetLanguageInfo(_ printer: PMPrinter, _ info: UnsafePointer<PMLanguageInfo>) -> OSStatus ``` |
| To | ``` func PMPrinterGetLanguageInfo(_ printer: PMPrinter, _ info: UnsafeMutablePointer<PMLanguageInfo>) -> OSStatus ``` |

Modified PMPrinterGetLocation(PMPrinter) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified PMPrinterGetMakeAndModelName(PMPrinter, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterGetMakeAndModelName(_ printer: PMPrinter, _ makeAndModel: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterGetMakeAndModelName(_ printer: PMPrinter, _ makeAndModel: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.2 |

Modified PMPrinterGetMimeTypes(PMPrinter, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterGetMimeTypes(_ printer: PMPrinter, _ settings: PMPrintSettings, _ mimeTypes: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterGetMimeTypes(_ printer: PMPrinter, _ settings: PMPrintSettings, _ mimeTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMPrinterGetName(PMPrinter) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified PMPrinterGetOutputResolution(PMPrinter, PMPrintSettings, UnsafeMutablePointer<PMResolution>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterGetOutputResolution(_ printer: PMPrinter, _ printSettings: PMPrintSettings, _ resolutionP: UnsafePointer<PMResolution>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterGetOutputResolution(_ printer: PMPrinter, _ printSettings: PMPrintSettings, _ resolutionP: UnsafeMutablePointer<PMResolution>) -> OSStatus ``` | OS X 10.5 |

Modified PMPrinterGetPaperList(PMPrinter, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterGetPaperList(_ printer: PMPrinter, _ paperList: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterGetPaperList(_ printer: PMPrinter, _ paperList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMPrinterGetPrinterResolutionCount(PMPrinter, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMPrinterGetPrinterResolutionCount(_ printer: PMPrinter, _ countP: UnsafePointer<UInt32>) -> OSStatus ``` |
| To | ``` func PMPrinterGetPrinterResolutionCount(_ printer: PMPrinter, _ countP: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified PMPrinterGetState(PMPrinter, UnsafeMutablePointer<PMPrinterState>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterGetState(_ printer: PMPrinter, _ state: UnsafePointer<PMPrinterState>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterGetState(_ printer: PMPrinter, _ state: UnsafeMutablePointer<PMPrinterState>) -> OSStatus ``` | OS X 10.2 |

Modified PMPrinterIsDefault(PMPrinter) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified PMPrinterIsFavorite(PMPrinter) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified PMPrinterIsPostScriptCapable(PMPrinter) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified PMPrinterIsPostScriptPrinter(PMPrinter, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterIsPostScriptPrinter(_ printer: PMPrinter, _ isPSPrinter: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterIsPostScriptPrinter(_ printer: PMPrinter, _ isPSPrinter: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.5 |

Modified PMPrinterIsRemote(PMPrinter, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterIsRemote(_ printer: PMPrinter, _ isRemoteP: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterIsRemote(_ printer: PMPrinter, _ isRemoteP: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified PMPrinterPrintWithFile(PMPrinter, PMPrintSettings, PMPageFormat, CFString!, CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PMPrinterPrintWithProvider(PMPrinter, PMPrintSettings, PMPageFormat, CFString!, CGDataProvider!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PMPrinterSendCommand(PMPrinter, CFString!, CFString!, CFDictionary!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified PMPrinterSetDefault(PMPrinter) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified PMPrinterSetOutputResolution(PMPrinter, PMPrintSettings, UnsafePointer<PMResolution>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMPrinterSetOutputResolution(_ printer: PMPrinter, _ printSettings: PMPrintSettings, _ resolutionP: ConstUnsafePointer<PMResolution>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMPrinterSetOutputResolution(_ printer: PMPrinter, _ printSettings: PMPrintSettings, _ resolutionP: UnsafePointer<PMResolution>) -> OSStatus ``` | OS X 10.5 |

Modified PMPrinterWritePostScriptToURL(PMPrinter, PMPrintSettings, PMPageFormat, CFString!, CFURL!, CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified PMServerCreatePrinterList(PMServer, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMServerCreatePrinterList(_ server: PMServer, _ printerList: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMServerCreatePrinterList(_ server: PMServer, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.2 |

Modified PMServerLaunchPrinterBrowser(PMServer, CFDictionary!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified PMSessionBeginCGDocumentNoDialog(PMPrintSession, PMPrintSettings, PMPageFormat) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified PMSessionBeginPageNoDialog(PMPrintSession, PMPageFormat, UnsafePointer<PMRect>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionBeginPageNoDialog(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ pageFrame: ConstUnsafePointer<PMRect>) -> OSStatus ``` |
| To | ``` func PMSessionBeginPageNoDialog(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ pageFrame: UnsafePointer<PMRect>) -> OSStatus ``` |

Modified PMSessionCopyDestinationFormat(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMSessionCopyDestinationFormat(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destFormatP: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMSessionCopyDestinationFormat(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destFormatP: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.1 |

Modified PMSessionCopyDestinationLocation(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMSessionCopyDestinationLocation(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destLocationP: UnsafePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMSessionCopyDestinationLocation(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destLocationP: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.1 |

Modified PMSessionCopyOutputFormatList(PMPrintSession, PMDestinationType, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMSessionCopyOutputFormatList(_ printSession: PMPrintSession, _ destType: PMDestinationType, _ documentFormatP: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMSessionCopyOutputFormatList(_ printSession: PMPrintSession, _ destType: PMDestinationType, _ documentFormatP: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.1 |

Modified PMSessionCreatePageFormatList(PMPrintSession, PMPrinter, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMSessionCreatePageFormatList(_ printSession: PMPrintSession, _ printer: PMPrinter, _ pageFormatList: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMSessionCreatePageFormatList(_ printSession: PMPrintSession, _ printer: PMPrinter, _ pageFormatList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.1 |

Modified PMSessionCreatePrinterList(PMPrintSession, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<CFIndex>, UnsafeMutablePointer<PMPrinter>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMSessionCreatePrinterList(_ printSession: PMPrintSession, _ printerList: UnsafePointer<Unmanaged<CFArray>?>, _ currentIndex: UnsafePointer<CFIndex>, _ currentPrinter: UnsafePointer<PMPrinter>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMSessionCreatePrinterList(_ printSession: PMPrintSession, _ printerList: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ currentIndex: UnsafeMutablePointer<CFIndex>, _ currentPrinter: UnsafeMutablePointer<PMPrinter>) -> OSStatus ``` | OS X 10.1 |

Modified PMSessionGetCGGraphicsContext(PMPrintSession, UnsafeMutablePointer<Unmanaged<CGContext>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMSessionGetCGGraphicsContext(_ printSession: PMPrintSession, _ context: UnsafePointer<Unmanaged<CGContext>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMSessionGetCGGraphicsContext(_ printSession: PMPrintSession, _ context: UnsafeMutablePointer<Unmanaged<CGContext>?>) -> OSStatus ``` | OS X 10.4 |

Modified PMSessionGetCurrentPrinter(PMPrintSession, UnsafeMutablePointer<PMPrinter>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionGetCurrentPrinter(_ printSession: PMPrintSession, _ currentPrinter: UnsafePointer<PMPrinter>) -> OSStatus ``` |
| To | ``` func PMSessionGetCurrentPrinter(_ printSession: PMPrintSession, _ currentPrinter: UnsafeMutablePointer<PMPrinter>) -> OSStatus ``` |

Modified PMSessionGetDataFromSession(PMPrintSession, CFString!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionGetDataFromSession(_ printSession: PMPrintSession, _ key: CFString!, _ data: UnsafePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func PMSessionGetDataFromSession(_ printSession: PMPrintSession, _ key: CFString!, _ data: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |

Modified PMSessionGetDestinationType(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<PMDestinationType>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMSessionGetDestinationType(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destTypeP: UnsafePointer<PMDestinationType>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMSessionGetDestinationType(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ destTypeP: UnsafeMutablePointer<PMDestinationType>) -> OSStatus ``` | OS X 10.1 |

Modified PMSessionSetCurrentPMPrinter(PMPrintSession, PMPrinter) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PMSessionSetDestination(PMPrintSession, PMPrintSettings, PMDestinationType, CFString!, CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified PMSessionValidatePageFormat(PMPrintSession, PMPageFormat, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionValidatePageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ result: UnsafePointer<Boolean>) -> OSStatus ``` |
| To | ``` func PMSessionValidatePageFormat(_ printSession: PMPrintSession, _ pageFormat: PMPageFormat, _ result: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |

Modified PMSessionValidatePrintSettings(PMPrintSession, PMPrintSettings, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMSessionValidatePrintSettings(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ result: UnsafePointer<Boolean>) -> OSStatus ``` |
| To | ``` func PMSessionValidatePrintSettings(_ printSession: PMPrintSession, _ printSettings: PMPrintSettings, _ result: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |

Modified PMSetCollate(PMPrintSettings, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified PMSetDuplex(PMPrintSettings, PMDuplexMode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified PMSetPageFormatExtendedData(PMPageFormat, OSType, UInt32, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func PMSetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UInt32, _ extendedData: UnsafePointer<()>) -> OSStatus ``` |
| To | ``` func PMSetPageFormatExtendedData(_ pageFormat: PMPageFormat, _ dataID: OSType, _ size: UInt32, _ extendedData: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified PMWorkflowCopyItems(UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMWorkflowCopyItems(_ workflowItems: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMWorkflowCopyItems(_ workflowItems: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified PMWorkflowSubmitPDFWithOptions(CFURL!, CFString!, UnsafePointer<Int8>, CFURL!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PMWorkflowSubmitPDFWithOptions(_ workflowItem: CFURL!, _ title: CFString!, _ options: ConstUnsafePointer<Int8>, _ pdfFile: CFURL!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PMWorkflowSubmitPDFWithOptions(_ workflowItem: CFURL!, _ title: CFString!, _ options: UnsafePointer<Int8>, _ pdfFile: CFURL!) -> OSStatus ``` | OS X 10.3 |

Modified PMWorkflowSubmitPDFWithSettings(CFURL!, PMPrintSettings, CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PasteboardClear(Pasteboard!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PasteboardCopyItemFlavorData(Pasteboard!, PasteboardItemID, CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardCopyItemFlavorData(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ inFlavorType: CFString!, _ outData: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardCopyItemFlavorData(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ inFlavorType: CFString!, _ outData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.3 |

Modified PasteboardCopyItemFlavors(Pasteboard!, PasteboardItemID, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardCopyItemFlavors(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ outFlavorTypes: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardCopyItemFlavors(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ outFlavorTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified PasteboardCopyName(Pasteboard!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardCopyName(_ inPasteboard: Pasteboard!, _ outName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardCopyName(_ inPasteboard: Pasteboard!, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.4 |

Modified PasteboardCopyPasteLocation(Pasteboard!, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardCopyPasteLocation(_ inPasteboard: Pasteboard!, _ outPasteLocation: UnsafePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardCopyPasteLocation(_ inPasteboard: Pasteboard!, _ outPasteLocation: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.3 |

Modified PasteboardCreate(CFString!, UnsafeMutablePointer<Unmanaged<Pasteboard>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardCreate(_ inName: CFString!, _ outPasteboard: UnsafePointer<Unmanaged<Pasteboard>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardCreate(_ inName: CFString!, _ outPasteboard: UnsafeMutablePointer<Unmanaged<Pasteboard>?>) -> OSStatus ``` | OS X 10.3 |

Modified PasteboardGetItemCount(Pasteboard!, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardGetItemCount(_ inPasteboard: Pasteboard!, _ outItemCount: UnsafePointer<ItemCount>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardGetItemCount(_ inPasteboard: Pasteboard!, _ outItemCount: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.3 |

Modified PasteboardGetItemFlavorFlags(Pasteboard!, PasteboardItemID, CFString!, UnsafeMutablePointer<PasteboardFlavorFlags>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardGetItemFlavorFlags(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ inFlavorType: CFString!, _ outFlags: UnsafePointer<PasteboardFlavorFlags>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardGetItemFlavorFlags(_ inPasteboard: Pasteboard!, _ inItem: PasteboardItemID, _ inFlavorType: CFString!, _ outFlags: UnsafeMutablePointer<PasteboardFlavorFlags>) -> OSStatus ``` | OS X 10.3 |

Modified PasteboardGetItemIdentifier(Pasteboard!, CFIndex, UnsafeMutablePointer<PasteboardItemID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardGetItemIdentifier(_ inPasteboard: Pasteboard!, _ inIndex: CFIndex, _ outItem: UnsafePointer<PasteboardItemID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardGetItemIdentifier(_ inPasteboard: Pasteboard!, _ inIndex: CFIndex, _ outItem: UnsafeMutablePointer<PasteboardItemID>) -> OSStatus ``` | OS X 10.3 |

Modified PasteboardGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PasteboardItemID

|  | Declaration |
| --- | --- |
| From | ``` typealias PasteboardItemID = UnsafePointer<()> ``` |
| To | ``` typealias PasteboardItemID = UnsafeMutablePointer<Void> ``` |

Modified PasteboardPromiseKeeperProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias PasteboardPromiseKeeperProcPtr = CFunctionPointer<((Pasteboard!, PasteboardItemID, CFString!, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias PasteboardPromiseKeeperProcPtr = CFunctionPointer<((Pasteboard!, PasteboardItemID, CFString!, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified PasteboardPutItemFlavor(Pasteboard!, PasteboardItemID, CFString!, CFData!, PasteboardFlavorFlags) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PasteboardResolvePromises(Pasteboard!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PasteboardSetPasteLocation(Pasteboard!, CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PasteboardSetPromiseKeeper(Pasteboard!, PasteboardPromiseKeeperProcPtr, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PasteboardSetPromiseKeeper(_ inPasteboard: Pasteboard!, _ inPromiseKeeper: PasteboardPromiseKeeperProcPtr, _ inContext: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PasteboardSetPromiseKeeper(_ inPasteboard: Pasteboard!, _ inPromiseKeeper: PasteboardPromiseKeeperProcPtr, _ inContext: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.3 |

Modified PasteboardSynchronize(Pasteboard!) -> PasteboardSyncFlags

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified PatHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias PatHandle = UnsafePointer<PatPtr> ``` |
| To | ``` typealias PatHandle = UnsafeMutablePointer<PatPtr> ``` |

Modified PatPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias PatPtr = UnsafePointer<Pattern> ``` |
| To | ``` typealias PatPtr = UnsafeMutablePointer<Pattern> ``` |

Modified PicHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias PicHandle = UnsafePointer<PicPtr> ``` |
| To | ``` typealias PicHandle = UnsafeMutablePointer<PicPtr> ``` |

Modified PicPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias PicPtr = UnsafePointer<Picture> ``` |
| To | ``` typealias PicPtr = UnsafeMutablePointer<Picture> ``` |

Modified PixMapHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias PixMapHandle = UnsafePointer<PixMapPtr> ``` |
| To | ``` typealias PixMapHandle = UnsafeMutablePointer<PixMapPtr> ``` |

Modified PixMapPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias PixMapPtr = UnsafePointer<PixMap> ``` |
| To | ``` typealias PixMapPtr = UnsafeMutablePointer<PixMap> ``` |

Modified PixPatHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias PixPatHandle = UnsafePointer<PixPatPtr> ``` |
| To | ``` typealias PixPatHandle = UnsafeMutablePointer<PixPatPtr> ``` |

Modified PixPatPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias PixPatPtr = UnsafePointer<PixPat> ``` |
| To | ``` typealias PixPatPtr = UnsafeMutablePointer<PixPat> ``` |

Modified PlotIconRefInContext(CGContext!, UnsafePointer<CGRect>, IconAlignmentType, IconTransformType, UnsafePointer<RGBColor>, PlotIconRefFlags, IconRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PlotIconRefInContext(_ inContext: CGContext!, _ inRect: ConstUnsafePointer<CGRect>, _ inAlign: IconAlignmentType, _ inTransform: IconTransformType, _ inLabelColor: ConstUnsafePointer<RGBColor>, _ inFlags: PlotIconRefFlags, _ inIconRef: Icon!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func PlotIconRefInContext(_ inContext: CGContext!, _ inRect: UnsafePointer<CGRect>, _ inAlign: IconAlignmentType, _ inTransform: IconTransformType, _ inLabelColor: UnsafePointer<RGBColor>, _ inFlags: PlotIconRefFlags, _ inIconRef: IconRef) -> OSStatus ``` | OS X 10.1 |

Modified PolyHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias PolyHandle = UnsafePointer<PolyPtr> ``` |
| To | ``` typealias PolyHandle = UnsafeMutablePointer<PolyPtr> ``` |

Modified PolyPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias PolyPtr = UnsafePointer<MacPolygon> ``` |
| To | ``` typealias PolyPtr = UnsafeMutablePointer<MacPolygon> ``` |

Modified ProcessInfoExtendedRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ProcessInfoExtendedRecPtr = UnsafePointer<ProcessInfoExtendedRec> ``` |
| To | ``` typealias ProcessInfoExtendedRecPtr = UnsafeMutablePointer<ProcessInfoExtendedRec> ``` |

Modified ProcessInfoRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ProcessInfoRecPtr = UnsafePointer<ProcessInfoRec> ``` |
| To | ``` typealias ProcessInfoRecPtr = UnsafeMutablePointer<ProcessInfoRec> ``` |

Modified QDArcProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDArcProcPtr = CFunctionPointer<((GrafVerb, ConstUnsafePointer<Rect>, Int16, Int16) -> Void)> ``` |
| To | ``` typealias QDArcProcPtr = CFunctionPointer<((GrafVerb, UnsafePointer<Rect>, Int16, Int16) -> Void)> ``` |

Modified QDBitsProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDBitsProcPtr = CFunctionPointer<((ConstUnsafePointer<BitMap>, ConstUnsafePointer<Rect>, ConstUnsafePointer<Rect>, Int16, RgnHandle) -> Void)> ``` |
| To | ``` typealias QDBitsProcPtr = CFunctionPointer<((UnsafePointer<BitMap>, UnsafePointer<Rect>, UnsafePointer<Rect>, Int16, RgnHandle) -> Void)> ``` |

Modified QDGetPicProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDGetPicProcPtr = CFunctionPointer<((UnsafePointer<()>, Int16) -> Void)> ``` |
| To | ``` typealias QDGetPicProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>, Int16) -> Void)> ``` |

Modified QDOpcodeProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDOpcodeProcPtr = CFunctionPointer<((ConstUnsafePointer<Rect>, ConstUnsafePointer<Rect>, UInt16, Int16) -> Void)> ``` |
| To | ``` typealias QDOpcodeProcPtr = CFunctionPointer<((UnsafePointer<Rect>, UnsafePointer<Rect>, UInt16, Int16) -> Void)> ``` |

Modified QDOvalProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDOvalProcPtr = CFunctionPointer<((GrafVerb, ConstUnsafePointer<Rect>) -> Void)> ``` |
| To | ``` typealias QDOvalProcPtr = CFunctionPointer<((GrafVerb, UnsafePointer<Rect>) -> Void)> ``` |

Modified QDPrinterStatusProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPrinterStatusProcPtr = CFunctionPointer<((PrinterStatusOpcode, CGrafPtr, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias QDPrinterStatusProcPtr = CFunctionPointer<((PrinterStatusOpcode, CGrafPtr, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified QDPutPicProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDPutPicProcPtr = CFunctionPointer<((ConstUnsafePointer<()>, Int16) -> Void)> ``` |
| To | ``` typealias QDPutPicProcPtr = CFunctionPointer<((UnsafePointer<Void>, Int16) -> Void)> ``` |

Modified QDRRectProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRRectProcPtr = CFunctionPointer<((GrafVerb, ConstUnsafePointer<Rect>, Int16, Int16) -> Void)> ``` |
| To | ``` typealias QDRRectProcPtr = CFunctionPointer<((GrafVerb, UnsafePointer<Rect>, Int16, Int16) -> Void)> ``` |

Modified QDRectProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDRectProcPtr = CFunctionPointer<((GrafVerb, ConstUnsafePointer<Rect>) -> Void)> ``` |
| To | ``` typealias QDRectProcPtr = CFunctionPointer<((GrafVerb, UnsafePointer<Rect>) -> Void)> ``` |

Modified QDStdGlyphsProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDStdGlyphsProcPtr = CFunctionPointer<((UnsafePointer<()>, ByteCount) -> OSStatus)> ``` |
| To | ``` typealias QDStdGlyphsProcPtr = CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> OSStatus)> ``` |

Modified QDTextProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDTextProcPtr = CFunctionPointer<((Int16, ConstUnsafePointer<()>, Point, Point) -> Void)> ``` |
| To | ``` typealias QDTextProcPtr = CFunctionPointer<((Int16, UnsafePointer<Void>, Point, Point) -> Void)> ``` |

Modified QDTxMeasProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QDTxMeasProcPtr = CFunctionPointer<((Int16, ConstUnsafePointer<()>, UnsafePointer<Point>, UnsafePointer<Point>, UnsafePointer<FontInfo>) -> Int16)> ``` |
| To | ``` typealias QDTxMeasProcPtr = CFunctionPointer<((Int16, UnsafePointer<Void>, UnsafeMutablePointer<Point>, UnsafeMutablePointer<Point>, UnsafeMutablePointer<FontInfo>) -> Int16)> ``` |

Modified RedrawBackgroundProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias RedrawBackgroundProcPtr = CFunctionPointer<((ATSUTextLayout, UniCharArrayOffset, UniCharCount, UnsafePointer<ATSTrapezoid>, ItemCount) -> Boolean)> ``` |
| To | ``` typealias RedrawBackgroundProcPtr = CFunctionPointer<((ATSUTextLayout, UniCharArrayOffset, Int, UnsafeMutablePointer<ATSTrapezoid>, Int) -> Boolean)> ``` |

Modified RegionToRectsProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias RegionToRectsProcPtr = CFunctionPointer<((UInt16, RgnHandle, ConstUnsafePointer<Rect>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias RegionToRectsProcPtr = CFunctionPointer<((UInt16, RgnHandle, UnsafePointer<Rect>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified SetSpeechProperty(SpeechChannel, CFString!, AnyObject!) -> OSErr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SizeResourceRecHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias SizeResourceRecHandle = UnsafePointer<SizeResourceRecPtr> ``` |
| To | ``` typealias SizeResourceRecHandle = UnsafeMutablePointer<SizeResourceRecPtr> ``` |

Modified SizeResourceRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias SizeResourceRecPtr = UnsafePointer<SizeResourceRec> ``` |
| To | ``` typealias SizeResourceRecPtr = UnsafeMutablePointer<SizeResourceRec> ``` |

Modified SpeakCFString(SpeechChannel, CFString!, CFDictionary!) -> OSErr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SpeechChannel

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechChannel = UnsafePointer<SpeechChannelRecord> ``` |
| To | ``` typealias SpeechChannel = UnsafeMutablePointer<SpeechChannelRecord> ``` |

Modified SpeechSynthesisRegisterModuleURL(CFURL!) -> OSErr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SpeechSynthesisUnregisterModuleURL(CFURL!) -> OSErr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SpeechTextDoneProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias SpeechTextDoneProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, UnsafePointer<ConstUnsafePointer<()>>, UnsafePointer<UInt>, UnsafePointer<Int32>) -> Void)> ``` |
| To | ``` typealias SpeechTextDoneProcPtr = CFunctionPointer<((SpeechChannel, SRefCon, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<Int32>) -> Void)> ``` |

Modified TransformProcessType(UnsafePointer<ProcessSerialNumber>, ProcessApplicationTransformState) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TransformProcessType(_ psn: ConstUnsafePointer<ProcessSerialNumber>, _ transformState: ProcessApplicationTransformState) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TransformProcessType(_ psn: UnsafePointer<ProcessSerialNumber>, _ transformState: ProcessApplicationTransformState) -> OSStatus ``` | OS X 10.3 |

Modified TranslationCopyDestinationType(Translation!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TranslationCopyDestinationType(_ inTranslation: Translation!, _ outDestinationType: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TranslationCopyDestinationType(_ inTranslation: Translation!, _ outDestinationType: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.3 |

Modified TranslationCopySourceType(Translation!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TranslationCopySourceType(_ inTranslation: Translation!, _ outSourceType: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TranslationCopySourceType(_ inTranslation: Translation!, _ outSourceType: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.3 |

Modified TranslationCreate(CFString!, CFString!, TranslationFlags, UnsafeMutablePointer<Unmanaged<Translation>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TranslationCreate(_ inSourceType: CFString!, _ inDestinationType: CFString!, _ inTranslationFlags: TranslationFlags, _ outTranslation: UnsafePointer<Unmanaged<Translation>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TranslationCreate(_ inSourceType: CFString!, _ inDestinationType: CFString!, _ inTranslationFlags: TranslationFlags, _ outTranslation: UnsafeMutablePointer<Unmanaged<Translation>?>) -> OSStatus ``` | OS X 10.3 |

Modified TranslationCreateWithSourceArray(CFArray!, TranslationFlags, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TranslationCreateWithSourceArray(_ inSourceTypes: CFArray!, _ inTranslationFlags: TranslationFlags, _ outDestinationTypes: UnsafePointer<Unmanaged<CFArray>?>, _ outTranslations: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TranslationCreateWithSourceArray(_ inSourceTypes: CFArray!, _ inTranslationFlags: TranslationFlags, _ outDestinationTypes: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outTranslations: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.3 |

Modified TranslationGetTranslationFlags(Translation!, UnsafeMutablePointer<TranslationFlags>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TranslationGetTranslationFlags(_ inTranslation: Translation!, _ outTranslationFlags: UnsafePointer<TranslationFlags>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TranslationGetTranslationFlags(_ inTranslation: Translation!, _ outTranslationFlags: UnsafeMutablePointer<TranslationFlags>) -> OSStatus ``` | OS X 10.3 |

Modified TranslationGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified TranslationPerformForData(Translation!, CFData!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TranslationPerformForData(_ inTranslation: Translation!, _ inSourceData: CFData!, _ outDestinationData: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TranslationPerformForData(_ inTranslation: Translation!, _ inSourceData: CFData!, _ outDestinationData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.3 |

Modified TranslationPerformForFile(Translation!, UnsafePointer<FSRef>, UnsafePointer<FSRef>, CFString!, UnsafeMutablePointer<FSRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TranslationPerformForFile(_ inTranslation: Translation!, _ inSourceFile: ConstUnsafePointer<FSRef>, _ inDestinationDirectory: ConstUnsafePointer<FSRef>, _ inDestinationName: CFString!, _ outTranslatedFile: UnsafePointer<FSRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TranslationPerformForFile(_ inTranslation: Translation!, _ inSourceFile: UnsafePointer<FSRef>, _ inDestinationDirectory: UnsafePointer<FSRef>, _ inDestinationName: CFString!, _ outTranslatedFile: UnsafeMutablePointer<FSRef>) -> OSStatus ``` | OS X 10.3 |

Modified TranslationPerformForURL(Translation!, CFURL!, CFURL!, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func TranslationPerformForURL(_ inTranslation: Translation!, _ inSourceURL: CFURL!, _ inDestinationURL: CFURL!, _ outTranslatedURL: UnsafePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func TranslationPerformForURL(_ inTranslation: Translation!, _ inSourceURL: CFURL!, _ inDestinationURL: CFURL!, _ outTranslatedURL: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` | OS X 10.3 |

Modified UAZoomChangeFocus(UnsafePointer<CGRect>, UnsafePointer<CGRect>, UAZoomChangeFocusType) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func UAZoomChangeFocus(_ inRect: ConstUnsafePointer<CGRect>, _ inHighlightRect: ConstUnsafePointer<CGRect>, _ inType: UAZoomChangeFocusType) -> OSStatus ``` | OS X 10.10 |
| To | ``` func UAZoomChangeFocus(_ inRect: UnsafePointer<CGRect>, _ inHighlightRect: UnsafePointer<CGRect>, _ inType: UAZoomChangeFocusType) -> OSStatus ``` | OS X 10.4 |

Modified UAZoomEnabled() -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified UseSpeechDictionary(SpeechChannel, CFDictionary!) -> OSErr

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified VDGamRecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias VDGamRecPtr = UnsafePointer<VDGammaRecord> ``` |
| To | ``` typealias VDGamRecPtr = UnsafeMutablePointer<VDGammaRecord> ``` |

Modified VoiceSpecPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias VoiceSpecPtr = UnsafePointer<VoiceSpec> ``` |
| To | ``` typealias VoiceSpecPtr = UnsafeMutablePointer<VoiceSpec> ``` |

Modified WindowRef

|  | Declaration |
| --- | --- |
| From | ``` typealias WindowRef = Window ``` |
| To | ``` typealias WindowRef = WindowPtr ``` |

Modified kAXAttachmentTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXAutocorrectedTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kAXBackgroundColorTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXFontFamilyKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXFontNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXFontSizeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXFontTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXForegoundColorTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXForegroundColorTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXLinkTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXMarkedMisspelledTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kAXMisspelledTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXNaturalLanguageTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXReplacementStringTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXShadowTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXStrikethroughColorTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXStrikethroughTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXSuperscriptTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXTrustedCheckOptionPrompt

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kAXUnderlineColorTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXUnderlineTextAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kAXVisibleNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSpeechAudioGraphProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSpeechAudioOutputFormatProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSpeechAudioUnitProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSpeechCharacterModeProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechCommandDelimiterProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechCommandPrefix

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechCommandSuffix

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechCurrentVoiceProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechDictionaryAbbreviations

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechDictionaryEntryPhonemes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechDictionaryEntrySpelling

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechDictionaryLocaleIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechDictionaryModificationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechDictionaryPronunciations

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorCFCallBack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorCallbackCharacterOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorCallbackSpokenString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorNewest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorNewestCharacterOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorOldest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorOldestCharacterOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechErrorsProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechInputModeProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechModeLiteral

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechModeNormal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechModePhoneme

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechModeText

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechModeTune

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSpeechNoEndingProsody

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechNoSpeechInterrupt

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechNumberModeProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechOutputChannelMapProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSpeechOutputToAudioDeviceProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSpeechOutputToExtAudioFileProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSpeechOutputToFileDescriptorProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSpeechOutputToFileURLProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPhonemeCallBack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPhonemeInfoExample

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPhonemeInfoHiliteEnd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPhonemeInfoHiliteStart

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPhonemeInfoOpcode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPhonemeInfoSymbol

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPhonemeOptionsProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSpeechPhonemeSymbolsProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPitchBaseProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPitchModProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechPreflightThenPause

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechRateProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechRecentSyncProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechRefConProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechResetProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechSpeechDoneCallBack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechStatusNumberOfCharactersLeft

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechStatusOutputBusy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechStatusOutputPaused

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechStatusPhonemeCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechStatusProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechSyncCallBack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechSynthExtensionProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSpeechSynthesizerInfoIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechSynthesizerInfoManufacturer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechSynthesizerInfoProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechSynthesizerInfoVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechTextDoneCallBack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechVoiceCreator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechVoiceID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechVolumeProperty

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSpeechWordCFCallBack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

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
