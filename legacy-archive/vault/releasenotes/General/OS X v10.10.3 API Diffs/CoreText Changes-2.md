---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreText.html
archived_at: '2026-07-18T02:52:16.690305Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreText Changes

## CoreText

Removed CTFontOptions.valueRemoved CTFontStylisticClass.valueRemoved CTFontSymbolicTraits.valueRemoved CTFontTableOptions.ExcludeSyntheticRemoved CTFontTableOptions.valueRemoved CTLineBoundsOptions.valueRemoved CTRunStatus.valueRemoved CTUnderlineStyle.valueRemoved CTUnderlineStyleModifiers.valueAdded ALMXGlyphEntry.init()Added ALMXGlyphEntry.init(GlyphIndexOffset: Int16, HorizontalAdvance: Int16, XOffsetToHOrigin: Int16, VerticalAdvance: Int16, YOffsetToVOrigin: Int16)Added ALMXHeader.init()Added ALMXHeader.init(Version: Fixed, Flags: UInt16, NMasters: UInt16, FirstGlyph: UInt16, LastGlyph: UInt16, lookup: SFNTLookupTable)Added AnchorPoint.init()Added AnchorPoint.init(x: Int16, y: Int16)Added AnchorPointTable.init()Added AnchorPointTable.init(nPoints: UInt32, points:(AnchorPoint))Added AnkrTable.init()Added AnkrTable.init(version: UInt16, flags: UInt16, lookupTableOffset: UInt32, anchorPointTableOffset: UInt32)Added BslnFormat0Part.init()Added BslnFormat0Part.init(deltas: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16))Added BslnFormat1Part.init()Added BslnFormat1Part.init(deltas: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16), mappingData: SFNTLookupTable)Added BslnFormat2Part.init()Added BslnFormat2Part.init(stdGlyph: UInt16, ctlPoints:(Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16))Added BslnFormat3Part.init()Added BslnFormat3Part.init(stdGlyph: UInt16, ctlPoints:(Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16), mappingData: SFNTLookupTable)Added BslnFormatUnion [struct]Added BslnFormatUnion.init()Added BslnTable.init()Added BslnTable.partsAdded BslnTable.init(version: Fixed, format: BslnTableFormat, defaultBaseline: UInt16, parts: BslnFormatUnion)Added CTFontOptions.init(rawValue: CFOptionFlags)Added CTFontStylisticClass.init(rawValue: UInt32)Added CTFontSymbolicTraits.init(rawValue: UInt32)Added CTFontTableOptions.init(rawValue: UInt32)Added CTLineBoundsOptions.init(rawValue: CFOptionFlags)Added CTParagraphStyleSetting.init()Added CTParagraphStyleSetting.init(spec: CTParagraphStyleSpecifier, valueSize: Int, value: UnsafePointer<Void>)Added CTRunDelegateCallbacks.init()Added CTRunDelegateCallbacks.init(version: CFIndex, dealloc: CTRunDelegateDeallocateCallback, getAscent: CTRunDelegateGetAscentCallback, getDescent: CTRunDelegateGetDescentCallback, getWidth: CTRunDelegateGetWidthCallback)Added CTRunStatus.init(rawValue: UInt32)Added CTUnderlineStyle.init(rawValue: Int32)Added CTUnderlineStyleModifiers.init(rawValue: Int32)Added FontVariation.init()Added FontVariation.init(name: FourCharCode, value: Fixed)Added JustDirectionTable.init()Added JustDirectionTable.init(justClass: UInt16, widthDeltaClusters: UInt16, postcomp: UInt16, lookup: SFNTLookupTable)Added JustPCAction.init()Added JustPCAction.init(actionCount: UInt32, actions:(JustPCActionSubrecord))Added JustPCActionSubrecord.init()Added JustPCActionSubrecord.init(theClass: UInt16, theType: JustPCActionType, length: UInt32, data: UInt32)Added JustPCConditionalAddAction.init()Added JustPCConditionalAddAction.init(substThreshold: Fixed, addGlyph: UInt16, substGlyph: UInt16)Added JustPCDecompositionAction.init()Added JustPCDecompositionAction.init(lowerLimit: Fixed, upperLimit: Fixed, order: UInt16, count: UInt16, glyphs:(UInt16))Added JustPCDuctilityAction.init()Added JustPCDuctilityAction.init(ductilityAxis: UInt32, minimumLimit: Fixed, noStretchValue: Fixed, maximumLimit: Fixed)Added JustPCGlyphRepeatAddAction.init()Added JustPCGlyphRepeatAddAction.init(flags: UInt16, glyph: UInt16)Added JustPostcompTable.init()Added JustPostcompTable.init(lookupTable: SFNTLookupTable)Added JustTable.init()Added JustTable.init(version: Fixed, format: UInt16, horizHeaderOffset: UInt16, vertHeaderOffset: UInt16)Added JustWidthDeltaEntry.init()Added JustWidthDeltaEntry.init(justClass: UInt32, beforeGrowLimit: Fixed, beforeShrinkLimit: Fixed, afterGrowLimit: Fixed, afterShrinkLimit: Fixed, growFlags: JustificationFlags, shrinkFlags: JustificationFlags)Added JustWidthDeltaGroup.init()Added JustWidthDeltaGroup.init(count: UInt32, entries:(JustWidthDeltaEntry))Added KernFormatSpecificHeader [struct]Added KernFormatSpecificHeader.init()Added KernIndexArrayHeader.init()Added KernIndexArrayHeader.init(glyphCount: UInt16, kernValueCount: UInt8, leftClassCount: UInt8, rightClassCount: UInt8, flags: UInt8, kernValue:(Int16), leftClass:(UInt8), rightClass:(UInt8), kernIndex:(UInt8))Added KernKerningPair.init()Added KernKerningPair.init(left: UInt16, right: UInt16)Added KernOffsetTable.init()Added KernOffsetTable.init(firstGlyph: UInt16, nGlyphs: UInt16, offsetTable:(KernArrayOffset))Added KernOrderedListEntry.init()Added KernOrderedListEntry.init(pair: KernKerningPair, value: KernKerningValue)Added KernOrderedListHeader.init()Added KernOrderedListHeader.init(nPairs: UInt16, searchRange: UInt16, entrySelector: UInt16, rangeShift: UInt16, table:(UInt16))Added KernSimpleArrayHeader.init()Added KernSimpleArrayHeader.init(rowWidth: UInt16, leftOffsetTable: UInt16, rightOffsetTable: UInt16, theArray: KernArrayOffset, firstTable:(UInt16))Added KernStateEntry.init()Added KernStateEntry.init(newState: UInt16, flags: UInt16)Added KernStateHeader.init()Added KernStateHeader.init(header: STHeader, valueTable: UInt16, firstTable:(UInt8))Added KernSubtableHeader.init()Added KernSubtableHeader.fsHeaderAdded KernSubtableHeader.init(length: Int32, stInfo: KernSubtableInfo, tupleIndex: Int16, fsHeader: KernFormatSpecificHeader)Added KernTableHeader.init()Added KernTableHeader.init(version: Fixed, nTables: Int32, firstSubtable:(UInt16))Added KernVersion0Header.init()Added KernVersion0Header.init(version: UInt16, nTables: UInt16, firstSubtable:(UInt16))Added KernVersion0SubtableHeader.init()Added KernVersion0SubtableHeader.fsHeaderAdded KernVersion0SubtableHeader.init(version: UInt16, length: UInt16, stInfo: KernSubtableInfo, fsHeader: KernFormatSpecificHeader)Added KerxAnchorPointAction.init()Added KerxAnchorPointAction.init(markAnchorPoint: UInt16, currAnchorPoint: UInt16)Added KerxControlPointAction.init()Added KerxControlPointAction.init(markControlPoint: UInt16, currControlPoint: UInt16)Added KerxControlPointEntry.init()Added KerxControlPointEntry.init(newState: UInt16, flags: UInt16, actionIndex: UInt16)Added KerxControlPointHeader.init()Added KerxControlPointHeader.init(header: STXHeader, flags: UInt32, firstTable:(UInt8))Added KerxCoordinateAction.init()Added KerxCoordinateAction.init(markX: UInt16, markY: UInt16, currX: UInt16, currY: UInt16)Added KerxFormatSpecificHeader [struct]Added KerxFormatSpecificHeader.init()Added KerxIndexArrayHeader.init()Added KerxIndexArrayHeader.init(glyphCount: UInt16, kernValueCount: UInt16, leftClassCount: UInt16, rightClassCount: UInt16, flags: UInt16, kernValue:(Int16), leftClass:(UInt16), rightClass:(UInt16), kernIndex:(UInt16))Added KerxKerningPair.init()Added KerxKerningPair.init(left: UInt16, right: UInt16)Added KerxOrderedListEntry.init()Added KerxOrderedListEntry.init(pair: KerxKerningPair, value: KernKerningValue)Added KerxOrderedListHeader.init()Added KerxOrderedListHeader.init(nPairs: UInt32, searchRange: UInt32, entrySelector: UInt32, rangeShift: UInt32, table:(UInt32))Added KerxSimpleArrayHeader.init()Added KerxSimpleArrayHeader.init(rowWidth: UInt32, leftOffsetTable: UInt32, rightOffsetTable: UInt32, theArray: KerxArrayOffset, firstTable:(UInt32))Added KerxStateEntry.init()Added KerxStateEntry.init(newState: UInt16, flags: UInt16, valueIndex: UInt16)Added KerxStateHeader.init()Added KerxStateHeader.init(header: STXHeader, valueTable: UInt32, firstTable:(UInt8))Added KerxSubtableHeader.init()Added KerxSubtableHeader.fsHeaderAdded KerxSubtableHeader.init(length: UInt32, stInfo: KerxSubtableCoverage, tupleIndex: UInt32, fsHeader: KerxFormatSpecificHeader)Added KerxTableHeader.init()Added KerxTableHeader.init(version: Fixed, nTables: UInt32, firstSubtable:(UInt32))Added LcarCaretClassEntry.init()Added LcarCaretClassEntry.init(count: UInt16, partials:(UInt16))Added LcarCaretTable.init()Added LcarCaretTable.init(version: Fixed, format: UInt16, lookup: SFNTLookupTable)Added LtagStringRange.init()Added LtagStringRange.init(offset: UInt16, length: UInt16)Added LtagTable.init()Added LtagTable.init(version: UInt32, flags: UInt32, numTags: UInt32, tagRange:(LtagStringRange))Added MortChain.init()Added MortChain.init(defaultFlags: MortSubtableMaskFlags, length: UInt32, nFeatures: UInt16, nSubtables: UInt16, featureEntries:(MortFeatureEntry))Added MortContextualSubtable.init()Added MortContextualSubtable.init(header: STHeader, substitutionTableOffset: UInt16)Added MortFeatureEntry.init()Added MortFeatureEntry.init(featureType: UInt16, featureSelector: UInt16, enableFlags: MortSubtableMaskFlags, disableFlags: MortSubtableMaskFlags)Added MortInsertionSubtable.init()Added MortInsertionSubtable.init(header: STHeader)Added MortLigatureSubtable.init()Added MortLigatureSubtable.init(header: STHeader, ligatureActionTableOffset: UInt16, componentTableOffset: UInt16, ligatureTableOffset: UInt16)Added MortRearrangementSubtable.init()Added MortRearrangementSubtable.init(header: STHeader)Added MortSpecificSubtable [struct]Added MortSpecificSubtable.init()Added MortSubtable.init()Added MortSubtable.init(length: UInt16, coverage: UInt16, flags: MortSubtableMaskFlags, u: MortSpecificSubtable)Added MortSubtable.uAdded MortSwashSubtable.init()Added MortSwashSubtable.init(lookup: SFNTLookupTable)Added MortTable.init()Added MortTable.init(version: Fixed, nChains: UInt32, chains:(MortChain))Added MorxChain.init()Added MorxChain.init(defaultFlags: MortSubtableMaskFlags, length: UInt32, nFeatures: UInt32, nSubtables: UInt32, featureEntries:(MortFeatureEntry))Added MorxContextualSubtable.init()Added MorxContextualSubtable.init(header: STXHeader, substitutionTableOffset: UInt32)Added MorxInsertionSubtable.init()Added MorxInsertionSubtable.init(header: STXHeader, insertionGlyphTableOffset: UInt32)Added MorxLigatureSubtable.init()Added MorxLigatureSubtable.init(header: STXHeader, ligatureActionTableOffset: UInt32, componentTableOffset: UInt32, ligatureTableOffset: UInt32)Added MorxRearrangementSubtable.init()Added MorxRearrangementSubtable.init(header: STXHeader)Added MorxSpecificSubtable [struct]Added MorxSpecificSubtable.init()Added MorxSubtable.init()Added MorxSubtable.init(length: UInt32, coverage: UInt32, flags: MortSubtableMaskFlags, u: MorxSpecificSubtable)Added MorxSubtable.uAdded MorxTable.init()Added MorxTable.init(version: Fixed, nChains: UInt32, chains:(MorxChain))Added OpbdSideValues.init()Added OpbdSideValues.init(leftSideShift: Int16, topSideShift: Int16, rightSideShift: Int16, bottomSideShift: Int16)Added OpbdTable.init()Added OpbdTable.init(version: Fixed, format: OpbdTableFormat, lookupTable: SFNTLookupTable)Added PropLookupSegment.init()Added PropLookupSegment.init(lastGlyph: UInt16, firstGlyph: UInt16, value: UInt16)Added PropLookupSingle.init()Added PropLookupSingle.init(glyph: UInt16, props: PropCharProperties)Added PropTable.init()Added PropTable.init(version: Fixed, format: UInt16, defaultProps: PropCharProperties, lookup: SFNTLookupTable)Added ROTAGlyphEntry.init()Added ROTAGlyphEntry.init(GlyphIndexOffset: Int16, HBaselineOffset: Int16, VBaselineOffset: Int16)Added ROTAHeader.init()Added ROTAHeader.init(Version: Fixed, Flags: UInt16, NMasters: UInt16, FirstGlyph: UInt16, LastGlyph: UInt16, lookup: SFNTLookupTable)Added SFNTLookupArrayHeader.init()Added SFNTLookupArrayHeader.init(lookupValues: (SFNTLookupValue))Added SFNTLookupBinarySearchHeader.init()Added SFNTLookupBinarySearchHeader.init(unitSize: UInt16, nUnits: UInt16, searchRange: UInt16, entrySelector: UInt16, rangeShift: UInt16)Added SFNTLookupFormatSpecificHeader [struct]Added SFNTLookupFormatSpecificHeader.init()Added SFNTLookupSegment.init()Added SFNTLookupSegment.init(lastGlyph: UInt16, firstGlyph: UInt16, value:(UInt16))Added SFNTLookupSegmentHeader.init()Added SFNTLookupSegmentHeader.init(binSearch: SFNTLookupBinarySearchHeader, segments:(SFNTLookupSegment))Added SFNTLookupSingle.init()Added SFNTLookupSingle.init(glyph: UInt16, value:(UInt16))Added SFNTLookupSingleHeader.init()Added SFNTLookupSingleHeader.init(binSearch: SFNTLookupBinarySearchHeader, entries:(SFNTLookupSingle))Added SFNTLookupTable.init()Added SFNTLookupTable.init(format: SFNTLookupTableFormat, fsHeader: SFNTLookupFormatSpecificHeader)Added SFNTLookupTable.fsHeaderAdded SFNTLookupTrimmedArrayHeader.init()Added SFNTLookupTrimmedArrayHeader.init(firstGlyph: UInt16, count: UInt16, valueArray:(SFNTLookupValue))Added STClassTable.init()Added STClassTable.init(firstGlyph: UInt16, nGlyphs: UInt16, classes:(STClass))Added STEntryOne.init()Added STEntryOne.init(newState: UInt16, flags: UInt16, offset1: UInt16)Added STEntryTwo.init()Added STEntryTwo.init(newState: UInt16, flags: UInt16, offset1: UInt16, offset2: UInt16)Added STEntryZero.init()Added STEntryZero.init(newState: UInt16, flags: UInt16)Added STHeader.init()Added STHeader.init(filler: UInt8, nClasses: STClass, classTableOffset: UInt16, stateArrayOffset: UInt16, entryTableOffset: UInt16)Added STXEntryOne.init()Added STXEntryOne.init(newState: STXStateIndex, flags: UInt16, index1: UInt16)Added STXEntryTwo.init()Added STXEntryTwo.init(newState: STXStateIndex, flags: UInt16, index1: UInt16, index2: UInt16)Added STXEntryZero.init()Added STXEntryZero.init(newState: STXStateIndex, flags: UInt16)Added STXHeader.init()Added STXHeader.init(nClasses: UInt32, classTableOffset: UInt32, stateArrayOffset: UInt32, entryTableOffset: UInt32)Added TrakTable.init()Added TrakTable.init(version: Fixed, format: UInt16, horizOffset: UInt16, vertOffset: UInt16)Added TrakTableData.init()Added TrakTableData.init(nTracks: UInt16, nSizes: UInt16, sizeTableOffset: UInt32, trakTable:(TrakTableEntry))Added TrakTableEntry.init()Added TrakTableEntry.init(track: Fixed, nameTableIndex: UInt16, sizesOffset: UInt16)Added sfntCMapEncoding.init()Added sfntCMapEncoding.init(platformID: UInt16, scriptID: UInt16, offset: UInt32)Added sfntCMapExtendedSubHeader.init()Added sfntCMapExtendedSubHeader.init(format: UInt16, reserved: UInt16, length: UInt32, language: UInt32)Added sfntCMapHeader.init()Added sfntCMapHeader.init(version: UInt16, numTables: UInt16, encoding:(sfntCMapEncoding))Added sfntCMapSubHeader.init()Added sfntCMapSubHeader.init(format: UInt16, length: UInt16, languageID: UInt16)Added sfntDescriptorHeader.init()Added sfntDescriptorHeader.init(version: Fixed, descriptorCount: Int32, descriptor:(sfntFontDescriptor))Added sfntDirectory.init()Added sfntDirectory.init(format: FourCharCode, numOffsets: UInt16, searchRange: UInt16, entrySelector: UInt16, rangeShift: UInt16, table:(sfntDirectoryEntry))Added sfntDirectoryEntry.init()Added sfntDirectoryEntry.init(tableTag: FourCharCode, checkSum: UInt32, offset: UInt32, length: UInt32)Added sfntFeatureHeader.init()Added sfntFeatureHeader.init(version: Int32, featureNameCount: UInt16, featureSetCount: UInt16, reserved: Int32, names:(sfntFeatureName), settings:(sfntFontFeatureSetting), runs:(sfntFontRunFeature))Added sfntFeatureName.init()Added sfntFeatureName.init(featureType: UInt16, settingCount: UInt16, offsetToSettings: Int32, featureFlags: UInt16, nameID: Int16)Added sfntFontDescriptor.init()Added sfntFontDescriptor.init(name: FourCharCode, value: Fixed)Added sfntFontFeatureSetting.init()Added sfntFontFeatureSetting.init(setting: UInt16, nameID: Int16)Added sfntFontRunFeature.init()Added sfntFontRunFeature.init(featureType: UInt16, setting: UInt16)Added sfntInstance.init()Added sfntInstance.init(nameID: Int16, flags: Int16, coord:(Fixed))Added sfntNameHeader.init()Added sfntNameHeader.init(format: UInt16, count: UInt16, stringOffset: UInt16, rec:(sfntNameRecord))Added sfntNameRecord.init()Added sfntNameRecord.init(platformID: UInt16, scriptID: UInt16, languageID: UInt16, nameID: UInt16, length: UInt16, offset: UInt16)Added sfntVariationAxis.init()Added sfntVariationAxis.init(axisTag: FourCharCode, minValue: Fixed, defaultValue: Fixed, maxValue: Fixed, flags: Int16, nameID: Int16)Added sfntVariationHeader.init()Added sfntVariationHeader.init(version: Fixed, offsetToData: UInt16, countSizePairs: UInt16, axisCount: UInt16, axisSize: UInt16, instanceCount: UInt16, instanceSize: UInt16, axis:(sfntVariationAxis), instance:(sfntInstance))Added kMORXCoverLogicalOrderModified ALMXGlyphEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ALMXGlyphEntry {     var GlyphIndexOffset: Int16     var HorizontalAdvance: Int16     var XOffsetToHOrigin: Int16     var VerticalAdvance: Int16     var YOffsetToVOrigin: Int16 } ``` |
| To | ``` struct ALMXGlyphEntry {     var GlyphIndexOffset: Int16     var HorizontalAdvance: Int16     var XOffsetToHOrigin: Int16     var VerticalAdvance: Int16     var YOffsetToVOrigin: Int16     init()     init(GlyphIndexOffset GlyphIndexOffset: Int16, HorizontalAdvance HorizontalAdvance: Int16, XOffsetToHOrigin XOffsetToHOrigin: Int16, VerticalAdvance VerticalAdvance: Int16, YOffsetToVOrigin YOffsetToVOrigin: Int16) } ``` |

Modified ALMXHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ALMXHeader {     var Version: Fixed     var Flags: UInt16     var NMasters: UInt16     var FirstGlyph: UInt16     var LastGlyph: UInt16     var lookup: SFNTLookupTable } ``` |
| To | ``` struct ALMXHeader {     var Version: Fixed     var Flags: UInt16     var NMasters: UInt16     var FirstGlyph: UInt16     var LastGlyph: UInt16     var lookup: SFNTLookupTable     init()     init(Version Version: Fixed, Flags Flags: UInt16, NMasters NMasters: UInt16, FirstGlyph FirstGlyph: UInt16, LastGlyph LastGlyph: UInt16, lookup lookup: SFNTLookupTable) } ``` |

