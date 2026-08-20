---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/AudioUnit.html
archived_at: '2026-07-18T02:52:06.313370Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# AudioUnit Changes

## AudioUnit

Added AUChannelInfo.init()Added AUChannelInfo.init(inChannels: Int16, outChannels: Int16)Added AUDependentParameter.init()Added AUDependentParameter.init(mScope: AudioUnitScope, mParameterID: AudioUnitParameterID)Added AUDistanceAttenuationData.init()Added AUHostIdentifier.init()Added AUHostIdentifier.init(hostName: Unmanaged<CFString>!, hostVersion: AUNumVersion)Added AUHostVersionIdentifier.init()Added AUHostVersionIdentifier.init(hostName: Unmanaged<CFString>!, hostVersion: UInt32)Added AUInputSamplesInOutputCallbackStruct.init()Added AUInputSamplesInOutputCallbackStruct.init(inputToOutputCallback: AUInputSamplesInOutputCallback, userData: UnsafeMutablePointer<Void>)Added AUMIDIOutputCallbackStruct.init()Added AUMIDIOutputCallbackStruct.init(midiOutputCallback: AUMIDIOutputCallback, userData: UnsafeMutablePointer<Void>)Added AUNumVersion.init()Added AUNumVersion.init(nonRelRev: UInt8, stage: UInt8, minorAndBugRev: UInt8, majorRev: UInt8)Added AUParameterMIDIMapping.init()Added AUParameterMIDIMapping.init(mScope: AudioUnitScope, mElement: AudioUnitElement, mParameterID: AudioUnitParameterID, mFlags: UInt32, mSubRangeMin: AudioUnitParameterValue, mSubRangeMax: AudioUnitParameterValue, mStatus: UInt8, mData1: UInt8, reserved1: UInt8, reserved2: UInt8, reserved3: UInt32)Added AUPreset.init()Added AUPreset.init(presetNumber: Int32, presetName: Unmanaged<CFString>!)Added AURenderCallbackStruct.init()Added AURenderCallbackStruct.init(inputProc: AURenderCallback, inputProcRefCon: UnsafeMutablePointer<Void>)Added AUSamplerBankPresetData.init()Added AUSamplerBankPresetData.init(bankURL: Unmanaged<CFURL>!, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8, reserved: UInt8)Added AUSamplerInstrumentData.init()Added AUSamplerInstrumentData.init(fileURL: Unmanaged<CFURL>!, instrumentType: UInt8, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8)Added AudioCodecMagicCookieInfo.init()Added AudioCodecMagicCookieInfo.init(mMagicCookieSize: UInt32, mMagicCookie: UnsafePointer<Void>)Added AudioCodecPrimeInfo.init()Added AudioCodecPrimeInfo.init(leadingFrames: UInt32, trailingFrames: UInt32)Added AudioComponentDescription.init()Added AudioComponentDescription.init(componentType: OSType, componentSubType: OSType, componentManufacturer: OSType, componentFlags: UInt32, componentFlagsMask: UInt32)Added AudioComponentPlugInInterface.init()Added AudioComponentPlugInInterface.init(Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>, Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>, Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>, reserved: UnsafeMutablePointer<Void>)Added AudioOutputUnitStartAtTimeParams.init()Added AudioOutputUnitStartAtTimeParams.init(mTimestamp: AudioTimeStamp, mFlags: UInt32)Added AudioUnitCocoaViewInfo.init()Added AudioUnitCocoaViewInfo.init(mCocoaAUViewBundleLocation: Unmanaged<CFURL>!, mCocoaAUViewClass:(Unmanaged<CFString>?))Added AudioUnitConnection.init()Added AudioUnitConnection.init(sourceAudioUnit: AudioUnit, sourceOutputNumber: UInt32, destInputNumber: UInt32)Added AudioUnitExternalBuffer.init()Added AudioUnitExternalBuffer.init(buffer: UnsafeMutablePointer<UInt8>, size: UInt32)Added AudioUnitFrequencyResponseBin.init()Added AudioUnitFrequencyResponseBin.init(mFrequency: Float64, mMagnitude: Float64)Added AudioUnitMIDIControlMapping.init()Added AudioUnitMIDIControlMapping.init(midiNRPN: UInt16, midiControl: UInt8, scope: UInt8, element: AudioUnitElement, parameter: AudioUnitParameterID)Added AudioUnitMeterClipping.init()Added AudioUnitMeterClipping.init(peakValueSinceLastCall: Float32, sawInfinity: Boolean, sawNotANumber: Boolean)Added AudioUnitOtherPluginDesc.init()Added AudioUnitOtherPluginDesc.init(format: UInt32, plugin: AudioClassDescription)Added AudioUnitParameter.init()Added AudioUnitParameter.init(mAudioUnit: AudioUnit, mParameterID: AudioUnitParameterID, mScope: AudioUnitScope, mElement: AudioUnitElement)Added AudioUnitParameterEvent.init()Added AudioUnitParameterHistoryInfo.init()Added AudioUnitParameterHistoryInfo.init(updatesPerSecond: Float32, historyDurationInSeconds: Float32)Added AudioUnitParameterInfo.init()Added AudioUnitParameterInfo.init(name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName: Unmanaged<CFString>!, clumpID: UInt32, cfNameString: Unmanaged<CFString>!, unit: AudioUnitParameterUnit, minValue: AudioUnitParameterValue, maxValue: AudioUnitParameterValue, defaultValue: AudioUnitParameterValue, flags: UInt32)Added AudioUnitParameterNameInfo.init()Added AudioUnitParameterNameInfo.init(inID: AudioUnitParameterID, inDesiredLength: Int32, outName: Unmanaged<CFString>!)Added AudioUnitParameterStringFromValue.init()Added AudioUnitParameterStringFromValue.init(inParamID: AudioUnitParameterID, inValue: UnsafePointer<AudioUnitParameterValue>, outString: Unmanaged<CFString>!)Added AudioUnitParameterValueFromString.init()Added AudioUnitParameterValueFromString.init(inParamID: AudioUnitParameterID, inString: Unmanaged<CFString>!, outValue: AudioUnitParameterValue)Added AudioUnitParameterValueName.init()Added AudioUnitParameterValueName.init(inParamID: AudioUnitParameterID, inValue: UnsafePointer<Float32>, outName: Unmanaged<CFString>!)Added AudioUnitParameterValueTranslation.init()Added AudioUnitParameterValueTranslation.init(otherDesc: AudioUnitOtherPluginDesc, otherParamID: UInt32, otherValue: Float32, auParamID: AudioUnitParameterID, auValue: AudioUnitParameterValue)Added AudioUnitPresetMAS_SettingData.init()Added AudioUnitPresetMAS_SettingData.init(isStockSetting: UInt32, settingID: UInt32, dataLen: UInt32, data:(UInt8))Added AudioUnitPresetMAS_Settings.init()Added AudioUnitPresetMAS_Settings.init(manufacturerID: UInt32, effectID: UInt32, variantID: UInt32, settingsVersion: UInt32, numberOfSettings: UInt32, settings:(AudioUnitPresetMAS_SettingData))Added AudioUnitProperty.init()Added AudioUnitProperty.init(mAudioUnit: AudioUnit, mPropertyID: AudioUnitPropertyID, mScope: AudioUnitScope, mElement: AudioUnitElement)Added HostCallbackInfo.init()Added HostCallbackInfo.init(hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc: HostCallback_GetBeatAndTempo, musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation, transportStateProc: HostCallback_GetTransportState, transportStateProc2: HostCallback_GetTransportState2)Added MixerDistanceParams.init()Added MixerDistanceParams.init(mReferenceDistance: Float32, mMaxDistance: Float32, mMaxAttenuation: Float32)Added MusicDeviceNoteParams.init()Added MusicDeviceNoteParams.init(argCount: UInt32, mPitch: Float32, mVelocity: Float32, mControls:(NoteParamsControlValue))Added MusicDeviceStdNoteParams.init()Added MusicDeviceStdNoteParams.init(argCount: UInt32, mPitch: Float32, mVelocity: Float32)Added NoteParamsControlValue.init()Added NoteParamsControlValue.init(mID: AudioUnitParameterID, mValue: AudioUnitParameterValue)Added ScheduledAudioFileRegion.init()Added ScheduledAudioSlice.init()Added ScheduledAudioSlice.init(mTimeStamp: AudioTimeStamp, mCompletionProc: ScheduledAudioSliceCompletionProc, mCompletionProcUserData: UnsafeMutablePointer<Void>, mFlags: UInt32, mReserved: UInt32, mReserved2: UnsafeMutablePointer<Void>, mNumberFrames: UInt32, mBufferList: UnsafeMutablePointer<AudioBufferList>)Modified AUChannelInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUChannelInfo {     var inChannels: Int16     var outChannels: Int16 } ``` |
| To | ``` struct AUChannelInfo {     var inChannels: Int16     var outChannels: Int16     init()     init(inChannels inChannels: Int16, outChannels outChannels: Int16) } ``` |

Modified AUDependentParameter [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUDependentParameter {     var mScope: AudioUnitScope     var mParameterID: AudioUnitParameterID } ``` |
| To | ``` struct AUDependentParameter {     var mScope: AudioUnitScope     var mParameterID: AudioUnitParameterID     init()     init(mScope mScope: AudioUnitScope, mParameterID mParameterID: AudioUnitParameterID) } ``` |

