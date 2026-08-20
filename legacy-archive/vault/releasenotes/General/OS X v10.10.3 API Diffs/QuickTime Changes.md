---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/QuickTime.html
archived_at: '2026-07-18T02:52:38.245244Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# QuickTime Changes

## QuickTime

Added ChunkOffsetAtom.init()Added ChunkOffsetAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, chunkOffsetTable:(Int32))Added ClippingAtom.init()Added ClippingAtom.init(size: Int32, atomType: Int32, aRgnClip: RgnAtom)Added CloneAtom.init()Added CloneAtom.init(size: Int32, atomType: Int32, cloneInfo: CloneRecord)Added CloneRecord.init()Added CloneRecord.init(flags: Int32, masterTrackID: Int32)Added CompositionOffsetAtom.init()Added CompositionOffsetAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, compositionOffsetTable:(CompositionOffsetEntry))Added CompositionOffsetEntry.init()Added CompositionOffsetEntry.init(sampleCount: Int32, displayOffset: TimeValue)Added CompositionShiftLeastGreatestAtom.init()Added CompositionShiftLeastGreatestAtom.init(size: Int32, atomType: Int32, flags: Int32, compositionOffsetToDTDDeltaShift: Int32, leastDecodeToDisplayDelta: Int32, greatestDecodeToDisplayDelta: Int32, displayStartTime: Int32, displayEndTime: Int32)Added DataInfoAtom.init()Added DataInfoAtom.init(size: Int32, atomType: Int32, dataRef: DataRefAtom)Added EditListAtom.init()Added EditListAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, editListTable:(EditListType))Added EditListType.init()Added EditListType.init(trackDuration: TimeValue, mediaTime: TimeValue, mediaRate: Fixed)Added EditsAtom.init()Added EditsAtom.init(size: Int32, atomType: Int32, editList: EditListAtom)Added FileTypeAtom.init()Added FileTypeAtom.init(size: Int32, atomType: Int32, majorBrand: Int32, minorVersion: Int32, compatibleBrands:(Int32, Int32, Int32, Int32))Added HandlerAtom.init()Added HandlerAtom.init(size: Int32, atomType: Int32, hInfo: PublicHandlerInfo)Added HiliteAtom.init()Added HiliteAtom.init(size: Int32, atomType: Int32, selStart: Int32, selEnd: Int32)Added ImageDescription.init()Added ImageDescription.init(idSize: Int32, cType: CodecType, resvd1: Int32, resvd2: Int16, dataRefIndex: Int16, version: Int16, revisionLevel: Int16, vendor: Int32, temporalQuality: CodecQ, spatialQuality: CodecQ, width: Int16, height: Int16, hRes: Fixed, vRes: Fixed, dataSize: Int32, frameCount: Int16, name: Str31, depth: Int16, clutID: Int16)Added KaraokeAtom.init()Added KaraokeAtom.init(numEntries: Int32, karaokeEntries:(KaraokeRec))Added KaraokeRec.init()Added KaraokeRec.init(timeVal: TimeValue, beginHilite: Int16, endHilite: Int16)Added MatrixRecord.init()Added MatrixRecord.init(matrix: ((Fixed, Fixed, Fixed),(Fixed, Fixed, Fixed),(Fixed, Fixed, Fixed)))Added MatteAtom.init()Added MatteAtom.init(size: Int32, atomType: Int32, aCompressedMatte: MatteCompressedAtom)Added MatteCompressedAtom.init()Added MatteCompressedAtom.init(size: Int32, atomType: Int32, flags: Int32, matteImageDescription: ImageDescription, matteData:(Int8))Added MediaDirectory.init()Added MediaDirectory.init(size: Int32, atomType: Int32, mediaHeader: MediaHeaderAtom, mediaHandler: HandlerAtom, mediaInfo: MediaInfo)Added MediaHeader.init()Added MediaHeader.init(flags: Int32, creationTime: Int32, modificationTime: Int32, timeScale: TimeValue, duration: TimeValue, language: Int16, quality: Int16)Added MediaHeaderAtom.init()Added MediaHeaderAtom.init(size: Int32, atomType: Int32, header: MediaHeader)Added MediaInfo.init()Added MediaInfo.init(size: Int32, atomType: Int32)Added MovieDirectory.init()Added MovieDirectory.init(size: Int32, atomType: Int32, header: MovieHeaderAtom, movieClip: ClippingAtom, track:(TrackDirectoryEntry), userData: UserDataAtom)Added MovieHeader.init()Added MovieHeader.init(flags: Int32, creationTime: Int32, modificationTime: Int32, timeScale: TimeValue, duration: TimeValue, preferredRate: Fixed, preferredVolume: Int16, reserved1: Int16, preferredLong1: Int32, preferredLong2: Int32, matrix: MatrixRecord, previewTime: TimeValue, previewDuration: TimeValue, posterTime: TimeValue, selectionTime: TimeValue, selectionDuration: TimeValue, currentTime: TimeValue, nextTrackID: Int32)Added MovieHeaderAtom.init()Added MovieHeaderAtom.init(size: Int32, atomType: Int32, header: MovieHeader)Added MoviesUserData.init()Added MoviesUserData.init(size: Int32, udType: Int32, data:(Int8))Added PartialSyncSampleAtom.init()Added PartialSyncSampleAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, partialSyncSampleTable:(UInt32))Added PublicHandlerInfo.init()Added PublicHandlerInfo.init(flags: Int32, componentType: Int32, componentSubType: Int32, componentManufacturer: Int32, componentFlags: Int32, componentFlagsMask: Int32, componentName:(Int8))Added QTAltCPURatingRecord.init()Added QTAltCPURatingRecord.init(flags: UInt32, speed: UInt16)Added QTAltComponentCheckRecord.init()Added QTAltComponentCheckRecord.init(flags: Int32, cd: ComponentDescription, minVersion: UInt32)Added QTAltDataRateRecord.init()Added QTAltDataRateRecord.init(flags: Int32, dataRate: Int32)Added QTAltLanguageRecord.init()Added QTAltLanguageRecord.init(flags: Int32, language: Int16)Added QTAltVersionCheckRecord.init()Added QTAltVersionCheckRecord.init(flags: Int32, gestaltTag: OSType, val1: UInt32, val2: UInt32, checkType: Int16)Added QTRGBColor.init()Added QTRGBColor.init(red: UInt16, green: UInt16, blue: UInt16)Added QTVRSampleDescription.init()Added QTVRSampleDescription.init(descSize: UInt32, descType: UInt32, reserved1: UInt32, reserved2: UInt16, dataRefIndex: UInt16, data: UInt32)Added ReferenceMovieDataRefRecord.init()Added ReferenceMovieDataRefRecord.init(flags: Int32, dataRefType: OSType, dataRefSize: Int32, dataRef:(Int8))Added ReferenceMovieNetworkStatusRecord.init()Added ReferenceMovieNetworkStatusRecord.init(flags: UInt32, valueCount: UInt32, netStatusValues:(Int32))Added RgnAtom.init()Added RgnAtom.init(size: Int32, atomType: Int32, rgnSize: Int16, rgnBBox: Rect, data:(Int8))Added SampleDependencyAtom.init()Added SampleDependencyAtom.init(size: Int32, atomType: Int32, flags: Int32, sampleDependencyTable:(UInt8))Added SampleDescription.init()Added SampleDescription.init(descSize: Int32, dataFormat: Int32, resvd1: Int32, resvd2: Int16, dataRefIndex: Int16)Added SampleDescriptionAtom.init()Added SampleDescriptionAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, sampleDescTable:(SampleDescription))Added SampleSizeAtom.init()Added SampleSizeAtom.init(size: Int32, atomType: Int32, flags: Int32, sampleSize: Int32, numEntries: Int32, sampleSizeTable:(Int32))Added SampleTableAtom.init()Added SampleTableAtom.init(size: Int32, atomType: Int32, sampleDescription: SampleDescriptionAtom, timeToSampleNum: TimeToSampleNumAtom, sampleToChunk: SampleToChunkAtom, syncSample: SyncSampleAtom, sampleSize: SampleSizeAtom, chunkOffset: ChunkOffsetAtom, shadowSync: ShadowSyncAtom)Added SampleToChunk.init()Added SampleToChunk.init(firstChunk: Int32, samplesPerChunk: Int32, sampleDescriptionID: Int32)Added SampleToChunkAtom.init()Added SampleToChunkAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, sampleToChunkTable:(SampleToChunk))Added SecureContentInfoAtom.init()Added SecureContentInfoAtom.init(size: Int32, atomType: Int32)Added SecureContentSchemeInfoAtom.init()Added SecureContentSchemeInfoAtom.init(size: Int32, atomType: Int32)Added SecureContentSchemeTypeAtom.init()Added SecureContentSchemeTypeAtom.init(size: Int32, atomType: Int32, flags: Int32, schemeType: Int32, schemeVersion: UInt32)Added ShadowSync.init()Added ShadowSync.init(fdSampleNum: Int32, syncSampleNum: Int32)Added ShadowSyncAtom.init()Added ShadowSyncAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, shadowSyncTable:(ShadowSync))Added SoundDescription.init()Added SoundDescription.init(descSize: Int32, dataFormat: Int32, resvd1: Int32, resvd2: Int16, dataRefIndex: Int16, version: Int16, revlevel: Int16, vendor: Int32, numChannels: Int16, sampleSize: Int16, compressionID: Int16, packetSize: Int16, sampleRate: UnsignedFixed)Added SoundDescriptionV1.init()Added SoundDescriptionV1.init(desc: SoundDescription, samplesPerPacket: UInt32, bytesPerPacket: UInt32, bytesPerFrame: UInt32, bytesPerSample: UInt32)Added SoundDescriptionV2.init()Added SoundDescriptionV2.init(descSize: Int32, dataFormat: OSType, resvd1: Int32, resvd2: Int16, dataRefIndex: Int16, version: Int16, revlevel: Int16, vendor: Int32, always3: Int16, always16: Int16, alwaysMinus2: Int16, always0: Int16, always65536: UInt32, sizeOfStructOnly: UInt32, audioSampleRate: Float64, numAudioChannels: UInt32, always7F000000: Int32, constBitsPerChannel: UInt32, formatSpecificFlags: UInt32, constBytesPerAudioPacket: UInt32, constLPCMFramesPerAudioPacket: UInt32)Added SoundMediaInfo.init()Added SoundMediaInfo.init(size: Int32, atomType: Int32, header: SoundMediaInfoHeaderAtom, dataHandler: HandlerAtom, dataReference: DataRefAtom, sampleTable: SampleTableAtom)Added SoundMediaInfoHeader.init()Added SoundMediaInfoHeader.init(flags: Int32, balance: Int16, rsrvd: Int16)Added SoundMediaInfoHeaderAtom.init()Added SoundMediaInfoHeaderAtom.init(size: Int32, atomType: Int32, smiHeader: SoundMediaInfoHeader)Added SyncSampleAtom.init()Added SyncSampleAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, syncSampleTable:(Int32))Added TextBoxAtom.init()Added TextBoxAtom.init(size: Int32, atomType: Int32, textBox: Rect)Added TextDescription.init()Added TextDescription.init(descSize: Int32, dataFormat: Int32, resvd1: Int32, resvd2: Int16, dataRefIndex: Int16, displayFlags: Int32, textJustification: Int32, bgColor: QTRGBColor, defaultTextBox: Rect, defaultStyle: ScrpSTElement, defaultFontName:(Int8))Added TimeCodeDef.init()Added TimeCodeDef.init(flags: Int32, fTimeScale: TimeScale, frameDuration: TimeValue, numFrames: UInt8, padding: UInt8)Added TimeCodeDescription.init()Added TimeCodeDescription.init(descSize: Int32, dataFormat: Int32, resvd1: Int32, resvd2: Int16, dataRefIndex: Int16, flags: Int32, timeCodeDef: TimeCodeDef, srcRef:(Int32))Added TimeToSampleNum.init()Added TimeToSampleNum.init(sampleCount: Int32, sampleDuration: TimeValue)Added TimeToSampleNumAtom.init()Added TimeToSampleNumAtom.init(size: Int32, atomType: Int32, flags: Int32, numEntries: Int32, timeToSampleNumTable:(TimeToSampleNum))Added TrackCleanApertureDimensions.init()Added TrackCleanApertureDimensions.init(flags: Int32, cleanApertureDimensions: FixedPoint)Added TrackCleanApertureDimensionsAtom.init()Added TrackCleanApertureDimensionsAtom.init(size: Int32, atomType: Int32, cleanApertureDimensions: TrackCleanApertureDimensions)Added TrackDirectory.init()Added TrackDirectory.init(size: Int32, atomType: Int32, trackHeader: TrackHeaderAtom, trackClip: ClippingAtom, edits: EditsAtom, media: MediaDirectory, userData: UserDataAtom)Added TrackDirectoryEntry.init()Added TrackDirectoryEntry.init(trackDirectory: TrackDirectory)Added TrackEncodedPixelsDimensions.init()Added TrackEncodedPixelsDimensions.init(flags: Int32, encodedPixelsDimensions: FixedPoint)Added TrackEncodedPixelsDimensionsAtom.init()Added TrackEncodedPixelsDimensionsAtom.init(size: Int32, atomType: Int32, encodedPixelsDimensions: TrackEncodedPixelsDimensions)Added TrackHeader.init()Added TrackHeader.init(flags: Int32, creationTime: Int32, modificationTime: Int32, trackID: Int32, reserved1: Int32, duration: TimeValue, reserved2: Int32, reserved3: Int32, layer: Int16, alternateGroup: Int16, volume: Int16, reserved4: Int16, matrix: MatrixRecord, trackWidth: Fixed, trackHeight: Fixed)Added TrackHeaderAtom.init()Added TrackHeaderAtom.init(size: Int32, atomType: Int32, header: TrackHeader)Added TrackLoadSettings.init()Added TrackLoadSettings.init(preloadStartTime: TimeValue, preloadDuration: TimeValue, preloadFlags: Int32, defaultHints: Int32)Added TrackLoadSettingsAtom.init()Added TrackLoadSettingsAtom.init(size: Int32, atomType: Int32, settings: TrackLoadSettings)Added TrackProductionApertureDimensions.init()Added TrackProductionApertureDimensions.init(flags: Int32, productionApertureDimensions: FixedPoint)Added TrackProductionApertureDimensionsAtom.init()Added TrackProductionApertureDimensionsAtom.init(size: Int32, atomType: Int32, productionApertureDimensions: TrackProductionApertureDimensions)Added Tx3gDescription.init()Added Tx3gDescription.init(descSize: Int32, dataFormat: Int32, resvd1: Int32, resvd2: Int16, dataRefIndex: Int16, displayFlags: UInt32, horizontalJustification: Int8, verticalJustification: Int8, backgroundColor: Tx3gRGBAColor, defaultTextBox: Rect, defaultStyle: Tx3gStyleRecord)Added Tx3gFontRecord.init()Added Tx3gFontRecord.init(fontID: UInt16, nameLength: UInt8, name:(UInt8))Added Tx3gFontTableRecord.init()Added Tx3gFontTableRecord.init(entryCount: UInt16, fontEntries:(Tx3gFontRecord))Added Tx3gRGBAColor.init()Added Tx3gRGBAColor.init(red: UInt8, green: UInt8, blue: UInt8, transparency: UInt8)Added Tx3gStyleRecord.init()Added Tx3gStyleRecord.init(startChar: UInt16, endChar: UInt16, fontID: UInt16, fontFace: UInt8, fontSize: UInt8, fontColor: Tx3gRGBAColor)Added Tx3gStyleTableRecord.init()Added Tx3gStyleTableRecord.init(count: UInt16, table:(Tx3gStyleRecord))Added UserDataAtom.init()Added UserDataAtom.init(size: Int32, atomType: Int32, userData:(MoviesUserData))Added VideoMediaInfo.init()Added VideoMediaInfo.init(size: Int32, atomType: Int32, header: VideoMediaInfoHeaderAtom, dataHandler: HandlerAtom, dataInfo: DataInfoAtom, sampleTable: SampleTableAtom)Added VideoMediaInfoHeader.init()Added VideoMediaInfoHeader.init(flags: Int32, graphicsMode: Int16, opColorRed: Int16, opColorGreen: Int16, opColorBlue: Int16)Added VideoMediaInfoHeaderAtom.init()Added VideoMediaInfoHeaderAtom.init(size: Int32, atomType: Int32, vmiHeader: VideoMediaInfoHeader)Modified ChunkOffsetAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ChunkOffsetAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var chunkOffsetTable: (Int32) } ``` |
| To | ``` struct ChunkOffsetAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var chunkOffsetTable: (Int32)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, chunkOffsetTable chunkOffsetTable: (Int32)) } ``` |

Modified ClippingAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ClippingAtom {     var size: Int32     var atomType: Int32     var aRgnClip: RgnAtom } ``` |
| To | ``` struct ClippingAtom {     var size: Int32     var atomType: Int32     var aRgnClip: RgnAtom     init()     init(size size: Int32, atomType atomType: Int32, aRgnClip aRgnClip: RgnAtom) } ``` |