Modified AnchorPoint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AnchorPoint {     var x: Int16     var y: Int16 } ``` |
| To | ``` struct AnchorPoint {     var x: Int16     var y: Int16     init()     init(x x: Int16, y y: Int16) } ``` |

Modified AnchorPointTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AnchorPointTable {     var nPoints: UInt32     var points: (AnchorPoint) } ``` |
| To | ``` struct AnchorPointTable {     var nPoints: UInt32     var points: (AnchorPoint)     init()     init(nPoints nPoints: UInt32, points points: (AnchorPoint)) } ``` |

Modified AnkrTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AnkrTable {     var version: UInt16     var flags: UInt16     var lookupTableOffset: UInt32     var anchorPointTableOffset: UInt32 } ``` |
| To | ``` struct AnkrTable {     var version: UInt16     var flags: UInt16     var lookupTableOffset: UInt32     var anchorPointTableOffset: UInt32     init()     init(version version: UInt16, flags flags: UInt16, lookupTableOffset lookupTableOffset: UInt32, anchorPointTableOffset anchorPointTableOffset: UInt32) } ``` |

Modified BslnFormat0Part [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BslnFormat0Part {     var deltas: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16) } ``` |
| To | ``` struct BslnFormat0Part {     var deltas: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     init()     init(deltas deltas: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)) } ``` |

Modified BslnFormat1Part [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BslnFormat1Part {     var deltas: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     var mappingData: SFNTLookupTable } ``` |
| To | ``` struct BslnFormat1Part {     var deltas: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     var mappingData: SFNTLookupTable     init()     init(deltas deltas: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16), mappingData mappingData: SFNTLookupTable) } ``` |

Modified BslnFormat2Part [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BslnFormat2Part {     var stdGlyph: UInt16     var ctlPoints: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16) } ``` |
| To | ``` struct BslnFormat2Part {     var stdGlyph: UInt16     var ctlPoints: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     init()     init(stdGlyph stdGlyph: UInt16, ctlPoints ctlPoints: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)) } ``` |

Modified BslnFormat3Part [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BslnFormat3Part {     var stdGlyph: UInt16     var ctlPoints: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     var mappingData: SFNTLookupTable } ``` |
| To | ``` struct BslnFormat3Part {     var stdGlyph: UInt16     var ctlPoints: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16)     var mappingData: SFNTLookupTable     init()     init(stdGlyph stdGlyph: UInt16, ctlPoints ctlPoints: (Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16, Int16), mappingData mappingData: SFNTLookupTable) } ``` |

Modified BslnTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BslnTable {     var version: Fixed     var format: BslnTableFormat     var defaultBaseline: UInt16 } ``` |
| To | ``` struct BslnTable {     var version: Fixed     var format: BslnTableFormat     var defaultBaseline: UInt16     var parts: BslnFormatUnion     init()     init(version version: Fixed, format format: BslnTableFormat, defaultBaseline defaultBaseline: UInt16, parts parts: BslnFormatUnion) } ``` |

Modified CTFontOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontOptions : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var Default: CTFontOptions { get }     static var PreventAutoActivation: CTFontOptions { get }     static var PreferSystemFont: CTFontOptions { get } } ``` | RawOptionSet |
| To | ``` struct CTFontOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var Default: CTFontOptions { get }     static var PreventAutoActivation: CTFontOptions { get }     static var PreferSystemFont: CTFontOptions { get } } ``` | RawOptionSetType |

Modified CTFontOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CTFontStylisticClass [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontStylisticClass : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var ClassUnknown: CTFontStylisticClass { get }     static var ClassOldStyleSerifs: CTFontStylisticClass { get }     static var ClassTransitionalSerifs: CTFontStylisticClass { get }     static var ClassModernSerifs: CTFontStylisticClass { get }     static var ClassClarendonSerifs: CTFontStylisticClass { get }     static var ClassSlabSerifs: CTFontStylisticClass { get }     static var ClassFreeformSerifs: CTFontStylisticClass { get }     static var ClassSansSerif: CTFontStylisticClass { get }     static var ClassOrnamentals: CTFontStylisticClass { get }     static var ClassScripts: CTFontStylisticClass { get }     static var ClassSymbolic: CTFontStylisticClass { get }     static var UnknownClass: CTFontStylisticClass { get }     static var OldStyleSerifsClass: CTFontStylisticClass { get }     static var TransitionalSerifsClass: CTFontStylisticClass { get }     static var ModernSerifsClass: CTFontStylisticClass { get }     static var ClarendonSerifsClass: CTFontStylisticClass { get }     static var SlabSerifsClass: CTFontStylisticClass { get }     static var FreeformSerifsClass: CTFontStylisticClass { get }     static var SansSerifClass: CTFontStylisticClass { get }     static var OrnamentalsClass: CTFontStylisticClass { get }     static var ScriptsClass: CTFontStylisticClass { get }     static var SymbolicClass: CTFontStylisticClass { get } } ``` | RawOptionSet |
| To | ``` struct CTFontStylisticClass : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var ClassUnknown: CTFontStylisticClass { get }     static var ClassOldStyleSerifs: CTFontStylisticClass { get }     static var ClassTransitionalSerifs: CTFontStylisticClass { get }     static var ClassModernSerifs: CTFontStylisticClass { get }     static var ClassClarendonSerifs: CTFontStylisticClass { get }     static var ClassSlabSerifs: CTFontStylisticClass { get }     static var ClassFreeformSerifs: CTFontStylisticClass { get }     static var ClassSansSerif: CTFontStylisticClass { get }     static var ClassOrnamentals: CTFontStylisticClass { get }     static var ClassScripts: CTFontStylisticClass { get }     static var ClassSymbolic: CTFontStylisticClass { get }     static var UnknownClass: CTFontStylisticClass { get }     static var OldStyleSerifsClass: CTFontStylisticClass { get }     static var TransitionalSerifsClass: CTFontStylisticClass { get }     static var ModernSerifsClass: CTFontStylisticClass { get }     static var ClarendonSerifsClass: CTFontStylisticClass { get }     static var SlabSerifsClass: CTFontStylisticClass { get }     static var FreeformSerifsClass: CTFontStylisticClass { get }     static var SansSerifClass: CTFontStylisticClass { get }     static var OrnamentalsClass: CTFontStylisticClass { get }     static var ScriptsClass: CTFontStylisticClass { get }     static var SymbolicClass: CTFontStylisticClass { get } } ``` | RawOptionSetType |

Modified CTFontStylisticClass.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CTFontSymbolicTraits [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontSymbolicTraits : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var TraitItalic: CTFontSymbolicTraits { get }     static var TraitBold: CTFontSymbolicTraits { get }     static var TraitExpanded: CTFontSymbolicTraits { get }     static var TraitCondensed: CTFontSymbolicTraits { get }     static var TraitMonoSpace: CTFontSymbolicTraits { get }     static var TraitVertical: CTFontSymbolicTraits { get }     static var TraitUIOptimized: CTFontSymbolicTraits { get }     static var TraitColorGlyphs: CTFontSymbolicTraits { get }     static var TraitComposite: CTFontSymbolicTraits { get }     static var TraitClassMask: CTFontSymbolicTraits { get }     static var ItalicTrait: CTFontSymbolicTraits { get }     static var BoldTrait: CTFontSymbolicTraits { get }     static var ExpandedTrait: CTFontSymbolicTraits { get }     static var CondensedTrait: CTFontSymbolicTraits { get }     static var MonoSpaceTrait: CTFontSymbolicTraits { get }     static var VerticalTrait: CTFontSymbolicTraits { get }     static var UIOptimizedTrait: CTFontSymbolicTraits { get }     static var ColorGlyphsTrait: CTFontSymbolicTraits { get }     static var CompositeTrait: CTFontSymbolicTraits { get }     static var ClassMaskTrait: CTFontSymbolicTraits { get } } ``` | RawOptionSet |
| To | ``` struct CTFontSymbolicTraits : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var TraitItalic: CTFontSymbolicTraits { get }     static var TraitBold: CTFontSymbolicTraits { get }     static var TraitExpanded: CTFontSymbolicTraits { get }     static var TraitCondensed: CTFontSymbolicTraits { get }     static var TraitMonoSpace: CTFontSymbolicTraits { get }     static var TraitVertical: CTFontSymbolicTraits { get }     static var TraitUIOptimized: CTFontSymbolicTraits { get }     static var TraitColorGlyphs: CTFontSymbolicTraits { get }     static var TraitComposite: CTFontSymbolicTraits { get }     static var TraitClassMask: CTFontSymbolicTraits { get }     static var ItalicTrait: CTFontSymbolicTraits { get }     static var BoldTrait: CTFontSymbolicTraits { get }     static var ExpandedTrait: CTFontSymbolicTraits { get }     static var CondensedTrait: CTFontSymbolicTraits { get }     static var MonoSpaceTrait: CTFontSymbolicTraits { get }     static var VerticalTrait: CTFontSymbolicTraits { get }     static var UIOptimizedTrait: CTFontSymbolicTraits { get }     static var ColorGlyphsTrait: CTFontSymbolicTraits { get }     static var CompositeTrait: CTFontSymbolicTraits { get }     static var ClassMaskTrait: CTFontSymbolicTraits { get } } ``` | RawOptionSetType |

Modified CTFontSymbolicTraits.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CTFontTableOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTFontTableOptions : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var NoOptions: CTFontTableOptions { get }     static var ExcludeSynthetic: CTFontTableOptions { get } } ``` | RawOptionSet |
| To | ``` struct CTFontTableOptions : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var NoOptions: CTFontTableOptions { get }     static var ExcludeSynthetic: CTFontTableOptions { get } } ``` | RawOptionSetType |