Modified AUDistanceAttenuationData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUDistanceAttenuationData {     var inNumberOfPairs: UInt32 } ``` |
| To | ``` struct AUDistanceAttenuationData {     var inNumberOfPairs: UInt32     init() } ``` |

Modified AUHostIdentifier [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUHostIdentifier {     var hostName: Unmanaged<CFString>!     var hostVersion: AUNumVersion } ``` |
| To | ``` struct AUHostIdentifier {     var hostName: Unmanaged<CFString>!     var hostVersion: AUNumVersion     init()     init(hostName hostName: Unmanaged<CFString>!, hostVersion hostVersion: AUNumVersion) } ``` |

Modified AUHostVersionIdentifier [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUHostVersionIdentifier {     var hostName: Unmanaged<CFString>!     var hostVersion: UInt32 } ``` |
| To | ``` struct AUHostVersionIdentifier {     var hostName: Unmanaged<CFString>!     var hostVersion: UInt32     init()     init(hostName hostName: Unmanaged<CFString>!, hostVersion hostVersion: UInt32) } ``` |

Modified AUInputSamplesInOutputCallbackStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafePointer<()> } ``` |
| To | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafeMutablePointer<Void>     init()     init(inputToOutputCallback inputToOutputCallback: AUInputSamplesInOutputCallback, userData userData: UnsafeMutablePointer<Void>) } ``` |

Modified AUInputSamplesInOutputCallbackStruct.userData

|  | Declaration |
| --- | --- |
| From | ``` var userData: UnsafePointer<()> ``` |
| To | ``` var userData: UnsafeMutablePointer<Void> ``` |

Modified AUMIDIOutputCallbackStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUMIDIOutputCallbackStruct {     var midiOutputCallback: AUMIDIOutputCallback     var userData: UnsafePointer<()> } ``` |
| To | ``` struct AUMIDIOutputCallbackStruct {     var midiOutputCallback: AUMIDIOutputCallback     var userData: UnsafeMutablePointer<Void>     init()     init(midiOutputCallback midiOutputCallback: AUMIDIOutputCallback, userData userData: UnsafeMutablePointer<Void>) } ``` |

Modified AUMIDIOutputCallbackStruct.userData

|  | Declaration |
| --- | --- |
| From | ``` var userData: UnsafePointer<()> ``` |
| To | ``` var userData: UnsafeMutablePointer<Void> ``` |

Modified AUNumVersion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUNumVersion {     var nonRelRev: UInt8     var stage: UInt8     var minorAndBugRev: UInt8     var majorRev: UInt8 } ``` |
| To | ``` struct AUNumVersion {     var nonRelRev: UInt8     var stage: UInt8     var minorAndBugRev: UInt8     var majorRev: UInt8     init()     init(nonRelRev nonRelRev: UInt8, stage stage: UInt8, minorAndBugRev minorAndBugRev: UInt8, majorRev majorRev: UInt8) } ``` |

Modified AUParameterMIDIMapping [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUParameterMIDIMapping {     var mScope: AudioUnitScope     var mElement: AudioUnitElement     var mParameterID: AudioUnitParameterID     var mFlags: UInt32     var mSubRangeMin: AudioUnitParameterValue     var mSubRangeMax: AudioUnitParameterValue     var mStatus: UInt8     var mData1: UInt8     var reserved1: UInt8     var reserved2: UInt8     var reserved3: UInt32 } ``` |
| To | ``` struct AUParameterMIDIMapping {     var mScope: AudioUnitScope     var mElement: AudioUnitElement     var mParameterID: AudioUnitParameterID     var mFlags: UInt32     var mSubRangeMin: AudioUnitParameterValue     var mSubRangeMax: AudioUnitParameterValue     var mStatus: UInt8     var mData1: UInt8     var reserved1: UInt8     var reserved2: UInt8     var reserved3: UInt32     init()     init(mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement, mParameterID mParameterID: AudioUnitParameterID, mFlags mFlags: UInt32, mSubRangeMin mSubRangeMin: AudioUnitParameterValue, mSubRangeMax mSubRangeMax: AudioUnitParameterValue, mStatus mStatus: UInt8, mData1 mData1: UInt8, reserved1 reserved1: UInt8, reserved2 reserved2: UInt8, reserved3 reserved3: UInt32) } ``` |