Modified CloneAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CloneAtom {     var size: Int32     var atomType: Int32     var cloneInfo: CloneRecord } ``` |
| To | ``` struct CloneAtom {     var size: Int32     var atomType: Int32     var cloneInfo: CloneRecord     init()     init(size size: Int32, atomType atomType: Int32, cloneInfo cloneInfo: CloneRecord) } ``` |

Modified CloneRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CloneRecord {     var flags: Int32     var masterTrackID: Int32 } ``` |
| To | ``` struct CloneRecord {     var flags: Int32     var masterTrackID: Int32     init()     init(flags flags: Int32, masterTrackID masterTrackID: Int32) } ``` |

Modified CompositionOffsetAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CompositionOffsetAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var compositionOffsetTable: (CompositionOffsetEntry) } ``` |
| To | ``` struct CompositionOffsetAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var compositionOffsetTable: (CompositionOffsetEntry)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, compositionOffsetTable compositionOffsetTable: (CompositionOffsetEntry)) } ``` |

Modified CompositionOffsetEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CompositionOffsetEntry {     var sampleCount: Int32     var displayOffset: TimeValue } ``` |
| To | ``` struct CompositionOffsetEntry {     var sampleCount: Int32     var displayOffset: TimeValue     init()     init(sampleCount sampleCount: Int32, displayOffset displayOffset: TimeValue) } ``` |

Modified CompositionShiftLeastGreatestAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CompositionShiftLeastGreatestAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var compositionOffsetToDTDDeltaShift: Int32     var leastDecodeToDisplayDelta: Int32     var greatestDecodeToDisplayDelta: Int32     var displayStartTime: Int32     var displayEndTime: Int32 } ``` |
| To | ``` struct CompositionShiftLeastGreatestAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var compositionOffsetToDTDDeltaShift: Int32     var leastDecodeToDisplayDelta: Int32     var greatestDecodeToDisplayDelta: Int32     var displayStartTime: Int32     var displayEndTime: Int32     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, compositionOffsetToDTDDeltaShift compositionOffsetToDTDDeltaShift: Int32, leastDecodeToDisplayDelta leastDecodeToDisplayDelta: Int32, greatestDecodeToDisplayDelta greatestDecodeToDisplayDelta: Int32, displayStartTime displayStartTime: Int32, displayEndTime displayEndTime: Int32) } ``` |

Modified DataInfoAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DataInfoAtom {     var size: Int32     var atomType: Int32     var dataRef: DataRefAtom } ``` |
| To | ``` struct DataInfoAtom {     var size: Int32     var atomType: Int32     var dataRef: DataRefAtom     init()     init(size size: Int32, atomType atomType: Int32, dataRef dataRef: DataRefAtom) } ``` |

Modified EditListAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EditListAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var editListTable: (EditListType) } ``` |
| To | ``` struct EditListAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var editListTable: (EditListType)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, editListTable editListTable: (EditListType)) } ``` |

Modified EditListType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EditListType {     var trackDuration: TimeValue     var mediaTime: TimeValue     var mediaRate: Fixed } ``` |
| To | ``` struct EditListType {     var trackDuration: TimeValue     var mediaTime: TimeValue     var mediaRate: Fixed     init()     init(trackDuration trackDuration: TimeValue, mediaTime mediaTime: TimeValue, mediaRate mediaRate: Fixed) } ``` |

Modified EditsAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EditsAtom {     var size: Int32     var atomType: Int32     var editList: EditListAtom } ``` |
| To | ``` struct EditsAtom {     var size: Int32     var atomType: Int32     var editList: EditListAtom     init()     init(size size: Int32, atomType atomType: Int32, editList editList: EditListAtom) } ``` |

Modified FileTypeAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FileTypeAtom {     var size: Int32     var atomType: Int32     var majorBrand: Int32     var minorVersion: Int32     var compatibleBrands: (Int32, Int32, Int32, Int32) } ``` |
| To | ``` struct FileTypeAtom {     var size: Int32     var atomType: Int32     var majorBrand: Int32     var minorVersion: Int32     var compatibleBrands: (Int32, Int32, Int32, Int32)     init()     init(size size: Int32, atomType atomType: Int32, majorBrand majorBrand: Int32, minorVersion minorVersion: Int32, compatibleBrands compatibleBrands: (Int32, Int32, Int32, Int32)) } ``` |

Modified HandlerAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HandlerAtom {     var size: Int32     var atomType: Int32     var hInfo: PublicHandlerInfo } ``` |
| To | ``` struct HandlerAtom {     var size: Int32     var atomType: Int32     var hInfo: PublicHandlerInfo     init()     init(size size: Int32, atomType atomType: Int32, hInfo hInfo: PublicHandlerInfo) } ``` |

Modified HiliteAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HiliteAtom {     var size: Int32     var atomType: Int32     var selStart: Int32     var selEnd: Int32 } ``` |
| To | ``` struct HiliteAtom {     var size: Int32     var atomType: Int32     var selStart: Int32     var selEnd: Int32     init()     init(size size: Int32, atomType atomType: Int32, selStart selStart: Int32, selEnd selEnd: Int32) } ``` |

Modified ImageDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ImageDescription {     var idSize: Int32     var cType: CodecType     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var version: Int16     var revisionLevel: Int16     var vendor: Int32     var temporalQuality: CodecQ     var spatialQuality: CodecQ     var width: Int16     var height: Int16     var hRes: Fixed     var vRes: Fixed     var dataSize: Int32     var frameCount: Int16     var name: Str31     var depth: Int16     var clutID: Int16 } ``` |
| To | ``` struct ImageDescription {     var idSize: Int32     var cType: CodecType     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var version: Int16     var revisionLevel: Int16     var vendor: Int32     var temporalQuality: CodecQ     var spatialQuality: CodecQ     var width: Int16     var height: Int16     var hRes: Fixed     var vRes: Fixed     var dataSize: Int32     var frameCount: Int16     var name: Str31     var depth: Int16     var clutID: Int16     init()     init(idSize idSize: Int32, cType cType: CodecType, resvd1 resvd1: Int32, resvd2 resvd2: Int16, dataRefIndex dataRefIndex: Int16, version version: Int16, revisionLevel revisionLevel: Int16, vendor vendor: Int32, temporalQuality temporalQuality: CodecQ, spatialQuality spatialQuality: CodecQ, width width: Int16, height height: Int16, hRes hRes: Fixed, vRes vRes: Fixed, dataSize dataSize: Int32, frameCount frameCount: Int16, name name: Str31, depth depth: Int16, clutID clutID: Int16) } ``` |

Modified KaraokeAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KaraokeAtom {     var numEntries: Int32     var karaokeEntries: (KaraokeRec) } ``` |
| To | ``` struct KaraokeAtom {     var numEntries: Int32     var karaokeEntries: (KaraokeRec)     init()     init(numEntries numEntries: Int32, karaokeEntries karaokeEntries: (KaraokeRec)) } ``` |

Modified KaraokeRec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KaraokeRec {     var timeVal: TimeValue     var beginHilite: Int16     var endHilite: Int16 } ``` |
| To | ``` struct KaraokeRec {     var timeVal: TimeValue     var beginHilite: Int16     var endHilite: Int16     init()     init(timeVal timeVal: TimeValue, beginHilite beginHilite: Int16, endHilite endHilite: Int16) } ``` |

Modified MatrixRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MatrixRecord {     var matrix: ((Fixed, Fixed, Fixed), (Fixed, Fixed, Fixed), (Fixed, Fixed, Fixed)) } ``` |
| To | ``` struct MatrixRecord {     var matrix: ((Fixed, Fixed, Fixed), (Fixed, Fixed, Fixed), (Fixed, Fixed, Fixed))     init()     init(matrix matrix: ((Fixed, Fixed, Fixed), (Fixed, Fixed, Fixed), (Fixed, Fixed, Fixed))) } ``` |

Modified MatteAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MatteAtom {     var size: Int32     var atomType: Int32     var aCompressedMatte: MatteCompressedAtom } ``` |
| To | ``` struct MatteAtom {     var size: Int32     var atomType: Int32     var aCompressedMatte: MatteCompressedAtom     init()     init(size size: Int32, atomType atomType: Int32, aCompressedMatte aCompressedMatte: MatteCompressedAtom) } ``` |

Modified MatteCompressedAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MatteCompressedAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var matteImageDescription: ImageDescription     var matteData: (Int8) } ``` |
| To | ``` struct MatteCompressedAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var matteImageDescription: ImageDescription     var matteData: (Int8)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, matteImageDescription matteImageDescription: ImageDescription, matteData matteData: (Int8)) } ``` |