Modified CTFontTableOptions.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CTLineBoundsOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTLineBoundsOptions : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var ExcludeTypographicLeading: CTLineBoundsOptions { get }     static var ExcludeTypographicShifts: CTLineBoundsOptions { get }     static var UseHangingPunctuation: CTLineBoundsOptions { get }     static var UseGlyphPathBounds: CTLineBoundsOptions { get }     static var UseOpticalBounds: CTLineBoundsOptions { get } } ``` | RawOptionSet |
| To | ``` struct CTLineBoundsOptions : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var ExcludeTypographicLeading: CTLineBoundsOptions { get }     static var ExcludeTypographicShifts: CTLineBoundsOptions { get }     static var UseHangingPunctuation: CTLineBoundsOptions { get }     static var UseGlyphPathBounds: CTLineBoundsOptions { get }     static var UseOpticalBounds: CTLineBoundsOptions { get }     static var IncludeLanguageExtents: CTLineBoundsOptions { get } } ``` | RawOptionSetType |

Modified CTLineBoundsOptions.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CTParagraphStyleSetting [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTParagraphStyleSetting {     var spec: CTParagraphStyleSpecifier     var valueSize: UInt     var value: ConstUnsafePointer<()> } ``` |
| To | ``` struct CTParagraphStyleSetting {     var spec: CTParagraphStyleSpecifier     var valueSize: Int     var value: UnsafePointer<Void>     init()     init(spec spec: CTParagraphStyleSpecifier, valueSize valueSize: Int, value value: UnsafePointer<Void>) } ``` |

Modified CTParagraphStyleSetting.value

|  | Declaration |
| --- | --- |
| From | ``` var value: ConstUnsafePointer<()> ``` |
| To | ``` var value: UnsafePointer<Void> ``` |

Modified CTParagraphStyleSetting.valueSize

|  | Declaration |
| --- | --- |
| From | ``` var valueSize: UInt ``` |
| To | ``` var valueSize: Int ``` |

Modified CTRunDelegateCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CTRunDelegateCallbacks {     var version: CFIndex     var dealloc: CTRunDelegateDeallocateCallback     var getAscent: CTRunDelegateGetAscentCallback     var getDescent: CTRunDelegateGetDescentCallback     var getWidth: CTRunDelegateGetWidthCallback } ``` |
| To | ``` struct CTRunDelegateCallbacks {     var version: CFIndex     var dealloc: CTRunDelegateDeallocateCallback     var getAscent: CTRunDelegateGetAscentCallback     var getDescent: CTRunDelegateGetDescentCallback     var getWidth: CTRunDelegateGetWidthCallback     init()     init(version version: CFIndex, dealloc dealloc: CTRunDelegateDeallocateCallback, getAscent getAscent: CTRunDelegateGetAscentCallback, getDescent getDescent: CTRunDelegateGetDescentCallback, getWidth getWidth: CTRunDelegateGetWidthCallback) } ``` |

Modified CTRunStatus [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTRunStatus : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var NoStatus: CTRunStatus { get }     static var RightToLeft: CTRunStatus { get }     static var NonMonotonic: CTRunStatus { get }     static var HasNonIdentityMatrix: CTRunStatus { get } } ``` | RawOptionSet |
| To | ``` struct CTRunStatus : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var NoStatus: CTRunStatus { get }     static var RightToLeft: CTRunStatus { get }     static var NonMonotonic: CTRunStatus { get }     static var HasNonIdentityMatrix: CTRunStatus { get } } ``` | RawOptionSetType |

