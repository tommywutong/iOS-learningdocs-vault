---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/AudioUnit.html
archived_at: '2026-07-18T02:56:21.872110Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# AudioUnit Changes

## AudioUnit

Added AUChannelInfo.init()Added AUChannelInfo.init(inChannels: Int16, outChannels: Int16)Added AUDependentParameter.init()Added AUDependentParameter.init(mScope: AudioUnitScope, mParameterID: AudioUnitParameterID)Added AUInputSamplesInOutputCallbackStruct.init()Added AUInputSamplesInOutputCallbackStruct.init(inputToOutputCallback: AUInputSamplesInOutputCallback, userData: UnsafeMutablePointer<Void>)Added AUPreset.init()Added AUPreset.init(presetNumber: Int32, presetName: Unmanaged<CFString>!)Added AURenderCallbackStruct.init()Added AURenderCallbackStruct.init(inputProc: AURenderCallback, inputProcRefCon: UnsafeMutablePointer<Void>)Added AUSamplerBankPresetData.init()Added AUSamplerBankPresetData.init(bankURL: Unmanaged<CFURL>!, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8, reserved: UInt8)Added AUSamplerInstrumentData.init()Added AUSamplerInstrumentData.init(fileURL: Unmanaged<CFURL>!, instrumentType: UInt8, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8)Added AudioComponentDescription.init()Added AudioComponentDescription.init(componentType: OSType, componentSubType: OSType, componentManufacturer: OSType, componentFlags: UInt32, componentFlagsMask: UInt32)Added AudioComponentPlugInInterface.init()Added AudioComponentPlugInInterface.init(Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>, Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>, Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>, reserved: UnsafeMutablePointer<Void>)Added AudioOutputUnitMIDICallbacks.init()Added AudioOutputUnitMIDICallbacks.init(userData: UnsafeMutablePointer<Void>, MIDIEventProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void)>, MIDISysExProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void)>)Added AudioOutputUnitStartAtTimeParams.init()Added AudioOutputUnitStartAtTimeParams.init(mTimestamp: AudioTimeStamp, mFlags: UInt32)Added AudioUnitConnection.init()Added AudioUnitConnection.init(sourceAudioUnit: AudioUnit, sourceOutputNumber: UInt32, destInputNumber: UInt32)Added AudioUnitExternalBuffer.init()Added AudioUnitExternalBuffer.init(buffer: UnsafeMutablePointer<UInt8>, size: UInt32)Added AudioUnitFrequencyResponseBin.init()Added AudioUnitFrequencyResponseBin.init(mFrequency: Float64, mMagnitude: Float64)Added AudioUnitMeterClipping.init()Added AudioUnitMeterClipping.init(peakValueSinceLastCall: Float32, sawInfinity: Boolean, sawNotANumber: Boolean)Added AudioUnitParameter.init()Added AudioUnitParameter.init(mAudioUnit: AudioUnit, mParameterID: AudioUnitParameterID, mScope: AudioUnitScope, mElement: AudioUnitElement)Added AudioUnitParameterEvent.init()Added AudioUnitParameterHistoryInfo.init()Added AudioUnitParameterHistoryInfo.init(updatesPerSecond: Float32, historyDurationInSeconds: Float32)Added AudioUnitParameterInfo.init()Added AudioUnitParameterInfo.init(name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName: Unmanaged<CFString>!, clumpID: UInt32, cfNameString: Unmanaged<CFString>!, unit: AudioUnitParameterUnit, minValue: AudioUnitParameterValue, maxValue: AudioUnitParameterValue, defaultValue: AudioUnitParameterValue, flags: UInt32)Added AudioUnitParameterNameInfo.init()Added AudioUnitParameterNameInfo.init(inID: AudioUnitParameterID, inDesiredLength: Int32, outName: Unmanaged<CFString>!)Added AudioUnitParameterStringFromValue.init()Added AudioUnitParameterStringFromValue.init(inParamID: AudioUnitParameterID, inValue: UnsafePointer<AudioUnitParameterValue>, outString: Unmanaged<CFString>!)Added AudioUnitParameterValueFromString.init()Added AudioUnitParameterValueFromString.init(inParamID: AudioUnitParameterID, inString: Unmanaged<CFString>!, outValue: AudioUnitParameterValue)Added AudioUnitProperty.init()Added AudioUnitProperty.init(mAudioUnit: AudioUnit, mPropertyID: AudioUnitPropertyID, mScope: AudioUnitScope, mElement: AudioUnitElement)Added HostCallbackInfo.init()Added HostCallbackInfo.init(hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc: HostCallback_GetBeatAndTempo, musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation, transportStateProc: HostCallback_GetTransportState, transportStateProc2: HostCallback_GetTransportState2)Added MixerDistanceParams.init()Added MixerDistanceParams.init(mReferenceDistance: Float32, mMaxDistance: Float32, mMaxAttenuation: Float32)Added MusicDeviceNoteParams.init()Added MusicDeviceNoteParams.init(argCount: UInt32, mPitch: Float32, mVelocity: Float32, mControls:(NoteParamsControlValue))Added MusicDeviceStdNoteParams.init()Added MusicDeviceStdNoteParams.init(argCount: UInt32, mPitch: Float32, mVelocity: Float32)Added NoteParamsControlValue.init()Added NoteParamsControlValue.init(mID: AudioUnitParameterID, mValue: AudioUnitParameterValue)Added ScheduledAudioFileRegion.init()Added ScheduledAudioSlice.init()Added ScheduledAudioSlice.init(mTimeStamp: AudioTimeStamp, mCompletionProc: ScheduledAudioSliceCompletionProc, mCompletionProcUserData: UnsafeMutablePointer<Void>, mFlags: UInt32, mReserved: UInt32, mReserved2: UnsafeMutablePointer<Void>, mNumberFrames: UInt32, mBufferList: UnsafeMutablePointer<AudioBufferList>)Modified AUChannelInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUChannelInfo {     var inChannels: Int16     var outChannels: Int16 } ``` |
| To | ``` struct AUChannelInfo {     var inChannels: Int16     var outChannels: Int16     init()     init(inChannels inChannels: Int16, outChannels outChannels: Int16) } ``` |

Modified AUDependentParameter [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUDependentParameter {     var mScope: AudioUnitScope     var mParameterID: AudioUnitParameterID } ``` |
| To | ``` struct AUDependentParameter {     var mScope: AudioUnitScope     var mParameterID: AudioUnitParameterID     init()     init(mScope mScope: AudioUnitScope, mParameterID mParameterID: AudioUnitParameterID) } ``` |

Modified AUInputSamplesInOutputCallbackStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafeMutablePointer<Void>     init()     init(inputToOutputCallback inputToOutputCallback: AUInputSamplesInOutputCallback, userData userData: UnsafeMutablePointer<Void>) } ``` |

Modified AUPreset [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUPreset {     var presetNumber: Int32     var presetName: Unmanaged<CFString>! } ``` |
| To | ``` struct AUPreset {     var presetNumber: Int32     var presetName: Unmanaged<CFString>!     init()     init(presetNumber presetNumber: Int32, presetName presetName: Unmanaged<CFString>!) } ``` |

Modified AURenderCallbackStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AURenderCallbackStruct {     var inputProc: AURenderCallback     var inputProcRefCon: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct AURenderCallbackStruct {     var inputProc: AURenderCallback     var inputProcRefCon: UnsafeMutablePointer<Void>     init()     init(inputProc inputProc: AURenderCallback, inputProcRefCon inputProcRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified AUSamplerBankPresetData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUSamplerBankPresetData {     var bankURL: Unmanaged<CFURL>!     var bankMSB: UInt8     var bankLSB: UInt8     var presetID: UInt8     var reserved: UInt8 } ``` |
| To | ``` struct AUSamplerBankPresetData {     var bankURL: Unmanaged<CFURL>!     var bankMSB: UInt8     var bankLSB: UInt8     var presetID: UInt8     var reserved: UInt8     init()     init(bankURL bankURL: Unmanaged<CFURL>!, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, presetID presetID: UInt8, reserved reserved: UInt8) } ``` |

Modified AUSamplerInstrumentData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUSamplerInstrumentData {     var fileURL: Unmanaged<CFURL>!     var instrumentType: UInt8     var bankMSB: UInt8     var bankLSB: UInt8     var presetID: UInt8 } ``` |
| To | ``` struct AUSamplerInstrumentData {     var fileURL: Unmanaged<CFURL>!     var instrumentType: UInt8     var bankMSB: UInt8     var bankLSB: UInt8     var presetID: UInt8     init()     init(fileURL fileURL: Unmanaged<CFURL>!, instrumentType instrumentType: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, presetID presetID: UInt8) } ``` |

Modified AudioComponentDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioComponentDescription {     var componentType: OSType     var componentSubType: OSType     var componentManufacturer: OSType     var componentFlags: UInt32     var componentFlagsMask: UInt32 } ``` |
| To | ``` struct AudioComponentDescription {     var componentType: OSType     var componentSubType: OSType     var componentManufacturer: OSType     var componentFlags: UInt32     var componentFlagsMask: UInt32     init()     init(componentType componentType: OSType, componentSubType componentSubType: OSType, componentManufacturer componentManufacturer: OSType, componentFlags componentFlags: UInt32, componentFlagsMask componentFlagsMask: UInt32) } ``` |

Modified AudioComponentPlugInInterface [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioComponentPlugInInterface {     var Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>     var Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>     var Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>     var reserved: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct AudioComponentPlugInInterface {     var Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>     var Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>     var Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>     var reserved: UnsafeMutablePointer<Void>     init()     init(Open Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>, Close Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>, Lookup Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>, reserved reserved: UnsafeMutablePointer<Void>) } ``` |

Modified AudioOutputUnitMIDICallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioOutputUnitMIDICallbacks {     var userData: UnsafeMutablePointer<Void>     var MIDIEventProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void)>     var MIDISysExProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void)> } ``` |
| To | ``` struct AudioOutputUnitMIDICallbacks {     var userData: UnsafeMutablePointer<Void>     var MIDIEventProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void)>     var MIDISysExProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void)>     init()     init(userData userData: UnsafeMutablePointer<Void>, MIDIEventProc MIDIEventProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void)>, MIDISysExProc MIDISysExProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void)>) } ``` |

Modified AudioOutputUnitStartAtTimeParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioOutputUnitStartAtTimeParams {     var mTimestamp: AudioTimeStamp     var mFlags: UInt32 } ``` |
| To | ``` struct AudioOutputUnitStartAtTimeParams {     var mTimestamp: AudioTimeStamp     var mFlags: UInt32     init()     init(mTimestamp mTimestamp: AudioTimeStamp, mFlags mFlags: UInt32) } ``` |