Modified MediaDirectory [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MediaDirectory {     var size: Int32     var atomType: Int32     var mediaHeader: MediaHeaderAtom     var mediaHandler: HandlerAtom     var mediaInfo: MediaInfo } ``` |
| To | ``` struct MediaDirectory {     var size: Int32     var atomType: Int32     var mediaHeader: MediaHeaderAtom     var mediaHandler: HandlerAtom     var mediaInfo: MediaInfo     init()     init(size size: Int32, atomType atomType: Int32, mediaHeader mediaHeader: MediaHeaderAtom, mediaHandler mediaHandler: HandlerAtom, mediaInfo mediaInfo: MediaInfo) } ``` |

Modified MediaHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MediaHeader {     var flags: Int32     var creationTime: Int32     var modificationTime: Int32     var timeScale: TimeValue     var duration: TimeValue     var language: Int16     var quality: Int16 } ``` |
| To | ``` struct MediaHeader {     var flags: Int32     var creationTime: Int32     var modificationTime: Int32     var timeScale: TimeValue     var duration: TimeValue     var language: Int16     var quality: Int16     init()     init(flags flags: Int32, creationTime creationTime: Int32, modificationTime modificationTime: Int32, timeScale timeScale: TimeValue, duration duration: TimeValue, language language: Int16, quality quality: Int16) } ``` |

Modified MediaHeaderAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MediaHeaderAtom {     var size: Int32     var atomType: Int32     var header: MediaHeader } ``` |
| To | ``` struct MediaHeaderAtom {     var size: Int32     var atomType: Int32     var header: MediaHeader     init()     init(size size: Int32, atomType atomType: Int32, header header: MediaHeader) } ``` |

Modified MediaInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MediaInfo {     var size: Int32     var atomType: Int32 } ``` |
| To | ``` struct MediaInfo {     var size: Int32     var atomType: Int32     init()     init(size size: Int32, atomType atomType: Int32) } ``` |

Modified MovieDirectory [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MovieDirectory {     var size: Int32     var atomType: Int32     var header: MovieHeaderAtom     var movieClip: ClippingAtom     var track: (TrackDirectoryEntry)     var userData: UserDataAtom } ``` |
| To | ``` struct MovieDirectory {     var size: Int32     var atomType: Int32     var header: MovieHeaderAtom     var movieClip: ClippingAtom     var track: (TrackDirectoryEntry)     var userData: UserDataAtom     init()     init(size size: Int32, atomType atomType: Int32, header header: MovieHeaderAtom, movieClip movieClip: ClippingAtom, track track: (TrackDirectoryEntry), userData userData: UserDataAtom) } ``` |

Modified MovieHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MovieHeader {     var flags: Int32     var creationTime: Int32     var modificationTime: Int32     var timeScale: TimeValue     var duration: TimeValue     var preferredRate: Fixed     var preferredVolume: Int16     var reserved1: Int16     var preferredLong1: Int32     var preferredLong2: Int32     var matrix: MatrixRecord     var previewTime: TimeValue     var previewDuration: TimeValue     var posterTime: TimeValue     var selectionTime: TimeValue     var selectionDuration: TimeValue     var currentTime: TimeValue     var nextTrackID: Int32 } ``` |
| To | ``` struct MovieHeader {     var flags: Int32     var creationTime: Int32     var modificationTime: Int32     var timeScale: TimeValue     var duration: TimeValue     var preferredRate: Fixed     var preferredVolume: Int16     var reserved1: Int16     var preferredLong1: Int32     var preferredLong2: Int32     var matrix: MatrixRecord     var previewTime: TimeValue     var previewDuration: TimeValue     var posterTime: TimeValue     var selectionTime: TimeValue     var selectionDuration: TimeValue     var currentTime: TimeValue     var nextTrackID: Int32     init()     init(flags flags: Int32, creationTime creationTime: Int32, modificationTime modificationTime: Int32, timeScale timeScale: TimeValue, duration duration: TimeValue, preferredRate preferredRate: Fixed, preferredVolume preferredVolume: Int16, reserved1 reserved1: Int16, preferredLong1 preferredLong1: Int32, preferredLong2 preferredLong2: Int32, matrix matrix: MatrixRecord, previewTime previewTime: TimeValue, previewDuration previewDuration: TimeValue, posterTime posterTime: TimeValue, selectionTime selectionTime: TimeValue, selectionDuration selectionDuration: TimeValue, currentTime currentTime: TimeValue, nextTrackID nextTrackID: Int32) } ``` |

Modified MovieHeaderAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MovieHeaderAtom {     var size: Int32     var atomType: Int32     var header: MovieHeader } ``` |
| To | ``` struct MovieHeaderAtom {     var size: Int32     var atomType: Int32     var header: MovieHeader     init()     init(size size: Int32, atomType atomType: Int32, header header: MovieHeader) } ``` |

Modified MoviesUserData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MoviesUserData {     var size: Int32     var udType: Int32     var data: (Int8) } ``` |
| To | ``` struct MoviesUserData {     var size: Int32     var udType: Int32     var data: (Int8)     init()     init(size size: Int32, udType udType: Int32, data data: (Int8)) } ``` |

Modified PartialSyncSampleAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PartialSyncSampleAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var partialSyncSampleTable: (UInt32) } ``` |
| To | ``` struct PartialSyncSampleAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var partialSyncSampleTable: (UInt32)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, partialSyncSampleTable partialSyncSampleTable: (UInt32)) } ``` |

Modified PublicHandlerInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PublicHandlerInfo {     var flags: Int32     var componentType: Int32     var componentSubType: Int32     var componentManufacturer: Int32     var componentFlags: Int32     var componentFlagsMask: Int32     var componentName: (Int8) } ``` |
| To | ``` struct PublicHandlerInfo {     var flags: Int32     var componentType: Int32     var componentSubType: Int32     var componentManufacturer: Int32     var componentFlags: Int32     var componentFlagsMask: Int32     var componentName: (Int8)     init()     init(flags flags: Int32, componentType componentType: Int32, componentSubType componentSubType: Int32, componentManufacturer componentManufacturer: Int32, componentFlags componentFlags: Int32, componentFlagsMask componentFlagsMask: Int32, componentName componentName: (Int8)) } ``` |

Modified QTAltCPURatingRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTAltCPURatingRecord {     var flags: UInt32     var speed: UInt16 } ``` |
| To | ``` struct QTAltCPURatingRecord {     var flags: UInt32     var speed: UInt16     init()     init(flags flags: UInt32, speed speed: UInt16) } ``` |

Modified QTAltComponentCheckRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTAltComponentCheckRecord {     var flags: Int32     var cd: ComponentDescription     var minVersion: UInt32 } ``` |
| To | ``` struct QTAltComponentCheckRecord {     var flags: Int32     var cd: ComponentDescription     var minVersion: UInt32     init()     init(flags flags: Int32, cd cd: ComponentDescription, minVersion minVersion: UInt32) } ``` |

Modified QTAltDataRateRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTAltDataRateRecord {     var flags: Int32     var dataRate: Int32 } ``` |
| To | ``` struct QTAltDataRateRecord {     var flags: Int32     var dataRate: Int32     init()     init(flags flags: Int32, dataRate dataRate: Int32) } ``` |

Modified QTAltLanguageRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTAltLanguageRecord {     var flags: Int32     var language: Int16 } ``` |
| To | ``` struct QTAltLanguageRecord {     var flags: Int32     var language: Int16     init()     init(flags flags: Int32, language language: Int16) } ``` |

Modified QTAltVersionCheckRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTAltVersionCheckRecord {     var flags: Int32     var gestaltTag: OSType     var val1: UInt32     var val2: UInt32     var checkType: Int16 } ``` |
| To | ``` struct QTAltVersionCheckRecord {     var flags: Int32     var gestaltTag: OSType     var val1: UInt32     var val2: UInt32     var checkType: Int16     init()     init(flags flags: Int32, gestaltTag gestaltTag: OSType, val1 val1: UInt32, val2 val2: UInt32, checkType checkType: Int16) } ``` |

Modified QTRGBColor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTRGBColor {     var red: UInt16     var green: UInt16     var blue: UInt16 } ``` |
| To | ``` struct QTRGBColor {     var red: UInt16     var green: UInt16     var blue: UInt16     init()     init(red red: UInt16, green green: UInt16, blue blue: UInt16) } ``` |

Modified QTVRSampleDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QTVRSampleDescription {     var descSize: UInt32     var descType: UInt32     var reserved1: UInt32     var reserved2: UInt16     var dataRefIndex: UInt16     var data: UInt32 } ``` |
| To | ``` struct QTVRSampleDescription {     var descSize: UInt32     var descType: UInt32     var reserved1: UInt32     var reserved2: UInt16     var dataRefIndex: UInt16     var data: UInt32     init()     init(descSize descSize: UInt32, descType descType: UInt32, reserved1 reserved1: UInt32, reserved2 reserved2: UInt16, dataRefIndex dataRefIndex: UInt16, data data: UInt32) } ``` |

Modified ReferenceMovieDataRefRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ReferenceMovieDataRefRecord {     var flags: Int32     var dataRefType: OSType     var dataRefSize: Int32     var dataRef: (Int8) } ``` |
| To | ``` struct ReferenceMovieDataRefRecord {     var flags: Int32     var dataRefType: OSType     var dataRefSize: Int32     var dataRef: (Int8)     init()     init(flags flags: Int32, dataRefType dataRefType: OSType, dataRefSize dataRefSize: Int32, dataRef dataRef: (Int8)) } ``` |

Modified ReferenceMovieNetworkStatusRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ReferenceMovieNetworkStatusRecord {     var flags: UInt32     var valueCount: UInt32     var netStatusValues: (Int32) } ``` |
| To | ``` struct ReferenceMovieNetworkStatusRecord {     var flags: UInt32     var valueCount: UInt32     var netStatusValues: (Int32)     init()     init(flags flags: UInt32, valueCount valueCount: UInt32, netStatusValues netStatusValues: (Int32)) } ``` |

Modified RgnAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct RgnAtom {     var size: Int32     var atomType: Int32     var rgnSize: Int16     var rgnBBox: Rect     var data: (Int8) } ``` |
| To | ``` struct RgnAtom {     var size: Int32     var atomType: Int32     var rgnSize: Int16     var rgnBBox: Rect     var data: (Int8)     init()     init(size size: Int32, atomType atomType: Int32, rgnSize rgnSize: Int16, rgnBBox rgnBBox: Rect, data data: (Int8)) } ``` |

Modified SampleDependencyAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SampleDependencyAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var sampleDependencyTable: (UInt8) } ``` |
| To | ``` struct SampleDependencyAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var sampleDependencyTable: (UInt8)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, sampleDependencyTable sampleDependencyTable: (UInt8)) } ``` |

Modified SampleDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SampleDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16 } ``` |
| To | ``` struct SampleDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     init()     init(descSize descSize: Int32, dataFormat dataFormat: Int32, resvd1 resvd1: Int32, resvd2 resvd2: Int16, dataRefIndex dataRefIndex: Int16) } ``` |

Modified SampleDescriptionAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SampleDescriptionAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var sampleDescTable: (SampleDescription) } ``` |
| To | ``` struct SampleDescriptionAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var sampleDescTable: (SampleDescription)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, sampleDescTable sampleDescTable: (SampleDescription)) } ``` |

Modified SampleSizeAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SampleSizeAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var sampleSize: Int32     var numEntries: Int32     var sampleSizeTable: (Int32) } ``` |
| To | ``` struct SampleSizeAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var sampleSize: Int32     var numEntries: Int32     var sampleSizeTable: (Int32)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, sampleSize sampleSize: Int32, numEntries numEntries: Int32, sampleSizeTable sampleSizeTable: (Int32)) } ``` |

Modified SampleTableAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SampleTableAtom {     var size: Int32     var atomType: Int32     var sampleDescription: SampleDescriptionAtom     var timeToSampleNum: TimeToSampleNumAtom     var sampleToChunk: SampleToChunkAtom     var syncSample: SyncSampleAtom     var sampleSize: SampleSizeAtom     var chunkOffset: ChunkOffsetAtom     var shadowSync: ShadowSyncAtom } ``` |
| To | ``` struct SampleTableAtom {     var size: Int32     var atomType: Int32     var sampleDescription: SampleDescriptionAtom     var timeToSampleNum: TimeToSampleNumAtom     var sampleToChunk: SampleToChunkAtom     var syncSample: SyncSampleAtom     var sampleSize: SampleSizeAtom     var chunkOffset: ChunkOffsetAtom     var shadowSync: ShadowSyncAtom     init()     init(size size: Int32, atomType atomType: Int32, sampleDescription sampleDescription: SampleDescriptionAtom, timeToSampleNum timeToSampleNum: TimeToSampleNumAtom, sampleToChunk sampleToChunk: SampleToChunkAtom, syncSample syncSample: SyncSampleAtom, sampleSize sampleSize: SampleSizeAtom, chunkOffset chunkOffset: ChunkOffsetAtom, shadowSync shadowSync: ShadowSyncAtom) } ``` |

Modified SampleToChunk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SampleToChunk {     var firstChunk: Int32     var samplesPerChunk: Int32     var sampleDescriptionID: Int32 } ``` |
| To | ``` struct SampleToChunk {     var firstChunk: Int32     var samplesPerChunk: Int32     var sampleDescriptionID: Int32     init()     init(firstChunk firstChunk: Int32, samplesPerChunk samplesPerChunk: Int32, sampleDescriptionID sampleDescriptionID: Int32) } ``` |

Modified SampleToChunkAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SampleToChunkAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var sampleToChunkTable: (SampleToChunk) } ``` |
| To | ``` struct SampleToChunkAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var sampleToChunkTable: (SampleToChunk)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, sampleToChunkTable sampleToChunkTable: (SampleToChunk)) } ``` |

Modified SecureContentInfoAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecureContentInfoAtom {     var size: Int32     var atomType: Int32 } ``` |
| To | ``` struct SecureContentInfoAtom {     var size: Int32     var atomType: Int32     init()     init(size size: Int32, atomType atomType: Int32) } ``` |

Modified SecureContentSchemeInfoAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecureContentSchemeInfoAtom {     var size: Int32     var atomType: Int32 } ``` |
| To | ``` struct SecureContentSchemeInfoAtom {     var size: Int32     var atomType: Int32     init()     init(size size: Int32, atomType atomType: Int32) } ``` |

Modified SecureContentSchemeTypeAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecureContentSchemeTypeAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var schemeType: Int32     var schemeVersion: UInt32 } ``` |
| To | ``` struct SecureContentSchemeTypeAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var schemeType: Int32     var schemeVersion: UInt32     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, schemeType schemeType: Int32, schemeVersion schemeVersion: UInt32) } ``` |

Modified ShadowSync [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ShadowSync {     var fdSampleNum: Int32     var syncSampleNum: Int32 } ``` |
| To | ``` struct ShadowSync {     var fdSampleNum: Int32     var syncSampleNum: Int32     init()     init(fdSampleNum fdSampleNum: Int32, syncSampleNum syncSampleNum: Int32) } ``` |

Modified ShadowSyncAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ShadowSyncAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var shadowSyncTable: (ShadowSync) } ``` |
| To | ``` struct ShadowSyncAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var shadowSyncTable: (ShadowSync)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, shadowSyncTable shadowSyncTable: (ShadowSync)) } ``` |

Modified SoundDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SoundDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var version: Int16     var revlevel: Int16     var vendor: Int32     var numChannels: Int16     var sampleSize: Int16     var compressionID: Int16     var packetSize: Int16     var sampleRate: UnsignedFixed } ``` |
| To | ``` struct SoundDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var version: Int16     var revlevel: Int16     var vendor: Int32     var numChannels: Int16     var sampleSize: Int16     var compressionID: Int16     var packetSize: Int16     var sampleRate: UnsignedFixed     init()     init(descSize descSize: Int32, dataFormat dataFormat: Int32, resvd1 resvd1: Int32, resvd2 resvd2: Int16, dataRefIndex dataRefIndex: Int16, version version: Int16, revlevel revlevel: Int16, vendor vendor: Int32, numChannels numChannels: Int16, sampleSize sampleSize: Int16, compressionID compressionID: Int16, packetSize packetSize: Int16, sampleRate sampleRate: UnsignedFixed) } ``` |

Modified SoundDescriptionV1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SoundDescriptionV1 {     var desc: SoundDescription     var samplesPerPacket: UInt32     var bytesPerPacket: UInt32     var bytesPerFrame: UInt32     var bytesPerSample: UInt32 } ``` |
| To | ``` struct SoundDescriptionV1 {     var desc: SoundDescription     var samplesPerPacket: UInt32     var bytesPerPacket: UInt32     var bytesPerFrame: UInt32     var bytesPerSample: UInt32     init()     init(desc desc: SoundDescription, samplesPerPacket samplesPerPacket: UInt32, bytesPerPacket bytesPerPacket: UInt32, bytesPerFrame bytesPerFrame: UInt32, bytesPerSample bytesPerSample: UInt32) } ``` |