Modified CTRunStatus.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CTUnderlineStyle [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTUnderlineStyle : RawOptionSet {     init(_ value: Int32)     var value: Int32     static var None: CTUnderlineStyle { get }     static var Single: CTUnderlineStyle { get }     static var Thick: CTUnderlineStyle { get }     static var Double: CTUnderlineStyle { get } } ``` | RawOptionSet |
| To | ``` struct CTUnderlineStyle : RawOptionSetType {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     static var None: CTUnderlineStyle { get }     static var Single: CTUnderlineStyle { get }     static var Thick: CTUnderlineStyle { get }     static var Double: CTUnderlineStyle { get } } ``` | RawOptionSetType |

Modified CTUnderlineStyle.init(_: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: Int32) ``` |
| To | ``` init(_ rawValue: Int32) ``` |

Modified CTUnderlineStyleModifiers [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CTUnderlineStyleModifiers : RawOptionSet {     init(_ value: Int32)     var value: Int32     static var PatternSolid: CTUnderlineStyleModifiers { get }     static var PatternDot: CTUnderlineStyleModifiers { get }     static var PatternDash: CTUnderlineStyleModifiers { get }     static var PatternDashDot: CTUnderlineStyleModifiers { get }     static var PatternDashDotDot: CTUnderlineStyleModifiers { get } } ``` | RawOptionSet |
| To | ``` struct CTUnderlineStyleModifiers : RawOptionSetType {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     static var PatternSolid: CTUnderlineStyleModifiers { get }     static var PatternDot: CTUnderlineStyleModifiers { get }     static var PatternDash: CTUnderlineStyleModifiers { get }     static var PatternDashDot: CTUnderlineStyleModifiers { get }     static var PatternDashDotDot: CTUnderlineStyleModifiers { get } } ``` | RawOptionSetType |

Modified CTUnderlineStyleModifiers.init(_: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: Int32) ``` |
| To | ``` init(_ rawValue: Int32) ``` |

Modified FontVariation [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FontVariation {     var name: FourCharCode     var value: Fixed } ``` |
| To | ``` struct FontVariation {     var name: FourCharCode     var value: Fixed     init()     init(name name: FourCharCode, value value: Fixed) } ``` |

Modified JustDirectionTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustDirectionTable {     var justClass: UInt16     var widthDeltaClusters: UInt16     var postcomp: UInt16     var lookup: SFNTLookupTable } ``` |
| To | ``` struct JustDirectionTable {     var justClass: UInt16     var widthDeltaClusters: UInt16     var postcomp: UInt16     var lookup: SFNTLookupTable     init()     init(justClass justClass: UInt16, widthDeltaClusters widthDeltaClusters: UInt16, postcomp postcomp: UInt16, lookup lookup: SFNTLookupTable) } ``` |

Modified JustPCAction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustPCAction {     var actionCount: UInt32     var actions: (JustPCActionSubrecord) } ``` |
| To | ``` struct JustPCAction {     var actionCount: UInt32     var actions: (JustPCActionSubrecord)     init()     init(actionCount actionCount: UInt32, actions actions: (JustPCActionSubrecord)) } ``` |

Modified JustPCActionSubrecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustPCActionSubrecord {     var theClass: UInt16     var theType: JustPCActionType     var length: UInt32     var data: UInt32 } ``` |
| To | ``` struct JustPCActionSubrecord {     var theClass: UInt16     var theType: JustPCActionType     var length: UInt32     var data: UInt32     init()     init(theClass theClass: UInt16, theType theType: JustPCActionType, length length: UInt32, data data: UInt32) } ``` |

Modified JustPCConditionalAddAction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustPCConditionalAddAction {     var substThreshold: Fixed     var addGlyph: UInt16     var substGlyph: UInt16 } ``` |
| To | ``` struct JustPCConditionalAddAction {     var substThreshold: Fixed     var addGlyph: UInt16     var substGlyph: UInt16     init()     init(substThreshold substThreshold: Fixed, addGlyph addGlyph: UInt16, substGlyph substGlyph: UInt16) } ``` |

Modified JustPCDecompositionAction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustPCDecompositionAction {     var lowerLimit: Fixed     var upperLimit: Fixed     var order: UInt16     var count: UInt16     var glyphs: (UInt16) } ``` |
| To | ``` struct JustPCDecompositionAction {     var lowerLimit: Fixed     var upperLimit: Fixed     var order: UInt16     var count: UInt16     var glyphs: (UInt16)     init()     init(lowerLimit lowerLimit: Fixed, upperLimit upperLimit: Fixed, order order: UInt16, count count: UInt16, glyphs glyphs: (UInt16)) } ``` |

Modified JustPCDuctilityAction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustPCDuctilityAction {     var ductilityAxis: UInt32     var minimumLimit: Fixed     var noStretchValue: Fixed     var maximumLimit: Fixed } ``` |
| To | ``` struct JustPCDuctilityAction {     var ductilityAxis: UInt32     var minimumLimit: Fixed     var noStretchValue: Fixed     var maximumLimit: Fixed     init()     init(ductilityAxis ductilityAxis: UInt32, minimumLimit minimumLimit: Fixed, noStretchValue noStretchValue: Fixed, maximumLimit maximumLimit: Fixed) } ``` |

Modified JustPCGlyphRepeatAddAction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustPCGlyphRepeatAddAction {     var flags: UInt16     var glyph: UInt16 } ``` |
| To | ``` struct JustPCGlyphRepeatAddAction {     var flags: UInt16     var glyph: UInt16     init()     init(flags flags: UInt16, glyph glyph: UInt16) } ``` |

Modified JustPostcompTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustPostcompTable {     var lookupTable: SFNTLookupTable } ``` |
| To | ``` struct JustPostcompTable {     var lookupTable: SFNTLookupTable     init()     init(lookupTable lookupTable: SFNTLookupTable) } ``` |

Modified JustTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustTable {     var version: Fixed     var format: UInt16     var horizHeaderOffset: UInt16     var vertHeaderOffset: UInt16 } ``` |
| To | ``` struct JustTable {     var version: Fixed     var format: UInt16     var horizHeaderOffset: UInt16     var vertHeaderOffset: UInt16     init()     init(version version: Fixed, format format: UInt16, horizHeaderOffset horizHeaderOffset: UInt16, vertHeaderOffset vertHeaderOffset: UInt16) } ``` |

Modified JustWidthDeltaEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustWidthDeltaEntry {     var justClass: UInt32     var beforeGrowLimit: Fixed     var beforeShrinkLimit: Fixed     var afterGrowLimit: Fixed     var afterShrinkLimit: Fixed     var growFlags: JustificationFlags     var shrinkFlags: JustificationFlags } ``` |
| To | ``` struct JustWidthDeltaEntry {     var justClass: UInt32     var beforeGrowLimit: Fixed     var beforeShrinkLimit: Fixed     var afterGrowLimit: Fixed     var afterShrinkLimit: Fixed     var growFlags: JustificationFlags     var shrinkFlags: JustificationFlags     init()     init(justClass justClass: UInt32, beforeGrowLimit beforeGrowLimit: Fixed, beforeShrinkLimit beforeShrinkLimit: Fixed, afterGrowLimit afterGrowLimit: Fixed, afterShrinkLimit afterShrinkLimit: Fixed, growFlags growFlags: JustificationFlags, shrinkFlags shrinkFlags: JustificationFlags) } ``` |

Modified JustWidthDeltaGroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct JustWidthDeltaGroup {     var count: UInt32     var entries: (JustWidthDeltaEntry) } ``` |
| To | ``` struct JustWidthDeltaGroup {     var count: UInt32     var entries: (JustWidthDeltaEntry)     init()     init(count count: UInt32, entries entries: (JustWidthDeltaEntry)) } ``` |

Modified KernIndexArrayHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernIndexArrayHeader {     var glyphCount: UInt16     var kernValueCount: UInt8     var leftClassCount: UInt8     var rightClassCount: UInt8     var flags: UInt8     var kernValue: (Int16)     var leftClass: (UInt8)     var rightClass: (UInt8)     var kernIndex: (UInt8) } ``` |
| To | ``` struct KernIndexArrayHeader {     var glyphCount: UInt16     var kernValueCount: UInt8     var leftClassCount: UInt8     var rightClassCount: UInt8     var flags: UInt8     var kernValue: (Int16)     var leftClass: (UInt8)     var rightClass: (UInt8)     var kernIndex: (UInt8)     init()     init(glyphCount glyphCount: UInt16, kernValueCount kernValueCount: UInt8, leftClassCount leftClassCount: UInt8, rightClassCount rightClassCount: UInt8, flags flags: UInt8, kernValue kernValue: (Int16), leftClass leftClass: (UInt8), rightClass rightClass: (UInt8), kernIndex kernIndex: (UInt8)) } ``` |

Modified KernKerningPair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernKerningPair {     var left: UInt16     var right: UInt16 } ``` |
| To | ``` struct KernKerningPair {     var left: UInt16     var right: UInt16     init()     init(left left: UInt16, right right: UInt16) } ``` |

Modified KernOffsetTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernOffsetTable {     var firstGlyph: UInt16     var nGlyphs: UInt16     var offsetTable: (KernArrayOffset) } ``` |
| To | ``` struct KernOffsetTable {     var firstGlyph: UInt16     var nGlyphs: UInt16     var offsetTable: (KernArrayOffset)     init()     init(firstGlyph firstGlyph: UInt16, nGlyphs nGlyphs: UInt16, offsetTable offsetTable: (KernArrayOffset)) } ``` |

Modified KernOrderedListEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernOrderedListEntry {     var pair: KernKerningPair     var value: KernKerningValue } ``` |
| To | ``` struct KernOrderedListEntry {     var pair: KernKerningPair     var value: KernKerningValue     init()     init(pair pair: KernKerningPair, value value: KernKerningValue) } ``` |

Modified KernOrderedListHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernOrderedListHeader {     var nPairs: UInt16     var searchRange: UInt16     var entrySelector: UInt16     var rangeShift: UInt16     var table: (UInt16) } ``` |
| To | ``` struct KernOrderedListHeader {     var nPairs: UInt16     var searchRange: UInt16     var entrySelector: UInt16     var rangeShift: UInt16     var table: (UInt16)     init()     init(nPairs nPairs: UInt16, searchRange searchRange: UInt16, entrySelector entrySelector: UInt16, rangeShift rangeShift: UInt16, table table: (UInt16)) } ``` |

Modified KernSimpleArrayHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernSimpleArrayHeader {     var rowWidth: UInt16     var leftOffsetTable: UInt16     var rightOffsetTable: UInt16     var theArray: KernArrayOffset     var firstTable: (UInt16) } ``` |
| To | ``` struct KernSimpleArrayHeader {     var rowWidth: UInt16     var leftOffsetTable: UInt16     var rightOffsetTable: UInt16     var theArray: KernArrayOffset     var firstTable: (UInt16)     init()     init(rowWidth rowWidth: UInt16, leftOffsetTable leftOffsetTable: UInt16, rightOffsetTable rightOffsetTable: UInt16, theArray theArray: KernArrayOffset, firstTable firstTable: (UInt16)) } ``` |

Modified KernStateEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernStateEntry {     var newState: UInt16     var flags: UInt16 } ``` |
| To | ``` struct KernStateEntry {     var newState: UInt16     var flags: UInt16     init()     init(newState newState: UInt16, flags flags: UInt16) } ``` |

Modified KernStateHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernStateHeader {     var header: STHeader     var valueTable: UInt16     var firstTable: (UInt8) } ``` |
| To | ``` struct KernStateHeader {     var header: STHeader     var valueTable: UInt16     var firstTable: (UInt8)     init()     init(header header: STHeader, valueTable valueTable: UInt16, firstTable firstTable: (UInt8)) } ``` |

Modified KernSubtableHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernSubtableHeader {     var length: Int32     var stInfo: KernSubtableInfo     var tupleIndex: Int16 } ``` |
| To | ``` struct KernSubtableHeader {     var length: Int32     var stInfo: KernSubtableInfo     var tupleIndex: Int16     var fsHeader: KernFormatSpecificHeader     init()     init(length length: Int32, stInfo stInfo: KernSubtableInfo, tupleIndex tupleIndex: Int16, fsHeader fsHeader: KernFormatSpecificHeader) } ``` |

Modified KernTableHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernTableHeader {     var version: Fixed     var nTables: Int32     var firstSubtable: (UInt16) } ``` |
| To | ``` struct KernTableHeader {     var version: Fixed     var nTables: Int32     var firstSubtable: (UInt16)     init()     init(version version: Fixed, nTables nTables: Int32, firstSubtable firstSubtable: (UInt16)) } ``` |

Modified KernVersion0Header [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernVersion0Header {     var version: UInt16     var nTables: UInt16     var firstSubtable: (UInt16) } ``` |
| To | ``` struct KernVersion0Header {     var version: UInt16     var nTables: UInt16     var firstSubtable: (UInt16)     init()     init(version version: UInt16, nTables nTables: UInt16, firstSubtable firstSubtable: (UInt16)) } ``` |

Modified KernVersion0SubtableHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernVersion0SubtableHeader {     var version: UInt16     var length: UInt16     var stInfo: KernSubtableInfo } ``` |
| To | ``` struct KernVersion0SubtableHeader {     var version: UInt16     var length: UInt16     var stInfo: KernSubtableInfo     var fsHeader: KernFormatSpecificHeader     init()     init(version version: UInt16, length length: UInt16, stInfo stInfo: KernSubtableInfo, fsHeader fsHeader: KernFormatSpecificHeader) } ``` |

Modified KerxAnchorPointAction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxAnchorPointAction {     var markAnchorPoint: UInt16     var currAnchorPoint: UInt16 } ``` |
| To | ``` struct KerxAnchorPointAction {     var markAnchorPoint: UInt16     var currAnchorPoint: UInt16     init()     init(markAnchorPoint markAnchorPoint: UInt16, currAnchorPoint currAnchorPoint: UInt16) } ``` |

Modified KerxControlPointAction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxControlPointAction {     var markControlPoint: UInt16     var currControlPoint: UInt16 } ``` |
| To | ``` struct KerxControlPointAction {     var markControlPoint: UInt16     var currControlPoint: UInt16     init()     init(markControlPoint markControlPoint: UInt16, currControlPoint currControlPoint: UInt16) } ``` |

Modified KerxControlPointEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxControlPointEntry {     var newState: UInt16     var flags: UInt16     var actionIndex: UInt16 } ``` |
| To | ``` struct KerxControlPointEntry {     var newState: UInt16     var flags: UInt16     var actionIndex: UInt16     init()     init(newState newState: UInt16, flags flags: UInt16, actionIndex actionIndex: UInt16) } ``` |

Modified KerxControlPointHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxControlPointHeader {     var header: STXHeader     var flags: UInt32     var firstTable: (UInt8) } ``` |
| To | ``` struct KerxControlPointHeader {     var header: STXHeader     var flags: UInt32     var firstTable: (UInt8)     init()     init(header header: STXHeader, flags flags: UInt32, firstTable firstTable: (UInt8)) } ``` |

Modified KerxCoordinateAction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxCoordinateAction {     var markX: UInt16     var markY: UInt16     var currX: UInt16     var currY: UInt16 } ``` |
| To | ``` struct KerxCoordinateAction {     var markX: UInt16     var markY: UInt16     var currX: UInt16     var currY: UInt16     init()     init(markX markX: UInt16, markY markY: UInt16, currX currX: UInt16, currY currY: UInt16) } ``` |

Modified KerxIndexArrayHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxIndexArrayHeader {     var glyphCount: UInt16     var kernValueCount: UInt16     var leftClassCount: UInt16     var rightClassCount: UInt16     var flags: UInt16     var kernValue: (Int16)     var leftClass: (UInt16)     var rightClass: (UInt16)     var kernIndex: (UInt16) } ``` |
| To | ``` struct KerxIndexArrayHeader {     var glyphCount: UInt16     var kernValueCount: UInt16     var leftClassCount: UInt16     var rightClassCount: UInt16     var flags: UInt16     var kernValue: (Int16)     var leftClass: (UInt16)     var rightClass: (UInt16)     var kernIndex: (UInt16)     init()     init(glyphCount glyphCount: UInt16, kernValueCount kernValueCount: UInt16, leftClassCount leftClassCount: UInt16, rightClassCount rightClassCount: UInt16, flags flags: UInt16, kernValue kernValue: (Int16), leftClass leftClass: (UInt16), rightClass rightClass: (UInt16), kernIndex kernIndex: (UInt16)) } ``` |

Modified KerxKerningPair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxKerningPair {     var left: UInt16     var right: UInt16 } ``` |
| To | ``` struct KerxKerningPair {     var left: UInt16     var right: UInt16     init()     init(left left: UInt16, right right: UInt16) } ``` |

Modified KerxOrderedListEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxOrderedListEntry {     var pair: KerxKerningPair     var value: KernKerningValue } ``` |
| To | ``` struct KerxOrderedListEntry {     var pair: KerxKerningPair     var value: KernKerningValue     init()     init(pair pair: KerxKerningPair, value value: KernKerningValue) } ``` |

Modified KerxOrderedListHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxOrderedListHeader {     var nPairs: UInt32     var searchRange: UInt32     var entrySelector: UInt32     var rangeShift: UInt32     var table: (UInt32) } ``` |
| To | ``` struct KerxOrderedListHeader {     var nPairs: UInt32     var searchRange: UInt32     var entrySelector: UInt32     var rangeShift: UInt32     var table: (UInt32)     init()     init(nPairs nPairs: UInt32, searchRange searchRange: UInt32, entrySelector entrySelector: UInt32, rangeShift rangeShift: UInt32, table table: (UInt32)) } ``` |

Modified KerxSimpleArrayHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxSimpleArrayHeader {     var rowWidth: UInt32     var leftOffsetTable: UInt32     var rightOffsetTable: UInt32     var theArray: KerxArrayOffset     var firstTable: (UInt32) } ``` |
| To | ``` struct KerxSimpleArrayHeader {     var rowWidth: UInt32     var leftOffsetTable: UInt32     var rightOffsetTable: UInt32     var theArray: KerxArrayOffset     var firstTable: (UInt32)     init()     init(rowWidth rowWidth: UInt32, leftOffsetTable leftOffsetTable: UInt32, rightOffsetTable rightOffsetTable: UInt32, theArray theArray: KerxArrayOffset, firstTable firstTable: (UInt32)) } ``` |

Modified KerxStateEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxStateEntry {     var newState: UInt16     var flags: UInt16     var valueIndex: UInt16 } ``` |
| To | ``` struct KerxStateEntry {     var newState: UInt16     var flags: UInt16     var valueIndex: UInt16     init()     init(newState newState: UInt16, flags flags: UInt16, valueIndex valueIndex: UInt16) } ``` |

Modified KerxStateHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxStateHeader {     var header: STXHeader     var valueTable: UInt32     var firstTable: (UInt8) } ``` |
| To | ``` struct KerxStateHeader {     var header: STXHeader     var valueTable: UInt32     var firstTable: (UInt8)     init()     init(header header: STXHeader, valueTable valueTable: UInt32, firstTable firstTable: (UInt8)) } ``` |

Modified KerxSubtableHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxSubtableHeader {     var length: UInt32     var stInfo: KerxSubtableCoverage     var tupleIndex: UInt32 } ``` |
| To | ``` struct KerxSubtableHeader {     var length: UInt32     var stInfo: KerxSubtableCoverage     var tupleIndex: UInt32     var fsHeader: KerxFormatSpecificHeader     init()     init(length length: UInt32, stInfo stInfo: KerxSubtableCoverage, tupleIndex tupleIndex: UInt32, fsHeader fsHeader: KerxFormatSpecificHeader) } ``` |

Modified KerxTableHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxTableHeader {     var version: Fixed     var nTables: UInt32     var firstSubtable: (UInt32) } ``` |
| To | ``` struct KerxTableHeader {     var version: Fixed     var nTables: UInt32     var firstSubtable: (UInt32)     init()     init(version version: Fixed, nTables nTables: UInt32, firstSubtable firstSubtable: (UInt32)) } ``` |

Modified LcarCaretClassEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LcarCaretClassEntry {     var count: UInt16     var partials: (UInt16) } ``` |
| To | ``` struct LcarCaretClassEntry {     var count: UInt16     var partials: (UInt16)     init()     init(count count: UInt16, partials partials: (UInt16)) } ``` |

Modified LcarCaretTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LcarCaretTable {     var version: Fixed     var format: UInt16     var lookup: SFNTLookupTable } ``` |
| To | ``` struct LcarCaretTable {     var version: Fixed     var format: UInt16     var lookup: SFNTLookupTable     init()     init(version version: Fixed, format format: UInt16, lookup lookup: SFNTLookupTable) } ``` |

Modified LtagStringRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LtagStringRange {     var offset: UInt16     var length: UInt16 } ``` |
| To | ``` struct LtagStringRange {     var offset: UInt16     var length: UInt16     init()     init(offset offset: UInt16, length length: UInt16) } ``` |

Modified LtagTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LtagTable {     var version: UInt32     var flags: UInt32     var numTags: UInt32     var tagRange: (LtagStringRange) } ``` |
| To | ``` struct LtagTable {     var version: UInt32     var flags: UInt32     var numTags: UInt32     var tagRange: (LtagStringRange)     init()     init(version version: UInt32, flags flags: UInt32, numTags numTags: UInt32, tagRange tagRange: (LtagStringRange)) } ``` |

Modified MortChain [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortChain {     var defaultFlags: MortSubtableMaskFlags     var length: UInt32     var nFeatures: UInt16     var nSubtables: UInt16     var featureEntries: (MortFeatureEntry) } ``` |
| To | ``` struct MortChain {     var defaultFlags: MortSubtableMaskFlags     var length: UInt32     var nFeatures: UInt16     var nSubtables: UInt16     var featureEntries: (MortFeatureEntry)     init()     init(defaultFlags defaultFlags: MortSubtableMaskFlags, length length: UInt32, nFeatures nFeatures: UInt16, nSubtables nSubtables: UInt16, featureEntries featureEntries: (MortFeatureEntry)) } ``` |

Modified MortContextualSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortContextualSubtable {     var header: STHeader     var substitutionTableOffset: UInt16 } ``` |
| To | ``` struct MortContextualSubtable {     var header: STHeader     var substitutionTableOffset: UInt16     init()     init(header header: STHeader, substitutionTableOffset substitutionTableOffset: UInt16) } ``` |

Modified MortFeatureEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortFeatureEntry {     var featureType: UInt16     var featureSelector: UInt16     var enableFlags: MortSubtableMaskFlags     var disableFlags: MortSubtableMaskFlags } ``` |
| To | ``` struct MortFeatureEntry {     var featureType: UInt16     var featureSelector: UInt16     var enableFlags: MortSubtableMaskFlags     var disableFlags: MortSubtableMaskFlags     init()     init(featureType featureType: UInt16, featureSelector featureSelector: UInt16, enableFlags enableFlags: MortSubtableMaskFlags, disableFlags disableFlags: MortSubtableMaskFlags) } ``` |

Modified MortInsertionSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortInsertionSubtable {     var header: STHeader } ``` |
| To | ``` struct MortInsertionSubtable {     var header: STHeader     init()     init(header header: STHeader) } ``` |

Modified MortLigatureSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortLigatureSubtable {     var header: STHeader     var ligatureActionTableOffset: UInt16     var componentTableOffset: UInt16     var ligatureTableOffset: UInt16 } ``` |
| To | ``` struct MortLigatureSubtable {     var header: STHeader     var ligatureActionTableOffset: UInt16     var componentTableOffset: UInt16     var ligatureTableOffset: UInt16     init()     init(header header: STHeader, ligatureActionTableOffset ligatureActionTableOffset: UInt16, componentTableOffset componentTableOffset: UInt16, ligatureTableOffset ligatureTableOffset: UInt16) } ``` |

Modified MortRearrangementSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortRearrangementSubtable {     var header: STHeader } ``` |
| To | ``` struct MortRearrangementSubtable {     var header: STHeader     init()     init(header header: STHeader) } ``` |

Modified MortSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortSubtable {     var length: UInt16     var coverage: UInt16     var flags: MortSubtableMaskFlags } ``` |
| To | ``` struct MortSubtable {     var length: UInt16     var coverage: UInt16     var flags: MortSubtableMaskFlags     var u: MortSpecificSubtable     init()     init(length length: UInt16, coverage coverage: UInt16, flags flags: MortSubtableMaskFlags, u u: MortSpecificSubtable) } ``` |

Modified MortSwashSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortSwashSubtable {     var lookup: SFNTLookupTable } ``` |
| To | ``` struct MortSwashSubtable {     var lookup: SFNTLookupTable     init()     init(lookup lookup: SFNTLookupTable) } ``` |

Modified MortTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortTable {     var version: Fixed     var nChains: UInt32     var chains: (MortChain) } ``` |
| To | ``` struct MortTable {     var version: Fixed     var nChains: UInt32     var chains: (MortChain)     init()     init(version version: Fixed, nChains nChains: UInt32, chains chains: (MortChain)) } ``` |

Modified MorxChain [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorxChain {     var defaultFlags: MortSubtableMaskFlags     var length: UInt32     var nFeatures: UInt32     var nSubtables: UInt32     var featureEntries: (MortFeatureEntry) } ``` |
| To | ``` struct MorxChain {     var defaultFlags: MortSubtableMaskFlags     var length: UInt32     var nFeatures: UInt32     var nSubtables: UInt32     var featureEntries: (MortFeatureEntry)     init()     init(defaultFlags defaultFlags: MortSubtableMaskFlags, length length: UInt32, nFeatures nFeatures: UInt32, nSubtables nSubtables: UInt32, featureEntries featureEntries: (MortFeatureEntry)) } ``` |

Modified MorxContextualSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorxContextualSubtable {     var header: STXHeader     var substitutionTableOffset: UInt32 } ``` |
| To | ``` struct MorxContextualSubtable {     var header: STXHeader     var substitutionTableOffset: UInt32     init()     init(header header: STXHeader, substitutionTableOffset substitutionTableOffset: UInt32) } ``` |

Modified MorxInsertionSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorxInsertionSubtable {     var header: STXHeader     var insertionGlyphTableOffset: UInt32 } ``` |
| To | ``` struct MorxInsertionSubtable {     var header: STXHeader     var insertionGlyphTableOffset: UInt32     init()     init(header header: STXHeader, insertionGlyphTableOffset insertionGlyphTableOffset: UInt32) } ``` |

Modified MorxLigatureSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorxLigatureSubtable {     var header: STXHeader     var ligatureActionTableOffset: UInt32     var componentTableOffset: UInt32     var ligatureTableOffset: UInt32 } ``` |
| To | ``` struct MorxLigatureSubtable {     var header: STXHeader     var ligatureActionTableOffset: UInt32     var componentTableOffset: UInt32     var ligatureTableOffset: UInt32     init()     init(header header: STXHeader, ligatureActionTableOffset ligatureActionTableOffset: UInt32, componentTableOffset componentTableOffset: UInt32, ligatureTableOffset ligatureTableOffset: UInt32) } ``` |

Modified MorxRearrangementSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorxRearrangementSubtable {     var header: STXHeader } ``` |
| To | ``` struct MorxRearrangementSubtable {     var header: STXHeader     init()     init(header header: STXHeader) } ``` |

Modified MorxSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorxSubtable {     var length: UInt32     var coverage: UInt32     var flags: MortSubtableMaskFlags } ``` |
| To | ``` struct MorxSubtable {     var length: UInt32     var coverage: UInt32     var flags: MortSubtableMaskFlags     var u: MorxSpecificSubtable     init()     init(length length: UInt32, coverage coverage: UInt32, flags flags: MortSubtableMaskFlags, u u: MorxSpecificSubtable) } ``` |

Modified MorxTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorxTable {     var version: Fixed     var nChains: UInt32     var chains: (MorxChain) } ``` |
| To | ``` struct MorxTable {     var version: Fixed     var nChains: UInt32     var chains: (MorxChain)     init()     init(version version: Fixed, nChains nChains: UInt32, chains chains: (MorxChain)) } ``` |

Modified OpbdSideValues [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OpbdSideValues {     var leftSideShift: Int16     var topSideShift: Int16     var rightSideShift: Int16     var bottomSideShift: Int16 } ``` |
| To | ``` struct OpbdSideValues {     var leftSideShift: Int16     var topSideShift: Int16     var rightSideShift: Int16     var bottomSideShift: Int16     init()     init(leftSideShift leftSideShift: Int16, topSideShift topSideShift: Int16, rightSideShift rightSideShift: Int16, bottomSideShift bottomSideShift: Int16) } ``` |

Modified OpbdTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct OpbdTable {     var version: Fixed     var format: OpbdTableFormat     var lookupTable: SFNTLookupTable } ``` |
| To | ``` struct OpbdTable {     var version: Fixed     var format: OpbdTableFormat     var lookupTable: SFNTLookupTable     init()     init(version version: Fixed, format format: OpbdTableFormat, lookupTable lookupTable: SFNTLookupTable) } ``` |

Modified PropLookupSegment [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PropLookupSegment {     var lastGlyph: UInt16     var firstGlyph: UInt16     var value: UInt16 } ``` |
| To | ``` struct PropLookupSegment {     var lastGlyph: UInt16     var firstGlyph: UInt16     var value: UInt16     init()     init(lastGlyph lastGlyph: UInt16, firstGlyph firstGlyph: UInt16, value value: UInt16) } ``` |

Modified PropLookupSingle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PropLookupSingle {     var glyph: UInt16     var props: PropCharProperties } ``` |
| To | ``` struct PropLookupSingle {     var glyph: UInt16     var props: PropCharProperties     init()     init(glyph glyph: UInt16, props props: PropCharProperties) } ``` |

Modified PropTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PropTable {     var version: Fixed     var format: UInt16     var defaultProps: PropCharProperties     var lookup: SFNTLookupTable } ``` |
| To | ``` struct PropTable {     var version: Fixed     var format: UInt16     var defaultProps: PropCharProperties     var lookup: SFNTLookupTable     init()     init(version version: Fixed, format format: UInt16, defaultProps defaultProps: PropCharProperties, lookup lookup: SFNTLookupTable) } ``` |

Modified ROTAGlyphEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ROTAGlyphEntry {     var GlyphIndexOffset: Int16     var HBaselineOffset: Int16     var VBaselineOffset: Int16 } ``` |
| To | ``` struct ROTAGlyphEntry {     var GlyphIndexOffset: Int16     var HBaselineOffset: Int16     var VBaselineOffset: Int16     init()     init(GlyphIndexOffset GlyphIndexOffset: Int16, HBaselineOffset HBaselineOffset: Int16, VBaselineOffset VBaselineOffset: Int16) } ``` |

Modified ROTAHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ROTAHeader {     var Version: Fixed     var Flags: UInt16     var NMasters: UInt16     var FirstGlyph: UInt16     var LastGlyph: UInt16     var lookup: SFNTLookupTable } ``` |
| To | ``` struct ROTAHeader {     var Version: Fixed     var Flags: UInt16     var NMasters: UInt16     var FirstGlyph: UInt16     var LastGlyph: UInt16     var lookup: SFNTLookupTable     init()     init(Version Version: Fixed, Flags Flags: UInt16, NMasters NMasters: UInt16, FirstGlyph FirstGlyph: UInt16, LastGlyph LastGlyph: UInt16, lookup lookup: SFNTLookupTable) } ``` |

Modified SFNTLookupArrayHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupArrayHeader {     var lookupValues: (SFNTLookupValue) } ``` |
| To | ``` struct SFNTLookupArrayHeader {     var lookupValues: (SFNTLookupValue)     init()     init(lookupValues lookupValues: (SFNTLookupValue)) } ``` |

Modified SFNTLookupBinarySearchHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupBinarySearchHeader {     var unitSize: UInt16     var nUnits: UInt16     var searchRange: UInt16     var entrySelector: UInt16     var rangeShift: UInt16 } ``` |
| To | ``` struct SFNTLookupBinarySearchHeader {     var unitSize: UInt16     var nUnits: UInt16     var searchRange: UInt16     var entrySelector: UInt16     var rangeShift: UInt16     init()     init(unitSize unitSize: UInt16, nUnits nUnits: UInt16, searchRange searchRange: UInt16, entrySelector entrySelector: UInt16, rangeShift rangeShift: UInt16) } ``` |

Modified SFNTLookupSegment [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupSegment {     var lastGlyph: UInt16     var firstGlyph: UInt16     var value: (UInt16) } ``` |
| To | ``` struct SFNTLookupSegment {     var lastGlyph: UInt16     var firstGlyph: UInt16     var value: (UInt16)     init()     init(lastGlyph lastGlyph: UInt16, firstGlyph firstGlyph: UInt16, value value: (UInt16)) } ``` |

Modified SFNTLookupSegmentHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupSegmentHeader {     var binSearch: SFNTLookupBinarySearchHeader     var segments: (SFNTLookupSegment) } ``` |
| To | ``` struct SFNTLookupSegmentHeader {     var binSearch: SFNTLookupBinarySearchHeader     var segments: (SFNTLookupSegment)     init()     init(binSearch binSearch: SFNTLookupBinarySearchHeader, segments segments: (SFNTLookupSegment)) } ``` |

Modified SFNTLookupSingle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupSingle {     var glyph: UInt16     var value: (UInt16) } ``` |
| To | ``` struct SFNTLookupSingle {     var glyph: UInt16     var value: (UInt16)     init()     init(glyph glyph: UInt16, value value: (UInt16)) } ``` |

Modified SFNTLookupSingleHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupSingleHeader {     var binSearch: SFNTLookupBinarySearchHeader     var entries: (SFNTLookupSingle) } ``` |
| To | ``` struct SFNTLookupSingleHeader {     var binSearch: SFNTLookupBinarySearchHeader     var entries: (SFNTLookupSingle)     init()     init(binSearch binSearch: SFNTLookupBinarySearchHeader, entries entries: (SFNTLookupSingle)) } ``` |

Modified SFNTLookupTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupTable {     var format: SFNTLookupTableFormat } ``` |
| To | ``` struct SFNTLookupTable {     var format: SFNTLookupTableFormat     var fsHeader: SFNTLookupFormatSpecificHeader     init()     init(format format: SFNTLookupTableFormat, fsHeader fsHeader: SFNTLookupFormatSpecificHeader) } ``` |

Modified SFNTLookupTrimmedArrayHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupTrimmedArrayHeader {     var firstGlyph: UInt16     var count: UInt16     var valueArray: (SFNTLookupValue) } ``` |
| To | ``` struct SFNTLookupTrimmedArrayHeader {     var firstGlyph: UInt16     var count: UInt16     var valueArray: (SFNTLookupValue)     init()     init(firstGlyph firstGlyph: UInt16, count count: UInt16, valueArray valueArray: (SFNTLookupValue)) } ``` |

Modified STClassTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STClassTable {     var firstGlyph: UInt16     var nGlyphs: UInt16     var classes: (STClass) } ``` |
| To | ``` struct STClassTable {     var firstGlyph: UInt16     var nGlyphs: UInt16     var classes: (STClass)     init()     init(firstGlyph firstGlyph: UInt16, nGlyphs nGlyphs: UInt16, classes classes: (STClass)) } ``` |

Modified STEntryOne [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STEntryOne {     var newState: UInt16     var flags: UInt16     var offset1: UInt16 } ``` |
| To | ``` struct STEntryOne {     var newState: UInt16     var flags: UInt16     var offset1: UInt16     init()     init(newState newState: UInt16, flags flags: UInt16, offset1 offset1: UInt16) } ``` |

Modified STEntryTwo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STEntryTwo {     var newState: UInt16     var flags: UInt16     var offset1: UInt16     var offset2: UInt16 } ``` |
| To | ``` struct STEntryTwo {     var newState: UInt16     var flags: UInt16     var offset1: UInt16     var offset2: UInt16     init()     init(newState newState: UInt16, flags flags: UInt16, offset1 offset1: UInt16, offset2 offset2: UInt16) } ``` |

Modified STEntryZero [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STEntryZero {     var newState: UInt16     var flags: UInt16 } ``` |
| To | ``` struct STEntryZero {     var newState: UInt16     var flags: UInt16     init()     init(newState newState: UInt16, flags flags: UInt16) } ``` |

Modified STHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STHeader {     var filler: UInt8     var nClasses: STClass     var classTableOffset: UInt16     var stateArrayOffset: UInt16     var entryTableOffset: UInt16 } ``` |
| To | ``` struct STHeader {     var filler: UInt8     var nClasses: STClass     var classTableOffset: UInt16     var stateArrayOffset: UInt16     var entryTableOffset: UInt16     init()     init(filler filler: UInt8, nClasses nClasses: STClass, classTableOffset classTableOffset: UInt16, stateArrayOffset stateArrayOffset: UInt16, entryTableOffset entryTableOffset: UInt16) } ``` |

Modified STXEntryOne [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STXEntryOne {     var newState: STXStateIndex     var flags: UInt16     var index1: UInt16 } ``` |
| To | ``` struct STXEntryOne {     var newState: STXStateIndex     var flags: UInt16     var index1: UInt16     init()     init(newState newState: STXStateIndex, flags flags: UInt16, index1 index1: UInt16) } ``` |

Modified STXEntryTwo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STXEntryTwo {     var newState: STXStateIndex     var flags: UInt16     var index1: UInt16     var index2: UInt16 } ``` |
| To | ``` struct STXEntryTwo {     var newState: STXStateIndex     var flags: UInt16     var index1: UInt16     var index2: UInt16     init()     init(newState newState: STXStateIndex, flags flags: UInt16, index1 index1: UInt16, index2 index2: UInt16) } ``` |

Modified STXEntryZero [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STXEntryZero {     var newState: STXStateIndex     var flags: UInt16 } ``` |
| To | ``` struct STXEntryZero {     var newState: STXStateIndex     var flags: UInt16     init()     init(newState newState: STXStateIndex, flags flags: UInt16) } ``` |

Modified STXHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct STXHeader {     var nClasses: UInt32     var classTableOffset: UInt32     var stateArrayOffset: UInt32     var entryTableOffset: UInt32 } ``` |
| To | ``` struct STXHeader {     var nClasses: UInt32     var classTableOffset: UInt32     var stateArrayOffset: UInt32     var entryTableOffset: UInt32     init()     init(nClasses nClasses: UInt32, classTableOffset classTableOffset: UInt32, stateArrayOffset stateArrayOffset: UInt32, entryTableOffset entryTableOffset: UInt32) } ``` |

Modified TrakTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrakTable {     var version: Fixed     var format: UInt16     var horizOffset: UInt16     var vertOffset: UInt16 } ``` |
| To | ``` struct TrakTable {     var version: Fixed     var format: UInt16     var horizOffset: UInt16     var vertOffset: UInt16     init()     init(version version: Fixed, format format: UInt16, horizOffset horizOffset: UInt16, vertOffset vertOffset: UInt16) } ``` |

Modified TrakTableData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrakTableData {     var nTracks: UInt16     var nSizes: UInt16     var sizeTableOffset: UInt32     var trakTable: (TrakTableEntry) } ``` |
| To | ``` struct TrakTableData {     var nTracks: UInt16     var nSizes: UInt16     var sizeTableOffset: UInt32     var trakTable: (TrakTableEntry)     init()     init(nTracks nTracks: UInt16, nSizes nSizes: UInt16, sizeTableOffset sizeTableOffset: UInt32, trakTable trakTable: (TrakTableEntry)) } ``` |

Modified TrakTableEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrakTableEntry {     var track: Fixed     var nameTableIndex: UInt16     var sizesOffset: UInt16 } ``` |
| To | ``` struct TrakTableEntry {     var track: Fixed     var nameTableIndex: UInt16     var sizesOffset: UInt16     init()     init(track track: Fixed, nameTableIndex nameTableIndex: UInt16, sizesOffset sizesOffset: UInt16) } ``` |

Modified sfntCMapEncoding [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntCMapEncoding {     var platformID: UInt16     var scriptID: UInt16     var offset: UInt32 } ``` |
| To | ``` struct sfntCMapEncoding {     var platformID: UInt16     var scriptID: UInt16     var offset: UInt32     init()     init(platformID platformID: UInt16, scriptID scriptID: UInt16, offset offset: UInt32) } ``` |

Modified sfntCMapExtendedSubHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntCMapExtendedSubHeader {     var format: UInt16     var reserved: UInt16     var length: UInt32     var language: UInt32 } ``` |
| To | ``` struct sfntCMapExtendedSubHeader {     var format: UInt16     var reserved: UInt16     var length: UInt32     var language: UInt32     init()     init(format format: UInt16, reserved reserved: UInt16, length length: UInt32, language language: UInt32) } ``` |

Modified sfntCMapHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntCMapHeader {     var version: UInt16     var numTables: UInt16     var encoding: (sfntCMapEncoding) } ``` |
| To | ``` struct sfntCMapHeader {     var version: UInt16     var numTables: UInt16     var encoding: (sfntCMapEncoding)     init()     init(version version: UInt16, numTables numTables: UInt16, encoding encoding: (sfntCMapEncoding)) } ``` |

Modified sfntCMapSubHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntCMapSubHeader {     var format: UInt16     var length: UInt16     var languageID: UInt16 } ``` |
| To | ``` struct sfntCMapSubHeader {     var format: UInt16     var length: UInt16     var languageID: UInt16     init()     init(format format: UInt16, length length: UInt16, languageID languageID: UInt16) } ``` |

Modified sfntDescriptorHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntDescriptorHeader {     var version: Fixed     var descriptorCount: Int32     var descriptor: (sfntFontDescriptor) } ``` |
| To | ``` struct sfntDescriptorHeader {     var version: Fixed     var descriptorCount: Int32     var descriptor: (sfntFontDescriptor)     init()     init(version version: Fixed, descriptorCount descriptorCount: Int32, descriptor descriptor: (sfntFontDescriptor)) } ``` |

Modified sfntDirectory [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntDirectory {     var format: FourCharCode     var numOffsets: UInt16     var searchRange: UInt16     var entrySelector: UInt16     var rangeShift: UInt16     var table: (sfntDirectoryEntry) } ``` |
| To | ``` struct sfntDirectory {     var format: FourCharCode     var numOffsets: UInt16     var searchRange: UInt16     var entrySelector: UInt16     var rangeShift: UInt16     var table: (sfntDirectoryEntry)     init()     init(format format: FourCharCode, numOffsets numOffsets: UInt16, searchRange searchRange: UInt16, entrySelector entrySelector: UInt16, rangeShift rangeShift: UInt16, table table: (sfntDirectoryEntry)) } ``` |

Modified sfntDirectoryEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntDirectoryEntry {     var tableTag: FourCharCode     var checkSum: UInt32     var offset: UInt32     var length: UInt32 } ``` |
| To | ``` struct sfntDirectoryEntry {     var tableTag: FourCharCode     var checkSum: UInt32     var offset: UInt32     var length: UInt32     init()     init(tableTag tableTag: FourCharCode, checkSum checkSum: UInt32, offset offset: UInt32, length length: UInt32) } ``` |

Modified sfntFeatureHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntFeatureHeader {     var version: Int32     var featureNameCount: UInt16     var featureSetCount: UInt16     var reserved: Int32     var names: (sfntFeatureName)     var settings: (sfntFontFeatureSetting)     var runs: (sfntFontRunFeature) } ``` |
| To | ``` struct sfntFeatureHeader {     var version: Int32     var featureNameCount: UInt16     var featureSetCount: UInt16     var reserved: Int32     var names: (sfntFeatureName)     var settings: (sfntFontFeatureSetting)     var runs: (sfntFontRunFeature)     init()     init(version version: Int32, featureNameCount featureNameCount: UInt16, featureSetCount featureSetCount: UInt16, reserved reserved: Int32, names names: (sfntFeatureName), settings settings: (sfntFontFeatureSetting), runs runs: (sfntFontRunFeature)) } ``` |

Modified sfntFeatureName [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntFeatureName {     var featureType: UInt16     var settingCount: UInt16     var offsetToSettings: Int32     var featureFlags: UInt16     var nameID: Int16 } ``` |
| To | ``` struct sfntFeatureName {     var featureType: UInt16     var settingCount: UInt16     var offsetToSettings: Int32     var featureFlags: UInt16     var nameID: Int16     init()     init(featureType featureType: UInt16, settingCount settingCount: UInt16, offsetToSettings offsetToSettings: Int32, featureFlags featureFlags: UInt16, nameID nameID: Int16) } ``` |

Modified sfntFontDescriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntFontDescriptor {     var name: FourCharCode     var value: Fixed } ``` |
| To | ``` struct sfntFontDescriptor {     var name: FourCharCode     var value: Fixed     init()     init(name name: FourCharCode, value value: Fixed) } ``` |

Modified sfntFontFeatureSetting [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntFontFeatureSetting {     var setting: UInt16     var nameID: Int16 } ``` |
| To | ``` struct sfntFontFeatureSetting {     var setting: UInt16     var nameID: Int16     init()     init(setting setting: UInt16, nameID nameID: Int16) } ``` |

Modified sfntFontRunFeature [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntFontRunFeature {     var featureType: UInt16     var setting: UInt16 } ``` |
| To | ``` struct sfntFontRunFeature {     var featureType: UInt16     var setting: UInt16     init()     init(featureType featureType: UInt16, setting setting: UInt16) } ``` |

Modified sfntInstance [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntInstance {     var nameID: Int16     var flags: Int16     var coord: (Fixed) } ``` |
| To | ``` struct sfntInstance {     var nameID: Int16     var flags: Int16     var coord: (Fixed)     init()     init(nameID nameID: Int16, flags flags: Int16, coord coord: (Fixed)) } ``` |

Modified sfntNameHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntNameHeader {     var format: UInt16     var count: UInt16     var stringOffset: UInt16     var rec: (sfntNameRecord) } ``` |
| To | ``` struct sfntNameHeader {     var format: UInt16     var count: UInt16     var stringOffset: UInt16     var rec: (sfntNameRecord)     init()     init(format format: UInt16, count count: UInt16, stringOffset stringOffset: UInt16, rec rec: (sfntNameRecord)) } ``` |

Modified sfntNameRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntNameRecord {     var platformID: UInt16     var scriptID: UInt16     var languageID: UInt16     var nameID: UInt16     var length: UInt16     var offset: UInt16 } ``` |
| To | ``` struct sfntNameRecord {     var platformID: UInt16     var scriptID: UInt16     var languageID: UInt16     var nameID: UInt16     var length: UInt16     var offset: UInt16     init()     init(platformID platformID: UInt16, scriptID scriptID: UInt16, languageID languageID: UInt16, nameID nameID: UInt16, length length: UInt16, offset offset: UInt16) } ``` |

Modified sfntVariationAxis [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntVariationAxis {     var axisTag: FourCharCode     var minValue: Fixed     var defaultValue: Fixed     var maxValue: Fixed     var flags: Int16     var nameID: Int16 } ``` |
| To | ``` struct sfntVariationAxis {     var axisTag: FourCharCode     var minValue: Fixed     var defaultValue: Fixed     var maxValue: Fixed     var flags: Int16     var nameID: Int16     init()     init(axisTag axisTag: FourCharCode, minValue minValue: Fixed, defaultValue defaultValue: Fixed, maxValue maxValue: Fixed, flags flags: Int16, nameID nameID: Int16) } ``` |

Modified sfntVariationHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sfntVariationHeader {     var version: Fixed     var offsetToData: UInt16     var countSizePairs: UInt16     var axisCount: UInt16     var axisSize: UInt16     var instanceCount: UInt16     var instanceSize: UInt16     var axis: (sfntVariationAxis)     var instance: (sfntInstance) } ``` |
| To | ``` struct sfntVariationHeader {     var version: Fixed     var offsetToData: UInt16     var countSizePairs: UInt16     var axisCount: UInt16     var axisSize: UInt16     var instanceCount: UInt16     var instanceSize: UInt16     var axis: (sfntVariationAxis)     var instance: (sfntInstance)     init()     init(version version: Fixed, offsetToData offsetToData: UInt16, countSizePairs countSizePairs: UInt16, axisCount axisCount: UInt16, axisSize axisSize: UInt16, instanceCount instanceCount: UInt16, instanceSize instanceSize: UInt16, axis axis: (sfntVariationAxis), instance instance: (sfntInstance)) } ``` |

Modified BslnTablePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias BslnTablePtr = UnsafePointer<BslnTable> ``` |
| To | ``` typealias BslnTablePtr = UnsafeMutablePointer<BslnTable> ``` |

Modified CTFontCollectionCopyExclusionDescriptors(CTFontCollection!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionCopyFontAttribute(CTFontCollection!, CFString!, CTFontCollectionCopyOptions) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionCopyFontAttributes(CTFontCollection!, CFSet!, CTFontCollectionCopyOptions) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionCopyQueryDescriptors(CTFontCollection!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionCreateCopyWithFontDescriptors(CTFontCollection!, CFArray!, CFDictionary!) -> CTFontCollection!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCollectionCreateFromAvailableFonts(CFDictionary!) -> CTFontCollection!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCollectionCreateMatchingFontDescriptors(CTFontCollection!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCollectionCreateMatchingFontDescriptorsForFamily(CTFontCollection!, CFString!, CFDictionary!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(CTFontCollection!, CTFontCollectionSortDescriptorsCallback, UnsafeMutablePointer<Void>) -> CFArray!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_ collection: CTFontCollection!, _ sortCallback: CTFontCollectionSortDescriptorsCallback, _ refCon: UnsafePointer<()>) -> CFArray! ``` | OS X 10.10 |
| To | ``` func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_ collection: CTFontCollection!, _ sortCallback: CTFontCollectionSortDescriptorsCallback, _ refCon: UnsafeMutablePointer<Void>) -> CFArray! ``` | OS X 10.5 |

Modified CTFontCollectionCreateMatchingFontDescriptorsWithOptions(CTFontCollection!, CFDictionary!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionCreateMutableCopy(CTFontCollection!) -> CTMutableFontCollection!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionCreateWithFontDescriptors(CFArray!, CFDictionary!) -> CTFontCollection!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCollectionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCollectionSetExclusionDescriptors(CTMutableFontCollection!, CFArray!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionSetQueryDescriptors(CTMutableFontCollection!, CFArray!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontCollectionSortDescriptorsCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CTFontCollectionSortDescriptorsCallback = CFunctionPointer<((CTFontDescriptor!, CTFontDescriptor!, UnsafePointer<()>) -> CFComparisonResult)> ``` |
| To | ``` typealias CTFontCollectionSortDescriptorsCallback = CFunctionPointer<((CTFontDescriptor!, CTFontDescriptor!, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |

Modified CTFontCopyAttribute(CTFont!, CFString!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyAvailableTables(CTFont!, CTFontTableOptions) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyCharacterSet(CTFont!) -> CFCharacterSet!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyDefaultCascadeListForLanguages(CTFont!, CFArray!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CTFontCopyDisplayName(CTFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyFamilyName(CTFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyFeatureSettings(CTFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyFeatures(CTFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyFontDescriptor(CTFont!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyFullName(CTFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyGraphicsFont(CTFont!, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> CGFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCopyGraphicsFont(_ font: CTFont!, _ attributes: UnsafePointer<Unmanaged<CTFontDescriptor>?>) -> CGFont! ``` | OS X 10.10 |
| To | ``` func CTFontCopyGraphicsFont(_ font: CTFont!, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> CGFont! ``` | OS X 10.5 |

Modified CTFontCopyLocalizedName(CTFont!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFString!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCopyLocalizedName(_ font: CTFont!, _ nameKey: CFString!, _ actualLanguage: UnsafePointer<Unmanaged<CFString>?>) -> CFString! ``` | OS X 10.10 |
| To | ``` func CTFontCopyLocalizedName(_ font: CTFont!, _ nameKey: CFString!, _ actualLanguage: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFString! ``` | OS X 10.5 |

Modified CTFontCopyName(CTFont!, CFString!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyPostScriptName(CTFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopySupportedLanguages(CTFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyTable(CTFont!, CTFontTableTag, CTFontTableOptions) -> CFData!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyTraits(CTFont!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyVariation(CTFont!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCopyVariationAxes(CTFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCreateCopyWithAttributes(CTFont!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontDescriptor!) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateCopyWithAttributes(_ font: CTFont!, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor!) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateCopyWithAttributes(_ font: CTFont!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor!) -> CTFont! ``` | OS X 10.5 |

Modified CTFontCreateCopyWithFamily(CTFont!, CGFloat, UnsafePointer<CGAffineTransform>, CFString!) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateCopyWithFamily(_ font: CTFont!, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>, _ family: CFString!) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateCopyWithFamily(_ font: CTFont!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ family: CFString!) -> CTFont! ``` | OS X 10.5 |

Modified CTFontCreateCopyWithSymbolicTraits(CTFont!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateCopyWithSymbolicTraits(_ font: CTFont!, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateCopyWithSymbolicTraits(_ font: CTFont!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFont! ``` | OS X 10.5 |

Modified CTFontCreateForString(CTFont!, CFString!, CFRange) -> CTFont!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCreatePathForGlyph(CTFont!, CGGlyph, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreatePathForGlyph(_ font: CTFont!, _ glyph: CGGlyph, _ transform: ConstUnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.10 |
| To | ``` func CTFontCreatePathForGlyph(_ font: CTFont!, _ glyph: CGGlyph, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.5 |

Modified CTFontCreateUIFontForLanguage(CTFontUIFontType, CGFloat, CFString!) -> CTFont!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontCreateWithFontDescriptor(CTFontDescriptor!, CGFloat, UnsafePointer<CGAffineTransform>) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateWithFontDescriptor(_ descriptor: CTFontDescriptor!, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateWithFontDescriptor(_ descriptor: CTFontDescriptor!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>) -> CTFont! ``` | OS X 10.5 |

Modified CTFontCreateWithFontDescriptorAndOptions(CTFontDescriptor!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontOptions) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateWithFontDescriptorAndOptions(_ descriptor: CTFontDescriptor!, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateWithFontDescriptorAndOptions(_ descriptor: CTFontDescriptor!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont! ``` | OS X 10.6 |

Modified CTFontCreateWithGraphicsFont(CGFont!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontDescriptor!) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateWithGraphicsFont(_ graphicsFont: CGFont!, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor!) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateWithGraphicsFont(_ graphicsFont: CGFont!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor!) -> CTFont! ``` | OS X 10.5 |

Modified CTFontCreateWithName(CFString!, CGFloat, UnsafePointer<CGAffineTransform>) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateWithName(_ name: CFString!, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateWithName(_ name: CFString!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>) -> CTFont! ``` | OS X 10.5 |

Modified CTFontCreateWithNameAndOptions(CFString!, CGFloat, UnsafePointer<CGAffineTransform>, CTFontOptions) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateWithNameAndOptions(_ name: CFString!, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateWithNameAndOptions(_ name: CFString!, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ options: CTFontOptions) -> CTFont! ``` | OS X 10.6 |

Modified CTFontCreateWithPlatformFont(ATSFontRef, CGFloat, UnsafePointer<CGAffineTransform>, CTFontDescriptor!) -> CTFont!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontCreateWithPlatformFont(_ platformFont: ATSFontRef, _ size: CGFloat, _ matrix: ConstUnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor!) -> CTFont! ``` | OS X 10.10 |
| To | ``` func CTFontCreateWithPlatformFont(_ platformFont: ATSFontRef, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>, _ attributes: CTFontDescriptor!) -> CTFont! ``` | OS X 10.5 |

Modified CTFontCreateWithQuickdrawInstance(ConstStr255Param, Int16, UInt8, CGFloat) -> CTFont!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCopyAttribute(CTFontDescriptor!, CFString!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCopyAttributes(CTFontDescriptor!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCopyLocalizedAttribute(CTFontDescriptor!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontDescriptorCopyLocalizedAttribute(_ descriptor: CTFontDescriptor!, _ attribute: CFString!, _ language: UnsafePointer<Unmanaged<CFString>?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func CTFontDescriptorCopyLocalizedAttribute(_ descriptor: CTFontDescriptor!, _ attribute: CFString!, _ language: UnsafeMutablePointer<Unmanaged<CFString>?>) -> AnyObject! ``` | OS X 10.5 |

Modified CTFontDescriptorCreateCopyWithAttributes(CTFontDescriptor!, CFDictionary!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCreateCopyWithFamily(CTFontDescriptor!, CFString!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CTFontDescriptorCreateCopyWithFeature(CTFontDescriptor!, CFNumber!, CFNumber!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCreateCopyWithSymbolicTraits(CTFontDescriptor!, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CTFontDescriptorCreateCopyWithVariation(CTFontDescriptor!, CFNumber!, CGFloat) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCreateMatchingFontDescriptor(CTFontDescriptor!, CFSet!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCreateMatchingFontDescriptors(CTFontDescriptor!, CFSet!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCreateWithAttributes(CFDictionary!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorCreateWithNameAndSize(CFString!, CGFloat) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontDescriptorMatchFontDescriptorsWithProgressHandler(CFArray!, CFSet!, CTFontDescriptorProgressHandler!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CTFontDrawGlyphs(CTFont!, UnsafePointer<CGGlyph>, UnsafePointer<CGPoint>, Int, CGContext!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontDrawGlyphs(_ font: CTFont!, _ glyphs: ConstUnsafePointer<CGGlyph>, _ positions: ConstUnsafePointer<CGPoint>, _ count: UInt, _ context: CGContext!) ``` | OS X 10.10 |
| To | ``` func CTFontDrawGlyphs(_ font: CTFont!, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int, _ context: CGContext!) ``` | OS X 10.7 |

Modified CTFontGetAdvancesForGlyphs(CTFont!, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex) -> Double

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontGetAdvancesForGlyphs(_ font: CTFont!, _ orientation: CTFontOrientation, _ glyphs: ConstUnsafePointer<CGGlyph>, _ advances: UnsafePointer<CGSize>, _ count: CFIndex) -> Double ``` | OS X 10.10 |
| To | ``` func CTFontGetAdvancesForGlyphs(_ font: CTFont!, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ advances: UnsafeMutablePointer<CGSize>, _ count: CFIndex) -> Double ``` | OS X 10.5 |

Modified CTFontGetAscent(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetBoundingBox(CTFont!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetBoundingRectsForGlyphs(CTFont!, CTFontOrientation, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>, CFIndex) -> CGRect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontGetBoundingRectsForGlyphs(_ font: CTFont!, _ orientation: CTFontOrientation, _ glyphs: ConstUnsafePointer<CGGlyph>, _ boundingRects: UnsafePointer<CGRect>, _ count: CFIndex) -> CGRect ``` | OS X 10.10 |
| To | ``` func CTFontGetBoundingRectsForGlyphs(_ font: CTFont!, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>, _ count: CFIndex) -> CGRect ``` | OS X 10.5 |

Modified CTFontGetCapHeight(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetDescent(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetGlyphCount(CTFont!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetGlyphWithName(CTFont!, CFString!) -> CGGlyph

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetGlyphsForCharacters(CTFont!, UnsafePointer<UniChar>, UnsafeMutablePointer<CGGlyph>, CFIndex) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontGetGlyphsForCharacters(_ font: CTFont!, _ characters: ConstUnsafePointer<UniChar>, _ glyphs: UnsafePointer<CGGlyph>, _ count: CFIndex) -> Bool ``` | OS X 10.10 |
| To | ``` func CTFontGetGlyphsForCharacters(_ font: CTFont!, _ characters: UnsafePointer<UniChar>, _ glyphs: UnsafeMutablePointer<CGGlyph>, _ count: CFIndex) -> Bool ``` | OS X 10.5 |

Modified CTFontGetLeading(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetLigatureCaretPositions(CTFont!, CGGlyph, UnsafeMutablePointer<CGFloat>, CFIndex) -> CFIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontGetLigatureCaretPositions(_ font: CTFont!, _ glyph: CGGlyph, _ positions: UnsafePointer<CGFloat>, _ maxPositions: CFIndex) -> CFIndex ``` | OS X 10.10 |
| To | ``` func CTFontGetLigatureCaretPositions(_ font: CTFont!, _ glyph: CGGlyph, _ positions: UnsafeMutablePointer<CGFloat>, _ maxPositions: CFIndex) -> CFIndex ``` | OS X 10.5 |

Modified CTFontGetMatrix(CTFont!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetOpticalBoundsForGlyphs(CTFont!, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGRect>, CFIndex, CFOptionFlags) -> CGRect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontGetOpticalBoundsForGlyphs(_ font: CTFont!, _ glyphs: ConstUnsafePointer<CGGlyph>, _ boundingRects: UnsafePointer<CGRect>, _ count: CFIndex, _ options: CFOptionFlags) -> CGRect ``` | OS X 10.10 |
| To | ``` func CTFontGetOpticalBoundsForGlyphs(_ font: CTFont!, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>, _ count: CFIndex, _ options: CFOptionFlags) -> CGRect ``` | OS X 10.8 |

Modified CTFontGetPlatformFont(CTFont!, UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> ATSFontRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontGetPlatformFont(_ font: CTFont!, _ attributes: UnsafePointer<Unmanaged<CTFontDescriptor>?>) -> ATSFontRef ``` | OS X 10.10 |
| To | ``` func CTFontGetPlatformFont(_ font: CTFont!, _ attributes: UnsafeMutablePointer<Unmanaged<CTFontDescriptor>?>) -> ATSFontRef ``` | OS X 10.5 |

Modified CTFontGetSize(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetSlantAngle(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetStringEncoding(CTFont!) -> CFStringEncoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetSymbolicTraits(CTFont!) -> CTFontSymbolicTraits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetUnderlinePosition(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetUnderlineThickness(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetUnitsPerEm(CTFont!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontGetVerticalTranslationsForGlyphs(CTFont!, UnsafePointer<CGGlyph>, UnsafeMutablePointer<CGSize>, CFIndex)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontGetVerticalTranslationsForGlyphs(_ font: CTFont!, _ glyphs: ConstUnsafePointer<CGGlyph>, _ translations: UnsafePointer<CGSize>, _ count: CFIndex) ``` | OS X 10.10 |
| To | ``` func CTFontGetVerticalTranslationsForGlyphs(_ font: CTFont!, _ glyphs: UnsafePointer<CGGlyph>, _ translations: UnsafeMutablePointer<CGSize>, _ count: CFIndex) ``` | OS X 10.5 |

Modified CTFontGetXHeight(CTFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFontManagerCompareFontFamilyNames(UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Void>) -> CFComparisonResult

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontManagerCompareFontFamilyNames(_ family1: ConstUnsafePointer<()>, _ family2: ConstUnsafePointer<()>, _ context: UnsafePointer<()>) -> CFComparisonResult ``` | OS X 10.10 |
| To | ``` func CTFontManagerCompareFontFamilyNames(_ family1: UnsafePointer<Void>, _ family2: UnsafePointer<Void>, _ context: UnsafeMutablePointer<Void>) -> CFComparisonResult ``` | OS X 10.6 |

Modified CTFontManagerCopyAvailableFontFamilyNames() -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerCopyAvailableFontURLs() -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerCopyAvailablePostScriptNames() -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerCreateFontDescriptorFromData(CFData!) -> CTFontDescriptor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CTFontManagerCreateFontDescriptorsFromURL(CFURL!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerCreateFontRequestRunLoopSource(CFIndex,((CFDictionary!, pid_t) -> Unmanaged<CFArray>!)!) -> CFRunLoopSource!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerEnableFontDescriptors(CFArray!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerGetAutoActivationSetting(CFString!) -> CTFontManagerAutoActivationSetting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerGetScopeForURL(CFURL!) -> CTFontManagerScope

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerIsSupportedFont(CFURL!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerRegisterFontsForURL(CFURL!, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontManagerRegisterFontsForURL(_ fontURL: CFURL!, _ scope: CTFontManagerScope, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CTFontManagerRegisterFontsForURL(_ fontURL: CFURL!, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified CTFontManagerRegisterFontsForURLs(CFArray!, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontManagerRegisterFontsForURLs(_ fontURLs: CFArray!, _ scope: CTFontManagerScope, _ errors: UnsafePointer<Unmanaged<CFArray>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CTFontManagerRegisterFontsForURLs(_ fontURLs: CFArray!, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool ``` | OS X 10.6 |

Modified CTFontManagerRegisterGraphicsFont(CGFont!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontManagerRegisterGraphicsFont(_ font: CGFont!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CTFontManagerRegisterGraphicsFont(_ font: CGFont!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.8 |

Modified CTFontManagerSetAutoActivationSetting(CFString!, CTFontManagerAutoActivationSetting)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTFontManagerUnregisterFontsForURL(CFURL!, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontManagerUnregisterFontsForURL(_ fontURL: CFURL!, _ scope: CTFontManagerScope, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CTFontManagerUnregisterFontsForURL(_ fontURL: CFURL!, _ scope: CTFontManagerScope, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.6 |

Modified CTFontManagerUnregisterFontsForURLs(CFArray!, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontManagerUnregisterFontsForURLs(_ fontURLs: CFArray!, _ scope: CTFontManagerScope, _ errors: UnsafePointer<Unmanaged<CFArray>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CTFontManagerUnregisterFontsForURLs(_ fontURLs: CFArray!, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> Bool ``` | OS X 10.6 |

Modified CTFontManagerUnregisterGraphicsFont(CGFont!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFontManagerUnregisterGraphicsFont(_ font: CGFont!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CTFontManagerUnregisterGraphicsFont(_ font: CGFont!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.8 |

Modified CTFrameDraw(CTFrame!, CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFrameGetFrameAttributes(CTFrame!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFrameGetLineOrigins(CTFrame!, CFRange, UnsafeMutablePointer<CGPoint>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFrameGetLineOrigins(_ frame: CTFrame!, _ range: CFRange, _ origins: UnsafePointer<CGPoint>) ``` | OS X 10.10 |
| To | ``` func CTFrameGetLineOrigins(_ frame: CTFrame!, _ range: CFRange, _ origins: UnsafeMutablePointer<CGPoint>) ``` | OS X 10.5 |

Modified CTFrameGetLines(CTFrame!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFrameGetPath(CTFrame!) -> CGPath!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFrameGetStringRange(CTFrame!) -> CFRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFrameGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFrameGetVisibleStringRange(CTFrame!) -> CFRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFramesetterCreateFrame(CTFramesetter!, CFRange, CGPath!, CFDictionary!) -> CTFrame!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFramesetterCreateWithAttributedString(CFAttributedString!) -> CTFramesetter!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFramesetterGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFramesetterGetTypesetter(CTFramesetter!) -> CTTypesetter!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTFramesetterSuggestFrameSizeWithConstraints(CTFramesetter!, CFRange, CFDictionary!, CGSize, UnsafeMutablePointer<CFRange>) -> CGSize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTFramesetterSuggestFrameSizeWithConstraints(_ framesetter: CTFramesetter!, _ stringRange: CFRange, _ frameAttributes: CFDictionary!, _ constraints: CGSize, _ fitRange: UnsafePointer<CFRange>) -> CGSize ``` | OS X 10.10 |
| To | ``` func CTFramesetterSuggestFrameSizeWithConstraints(_ framesetter: CTFramesetter!, _ stringRange: CFRange, _ frameAttributes: CFDictionary!, _ constraints: CGSize, _ fitRange: UnsafeMutablePointer<CFRange>) -> CGSize ``` | OS X 10.5 |

Modified CTGetCoreTextVersion() -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTGlyphInfoCreateWithCharacterIdentifier(CGFontIndex, CTCharacterCollection, CFString!) -> CTGlyphInfo!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTGlyphInfoCreateWithGlyph(CGGlyph, CTFont!, CFString!) -> CTGlyphInfo!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTGlyphInfoCreateWithGlyphName(CFString!, CTFont!, CFString!) -> CTGlyphInfo!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTGlyphInfoGetCharacterCollection(CTGlyphInfo!) -> CTCharacterCollection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTGlyphInfoGetCharacterIdentifier(CTGlyphInfo!) -> CGFontIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTGlyphInfoGetGlyphName(CTGlyphInfo!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTGlyphInfoGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineCreateJustifiedLine(CTLine!, CGFloat, Double) -> CTLine!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineCreateTruncatedLine(CTLine!, Double, CTLineTruncationType, CTLine!) -> CTLine!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineCreateWithAttributedString(CFAttributedString!) -> CTLine!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineDraw(CTLine!, CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetBoundsWithOptions(CTLine!, CTLineBoundsOptions) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CTLineGetGlyphCount(CTLine!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetGlyphRuns(CTLine!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetImageBounds(CTLine!, CGContext!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetOffsetForStringIndex(CTLine!, CFIndex, UnsafeMutablePointer<CGFloat>) -> CGFloat

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTLineGetOffsetForStringIndex(_ line: CTLine!, _ charIndex: CFIndex, _ secondaryOffset: UnsafePointer<CGFloat>) -> CGFloat ``` | OS X 10.10 |
| To | ``` func CTLineGetOffsetForStringIndex(_ line: CTLine!, _ charIndex: CFIndex, _ secondaryOffset: UnsafeMutablePointer<CGFloat>) -> CGFloat ``` | OS X 10.5 |

Modified CTLineGetPenOffsetForFlush(CTLine!, CGFloat, Double) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetStringIndexForPosition(CTLine!, CGPoint) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetStringRange(CTLine!) -> CFRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetTrailingWhitespaceWidth(CTLine!) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTLineGetTypographicBounds(CTLine!, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Double

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTLineGetTypographicBounds(_ line: CTLine!, _ ascent: UnsafePointer<CGFloat>, _ descent: UnsafePointer<CGFloat>, _ leading: UnsafePointer<CGFloat>) -> Double ``` | OS X 10.10 |
| To | ``` func CTLineGetTypographicBounds(_ line: CTLine!, _ ascent: UnsafeMutablePointer<CGFloat>, _ descent: UnsafeMutablePointer<CGFloat>, _ leading: UnsafeMutablePointer<CGFloat>) -> Double ``` | OS X 10.5 |

Modified CTParagraphStyleCreate(UnsafePointer<CTParagraphStyleSetting>, Int) -> CTParagraphStyle!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTParagraphStyleCreate(_ settings: ConstUnsafePointer<CTParagraphStyleSetting>, _ settingCount: UInt) -> CTParagraphStyle! ``` | OS X 10.10 |
| To | ``` func CTParagraphStyleCreate(_ settings: UnsafePointer<CTParagraphStyleSetting>, _ settingCount: Int) -> CTParagraphStyle! ``` | OS X 10.5 |

Modified CTParagraphStyleCreateCopy(CTParagraphStyle!) -> CTParagraphStyle!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTParagraphStyleGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTParagraphStyleGetValueForSpecifier(CTParagraphStyle!, CTParagraphStyleSpecifier, Int, UnsafeMutablePointer<Void>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTParagraphStyleGetValueForSpecifier(_ paragraphStyle: CTParagraphStyle!, _ spec: CTParagraphStyleSpecifier, _ valueBufferSize: UInt, _ valueBuffer: UnsafePointer<()>) -> Bool ``` | OS X 10.10 |
| To | ``` func CTParagraphStyleGetValueForSpecifier(_ paragraphStyle: CTParagraphStyle!, _ spec: CTParagraphStyleSpecifier, _ valueBufferSize: Int, _ valueBuffer: UnsafeMutablePointer<Void>) -> Bool ``` | OS X 10.5 |

Modified CTRubyAnnotationCreate(CTRubyAlignment, CTRubyOverhang, CGFloat, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CTRubyAnnotation>!

|  | Declaration |
| --- | --- |
| From | ``` func CTRubyAnnotationCreate(_ alignment: CTRubyAlignment, _ overhang: CTRubyOverhang, _ sizeFactor: CGFloat, _ text: UnsafePointer<Unmanaged<CFString>?>) -> Unmanaged<CTRubyAnnotation>! ``` |
| To | ``` func CTRubyAnnotationCreate(_ alignment: CTRubyAlignment, _ overhang: CTRubyOverhang, _ sizeFactor: CGFloat, _ text: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Unmanaged<CTRubyAnnotation>! ``` |

Modified CTRunDelegateCreate(UnsafePointer<CTRunDelegateCallbacks>, UnsafeMutablePointer<Void>) -> CTRunDelegate!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunDelegateCreate(_ callbacks: ConstUnsafePointer<CTRunDelegateCallbacks>, _ refCon: UnsafePointer<()>) -> CTRunDelegate! ``` | OS X 10.10 |
| To | ``` func CTRunDelegateCreate(_ callbacks: UnsafePointer<CTRunDelegateCallbacks>, _ refCon: UnsafeMutablePointer<Void>) -> CTRunDelegate! ``` | OS X 10.5 |

Modified CTRunDelegateDeallocateCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateDeallocateCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CTRunDelegateDeallocateCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CTRunDelegateGetAscentCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetAscentCallback = CFunctionPointer<((UnsafePointer<()>) -> CGFloat)> ``` |
| To | ``` typealias CTRunDelegateGetAscentCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> CGFloat)> ``` |

Modified CTRunDelegateGetDescentCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetDescentCallback = CFunctionPointer<((UnsafePointer<()>) -> CGFloat)> ``` |
| To | ``` typealias CTRunDelegateGetDescentCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> CGFloat)> ``` |

Modified CTRunDelegateGetRefCon(CTRunDelegate!) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunDelegateGetRefCon(_ runDelegate: CTRunDelegate!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func CTRunDelegateGetRefCon(_ runDelegate: CTRunDelegate!) -> UnsafeMutablePointer<Void> ``` | OS X 10.5 |

Modified CTRunDelegateGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunDelegateGetWidthCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CTRunDelegateGetWidthCallback = CFunctionPointer<((UnsafePointer<()>) -> CGFloat)> ``` |
| To | ``` typealias CTRunDelegateGetWidthCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> CGFloat)> ``` |

Modified CTRunDraw(CTRun!, CGContext!, CFRange)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunGetAdvances(CTRun!, CFRange, UnsafeMutablePointer<CGSize>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetAdvances(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafePointer<CGSize>) ``` | OS X 10.10 |
| To | ``` func CTRunGetAdvances(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGSize>) ``` | OS X 10.5 |

Modified CTRunGetAdvancesPtr(CTRun!) -> UnsafePointer<CGSize>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetAdvancesPtr(_ run: CTRun!) -> ConstUnsafePointer<CGSize> ``` | OS X 10.10 |
| To | ``` func CTRunGetAdvancesPtr(_ run: CTRun!) -> UnsafePointer<CGSize> ``` | OS X 10.5 |

Modified CTRunGetAttributes(CTRun!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunGetGlyphCount(CTRun!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunGetGlyphs(CTRun!, CFRange, UnsafeMutablePointer<CGGlyph>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetGlyphs(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafePointer<CGGlyph>) ``` | OS X 10.10 |
| To | ``` func CTRunGetGlyphs(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGGlyph>) ``` | OS X 10.5 |

Modified CTRunGetGlyphsPtr(CTRun!) -> UnsafePointer<CGGlyph>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetGlyphsPtr(_ run: CTRun!) -> ConstUnsafePointer<CGGlyph> ``` | OS X 10.10 |
| To | ``` func CTRunGetGlyphsPtr(_ run: CTRun!) -> UnsafePointer<CGGlyph> ``` | OS X 10.5 |

Modified CTRunGetImageBounds(CTRun!, CGContext!, CFRange) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunGetPositions(CTRun!, CFRange, UnsafeMutablePointer<CGPoint>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetPositions(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafePointer<CGPoint>) ``` | OS X 10.10 |
| To | ``` func CTRunGetPositions(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafeMutablePointer<CGPoint>) ``` | OS X 10.5 |

Modified CTRunGetPositionsPtr(CTRun!) -> UnsafePointer<CGPoint>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetPositionsPtr(_ run: CTRun!) -> ConstUnsafePointer<CGPoint> ``` | OS X 10.10 |
| To | ``` func CTRunGetPositionsPtr(_ run: CTRun!) -> UnsafePointer<CGPoint> ``` | OS X 10.5 |

Modified CTRunGetStatus(CTRun!) -> CTRunStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunGetStringIndices(CTRun!, CFRange, UnsafeMutablePointer<CFIndex>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetStringIndices(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafePointer<CFIndex>) ``` | OS X 10.10 |
| To | ``` func CTRunGetStringIndices(_ run: CTRun!, _ range: CFRange, _ buffer: UnsafeMutablePointer<CFIndex>) ``` | OS X 10.5 |

Modified CTRunGetStringIndicesPtr(CTRun!) -> UnsafePointer<CFIndex>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetStringIndicesPtr(_ run: CTRun!) -> ConstUnsafePointer<CFIndex> ``` | OS X 10.10 |
| To | ``` func CTRunGetStringIndicesPtr(_ run: CTRun!) -> UnsafePointer<CFIndex> ``` | OS X 10.5 |

Modified CTRunGetStringRange(CTRun!) -> CFRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunGetTextMatrix(CTRun!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTRunGetTypographicBounds(CTRun!, CFRange, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Double

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CTRunGetTypographicBounds(_ run: CTRun!, _ range: CFRange, _ ascent: UnsafePointer<CGFloat>, _ descent: UnsafePointer<CGFloat>, _ leading: UnsafePointer<CGFloat>) -> Double ``` | OS X 10.10 |
| To | ``` func CTRunGetTypographicBounds(_ run: CTRun!, _ range: CFRange, _ ascent: UnsafeMutablePointer<CGFloat>, _ descent: UnsafeMutablePointer<CGFloat>, _ leading: UnsafeMutablePointer<CGFloat>) -> Double ``` | OS X 10.5 |

Modified CTTextTabCreate(CTTextAlignment, Double, CFDictionary!) -> CTTextTab!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTextTabGetAlignment(CTTextTab!) -> CTTextAlignment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTextTabGetLocation(CTTextTab!) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTextTabGetOptions(CTTextTab!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTextTabGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTypesetterCreateLine(CTTypesetter!, CFRange) -> CTLine!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTypesetterCreateLineWithOffset(CTTypesetter!, CFRange, Double) -> CTLine!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTTypesetterCreateWithAttributedString(CFAttributedString!) -> CTTypesetter!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTypesetterCreateWithAttributedStringAndOptions(CFAttributedString!, CFDictionary!) -> CTTypesetter!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTypesetterGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTypesetterSuggestClusterBreak(CTTypesetter!, CFIndex, Double) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTypesetterSuggestClusterBreakWithOffset(CTTypesetter!, CFIndex, Double, Double) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CTTypesetterSuggestLineBreak(CTTypesetter!, CFIndex, Double) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CTTypesetterSuggestLineBreakWithOffset(CTTypesetter!, CFIndex, Double, Double) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified KernOffsetTablePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias KernOffsetTablePtr = UnsafePointer<KernOffsetTable> ``` |
| To | ``` typealias KernOffsetTablePtr = UnsafeMutablePointer<KernOffsetTable> ``` |

Modified KernOrderedListEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias KernOrderedListEntryPtr = UnsafePointer<KernOrderedListEntry> ``` |
| To | ``` typealias KernOrderedListEntryPtr = UnsafeMutablePointer<KernOrderedListEntry> ``` |

Modified KernSubtableHeaderPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias KernSubtableHeaderPtr = UnsafePointer<KernSubtableHeader> ``` |
| To | ``` typealias KernSubtableHeaderPtr = UnsafeMutablePointer<KernSubtableHeader> ``` |

Modified KernTableHeaderHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias KernTableHeaderHandle = UnsafePointer<KernTableHeaderPtr> ``` |
| To | ``` typealias KernTableHeaderHandle = UnsafeMutablePointer<KernTableHeaderPtr> ``` |

Modified KernTableHeaderPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias KernTableHeaderPtr = UnsafePointer<KernTableHeader> ``` |
| To | ``` typealias KernTableHeaderPtr = UnsafeMutablePointer<KernTableHeader> ``` |

Modified KerxOrderedListEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias KerxOrderedListEntryPtr = UnsafePointer<KerxOrderedListEntry> ``` |
| To | ``` typealias KerxOrderedListEntryPtr = UnsafeMutablePointer<KerxOrderedListEntry> ``` |

Modified KerxSubtableHeaderPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias KerxSubtableHeaderPtr = UnsafePointer<KerxSubtableHeader> ``` |
| To | ``` typealias KerxSubtableHeaderPtr = UnsafeMutablePointer<KerxSubtableHeader> ``` |

Modified KerxTableHeaderHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias KerxTableHeaderHandle = UnsafePointer<KerxTableHeaderPtr> ``` |
| To | ``` typealias KerxTableHeaderHandle = UnsafeMutablePointer<KerxTableHeaderPtr> ``` |

Modified KerxTableHeaderPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias KerxTableHeaderPtr = UnsafePointer<KerxTableHeader> ``` |
| To | ``` typealias KerxTableHeaderPtr = UnsafeMutablePointer<KerxTableHeader> ``` |

Modified LcarCaretTablePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias LcarCaretTablePtr = UnsafePointer<LcarCaretTable> ``` |
| To | ``` typealias LcarCaretTablePtr = UnsafeMutablePointer<LcarCaretTable> ``` |

Modified SFNTLookupTableHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias SFNTLookupTableHandle = UnsafePointer<SFNTLookupTablePtr> ``` |
| To | ``` typealias SFNTLookupTableHandle = UnsafeMutablePointer<SFNTLookupTablePtr> ``` |

Modified SFNTLookupTablePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias SFNTLookupTablePtr = UnsafePointer<SFNTLookupTable> ``` |
| To | ``` typealias SFNTLookupTablePtr = UnsafeMutablePointer<SFNTLookupTable> ``` |

Modified kCTBaselineClassAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineClassHanging

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineClassIdeographicCentered

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineClassIdeographicHigh

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineClassIdeographicLow

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineClassMath

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineClassRoman

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineInfoAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineOriginalFont

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineReferenceFont

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTBaselineReferenceInfoAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTCharacterShapeAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontBaselineAdjustAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontCascadeListAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontCharacterSetAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontCollectionDisallowAutoActivationOption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCTFontCollectionIncludeDisabledFontsOption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCTFontCollectionRemoveDuplicatesOption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontCopyrightNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontDescriptionNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontDescriptorMatchingCurrentAssetSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontDescriptorMatchingDescriptors

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontDescriptorMatchingError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontDescriptorMatchingPercentage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontDescriptorMatchingResult

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontDescriptorMatchingSourceDescriptor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontDescriptorMatchingTotalAssetSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontDescriptorMatchingTotalDownloadedSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontDesignerNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontDesignerURLNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontDisplayNameAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontDownloadableAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCTFontEnabledAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontFamilyNameAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFamilyNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureSelectorDefaultKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureSelectorIdentifierKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureSelectorNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureSelectorSettingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureSettingsAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureTypeExclusiveKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureTypeIdentifierKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureTypeNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeatureTypeSelectorsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFeaturesAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFixedAdvanceAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontFormatAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontFullNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontLanguagesAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontLicenseNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontLicenseURLNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontMacintoshEncodingsAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontManagerBundleIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontManagerErrorDomain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontManagerErrorFontURLsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontManagerRegisteredFontsChangedNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontManufacturerNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontMatrixAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontNameAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontOrientationAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontPostScriptCIDNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontPostScriptNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontPriorityAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontRegistrationScopeAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontSampleTextNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontSizeAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontSlantTrait

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontStyleNameAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontStyleNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontSubFamilyNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontSymbolicTrait

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontTrademarkNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontTraitsAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontURLAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTFontUniqueNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontVariationAttribute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontVariationAxisDefaultValueKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontVariationAxisIdentifierKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontVariationAxisMaximumValueKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontVariationAxisMinimumValueKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontVariationAxisNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontVendorURLNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontVersionNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontWeightTrait

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFontWidthTrait

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTForegroundColorAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTForegroundColorFromContextAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTFrameClippingPathsAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCTFramePathClippingPathAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCTFramePathFillRuleAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCTFramePathWidthAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCTFrameProgressionAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTGlyphInfoAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTKernAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTLanguageAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCTLigatureAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTParagraphStyleAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTRunDelegateAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTStrokeColorAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTStrokeWidthAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCTSuperscriptAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTTabColumnTerminatorsAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTTypesetterOptionForcedEmbeddingLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTUnderlineColorAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTUnderlineStyleAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTVerticalFormsAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCTWritingDirectionAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

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