Modified AUPreset [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUPreset {     var presetNumber: Int32     var presetName: Unmanaged<CFString>! } ``` |
| To | ``` struct AUPreset {     var presetNumber: Int32     var presetName: Unmanaged<CFString>!     init()     init(presetNumber presetNumber: Int32, presetName presetName: Unmanaged<CFString>!) } ``` |

Modified AURenderCallbackStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AURenderCallbackStruct {     var inputProc: AURenderCallback     var inputProcRefCon: UnsafePointer<()> } ``` |
| To | ``` struct AURenderCallbackStruct {     var inputProc: AURenderCallback     var inputProcRefCon: UnsafeMutablePointer<Void>     init()     init(inputProc inputProc: AURenderCallback, inputProcRefCon inputProcRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified AURenderCallbackStruct.inputProcRefCon

|  | Declaration |
| --- | --- |
| From | ``` var inputProcRefCon: UnsafePointer<()> ``` |
| To | ``` var inputProcRefCon: UnsafeMutablePointer<Void> ``` |

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

Modified AudioCodecMagicCookieInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioCodecMagicCookieInfo {     var mMagicCookieSize: UInt32     var mMagicCookie: ConstUnsafePointer<()> } ``` |
| To | ``` struct AudioCodecMagicCookieInfo {     var mMagicCookieSize: UInt32     var mMagicCookie: UnsafePointer<Void>     init()     init(mMagicCookieSize mMagicCookieSize: UInt32, mMagicCookie mMagicCookie: UnsafePointer<Void>) } ``` |

Modified AudioCodecMagicCookieInfo.mMagicCookie

|  | Declaration |
| --- | --- |
| From | ``` var mMagicCookie: ConstUnsafePointer<()> ``` |
| To | ``` var mMagicCookie: UnsafePointer<Void> ``` |

Modified AudioCodecPrimeInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioCodecPrimeInfo {     var leadingFrames: UInt32     var trailingFrames: UInt32 } ``` |
| To | ``` struct AudioCodecPrimeInfo {     var leadingFrames: UInt32     var trailingFrames: UInt32     init()     init(leadingFrames leadingFrames: UInt32, trailingFrames trailingFrames: UInt32) } ``` |

Modified AudioComponentDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioComponentDescription {     var componentType: OSType     var componentSubType: OSType     var componentManufacturer: OSType     var componentFlags: UInt32     var componentFlagsMask: UInt32 } ``` |
| To | ``` struct AudioComponentDescription {     var componentType: OSType     var componentSubType: OSType     var componentManufacturer: OSType     var componentFlags: UInt32     var componentFlagsMask: UInt32     init()     init(componentType componentType: OSType, componentSubType componentSubType: OSType, componentManufacturer componentManufacturer: OSType, componentFlags componentFlags: UInt32, componentFlagsMask componentFlagsMask: UInt32) } ``` |

Modified AudioComponentPlugInInterface [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioComponentPlugInInterface {     var Open: CFunctionPointer<((UnsafePointer<()>, AudioComponentInstance) -> OSStatus)>     var Close: CFunctionPointer<((UnsafePointer<()>) -> OSStatus)>     var Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>     var reserved: UnsafePointer<()> } ``` |
| To | ``` struct AudioComponentPlugInInterface {     var Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>     var Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>     var Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>     var reserved: UnsafeMutablePointer<Void>     init()     init(Open Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>, Close Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>, Lookup Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>, reserved reserved: UnsafeMutablePointer<Void>) } ``` |

Modified AudioComponentPlugInInterface.Close

|  | Declaration |
| --- | --- |
| From | ``` var Close: CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` var Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioComponentPlugInInterface.Open

|  | Declaration |
| --- | --- |
| From | ``` var Open: CFunctionPointer<((UnsafePointer<()>, AudioComponentInstance) -> OSStatus)> ``` |
| To | ``` var Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)> ``` |

Modified AudioComponentPlugInInterface.reserved

|  | Declaration |
| --- | --- |
| From | ``` var reserved: UnsafePointer<()> ``` |
| To | ``` var reserved: UnsafeMutablePointer<Void> ``` |

Modified AudioOutputUnitStartAtTimeParams [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioOutputUnitStartAtTimeParams {     var mTimestamp: AudioTimeStamp     var mFlags: UInt32 } ``` |
| To | ``` struct AudioOutputUnitStartAtTimeParams {     var mTimestamp: AudioTimeStamp     var mFlags: UInt32     init()     init(mTimestamp mTimestamp: AudioTimeStamp, mFlags mFlags: UInt32) } ``` |

Modified AudioUnitCocoaViewInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitCocoaViewInfo {     var mCocoaAUViewBundleLocation: Unmanaged<CFURL>!     var mCocoaAUViewClass: (Unmanaged<CFString>?) } ``` |
| To | ``` struct AudioUnitCocoaViewInfo {     var mCocoaAUViewBundleLocation: Unmanaged<CFURL>!     var mCocoaAUViewClass: (Unmanaged<CFString>?)     init()     init(mCocoaAUViewBundleLocation mCocoaAUViewBundleLocation: Unmanaged<CFURL>!, mCocoaAUViewClass mCocoaAUViewClass: (Unmanaged<CFString>?)) } ``` |

Modified AudioUnitConnection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitConnection {     var sourceAudioUnit: AudioUnit     var sourceOutputNumber: UInt32     var destInputNumber: UInt32 } ``` |
| To | ``` struct AudioUnitConnection {     var sourceAudioUnit: AudioUnit     var sourceOutputNumber: UInt32     var destInputNumber: UInt32     init()     init(sourceAudioUnit sourceAudioUnit: AudioUnit, sourceOutputNumber sourceOutputNumber: UInt32, destInputNumber destInputNumber: UInt32) } ``` |

Modified AudioUnitExternalBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitExternalBuffer {     var buffer: UnsafePointer<Byte>     var size: UInt32 } ``` |
| To | ``` struct AudioUnitExternalBuffer {     var buffer: UnsafeMutablePointer<UInt8>     var size: UInt32     init()     init(buffer buffer: UnsafeMutablePointer<UInt8>, size size: UInt32) } ``` |

Modified AudioUnitExternalBuffer.buffer

|  | Declaration |
| --- | --- |
| From | ``` var buffer: UnsafePointer<Byte> ``` |
| To | ``` var buffer: UnsafeMutablePointer<UInt8> ``` |

Modified AudioUnitFrequencyResponseBin [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitFrequencyResponseBin {     var mFrequency: Float64     var mMagnitude: Float64 } ``` |
| To | ``` struct AudioUnitFrequencyResponseBin {     var mFrequency: Float64     var mMagnitude: Float64     init()     init(mFrequency mFrequency: Float64, mMagnitude mMagnitude: Float64) } ``` |

Modified AudioUnitMIDIControlMapping [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitMIDIControlMapping {     var midiNRPN: UInt16     var midiControl: UInt8     var scope: UInt8     var element: AudioUnitElement     var parameter: AudioUnitParameterID } ``` |
| To | ``` struct AudioUnitMIDIControlMapping {     var midiNRPN: UInt16     var midiControl: UInt8     var scope: UInt8     var element: AudioUnitElement     var parameter: AudioUnitParameterID     init()     init(midiNRPN midiNRPN: UInt16, midiControl midiControl: UInt8, scope scope: UInt8, element element: AudioUnitElement, parameter parameter: AudioUnitParameterID) } ``` |

Modified AudioUnitMeterClipping [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitMeterClipping {     var peakValueSinceLastCall: Float32     var sawInfinity: Boolean     var sawNotANumber: Boolean } ``` |
| To | ``` struct AudioUnitMeterClipping {     var peakValueSinceLastCall: Float32     var sawInfinity: Boolean     var sawNotANumber: Boolean     init()     init(peakValueSinceLastCall peakValueSinceLastCall: Float32, sawInfinity sawInfinity: Boolean, sawNotANumber sawNotANumber: Boolean) } ``` |

Modified AudioUnitOtherPluginDesc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitOtherPluginDesc {     var format: UInt32     var plugin: AudioClassDescription } ``` |
| To | ``` struct AudioUnitOtherPluginDesc {     var format: UInt32     var plugin: AudioClassDescription     init()     init(format format: UInt32, plugin plugin: AudioClassDescription) } ``` |

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
| From | ``` struct AudioUnitParameterStringFromValue {     var inParamID: AudioUnitParameterID     var inValue: ConstUnsafePointer<AudioUnitParameterValue>     var outString: Unmanaged<CFString>! } ``` |
| To | ``` struct AudioUnitParameterStringFromValue {     var inParamID: AudioUnitParameterID     var inValue: UnsafePointer<AudioUnitParameterValue>     var outString: Unmanaged<CFString>!     init()     init(inParamID inParamID: AudioUnitParameterID, inValue inValue: UnsafePointer<AudioUnitParameterValue>, outString outString: Unmanaged<CFString>!) } ``` |

Modified AudioUnitParameterStringFromValue.inValue

|  | Declaration |
| --- | --- |
| From | ``` var inValue: ConstUnsafePointer<AudioUnitParameterValue> ``` |
| To | ``` var inValue: UnsafePointer<AudioUnitParameterValue> ``` |

Modified AudioUnitParameterValueFromString [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterValueFromString {     var inParamID: AudioUnitParameterID     var inString: Unmanaged<CFString>!     var outValue: AudioUnitParameterValue } ``` |
| To | ``` struct AudioUnitParameterValueFromString {     var inParamID: AudioUnitParameterID     var inString: Unmanaged<CFString>!     var outValue: AudioUnitParameterValue     init()     init(inParamID inParamID: AudioUnitParameterID, inString inString: Unmanaged<CFString>!, outValue outValue: AudioUnitParameterValue) } ``` |

Modified AudioUnitParameterValueName [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterValueName {     var inParamID: AudioUnitParameterID     var inValue: ConstUnsafePointer<Float32>     var outName: Unmanaged<CFString>! } ``` |
| To | ``` struct AudioUnitParameterValueName {     var inParamID: AudioUnitParameterID     var inValue: UnsafePointer<Float32>     var outName: Unmanaged<CFString>!     init()     init(inParamID inParamID: AudioUnitParameterID, inValue inValue: UnsafePointer<Float32>, outName outName: Unmanaged<CFString>!) } ``` |

Modified AudioUnitParameterValueName.inValue

|  | Declaration |
| --- | --- |
| From | ``` var inValue: ConstUnsafePointer<Float32> ``` |
| To | ``` var inValue: UnsafePointer<Float32> ``` |

Modified AudioUnitParameterValueTranslation [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterValueTranslation {     var otherDesc: AudioUnitOtherPluginDesc     var otherParamID: UInt32     var otherValue: Float32     var auParamID: AudioUnitParameterID     var auValue: AudioUnitParameterValue } ``` |
| To | ``` struct AudioUnitParameterValueTranslation {     var otherDesc: AudioUnitOtherPluginDesc     var otherParamID: UInt32     var otherValue: Float32     var auParamID: AudioUnitParameterID     var auValue: AudioUnitParameterValue     init()     init(otherDesc otherDesc: AudioUnitOtherPluginDesc, otherParamID otherParamID: UInt32, otherValue otherValue: Float32, auParamID auParamID: AudioUnitParameterID, auValue auValue: AudioUnitParameterValue) } ``` |

Modified AudioUnitPresetMAS_SettingData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitPresetMAS_SettingData {     var isStockSetting: UInt32     var settingID: UInt32     var dataLen: UInt32     var data: (UInt8) } ``` |
| To | ``` struct AudioUnitPresetMAS_SettingData {     var isStockSetting: UInt32     var settingID: UInt32     var dataLen: UInt32     var data: (UInt8)     init()     init(isStockSetting isStockSetting: UInt32, settingID settingID: UInt32, dataLen dataLen: UInt32, data data: (UInt8)) } ``` |

Modified AudioUnitPresetMAS_Settings [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitPresetMAS_Settings {     var manufacturerID: UInt32     var effectID: UInt32     var variantID: UInt32     var settingsVersion: UInt32     var numberOfSettings: UInt32     var settings: (AudioUnitPresetMAS_SettingData) } ``` |
| To | ``` struct AudioUnitPresetMAS_Settings {     var manufacturerID: UInt32     var effectID: UInt32     var variantID: UInt32     var settingsVersion: UInt32     var numberOfSettings: UInt32     var settings: (AudioUnitPresetMAS_SettingData)     init()     init(manufacturerID manufacturerID: UInt32, effectID effectID: UInt32, variantID variantID: UInt32, settingsVersion settingsVersion: UInt32, numberOfSettings numberOfSettings: UInt32, settings settings: (AudioUnitPresetMAS_SettingData)) } ``` |

Modified AudioUnitProperty [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitProperty {     var mAudioUnit: AudioUnit     var mPropertyID: AudioUnitPropertyID     var mScope: AudioUnitScope     var mElement: AudioUnitElement } ``` |
| To | ``` struct AudioUnitProperty {     var mAudioUnit: AudioUnit     var mPropertyID: AudioUnitPropertyID     var mScope: AudioUnitScope     var mElement: AudioUnitElement     init()     init(mAudioUnit mAudioUnit: AudioUnit, mPropertyID mPropertyID: AudioUnitPropertyID, mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement) } ``` |

Modified HostCallbackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HostCallbackInfo {     var hostUserData: UnsafePointer<()>     var beatAndTempoProc: HostCallback_GetBeatAndTempo     var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation     var transportStateProc: HostCallback_GetTransportState     var transportStateProc2: HostCallback_GetTransportState2 } ``` |
| To | ``` struct HostCallbackInfo {     var hostUserData: UnsafeMutablePointer<Void>     var beatAndTempoProc: HostCallback_GetBeatAndTempo     var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation     var transportStateProc: HostCallback_GetTransportState     var transportStateProc2: HostCallback_GetTransportState2     init()     init(hostUserData hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc beatAndTempoProc: HostCallback_GetBeatAndTempo, musicalTimeLocationProc musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation, transportStateProc transportStateProc: HostCallback_GetTransportState, transportStateProc2 transportStateProc2: HostCallback_GetTransportState2) } ``` |

Modified HostCallbackInfo.hostUserData

|  | Declaration |
| --- | --- |
| From | ``` var hostUserData: UnsafePointer<()> ``` |
| To | ``` var hostUserData: UnsafeMutablePointer<Void> ``` |

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
| From | ``` struct ScheduledAudioFileRegion {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioFileRegionCompletionProc     var mCompletionProcUserData: UnsafePointer<()>     var mAudioFile: COpaquePointer     var mLoopCount: UInt32     var mStartFrame: Int64     var mFramesToPlay: UInt32 } ``` |
| To | ``` struct ScheduledAudioFileRegion {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioFileRegionCompletionProc     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mAudioFile: COpaquePointer     var mLoopCount: UInt32     var mStartFrame: Int64     var mFramesToPlay: UInt32     init() } ``` |

Modified ScheduledAudioFileRegion.mCompletionProcUserData

|  | Declaration |
| --- | --- |
| From | ``` var mCompletionProcUserData: UnsafePointer<()> ``` |
| To | ``` var mCompletionProcUserData: UnsafeMutablePointer<Void> ``` |

Modified ScheduledAudioSlice [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ScheduledAudioSlice {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioSliceCompletionProc     var mCompletionProcUserData: UnsafePointer<()>     var mFlags: UInt32     var mReserved: UInt32     var mReserved2: UnsafePointer<()>     var mNumberFrames: UInt32     var mBufferList: UnsafePointer<AudioBufferList> } ``` |
| To | ``` struct ScheduledAudioSlice {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioSliceCompletionProc     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mFlags: UInt32     var mReserved: UInt32     var mReserved2: UnsafeMutablePointer<Void>     var mNumberFrames: UInt32     var mBufferList: UnsafeMutablePointer<AudioBufferList>     init()     init(mTimeStamp mTimeStamp: AudioTimeStamp, mCompletionProc mCompletionProc: ScheduledAudioSliceCompletionProc, mCompletionProcUserData mCompletionProcUserData: UnsafeMutablePointer<Void>, mFlags mFlags: UInt32, mReserved mReserved: UInt32, mReserved2 mReserved2: UnsafeMutablePointer<Void>, mNumberFrames mNumberFrames: UInt32, mBufferList mBufferList: UnsafeMutablePointer<AudioBufferList>) } ``` |

Modified ScheduledAudioSlice.mBufferList

|  | Declaration |
| --- | --- |
| From | ``` var mBufferList: UnsafePointer<AudioBufferList> ``` |
| To | ``` var mBufferList: UnsafeMutablePointer<AudioBufferList> ``` |

Modified ScheduledAudioSlice.mCompletionProcUserData

|  | Declaration |
| --- | --- |
| From | ``` var mCompletionProcUserData: UnsafePointer<()> ``` |
| To | ``` var mCompletionProcUserData: UnsafeMutablePointer<Void> ``` |

Modified ScheduledAudioSlice.mReserved2

|  | Declaration |
| --- | --- |
| From | ``` var mReserved2: UnsafePointer<()> ``` |
| To | ``` var mReserved2: UnsafeMutablePointer<Void> ``` |

Modified AUInputSamplesInOutputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AUInputSamplesInOutputCallback = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<AudioTimeStamp>, Float64, Float64) -> Void)> ``` |
| To | ``` typealias AUInputSamplesInOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioTimeStamp>, Float64, Float64) -> Void)> ``` |

Modified AUMIDIOutputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AUMIDIOutputCallback = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<AudioTimeStamp>, UInt32, COpaquePointer) -> OSStatus)> ``` |
| To | ``` typealias AUMIDIOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioTimeStamp>, UInt32, COpaquePointer) -> OSStatus)> ``` |

Modified AURenderCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AURenderCallback = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<AudioUnitRenderActionFlags>, ConstUnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus)> ``` |
| To | ``` typealias AURenderCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus)> ``` |

Modified AudioCodecAppendInputBufferList(AudioCodec, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioCodecAppendInputBufferList(_ inCodec: AudioCodec, _ inBufferList: ConstUnsafePointer<AudioBufferList>, _ ioNumberPackets: UnsafePointer<UInt32>, _ inPacketDescription: ConstUnsafePointer<AudioStreamPacketDescription>, _ outBytesConsumed: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioCodecAppendInputBufferList(_ inCodec: AudioCodec, _ inBufferList: UnsafePointer<AudioBufferList>, _ ioNumberPackets: UnsafeMutablePointer<UInt32>, _ inPacketDescription: UnsafePointer<AudioStreamPacketDescription>, _ outBytesConsumed: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.7 |

Modified AudioCodecAppendInputBufferListProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecAppendInputBufferListProc = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<AudioBufferList>, UnsafePointer<UInt32>, ConstUnsafePointer<AudioStreamPacketDescription>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecAppendInputBufferListProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioCodecAppendInputData(AudioCodec, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioCodecAppendInputData(_ inCodec: AudioCodec, _ inInputData: ConstUnsafePointer<()>, _ ioInputDataByteSize: UnsafePointer<UInt32>, _ ioNumberPackets: UnsafePointer<UInt32>, _ inPacketDescription: ConstUnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioCodecAppendInputData(_ inCodec: AudioCodec, _ inInputData: UnsafePointer<Void>, _ ioInputDataByteSize: UnsafeMutablePointer<UInt32>, _ ioNumberPackets: UnsafeMutablePointer<UInt32>, _ inPacketDescription: UnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` | OS X 10.2 |

Modified AudioCodecAppendInputDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecAppendInputDataProc = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<()>, UnsafePointer<UInt32>, UnsafePointer<UInt32>, ConstUnsafePointer<AudioStreamPacketDescription>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecAppendInputDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>) -> OSStatus)> ``` |

Modified AudioCodecGetProperty(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioCodecGetProperty(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioCodecGetProperty(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioCodecGetPropertyInfo(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioCodecGetPropertyInfo(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ outSize: UnsafePointer<UInt32>, _ outWritable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioCodecGetPropertyInfo(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.2 |

Modified AudioCodecGetPropertyInfoProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecGetPropertyInfoProc = CFunctionPointer<((UnsafePointer<()>, AudioCodecPropertyID, UnsafePointer<UInt32>, UnsafePointer<Boolean>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecGetPropertyInfoProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus)> ``` |

Modified AudioCodecGetPropertyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecGetPropertyProc = CFunctionPointer<((UnsafePointer<()>, AudioCodecPropertyID, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecGetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioCodecInitialize(AudioCodec, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioCodecInitialize(_ inCodec: AudioCodec, _ inInputFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inOutputFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inMagicCookie: ConstUnsafePointer<()>, _ inMagicCookieByteSize: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioCodecInitialize(_ inCodec: AudioCodec, _ inInputFormat: UnsafePointer<AudioStreamBasicDescription>, _ inOutputFormat: UnsafePointer<AudioStreamBasicDescription>, _ inMagicCookie: UnsafePointer<Void>, _ inMagicCookieByteSize: UInt32) -> OSStatus ``` | OS X 10.2 |

Modified AudioCodecInitializeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecInitializeProc = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<AudioStreamBasicDescription>, ConstUnsafePointer<AudioStreamBasicDescription>, ConstUnsafePointer<()>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecInitializeProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<Void>, UInt32) -> OSStatus)> ``` |

Modified AudioCodecProduceOutputBufferList(AudioCodec, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioCodecProduceOutputBufferList(_ inCodec: AudioCodec, _ ioBufferList: UnsafePointer<AudioBufferList>, _ ioNumberPackets: UnsafePointer<UInt32>, _ outPacketDescription: UnsafePointer<AudioStreamPacketDescription>, _ outStatus: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioCodecProduceOutputBufferList(_ inCodec: AudioCodec, _ ioBufferList: UnsafeMutablePointer<AudioBufferList>, _ ioNumberPackets: UnsafeMutablePointer<UInt32>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>, _ outStatus: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.7 |

Modified AudioCodecProduceOutputBufferListProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecProduceOutputBufferListProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<AudioBufferList>, UnsafePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecProduceOutputBufferListProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioCodecProduceOutputPackets(AudioCodec, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioCodecProduceOutputPackets(_ inCodec: AudioCodec, _ outOutputData: UnsafePointer<()>, _ ioOutputDataByteSize: UnsafePointer<UInt32>, _ ioNumberPackets: UnsafePointer<UInt32>, _ outPacketDescription: UnsafePointer<AudioStreamPacketDescription>, _ outStatus: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioCodecProduceOutputPackets(_ inCodec: AudioCodec, _ outOutputData: UnsafeMutablePointer<Void>, _ ioOutputDataByteSize: UnsafeMutablePointer<UInt32>, _ ioNumberPackets: UnsafeMutablePointer<UInt32>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>, _ outStatus: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.2 |

Modified AudioCodecProduceOutputPacketsProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecProduceOutputPacketsProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, UnsafePointer<UInt32>, UnsafePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecProduceOutputPacketsProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioCodecReset(AudioCodec) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified AudioCodecResetProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecResetProc = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecResetProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioCodecSetProperty(AudioCodec, AudioCodecPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioCodecSetProperty(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioCodecSetProperty(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioCodecSetPropertyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecSetPropertyProc = CFunctionPointer<((UnsafePointer<()>, AudioCodecPropertyID, UInt32, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecSetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioCodecPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus)> ``` |

Modified AudioCodecUninitialize(AudioCodec) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified AudioCodecUninitializeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecUninitializeProc = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecUninitializeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioComponentCopyConfigurationInfo(_ inComponent: AudioComponent, _ outConfigurationInfo: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioComponentCopyConfigurationInfo(_ inComponent: AudioComponent, _ outConfigurationInfo: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.7 |

Modified AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioComponentCopyName(_ inComponent: AudioComponent, _ outName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioComponentCopyName(_ inComponent: AudioComponent, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.6 |

Modified AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioComponentCount(_ inDesc: ConstUnsafePointer<AudioComponentDescription>) -> UInt32 ``` | OS X 10.10 |
| To | ``` func AudioComponentCount(_ inDesc: UnsafePointer<AudioComponentDescription>) -> UInt32 ``` | OS X 10.6 |

Modified AudioComponentFactoryFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioComponentFactoryFunction = CFunctionPointer<((ConstUnsafePointer<AudioComponentDescription>) -> UnsafePointer<AudioComponentPlugInInterface>)> ``` |
| To | ``` typealias AudioComponentFactoryFunction = CFunctionPointer<((UnsafePointer<AudioComponentDescription>) -> UnsafeMutablePointer<AudioComponentPlugInInterface>)> ``` |

Modified AudioComponentFindNext(AudioComponent, UnsafePointer<AudioComponentDescription>) -> AudioComponent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioComponentFindNext(_ inComponent: AudioComponent, _ inDesc: ConstUnsafePointer<AudioComponentDescription>) -> AudioComponent ``` | OS X 10.10 |
| To | ``` func AudioComponentFindNext(_ inComponent: AudioComponent, _ inDesc: UnsafePointer<AudioComponentDescription>) -> AudioComponent ``` | OS X 10.6 |

Modified AudioComponentGetDescription(AudioComponent, UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioComponentGetDescription(_ inComponent: AudioComponent, _ outDesc: UnsafePointer<AudioComponentDescription>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioComponentGetDescription(_ inComponent: AudioComponent, _ outDesc: UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus ``` | OS X 10.6 |

Modified AudioComponentGetVersion(AudioComponent, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioComponentGetVersion(_ inComponent: AudioComponent, _ outVersion: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioComponentGetVersion(_ inComponent: AudioComponent, _ outVersion: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.6 |

Modified AudioComponentInstance

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioComponentInstance = UnsafePointer<ComponentInstanceRecord> ``` |
| To | ``` typealias AudioComponentInstance = UnsafeMutablePointer<ComponentInstanceRecord> ``` |

Modified AudioComponentInstanceCanDo(AudioComponentInstance, Int16) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified AudioComponentInstanceDispose(AudioComponentInstance) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified AudioComponentInstanceGetComponent(AudioComponentInstance) -> AudioComponent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified AudioComponentInstanceNew(AudioComponent, UnsafeMutablePointer<AudioComponentInstance>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioComponentInstanceNew(_ inComponent: AudioComponent, _ outInstance: UnsafePointer<AudioComponentInstance>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioComponentInstanceNew(_ inComponent: AudioComponent, _ outInstance: UnsafeMutablePointer<AudioComponentInstance>) -> OSStatus ``` | OS X 10.6 |

Modified AudioComponentRegister(UnsafePointer<AudioComponentDescription>, CFString!, UInt32, AudioComponentFactoryFunction) -> AudioComponent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioComponentRegister(_ inDesc: ConstUnsafePointer<AudioComponentDescription>, _ inName: CFString!, _ inVersion: UInt32, _ inFactory: AudioComponentFactoryFunction) -> AudioComponent ``` | OS X 10.10 |
| To | ``` func AudioComponentRegister(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString!, _ inVersion: UInt32, _ inFactory: AudioComponentFactoryFunction) -> AudioComponent ``` | OS X 10.7 |

Modified AudioOutputUnitStart(AudioUnit) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioOutputUnitStartProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioOutputUnitStartProc = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioOutputUnitStartProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioOutputUnitStop(AudioUnit) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioOutputUnitStopProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioOutputUnitStopProc = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioOutputUnitStopProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioUnitAddPropertyListener(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitAddPropertyListener(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioUnitPropertyListenerProc, _ inProcUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitAddPropertyListener(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioUnitPropertyListenerProc, _ inProcUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.0 |

Modified AudioUnitAddPropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitAddPropertyListenerProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitAddPropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioUnitAddRenderNotify(AudioUnit, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitAddRenderNotify(_ inUnit: AudioUnit, _ inProc: AURenderCallback, _ inProcUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitAddRenderNotify(_ inUnit: AudioUnit, _ inProc: AURenderCallback, _ inProcUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioUnitAddRenderNotifyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitAddRenderNotifyProc = CFunctionPointer<((UnsafePointer<()>, AURenderCallback, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitAddRenderNotifyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioUnitComplexRenderProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitComplexRenderProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<AudioUnitRenderActionFlags>, ConstUnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, UnsafePointer<AudioBufferList>, UnsafePointer<()>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitComplexRenderProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioUnitGetParameter(AudioUnit, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitGetParameter(_ inUnit: AudioUnit, _ inID: AudioUnitParameterID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outValue: UnsafePointer<AudioUnitParameterValue>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitGetParameter(_ inUnit: AudioUnit, _ inID: AudioUnitParameterID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outValue: UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus ``` | OS X 10.0 |

Modified AudioUnitGetParameterProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitGetParameterProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafePointer<AudioUnitParameterValue>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitGetParameterProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus)> ``` |

Modified AudioUnitGetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitGetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outData: UnsafePointer<()>, _ ioDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitGetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outData: UnsafeMutablePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.0 |

Modified AudioUnitGetPropertyInfo(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitGetPropertyInfo(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outDataSize: UnsafePointer<UInt32>, _ outWritable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitGetPropertyInfo(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.0 |

Modified AudioUnitGetPropertyInfoProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitGetPropertyInfoProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafePointer<UInt32>, UnsafePointer<Boolean>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitGetPropertyInfoProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus)> ``` |

Modified AudioUnitGetPropertyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitGetPropertyProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafePointer<()>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitGetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioUnitInitialize(AudioUnit) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioUnitInitializeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitInitializeProc = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitInitializeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioUnitProcess(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitProcess(_ inUnit: AudioUnit, _ ioActionFlags: UnsafePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: ConstUnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ ioData: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitProcess(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.7 |

Modified AudioUnitProcessMultiple(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitProcessMultiple(_ inUnit: AudioUnit, _ ioActionFlags: UnsafePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: ConstUnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ inNumberInputBufferLists: UInt32, _ inInputBufferLists: UnsafePointer<ConstUnsafePointer<AudioBufferList>>, _ inNumberOutputBufferLists: UInt32, _ ioOutputBufferLists: UnsafePointer<UnsafePointer<AudioBufferList>>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitProcessMultiple(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ inNumberInputBufferLists: UInt32, _ inInputBufferLists: UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, _ inNumberOutputBufferLists: UInt32, _ ioOutputBufferLists: UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus ``` | OS X 10.7 |

Modified AudioUnitProcessMultipleProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitProcessMultipleProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<AudioUnitRenderActionFlags>, ConstUnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafePointer<ConstUnsafePointer<AudioBufferList>>, UInt32, UnsafePointer<UnsafePointer<AudioBufferList>>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitProcessMultipleProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus)> ``` |

Modified AudioUnitProcessProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitProcessProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<AudioUnitRenderActionFlags>, ConstUnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitProcessProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus)> ``` |

Modified AudioUnitPropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitPropertyListenerProc = CFunctionPointer<((UnsafePointer<()>, AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement) -> Void)> ``` |
| To | ``` typealias AudioUnitPropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement) -> Void)> ``` |

Modified AudioUnitRemovePropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitRemovePropertyListenerProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitPropertyID, AudioUnitPropertyListenerProc) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitRemovePropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc) -> OSStatus)> ``` |

Modified AudioUnitRemovePropertyListenerWithUserData(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitRemovePropertyListenerWithUserData(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioUnitPropertyListenerProc, _ inProcUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitRemovePropertyListenerWithUserData(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioUnitPropertyListenerProc, _ inProcUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioUnitRemovePropertyListenerWithUserDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitRemovePropertyListenerWithUserDataProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitRemovePropertyListenerWithUserDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioUnitRemoveRenderNotify(AudioUnit, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitRemoveRenderNotify(_ inUnit: AudioUnit, _ inProc: AURenderCallback, _ inProcUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitRemoveRenderNotify(_ inUnit: AudioUnit, _ inProc: AURenderCallback, _ inProcUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioUnitRemoveRenderNotifyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitRemoveRenderNotifyProc = CFunctionPointer<((UnsafePointer<()>, AURenderCallback, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitRemoveRenderNotifyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioUnitRender(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitRender(_ inUnit: AudioUnit, _ ioActionFlags: UnsafePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: ConstUnsafePointer<AudioTimeStamp>, _ inOutputBusNumber: UInt32, _ inNumberFrames: UInt32, _ ioData: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitRender(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inOutputBusNumber: UInt32, _ inNumberFrames: UInt32, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.2 |

Modified AudioUnitRenderProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitRenderProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<AudioUnitRenderActionFlags>, ConstUnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitRenderProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus)> ``` |

Modified AudioUnitReset(AudioUnit, AudioUnitScope, AudioUnitElement) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioUnitResetProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitResetProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitScope, AudioUnitElement) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitResetProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitScope, AudioUnitElement) -> OSStatus)> ``` |

Modified AudioUnitScheduleParameters(AudioUnit, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitScheduleParameters(_ inUnit: AudioUnit, _ inParameterEvent: ConstUnsafePointer<AudioUnitParameterEvent>, _ inNumParamEvents: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitScheduleParameters(_ inUnit: AudioUnit, _ inParameterEvent: UnsafePointer<AudioUnitParameterEvent>, _ inNumParamEvents: UInt32) -> OSStatus ``` | OS X 10.2 |

Modified AudioUnitScheduleParametersProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitScheduleParametersProc = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitScheduleParametersProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus)> ``` |

Modified AudioUnitSetParameter(AudioUnit, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioUnitSetParameterProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitSetParameterProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitSetParameterProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus)> ``` |

Modified AudioUnitSetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioUnitSetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ inData: ConstUnsafePointer<()>, _ inDataSize: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioUnitSetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ inData: UnsafePointer<Void>, _ inDataSize: UInt32) -> OSStatus ``` | OS X 10.0 |

Modified AudioUnitSetPropertyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitSetPropertyProc = CFunctionPointer<((UnsafePointer<()>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, ConstUnsafePointer<()>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitSetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafePointer<Void>, UInt32) -> OSStatus)> ``` |

Modified AudioUnitUninitialize(AudioUnit) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioUnitUninitializeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitUninitializeProc = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitUninitializeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified HostCallback_GetBeatAndTempo

|  | Declaration |
| --- | --- |
| From | ``` typealias HostCallback_GetBeatAndTempo = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<Float64>, UnsafePointer<Float64>) -> OSStatus)> ``` |
| To | ``` typealias HostCallback_GetBeatAndTempo = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus)> ``` |

Modified HostCallback_GetMusicalTimeLocation

|  | Declaration |
| --- | --- |
| From | ``` typealias HostCallback_GetMusicalTimeLocation = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<UInt32>, UnsafePointer<Float32>, UnsafePointer<UInt32>, UnsafePointer<Float64>) -> OSStatus)> ``` |
| To | ``` typealias HostCallback_GetMusicalTimeLocation = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Float32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Float64>) -> OSStatus)> ``` |

Modified HostCallback_GetTransportState

|  | Declaration |
| --- | --- |
| From | ``` typealias HostCallback_GetTransportState = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<Boolean>, UnsafePointer<Boolean>, UnsafePointer<Float64>, UnsafePointer<Boolean>, UnsafePointer<Float64>, UnsafePointer<Float64>) -> OSStatus)> ``` |
| To | ``` typealias HostCallback_GetTransportState = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus)> ``` |

Modified HostCallback_GetTransportState2

|  | Declaration |
| --- | --- |
| From | ``` typealias HostCallback_GetTransportState2 = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<Boolean>, UnsafePointer<Boolean>, UnsafePointer<Boolean>, UnsafePointer<Float64>, UnsafePointer<Boolean>, UnsafePointer<Float64>, UnsafePointer<Float64>) -> OSStatus)> ``` |
| To | ``` typealias HostCallback_GetTransportState2 = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus)> ``` |

Modified MusicDeviceMIDIEvent(MusicDeviceComponent, UInt32, UInt32, UInt32, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicDeviceMIDIEventProc

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicDeviceMIDIEventProc = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32, UInt32, UInt32) -> OSStatus)> ``` |
| To | ``` typealias MusicDeviceMIDIEventProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> OSStatus)> ``` |

Modified MusicDeviceStartNote(MusicDeviceComponent, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicDeviceStartNote(_ inUnit: MusicDeviceComponent, _ inInstrument: MusicDeviceInstrumentID, _ inGroupID: MusicDeviceGroupID, _ outNoteInstanceID: UnsafePointer<NoteInstanceID>, _ inOffsetSampleFrame: UInt32, _ inParams: ConstUnsafePointer<MusicDeviceNoteParams>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicDeviceStartNote(_ inUnit: MusicDeviceComponent, _ inInstrument: MusicDeviceInstrumentID, _ inGroupID: MusicDeviceGroupID, _ outNoteInstanceID: UnsafeMutablePointer<NoteInstanceID>, _ inOffsetSampleFrame: UInt32, _ inParams: UnsafePointer<MusicDeviceNoteParams>) -> OSStatus ``` | OS X 10.0 |

Modified MusicDeviceStartNoteProc

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicDeviceStartNoteProc = CFunctionPointer<((UnsafePointer<()>, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafePointer<NoteInstanceID>, UInt32, ConstUnsafePointer<MusicDeviceNoteParams>) -> OSStatus)> ``` |
| To | ``` typealias MusicDeviceStartNoteProc = CFunctionPointer<((UnsafeMutablePointer<Void>, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus)> ``` |

Modified MusicDeviceStopNote(MusicDeviceComponent, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicDeviceStopNoteProc

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicDeviceStopNoteProc = CFunctionPointer<((UnsafePointer<()>, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus)> ``` |
| To | ``` typealias MusicDeviceStopNoteProc = CFunctionPointer<((UnsafeMutablePointer<Void>, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus)> ``` |

Modified MusicDeviceSysEx(MusicDeviceComponent, UnsafePointer<UInt8>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicDeviceSysEx(_ inUnit: MusicDeviceComponent, _ inData: ConstUnsafePointer<UInt8>, _ inLength: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicDeviceSysEx(_ inUnit: MusicDeviceComponent, _ inData: UnsafePointer<UInt8>, _ inLength: UInt32) -> OSStatus ``` | OS X 10.0 |

Modified MusicDeviceSysExProc

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicDeviceSysExProc = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<UInt8>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias MusicDeviceSysExProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> OSStatus)> ``` |

Modified ScheduledAudioFileRegionCompletionProc

|  | Declaration |
| --- | --- |
| From | ``` typealias ScheduledAudioFileRegionCompletionProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<ScheduledAudioFileRegion>, OSStatus) -> Void)> ``` |
| To | ``` typealias ScheduledAudioFileRegionCompletionProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<ScheduledAudioFileRegion>, OSStatus) -> Void)> ``` |

Modified ScheduledAudioSliceCompletionProc

|  | Declaration |
| --- | --- |
| From | ``` typealias ScheduledAudioSliceCompletionProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<ScheduledAudioSlice>) -> Void)> ``` |
| To | ``` typealias ScheduledAudioSliceCompletionProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<ScheduledAudioSlice>) -> Void)> ``` |

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