Modified SoundDescriptionV2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SoundDescriptionV2 {     var descSize: Int32     var dataFormat: OSType     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var version: Int16     var revlevel: Int16     var vendor: Int32     var always3: Int16     var always16: Int16     var alwaysMinus2: Int16     var always0: Int16     var always65536: UInt32     var sizeOfStructOnly: UInt32     var audioSampleRate: Float64     var numAudioChannels: UInt32     var always7F000000: Int32     var constBitsPerChannel: UInt32     var formatSpecificFlags: UInt32     var constBytesPerAudioPacket: UInt32     var constLPCMFramesPerAudioPacket: UInt32 } ``` |
| To | ``` struct SoundDescriptionV2 {     var descSize: Int32     var dataFormat: OSType     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var version: Int16     var revlevel: Int16     var vendor: Int32     var always3: Int16     var always16: Int16     var alwaysMinus2: Int16     var always0: Int16     var always65536: UInt32     var sizeOfStructOnly: UInt32     var audioSampleRate: Float64     var numAudioChannels: UInt32     var always7F000000: Int32     var constBitsPerChannel: UInt32     var formatSpecificFlags: UInt32     var constBytesPerAudioPacket: UInt32     var constLPCMFramesPerAudioPacket: UInt32     init()     init(descSize descSize: Int32, dataFormat dataFormat: OSType, resvd1 resvd1: Int32, resvd2 resvd2: Int16, dataRefIndex dataRefIndex: Int16, version version: Int16, revlevel revlevel: Int16, vendor vendor: Int32, always3 always3: Int16, always16 always16: Int16, alwaysMinus2 alwaysMinus2: Int16, always0 always0: Int16, always65536 always65536: UInt32, sizeOfStructOnly sizeOfStructOnly: UInt32, audioSampleRate audioSampleRate: Float64, numAudioChannels numAudioChannels: UInt32, always7F000000 always7F000000: Int32, constBitsPerChannel constBitsPerChannel: UInt32, formatSpecificFlags formatSpecificFlags: UInt32, constBytesPerAudioPacket constBytesPerAudioPacket: UInt32, constLPCMFramesPerAudioPacket constLPCMFramesPerAudioPacket: UInt32) } ``` |

Modified SoundMediaInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SoundMediaInfo {     var size: Int32     var atomType: Int32     var header: SoundMediaInfoHeaderAtom     var dataHandler: HandlerAtom     var dataReference: DataRefAtom     var sampleTable: SampleTableAtom } ``` |
| To | ``` struct SoundMediaInfo {     var size: Int32     var atomType: Int32     var header: SoundMediaInfoHeaderAtom     var dataHandler: HandlerAtom     var dataReference: DataRefAtom     var sampleTable: SampleTableAtom     init()     init(size size: Int32, atomType atomType: Int32, header header: SoundMediaInfoHeaderAtom, dataHandler dataHandler: HandlerAtom, dataReference dataReference: DataRefAtom, sampleTable sampleTable: SampleTableAtom) } ``` |

Modified SoundMediaInfoHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SoundMediaInfoHeader {     var flags: Int32     var balance: Int16     var rsrvd: Int16 } ``` |
| To | ``` struct SoundMediaInfoHeader {     var flags: Int32     var balance: Int16     var rsrvd: Int16     init()     init(flags flags: Int32, balance balance: Int16, rsrvd rsrvd: Int16) } ``` |

Modified SoundMediaInfoHeaderAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SoundMediaInfoHeaderAtom {     var size: Int32     var atomType: Int32     var smiHeader: SoundMediaInfoHeader } ``` |
| To | ``` struct SoundMediaInfoHeaderAtom {     var size: Int32     var atomType: Int32     var smiHeader: SoundMediaInfoHeader     init()     init(size size: Int32, atomType atomType: Int32, smiHeader smiHeader: SoundMediaInfoHeader) } ``` |

Modified SyncSampleAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SyncSampleAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var syncSampleTable: (Int32) } ``` |
| To | ``` struct SyncSampleAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var syncSampleTable: (Int32)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, syncSampleTable syncSampleTable: (Int32)) } ``` |

Modified TextBoxAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TextBoxAtom {     var size: Int32     var atomType: Int32     var textBox: Rect } ``` |
| To | ``` struct TextBoxAtom {     var size: Int32     var atomType: Int32     var textBox: Rect     init()     init(size size: Int32, atomType atomType: Int32, textBox textBox: Rect) } ``` |

Modified TextDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TextDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var displayFlags: Int32     var textJustification: Int32     var bgColor: QTRGBColor     var defaultTextBox: Rect     var defaultStyle: ScrpSTElement     var defaultFontName: (Int8) } ``` |
| To | ``` struct TextDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var displayFlags: Int32     var textJustification: Int32     var bgColor: QTRGBColor     var defaultTextBox: Rect     var defaultStyle: ScrpSTElement     var defaultFontName: (Int8)     init()     init(descSize descSize: Int32, dataFormat dataFormat: Int32, resvd1 resvd1: Int32, resvd2 resvd2: Int16, dataRefIndex dataRefIndex: Int16, displayFlags displayFlags: Int32, textJustification textJustification: Int32, bgColor bgColor: QTRGBColor, defaultTextBox defaultTextBox: Rect, defaultStyle defaultStyle: ScrpSTElement, defaultFontName defaultFontName: (Int8)) } ``` |

Modified TimeCodeDef [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TimeCodeDef {     var flags: Int32     var fTimeScale: TimeScale     var frameDuration: TimeValue     var numFrames: UInt8     var padding: UInt8 } ``` |
| To | ``` struct TimeCodeDef {     var flags: Int32     var fTimeScale: TimeScale     var frameDuration: TimeValue     var numFrames: UInt8     var padding: UInt8     init()     init(flags flags: Int32, fTimeScale fTimeScale: TimeScale, frameDuration frameDuration: TimeValue, numFrames numFrames: UInt8, padding padding: UInt8) } ``` |

Modified TimeCodeDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TimeCodeDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var flags: Int32     var timeCodeDef: TimeCodeDef     var srcRef: (Int32) } ``` |
| To | ``` struct TimeCodeDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var flags: Int32     var timeCodeDef: TimeCodeDef     var srcRef: (Int32)     init()     init(descSize descSize: Int32, dataFormat dataFormat: Int32, resvd1 resvd1: Int32, resvd2 resvd2: Int16, dataRefIndex dataRefIndex: Int16, flags flags: Int32, timeCodeDef timeCodeDef: TimeCodeDef, srcRef srcRef: (Int32)) } ``` |

Modified TimeToSampleNum [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TimeToSampleNum {     var sampleCount: Int32     var sampleDuration: TimeValue } ``` |
| To | ``` struct TimeToSampleNum {     var sampleCount: Int32     var sampleDuration: TimeValue     init()     init(sampleCount sampleCount: Int32, sampleDuration sampleDuration: TimeValue) } ``` |

Modified TimeToSampleNumAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TimeToSampleNumAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var timeToSampleNumTable: (TimeToSampleNum) } ``` |
| To | ``` struct TimeToSampleNumAtom {     var size: Int32     var atomType: Int32     var flags: Int32     var numEntries: Int32     var timeToSampleNumTable: (TimeToSampleNum)     init()     init(size size: Int32, atomType atomType: Int32, flags flags: Int32, numEntries numEntries: Int32, timeToSampleNumTable timeToSampleNumTable: (TimeToSampleNum)) } ``` |

Modified TrackCleanApertureDimensions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackCleanApertureDimensions {     var flags: Int32     var cleanApertureDimensions: FixedPoint } ``` |
| To | ``` struct TrackCleanApertureDimensions {     var flags: Int32     var cleanApertureDimensions: FixedPoint     init()     init(flags flags: Int32, cleanApertureDimensions cleanApertureDimensions: FixedPoint) } ``` |

Modified TrackCleanApertureDimensionsAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackCleanApertureDimensionsAtom {     var size: Int32     var atomType: Int32     var cleanApertureDimensions: TrackCleanApertureDimensions } ``` |
| To | ``` struct TrackCleanApertureDimensionsAtom {     var size: Int32     var atomType: Int32     var cleanApertureDimensions: TrackCleanApertureDimensions     init()     init(size size: Int32, atomType atomType: Int32, cleanApertureDimensions cleanApertureDimensions: TrackCleanApertureDimensions) } ``` |

Modified TrackDirectory [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackDirectory {     var size: Int32     var atomType: Int32     var trackHeader: TrackHeaderAtom     var trackClip: ClippingAtom     var edits: EditsAtom     var media: MediaDirectory     var userData: UserDataAtom } ``` |
| To | ``` struct TrackDirectory {     var size: Int32     var atomType: Int32     var trackHeader: TrackHeaderAtom     var trackClip: ClippingAtom     var edits: EditsAtom     var media: MediaDirectory     var userData: UserDataAtom     init()     init(size size: Int32, atomType atomType: Int32, trackHeader trackHeader: TrackHeaderAtom, trackClip trackClip: ClippingAtom, edits edits: EditsAtom, media media: MediaDirectory, userData userData: UserDataAtom) } ``` |