Modified AudioUnitConnection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitConnection {     var sourceAudioUnit: AudioUnit     var sourceOutputNumber: UInt32     var destInputNumber: UInt32 } ``` |
| To | ``` struct AudioUnitConnection {     var sourceAudioUnit: AudioUnit     var sourceOutputNumber: UInt32     var destInputNumber: UInt32     init()     init(sourceAudioUnit sourceAudioUnit: AudioUnit, sourceOutputNumber sourceOutputNumber: UInt32, destInputNumber destInputNumber: UInt32) } ``` |

Modified AudioUnitExternalBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitExternalBuffer {     var buffer: UnsafeMutablePointer<Byte>     var size: UInt32 } ``` |
| To | ``` struct AudioUnitExternalBuffer {     var buffer: UnsafeMutablePointer<UInt8>     var size: UInt32     init()     init(buffer buffer: UnsafeMutablePointer<UInt8>, size size: UInt32) } ``` |

Modified AudioUnitExternalBuffer.buffer

|  | Declaration |
| --- | --- |
| From | ``` var buffer: UnsafeMutablePointer<Byte> ``` |
| To | ``` var buffer: UnsafeMutablePointer<UInt8> ``` |

Modified AudioUnitFrequencyResponseBin [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitFrequencyResponseBin {     var mFrequency: Float64     var mMagnitude: Float64 } ``` |
| To | ``` struct AudioUnitFrequencyResponseBin {     var mFrequency: Float64     var mMagnitude: Float64     init()     init(mFrequency mFrequency: Float64, mMagnitude mMagnitude: Float64) } ``` |

Modified AudioUnitMeterClipping [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitMeterClipping {     var peakValueSinceLastCall: Float32     var sawInfinity: Boolean     var sawNotANumber: Boolean } ``` |
| To | ``` struct AudioUnitMeterClipping {     var peakValueSinceLastCall: Float32     var sawInfinity: Boolean     var sawNotANumber: Boolean     init()     init(peakValueSinceLastCall peakValueSinceLastCall: Float32, sawInfinity sawInfinity: Boolean, sawNotANumber sawNotANumber: Boolean) } ``` |

Modified AudioUnitParameter [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameter {     var mAudioUnit: AudioUnit     var mParameterID: AudioUnitParameterID     var mScope: AudioUnitScope     var mElement: AudioUnitElement } ``` |
| To | ``` struct AudioUnitParameter {     var mAudioUnit: AudioUnit     var mParameterID: AudioUnitParameterID     var mScope: AudioUnitScope     var mElement: AudioUnitElement     init()     init(mAudioUnit mAudioUnit: AudioUnit, mParameterID mParameterID: AudioUnitParameterID, mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement) } ``` |

Modified AudioUnitParameterEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var parameter: AudioUnitParameterID     var eventType: AUParameterEventType } ``` |
| To | ``` struct AudioUnitParameterEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var parameter: AudioUnitParameterID     var eventType: AUParameterEventType     init() } ``` |

Modified AudioUnitParameterHistoryInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterHistoryInfo {     var updatesPerSecond: Float32     var historyDurationInSeconds: Float32 } ``` |
| To | ``` struct AudioUnitParameterHistoryInfo {     var updatesPerSecond: Float32     var historyDurationInSeconds: Float32     init()     init(updatesPerSecond updatesPerSecond: Float32, historyDurationInSeconds historyDurationInSeconds: Float32) } ``` |

Modified AudioUnitParameterInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterInfo {     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var unitName: Unmanaged<CFString>!     var clumpID: UInt32     var cfNameString: Unmanaged<CFString>!     var unit: AudioUnitParameterUnit     var minValue: AudioUnitParameterValue     var maxValue: AudioUnitParameterValue     var defaultValue: AudioUnitParameterValue     var flags: UInt32 } ``` |
| To | ``` struct AudioUnitParameterInfo {     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var unitName: Unmanaged<CFString>!     var clumpID: UInt32     var cfNameString: Unmanaged<CFString>!     var unit: AudioUnitParameterUnit     var minValue: AudioUnitParameterValue     var maxValue: AudioUnitParameterValue     var defaultValue: AudioUnitParameterValue     var flags: UInt32     init()     init(name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName unitName: Unmanaged<CFString>!, clumpID clumpID: UInt32, cfNameString cfNameString: Unmanaged<CFString>!, unit unit: AudioUnitParameterUnit, minValue minValue: AudioUnitParameterValue, maxValue maxValue: AudioUnitParameterValue, defaultValue defaultValue: AudioUnitParameterValue, flags flags: UInt32) } ``` |

Modified AudioUnitParameterNameInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterNameInfo {     var inID: AudioUnitParameterID     var inDesiredLength: Int32     var outName: Unmanaged<CFString>! } ``` |
| To | ``` struct AudioUnitParameterNameInfo {     var inID: AudioUnitParameterID     var inDesiredLength: Int32     var outName: Unmanaged<CFString>!     init()     init(inID inID: AudioUnitParameterID, inDesiredLength inDesiredLength: Int32, outName outName: Unmanaged<CFString>!) } ``` |

Modified AudioUnitParameterStringFromValue [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterStringFromValue {     var inParamID: AudioUnitParameterID     var inValue: UnsafePointer<AudioUnitParameterValue>     var outString: Unmanaged<CFString>! } ``` |
| To | ``` struct AudioUnitParameterStringFromValue {     var inParamID: AudioUnitParameterID     var inValue: UnsafePointer<AudioUnitParameterValue>     var outString: Unmanaged<CFString>!     init()     init(inParamID inParamID: AudioUnitParameterID, inValue inValue: UnsafePointer<AudioUnitParameterValue>, outString outString: Unmanaged<CFString>!) } ``` |

Modified AudioUnitParameterValueFromString [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterValueFromString {     var inParamID: AudioUnitParameterID     var inString: Unmanaged<CFString>!     var outValue: AudioUnitParameterValue } ``` |
| To | ``` struct AudioUnitParameterValueFromString {     var inParamID: AudioUnitParameterID     var inString: Unmanaged<CFString>!     var outValue: AudioUnitParameterValue     init()     init(inParamID inParamID: AudioUnitParameterID, inString inString: Unmanaged<CFString>!, outValue outValue: AudioUnitParameterValue) } ``` |

Modified AudioUnitProperty [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitProperty {     var mAudioUnit: AudioUnit     var mPropertyID: AudioUnitPropertyID     var mScope: AudioUnitScope     var mElement: AudioUnitElement } ``` |
| To | ``` struct AudioUnitProperty {     var mAudioUnit: AudioUnit     var mPropertyID: AudioUnitPropertyID     var mScope: AudioUnitScope     var mElement: AudioUnitElement     init()     init(mAudioUnit mAudioUnit: AudioUnit, mPropertyID mPropertyID: AudioUnitPropertyID, mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement) } ``` |

Modified HostCallbackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HostCallbackInfo {     var hostUserData: UnsafeMutablePointer<Void>     var beatAndTempoProc: HostCallback_GetBeatAndTempo     var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation     var transportStateProc: HostCallback_GetTransportState     var transportStateProc2: HostCallback_GetTransportState2 } ``` |
| To | ``` struct HostCallbackInfo {     var hostUserData: UnsafeMutablePointer<Void>     var beatAndTempoProc: HostCallback_GetBeatAndTempo     var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation     var transportStateProc: HostCallback_GetTransportState     var transportStateProc2: HostCallback_GetTransportState2     init()     init(hostUserData hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc beatAndTempoProc: HostCallback_GetBeatAndTempo, musicalTimeLocationProc musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation, transportStateProc transportStateProc: HostCallback_GetTransportState, transportStateProc2 transportStateProc2: HostCallback_GetTransportState2) } ``` |

Modified MixerDistanceParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MixerDistanceParams {     var mReferenceDistance: Float32     var mMaxDistance: Float32     var mMaxAttenuation: Float32 } ``` |
| To | ``` struct MixerDistanceParams {     var mReferenceDistance: Float32     var mMaxDistance: Float32     var mMaxAttenuation: Float32     init()     init(mReferenceDistance mReferenceDistance: Float32, mMaxDistance mMaxDistance: Float32, mMaxAttenuation mMaxAttenuation: Float32) } ``` |

Modified MusicDeviceNoteParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MusicDeviceNoteParams {     var argCount: UInt32     var mPitch: Float32     var mVelocity: Float32     var mControls: (NoteParamsControlValue) } ``` |
| To | ``` struct MusicDeviceNoteParams {     var argCount: UInt32     var mPitch: Float32     var mVelocity: Float32     var mControls: (NoteParamsControlValue)     init()     init(argCount argCount: UInt32, mPitch mPitch: Float32, mVelocity mVelocity: Float32, mControls mControls: (NoteParamsControlValue)) } ``` |

Modified MusicDeviceStdNoteParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MusicDeviceStdNoteParams {     var argCount: UInt32     var mPitch: Float32     var mVelocity: Float32 } ``` |
| To | ``` struct MusicDeviceStdNoteParams {     var argCount: UInt32     var mPitch: Float32     var mVelocity: Float32     init()     init(argCount argCount: UInt32, mPitch mPitch: Float32, mVelocity mVelocity: Float32) } ``` |

Modified NoteParamsControlValue [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NoteParamsControlValue {     var mID: AudioUnitParameterID     var mValue: AudioUnitParameterValue } ``` |
| To | ``` struct NoteParamsControlValue {     var mID: AudioUnitParameterID     var mValue: AudioUnitParameterValue     init()     init(mID mID: AudioUnitParameterID, mValue mValue: AudioUnitParameterValue) } ``` |

Modified ScheduledAudioFileRegion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScheduledAudioFileRegion {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioFileRegionCompletionProc     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mAudioFile: COpaquePointer     var mLoopCount: UInt32     var mStartFrame: Int64     var mFramesToPlay: UInt32 } ``` |
| To | ``` struct ScheduledAudioFileRegion {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioFileRegionCompletionProc     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mAudioFile: COpaquePointer     var mLoopCount: UInt32     var mStartFrame: Int64     var mFramesToPlay: UInt32     init() } ``` |

Modified ScheduledAudioSlice [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScheduledAudioSlice {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioSliceCompletionProc     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mFlags: UInt32     var mReserved: UInt32     var mReserved2: UnsafeMutablePointer<Void>     var mNumberFrames: UInt32     var mBufferList: UnsafeMutablePointer<AudioBufferList> } ``` |
| To | ``` struct ScheduledAudioSlice {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioSliceCompletionProc     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mFlags: UInt32     var mReserved: UInt32     var mReserved2: UnsafeMutablePointer<Void>     var mNumberFrames: UInt32     var mBufferList: UnsafeMutablePointer<AudioBufferList>     init()     init(mTimeStamp mTimeStamp: AudioTimeStamp, mCompletionProc mCompletionProc: ScheduledAudioSliceCompletionProc, mCompletionProcUserData mCompletionProcUserData: UnsafeMutablePointer<Void>, mFlags mFlags: UInt32, mReserved mReserved: UInt32, mReserved2 mReserved2: UnsafeMutablePointer<Void>, mNumberFrames mNumberFrames: UInt32, mBufferList mBufferList: UnsafeMutablePointer<AudioBufferList>) } ``` |

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