Modified TrackDirectoryEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackDirectoryEntry {     var trackDirectory: TrackDirectory } ``` |
| To | ``` struct TrackDirectoryEntry {     var trackDirectory: TrackDirectory     init()     init(trackDirectory trackDirectory: TrackDirectory) } ``` |

Modified TrackEncodedPixelsDimensions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackEncodedPixelsDimensions {     var flags: Int32     var encodedPixelsDimensions: FixedPoint } ``` |
| To | ``` struct TrackEncodedPixelsDimensions {     var flags: Int32     var encodedPixelsDimensions: FixedPoint     init()     init(flags flags: Int32, encodedPixelsDimensions encodedPixelsDimensions: FixedPoint) } ``` |

Modified TrackEncodedPixelsDimensionsAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackEncodedPixelsDimensionsAtom {     var size: Int32     var atomType: Int32     var encodedPixelsDimensions: TrackEncodedPixelsDimensions } ``` |
| To | ``` struct TrackEncodedPixelsDimensionsAtom {     var size: Int32     var atomType: Int32     var encodedPixelsDimensions: TrackEncodedPixelsDimensions     init()     init(size size: Int32, atomType atomType: Int32, encodedPixelsDimensions encodedPixelsDimensions: TrackEncodedPixelsDimensions) } ``` |

Modified TrackHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackHeader {     var flags: Int32     var creationTime: Int32     var modificationTime: Int32     var trackID: Int32     var reserved1: Int32     var duration: TimeValue     var reserved2: Int32     var reserved3: Int32     var layer: Int16     var alternateGroup: Int16     var volume: Int16     var reserved4: Int16     var matrix: MatrixRecord     var trackWidth: Fixed     var trackHeight: Fixed } ``` |
| To | ``` struct TrackHeader {     var flags: Int32     var creationTime: Int32     var modificationTime: Int32     var trackID: Int32     var reserved1: Int32     var duration: TimeValue     var reserved2: Int32     var reserved3: Int32     var layer: Int16     var alternateGroup: Int16     var volume: Int16     var reserved4: Int16     var matrix: MatrixRecord     var trackWidth: Fixed     var trackHeight: Fixed     init()     init(flags flags: Int32, creationTime creationTime: Int32, modificationTime modificationTime: Int32, trackID trackID: Int32, reserved1 reserved1: Int32, duration duration: TimeValue, reserved2 reserved2: Int32, reserved3 reserved3: Int32, layer layer: Int16, alternateGroup alternateGroup: Int16, volume volume: Int16, reserved4 reserved4: Int16, matrix matrix: MatrixRecord, trackWidth trackWidth: Fixed, trackHeight trackHeight: Fixed) } ``` |

Modified TrackHeaderAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackHeaderAtom {     var size: Int32     var atomType: Int32     var header: TrackHeader } ``` |
| To | ``` struct TrackHeaderAtom {     var size: Int32     var atomType: Int32     var header: TrackHeader     init()     init(size size: Int32, atomType atomType: Int32, header header: TrackHeader) } ``` |

Modified TrackLoadSettings [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackLoadSettings {     var preloadStartTime: TimeValue     var preloadDuration: TimeValue     var preloadFlags: Int32     var defaultHints: Int32 } ``` |
| To | ``` struct TrackLoadSettings {     var preloadStartTime: TimeValue     var preloadDuration: TimeValue     var preloadFlags: Int32     var defaultHints: Int32     init()     init(preloadStartTime preloadStartTime: TimeValue, preloadDuration preloadDuration: TimeValue, preloadFlags preloadFlags: Int32, defaultHints defaultHints: Int32) } ``` |

Modified TrackLoadSettingsAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackLoadSettingsAtom {     var size: Int32     var atomType: Int32     var settings: TrackLoadSettings } ``` |
| To | ``` struct TrackLoadSettingsAtom {     var size: Int32     var atomType: Int32     var settings: TrackLoadSettings     init()     init(size size: Int32, atomType atomType: Int32, settings settings: TrackLoadSettings) } ``` |

Modified TrackProductionApertureDimensions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackProductionApertureDimensions {     var flags: Int32     var productionApertureDimensions: FixedPoint } ``` |
| To | ``` struct TrackProductionApertureDimensions {     var flags: Int32     var productionApertureDimensions: FixedPoint     init()     init(flags flags: Int32, productionApertureDimensions productionApertureDimensions: FixedPoint) } ``` |

Modified TrackProductionApertureDimensionsAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct TrackProductionApertureDimensionsAtom {     var size: Int32     var atomType: Int32     var productionApertureDimensions: TrackProductionApertureDimensions } ``` |
| To | ``` struct TrackProductionApertureDimensionsAtom {     var size: Int32     var atomType: Int32     var productionApertureDimensions: TrackProductionApertureDimensions     init()     init(size size: Int32, atomType atomType: Int32, productionApertureDimensions productionApertureDimensions: TrackProductionApertureDimensions) } ``` |

Modified Tx3gDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tx3gDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var displayFlags: UInt32     var horizontalJustification: Int8     var verticalJustification: Int8     var backgroundColor: Tx3gRGBAColor     var defaultTextBox: Rect     var defaultStyle: Tx3gStyleRecord } ``` |
| To | ``` struct Tx3gDescription {     var descSize: Int32     var dataFormat: Int32     var resvd1: Int32     var resvd2: Int16     var dataRefIndex: Int16     var displayFlags: UInt32     var horizontalJustification: Int8     var verticalJustification: Int8     var backgroundColor: Tx3gRGBAColor     var defaultTextBox: Rect     var defaultStyle: Tx3gStyleRecord     init()     init(descSize descSize: Int32, dataFormat dataFormat: Int32, resvd1 resvd1: Int32, resvd2 resvd2: Int16, dataRefIndex dataRefIndex: Int16, displayFlags displayFlags: UInt32, horizontalJustification horizontalJustification: Int8, verticalJustification verticalJustification: Int8, backgroundColor backgroundColor: Tx3gRGBAColor, defaultTextBox defaultTextBox: Rect, defaultStyle defaultStyle: Tx3gStyleRecord) } ``` |

Modified Tx3gFontRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tx3gFontRecord {     var fontID: UInt16     var nameLength: UInt8     var name: (UInt8) } ``` |
| To | ``` struct Tx3gFontRecord {     var fontID: UInt16     var nameLength: UInt8     var name: (UInt8)     init()     init(fontID fontID: UInt16, nameLength nameLength: UInt8, name name: (UInt8)) } ``` |

Modified Tx3gFontTableRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tx3gFontTableRecord {     var entryCount: UInt16     var fontEntries: (Tx3gFontRecord) } ``` |
| To | ``` struct Tx3gFontTableRecord {     var entryCount: UInt16     var fontEntries: (Tx3gFontRecord)     init()     init(entryCount entryCount: UInt16, fontEntries fontEntries: (Tx3gFontRecord)) } ``` |

Modified Tx3gRGBAColor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tx3gRGBAColor {     var red: UInt8     var green: UInt8     var blue: UInt8     var transparency: UInt8 } ``` |
| To | ``` struct Tx3gRGBAColor {     var red: UInt8     var green: UInt8     var blue: UInt8     var transparency: UInt8     init()     init(red red: UInt8, green green: UInt8, blue blue: UInt8, transparency transparency: UInt8) } ``` |

Modified Tx3gStyleRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tx3gStyleRecord {     var startChar: UInt16     var endChar: UInt16     var fontID: UInt16     var fontFace: UInt8     var fontSize: UInt8     var fontColor: Tx3gRGBAColor } ``` |
| To | ``` struct Tx3gStyleRecord {     var startChar: UInt16     var endChar: UInt16     var fontID: UInt16     var fontFace: UInt8     var fontSize: UInt8     var fontColor: Tx3gRGBAColor     init()     init(startChar startChar: UInt16, endChar endChar: UInt16, fontID fontID: UInt16, fontFace fontFace: UInt8, fontSize fontSize: UInt8, fontColor fontColor: Tx3gRGBAColor) } ``` |

Modified Tx3gStyleTableRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Tx3gStyleTableRecord {     var count: UInt16     var table: (Tx3gStyleRecord) } ``` |
| To | ``` struct Tx3gStyleTableRecord {     var count: UInt16     var table: (Tx3gStyleRecord)     init()     init(count count: UInt16, table table: (Tx3gStyleRecord)) } ``` |

Modified UserDataAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UserDataAtom {     var size: Int32     var atomType: Int32     var userData: (MoviesUserData) } ``` |
| To | ``` struct UserDataAtom {     var size: Int32     var atomType: Int32     var userData: (MoviesUserData)     init()     init(size size: Int32, atomType atomType: Int32, userData userData: (MoviesUserData)) } ``` |

Modified VideoMediaInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VideoMediaInfo {     var size: Int32     var atomType: Int32     var header: VideoMediaInfoHeaderAtom     var dataHandler: HandlerAtom     var dataInfo: DataInfoAtom     var sampleTable: SampleTableAtom } ``` |
| To | ``` struct VideoMediaInfo {     var size: Int32     var atomType: Int32     var header: VideoMediaInfoHeaderAtom     var dataHandler: HandlerAtom     var dataInfo: DataInfoAtom     var sampleTable: SampleTableAtom     init()     init(size size: Int32, atomType atomType: Int32, header header: VideoMediaInfoHeaderAtom, dataHandler dataHandler: HandlerAtom, dataInfo dataInfo: DataInfoAtom, sampleTable sampleTable: SampleTableAtom) } ``` |

Modified VideoMediaInfoHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VideoMediaInfoHeader {     var flags: Int32     var graphicsMode: Int16     var opColorRed: Int16     var opColorGreen: Int16     var opColorBlue: Int16 } ``` |
| To | ``` struct VideoMediaInfoHeader {     var flags: Int32     var graphicsMode: Int16     var opColorRed: Int16     var opColorGreen: Int16     var opColorBlue: Int16     init()     init(flags flags: Int32, graphicsMode graphicsMode: Int16, opColorRed opColorRed: Int16, opColorGreen opColorGreen: Int16, opColorBlue opColorBlue: Int16) } ``` |

Modified VideoMediaInfoHeaderAtom [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VideoMediaInfoHeaderAtom {     var size: Int32     var atomType: Int32     var vmiHeader: VideoMediaInfoHeader } ``` |
| To | ``` struct VideoMediaInfoHeaderAtom {     var size: Int32     var atomType: Int32     var vmiHeader: VideoMediaInfoHeader     init()     init(size size: Int32, atomType atomType: Int32, vmiHeader vmiHeader: VideoMediaInfoHeader) } ``` |

Modified ImageDescriptionHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias ImageDescriptionHandle = UnsafePointer<ImageDescriptionPtr> ``` |
| To | ``` typealias ImageDescriptionHandle = UnsafeMutablePointer<ImageDescriptionPtr> ``` |

Modified ImageDescriptionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias ImageDescriptionPtr = UnsafePointer<ImageDescription> ``` |
| To | ``` typealias ImageDescriptionPtr = UnsafeMutablePointer<ImageDescription> ``` |

Modified MatrixRecordPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias MatrixRecordPtr = UnsafePointer<MatrixRecord> ``` |
| To | ``` typealias MatrixRecordPtr = UnsafeMutablePointer<MatrixRecord> ``` |

Modified QTVRSampleDescriptionHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias QTVRSampleDescriptionHandle = UnsafePointer<QTVRSampleDescriptionPtr> ``` |
| To | ``` typealias QTVRSampleDescriptionHandle = UnsafeMutablePointer<QTVRSampleDescriptionPtr> ``` |

Modified QTVRSampleDescriptionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias QTVRSampleDescriptionPtr = UnsafePointer<QTVRSampleDescription> ``` |
| To | ``` typealias QTVRSampleDescriptionPtr = UnsafeMutablePointer<QTVRSampleDescription> ``` |

Modified SampleDescriptionHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias SampleDescriptionHandle = UnsafePointer<SampleDescriptionPtr> ``` |
| To | ``` typealias SampleDescriptionHandle = UnsafeMutablePointer<SampleDescriptionPtr> ``` |

Modified SampleDescriptionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias SampleDescriptionPtr = UnsafePointer<SampleDescription> ``` |
| To | ``` typealias SampleDescriptionPtr = UnsafeMutablePointer<SampleDescription> ``` |

Modified SoundDescriptionHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias SoundDescriptionHandle = UnsafePointer<SoundDescriptionPtr> ``` |
| To | ``` typealias SoundDescriptionHandle = UnsafeMutablePointer<SoundDescriptionPtr> ``` |

Modified SoundDescriptionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias SoundDescriptionPtr = UnsafePointer<SoundDescription> ``` |
| To | ``` typealias SoundDescriptionPtr = UnsafeMutablePointer<SoundDescription> ``` |

Modified SoundDescriptionV1Handle

|  | Declaration |
| --- | --- |
| From | ``` typealias SoundDescriptionV1Handle = UnsafePointer<SoundDescriptionV1Ptr> ``` |
| To | ``` typealias SoundDescriptionV1Handle = UnsafeMutablePointer<SoundDescriptionV1Ptr> ``` |

Modified SoundDescriptionV1Ptr

|  | Declaration |
| --- | --- |
| From | ``` typealias SoundDescriptionV1Ptr = UnsafePointer<SoundDescriptionV1> ``` |
| To | ``` typealias SoundDescriptionV1Ptr = UnsafeMutablePointer<SoundDescriptionV1> ``` |

Modified SoundDescriptionV2Handle

|  | Declaration |
| --- | --- |
| From | ``` typealias SoundDescriptionV2Handle = UnsafePointer<SoundDescriptionV2Ptr> ``` |
| To | ``` typealias SoundDescriptionV2Handle = UnsafeMutablePointer<SoundDescriptionV2Ptr> ``` |

Modified SoundDescriptionV2Ptr

|  | Declaration |
| --- | --- |
| From | ``` typealias SoundDescriptionV2Ptr = UnsafePointer<SoundDescriptionV2> ``` |
| To | ``` typealias SoundDescriptionV2Ptr = UnsafeMutablePointer<SoundDescriptionV2> ``` |

Modified TextDescriptionHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias TextDescriptionHandle = UnsafePointer<TextDescriptionPtr> ``` |
| To | ``` typealias TextDescriptionHandle = UnsafeMutablePointer<TextDescriptionPtr> ``` |

Modified TextDescriptionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TextDescriptionPtr = UnsafePointer<TextDescription> ``` |
| To | ``` typealias TextDescriptionPtr = UnsafeMutablePointer<TextDescription> ``` |

Modified TimeCodeDescriptionHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias TimeCodeDescriptionHandle = UnsafePointer<TimeCodeDescriptionPtr> ``` |
| To | ``` typealias TimeCodeDescriptionHandle = UnsafeMutablePointer<TimeCodeDescriptionPtr> ``` |

Modified TimeCodeDescriptionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias TimeCodeDescriptionPtr = UnsafePointer<TimeCodeDescription> ``` |
| To | ``` typealias TimeCodeDescriptionPtr = UnsafeMutablePointer<TimeCodeDescription> ``` |

Modified Tx3gDescriptionHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gDescriptionHandle = UnsafePointer<Tx3gDescriptionPtr> ``` |
| To | ``` typealias Tx3gDescriptionHandle = UnsafeMutablePointer<Tx3gDescriptionPtr> ``` |

Modified Tx3gDescriptionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gDescriptionPtr = UnsafePointer<Tx3gDescription> ``` |
| To | ``` typealias Tx3gDescriptionPtr = UnsafeMutablePointer<Tx3gDescription> ``` |

Modified Tx3gFontRecordPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gFontRecordPtr = UnsafePointer<Tx3gFontRecord> ``` |
| To | ``` typealias Tx3gFontRecordPtr = UnsafeMutablePointer<Tx3gFontRecord> ``` |

Modified Tx3gFontTableHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gFontTableHandle = UnsafePointer<Tx3gFontTablePtr> ``` |
| To | ``` typealias Tx3gFontTableHandle = UnsafeMutablePointer<Tx3gFontTablePtr> ``` |

Modified Tx3gFontTablePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gFontTablePtr = UnsafePointer<Tx3gFontTableRecord> ``` |
| To | ``` typealias Tx3gFontTablePtr = UnsafeMutablePointer<Tx3gFontTableRecord> ``` |

Modified Tx3gStyleHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gStyleHandle = UnsafePointer<Tx3gStylePtr> ``` |
| To | ``` typealias Tx3gStyleHandle = UnsafeMutablePointer<Tx3gStylePtr> ``` |

Modified Tx3gStylePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gStylePtr = UnsafePointer<Tx3gStyleRecord> ``` |
| To | ``` typealias Tx3gStylePtr = UnsafeMutablePointer<Tx3gStyleRecord> ``` |

Modified Tx3gStyleTableHandle

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gStyleTableHandle = UnsafePointer<Tx3gStyleTablePtr> ``` |
| To | ``` typealias Tx3gStyleTableHandle = UnsafeMutablePointer<Tx3gStyleTablePtr> ``` |

Modified Tx3gStyleTablePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias Tx3gStyleTablePtr = UnsafePointer<Tx3gStyleTableRecord> ``` |
| To | ``` typealias Tx3gStyleTablePtr = UnsafeMutablePointer<Tx3gStyleTableRecord> ``` |

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
