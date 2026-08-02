---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/AudioUnit.html
archived_at: '2026-07-18T02:53:19.961682Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AudioUnit Changes for Swift

### AudioUnit

Removed AudioComponentPlugInInterface.init()Removed AudioComponentPlugInInterface.init(Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>, Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>, Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>, reserved: UnsafeMutablePointer<Void>)Removed AudioUnitCocoaViewInfo.init()Removed AudioUnitCocoaViewInfo.init(mCocoaAUViewBundleLocation: Unmanaged<CFURL>!, mCocoaAUViewClass: (Unmanaged<CFString>?))Removed AudioUnitConnection.init()Removed AudioUnitConnection.init(sourceAudioUnit: AudioUnit, sourceOutputNumber: UInt32, destInputNumber: UInt32)Removed AudioUnitExternalBuffer.init()Removed AudioUnitExternalBuffer.init(buffer: UnsafeMutablePointer<UInt8>, size: UInt32)Removed AudioUnitMeterClipping.init(peakValueSinceLastCall: Float32, sawInfinity: Boolean, sawNotANumber: Boolean)Removed AudioUnitParameter.init()Removed AudioUnitParameter.init(mAudioUnit: AudioUnit, mParameterID: AudioUnitParameterID, mScope: AudioUnitScope, mElement: AudioUnitElement)Removed AudioUnitParameterInfo.init(name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName: Unmanaged<CFString>!, clumpID: UInt32, cfNameString: Unmanaged<CFString>!, unit: AudioUnitParameterUnit, minValue: AudioUnitParameterValue, maxValue: AudioUnitParameterValue, defaultValue: AudioUnitParameterValue, flags: UInt32)Removed AudioUnitParameterNameInfo.init(inID: AudioUnitParameterID, inDesiredLength: Int32, outName: Unmanaged<CFString>!)Removed AudioUnitParameterStringFromValue.init()Removed AudioUnitParameterStringFromValue.init(inParamID: AudioUnitParameterID, inValue: UnsafePointer<AudioUnitParameterValue>, outString: Unmanaged<CFString>!)Removed AudioUnitParameterValueFromString.init()Removed AudioUnitParameterValueFromString.init(inParamID: AudioUnitParameterID, inString: Unmanaged<CFString>!, outValue: AudioUnitParameterValue)Removed AudioUnitParameterValueName.init()Removed AudioUnitParameterValueName.init(inParamID: AudioUnitParameterID, inValue: UnsafePointer<Float32>, outName: Unmanaged<CFString>!)Removed AudioUnitProperty.init()Removed AudioUnitProperty.init(mAudioUnit: AudioUnit, mPropertyID: AudioUnitPropertyID, mScope: AudioUnitScope, mElement: AudioUnitElement)Removed AUHostIdentifier.init()Removed AUHostIdentifier.init(hostName: Unmanaged<CFString>!, hostVersion: AUNumVersion)Removed AUHostVersionIdentifier.init()Removed AUHostVersionIdentifier.init(hostName: Unmanaged<CFString>!, hostVersion: UInt32)Removed AUInputSamplesInOutputCallbackStruct.init()Removed AUInputSamplesInOutputCallbackStruct.init(inputToOutputCallback: AUInputSamplesInOutputCallback, userData: UnsafeMutablePointer<Void>)Removed AUMIDIOutputCallbackStruct.init()Removed AUMIDIOutputCallbackStruct.init(midiOutputCallback: AUMIDIOutputCallback, userData: UnsafeMutablePointer<Void>)Removed AUParameterMIDIMapping.init(mScope: AudioUnitScope, mElement: AudioUnitElement, mParameterID: AudioUnitParameterID, mFlags: UInt32, mSubRangeMin: AudioUnitParameterValue, mSubRangeMax: AudioUnitParameterValue, mStatus: UInt8, mData1: UInt8, reserved1: UInt8, reserved2: UInt8, reserved3: UInt32)Removed AUPreset.init()Removed AUPreset.init(presetNumber: Int32, presetName: Unmanaged<CFString>!)Removed AURenderCallbackStruct.init()Removed AURenderCallbackStruct.init(inputProc: AURenderCallback, inputProcRefCon: UnsafeMutablePointer<Void>)Removed AUSamplerBankPresetData.init()Removed AUSamplerBankPresetData.init(bankURL: Unmanaged<CFURL>!, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8, reserved: UInt8)Removed AUSamplerInstrumentData.init()Removed AUSamplerInstrumentData.init(fileURL: Unmanaged<CFURL>!, instrumentType: UInt8, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8)Removed HostCallbackInfo.init(hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc: HostCallback_GetBeatAndTempo, musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation, transportStateProc: HostCallback_GetTransportState, transportStateProc2: HostCallback_GetTransportState2)Removed ScheduledAudioFileRegion.init()Removed ScheduledAudioSlice.init()Removed ScheduledAudioSlice.init(mTimeStamp: AudioTimeStamp, mCompletionProc: ScheduledAudioSliceCompletionProc, mCompletionProcUserData: UnsafeMutablePointer<Void>, mFlags: UInt32, mReserved: UInt32, mReserved2: UnsafeMutablePointer<Void>, mNumberFrames: UInt32, mBufferList: UnsafeMutablePointer<AudioBufferList>)Removed AudioUnitParameterUnitRemoved AudioUnitRenderActionFlagsRemoved AUParameterEventTypeRemoved k3DMixerAttenuationCurve_ExponentialRemoved k3DMixerAttenuationCurve_InverseRemoved k3DMixerAttenuationCurve_LinearRemoved k3DMixerAttenuationCurve_PowerRemoved k3DMixerRenderingFlags_ConstantReverbBlendRemoved k3DMixerRenderingFlags_DistanceAttenuationRemoved k3DMixerRenderingFlags_DistanceDiffusionRemoved k3DMixerRenderingFlags_DistanceFilterRemoved k3DMixerRenderingFlags_DopplerShiftRemoved k3DMixerRenderingFlags_InterAuralDelayRemoved k3DMixerRenderingFlags_LinearDistanceAttenuationRemoved kAudioComponentFlag_SandboxSafeRemoved kAudioComponentFlag_UnsearchableRemoved kAudioOfflineUnitRenderAction_CompleteRemoved kAudioOfflineUnitRenderAction_PreflightRemoved kAudioOfflineUnitRenderAction_RenderRemoved kAudioSettingsFlags_ExpertParameterRemoved kAudioSettingsFlags_InvisibleParameterRemoved kAudioSettingsFlags_MetaParameterRemoved kAudioSettingsFlags_UserInterfaceParameterRemoved kAudioUnitParameterFlag_CanRampRemoved kAudioUnitParameterFlag_CFNameReleaseRemoved kAudioUnitParameterFlag_DisplayCubedRemoved kAudioUnitParameterFlag_DisplayCubeRootRemoved kAudioUnitParameterFlag_DisplayExponentialRemoved kAudioUnitParameterFlag_DisplayLogarithmicRemoved kAudioUnitParameterFlag_DisplayMaskRemoved kAudioUnitParameterFlag_DisplaySquaredRemoved kAudioUnitParameterFlag_DisplaySquareRootRemoved kAudioUnitParameterFlag_ExpertModeRemoved kAudioUnitParameterFlag_HasCFNameStringRemoved kAudioUnitParameterFlag_HasClumpRemoved kAudioUnitParameterFlag_IsElementMetaRemoved kAudioUnitParameterFlag_IsGlobalMetaRemoved kAudioUnitParameterFlag_IsHighResolutionRemoved kAudioUnitParameterFlag_IsReadableRemoved kAudioUnitParameterFlag_IsWritableRemoved kAudioUnitParameterFlag_MeterReadOnlyRemoved kAudioUnitParameterFlag_NonRealTimeRemoved kAudioUnitParameterFlag_OmitFromPresetsRemoved kAudioUnitParameterFlag_PlotHistoryRemoved kAudioUnitParameterFlag_ValuesHaveStringsRemoved kAudioUnitParameterUnit_AbsoluteCentsRemoved kAudioUnitParameterUnit_BeatsRemoved kAudioUnitParameterUnit_BooleanRemoved kAudioUnitParameterUnit_BPMRemoved kAudioUnitParameterUnit_CentsRemoved kAudioUnitParameterUnit_CustomUnitRemoved kAudioUnitParameterUnit_DecibelsRemoved kAudioUnitParameterUnit_DegreesRemoved kAudioUnitParameterUnit_EqualPowerCrossfadeRemoved kAudioUnitParameterUnit_GenericRemoved kAudioUnitParameterUnit_HertzRemoved kAudioUnitParameterUnit_IndexedRemoved kAudioUnitParameterUnit_LinearGainRemoved kAudioUnitParameterUnit_MetersRemoved kAudioUnitParameterUnit_MIDIControllerRemoved kAudioUnitParameterUnit_MIDINoteNumberRemoved kAudioUnitParameterUnit_MillisecondsRemoved kAudioUnitParameterUnit_MixerFaderCurve1Removed kAudioUnitParameterUnit_OctavesRemoved kAudioUnitParameterUnit_PanRemoved kAudioUnitParameterUnit_PercentRemoved kAudioUnitParameterUnit_PhaseRemoved kAudioUnitParameterUnit_RateRemoved kAudioUnitParameterUnit_RatioRemoved kAudioUnitParameterUnit_RelativeSemiTonesRemoved kAudioUnitParameterUnit_SampleFramesRemoved kAudioUnitParameterUnit_SecondsRemoved kAudioUnitRenderAction_DoNotCheckRenderArgsRemoved kAudioUnitRenderAction_OutputIsSilenceRemoved kAudioUnitRenderAction_PostRenderRemoved kAudioUnitRenderAction_PostRenderErrorRemoved kAudioUnitRenderAction_PreRenderRemoved kAUParameterMIDIMapping_AnyChannelFlagRemoved kAUParameterMIDIMapping_AnyNoteFlagRemoved kAUParameterMIDIMapping_BipolarRemoved kAUParameterMIDIMapping_Bipolar_OnRemoved kAUParameterMIDIMapping_SubRangeRemoved kAUParameterMIDIMapping_ToggleRemoved kParameterEvent_ImmediateRemoved kParameterEvent_RampedRemoved kReverbRoomType_CathedralRemoved kReverbRoomType_LargeChamberRemoved kReverbRoomType_LargeHallRemoved kReverbRoomType_LargeHall2Removed kReverbRoomType_LargeRoomRemoved kReverbRoomType_LargeRoom2Removed kReverbRoomType_MediumChamberRemoved kReverbRoomType_MediumHallRemoved kReverbRoomType_MediumHall2Removed kReverbRoomType_MediumHall3Removed kReverbRoomType_MediumRoomRemoved kReverbRoomType_PlateRemoved kReverbRoomType_SmallRoomRemoved kScheduledAudioSliceFlag_BeganToRenderRemoved kScheduledAudioSliceFlag_BeganToRenderLateRemoved kScheduledAudioSliceFlag_CompleteRemoved kScheduledAudioSliceFlag_InterruptRemoved kScheduledAudioSliceFlag_InterruptAtLoopRemoved kScheduledAudioSliceFlag_LoopRemoved kSpatializationAlgorithm_EqualPowerPanningRemoved kSpatializationAlgorithm_HRTFRemoved kSpatializationAlgorithm_SoundFieldRemoved kSpatializationAlgorithm_SphericalHeadRemoved kSpatializationAlgorithm_StereoPassThroughRemoved kSpatializationAlgorithm_VectorBasedPanningRemoved kSpatialMixerAttenuationCurve_ExponentialRemoved kSpatialMixerAttenuationCurve_InverseRemoved kSpatialMixerAttenuationCurve_LinearRemoved kSpatialMixerAttenuationCurve_PowerRemoved kSpatialMixerRenderingFlags_DistanceAttenuationRemoved kSpatialMixerRenderingFlags_InterAuralDelayAdded [AU3DMixerAttenuationCurve [enum]](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve)Added [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Exponential](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_exponential)Added [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Inverse](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_inverse)Added [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Linear](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_linear)Added [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Power](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_power)Added [AU3DMixerRenderingFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags)Added AU3DMixerRenderingFlags.init(rawValue: UInt32)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_ConstantReverbBlend](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_constantreverbblend)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_distanceattenuation)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceDiffusion](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/1439784-k3dmixerrenderingflags_distanced)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceFilter](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/1440885-k3dmixerrenderingflags_distancef)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DopplerShift](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_dopplershift)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_InterAuralDelay](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_interauraldelay)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_LinearDistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_lineardistanceattenuation)Added [AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounit)Added [AUAudioUnit.allocateRenderResources() throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387620-allocaterenderresources)Added [AUAudioUnit.allParameterValues](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387679-allparametervalues)Added [AUAudioUnit.audioUnitName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387640-audiounitname)Added [AUAudioUnit.canPerformInput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387551-canperforminput)Added [AUAudioUnit.canPerformOutput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387656-canperformoutput)Added [AUAudioUnit.canProcessInPlace](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387583-canprocessinplace)Added [AUAudioUnit.channelCapabilities](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387685-channelcapabilities)Added [AUAudioUnit.component](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387535-component)Added [AUAudioUnit.componentDescription](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387568-componentdescription)Added [AUAudioUnit.componentName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387566-componentname)Added [AUAudioUnit.componentVersion](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387555-componentversion)Added [AUAudioUnit.contextName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387553-contextname)Added [AUAudioUnit.currentPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387668-currentpreset)Added [AUAudioUnit.deallocateRenderResources()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387612-deallocaterenderresources)Added [AUAudioUnit.deviceID](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387683-deviceid)Added [AUAudioUnit.factoryPresets](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387526-factorypresets)Added [AUAudioUnit.fullState](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387500-fullstate)Added [AUAudioUnit.fullStateForDocument](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387630-fullstatefordocument)Added [AUAudioUnit.init(componentDescription: AudioComponentDescription) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387570-init)Added [AUAudioUnit.init(componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387664-initwithcomponentdescription)Added [AUAudioUnit.inputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387636-inputbusses)Added [AUAudioUnit.inputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387660-inputenabled)Added [AUAudioUnit.inputHandler](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387616-inputhandler)Added [AUAudioUnit.instantiateWithComponentDescription(_: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AUAudioUnit?, NSError?) -> Void) [class]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387606-instantiate)Added [AUAudioUnit.internalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439864-internalrenderblock)Added [AUAudioUnit.latency](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387675-latency)Added [AUAudioUnit.manufacturerName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387681-manufacturername)Added [AUAudioUnit.maximumFramesToRender](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387654-maximumframestorender)Added [AUAudioUnit.musicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387669-musicalcontextblock)Added [AUAudioUnit.musicDeviceOrEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387497-ismusicdeviceoreffect)Added [AUAudioUnit.outputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387503-outputbusses)Added [AUAudioUnit.outputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387646-outputenabled)Added [AUAudioUnit.outputProvider](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387596-outputprovider)Added [AUAudioUnit.parametersForOverviewWithCount(_: Int) -> [NSNumber]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387549-parametersforoverview)Added [AUAudioUnit.parameterTree](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387650-parametertree)Added [AUAudioUnit.registerSubclass(_: AnyClass, asComponentDescription: AudioComponentDescription, name: String, version: UInt32) [class]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1438315-registersubclass)Added [AUAudioUnit.removeRenderObserver(_: Int)](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387564-removerenderobserver)Added [AUAudioUnit.renderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387687-renderblock)Added [AUAudioUnit.renderingOffline](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387578-renderingoffline)Added [AUAudioUnit.renderQuality](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387648-renderquality)Added [AUAudioUnit.renderResourcesAllocated](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387618-renderresourcesallocated)Added [AUAudioUnit.reset()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387658-reset)Added [AUAudioUnit.scheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387576-schedulemidieventblock)Added [AUAudioUnit.scheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387677-scheduleparameterblock)Added [AUAudioUnit.setDeviceID(_: AudioObjectID) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387608-setdeviceid)Added [AUAudioUnit.setRenderResourcesAllocated(_: Bool)](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1440830-setrenderresourcesallocated)Added [AUAudioUnit.shouldBypassEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387545-shouldbypasseffect)Added [AUAudioUnit.shouldChangeToFormat(_: AVAudioFormat, forBus: AUAudioUnitBus) -> Bool](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439999-shouldchange)Added [AUAudioUnit.startHardware() throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387581-starthardware)Added [AUAudioUnit.stopHardware()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387642-stophardware)Added [AUAudioUnit.tailTime](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387614-tailtime)Added [AUAudioUnit.tokenByAddingRenderObserver(_: AURenderObserver) -> Int](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387509-token)Added [AUAudioUnit.transportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387559-transportstateblock)Added [AUAudioUnit.virtualMIDICableCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387666-virtualmidicablecount)Added [AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus)Added [AUAudioUnitBus.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387524-bustype)Added [AUAudioUnitBus.contextPresentationLatency](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387547-contextpresentationlatency)Added [AUAudioUnitBus.enabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387634-isenabled)Added [AUAudioUnitBus.format](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387689-format)Added [AUAudioUnitBus.index](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387557-index)Added [AUAudioUnitBus.init(format: AVAudioFormat) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440039-initwithformat)Added [AUAudioUnitBus.maximumChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1439855-maximumchannelcount)Added [AUAudioUnitBus.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387514-name)Added [AUAudioUnitBus.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387638-owneraudiounit)Added [AUAudioUnitBus.setFormat(_: AVAudioFormat) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387644-setformat)Added [AUAudioUnitBus.supportedChannelCounts](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440352-supportedchannelcounts)Added [AUAudioUnitBus.supportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387622-supportedchannellayouttags)Added [AUAudioUnitBusArray](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray)Added [AUAudioUnitBusArray.addObserverToAllBusses(_: NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387520-addobservertoallbusses)Added [AUAudioUnitBusArray.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387671-bustype)Added [AUAudioUnitBusArray.count](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387673-count)Added [AUAudioUnitBusArray.countChangeable](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387537-countchangeable)Added [AUAudioUnitBusArray.init(audioUnit: AUAudioUnit, busType: AUAudioUnitBusType)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387662-initwithaudiounit)Added [AUAudioUnitBusArray.init(audioUnit: AUAudioUnit, busType: AUAudioUnitBusType, busses: [AUAudioUnitBus])](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387516-initwithaudiounit)Added [AUAudioUnitBusArray.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387510-owneraudiounit)Added [AUAudioUnitBusArray.removeObserverFromAllBusses(_: NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387505-removeobserverfromallbusses)Added [AUAudioUnitBusArray.replaceBusses(_: [AUAudioUnitBus])](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1440520-replacebusses)Added [AUAudioUnitBusArray.setBusCount(_: Int) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387598-setbuscount)Added [AUAudioUnitBusArray.subscript(_: Int) -> AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387507-subscript)Added [AUAudioUnitBusType [enum]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype)Added [AUAudioUnitBusType.Input](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/input)Added [AUAudioUnitBusType.Output](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/output)Added [AUAudioUnitFactory](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory)Added [AUAudioUnitFactory.createAudioUnitWithComponentDescription(_: AudioComponentDescription) throws -> AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory/1440321-createaudiounitwithcomponentdesc)Added [AUAudioUnitPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset)Added [AUAudioUnitPreset.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387587-name)Added [AUAudioUnitPreset.number](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387626-number)Added [AUAudioUnitV2Bridge](https://developer.apple.com/documentation/audiotoolbox/auaudiounitv2bridge)Added [AUCocoaUIBase](https://developer.apple.com/documentation/audiotoolbox/aucocoauibase)Added [AUCocoaUIBase.interfaceVersion() -> UInt32](https://developer.apple.com/documentation/audiotoolbox/aucocoauibase/1395990-interfaceversion)Added [AUCocoaUIBase.uiViewForAudioUnit(_: AudioUnit, withSize: NSSize) -> NSView?](https://developer.apple.com/documentation/audiotoolbox/aucocoauibase/1395992-uiviewforaudiounit)Added [AudioComponentFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags)Added [AudioComponentFlags.CanLoadInProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/1410506-canloadinprocess)Added AudioComponentFlags.init(rawValue: UInt32)Added [AudioComponentFlags.IsV3AudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_isv3audiounit)Added [AudioComponentFlags.RequiresAsyncInstantiation](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_requiresasyncinstantiation)Added [AudioComponentFlags.SandboxSafe](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_sandboxsafe)Added [AudioComponentFlags.Unsearchable](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_unsearchable)Added [AudioComponentInstantiationOptions [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions)Added AudioComponentInstantiationOptions.init(rawValue: UInt32)Added [AudioComponentInstantiationOptions.LoadInProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions/kaudiocomponentinstantiation_loadinprocess)Added [AudioComponentInstantiationOptions.LoadOutOfProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions/kaudiocomponentinstantiation_loadoutofprocess)Added [AudioComponentValidationResult [enum]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult)Added [AudioComponentValidationResult.Failed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/failed)Added [AudioComponentValidationResult.Passed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_passed)Added [AudioComponentValidationResult.TimedOut](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/timedout)Added [AudioComponentValidationResult.UnauthorizedError_Init](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_unauthorizederror_init)Added [AudioComponentValidationResult.UnauthorizedError_Open](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/unauthorizederror_open)Added [AudioComponentValidationResult.Unknown](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/unknown)Added [AudioSettingsFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiosettingsflags)Added [AudioSettingsFlags.ExpertParameter](https://developer.apple.com/documentation/audiotoolbox/audiosettingsflags/kaudiosettingsflags_expertparameter)Added AudioSettingsFlags.init(rawValue: UInt32)Added [AudioSettingsFlags.InvisibleParameter](https://developer.apple.com/documentation/audiotoolbox/audiosettingsflags/kaudiosettingsflags_invisibleparameter)Added [AudioSettingsFlags.MetaParameter](https://developer.apple.com/documentation/audiotoolbox/audiosettingsflags/1438677-metaparameter)Added [AudioSettingsFlags.UserInterfaceParameter](https://developer.apple.com/documentation/audiotoolbox/audiosettingsflags/kaudiosettingsflags_userinterfaceparameter)Added AudioUnitMeterClipping.init(peakValueSinceLastCall: Float32, sawInfinity: DarwinBoolean, sawNotANumber: DarwinBoolean)Added AudioUnitParameterInfo.init(name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName: Unmanaged<CFString>?, clumpID: UInt32, cfNameString: Unmanaged<CFString>?, unit: AudioUnitParameterUnit, minValue: AudioUnitParameterValue, maxValue: AudioUnitParameterValue, defaultValue: AudioUnitParameterValue, flags: AudioUnitParameterOptions)Added AudioUnitParameterNameInfo.init(inID: AudioUnitParameterID, inDesiredLength: Int32, outName: Unmanaged<CFString>?)Added [AudioUnitParameterOptions [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions)Added [AudioUnitParameterOptions.Flag_CanRamp](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_canramp)Added [AudioUnitParameterOptions.Flag_CFNameRelease](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439788-flag_cfnamerelease)Added [AudioUnitParameterOptions.Flag_DisplayCubed](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439330-flag_displaycubed)Added [AudioUnitParameterOptions.Flag_DisplayCubeRoot](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440958-flag_displaycuberoot)Added [AudioUnitParameterOptions.Flag_DisplayExponential](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displayexponential)Added [AudioUnitParameterOptions.Flag_DisplayLogarithmic](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displaylogarithmic)Added [AudioUnitParameterOptions.Flag_DisplayMask](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displaymask)Added [AudioUnitParameterOptions.Flag_DisplaySquared](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440750-flag_displaysquared)Added [AudioUnitParameterOptions.Flag_DisplaySquareRoot](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1441018-flag_displaysquareroot)Added [AudioUnitParameterOptions.Flag_ExpertMode](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_expertmode)Added [AudioUnitParameterOptions.Flag_HasCFNameString](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_hascfnamestring)Added [AudioUnitParameterOptions.Flag_HasClump](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_hasclump)Added [AudioUnitParameterOptions.Flag_IsElementMeta](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439961-flag_iselementmeta)Added [AudioUnitParameterOptions.Flag_IsGlobalMeta](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_isglobalmeta)Added [AudioUnitParameterOptions.Flag_IsHighResolution](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_ishighresolution)Added [AudioUnitParameterOptions.Flag_IsReadable](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1438604-flag_isreadable)Added [AudioUnitParameterOptions.Flag_IsWritable](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440477-flag_iswritable)Added [AudioUnitParameterOptions.Flag_MeterReadOnly](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439379-flag_meterreadonly)Added [AudioUnitParameterOptions.Flag_NonRealTime](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_nonrealtime)Added [AudioUnitParameterOptions.Flag_OmitFromPresets](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_omitfrompresets)Added [AudioUnitParameterOptions.Flag_PlotHistory](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_plothistory)Added [AudioUnitParameterOptions.Flag_ValuesHaveStrings](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440179-flag_valueshavestrings)Added AudioUnitParameterOptions.init(rawValue: UInt32)Added [AudioUnitParameterUnit [enum]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit)Added [AudioUnitParameterUnit.AbsoluteCents](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_absolutecents)Added [AudioUnitParameterUnit.Beats](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/beats)Added [AudioUnitParameterUnit.Boolean](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_boolean)Added [AudioUnitParameterUnit.BPM](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_bpm)Added [AudioUnitParameterUnit.Cents](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_cents)Added [AudioUnitParameterUnit.CustomUnit](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/customunit)Added [AudioUnitParameterUnit.Decibels](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_decibels)Added [AudioUnitParameterUnit.Degrees](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_degrees)Added [AudioUnitParameterUnit.EqualPowerCrossfade](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_equalpowercrossfade)Added [AudioUnitParameterUnit.Generic](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/generic)Added [AudioUnitParameterUnit.Hertz](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/hertz)Added [AudioUnitParameterUnit.Indexed](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/indexed)Added [AudioUnitParameterUnit.LinearGain](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_lineargain)Added [AudioUnitParameterUnit.Meters](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/meters)Added [AudioUnitParameterUnit.MIDIController](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/midicontroller)Added [AudioUnitParameterUnit.MIDINoteNumber](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/midinotenumber)Added [AudioUnitParameterUnit.Milliseconds](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/milliseconds)Added [AudioUnitParameterUnit.MixerFaderCurve1](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/mixerfadercurve1)Added [AudioUnitParameterUnit.Octaves](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_octaves)Added [AudioUnitParameterUnit.Pan](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_pan)Added [AudioUnitParameterUnit.Percent](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_percent)Added [AudioUnitParameterUnit.Phase](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_phase)Added [AudioUnitParameterUnit.Rate](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_rate)Added [AudioUnitParameterUnit.Ratio](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/ratio)Added [AudioUnitParameterUnit.RelativeSemiTones](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_relativesemitones)Added [AudioUnitParameterUnit.SampleFrames](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_sampleframes)Added [AudioUnitParameterUnit.Seconds](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_seconds)Added [AudioUnitRenderActionFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags)Added AudioUnitRenderActionFlags.init(rawValue: UInt32)Added [AudioUnitRenderActionFlags.OfflineUnitRenderAction_Complete](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudioofflineunitrenderaction_complete)Added [AudioUnitRenderActionFlags.OfflineUnitRenderAction_Preflight](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudioofflineunitrenderaction_preflight)Added [AudioUnitRenderActionFlags.OfflineUnitRenderAction_Render](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1439632-offlineunitrenderaction_render)Added [AudioUnitRenderActionFlags.UnitRenderAction_DoNotCheckRenderArgs](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_donotcheckrenderargs)Added [AudioUnitRenderActionFlags.UnitRenderAction_OutputIsSilence](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_outputissilence)Added [AudioUnitRenderActionFlags.UnitRenderAction_PostRender](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1440615-unitrenderaction_postrender)Added [AudioUnitRenderActionFlags.UnitRenderAction_PostRenderError](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_postrendererror)Added [AudioUnitRenderActionFlags.UnitRenderAction_PreRender](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1440530-unitrenderaction_prerender)Added [AUHostTransportStateFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags)Added [AUHostTransportStateFlags.Changed](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387572-changed)Added [AUHostTransportStateFlags.Cycling](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstatecycling)Added AUHostTransportStateFlags.init(rawValue: UInt)Added [AUHostTransportStateFlags.Moving](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387579-moving)Added [AUHostTransportStateFlags.Recording](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387591-recording)Added [AUMIDIEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aumidievent)Added [AUMIDIEvent.cable](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439751-cable)Added [AUMIDIEvent.data](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1438814-data)Added [AUMIDIEvent.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440373-eventsampletime)Added [AUMIDIEvent.eventType](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440184-eventtype)Added AUMIDIEvent.init()Added AUMIDIEvent.init(next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8, length: UInt16, cable: UInt8, data: (UInt8, UInt8, UInt8))Added [AUMIDIEvent.length](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439101-length)Added [AUMIDIEvent.next](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439283-next)Added [AUMIDIEvent.reserved](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440361-reserved)Added [AUParameter](https://developer.apple.com/documentation/audiotoolbox/auparameter)Added [AUParameter.address](https://developer.apple.com/documentation/audiotoolbox/auparameter/1441037-address)Added [AUParameter.dependentParameters](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440649-dependentparameters)Added [AUParameter.flags](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439938-flags)Added [AUParameter.maxValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438427-maxvalue)Added [AUParameter.minValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440270-minvalue)Added [AUParameter.setValue(_: AUValue, originator: AUParameterObserverToken)](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439968-setvalue)Added [AUParameter.setValue(_: AUValue, originator: AUParameterObserverToken, atHostTime: UInt64)](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438450-setvalue)Added [AUParameter.stringFromValue(_: UnsafePointer<AUValue>) -> String](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440901-stringfromvalue)Added [AUParameter.unit](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440698-unit)Added [AUParameter.unitName](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438490-unitname)Added [AUParameter.value](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439301-value)Added [AUParameter.valueFromString(_: String) -> AUValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440495-valuefromstring)Added [AUParameter.valueStrings](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438358-valuestrings)Added [AUParameterEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/auparameterevent)Added [AUParameterEvent.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440912-eventsampletime)Added [AUParameterEvent.eventType](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1438332-eventtype)Added AUParameterEvent.init()Added AUParameterEvent.init(next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: (UInt8, UInt8, UInt8), rampDurationSampleFrames: AUAudioFrameCount, parameterAddress: AUParameterAddress, value: AUValue)Added [AUParameterEvent.next](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440983-next)Added [AUParameterEvent.parameterAddress](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440605-parameteraddress)Added [AUParameterEvent.rampDurationSampleFrames](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1439037-rampdurationsampleframes)Added [AUParameterEvent.reserved](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1439165-reserved)Added [AUParameterEvent.value](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440528-value)Added [AUParameterEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype)Added [AUParameterEventType.ParameterEvent_Immediate](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype/parameterevent_immediate)Added [AUParameterEventType.ParameterEvent_Ramped](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype/kparameterevent_ramped)Added [AUParameterGroup](https://developer.apple.com/documentation/audiotoolbox/auparametergroup)Added [AUParameterGroup.allParameters](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439439-allparameters)Added [AUParameterGroup.children](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439325-children)Added AUParameterMIDIMapping.init(mScope: AudioUnitScope, mElement: AudioUnitElement, mParameterID: AudioUnitParameterID, mFlags: AUParameterMIDIMappingFlags, mSubRangeMin: AudioUnitParameterValue, mSubRangeMax: AudioUnitParameterValue, mStatus: UInt8, mData1: UInt8, reserved1: UInt8, reserved2: UInt8, reserved3: UInt32)Added [AUParameterMIDIMappingFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auparametermidimappingflags)Added [AUParameterMIDIMappingFlags.AnyChannelFlag](https://developer.apple.com/documentation/audiotoolbox/auparametermidimappingflags/kauparametermidimapping_anychannelflag)Added [AUParameterMIDIMappingFlags.AnyNoteFlag](https://developer.apple.com/documentation/audiotoolbox/auparametermidimappingflags/1438606-anynoteflag)Added [AUParameterMIDIMappingFlags.Bipolar](https://developer.apple.com/documentation/audiotoolbox/auparametermidimappingflags/kauparametermidimapping_bipolar)Added [AUParameterMIDIMappingFlags.Bipolar_On](https://developer.apple.com/documentation/audiotoolbox/auparametermidimappingflags/1438313-bipolar_on)Added AUParameterMIDIMappingFlags.init(rawValue: UInt32)Added [AUParameterMIDIMappingFlags.SubRange](https://developer.apple.com/documentation/audiotoolbox/auparametermidimappingflags/kauparametermidimapping_subrange)Added [AUParameterMIDIMappingFlags.Toggle](https://developer.apple.com/documentation/audiotoolbox/auparametermidimappingflags/kauparametermidimapping_toggle)Added [AUParameterNode](https://developer.apple.com/documentation/audiotoolbox/auparameternode)Added [AUParameterNode.displayName](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440278-displayname)Added [AUParameterNode.displayNameWithLength(_: Int) -> String](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439449-displaynamewithlength)Added [AUParameterNode.identifier](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440186-identifier)Added [AUParameterNode.implementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439427-implementordisplaynamewithlength)Added [AUParameterNode.implementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440045-implementorstringfromvaluecallba)Added [AUParameterNode.implementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439270-implementorvaluefromstringcallba)Added [AUParameterNode.implementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439658-implementorvalueobserver)Added [AUParameterNode.implementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439942-implementorvalueprovider)Added [AUParameterNode.keyPath](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439420-keypath)Added [AUParameterNode.removeParameterObserver(_: AUParameterObserverToken)](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439314-removeparameterobserver)Added [AUParameterNode.tokenByAddingParameterObserver(_: AUParameterObserver) -> AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440811-token)Added [AUParameterNode.tokenByAddingParameterRecordingObserver(_: AUParameterRecordingObserver) -> AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440903-tokenbyaddingparameterrecordingo)Added [AUParameterTree](https://developer.apple.com/documentation/audiotoolbox/auparametertree)Added [AUParameterTree.createGroupFromTemplate(_: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439822-creategroupfromtemplate)Added [AUParameterTree.createGroupTemplate(_: [AUParameterNode]) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439912-creategrouptemplate)Added [AUParameterTree.createGroupWithIdentifier(_: String, name: String, children: [AUParameterNode]) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439002-creategroupwithidentifier)Added [AUParameterTree.createParameterWithIdentifier(_: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1440598-createparameter)Added [AUParameterTree.createTreeWithChildren(_: [AUParameterNode]) -> AUParameterTree [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438522-createtree)Added [AUParameterTree.parameterWithAddress(_: AUParameterAddress) -> AUParameter?](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439569-parameter)Added [AUParameterTree.parameterWithID(_: AudioUnitParameterID, scope: AudioUnitScope, element: AudioUnitElement) -> AUParameter?](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438918-parameter)Added [AURecordedParameterEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent)Added [AURecordedParameterEvent.address](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1438335-address)Added [AURecordedParameterEvent.hostTime](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1440955-hosttime)Added AURecordedParameterEvent.init()Added AURecordedParameterEvent.init(hostTime: UInt64, address: AUParameterAddress, value: AUValue)Added [AURecordedParameterEvent.value](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1440438-value)Added [AURenderEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aurenderevent)Added AURenderEvent.init()Added [AURenderEventHeader [struct]](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader)Added [AURenderEventHeader.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440010-eventsampletime)Added [AURenderEventHeader.eventType](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440946-eventtype)Added AURenderEventHeader.init()Added AURenderEventHeader.init(next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8)Added [AURenderEventHeader.next](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1439936-next)Added [AURenderEventHeader.reserved](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440587-reserved)Added [AURenderEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype)Added [AURenderEventType.MIDI](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midi)Added [AURenderEventType.MIDISysEx](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midisysex)Added [AURenderEventType.Parameter](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/parameter)Added [AURenderEventType.ParameterRamp](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/parameterramp)Added [AUReverbRoomType [enum]](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype)Added [AUReverbRoomType.ReverbRoomType_Cathedral](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_cathedral)Added [AUReverbRoomType.ReverbRoomType_LargeChamber](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largechamber)Added [AUReverbRoomType.ReverbRoomType_LargeHall](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largehall)Added [AUReverbRoomType.ReverbRoomType_LargeHall2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largehall2)Added [AUReverbRoomType.ReverbRoomType_LargeRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largeroom)Added [AUReverbRoomType.ReverbRoomType_LargeRoom2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largeroom2)Added [AUReverbRoomType.ReverbRoomType_MediumChamber](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_mediumchamber)Added [AUReverbRoomType.ReverbRoomType_MediumHall](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall)Added [AUReverbRoomType.ReverbRoomType_MediumHall2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall2)Added [AUReverbRoomType.ReverbRoomType_MediumHall3](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall3)Added [AUReverbRoomType.ReverbRoomType_MediumRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumroom)Added [AUReverbRoomType.ReverbRoomType_Plate](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_plate)Added [AUReverbRoomType.ReverbRoomType_SmallRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_smallroom)Added [AUScheduledAudioSliceFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags)Added AUScheduledAudioSliceFlags.init(rawValue: UInt32)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_BeganToRender](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_begantorender)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_BeganToRenderLate](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1438581-scheduledaudiosliceflag_begantor)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_Complete](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1440491-scheduledaudiosliceflag_complete)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_Interrupt](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_interrupt)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_InterruptAtLoop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1441008-scheduledaudiosliceflag_interrup)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_Loop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_loop)Added [AUSpatializationAlgorithm [enum]](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_EqualPowerPanning](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_equalpowerpanning)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_HRTF](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/kspatializationalgorithm_hrtf)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_SoundField](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/kspatializationalgorithm_soundfield)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_SphericalHead](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_sphericalhead)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_StereoPassThrough](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_stereopassthrough)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_VectorBasedPanning](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_vectorbasedpanning)Added [AUSpatialMixerAttenuationCurve [enum]](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve)Added [AUSpatialMixerAttenuationCurve.SpatialMixerAttenuationCurve_Exponential](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_exponential)Added [AUSpatialMixerAttenuationCurve.SpatialMixerAttenuationCurve_Inverse](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_inverse)Added [AUSpatialMixerAttenuationCurve.SpatialMixerAttenuationCurve_Linear](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/spatialmixerattenuationcurve_linear)Added [AUSpatialMixerAttenuationCurve.SpatialMixerAttenuationCurve_Power](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_power)Added [AUSpatialMixerRenderingFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags)Added AUSpatialMixerRenderingFlags.init(rawValue: UInt32)Added [AUSpatialMixerRenderingFlags.SpatialMixerRenderingFlags_DistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_distanceattenuation)Added [AUSpatialMixerRenderingFlags.SpatialMixerRenderingFlags_InterAuralDelay](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_interauraldelay)Added HostCallbackInfo.init(hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc: HostCallback_GetBeatAndTempo?, musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation?, transportStateProc: HostCallback_GetTransportState?, transportStateProc2: HostCallback_GetTransportState2?)Added [AUAudioChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiochannelcount)Added [AUAudioFrameCount](https://developer.apple.com/documentation/audiotoolbox/auaudioframecount)Added [AUAudioUnitStatus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitstatus)Added [AudioComponentGetIcon(_: AudioComponent) -> NSImage?](https://developer.apple.com/documentation/audiotoolbox/1410443-audiocomponentgeticon)Added [AudioComponentInstantiate(_: AudioComponent, _: AudioComponentInstantiationOptions, _: (AudioComponentInstance, OSStatus) -> Void)](https://developer.apple.com/documentation/audiotoolbox/1410517-audiocomponentinstantiate)Added [AudioComponentValidate(_: AudioComponent, _: CFDictionary?, _: UnsafeMutablePointer<AudioComponentValidationResult>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1410466-audiocomponentvalidate)Added [AUEventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aueventsampletime)Added AUEventSampleTimeImmediateAdded [AUHostMusicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auhostmusicalcontextblock)Added [AUHostTransportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateblock)Added [AUImplementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementordisplaynamewithlengthcallback)Added [AUImplementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorstringfromvaluecallback)Added [AUImplementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorvaluefromstringcallback)Added [AUImplementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueobserver)Added [AUImplementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueprovider)Added [AUInputHandler](https://developer.apple.com/documentation/audiotoolbox/auinputhandler)Added [AUInternalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auinternalrenderblock)Added [AUParameterAddress](https://developer.apple.com/documentation/audiotoolbox/auparameteraddress)Added [AUParameterObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterobserver)Added [AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameterobservertoken)Added [AUParameterRecordingObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterrecordingobserver)Added [AURenderBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderblock)Added [AURenderObserver](https://developer.apple.com/documentation/audiotoolbox/aurenderobserver)Added [AURenderPullInputBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderpullinputblock)Added [AUScheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auschedulemidieventblock)Added [AUScheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auscheduleparameterblock)Added [AUValue](https://developer.apple.com/documentation/audiotoolbox/auvalue)Added [GetAudioUnitParameterDisplayType(_: AudioUnitParameterOptions) -> AudioUnitParameterOptions](https://developer.apple.com/documentation/audiotoolbox/1440794-getaudiounitparameterdisplaytype)Added [kAudioComponentConfigurationInfo_ValidationResult](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentconfigurationinfo_validationresult)Added [kAudioComponentErr_InstanceInvalidated](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponenterr_instanceinvalidated)Added [kAudioComponentInstanceInvalidationNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentinstanceinvalidationnotification)Added [kAudioComponentRegistrationsChangedNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentregistrationschangednotification)Added [kAudioComponentValidationParameter_ForceValidation](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_forcevalidation)Added [kAudioComponentValidationParameter_TimeOut](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_timeout)Added [kAudioUnitConfigurationInfo_BusCountWritable](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_buscountwritable)Added [kAudioUnitConfigurationInfo_SupportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_supportedchannellayouttags)Added kAudioUnitProperty_ParametersForOverviewAdded kAudioUnitProperty_RequestViewControllerAdded kAudioUnitSubType_MultiSplitterAdded [SetAudioUnitParameterDisplayType(_: AudioUnitParameterOptions, _: AudioUnitParameterOptions) -> AudioUnitParameterOptions](https://developer.apple.com/documentation/audiotoolbox/1440769-setaudiounitparameterdisplaytype)Modified [AudioComponentPlugInInterface [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioComponentPlugInInterface {     var Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>     var Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>     var Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>     var reserved: UnsafeMutablePointer<Void>     init()     init(Open Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>, Close Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>, Lookup Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>, reserved reserved: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct AudioComponentPlugInInterface {     var Open: (UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus     var Close: (UnsafeMutablePointer<Void>) -> OSStatus     var Lookup: (Int16) -> AudioComponentMethod     var reserved: UnsafeMutablePointer<Void> } ``` |

Modified [AudioComponentPlugInInterface.Close](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/1410449-close)

|  | Declaration |
| --- | --- |
| From | ``` var Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` var Close: (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioComponentPlugInInterface.Lookup](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/1410481-lookup)

|  | Declaration |
| --- | --- |
| From | ``` var Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)> ``` |
| To | ``` var Lookup: (Int16) -> AudioComponentMethod ``` |

Modified [AudioComponentPlugInInterface.Open](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/1410462-open)

|  | Declaration |
| --- | --- |
| From | ``` var Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)> ``` |
| To | ``` var Open: (UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus ``` |

Modified [AudioUnitCocoaViewInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitcocoaviewinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitCocoaViewInfo {     var mCocoaAUViewBundleLocation: Unmanaged<CFURL>!     var mCocoaAUViewClass: (Unmanaged<CFString>?)     init()     init(mCocoaAUViewBundleLocation mCocoaAUViewBundleLocation: Unmanaged<CFURL>!, mCocoaAUViewClass mCocoaAUViewClass: (Unmanaged<CFString>?)) } ``` |
| To | ``` struct AudioUnitCocoaViewInfo {     var mCocoaAUViewBundleLocation: Unmanaged<CFURL>     var mCocoaAUViewClass: (Unmanaged<CFString>?) } ``` |

Modified [AudioUnitCocoaViewInfo.mCocoaAUViewBundleLocation](https://developer.apple.com/documentation/audiotoolbox/audiounitcocoaviewinfo/1439131-mcocoaauviewbundlelocation)

|  | Declaration |
| --- | --- |
| From | ``` var mCocoaAUViewBundleLocation: Unmanaged<CFURL>! ``` |
| To | ``` var mCocoaAUViewBundleLocation: Unmanaged<CFURL> ``` |

Modified [AudioUnitConnection [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitconnection)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitConnection {     var sourceAudioUnit: AudioUnit     var sourceOutputNumber: UInt32     var destInputNumber: UInt32     init()     init(sourceAudioUnit sourceAudioUnit: AudioUnit, sourceOutputNumber sourceOutputNumber: UInt32, destInputNumber destInputNumber: UInt32) } ``` |
| To | ``` struct AudioUnitConnection {     var sourceAudioUnit: AudioUnit     var sourceOutputNumber: UInt32     var destInputNumber: UInt32 } ``` |

Modified [AudioUnitExternalBuffer [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitexternalbuffer)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitExternalBuffer {     var buffer: UnsafeMutablePointer<UInt8>     var size: UInt32     init()     init(buffer buffer: UnsafeMutablePointer<UInt8>, size size: UInt32) } ``` |
| To | ``` struct AudioUnitExternalBuffer {     var buffer: UnsafeMutablePointer<UInt8>     var size: UInt32 } ``` |

Modified [AudioUnitMeterClipping [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitMeterClipping {     var peakValueSinceLastCall: Float32     var sawInfinity: Boolean     var sawNotANumber: Boolean     init()     init(peakValueSinceLastCall peakValueSinceLastCall: Float32, sawInfinity sawInfinity: Boolean, sawNotANumber sawNotANumber: Boolean) } ``` |
| To | ``` struct AudioUnitMeterClipping {     var peakValueSinceLastCall: Float32     var sawInfinity: DarwinBoolean     var sawNotANumber: DarwinBoolean     init()     init(peakValueSinceLastCall peakValueSinceLastCall: Float32, sawInfinity sawInfinity: DarwinBoolean, sawNotANumber sawNotANumber: DarwinBoolean) } ``` |

Modified [AudioUnitMeterClipping.sawInfinity](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping/1438398-sawinfinity)

|  | Declaration |
| --- | --- |
| From | ``` var sawInfinity: Boolean ``` |
| To | ``` var sawInfinity: DarwinBoolean ``` |

Modified [AudioUnitMeterClipping.sawNotANumber](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping/1439628-sawnotanumber)

|  | Declaration |
| --- | --- |
| From | ``` var sawNotANumber: Boolean ``` |
| To | ``` var sawNotANumber: DarwinBoolean ``` |

Modified [AudioUnitParameter [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameter)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameter {     var mAudioUnit: AudioUnit     var mParameterID: AudioUnitParameterID     var mScope: AudioUnitScope     var mElement: AudioUnitElement     init()     init(mAudioUnit mAudioUnit: AudioUnit, mParameterID mParameterID: AudioUnitParameterID, mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement) } ``` |
| To | ``` struct AudioUnitParameter {     var mAudioUnit: AudioUnit     var mParameterID: AudioUnitParameterID     var mScope: AudioUnitScope     var mElement: AudioUnitElement } ``` |

Modified [AudioUnitParameterInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterInfo {     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var unitName: Unmanaged<CFString>!     var clumpID: UInt32     var cfNameString: Unmanaged<CFString>!     var unit: AudioUnitParameterUnit     var minValue: AudioUnitParameterValue     var maxValue: AudioUnitParameterValue     var defaultValue: AudioUnitParameterValue     var flags: UInt32     init()     init(name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName unitName: Unmanaged<CFString>!, clumpID clumpID: UInt32, cfNameString cfNameString: Unmanaged<CFString>!, unit unit: AudioUnitParameterUnit, minValue minValue: AudioUnitParameterValue, maxValue maxValue: AudioUnitParameterValue, defaultValue defaultValue: AudioUnitParameterValue, flags flags: UInt32) } ``` |
| To | ``` struct AudioUnitParameterInfo {     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var unitName: Unmanaged<CFString>?     var clumpID: UInt32     var cfNameString: Unmanaged<CFString>?     var unit: AudioUnitParameterUnit     var minValue: AudioUnitParameterValue     var maxValue: AudioUnitParameterValue     var defaultValue: AudioUnitParameterValue     var flags: AudioUnitParameterOptions     init()     init(name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName unitName: Unmanaged<CFString>?, clumpID clumpID: UInt32, cfNameString cfNameString: Unmanaged<CFString>?, unit unit: AudioUnitParameterUnit, minValue minValue: AudioUnitParameterValue, maxValue maxValue: AudioUnitParameterValue, defaultValue defaultValue: AudioUnitParameterValue, flags flags: AudioUnitParameterOptions) } ``` |

Modified [AudioUnitParameterInfo.cfNameString](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439972-cfnamestring)

|  | Declaration |
| --- | --- |
| From | ``` var cfNameString: Unmanaged<CFString>! ``` |
| To | ``` var cfNameString: Unmanaged<CFString>? ``` |

Modified [AudioUnitParameterInfo.flags](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1440939-flags)

|  | Declaration |
| --- | --- |
| From | ``` var flags: UInt32 ``` |
| To | ``` var flags: AudioUnitParameterOptions ``` |

Modified [AudioUnitParameterInfo.unitName](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439337-unitname)

|  | Declaration |
| --- | --- |
| From | ``` var unitName: Unmanaged<CFString>! ``` |
| To | ``` var unitName: Unmanaged<CFString>? ``` |

Modified [AudioUnitParameterNameInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteridname)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterNameInfo {     var inID: AudioUnitParameterID     var inDesiredLength: Int32     var outName: Unmanaged<CFString>!     init()     init(inID inID: AudioUnitParameterID, inDesiredLength inDesiredLength: Int32, outName outName: Unmanaged<CFString>!) } ``` |
| To | ``` struct AudioUnitParameterNameInfo {     var inID: AudioUnitParameterID     var inDesiredLength: Int32     var outName: Unmanaged<CFString>?     init()     init(inID inID: AudioUnitParameterID, inDesiredLength inDesiredLength: Int32, outName outName: Unmanaged<CFString>?) } ``` |

Modified [AudioUnitParameterNameInfo.outName](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteridname/1440656-outname)

|  | Declaration |
| --- | --- |
| From | ``` var outName: Unmanaged<CFString>! ``` |
| To | ``` var outName: Unmanaged<CFString>? ``` |

Modified [AudioUnitParameterStringFromValue [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterstringfromvalue)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterStringFromValue {     var inParamID: AudioUnitParameterID     var inValue: UnsafePointer<AudioUnitParameterValue>     var outString: Unmanaged<CFString>!     init()     init(inParamID inParamID: AudioUnitParameterID, inValue inValue: UnsafePointer<AudioUnitParameterValue>, outString outString: Unmanaged<CFString>!) } ``` |
| To | ``` struct AudioUnitParameterStringFromValue {     var inParamID: AudioUnitParameterID     var inValue: UnsafePointer<AudioUnitParameterValue>     var outString: Unmanaged<CFString>? } ``` |

Modified [AudioUnitParameterStringFromValue.outString](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterstringfromvalue/1439491-outstring)

|  | Declaration |
| --- | --- |
| From | ``` var outString: Unmanaged<CFString>! ``` |
| To | ``` var outString: Unmanaged<CFString>? ``` |

Modified [AudioUnitParameterValueFromString [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluefromstring)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterValueFromString {     var inParamID: AudioUnitParameterID     var inString: Unmanaged<CFString>!     var outValue: AudioUnitParameterValue     init()     init(inParamID inParamID: AudioUnitParameterID, inString inString: Unmanaged<CFString>!, outValue outValue: AudioUnitParameterValue) } ``` |
| To | ``` struct AudioUnitParameterValueFromString {     var inParamID: AudioUnitParameterID     var inString: Unmanaged<CFString>     var outValue: AudioUnitParameterValue } ``` |

Modified [AudioUnitParameterValueFromString.inString](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluefromstring/1440393-instring)

|  | Declaration |
| --- | --- |
| From | ``` var inString: Unmanaged<CFString>! ``` |
| To | ``` var inString: Unmanaged<CFString> ``` |

Modified [AudioUnitParameterValueName [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluename)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitParameterValueName {     var inParamID: AudioUnitParameterID     var inValue: UnsafePointer<Float32>     var outName: Unmanaged<CFString>!     init()     init(inParamID inParamID: AudioUnitParameterID, inValue inValue: UnsafePointer<Float32>, outName outName: Unmanaged<CFString>!) } ``` |
| To | ``` struct AudioUnitParameterValueName {     var inParamID: AudioUnitParameterID     var inValue: UnsafePointer<Float32>     var outName: Unmanaged<CFString> } ``` |

Modified [AudioUnitParameterValueName.outName](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluename/1439447-outname)

|  | Declaration |
| --- | --- |
| From | ``` var outName: Unmanaged<CFString>! ``` |
| To | ``` var outName: Unmanaged<CFString> ``` |

Modified [AudioUnitProperty [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitproperty)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitProperty {     var mAudioUnit: AudioUnit     var mPropertyID: AudioUnitPropertyID     var mScope: AudioUnitScope     var mElement: AudioUnitElement     init()     init(mAudioUnit mAudioUnit: AudioUnit, mPropertyID mPropertyID: AudioUnitPropertyID, mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement) } ``` |
| To | ``` struct AudioUnitProperty {     var mAudioUnit: AudioUnit     var mPropertyID: AudioUnitPropertyID     var mScope: AudioUnitScope     var mElement: AudioUnitElement } ``` |

Modified [AUDistanceAttenuationData [struct]](https://developer.apple.com/documentation/audiotoolbox/audistanceattenuationdata)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.5 | OS X 10.11 |

Modified AUDistanceAttenuationData.init()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [AUDistanceAttenuationData.inNumberOfPairs](https://developer.apple.com/documentation/audiotoolbox/audistanceattenuationdata/1439637-innumberofpairs)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [AUHostIdentifier [struct]](https://developer.apple.com/documentation/audiotoolbox/auhostidentifier)

|  | Declaration |
| --- | --- |
| From | ``` struct AUHostIdentifier {     var hostName: Unmanaged<CFString>!     var hostVersion: AUNumVersion     init()     init(hostName hostName: Unmanaged<CFString>!, hostVersion hostVersion: AUNumVersion) } ``` |
| To | ``` struct AUHostIdentifier {     var hostName: Unmanaged<CFString>     var hostVersion: AUNumVersion } ``` |

Modified [AUHostIdentifier.hostName](https://developer.apple.com/documentation/audiotoolbox/auhostidentifier/1438546-hostname)

|  | Declaration |
| --- | --- |
| From | ``` var hostName: Unmanaged<CFString>! ``` |
| To | ``` var hostName: Unmanaged<CFString> ``` |

Modified [AUHostVersionIdentifier [struct]](https://developer.apple.com/documentation/audiotoolbox/auhostversionidentifier)

|  | Declaration |
| --- | --- |
| From | ``` struct AUHostVersionIdentifier {     var hostName: Unmanaged<CFString>!     var hostVersion: UInt32     init()     init(hostName hostName: Unmanaged<CFString>!, hostVersion hostVersion: UInt32) } ``` |
| To | ``` struct AUHostVersionIdentifier {     var hostName: Unmanaged<CFString>     var hostVersion: UInt32 } ``` |

Modified [AUHostVersionIdentifier.hostName](https://developer.apple.com/documentation/audiotoolbox/auhostversionidentifier/1439928-hostname)

|  | Declaration |
| --- | --- |
| From | ``` var hostName: Unmanaged<CFString>! ``` |
| To | ``` var hostName: Unmanaged<CFString> ``` |

Modified [AUInputSamplesInOutputCallbackStruct [struct]](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallbackstruct)

|  | Declaration |
| --- | --- |
| From | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafeMutablePointer<Void>     init()     init(inputToOutputCallback inputToOutputCallback: AUInputSamplesInOutputCallback, userData userData: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafeMutablePointer<Void> } ``` |

Modified [AUMIDIOutputCallbackStruct [struct]](https://developer.apple.com/documentation/audiotoolbox/aumidioutputcallbackstruct)

|  | Declaration |
| --- | --- |
| From | ``` struct AUMIDIOutputCallbackStruct {     var midiOutputCallback: AUMIDIOutputCallback     var userData: UnsafeMutablePointer<Void>     init()     init(midiOutputCallback midiOutputCallback: AUMIDIOutputCallback, userData userData: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct AUMIDIOutputCallbackStruct {     var midiOutputCallback: AUMIDIOutputCallback     var userData: UnsafeMutablePointer<Void> } ``` |

Modified [AUParameterMIDIMapping [struct]](https://developer.apple.com/documentation/audiotoolbox/auparametermidimapping)

|  | Declaration |
| --- | --- |
| From | ``` struct AUParameterMIDIMapping {     var mScope: AudioUnitScope     var mElement: AudioUnitElement     var mParameterID: AudioUnitParameterID     var mFlags: UInt32     var mSubRangeMin: AudioUnitParameterValue     var mSubRangeMax: AudioUnitParameterValue     var mStatus: UInt8     var mData1: UInt8     var reserved1: UInt8     var reserved2: UInt8     var reserved3: UInt32     init()     init(mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement, mParameterID mParameterID: AudioUnitParameterID, mFlags mFlags: UInt32, mSubRangeMin mSubRangeMin: AudioUnitParameterValue, mSubRangeMax mSubRangeMax: AudioUnitParameterValue, mStatus mStatus: UInt8, mData1 mData1: UInt8, reserved1 reserved1: UInt8, reserved2 reserved2: UInt8, reserved3 reserved3: UInt32) } ``` |
| To | ``` struct AUParameterMIDIMapping {     var mScope: AudioUnitScope     var mElement: AudioUnitElement     var mParameterID: AudioUnitParameterID     var mFlags: AUParameterMIDIMappingFlags     var mSubRangeMin: AudioUnitParameterValue     var mSubRangeMax: AudioUnitParameterValue     var mStatus: UInt8     var mData1: UInt8     var reserved1: UInt8     var reserved2: UInt8     var reserved3: UInt32     init()     init(mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement, mParameterID mParameterID: AudioUnitParameterID, mFlags mFlags: AUParameterMIDIMappingFlags, mSubRangeMin mSubRangeMin: AudioUnitParameterValue, mSubRangeMax mSubRangeMax: AudioUnitParameterValue, mStatus mStatus: UInt8, mData1 mData1: UInt8, reserved1 reserved1: UInt8, reserved2 reserved2: UInt8, reserved3 reserved3: UInt32) } ``` |

Modified [AUParameterMIDIMapping.mFlags](https://developer.apple.com/documentation/audiotoolbox/auparametermidimapping/1438384-mflags)

|  | Declaration |
| --- | --- |
| From | ``` var mFlags: UInt32 ``` |
| To | ``` var mFlags: AUParameterMIDIMappingFlags ``` |

Modified [AUPreset [struct]](https://developer.apple.com/documentation/audiotoolbox/aupreset)

|  | Declaration |
| --- | --- |
| From | ``` struct AUPreset {     var presetNumber: Int32     var presetName: Unmanaged<CFString>!     init()     init(presetNumber presetNumber: Int32, presetName presetName: Unmanaged<CFString>!) } ``` |
| To | ``` struct AUPreset {     var presetNumber: Int32     var presetName: Unmanaged<CFString> } ``` |

Modified [AUPreset.presetName](https://developer.apple.com/documentation/audiotoolbox/aupreset/1440636-presetname)

|  | Declaration |
| --- | --- |
| From | ``` var presetName: Unmanaged<CFString>! ``` |
| To | ``` var presetName: Unmanaged<CFString> ``` |

Modified [AURenderCallbackStruct [struct]](https://developer.apple.com/documentation/audiotoolbox/aurendercallbackstruct)

|  | Declaration |
| --- | --- |
| From | ``` struct AURenderCallbackStruct {     var inputProc: AURenderCallback     var inputProcRefCon: UnsafeMutablePointer<Void>     init()     init(inputProc inputProc: AURenderCallback, inputProcRefCon inputProcRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct AURenderCallbackStruct {     var inputProc: AURenderCallback     var inputProcRefCon: UnsafeMutablePointer<Void> } ``` |

Modified [AUSamplerBankPresetData [struct]](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata)

|  | Declaration |
| --- | --- |
| From | ``` struct AUSamplerBankPresetData {     var bankURL: Unmanaged<CFURL>!     var bankMSB: UInt8     var bankLSB: UInt8     var presetID: UInt8     var reserved: UInt8     init()     init(bankURL bankURL: Unmanaged<CFURL>!, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, presetID presetID: UInt8, reserved reserved: UInt8) } ``` |
| To | ``` struct AUSamplerBankPresetData {     var bankURL: Unmanaged<CFURL>     var bankMSB: UInt8     var bankLSB: UInt8     var presetID: UInt8     var reserved: UInt8 } ``` |

Modified [AUSamplerBankPresetData.bankURL](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata/1438574-bankurl)

|  | Declaration |
| --- | --- |
| From | ``` var bankURL: Unmanaged<CFURL>! ``` |
| To | ``` var bankURL: Unmanaged<CFURL> ``` |

Modified [AUSamplerInstrumentData [struct]](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata)

|  | Declaration |
| --- | --- |
| From | ``` struct AUSamplerInstrumentData {     var fileURL: Unmanaged<CFURL>!     var instrumentType: UInt8     var bankMSB: UInt8     var bankLSB: UInt8     var presetID: UInt8     init()     init(fileURL fileURL: Unmanaged<CFURL>!, instrumentType instrumentType: UInt8, bankMSB bankMSB: UInt8, bankLSB bankLSB: UInt8, presetID presetID: UInt8) } ``` |
| To | ``` struct AUSamplerInstrumentData {     var fileURL: Unmanaged<CFURL>     var instrumentType: UInt8     var bankMSB: UInt8     var bankLSB: UInt8     var presetID: UInt8 } ``` |

Modified [AUSamplerInstrumentData.fileURL](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata/1439725-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` var fileURL: Unmanaged<CFURL>! ``` |
| To | ``` var fileURL: Unmanaged<CFURL> ``` |

Modified [HostCallbackInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct HostCallbackInfo {     var hostUserData: UnsafeMutablePointer<Void>     var beatAndTempoProc: HostCallback_GetBeatAndTempo     var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation     var transportStateProc: HostCallback_GetTransportState     var transportStateProc2: HostCallback_GetTransportState2     init()     init(hostUserData hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc beatAndTempoProc: HostCallback_GetBeatAndTempo, musicalTimeLocationProc musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation, transportStateProc transportStateProc: HostCallback_GetTransportState, transportStateProc2 transportStateProc2: HostCallback_GetTransportState2) } ``` |
| To | ``` struct HostCallbackInfo {     var hostUserData: UnsafeMutablePointer<Void>     var beatAndTempoProc: HostCallback_GetBeatAndTempo?     var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation?     var transportStateProc: HostCallback_GetTransportState?     var transportStateProc2: HostCallback_GetTransportState2?     init()     init(hostUserData hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc beatAndTempoProc: HostCallback_GetBeatAndTempo?, musicalTimeLocationProc musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation?, transportStateProc transportStateProc: HostCallback_GetTransportState?, transportStateProc2 transportStateProc2: HostCallback_GetTransportState2?) } ``` |

Modified [HostCallbackInfo.beatAndTempoProc](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439047-beatandtempoproc)

|  | Declaration |
| --- | --- |
| From | ``` var beatAndTempoProc: HostCallback_GetBeatAndTempo ``` |
| To | ``` var beatAndTempoProc: HostCallback_GetBeatAndTempo? ``` |

Modified [HostCallbackInfo.musicalTimeLocationProc](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1440190-musicaltimelocationproc)

|  | Declaration |
| --- | --- |
| From | ``` var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation ``` |
| To | ``` var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation? ``` |

Modified [HostCallbackInfo.transportStateProc](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439276-transportstateproc)

|  | Declaration |
| --- | --- |
| From | ``` var transportStateProc: HostCallback_GetTransportState ``` |
| To | ``` var transportStateProc: HostCallback_GetTransportState? ``` |

Modified [HostCallbackInfo.transportStateProc2](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439489-transportstateproc2)

|  | Declaration |
| --- | --- |
| From | ``` var transportStateProc2: HostCallback_GetTransportState2 ``` |
| To | ``` var transportStateProc2: HostCallback_GetTransportState2? ``` |

Modified [ScheduledAudioFileRegion [struct]](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion)

|  | Declaration |
| --- | --- |
| From | ``` struct ScheduledAudioFileRegion {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioFileRegionCompletionProc     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mAudioFile: COpaquePointer     var mLoopCount: UInt32     var mStartFrame: Int64     var mFramesToPlay: UInt32     init() } ``` |
| To | ``` struct ScheduledAudioFileRegion {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioFileRegionCompletionProc?     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mAudioFile: COpaquePointer     var mLoopCount: UInt32     var mStartFrame: Int64     var mFramesToPlay: UInt32 } ``` |

Modified [ScheduledAudioFileRegion.mCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion/1440737-mcompletionproc)

|  | Declaration |
| --- | --- |
| From | ``` var mCompletionProc: ScheduledAudioFileRegionCompletionProc ``` |
| To | ``` var mCompletionProc: ScheduledAudioFileRegionCompletionProc? ``` |

Modified [ScheduledAudioSlice [struct]](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice)

|  | Declaration |
| --- | --- |
| From | ``` struct ScheduledAudioSlice {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioSliceCompletionProc     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mFlags: UInt32     var mReserved: UInt32     var mReserved2: UnsafeMutablePointer<Void>     var mNumberFrames: UInt32     var mBufferList: UnsafeMutablePointer<AudioBufferList>     init()     init(mTimeStamp mTimeStamp: AudioTimeStamp, mCompletionProc mCompletionProc: ScheduledAudioSliceCompletionProc, mCompletionProcUserData mCompletionProcUserData: UnsafeMutablePointer<Void>, mFlags mFlags: UInt32, mReserved mReserved: UInt32, mReserved2 mReserved2: UnsafeMutablePointer<Void>, mNumberFrames mNumberFrames: UInt32, mBufferList mBufferList: UnsafeMutablePointer<AudioBufferList>) } ``` |
| To | ``` struct ScheduledAudioSlice {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioSliceCompletionProc?     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mFlags: AUScheduledAudioSliceFlags     var mReserved: UInt32     var mReserved2: UnsafeMutablePointer<Void>     var mNumberFrames: UInt32     var mBufferList: UnsafeMutablePointer<AudioBufferList> } ``` |

Modified [ScheduledAudioSlice.mCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1440285-mcompletionproc)

|  | Declaration |
| --- | --- |
| From | ``` var mCompletionProc: ScheduledAudioSliceCompletionProc ``` |
| To | ``` var mCompletionProc: ScheduledAudioSliceCompletionProc? ``` |

Modified [ScheduledAudioSlice.mFlags](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1438587-mflags)

|  | Declaration |
| --- | --- |
| From | ``` var mFlags: UInt32 ``` |
| To | ``` var mFlags: AUScheduledAudioSliceFlags ``` |

Modified [AudioCodecAppendInputBufferListProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecappendinputbufferlistproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecAppendInputBufferListProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecAppendInputBufferListProc = (UnsafeMutablePointer<Void>, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioCodecAppendInputDataProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecappendinputdataproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecAppendInputDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecAppendInputDataProc = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` |

Modified [AudioCodecGetPropertyInfo(_: AudioCodec, _: AudioCodecPropertyID, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1439602-audiocodecgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioCodecGetPropertyInfo(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AudioCodecGetPropertyInfo(_ inCodec: AudioCodec, _ inPropertyID: AudioCodecPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioCodecGetPropertyInfoProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecgetpropertyinfoproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecGetPropertyInfoProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecGetPropertyInfoProc = (UnsafeMutablePointer<Void>, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioCodecGetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecgetpropertyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecGetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecGetPropertyProc = (UnsafeMutablePointer<Void>, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioCodecInitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecinitializeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecInitializeProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<Void>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecInitializeProc = (UnsafeMutablePointer<Void>, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<Void>, UInt32) -> OSStatus ``` |

Modified [AudioCodecProduceOutputBufferListProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecproduceoutputbufferlistproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecProduceOutputBufferListProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecProduceOutputBufferListProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioCodecProduceOutputPacketsProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecproduceoutputpacketsproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecProduceOutputPacketsProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecProduceOutputPacketsProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioCodecResetProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecresetproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecResetProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecResetProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioCodecSetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecsetpropertyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecSetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioCodecPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecSetPropertyProc = (UnsafeMutablePointer<Void>, AudioCodecPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus ``` |

Modified [AudioCodecUninitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiocodecuninitializeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioCodecUninitializeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioCodecUninitializeProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioComponentFactoryFunction](https://developer.apple.com/documentation/audiotoolbox/audiocomponentfactoryfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioComponentFactoryFunction = CFunctionPointer<((UnsafePointer<AudioComponentDescription>) -> UnsafeMutablePointer<AudioComponentPlugInInterface>)> ``` |
| To | ``` typealias AudioComponentFactoryFunction = (UnsafePointer<AudioComponentDescription>) -> UnsafeMutablePointer<AudioComponentPlugInInterface> ``` |

Modified [AudioComponentInstanceCanDo(_: AudioComponentInstance, _: Int16) -> Bool](https://developer.apple.com/documentation/audiotoolbox/1410504-audiocomponentinstancecando)

|  | Declaration |
| --- | --- |
| From | ``` func AudioComponentInstanceCanDo(_ inInstance: AudioComponentInstance, _ inSelectorID: Int16) -> Boolean ``` |
| To | ``` func AudioComponentInstanceCanDo(_ inInstance: AudioComponentInstance, _ inSelectorID: Int16) -> Bool ``` |

Modified [AudioComponentRegister(_: UnsafePointer<AudioComponentDescription>, _: CFString, _: UInt32, _: AudioComponentFactoryFunction) -> AudioComponent](https://developer.apple.com/documentation/audiotoolbox/1410487-audiocomponentregister)

|  | Declaration |
| --- | --- |
| From | ``` func AudioComponentRegister(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString!, _ inVersion: UInt32, _ inFactory: AudioComponentFactoryFunction) -> AudioComponent ``` |
| To | ``` func AudioComponentRegister(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString, _ inVersion: UInt32, _ inFactory: AudioComponentFactoryFunction) -> AudioComponent ``` |

Modified [AudioOutputUnitStartProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioOutputUnitStartProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioOutputUnitStartProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioOutputUnitStopProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstopproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioOutputUnitStopProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioOutputUnitStopProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioUnitAddPropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiounitaddpropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitAddPropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitAddPropertyListenerProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioUnitAddRenderNotifyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitaddrendernotifyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitAddRenderNotifyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitAddRenderNotifyProc = (UnsafeMutablePointer<Void>, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioUnitComplexRenderProc](https://developer.apple.com/documentation/audiotoolbox/audiounitcomplexrenderproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitComplexRenderProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitComplexRenderProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioUnitGetParameterProc](https://developer.apple.com/documentation/audiotoolbox/audiounitgetparameterproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitGetParameterProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitGetParameterProc = (UnsafeMutablePointer<Void>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus ``` |

Modified [AudioUnitGetPropertyInfo(_: AudioUnit, _: AudioUnitPropertyID, _: AudioUnitScope, _: AudioUnitElement, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440663-audiounitgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioUnitGetPropertyInfo(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AudioUnitGetPropertyInfo(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioUnitGetPropertyInfoProc](https://developer.apple.com/documentation/audiotoolbox/audiounitgetpropertyinfoproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitGetPropertyInfoProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitGetPropertyInfoProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioUnitGetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitgetpropertyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitGetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitGetPropertyProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioUnitInitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiounitinitializeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitInitializeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitInitializeProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioUnitProcessMultipleProc](https://developer.apple.com/documentation/audiotoolbox/audiounitprocessmultipleproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitProcessMultipleProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitProcessMultipleProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus ``` |

Modified [AudioUnitProcessProc](https://developer.apple.com/documentation/audiotoolbox/audiounitprocessproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitProcessProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitProcessProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` |

Modified [AudioUnitPropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiounitpropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitPropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement) -> Void)> ``` |
| To | ``` typealias AudioUnitPropertyListenerProc = (UnsafeMutablePointer<Void>, AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement) -> Void ``` |

Modified [AudioUnitRemovePropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremovepropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitRemovePropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitRemovePropertyListenerProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc) -> OSStatus ``` |

Modified [AudioUnitRemovePropertyListenerWithUserDataProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremovepropertylistenerwithuserdataproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitRemovePropertyListenerWithUserDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitRemovePropertyListenerWithUserDataProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioUnitRemoveRenderNotifyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremoverendernotifyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitRemoveRenderNotifyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitRemoveRenderNotifyProc = (UnsafeMutablePointer<Void>, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioUnitRenderProc](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitRenderProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitRenderProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` |

Modified [AudioUnitResetProc](https://developer.apple.com/documentation/audiotoolbox/audiounitresetproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitResetProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitScope, AudioUnitElement) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitResetProc = (UnsafeMutablePointer<Void>, AudioUnitScope, AudioUnitElement) -> OSStatus ``` |

Modified [AudioUnitScheduleParametersProc](https://developer.apple.com/documentation/audiotoolbox/audiounitscheduleparametersproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitScheduleParametersProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitScheduleParametersProc = (UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus ``` |

Modified [AudioUnitSetParameterProc](https://developer.apple.com/documentation/audiotoolbox/audiounitsetparameterproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitSetParameterProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitSetParameterProc = (UnsafeMutablePointer<Void>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus ``` |

Modified [AudioUnitSetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitsetpropertyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitSetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafePointer<Void>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitSetPropertyProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafePointer<Void>, UInt32) -> OSStatus ``` |

Modified [AudioUnitUninitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiounituninitializeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioUnitUninitializeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioUnitUninitializeProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AUInputSamplesInOutputCallback](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AUInputSamplesInOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioTimeStamp>, Float64, Float64) -> Void)> ``` |
| To | ``` typealias AUInputSamplesInOutputCallback = (UnsafeMutablePointer<Void>, UnsafePointer<AudioTimeStamp>, Float64, Float64) -> Void ``` |

Modified [AUMIDIOutputCallback](https://developer.apple.com/documentation/audiotoolbox/aumidioutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AUMIDIOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<AudioTimeStamp>, UInt32, COpaquePointer) -> OSStatus)> ``` |
| To | ``` typealias AUMIDIOutputCallback = (UnsafeMutablePointer<Void>, UnsafePointer<AudioTimeStamp>, UInt32, COpaquePointer) -> OSStatus ``` |

Modified [AURenderCallback](https://developer.apple.com/documentation/audiotoolbox/aurendercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AURenderCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus)> ``` |
| To | ``` typealias AURenderCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` |

Modified [HostCallback_GetBeatAndTempo](https://developer.apple.com/documentation/audiotoolbox/hostcallback_getbeatandtempo)

|  | Declaration |
| --- | --- |
| From | ``` typealias HostCallback_GetBeatAndTempo = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus)> ``` |
| To | ``` typealias HostCallback_GetBeatAndTempo = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus ``` |

Modified [HostCallback_GetMusicalTimeLocation](https://developer.apple.com/documentation/audiotoolbox/hostcallback_getmusicaltimelocation)

|  | Declaration |
| --- | --- |
| From | ``` typealias HostCallback_GetMusicalTimeLocation = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Float32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Float64>) -> OSStatus)> ``` |
| To | ``` typealias HostCallback_GetMusicalTimeLocation = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Float32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Float64>) -> OSStatus ``` |

Modified [HostCallback_GetTransportState](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate)

|  | Declaration |
| --- | --- |
| From | ``` typealias HostCallback_GetTransportState = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus)> ``` |
| To | ``` typealias HostCallback_GetTransportState = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus ``` |

Modified [HostCallback_GetTransportState2](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate2)

|  | Declaration |
| --- | --- |
| From | ``` typealias HostCallback_GetTransportState2 = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus)> ``` |
| To | ``` typealias HostCallback_GetTransportState2 = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus ``` |

Modified k3DMixerParam_Azimuth

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_Azimuth: Int { get } ``` |
| To | ``` var k3DMixerParam_Azimuth: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_Distance

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_Distance: Int { get } ``` |
| To | ``` var k3DMixerParam_Distance: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_Elevation

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_Elevation: Int { get } ``` |
| To | ``` var k3DMixerParam_Elevation: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_Gain

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_Gain: Int { get } ``` |
| To | ``` var k3DMixerParam_Gain: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_GlobalReverbGain

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_GlobalReverbGain: Int { get } ``` |
| To | ``` var k3DMixerParam_GlobalReverbGain: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_MaxGain

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_MaxGain: Int { get } ``` |
| To | ``` var k3DMixerParam_MaxGain: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_MinGain

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_MinGain: Int { get } ``` |
| To | ``` var k3DMixerParam_MinGain: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_ObstructionAttenuation

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_ObstructionAttenuation: Int { get } ``` |
| To | ``` var k3DMixerParam_ObstructionAttenuation: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_OcclusionAttenuation

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_OcclusionAttenuation: Int { get } ``` |
| To | ``` var k3DMixerParam_OcclusionAttenuation: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_PlaybackRate

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_PlaybackRate: Int { get } ``` |
| To | ``` var k3DMixerParam_PlaybackRate: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_PostAveragePower

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_PostAveragePower: Int { get } ``` |
| To | ``` var k3DMixerParam_PostAveragePower: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_PostPeakHoldLevel

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_PostPeakHoldLevel: Int { get } ``` |
| To | ``` var k3DMixerParam_PostPeakHoldLevel: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_PreAveragePower

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_PreAveragePower: Int { get } ``` |
| To | ``` var k3DMixerParam_PreAveragePower: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_PrePeakHoldLevel

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_PrePeakHoldLevel: Int { get } ``` |
| To | ``` var k3DMixerParam_PrePeakHoldLevel: AudioUnitParameterID { get } ``` |

Modified k3DMixerParam_ReverbBlend

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_ReverbBlend: Int { get } ``` |
| To | ``` var k3DMixerParam_ReverbBlend: AudioUnitParameterID { get } ``` |

Modified kAudioCodecAppendInputBufferListSelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecAppendInputBufferListSelect: Int { get } ``` |
| To | ``` var kAudioCodecAppendInputBufferListSelect: UInt32 { get } ``` |

Modified kAudioCodecAppendInputDataSelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecAppendInputDataSelect: Int { get } ``` |
| To | ``` var kAudioCodecAppendInputDataSelect: UInt32 { get } ``` |

Modified kAudioCodecBadPropertySizeError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBadPropertySizeError: Int { get } ``` |
| To | ``` var kAudioCodecBadPropertySizeError: OSStatus { get } ``` |

Modified kAudioCodecBitRateControlMode_Constant

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBitRateControlMode_Constant: Int { get } ``` |
| To | ``` var kAudioCodecBitRateControlMode_Constant: UInt32 { get } ``` |

Modified kAudioCodecBitRateControlMode_LongTermAverage

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBitRateControlMode_LongTermAverage: Int { get } ``` |
| To | ``` var kAudioCodecBitRateControlMode_LongTermAverage: UInt32 { get } ``` |

Modified kAudioCodecBitRateControlMode_Variable

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBitRateControlMode_Variable: Int { get } ``` |
| To | ``` var kAudioCodecBitRateControlMode_Variable: UInt32 { get } ``` |

Modified kAudioCodecBitRateControlMode_VariableConstrained

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBitRateControlMode_VariableConstrained: Int { get } ``` |
| To | ``` var kAudioCodecBitRateControlMode_VariableConstrained: UInt32 { get } ``` |

Modified kAudioCodecBitRateFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBitRateFormat: Int { get } ``` |
| To | ``` var kAudioCodecBitRateFormat: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecBitRateFormat_ABR

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBitRateFormat_ABR: Int { get } ``` |
| To | ``` var kAudioCodecBitRateFormat_ABR: UInt32 { get } ``` |

Modified kAudioCodecBitRateFormat_CBR

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBitRateFormat_CBR: Int { get } ``` |
| To | ``` var kAudioCodecBitRateFormat_CBR: UInt32 { get } ``` |

Modified kAudioCodecBitRateFormat_VBR

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecBitRateFormat_VBR: Int { get } ``` |
| To | ``` var kAudioCodecBitRateFormat_VBR: UInt32 { get } ``` |

Modified kAudioCodecDelayMode_Compatibility

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecDelayMode_Compatibility: Int { get } ``` |
| To | ``` var kAudioCodecDelayMode_Compatibility: UInt32 { get } ``` |

Modified kAudioCodecDelayMode_Minimum

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecDelayMode_Minimum: Int { get } ``` |
| To | ``` var kAudioCodecDelayMode_Minimum: UInt32 { get } ``` |

Modified kAudioCodecDelayMode_Optimal

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecDelayMode_Optimal: Int { get } ``` |
| To | ``` var kAudioCodecDelayMode_Optimal: UInt32 { get } ``` |

Modified kAudioCodecDoesSampleRateConversion

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecDoesSampleRateConversion: Int { get } ``` |
| To | ``` var kAudioCodecDoesSampleRateConversion: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecExtendFrequencies

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecExtendFrequencies: Int { get } ``` |
| To | ``` var kAudioCodecExtendFrequencies: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecGetPropertyInfoSelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecGetPropertyInfoSelect: Int { get } ``` |
| To | ``` var kAudioCodecGetPropertyInfoSelect: UInt32 { get } ``` |

Modified kAudioCodecGetPropertySelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecGetPropertySelect: Int { get } ``` |
| To | ``` var kAudioCodecGetPropertySelect: UInt32 { get } ``` |

Modified kAudioCodecIllegalOperationError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecIllegalOperationError: Int { get } ``` |
| To | ``` var kAudioCodecIllegalOperationError: OSStatus { get } ``` |

Modified kAudioCodecInitializeSelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecInitializeSelect: Int { get } ``` |
| To | ``` var kAudioCodecInitializeSelect: UInt32 { get } ``` |

Modified kAudioCodecInputFormatsForOutputFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecInputFormatsForOutputFormat: Int { get } ``` |
| To | ``` var kAudioCodecInputFormatsForOutputFormat: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecNoError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecNoError: Int { get } ``` |
| To | ``` var kAudioCodecNoError: OSStatus { get } ``` |

Modified kAudioCodecNotEnoughBufferSpaceError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecNotEnoughBufferSpaceError: Int { get } ``` |
| To | ``` var kAudioCodecNotEnoughBufferSpaceError: OSStatus { get } ``` |

Modified kAudioCodecOutputFormatsForInputFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecOutputFormatsForInputFormat: Int { get } ``` |
| To | ``` var kAudioCodecOutputFormatsForInputFormat: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecOutputPrecedence

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecOutputPrecedence: Int { get } ``` |
| To | ``` var kAudioCodecOutputPrecedence: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecOutputPrecedenceBitRate

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecOutputPrecedenceBitRate: Int { get } ``` |
| To | ``` var kAudioCodecOutputPrecedenceBitRate: UInt32 { get } ``` |

Modified kAudioCodecOutputPrecedenceNone

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecOutputPrecedenceNone: Int { get } ``` |
| To | ``` var kAudioCodecOutputPrecedenceNone: UInt32 { get } ``` |

Modified kAudioCodecOutputPrecedenceSampleRate

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecOutputPrecedenceSampleRate: Int { get } ``` |
| To | ``` var kAudioCodecOutputPrecedenceSampleRate: UInt32 { get } ``` |

Modified kAudioCodecPrimeMethod_None

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPrimeMethod_None: Int { get } ``` |
| To | ``` var kAudioCodecPrimeMethod_None: UInt32 { get } ``` |

Modified kAudioCodecPrimeMethod_Normal

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPrimeMethod_Normal: Int { get } ``` |
| To | ``` var kAudioCodecPrimeMethod_Normal: UInt32 { get } ``` |

Modified kAudioCodecPrimeMethod_Pre

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPrimeMethod_Pre: Int { get } ``` |
| To | ``` var kAudioCodecPrimeMethod_Pre: UInt32 { get } ``` |

Modified kAudioCodecProduceOutputBufferListSelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecProduceOutputBufferListSelect: Int { get } ``` |
| To | ``` var kAudioCodecProduceOutputBufferListSelect: UInt32 { get } ``` |

Modified kAudioCodecProduceOutputDataSelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecProduceOutputDataSelect: Int { get } ``` |
| To | ``` var kAudioCodecProduceOutputDataSelect: UInt32 { get } ``` |

Modified kAudioCodecProduceOutputPacketAtEOF

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecProduceOutputPacketAtEOF: Int { get } ``` |
| To | ``` var kAudioCodecProduceOutputPacketAtEOF: UInt32 { get } ``` |

Modified kAudioCodecProduceOutputPacketFailure

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecProduceOutputPacketFailure: Int { get } ``` |
| To | ``` var kAudioCodecProduceOutputPacketFailure: UInt32 { get } ``` |

Modified kAudioCodecProduceOutputPacketNeedsMoreInputData

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecProduceOutputPacketNeedsMoreInputData: Int { get } ``` |
| To | ``` var kAudioCodecProduceOutputPacketNeedsMoreInputData: UInt32 { get } ``` |

Modified kAudioCodecProduceOutputPacketSuccess

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecProduceOutputPacketSuccess: Int { get } ``` |
| To | ``` var kAudioCodecProduceOutputPacketSuccess: UInt32 { get } ``` |

Modified kAudioCodecProduceOutputPacketSuccessHasMore

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecProduceOutputPacketSuccessHasMore: Int { get } ``` |
| To | ``` var kAudioCodecProduceOutputPacketSuccessHasMore: UInt32 { get } ``` |

Modified kAudioCodecPropertyAdjustLocalQuality

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAdjustLocalQuality: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAdjustLocalQuality: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyApplicableBitRateRange

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyApplicableBitRateRange: Int { get } ``` |
| To | ``` var kAudioCodecPropertyApplicableBitRateRange: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyApplicableInputSampleRates

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyApplicableInputSampleRates: Int { get } ``` |
| To | ``` var kAudioCodecPropertyApplicableInputSampleRates: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyApplicableOutputSampleRates

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyApplicableOutputSampleRates: Int { get } ``` |
| To | ``` var kAudioCodecPropertyApplicableOutputSampleRates: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableBitRateRange

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableBitRateRange: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableBitRateRange: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableBitRates

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableBitRates: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableBitRates: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableInputChannelLayouts

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableInputChannelLayouts: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableInputChannelLayouts: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableInputChannelLayoutTags

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableInputChannelLayoutTags: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableInputChannelLayoutTags: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableInputSampleRates

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableInputSampleRates: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableInputSampleRates: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableNumberChannels

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableNumberChannels: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableNumberChannels: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableOutputChannelLayouts

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableOutputChannelLayouts: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableOutputChannelLayouts: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableOutputChannelLayoutTags

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableOutputChannelLayoutTags: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableOutputChannelLayoutTags: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyAvailableOutputSampleRates

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyAvailableOutputSampleRates: Int { get } ``` |
| To | ``` var kAudioCodecPropertyAvailableOutputSampleRates: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyBitRateControlMode

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyBitRateControlMode: Int { get } ``` |
| To | ``` var kAudioCodecPropertyBitRateControlMode: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyCurrentInputChannelLayout

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyCurrentInputChannelLayout: Int { get } ``` |
| To | ``` var kAudioCodecPropertyCurrentInputChannelLayout: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyCurrentInputFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyCurrentInputFormat: Int { get } ``` |
| To | ``` var kAudioCodecPropertyCurrentInputFormat: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyCurrentInputSampleRate

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyCurrentInputSampleRate: Int { get } ``` |
| To | ``` var kAudioCodecPropertyCurrentInputSampleRate: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyCurrentOutputChannelLayout

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyCurrentOutputChannelLayout: Int { get } ``` |
| To | ``` var kAudioCodecPropertyCurrentOutputChannelLayout: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyCurrentOutputFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyCurrentOutputFormat: Int { get } ``` |
| To | ``` var kAudioCodecPropertyCurrentOutputFormat: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyCurrentOutputSampleRate

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyCurrentOutputSampleRate: Int { get } ``` |
| To | ``` var kAudioCodecPropertyCurrentOutputSampleRate: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyCurrentTargetBitRate

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyCurrentTargetBitRate: Int { get } ``` |
| To | ``` var kAudioCodecPropertyCurrentTargetBitRate: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyDelayMode

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyDelayMode: Int { get } ``` |
| To | ``` var kAudioCodecPropertyDelayMode: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyDoesSampleRateConversion

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyDoesSampleRateConversion: Int { get } ``` |
| To | ``` var kAudioCodecPropertyDoesSampleRateConversion: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyDynamicRangeControlMode

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyDynamicRangeControlMode: Int { get } ``` |
| To | ``` var kAudioCodecPropertyDynamicRangeControlMode: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyFormatCFString

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyFormatCFString: Int { get } ``` |
| To | ``` var kAudioCodecPropertyFormatCFString: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyFormatInfo

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyFormatInfo: Int { get } ``` |
| To | ``` var kAudioCodecPropertyFormatInfo: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyFormatList

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyFormatList: Int { get } ``` |
| To | ``` var kAudioCodecPropertyFormatList: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyHasVariablePacketByteSizes

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyHasVariablePacketByteSizes: Int { get } ``` |
| To | ``` var kAudioCodecPropertyHasVariablePacketByteSizes: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyInputBufferSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyInputBufferSize: Int { get } ``` |
| To | ``` var kAudioCodecPropertyInputBufferSize: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyInputChannelLayout

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyInputChannelLayout: Int { get } ``` |
| To | ``` var kAudioCodecPropertyInputChannelLayout: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyInputFormatsForOutputFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyInputFormatsForOutputFormat: Int { get } ``` |
| To | ``` var kAudioCodecPropertyInputFormatsForOutputFormat: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyIsInitialized

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyIsInitialized: Int { get } ``` |
| To | ``` var kAudioCodecPropertyIsInitialized: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyMagicCookie

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyMagicCookie: Int { get } ``` |
| To | ``` var kAudioCodecPropertyMagicCookie: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyManufacturerCFString

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyManufacturerCFString: Int { get } ``` |
| To | ``` var kAudioCodecPropertyManufacturerCFString: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyMaximumPacketByteSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyMaximumPacketByteSize: Int { get } ``` |
| To | ``` var kAudioCodecPropertyMaximumPacketByteSize: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyMinimumDelayMode

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyMinimumDelayMode: Int { get } ``` |
| To | ``` var kAudioCodecPropertyMinimumDelayMode: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyMinimumNumberInputPackets

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyMinimumNumberInputPackets: Int { get } ``` |
| To | ``` var kAudioCodecPropertyMinimumNumberInputPackets: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyMinimumNumberOutputPackets

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyMinimumNumberOutputPackets: Int { get } ``` |
| To | ``` var kAudioCodecPropertyMinimumNumberOutputPackets: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyNameCFString

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyNameCFString: Int { get } ``` |
| To | ``` var kAudioCodecPropertyNameCFString: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyOutputChannelLayout

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyOutputChannelLayout: Int { get } ``` |
| To | ``` var kAudioCodecPropertyOutputChannelLayout: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyOutputFormatsForInputFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyOutputFormatsForInputFormat: Int { get } ``` |
| To | ``` var kAudioCodecPropertyOutputFormatsForInputFormat: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyPacketFrameSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyPacketFrameSize: Int { get } ``` |
| To | ``` var kAudioCodecPropertyPacketFrameSize: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyPacketSizeLimitForVBR

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyPacketSizeLimitForVBR: Int { get } ``` |
| To | ``` var kAudioCodecPropertyPacketSizeLimitForVBR: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyPaddedZeros

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyPaddedZeros: Int { get } ``` |
| To | ``` var kAudioCodecPropertyPaddedZeros: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyPrimeInfo

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyPrimeInfo: Int { get } ``` |
| To | ``` var kAudioCodecPropertyPrimeInfo: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyPrimeMethod

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyPrimeMethod: Int { get } ``` |
| To | ``` var kAudioCodecPropertyPrimeMethod: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyProgramTargetLevel

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyProgramTargetLevel: Int { get } ``` |
| To | ``` var kAudioCodecPropertyProgramTargetLevel: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyProgramTargetLevelConstant

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyProgramTargetLevelConstant: Int { get } ``` |
| To | ``` var kAudioCodecPropertyProgramTargetLevelConstant: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyQualitySetting

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyQualitySetting: Int { get } ``` |
| To | ``` var kAudioCodecPropertyQualitySetting: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyRecommendedBitRateRange

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyRecommendedBitRateRange: Int { get } ``` |
| To | ``` var kAudioCodecPropertyRecommendedBitRateRange: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyRequiresPacketDescription

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyRequiresPacketDescription: Int { get } ``` |
| To | ``` var kAudioCodecPropertyRequiresPacketDescription: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertySettings

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertySettings: Int { get } ``` |
| To | ``` var kAudioCodecPropertySettings: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertySoundQualityForVBR

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertySoundQualityForVBR: Int { get } ``` |
| To | ``` var kAudioCodecPropertySoundQualityForVBR: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertySupportedInputFormats

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertySupportedInputFormats: Int { get } ``` |
| To | ``` var kAudioCodecPropertySupportedInputFormats: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertySupportedOutputFormats

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertySupportedOutputFormats: Int { get } ``` |
| To | ``` var kAudioCodecPropertySupportedOutputFormats: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyUsedInputBufferSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyUsedInputBufferSize: Int { get } ``` |
| To | ``` var kAudioCodecPropertyUsedInputBufferSize: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecPropertyZeroFramesPadded

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecPropertyZeroFramesPadded: Int { get } ``` |
| To | ``` var kAudioCodecPropertyZeroFramesPadded: AudioCodecPropertyID { get } ``` |

Modified kAudioCodecQuality_High

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecQuality_High: Int { get } ``` |
| To | ``` var kAudioCodecQuality_High: UInt32 { get } ``` |

Modified kAudioCodecQuality_Low

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecQuality_Low: Int { get } ``` |
| To | ``` var kAudioCodecQuality_Low: UInt32 { get } ``` |

Modified kAudioCodecQuality_Max

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecQuality_Max: Int { get } ``` |
| To | ``` var kAudioCodecQuality_Max: UInt32 { get } ``` |

Modified kAudioCodecQuality_Medium

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecQuality_Medium: Int { get } ``` |
| To | ``` var kAudioCodecQuality_Medium: UInt32 { get } ``` |

Modified kAudioCodecQuality_Min

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecQuality_Min: Int { get } ``` |
| To | ``` var kAudioCodecQuality_Min: UInt32 { get } ``` |

Modified kAudioCodecResetSelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecResetSelect: Int { get } ``` |
| To | ``` var kAudioCodecResetSelect: UInt32 { get } ``` |

Modified kAudioCodecSetPropertySelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecSetPropertySelect: Int { get } ``` |
| To | ``` var kAudioCodecSetPropertySelect: UInt32 { get } ``` |

Modified kAudioCodecStateError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecStateError: Int { get } ``` |
| To | ``` var kAudioCodecStateError: OSStatus { get } ``` |

Modified kAudioCodecUninitializeSelect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecUninitializeSelect: Int { get } ``` |
| To | ``` var kAudioCodecUninitializeSelect: UInt32 { get } ``` |

Modified kAudioCodecUnknownPropertyError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecUnknownPropertyError: Int { get } ``` |
| To | ``` var kAudioCodecUnknownPropertyError: OSStatus { get } ``` |

Modified kAudioCodecUnspecifiedError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecUnspecifiedError: Int { get } ``` |
| To | ``` var kAudioCodecUnspecifiedError: OSStatus { get } ``` |

Modified kAudioCodecUnsupportedFormatError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecUnsupportedFormatError: Int { get } ``` |
| To | ``` var kAudioCodecUnsupportedFormatError: OSStatus { get } ``` |

Modified kAudioCodecUseRecommendedSampleRate

|  | Declaration |
| --- | --- |
| From | ``` var kAudioCodecUseRecommendedSampleRate: Int { get } ``` |
| To | ``` var kAudioCodecUseRecommendedSampleRate: AudioCodecPropertyID { get } ``` |

Modified [kAudioDecoderComponentType](https://developer.apple.com/documentation/audiotoolbox/kaudiodecodercomponenttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDecoderComponentType: Int { get } ``` |
| To | ``` var kAudioDecoderComponentType: UInt32 { get } ``` |

Modified [kAudioEncoderComponentType](https://developer.apple.com/documentation/audiotoolbox/1494086-audio_codec_component_constants/kaudioencodercomponenttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioEncoderComponentType: Int { get } ``` |
| To | ``` var kAudioEncoderComponentType: UInt32 { get } ``` |

Modified kAudioOfflineUnitProperty_InputSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOfflineUnitProperty_InputSize: Int { get } ``` |
| To | ``` var kAudioOfflineUnitProperty_InputSize: AudioUnitPropertyID { get } ``` |

Modified kAudioOfflineUnitProperty_OutputSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOfflineUnitProperty_OutputSize: Int { get } ``` |
| To | ``` var kAudioOfflineUnitProperty_OutputSize: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_ChannelMap

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_ChannelMap: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_ChannelMap: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_CurrentDevice

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_CurrentDevice: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_CurrentDevice: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_EnableIO

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_EnableIO: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_EnableIO: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_HasIO

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_HasIO: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_HasIO: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_IsRunning

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_IsRunning: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_IsRunning: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_SetInputCallback

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_SetInputCallback: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_SetInputCallback: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_StartTime

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_StartTime: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_StartTime: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_StartTimestampsAtZero

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_StartTimestampsAtZero: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_StartTimestampsAtZero: AudioUnitPropertyID { get } ``` |

Modified [kAudioUnitErr_CannotDoInCurrentContext](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_cannotdoincurrentcontext)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_CannotDoInCurrentContext: Int { get } ``` |
| To | ``` var kAudioUnitErr_CannotDoInCurrentContext: OSStatus { get } ``` |

Modified [kAudioUnitErr_FailedInitialization](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_failedinitialization)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_FailedInitialization: Int { get } ``` |
| To | ``` var kAudioUnitErr_FailedInitialization: OSStatus { get } ``` |

Modified [kAudioUnitErr_FileNotSpecified](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_filenotspecified)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_FileNotSpecified: Int { get } ``` |
| To | ``` var kAudioUnitErr_FileNotSpecified: OSStatus { get } ``` |

Modified [kAudioUnitErr_FormatNotSupported](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_formatnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_FormatNotSupported: Int { get } ``` |
| To | ``` var kAudioUnitErr_FormatNotSupported: OSStatus { get } ``` |

Modified kAudioUnitErr_IllegalInstrument

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_IllegalInstrument: Int { get } ``` |
| To | ``` var kAudioUnitErr_IllegalInstrument: OSStatus { get } ``` |

Modified [kAudioUnitErr_Initialized](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_initialized)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_Initialized: Int { get } ``` |
| To | ``` var kAudioUnitErr_Initialized: OSStatus { get } ``` |

Modified kAudioUnitErr_InstrumentTypeNotFound

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_InstrumentTypeNotFound: Int { get } ``` |
| To | ``` var kAudioUnitErr_InstrumentTypeNotFound: OSStatus { get } ``` |

Modified [kAudioUnitErr_InvalidElement](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_invalidelement)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_InvalidElement: Int { get } ``` |
| To | ``` var kAudioUnitErr_InvalidElement: OSStatus { get } ``` |

Modified [kAudioUnitErr_InvalidFile](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_invalidfile)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_InvalidFile: Int { get } ``` |
| To | ``` var kAudioUnitErr_InvalidFile: OSStatus { get } ``` |

Modified [kAudioUnitErr_InvalidOfflineRender](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_invalidofflinerender)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_InvalidOfflineRender: Int { get } ``` |
| To | ``` var kAudioUnitErr_InvalidOfflineRender: OSStatus { get } ``` |

Modified [kAudioUnitErr_InvalidParameter](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_InvalidParameter: Int { get } ``` |
| To | ``` var kAudioUnitErr_InvalidParameter: OSStatus { get } ``` |

Modified [kAudioUnitErr_InvalidProperty](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_invalidproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_InvalidProperty: Int { get } ``` |
| To | ``` var kAudioUnitErr_InvalidProperty: OSStatus { get } ``` |

Modified [kAudioUnitErr_InvalidPropertyValue](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_invalidpropertyvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_InvalidPropertyValue: Int { get } ``` |
| To | ``` var kAudioUnitErr_InvalidPropertyValue: OSStatus { get } ``` |

Modified [kAudioUnitErr_InvalidScope](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_invalidscope)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_InvalidScope: Int { get } ``` |
| To | ``` var kAudioUnitErr_InvalidScope: OSStatus { get } ``` |

Modified [kAudioUnitErr_NoConnection](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_noconnection)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_NoConnection: Int { get } ``` |
| To | ``` var kAudioUnitErr_NoConnection: OSStatus { get } ``` |

Modified [kAudioUnitErr_PropertyNotInUse](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_propertynotinuse)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_PropertyNotInUse: Int { get } ``` |
| To | ``` var kAudioUnitErr_PropertyNotInUse: OSStatus { get } ``` |

Modified [kAudioUnitErr_PropertyNotWritable](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_propertynotwritable)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_PropertyNotWritable: Int { get } ``` |
| To | ``` var kAudioUnitErr_PropertyNotWritable: OSStatus { get } ``` |

Modified [kAudioUnitErr_TooManyFramesToProcess](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_toomanyframestoprocess)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_TooManyFramesToProcess: Int { get } ``` |
| To | ``` var kAudioUnitErr_TooManyFramesToProcess: OSStatus { get } ``` |

Modified [kAudioUnitErr_Unauthorized](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_unauthorized)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_Unauthorized: Int { get } ``` |
| To | ``` var kAudioUnitErr_Unauthorized: OSStatus { get } ``` |

Modified [kAudioUnitErr_Uninitialized](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_uninitialized)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_Uninitialized: Int { get } ``` |
| To | ``` var kAudioUnitErr_Uninitialized: OSStatus { get } ``` |

Modified [kAudioUnitErr_UnknownFileType](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_unknownfiletype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitErr_UnknownFileType: Int { get } ``` |
| To | ``` var kAudioUnitErr_UnknownFileType: OSStatus { get } ``` |

Modified kAudioUnitManufacturer_Apple

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitManufacturer_Apple: Int { get } ``` |
| To | ``` var kAudioUnitManufacturer_Apple: UInt32 { get } ``` |

Modified kAudioUnitMigrateProperty_FromPlugin

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitMigrateProperty_FromPlugin: Int { get } ``` |
| To | ``` var kAudioUnitMigrateProperty_FromPlugin: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitMigrateProperty_OldAutomation

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitMigrateProperty_OldAutomation: Int { get } ``` |
| To | ``` var kAudioUnitMigrateProperty_OldAutomation: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitOfflineProperty_InputSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitOfflineProperty_InputSize: Int { get } ``` |
| To | ``` var kAudioUnitOfflineProperty_InputSize: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitOfflineProperty_OutputSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitOfflineProperty_OutputSize: Int { get } ``` |
| To | ``` var kAudioUnitOfflineProperty_OutputSize: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitOfflineProperty_PreflightName

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitOfflineProperty_PreflightName: Int { get } ``` |
| To | ``` var kAudioUnitOfflineProperty_PreflightName: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitOfflineProperty_PreflightRequirements

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitOfflineProperty_PreflightRequirements: Int { get } ``` |
| To | ``` var kAudioUnitOfflineProperty_PreflightRequirements: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitOfflineProperty_StartOffset

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitOfflineProperty_StartOffset: Int { get } ``` |
| To | ``` var kAudioUnitOfflineProperty_StartOffset: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_3DMixerAttenuationCurve

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_3DMixerAttenuationCurve: Int { get } ``` |
| To | ``` var kAudioUnitProperty_3DMixerAttenuationCurve: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_3DMixerDistanceAtten

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_3DMixerDistanceAtten: Int { get } ``` |
| To | ``` var kAudioUnitProperty_3DMixerDistanceAtten: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_3DMixerDistanceParams

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_3DMixerDistanceParams: Int { get } ``` |
| To | ``` var kAudioUnitProperty_3DMixerDistanceParams: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_3DMixerRenderingFlags

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_3DMixerRenderingFlags: Int { get } ``` |
| To | ``` var kAudioUnitProperty_3DMixerRenderingFlags: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_AddParameterMIDIMapping

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_AddParameterMIDIMapping: Int { get } ``` |
| To | ``` var kAudioUnitProperty_AddParameterMIDIMapping: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_AllParameterMIDIMappings

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_AllParameterMIDIMappings: Int { get } ``` |
| To | ``` var kAudioUnitProperty_AllParameterMIDIMappings: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_AudioChannelLayout

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_AudioChannelLayout: Int { get } ``` |
| To | ``` var kAudioUnitProperty_AudioChannelLayout: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_AUHostIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_AUHostIdentifier: Int { get } ``` |
| To | ``` var kAudioUnitProperty_AUHostIdentifier: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_BusCount

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_BusCount: Int { get } ``` |
| To | ``` var kAudioUnitProperty_BusCount: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_BypassEffect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_BypassEffect: Int { get } ``` |
| To | ``` var kAudioUnitProperty_BypassEffect: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ClassInfo

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ClassInfo: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ClassInfo: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ClassInfoFromDocument

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ClassInfoFromDocument: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ClassInfoFromDocument: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_CocoaUI

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_CocoaUI: Int { get } ``` |
| To | ``` var kAudioUnitProperty_CocoaUI: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ContextName

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ContextName: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ContextName: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_CPULoad

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_CPULoad: Int { get } ``` |
| To | ``` var kAudioUnitProperty_CPULoad: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_CurrentPlayTime

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_CurrentPlayTime: Int { get } ``` |
| To | ``` var kAudioUnitProperty_CurrentPlayTime: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_CurrentPreset

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_CurrentPreset: Int { get } ``` |
| To | ``` var kAudioUnitProperty_CurrentPreset: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_DeferredRendererExtraLatency

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_DeferredRendererExtraLatency: Int { get } ``` |
| To | ``` var kAudioUnitProperty_DeferredRendererExtraLatency: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_DeferredRendererPullSize

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_DeferredRendererPullSize: Int { get } ``` |
| To | ``` var kAudioUnitProperty_DeferredRendererPullSize: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_DeferredRendererWaitFrames

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_DeferredRendererWaitFrames: Int { get } ``` |
| To | ``` var kAudioUnitProperty_DeferredRendererWaitFrames: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_DependentParameters

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_DependentParameters: Int { get } ``` |
| To | ``` var kAudioUnitProperty_DependentParameters: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_DistanceAttenuationData

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_DistanceAttenuationData: Int { get } ``` |
| To | ``` var kAudioUnitProperty_DistanceAttenuationData: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_DopplerShift

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_DopplerShift: Int { get } ``` |
| To | ``` var kAudioUnitProperty_DopplerShift: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ElementCount

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ElementCount: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ElementCount: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ElementName

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ElementName: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ElementName: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_FactoryPresets

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_FactoryPresets: Int { get } ``` |
| To | ``` var kAudioUnitProperty_FactoryPresets: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_FastDispatch

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_FastDispatch: Int { get } ``` |
| To | ``` var kAudioUnitProperty_FastDispatch: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_FrequencyResponse

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_FrequencyResponse: Int { get } ``` |
| To | ``` var kAudioUnitProperty_FrequencyResponse: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_GetUIComponentList

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_GetUIComponentList: Int { get } ``` |
| To | ``` var kAudioUnitProperty_GetUIComponentList: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_HostCallbacks

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_HostCallbacks: Int { get } ``` |
| To | ``` var kAudioUnitProperty_HostCallbacks: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_HotMapParameterMIDIMapping

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_HotMapParameterMIDIMapping: Int { get } ``` |
| To | ``` var kAudioUnitProperty_HotMapParameterMIDIMapping: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_IconLocation

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_IconLocation: Int { get } ``` |
| To | ``` var kAudioUnitProperty_IconLocation: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_InPlaceProcessing

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_InPlaceProcessing: Int { get } ``` |
| To | ``` var kAudioUnitProperty_InPlaceProcessing: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_InputSamplesInOutput

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_InputSamplesInOutput: Int { get } ``` |
| To | ``` var kAudioUnitProperty_InputSamplesInOutput: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_LastRenderError

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_LastRenderError: Int { get } ``` |
| To | ``` var kAudioUnitProperty_LastRenderError: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_Latency

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_Latency: Int { get } ``` |
| To | ``` var kAudioUnitProperty_Latency: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MakeConnection

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MakeConnection: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MakeConnection: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MatrixDimensions

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MatrixDimensions: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MatrixDimensions: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MatrixLevels

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MatrixLevels: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MatrixLevels: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MaximumFramesPerSlice

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MaximumFramesPerSlice: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MaximumFramesPerSlice: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MeterClipping

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MeterClipping: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MeterClipping: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MeteringMode

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MeteringMode: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MeteringMode: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MIDIControlMapping

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MIDIControlMapping: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MIDIControlMapping: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MIDIOutputCallback

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MIDIOutputCallback: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MIDIOutputCallback: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_MIDIOutputCallbackInfo

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_MIDIOutputCallbackInfo: Int { get } ``` |
| To | ``` var kAudioUnitProperty_MIDIOutputCallbackInfo: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_NickName

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_NickName: Int { get } ``` |
| To | ``` var kAudioUnitProperty_NickName: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_OfflineRender

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_OfflineRender: Int { get } ``` |
| To | ``` var kAudioUnitProperty_OfflineRender: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_PannerMode

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_PannerMode: Int { get } ``` |
| To | ``` var kAudioUnitProperty_PannerMode: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterClumpName

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterClumpName: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterClumpName: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterHistoryInfo

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterHistoryInfo: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterHistoryInfo: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterIDName

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterIDName: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterIDName: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterInfo

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterInfo: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterInfo: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterList

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterList: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterList: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterStringFromValue

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterStringFromValue: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterStringFromValue: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterValueFromString

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterValueFromString: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterValueFromString: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterValueName

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterValueName: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterValueName: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ParameterValueStrings

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterValueStrings: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterValueStrings: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_PresentationLatency

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_PresentationLatency: Int { get } ``` |
| To | ``` var kAudioUnitProperty_PresentationLatency: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_PresentPreset

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_PresentPreset: Int { get } ``` |
| To | ``` var kAudioUnitProperty_PresentPreset: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_RemoveParameterMIDIMapping

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_RemoveParameterMIDIMapping: Int { get } ``` |
| To | ``` var kAudioUnitProperty_RemoveParameterMIDIMapping: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_RenderQuality

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_RenderQuality: Int { get } ``` |
| To | ``` var kAudioUnitProperty_RenderQuality: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ReverbPreset

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ReverbPreset: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ReverbPreset: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ReverbRoomType

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ReverbRoomType: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ReverbRoomType: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SampleRate

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SampleRate: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SampleRate: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SampleRateConverterComplexity

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SampleRateConverterComplexity: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SampleRateConverterComplexity: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ScheduleAudioSlice

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ScheduleAudioSlice: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ScheduleAudioSlice: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ScheduledFileBufferSizeFrames

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ScheduledFileBufferSizeFrames: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ScheduledFileBufferSizeFrames: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ScheduledFileIDs

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ScheduledFileIDs: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ScheduledFileIDs: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ScheduledFileNumberBuffers

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ScheduledFileNumberBuffers: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ScheduledFileNumberBuffers: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ScheduledFilePrime

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ScheduledFilePrime: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ScheduledFilePrime: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ScheduledFileRegion

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ScheduledFileRegion: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ScheduledFileRegion: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ScheduleStartTimeStamp

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ScheduleStartTimeStamp: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ScheduleStartTimeStamp: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SetExternalBuffer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SetExternalBuffer: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SetExternalBuffer: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SetRenderCallback

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SetRenderCallback: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SetRenderCallback: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_ShouldAllocateBuffer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ShouldAllocateBuffer: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ShouldAllocateBuffer: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SpatializationAlgorithm

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SpatializationAlgorithm: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SpatializationAlgorithm: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SpatialMixerAttenuationCurve

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SpatialMixerAttenuationCurve: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SpatialMixerAttenuationCurve: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SpatialMixerDistanceParams

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SpatialMixerDistanceParams: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SpatialMixerDistanceParams: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SpatialMixerRenderingFlags

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SpatialMixerRenderingFlags: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SpatialMixerRenderingFlags: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SpeakerConfiguration

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SpeakerConfiguration: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SpeakerConfiguration: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SRCAlgorithm

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SRCAlgorithm: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SRCAlgorithm: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_StreamFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_StreamFormat: Int { get } ``` |
| To | ``` var kAudioUnitProperty_StreamFormat: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SupportedChannelLayoutTags

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SupportedChannelLayoutTags: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SupportedChannelLayoutTags: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_SupportedNumChannels

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_SupportedNumChannels: Int { get } ``` |
| To | ``` var kAudioUnitProperty_SupportedNumChannels: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_TailTime

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_TailTime: Int { get } ``` |
| To | ``` var kAudioUnitProperty_TailTime: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_UsesInternalReverb

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_UsesInternalReverb: Int { get } ``` |
| To | ``` var kAudioUnitProperty_UsesInternalReverb: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitSampleRateConverterComplexity_Linear

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSampleRateConverterComplexity_Linear: Int { get } ``` |
| To | ``` var kAudioUnitSampleRateConverterComplexity_Linear: UInt32 { get } ``` |

Modified kAudioUnitSampleRateConverterComplexity_Mastering

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSampleRateConverterComplexity_Mastering: Int { get } ``` |
| To | ``` var kAudioUnitSampleRateConverterComplexity_Mastering: UInt32 { get } ``` |

Modified kAudioUnitSampleRateConverterComplexity_Normal

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSampleRateConverterComplexity_Normal: Int { get } ``` |
| To | ``` var kAudioUnitSampleRateConverterComplexity_Normal: UInt32 { get } ``` |

Modified kAudioUnitScope_Global

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitScope_Global: Int { get } ``` |
| To | ``` var kAudioUnitScope_Global: AudioUnitScope { get } ``` |

Modified kAudioUnitScope_Group

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitScope_Group: Int { get } ``` |
| To | ``` var kAudioUnitScope_Group: AudioUnitScope { get } ``` |

Modified kAudioUnitScope_Input

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitScope_Input: Int { get } ``` |
| To | ``` var kAudioUnitScope_Input: AudioUnitScope { get } ``` |

Modified kAudioUnitScope_Layer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitScope_Layer: Int { get } ``` |
| To | ``` var kAudioUnitScope_Layer: AudioUnitScope { get } ``` |

Modified kAudioUnitScope_LayerItem

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitScope_LayerItem: Int { get } ``` |
| To | ``` var kAudioUnitScope_LayerItem: AudioUnitScope { get } ``` |

Modified kAudioUnitScope_Note

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitScope_Note: Int { get } ``` |
| To | ``` var kAudioUnitScope_Note: AudioUnitScope { get } ``` |

Modified kAudioUnitScope_Output

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitScope_Output: Int { get } ``` |
| To | ``` var kAudioUnitScope_Output: AudioUnitScope { get } ``` |

Modified kAudioUnitScope_Part

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitScope_Part: Int { get } ``` |
| To | ``` var kAudioUnitScope_Part: AudioUnitScope { get } ``` |

Modified kAudioUnitSRCAlgorithm_MediumQuality

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSRCAlgorithm_MediumQuality: Int { get } ``` |
| To | ``` var kAudioUnitSRCAlgorithm_MediumQuality: UInt32 { get } ``` |

Modified kAudioUnitSRCAlgorithm_Polyphase

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSRCAlgorithm_Polyphase: Int { get } ``` |
| To | ``` var kAudioUnitSRCAlgorithm_Polyphase: UInt32 { get } ``` |

Modified kAudioUnitSubType_3DMixer

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` var kAudioUnitSubType_3DMixer: Int { get } ``` | OS X 10.10 | -- |
| To | ``` var kAudioUnitSubType_3DMixer: UInt32 { get } ``` | OS X 10.3 | OS X 10.10 |

Modified kAudioUnitSubType_AUConverter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_AUConverter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_AUConverter: UInt32 { get } ``` |

Modified kAudioUnitSubType_AudioFilePlayer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_AudioFilePlayer: Int { get } ``` |
| To | ``` var kAudioUnitSubType_AudioFilePlayer: UInt32 { get } ``` |

Modified kAudioUnitSubType_AUFilter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_AUFilter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_AUFilter: UInt32 { get } ``` |

Modified kAudioUnitSubType_AUiPodTimeOther

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_AUiPodTimeOther: Int { get } ``` |
| To | ``` var kAudioUnitSubType_AUiPodTimeOther: UInt32 { get } ``` |

Modified kAudioUnitSubType_BandPassFilter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_BandPassFilter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_BandPassFilter: UInt32 { get } ``` |

Modified kAudioUnitSubType_DefaultOutput

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_DefaultOutput: Int { get } ``` |
| To | ``` var kAudioUnitSubType_DefaultOutput: UInt32 { get } ``` |

Modified kAudioUnitSubType_DeferredRenderer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_DeferredRenderer: Int { get } ``` |
| To | ``` var kAudioUnitSubType_DeferredRenderer: UInt32 { get } ``` |

Modified kAudioUnitSubType_Delay

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Delay: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Delay: UInt32 { get } ``` |

Modified kAudioUnitSubType_Distortion

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Distortion: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Distortion: UInt32 { get } ``` |

Modified kAudioUnitSubType_DLSSynth

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_DLSSynth: Int { get } ``` |
| To | ``` var kAudioUnitSubType_DLSSynth: UInt32 { get } ``` |

Modified kAudioUnitSubType_DynamicsProcessor

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_DynamicsProcessor: Int { get } ``` |
| To | ``` var kAudioUnitSubType_DynamicsProcessor: UInt32 { get } ``` |

Modified kAudioUnitSubType_GenericOutput

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_GenericOutput: Int { get } ``` |
| To | ``` var kAudioUnitSubType_GenericOutput: UInt32 { get } ``` |

Modified kAudioUnitSubType_GraphicEQ

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_GraphicEQ: Int { get } ``` |
| To | ``` var kAudioUnitSubType_GraphicEQ: UInt32 { get } ``` |

Modified kAudioUnitSubType_HALOutput

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_HALOutput: Int { get } ``` |
| To | ``` var kAudioUnitSubType_HALOutput: UInt32 { get } ``` |

Modified kAudioUnitSubType_HighPassFilter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_HighPassFilter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_HighPassFilter: UInt32 { get } ``` |

Modified kAudioUnitSubType_HighShelfFilter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_HighShelfFilter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_HighShelfFilter: UInt32 { get } ``` |

Modified kAudioUnitSubType_HRTFPanner

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_HRTFPanner: Int { get } ``` |
| To | ``` var kAudioUnitSubType_HRTFPanner: UInt32 { get } ``` |

Modified kAudioUnitSubType_LowPassFilter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_LowPassFilter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_LowPassFilter: UInt32 { get } ``` |

Modified kAudioUnitSubType_LowShelfFilter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_LowShelfFilter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_LowShelfFilter: UInt32 { get } ``` |

Modified kAudioUnitSubType_MatrixMixer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_MatrixMixer: Int { get } ``` |
| To | ``` var kAudioUnitSubType_MatrixMixer: UInt32 { get } ``` |

Modified kAudioUnitSubType_MatrixReverb

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_MatrixReverb: Int { get } ``` |
| To | ``` var kAudioUnitSubType_MatrixReverb: UInt32 { get } ``` |

Modified kAudioUnitSubType_Merger

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Merger: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Merger: UInt32 { get } ``` |

Modified kAudioUnitSubType_MIDISynth

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_MIDISynth: Int { get } ``` |
| To | ``` var kAudioUnitSubType_MIDISynth: UInt32 { get } ``` |

Modified kAudioUnitSubType_MultiBandCompressor

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_MultiBandCompressor: Int { get } ``` |
| To | ``` var kAudioUnitSubType_MultiBandCompressor: UInt32 { get } ``` |

Modified kAudioUnitSubType_MultiChannelMixer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_MultiChannelMixer: Int { get } ``` |
| To | ``` var kAudioUnitSubType_MultiChannelMixer: UInt32 { get } ``` |

Modified kAudioUnitSubType_NBandEQ

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_NBandEQ: Int { get } ``` |
| To | ``` var kAudioUnitSubType_NBandEQ: UInt32 { get } ``` |

Modified kAudioUnitSubType_NetReceive

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_NetReceive: Int { get } ``` |
| To | ``` var kAudioUnitSubType_NetReceive: UInt32 { get } ``` |

Modified kAudioUnitSubType_NetSend

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_NetSend: Int { get } ``` |
| To | ``` var kAudioUnitSubType_NetSend: UInt32 { get } ``` |

Modified kAudioUnitSubType_NewTimePitch

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_NewTimePitch: Int { get } ``` |
| To | ``` var kAudioUnitSubType_NewTimePitch: UInt32 { get } ``` |

Modified kAudioUnitSubType_ParametricEQ

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_ParametricEQ: Int { get } ``` |
| To | ``` var kAudioUnitSubType_ParametricEQ: UInt32 { get } ``` |

Modified kAudioUnitSubType_PeakLimiter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_PeakLimiter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_PeakLimiter: UInt32 { get } ``` |

Modified kAudioUnitSubType_Pitch

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Pitch: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Pitch: UInt32 { get } ``` |

Modified kAudioUnitSubType_RogerBeep

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_RogerBeep: Int { get } ``` |
| To | ``` var kAudioUnitSubType_RogerBeep: UInt32 { get } ``` |

Modified kAudioUnitSubType_RoundTripAAC

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_RoundTripAAC: Int { get } ``` |
| To | ``` var kAudioUnitSubType_RoundTripAAC: UInt32 { get } ``` |

Modified kAudioUnitSubType_SampleDelay

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_SampleDelay: Int { get } ``` |
| To | ``` var kAudioUnitSubType_SampleDelay: UInt32 { get } ``` |

Modified kAudioUnitSubType_Sampler

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Sampler: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Sampler: UInt32 { get } ``` |

Modified kAudioUnitSubType_ScheduledSoundPlayer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_ScheduledSoundPlayer: Int { get } ``` |
| To | ``` var kAudioUnitSubType_ScheduledSoundPlayer: UInt32 { get } ``` |

Modified kAudioUnitSubType_SoundFieldPanner

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_SoundFieldPanner: Int { get } ``` |
| To | ``` var kAudioUnitSubType_SoundFieldPanner: UInt32 { get } ``` |

Modified kAudioUnitSubType_SpatialMixer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_SpatialMixer: Int { get } ``` |
| To | ``` var kAudioUnitSubType_SpatialMixer: UInt32 { get } ``` |

Modified kAudioUnitSubType_SphericalHeadPanner

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_SphericalHeadPanner: Int { get } ``` |
| To | ``` var kAudioUnitSubType_SphericalHeadPanner: UInt32 { get } ``` |

Modified kAudioUnitSubType_Splitter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Splitter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Splitter: UInt32 { get } ``` |

Modified kAudioUnitSubType_StereoMixer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_StereoMixer: Int { get } ``` |
| To | ``` var kAudioUnitSubType_StereoMixer: UInt32 { get } ``` |

Modified kAudioUnitSubType_SystemOutput

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_SystemOutput: Int { get } ``` |
| To | ``` var kAudioUnitSubType_SystemOutput: UInt32 { get } ``` |

Modified kAudioUnitSubType_TimePitch

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_TimePitch: Int { get } ``` |
| To | ``` var kAudioUnitSubType_TimePitch: UInt32 { get } ``` |

Modified kAudioUnitSubType_Varispeed

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Varispeed: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Varispeed: UInt32 { get } ``` |

Modified kAudioUnitSubType_VectorPanner

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_VectorPanner: Int { get } ``` |
| To | ``` var kAudioUnitSubType_VectorPanner: UInt32 { get } ``` |

Modified kAudioUnitSubType_VoiceProcessingIO

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_VoiceProcessingIO: Int { get } ``` |
| To | ``` var kAudioUnitSubType_VoiceProcessingIO: UInt32 { get } ``` |

Modified kAudioUnitType_Effect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_Effect: Int { get } ``` |
| To | ``` var kAudioUnitType_Effect: UInt32 { get } ``` |

Modified kAudioUnitType_FormatConverter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_FormatConverter: Int { get } ``` |
| To | ``` var kAudioUnitType_FormatConverter: UInt32 { get } ``` |

Modified kAudioUnitType_Generator

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_Generator: Int { get } ``` |
| To | ``` var kAudioUnitType_Generator: UInt32 { get } ``` |

Modified kAudioUnitType_MIDIProcessor

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_MIDIProcessor: Int { get } ``` |
| To | ``` var kAudioUnitType_MIDIProcessor: UInt32 { get } ``` |

Modified kAudioUnitType_Mixer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_Mixer: Int { get } ``` |
| To | ``` var kAudioUnitType_Mixer: UInt32 { get } ``` |

Modified kAudioUnitType_MusicDevice

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_MusicDevice: Int { get } ``` |
| To | ``` var kAudioUnitType_MusicDevice: UInt32 { get } ``` |

Modified kAudioUnitType_MusicEffect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_MusicEffect: Int { get } ``` |
| To | ``` var kAudioUnitType_MusicEffect: UInt32 { get } ``` |

Modified kAudioUnitType_OfflineEffect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_OfflineEffect: Int { get } ``` |
| To | ``` var kAudioUnitType_OfflineEffect: UInt32 { get } ``` |

Modified kAudioUnitType_Output

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_Output: Int { get } ``` |
| To | ``` var kAudioUnitType_Output: UInt32 { get } ``` |

Modified kAudioUnitType_Panner

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_Panner: Int { get } ``` |
| To | ``` var kAudioUnitType_Panner: UInt32 { get } ``` |

Modified kAudioUnityCodecComponentType

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnityCodecComponentType: Int { get } ``` |
| To | ``` var kAudioUnityCodecComponentType: UInt32 { get } ``` |

Modified kAUGroupParameterID_AllNotesOff

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_AllNotesOff: Int { get } ``` |
| To | ``` var kAUGroupParameterID_AllNotesOff: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_AllSoundOff

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_AllSoundOff: Int { get } ``` |
| To | ``` var kAUGroupParameterID_AllSoundOff: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_ChannelPressure

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_ChannelPressure: Int { get } ``` |
| To | ``` var kAUGroupParameterID_ChannelPressure: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_DataEntry

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_DataEntry: Int { get } ``` |
| To | ``` var kAUGroupParameterID_DataEntry: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_DataEntry_LSB

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_DataEntry_LSB: Int { get } ``` |
| To | ``` var kAUGroupParameterID_DataEntry_LSB: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Expression

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Expression: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Expression: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Expression_LSB

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Expression_LSB: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Expression_LSB: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Foot

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Foot: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Foot: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Foot_LSB

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Foot_LSB: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Foot_LSB: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_KeyPressure

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_KeyPressure: Int { get } ``` |
| To | ``` var kAUGroupParameterID_KeyPressure: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_KeyPressure_FirstKey

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_KeyPressure_FirstKey: Int { get } ``` |
| To | ``` var kAUGroupParameterID_KeyPressure_FirstKey: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_KeyPressure_LastKey

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_KeyPressure_LastKey: Int { get } ``` |
| To | ``` var kAUGroupParameterID_KeyPressure_LastKey: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_ModWheel

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_ModWheel: Int { get } ``` |
| To | ``` var kAUGroupParameterID_ModWheel: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_ModWheel_LSB

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_ModWheel_LSB: Int { get } ``` |
| To | ``` var kAUGroupParameterID_ModWheel_LSB: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Pan

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Pan: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Pan: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Pan_LSB

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Pan_LSB: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Pan_LSB: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_PitchBend

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_PitchBend: Int { get } ``` |
| To | ``` var kAUGroupParameterID_PitchBend: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_ResetAllControllers

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_ResetAllControllers: Int { get } ``` |
| To | ``` var kAUGroupParameterID_ResetAllControllers: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Sostenuto

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Sostenuto: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Sostenuto: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Sustain

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Sustain: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Sustain: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Volume

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Volume: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Volume: AudioUnitParameterID { get } ``` |

Modified kAUGroupParameterID_Volume_LSB

|  | Declaration |
| --- | --- |
| From | ``` var kAUGroupParameterID_Volume_LSB: Int { get } ``` |
| To | ``` var kAUGroupParameterID_Volume_LSB: AudioUnitParameterID { get } ``` |

Modified kAULowShelfParam_CutoffFrequency

|  | Declaration |
| --- | --- |
| From | ``` var kAULowShelfParam_CutoffFrequency: Int { get } ``` |
| To | ``` var kAULowShelfParam_CutoffFrequency: AudioUnitParameterID { get } ``` |

Modified kAULowShelfParam_Gain

|  | Declaration |
| --- | --- |
| From | ``` var kAULowShelfParam_Gain: Int { get } ``` |
| To | ``` var kAULowShelfParam_Gain: AudioUnitParameterID { get } ``` |

Modified kAUMIDISynthProperty_EnablePreload

|  | Declaration |
| --- | --- |
| From | ``` var kAUMIDISynthProperty_EnablePreload: Int { get } ``` |
| To | ``` var kAUMIDISynthProperty_EnablePreload: AudioUnitPropertyID { get } ``` |

Modified kAUNBandEQParam_Bandwidth

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQParam_Bandwidth: Int { get } ``` |
| To | ``` var kAUNBandEQParam_Bandwidth: AudioUnitParameterID { get } ``` |

Modified kAUNBandEQParam_BypassBand

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQParam_BypassBand: Int { get } ``` |
| To | ``` var kAUNBandEQParam_BypassBand: AudioUnitParameterID { get } ``` |

Modified kAUNBandEQParam_FilterType

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQParam_FilterType: Int { get } ``` |
| To | ``` var kAUNBandEQParam_FilterType: AudioUnitParameterID { get } ``` |

Modified kAUNBandEQParam_Frequency

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQParam_Frequency: Int { get } ``` |
| To | ``` var kAUNBandEQParam_Frequency: AudioUnitParameterID { get } ``` |

Modified kAUNBandEQParam_Gain

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQParam_Gain: Int { get } ``` |
| To | ``` var kAUNBandEQParam_Gain: AudioUnitParameterID { get } ``` |

Modified kAUNBandEQParam_GlobalGain

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQParam_GlobalGain: Int { get } ``` |
| To | ``` var kAUNBandEQParam_GlobalGain: AudioUnitParameterID { get } ``` |

Modified kAUNBandEQProperty_BiquadCoefficients

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQProperty_BiquadCoefficients: Int { get } ``` |
| To | ``` var kAUNBandEQProperty_BiquadCoefficients: AudioUnitPropertyID { get } ``` |

Modified kAUNBandEQProperty_MaxNumberOfBands

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQProperty_MaxNumberOfBands: Int { get } ``` |
| To | ``` var kAUNBandEQProperty_MaxNumberOfBands: AudioUnitPropertyID { get } ``` |

Modified kAUNBandEQProperty_NumberOfBands

|  | Declaration |
| --- | --- |
| From | ``` var kAUNBandEQProperty_NumberOfBands: Int { get } ``` |
| To | ``` var kAUNBandEQProperty_NumberOfBands: AudioUnitPropertyID { get } ``` |

Modified kAUNetReceiveParam_NumParameters

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetReceiveParam_NumParameters: Int { get } ``` |
| To | ``` var kAUNetReceiveParam_NumParameters: AudioUnitParameterID { get } ``` |

Modified kAUNetReceiveParam_Status

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetReceiveParam_Status: Int { get } ``` |
| To | ``` var kAUNetReceiveParam_Status: AudioUnitParameterID { get } ``` |

Modified kAUNetReceiveProperty_Hostname

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetReceiveProperty_Hostname: Int { get } ``` |
| To | ``` var kAUNetReceiveProperty_Hostname: AudioUnitPropertyID { get } ``` |

Modified kAUNetReceiveProperty_Password

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetReceiveProperty_Password: Int { get } ``` |
| To | ``` var kAUNetReceiveProperty_Password: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendNumPresetFormats

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendNumPresetFormats: Int { get } ``` |
| To | ``` var kAUNetSendNumPresetFormats: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendParam_NumParameters

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendParam_NumParameters: Int { get } ``` |
| To | ``` var kAUNetSendParam_NumParameters: AudioUnitParameterID { get } ``` |

Modified kAUNetSendParam_Status

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendParam_Status: Int { get } ``` |
| To | ``` var kAUNetSendParam_Status: AudioUnitParameterID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_128kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_128kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_128kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_32kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_32kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_32kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_40kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_40kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_40kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_48kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_48kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_48kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_64kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_64kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_64kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_80kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_80kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_80kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_96kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_96kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_96kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_LD_32kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_LD_32kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_LD_32kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_LD_40kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_LD_40kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_LD_40kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_LD_48kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_LD_48kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_LD_48kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_AAC_LD_64kbpspc

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_AAC_LD_64kbpspc: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_AAC_LD_64kbpspc: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_IMA4

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_IMA4: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_IMA4: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_Lossless16

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_Lossless16: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_Lossless16: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_Lossless24

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_Lossless24: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_Lossless24: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_PCMFloat32

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_PCMFloat32: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_PCMFloat32: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_PCMInt16

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_PCMInt16: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_PCMInt16: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_PCMInt24

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_PCMInt24: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_PCMInt24: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendPresetFormat_ULaw

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendPresetFormat_ULaw: Int { get } ``` |
| To | ``` var kAUNetSendPresetFormat_ULaw: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendProperty_Disconnect

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendProperty_Disconnect: Int { get } ``` |
| To | ``` var kAUNetSendProperty_Disconnect: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendProperty_Password

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendProperty_Password: Int { get } ``` |
| To | ``` var kAUNetSendProperty_Password: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendProperty_PortNum

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendProperty_PortNum: Int { get } ``` |
| To | ``` var kAUNetSendProperty_PortNum: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendProperty_ServiceName

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendProperty_ServiceName: Int { get } ``` |
| To | ``` var kAUNetSendProperty_ServiceName: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendProperty_TransmissionFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendProperty_TransmissionFormat: Int { get } ``` |
| To | ``` var kAUNetSendProperty_TransmissionFormat: AudioUnitPropertyID { get } ``` |

Modified kAUNetSendProperty_TransmissionFormatIndex

|  | Declaration |
| --- | --- |
| From | ``` var kAUNetSendProperty_TransmissionFormatIndex: Int { get } ``` |
| To | ``` var kAUNetSendProperty_TransmissionFormatIndex: AudioUnitPropertyID { get } ``` |

Modified kAUSamplerParam_CoarseTuning

|  | Declaration |
| --- | --- |
| From | ``` var kAUSamplerParam_CoarseTuning: Int { get } ``` |
| To | ``` var kAUSamplerParam_CoarseTuning: AudioUnitParameterID { get } ``` |

Modified kAUSamplerParam_FineTuning

|  | Declaration |
| --- | --- |
| From | ``` var kAUSamplerParam_FineTuning: Int { get } ``` |
| To | ``` var kAUSamplerParam_FineTuning: AudioUnitParameterID { get } ``` |

Modified kAUSamplerParam_Gain

|  | Declaration |
| --- | --- |
| From | ``` var kAUSamplerParam_Gain: Int { get } ``` |
| To | ``` var kAUSamplerParam_Gain: AudioUnitParameterID { get } ``` |

Modified kAUSamplerParam_Pan

|  | Declaration |
| --- | --- |
| From | ``` var kAUSamplerParam_Pan: Int { get } ``` |
| To | ``` var kAUSamplerParam_Pan: AudioUnitParameterID { get } ``` |

Modified kAUSamplerProperty_BankAndPreset

|  | Declaration |
| --- | --- |
| From | ``` var kAUSamplerProperty_BankAndPreset: Int { get } ``` |
| To | ``` var kAUSamplerProperty_BankAndPreset: AudioUnitPropertyID { get } ``` |

Modified kAUSamplerProperty_LoadAudioFiles

|  | Declaration |
| --- | --- |
| From | ``` var kAUSamplerProperty_LoadAudioFiles: Int { get } ``` |
| To | ``` var kAUSamplerProperty_LoadAudioFiles: AudioUnitPropertyID { get } ``` |

Modified kAUSamplerProperty_LoadInstrument

|  | Declaration |
| --- | --- |
| From | ``` var kAUSamplerProperty_LoadInstrument: Int { get } ``` |
| To | ``` var kAUSamplerProperty_LoadInstrument: AudioUnitPropertyID { get } ``` |

Modified kAUSamplerProperty_LoadPresetFromBank

|  | Declaration |
| --- | --- |
| From | ``` var kAUSamplerProperty_LoadPresetFromBank: Int { get } ``` |
| To | ``` var kAUSamplerProperty_LoadPresetFromBank: AudioUnitPropertyID { get } ``` |

Modified kAUVoiceIOErr_UnexpectedNumberOfInputChannels

|  | Declaration |
| --- | --- |
| From | ``` var kAUVoiceIOErr_UnexpectedNumberOfInputChannels: Int { get } ``` |
| To | ``` var kAUVoiceIOErr_UnexpectedNumberOfInputChannels: OSStatus { get } ``` |

Modified kAUVoiceIOProperty_BypassVoiceProcessing

|  | Declaration |
| --- | --- |
| From | ``` var kAUVoiceIOProperty_BypassVoiceProcessing: Int { get } ``` |
| To | ``` var kAUVoiceIOProperty_BypassVoiceProcessing: AudioUnitPropertyID { get } ``` |

Modified kAUVoiceIOProperty_MuteOutput

|  | Declaration |
| --- | --- |
| From | ``` var kAUVoiceIOProperty_MuteOutput: Int { get } ``` |
| To | ``` var kAUVoiceIOProperty_MuteOutput: AudioUnitPropertyID { get } ``` |

Modified kAUVoiceIOProperty_VoiceProcessingEnableAGC

|  | Declaration |
| --- | --- |
| From | ``` var kAUVoiceIOProperty_VoiceProcessingEnableAGC: Int { get } ``` |
| To | ``` var kAUVoiceIOProperty_VoiceProcessingEnableAGC: AudioUnitPropertyID { get } ``` |

Modified kAUVoiceIOProperty_VoiceProcessingQuality

|  | Declaration |
| --- | --- |
| From | ``` var kAUVoiceIOProperty_VoiceProcessingQuality: Int { get } ``` |
| To | ``` var kAUVoiceIOProperty_VoiceProcessingQuality: AudioUnitPropertyID { get } ``` |

Modified kBandpassParam_Bandwidth

|  | Declaration |
| --- | --- |
| From | ``` var kBandpassParam_Bandwidth: Int { get } ``` |
| To | ``` var kBandpassParam_Bandwidth: AudioUnitParameterID { get } ``` |

Modified kBandpassParam_CenterFrequency

|  | Declaration |
| --- | --- |
| From | ``` var kBandpassParam_CenterFrequency: Int { get } ``` |
| To | ``` var kBandpassParam_CenterFrequency: AudioUnitParameterID { get } ``` |

Modified kDelayParam_DelayTime

|  | Declaration |
| --- | --- |
| From | ``` var kDelayParam_DelayTime: Int { get } ``` |
| To | ``` var kDelayParam_DelayTime: AudioUnitParameterID { get } ``` |

Modified kDelayParam_Feedback

|  | Declaration |
| --- | --- |
| From | ``` var kDelayParam_Feedback: Int { get } ``` |
| To | ``` var kDelayParam_Feedback: AudioUnitParameterID { get } ``` |

Modified kDelayParam_LopassCutoff

|  | Declaration |
| --- | --- |
| From | ``` var kDelayParam_LopassCutoff: Int { get } ``` |
| To | ``` var kDelayParam_LopassCutoff: AudioUnitParameterID { get } ``` |

Modified kDelayParam_WetDryMix

|  | Declaration |
| --- | --- |
| From | ``` var kDelayParam_WetDryMix: Int { get } ``` |
| To | ``` var kDelayParam_WetDryMix: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_CubicTerm

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_CubicTerm: Int { get } ``` |
| To | ``` var kDistortionParam_CubicTerm: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_Decay

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_Decay: Int { get } ``` |
| To | ``` var kDistortionParam_Decay: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_Decimation

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_Decimation: Int { get } ``` |
| To | ``` var kDistortionParam_Decimation: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_DecimationMix

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_DecimationMix: Int { get } ``` |
| To | ``` var kDistortionParam_DecimationMix: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_Delay

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_Delay: Int { get } ``` |
| To | ``` var kDistortionParam_Delay: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_DelayMix

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_DelayMix: Int { get } ``` |
| To | ``` var kDistortionParam_DelayMix: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_FinalMix

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_FinalMix: Int { get } ``` |
| To | ``` var kDistortionParam_FinalMix: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_LinearTerm

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_LinearTerm: Int { get } ``` |
| To | ``` var kDistortionParam_LinearTerm: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_PolynomialMix

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_PolynomialMix: Int { get } ``` |
| To | ``` var kDistortionParam_PolynomialMix: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_RingModBalance

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_RingModBalance: Int { get } ``` |
| To | ``` var kDistortionParam_RingModBalance: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_RingModFreq1

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_RingModFreq1: Int { get } ``` |
| To | ``` var kDistortionParam_RingModFreq1: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_RingModFreq2

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_RingModFreq2: Int { get } ``` |
| To | ``` var kDistortionParam_RingModFreq2: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_RingModMix

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_RingModMix: Int { get } ``` |
| To | ``` var kDistortionParam_RingModMix: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_Rounding

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_Rounding: Int { get } ``` |
| To | ``` var kDistortionParam_Rounding: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_SoftClipGain

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_SoftClipGain: Int { get } ``` |
| To | ``` var kDistortionParam_SoftClipGain: AudioUnitParameterID { get } ``` |

Modified kDistortionParam_SquaredTerm

|  | Declaration |
| --- | --- |
| From | ``` var kDistortionParam_SquaredTerm: Int { get } ``` |
| To | ``` var kDistortionParam_SquaredTerm: AudioUnitParameterID { get } ``` |

Modified kDynamicRangeControlMode_Heavy

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicRangeControlMode_Heavy: Int { get } ``` |
| To | ``` var kDynamicRangeControlMode_Heavy: UInt32 { get } ``` |

Modified kDynamicRangeControlMode_Light

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicRangeControlMode_Light: Int { get } ``` |
| To | ``` var kDynamicRangeControlMode_Light: UInt32 { get } ``` |

Modified kDynamicRangeControlMode_None

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicRangeControlMode_None: Int { get } ``` |
| To | ``` var kDynamicRangeControlMode_None: UInt32 { get } ``` |

Modified kDynamicsProcessorParam_AttackTime

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_AttackTime: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_AttackTime: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_CompressionAmount

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_CompressionAmount: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_CompressionAmount: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_ExpansionRatio

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_ExpansionRatio: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_ExpansionRatio: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_ExpansionThreshold

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_ExpansionThreshold: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_ExpansionThreshold: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_HeadRoom

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_HeadRoom: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_HeadRoom: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_InputAmplitude

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_InputAmplitude: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_InputAmplitude: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_MasterGain

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_MasterGain: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_MasterGain: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_OutputAmplitude

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_OutputAmplitude: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_OutputAmplitude: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_ReleaseTime

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_ReleaseTime: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_ReleaseTime: AudioUnitParameterID { get } ``` |

Modified kDynamicsProcessorParam_Threshold

|  | Declaration |
| --- | --- |
| From | ``` var kDynamicsProcessorParam_Threshold: Int { get } ``` |
| To | ``` var kDynamicsProcessorParam_Threshold: AudioUnitParameterID { get } ``` |

Modified kGraphicEQParam_NumberOfBands

|  | Declaration |
| --- | --- |
| From | ``` var kGraphicEQParam_NumberOfBands: Int { get } ``` |
| To | ``` var kGraphicEQParam_NumberOfBands: AudioUnitParameterID { get } ``` |

Modified kHALOutputParam_Volume

|  | Declaration |
| --- | --- |
| From | ``` var kHALOutputParam_Volume: Int { get } ``` |
| To | ``` var kHALOutputParam_Volume: AudioUnitParameterID { get } ``` |

Modified kHighShelfParam_CutOffFrequency

|  | Declaration |
| --- | --- |
| From | ``` var kHighShelfParam_CutOffFrequency: Int { get } ``` |
| To | ``` var kHighShelfParam_CutOffFrequency: AudioUnitParameterID { get } ``` |

Modified kHighShelfParam_Gain

|  | Declaration |
| --- | --- |
| From | ``` var kHighShelfParam_Gain: Int { get } ``` |
| To | ``` var kHighShelfParam_Gain: AudioUnitParameterID { get } ``` |

Modified kHintAdvanced

|  | Declaration |
| --- | --- |
| From | ``` var kHintAdvanced: Int { get } ``` |
| To | ``` var kHintAdvanced: UInt32 { get } ``` |

Modified kHintBasic

|  | Declaration |
| --- | --- |
| From | ``` var kHintBasic: Int { get } ``` |
| To | ``` var kHintBasic: UInt32 { get } ``` |

Modified kHintHidden

|  | Declaration |
| --- | --- |
| From | ``` var kHintHidden: Int { get } ``` |
| To | ``` var kHintHidden: UInt32 { get } ``` |

Modified kHipassParam_CutoffFrequency

|  | Declaration |
| --- | --- |
| From | ``` var kHipassParam_CutoffFrequency: Int { get } ``` |
| To | ``` var kHipassParam_CutoffFrequency: AudioUnitParameterID { get } ``` |

Modified kHipassParam_Resonance

|  | Declaration |
| --- | --- |
| From | ``` var kHipassParam_Resonance: Int { get } ``` |
| To | ``` var kHipassParam_Resonance: AudioUnitParameterID { get } ``` |

Modified kLimiterParam_AttackTime

|  | Declaration |
| --- | --- |
| From | ``` var kLimiterParam_AttackTime: Int { get } ``` |
| To | ``` var kLimiterParam_AttackTime: AudioUnitParameterID { get } ``` |

Modified kLimiterParam_DecayTime

|  | Declaration |
| --- | --- |
| From | ``` var kLimiterParam_DecayTime: Int { get } ``` |
| To | ``` var kLimiterParam_DecayTime: AudioUnitParameterID { get } ``` |

Modified kLimiterParam_PreGain

|  | Declaration |
| --- | --- |
| From | ``` var kLimiterParam_PreGain: Int { get } ``` |
| To | ``` var kLimiterParam_PreGain: AudioUnitParameterID { get } ``` |

Modified kLowPassParam_CutoffFrequency

|  | Declaration |
| --- | --- |
| From | ``` var kLowPassParam_CutoffFrequency: Int { get } ``` |
| To | ``` var kLowPassParam_CutoffFrequency: AudioUnitParameterID { get } ``` |

Modified kLowPassParam_Resonance

|  | Declaration |
| --- | --- |
| From | ``` var kLowPassParam_Resonance: Int { get } ``` |
| To | ``` var kLowPassParam_Resonance: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_Enable

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_Enable: Int { get } ``` |
| To | ``` var kMatrixMixerParam_Enable: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_PostAveragePower

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_PostAveragePower: Int { get } ``` |
| To | ``` var kMatrixMixerParam_PostAveragePower: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_PostAveragePowerLinear

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_PostAveragePowerLinear: Int { get } ``` |
| To | ``` var kMatrixMixerParam_PostAveragePowerLinear: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_PostPeakHoldLevel

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_PostPeakHoldLevel: Int { get } ``` |
| To | ``` var kMatrixMixerParam_PostPeakHoldLevel: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_PostPeakHoldLevelLinear

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_PostPeakHoldLevelLinear: Int { get } ``` |
| To | ``` var kMatrixMixerParam_PostPeakHoldLevelLinear: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_PreAveragePower

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_PreAveragePower: Int { get } ``` |
| To | ``` var kMatrixMixerParam_PreAveragePower: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_PreAveragePowerLinear

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_PreAveragePowerLinear: Int { get } ``` |
| To | ``` var kMatrixMixerParam_PreAveragePowerLinear: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_PrePeakHoldLevel

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_PrePeakHoldLevel: Int { get } ``` |
| To | ``` var kMatrixMixerParam_PrePeakHoldLevel: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_PrePeakHoldLevelLinear

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_PrePeakHoldLevelLinear: Int { get } ``` |
| To | ``` var kMatrixMixerParam_PrePeakHoldLevelLinear: AudioUnitParameterID { get } ``` |

Modified kMatrixMixerParam_Volume

|  | Declaration |
| --- | --- |
| From | ``` var kMatrixMixerParam_Volume: Int { get } ``` |
| To | ``` var kMatrixMixerParam_Volume: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_AttackTime

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_AttackTime: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_AttackTime: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_CompressionAmount1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_CompressionAmount1: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_CompressionAmount1: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_CompressionAmount2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_CompressionAmount2: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_CompressionAmount2: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_CompressionAmount3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_CompressionAmount3: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_CompressionAmount3: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_CompressionAmount4

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_CompressionAmount4: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_CompressionAmount4: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Crossover1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Crossover1: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Crossover1: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Crossover2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Crossover2: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Crossover2: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Crossover3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Crossover3: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Crossover3: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_EQ1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_EQ1: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_EQ1: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_EQ2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_EQ2: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_EQ2: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_EQ3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_EQ3: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_EQ3: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_EQ4

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_EQ4: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_EQ4: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Headroom1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Headroom1: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Headroom1: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Headroom2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Headroom2: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Headroom2: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Headroom3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Headroom3: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Headroom3: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Headroom4

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Headroom4: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Headroom4: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_InputAmplitude1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_InputAmplitude1: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_InputAmplitude1: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_InputAmplitude2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_InputAmplitude2: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_InputAmplitude2: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_InputAmplitude3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_InputAmplitude3: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_InputAmplitude3: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_InputAmplitude4

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_InputAmplitude4: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_InputAmplitude4: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_OutputAmplitude1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_OutputAmplitude1: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_OutputAmplitude1: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_OutputAmplitude2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_OutputAmplitude2: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_OutputAmplitude2: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_OutputAmplitude3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_OutputAmplitude3: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_OutputAmplitude3: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_OutputAmplitude4

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_OutputAmplitude4: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_OutputAmplitude4: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Postgain

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Postgain: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Postgain: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Pregain

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Pregain: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Pregain: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_ReleaseTime

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_ReleaseTime: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_ReleaseTime: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Threshold1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Threshold1: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Threshold1: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Threshold2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Threshold2: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Threshold2: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Threshold3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Threshold3: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Threshold3: AudioUnitParameterID { get } ``` |

Modified kMultibandCompressorParam_Threshold4

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandCompressorParam_Threshold4: Int { get } ``` |
| To | ``` var kMultibandCompressorParam_Threshold4: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_Bandwidth1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_Bandwidth1: Int { get } ``` |
| To | ``` var kMultibandFilter_Bandwidth1: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_Bandwidth2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_Bandwidth2: Int { get } ``` |
| To | ``` var kMultibandFilter_Bandwidth2: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_Bandwidth3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_Bandwidth3: Int { get } ``` |
| To | ``` var kMultibandFilter_Bandwidth3: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_CenterFreq1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_CenterFreq1: Int { get } ``` |
| To | ``` var kMultibandFilter_CenterFreq1: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_CenterFreq2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_CenterFreq2: Int { get } ``` |
| To | ``` var kMultibandFilter_CenterFreq2: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_CenterFreq3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_CenterFreq3: Int { get } ``` |
| To | ``` var kMultibandFilter_CenterFreq3: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_CenterGain1

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_CenterGain1: Int { get } ``` |
| To | ``` var kMultibandFilter_CenterGain1: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_CenterGain2

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_CenterGain2: Int { get } ``` |
| To | ``` var kMultibandFilter_CenterGain2: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_CenterGain3

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_CenterGain3: Int { get } ``` |
| To | ``` var kMultibandFilter_CenterGain3: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_HighFilterType

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_HighFilterType: Int { get } ``` |
| To | ``` var kMultibandFilter_HighFilterType: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_HighFrequency

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_HighFrequency: Int { get } ``` |
| To | ``` var kMultibandFilter_HighFrequency: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_HighGain

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_HighGain: Int { get } ``` |
| To | ``` var kMultibandFilter_HighGain: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_LowFilterType

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_LowFilterType: Int { get } ``` |
| To | ``` var kMultibandFilter_LowFilterType: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_LowFrequency

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_LowFrequency: Int { get } ``` |
| To | ``` var kMultibandFilter_LowFrequency: AudioUnitParameterID { get } ``` |

Modified kMultibandFilter_LowGain

|  | Declaration |
| --- | --- |
| From | ``` var kMultibandFilter_LowGain: Int { get } ``` |
| To | ``` var kMultibandFilter_LowGain: AudioUnitParameterID { get } ``` |

Modified kMultiChannelMixerParam_Enable

|  | Declaration |
| --- | --- |
| From | ``` var kMultiChannelMixerParam_Enable: Int { get } ``` |
| To | ``` var kMultiChannelMixerParam_Enable: AudioUnitParameterID { get } ``` |

Modified kMultiChannelMixerParam_Pan

|  | Declaration |
| --- | --- |
| From | ``` var kMultiChannelMixerParam_Pan: Int { get } ``` |
| To | ``` var kMultiChannelMixerParam_Pan: AudioUnitParameterID { get } ``` |

Modified kMultiChannelMixerParam_PostAveragePower

|  | Declaration |
| --- | --- |
| From | ``` var kMultiChannelMixerParam_PostAveragePower: Int { get } ``` |
| To | ``` var kMultiChannelMixerParam_PostAveragePower: AudioUnitParameterID { get } ``` |

Modified kMultiChannelMixerParam_PostPeakHoldLevel

|  | Declaration |
| --- | --- |
| From | ``` var kMultiChannelMixerParam_PostPeakHoldLevel: Int { get } ``` |
| To | ``` var kMultiChannelMixerParam_PostPeakHoldLevel: AudioUnitParameterID { get } ``` |

Modified kMultiChannelMixerParam_PreAveragePower

|  | Declaration |
| --- | --- |
| From | ``` var kMultiChannelMixerParam_PreAveragePower: Int { get } ``` |
| To | ``` var kMultiChannelMixerParam_PreAveragePower: AudioUnitParameterID { get } ``` |

Modified kMultiChannelMixerParam_PrePeakHoldLevel

|  | Declaration |
| --- | --- |
| From | ``` var kMultiChannelMixerParam_PrePeakHoldLevel: Int { get } ``` |
| To | ``` var kMultiChannelMixerParam_PrePeakHoldLevel: AudioUnitParameterID { get } ``` |

Modified kMultiChannelMixerParam_Volume

|  | Declaration |
| --- | --- |
| From | ``` var kMultiChannelMixerParam_Volume: Int { get } ``` |
| To | ``` var kMultiChannelMixerParam_Volume: AudioUnitParameterID { get } ``` |

Modified kMusicDeviceParam_ReverbVolume

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceParam_ReverbVolume: Int { get } ``` |
| To | ``` var kMusicDeviceParam_ReverbVolume: AudioUnitParameterID { get } ``` |

Modified kMusicDeviceParam_Tuning

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceParam_Tuning: Int { get } ``` |
| To | ``` var kMusicDeviceParam_Tuning: AudioUnitParameterID { get } ``` |

Modified kMusicDeviceParam_Volume

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceParam_Volume: Int { get } ``` |
| To | ``` var kMusicDeviceParam_Volume: AudioUnitParameterID { get } ``` |

Modified kMusicDeviceProperty_BankName

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_BankName: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_BankName: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_DualSchedulingMode

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_DualSchedulingMode: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_DualSchedulingMode: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_GroupOutputBus

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_GroupOutputBus: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_GroupOutputBus: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_InstrumentCount

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_InstrumentCount: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_InstrumentCount: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_InstrumentName

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_InstrumentName: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_InstrumentName: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_InstrumentNumber

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_InstrumentNumber: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_InstrumentNumber: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_MIDIXMLNames

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_MIDIXMLNames: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_MIDIXMLNames: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_PartGroup

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_PartGroup: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_PartGroup: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_SoundBankData

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_SoundBankData: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_SoundBankData: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_SoundBankFSRef

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_SoundBankFSRef: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_SoundBankFSRef: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_SoundBankFSSpec

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_SoundBankFSSpec: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_SoundBankFSSpec: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_SoundBankURL

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_SoundBankURL: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_SoundBankURL: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_StreamFromDisk

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_StreamFromDisk: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_StreamFromDisk: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_SupportsStartStopNote

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_SupportsStartStopNote: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_SupportsStartStopNote: AudioUnitPropertyID { get } ``` |

Modified kMusicDeviceProperty_UsesInternalReverb

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_UsesInternalReverb: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_UsesInternalReverb: AudioUnitPropertyID { get } ``` |

Modified kNewTimePitchParam_EnablePeakLocking

|  | Declaration |
| --- | --- |
| From | ``` var kNewTimePitchParam_EnablePeakLocking: Int { get } ``` |
| To | ``` var kNewTimePitchParam_EnablePeakLocking: AudioUnitParameterID { get } ``` |

Modified kNewTimePitchParam_Overlap

|  | Declaration |
| --- | --- |
| From | ``` var kNewTimePitchParam_Overlap: Int { get } ``` |
| To | ``` var kNewTimePitchParam_Overlap: AudioUnitParameterID { get } ``` |

Modified kNewTimePitchParam_Pitch

|  | Declaration |
| --- | --- |
| From | ``` var kNewTimePitchParam_Pitch: Int { get } ``` |
| To | ``` var kNewTimePitchParam_Pitch: AudioUnitParameterID { get } ``` |

Modified kNewTimePitchParam_Rate

|  | Declaration |
| --- | --- |
| From | ``` var kNewTimePitchParam_Rate: Int { get } ``` |
| To | ``` var kNewTimePitchParam_Rate: AudioUnitParameterID { get } ``` |

Modified kOtherPluginFormat_AU

|  | Declaration |
| --- | --- |
| From | ``` var kOtherPluginFormat_AU: Int { get } ``` |
| To | ``` var kOtherPluginFormat_AU: UInt32 { get } ``` |

Modified kOtherPluginFormat_kMAS

|  | Declaration |
| --- | --- |
| From | ``` var kOtherPluginFormat_kMAS: Int { get } ``` |
| To | ``` var kOtherPluginFormat_kMAS: UInt32 { get } ``` |

Modified kOtherPluginFormat_kVST

|  | Declaration |
| --- | --- |
| From | ``` var kOtherPluginFormat_kVST: Int { get } ``` |
| To | ``` var kOtherPluginFormat_kVST: UInt32 { get } ``` |

Modified kOtherPluginFormat_Undefined

|  | Declaration |
| --- | --- |
| From | ``` var kOtherPluginFormat_Undefined: Int { get } ``` |
| To | ``` var kOtherPluginFormat_Undefined: UInt32 { get } ``` |

Modified kPannerParam_Azimuth

|  | Declaration |
| --- | --- |
| From | ``` var kPannerParam_Azimuth: Int { get } ``` |
| To | ``` var kPannerParam_Azimuth: AudioUnitParameterID { get } ``` |

Modified kPannerParam_CoordScale

|  | Declaration |
| --- | --- |
| From | ``` var kPannerParam_CoordScale: Int { get } ``` |
| To | ``` var kPannerParam_CoordScale: AudioUnitParameterID { get } ``` |

Modified kPannerParam_Distance

|  | Declaration |
| --- | --- |
| From | ``` var kPannerParam_Distance: Int { get } ``` |
| To | ``` var kPannerParam_Distance: AudioUnitParameterID { get } ``` |

Modified kPannerParam_Elevation

|  | Declaration |
| --- | --- |
| From | ``` var kPannerParam_Elevation: Int { get } ``` |
| To | ``` var kPannerParam_Elevation: AudioUnitParameterID { get } ``` |

Modified kPannerParam_Gain

|  | Declaration |
| --- | --- |
| From | ``` var kPannerParam_Gain: Int { get } ``` |
| To | ``` var kPannerParam_Gain: AudioUnitParameterID { get } ``` |

Modified kPannerParam_RefDistance

|  | Declaration |
| --- | --- |
| From | ``` var kPannerParam_RefDistance: Int { get } ``` |
| To | ``` var kPannerParam_RefDistance: AudioUnitParameterID { get } ``` |

Modified kParametricEQParam_CenterFreq

|  | Declaration |
| --- | --- |
| From | ``` var kParametricEQParam_CenterFreq: Int { get } ``` |
| To | ``` var kParametricEQParam_CenterFreq: AudioUnitParameterID { get } ``` |

Modified kParametricEQParam_Gain

|  | Declaration |
| --- | --- |
| From | ``` var kParametricEQParam_Gain: Int { get } ``` |
| To | ``` var kParametricEQParam_Gain: AudioUnitParameterID { get } ``` |

Modified kParametricEQParam_Q

|  | Declaration |
| --- | --- |
| From | ``` var kParametricEQParam_Q: Int { get } ``` |
| To | ``` var kParametricEQParam_Q: AudioUnitParameterID { get } ``` |

Modified kProgramTargetLevel_Minus20dB

|  | Declaration |
| --- | --- |
| From | ``` var kProgramTargetLevel_Minus20dB: Int { get } ``` |
| To | ``` var kProgramTargetLevel_Minus20dB: UInt32 { get } ``` |

Modified kProgramTargetLevel_Minus23dB

|  | Declaration |
| --- | --- |
| From | ``` var kProgramTargetLevel_Minus23dB: Int { get } ``` |
| To | ``` var kProgramTargetLevel_Minus23dB: UInt32 { get } ``` |

Modified kProgramTargetLevel_Minus31dB

|  | Declaration |
| --- | --- |
| From | ``` var kProgramTargetLevel_Minus31dB: Int { get } ``` |
| To | ``` var kProgramTargetLevel_Minus31dB: UInt32 { get } ``` |

Modified kProgramTargetLevel_None

|  | Declaration |
| --- | --- |
| From | ``` var kProgramTargetLevel_None: Int { get } ``` |
| To | ``` var kProgramTargetLevel_None: UInt32 { get } ``` |

Modified kRandomParam_BoundA

|  | Declaration |
| --- | --- |
| From | ``` var kRandomParam_BoundA: Int { get } ``` |
| To | ``` var kRandomParam_BoundA: AudioUnitParameterID { get } ``` |

Modified kRandomParam_BoundB

|  | Declaration |
| --- | --- |
| From | ``` var kRandomParam_BoundB: Int { get } ``` |
| To | ``` var kRandomParam_BoundB: AudioUnitParameterID { get } ``` |

Modified kRandomParam_Curve

|  | Declaration |
| --- | --- |
| From | ``` var kRandomParam_Curve: Int { get } ``` |
| To | ``` var kRandomParam_Curve: AudioUnitParameterID { get } ``` |

Modified kReverbParam_DryWetMix

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_DryWetMix: Int { get } ``` |
| To | ``` var kReverbParam_DryWetMix: AudioUnitParameterID { get } ``` |

Modified kReverbParam_FilterBandwidth

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_FilterBandwidth: Int { get } ``` |
| To | ``` var kReverbParam_FilterBandwidth: AudioUnitParameterID { get } ``` |

Modified kReverbParam_FilterEnable

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_FilterEnable: Int { get } ``` |
| To | ``` var kReverbParam_FilterEnable: AudioUnitParameterID { get } ``` |

Modified kReverbParam_FilterFrequency

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_FilterFrequency: Int { get } ``` |
| To | ``` var kReverbParam_FilterFrequency: AudioUnitParameterID { get } ``` |

Modified kReverbParam_FilterGain

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_FilterGain: Int { get } ``` |
| To | ``` var kReverbParam_FilterGain: AudioUnitParameterID { get } ``` |

Modified kReverbParam_FilterType

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_FilterType: Int { get } ``` |
| To | ``` var kReverbParam_FilterType: AudioUnitParameterID { get } ``` |

Modified kReverbParam_LargeBrightness

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_LargeBrightness: Int { get } ``` |
| To | ``` var kReverbParam_LargeBrightness: AudioUnitParameterID { get } ``` |

Modified kReverbParam_LargeDelay

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_LargeDelay: Int { get } ``` |
| To | ``` var kReverbParam_LargeDelay: AudioUnitParameterID { get } ``` |

Modified kReverbParam_LargeDelayRange

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_LargeDelayRange: Int { get } ``` |
| To | ``` var kReverbParam_LargeDelayRange: AudioUnitParameterID { get } ``` |

Modified kReverbParam_LargeDensity

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_LargeDensity: Int { get } ``` |
| To | ``` var kReverbParam_LargeDensity: AudioUnitParameterID { get } ``` |

Modified kReverbParam_LargeSize

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_LargeSize: Int { get } ``` |
| To | ``` var kReverbParam_LargeSize: AudioUnitParameterID { get } ``` |

Modified kReverbParam_ModulationDepth

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_ModulationDepth: Int { get } ``` |
| To | ``` var kReverbParam_ModulationDepth: AudioUnitParameterID { get } ``` |

Modified kReverbParam_ModulationRate

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_ModulationRate: Int { get } ``` |
| To | ``` var kReverbParam_ModulationRate: AudioUnitParameterID { get } ``` |

Modified kReverbParam_PreDelay

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_PreDelay: Int { get } ``` |
| To | ``` var kReverbParam_PreDelay: AudioUnitParameterID { get } ``` |

Modified kReverbParam_SmallBrightness

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_SmallBrightness: Int { get } ``` |
| To | ``` var kReverbParam_SmallBrightness: AudioUnitParameterID { get } ``` |

Modified kReverbParam_SmallDelayRange

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_SmallDelayRange: Int { get } ``` |
| To | ``` var kReverbParam_SmallDelayRange: AudioUnitParameterID { get } ``` |

Modified kReverbParam_SmallDensity

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_SmallDensity: Int { get } ``` |
| To | ``` var kReverbParam_SmallDensity: AudioUnitParameterID { get } ``` |

Modified kReverbParam_SmallLargeMix

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_SmallLargeMix: Int { get } ``` |
| To | ``` var kReverbParam_SmallLargeMix: AudioUnitParameterID { get } ``` |

Modified kReverbParam_SmallSize

|  | Declaration |
| --- | --- |
| From | ``` var kReverbParam_SmallSize: Int { get } ``` |
| To | ``` var kReverbParam_SmallSize: AudioUnitParameterID { get } ``` |

Modified kRogerBeepParam_InGateThreshold

|  | Declaration |
| --- | --- |
| From | ``` var kRogerBeepParam_InGateThreshold: Int { get } ``` |
| To | ``` var kRogerBeepParam_InGateThreshold: AudioUnitParameterID { get } ``` |

Modified kRogerBeepParam_InGateThresholdTime

|  | Declaration |
| --- | --- |
| From | ``` var kRogerBeepParam_InGateThresholdTime: Int { get } ``` |
| To | ``` var kRogerBeepParam_InGateThresholdTime: AudioUnitParameterID { get } ``` |

Modified kRogerBeepParam_OutGateThreshold

|  | Declaration |
| --- | --- |
| From | ``` var kRogerBeepParam_OutGateThreshold: Int { get } ``` |
| To | ``` var kRogerBeepParam_OutGateThreshold: AudioUnitParameterID { get } ``` |

Modified kRogerBeepParam_OutGateThresholdTime

|  | Declaration |
| --- | --- |
| From | ``` var kRogerBeepParam_OutGateThresholdTime: Int { get } ``` |
| To | ``` var kRogerBeepParam_OutGateThresholdTime: AudioUnitParameterID { get } ``` |

Modified kRogerBeepParam_RogerGain

|  | Declaration |
| --- | --- |
| From | ``` var kRogerBeepParam_RogerGain: Int { get } ``` |
| To | ``` var kRogerBeepParam_RogerGain: AudioUnitParameterID { get } ``` |

Modified kRogerBeepParam_RogerType

|  | Declaration |
| --- | --- |
| From | ``` var kRogerBeepParam_RogerType: Int { get } ``` |
| To | ``` var kRogerBeepParam_RogerType: AudioUnitParameterID { get } ``` |

Modified kRogerBeepParam_Sensitivity

|  | Declaration |
| --- | --- |
| From | ``` var kRogerBeepParam_Sensitivity: Int { get } ``` |
| To | ``` var kRogerBeepParam_Sensitivity: AudioUnitParameterID { get } ``` |

Modified kRoundTripAACParam_BitRate

|  | Declaration |
| --- | --- |
| From | ``` var kRoundTripAACParam_BitRate: Int { get } ``` |
| To | ``` var kRoundTripAACParam_BitRate: AudioUnitParameterID { get } ``` |

Modified kRoundTripAACParam_CompressedFormatSampleRate

|  | Declaration |
| --- | --- |
| From | ``` var kRoundTripAACParam_CompressedFormatSampleRate: Int { get } ``` |
| To | ``` var kRoundTripAACParam_CompressedFormatSampleRate: AudioUnitParameterID { get } ``` |

Modified kRoundTripAACParam_EncodingStrategy

|  | Declaration |
| --- | --- |
| From | ``` var kRoundTripAACParam_EncodingStrategy: Int { get } ``` |
| To | ``` var kRoundTripAACParam_EncodingStrategy: AudioUnitParameterID { get } ``` |

Modified kRoundTripAACParam_Format

|  | Declaration |
| --- | --- |
| From | ``` var kRoundTripAACParam_Format: Int { get } ``` |
| To | ``` var kRoundTripAACParam_Format: AudioUnitParameterID { get } ``` |

Modified kRoundTripAACParam_Quality

|  | Declaration |
| --- | --- |
| From | ``` var kRoundTripAACParam_Quality: Int { get } ``` |
| To | ``` var kRoundTripAACParam_Quality: AudioUnitParameterID { get } ``` |

Modified kRoundTripAACParam_RateOrQuality

|  | Declaration |
| --- | --- |
| From | ``` var kRoundTripAACParam_RateOrQuality: Int { get } ``` |
| To | ``` var kRoundTripAACParam_RateOrQuality: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_Azimuth

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_Azimuth: Int { get } ``` |
| To | ``` var kSpatialMixerParam_Azimuth: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_Distance

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_Distance: Int { get } ``` |
| To | ``` var kSpatialMixerParam_Distance: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_Elevation

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_Elevation: Int { get } ``` |
| To | ``` var kSpatialMixerParam_Elevation: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_Enable

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_Enable: Int { get } ``` |
| To | ``` var kSpatialMixerParam_Enable: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_Gain

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_Gain: Int { get } ``` |
| To | ``` var kSpatialMixerParam_Gain: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_GlobalReverbGain

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_GlobalReverbGain: Int { get } ``` |
| To | ``` var kSpatialMixerParam_GlobalReverbGain: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_MaxGain

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_MaxGain: Int { get } ``` |
| To | ``` var kSpatialMixerParam_MaxGain: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_MinGain

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_MinGain: Int { get } ``` |
| To | ``` var kSpatialMixerParam_MinGain: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_ObstructionAttenuation

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_ObstructionAttenuation: Int { get } ``` |
| To | ``` var kSpatialMixerParam_ObstructionAttenuation: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_OcclusionAttenuation

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_OcclusionAttenuation: Int { get } ``` |
| To | ``` var kSpatialMixerParam_OcclusionAttenuation: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_PlaybackRate

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_PlaybackRate: Int { get } ``` |
| To | ``` var kSpatialMixerParam_PlaybackRate: AudioUnitParameterID { get } ``` |

Modified kSpatialMixerParam_ReverbBlend

|  | Declaration |
| --- | --- |
| From | ``` var kSpatialMixerParam_ReverbBlend: Int { get } ``` |
| To | ``` var kSpatialMixerParam_ReverbBlend: AudioUnitParameterID { get } ``` |

Modified kStereoMixerParam_Pan

|  | Declaration |
| --- | --- |
| From | ``` var kStereoMixerParam_Pan: Int { get } ``` |
| To | ``` var kStereoMixerParam_Pan: AudioUnitParameterID { get } ``` |

Modified kStereoMixerParam_PostAveragePower

|  | Declaration |
| --- | --- |
| From | ``` var kStereoMixerParam_PostAveragePower: Int { get } ``` |
| To | ``` var kStereoMixerParam_PostAveragePower: AudioUnitParameterID { get } ``` |

Modified kStereoMixerParam_PostPeakHoldLevel

|  | Declaration |
| --- | --- |
| From | ``` var kStereoMixerParam_PostPeakHoldLevel: Int { get } ``` |
| To | ``` var kStereoMixerParam_PostPeakHoldLevel: AudioUnitParameterID { get } ``` |

Modified kStereoMixerParam_PreAveragePower

|  | Declaration |
| --- | --- |
| From | ``` var kStereoMixerParam_PreAveragePower: Int { get } ``` |
| To | ``` var kStereoMixerParam_PreAveragePower: AudioUnitParameterID { get } ``` |

Modified kStereoMixerParam_PrePeakHoldLevel

|  | Declaration |
| --- | --- |
| From | ``` var kStereoMixerParam_PrePeakHoldLevel: Int { get } ``` |
| To | ``` var kStereoMixerParam_PrePeakHoldLevel: AudioUnitParameterID { get } ``` |

Modified kStereoMixerParam_Volume

|  | Declaration |
| --- | --- |
| From | ``` var kStereoMixerParam_Volume: Int { get } ``` |
| To | ``` var kStereoMixerParam_Volume: AudioUnitParameterID { get } ``` |

Modified kTimePitchParam_EffectBlend

|  | Declaration |
| --- | --- |
| From | ``` var kTimePitchParam_EffectBlend: Int { get } ``` |
| To | ``` var kTimePitchParam_EffectBlend: AudioUnitParameterID { get } ``` |

Modified kTimePitchParam_Pitch

|  | Declaration |
| --- | --- |
| From | ``` var kTimePitchParam_Pitch: Int { get } ``` |
| To | ``` var kTimePitchParam_Pitch: AudioUnitParameterID { get } ``` |

Modified kTimePitchParam_Rate

|  | Declaration |
| --- | --- |
| From | ``` var kTimePitchParam_Rate: Int { get } ``` |
| To | ``` var kTimePitchParam_Rate: AudioUnitParameterID { get } ``` |

Modified kVarispeedParam_PlaybackCents

|  | Declaration |
| --- | --- |
| From | ``` var kVarispeedParam_PlaybackCents: Int { get } ``` |
| To | ``` var kVarispeedParam_PlaybackCents: AudioUnitParameterID { get } ``` |

Modified kVarispeedParam_PlaybackRate

|  | Declaration |
| --- | --- |
| From | ``` var kVarispeedParam_PlaybackRate: Int { get } ``` |
| To | ``` var kVarispeedParam_PlaybackRate: AudioUnitParameterID { get } ``` |

Modified [MagicCookieInfo](https://developer.apple.com/documentation/audiotoolbox/magiccookieinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [MusicDeviceMIDIEventProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicemidieventproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicDeviceMIDIEventProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> OSStatus)> ``` |
| To | ``` typealias MusicDeviceMIDIEventProc = (UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> OSStatus ``` |

Modified [MusicDeviceStartNoteProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicestartnoteproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicDeviceStartNoteProc = CFunctionPointer<((UnsafeMutablePointer<Void>, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus)> ``` |
| To | ``` typealias MusicDeviceStartNoteProc = (UnsafeMutablePointer<Void>, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus ``` |

Modified [MusicDeviceStopNoteProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicestopnoteproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicDeviceStopNoteProc = CFunctionPointer<((UnsafeMutablePointer<Void>, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus)> ``` |
| To | ``` typealias MusicDeviceStopNoteProc = (UnsafeMutablePointer<Void>, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus ``` |

Modified [MusicDeviceSysExProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicesysexproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicDeviceSysExProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias MusicDeviceSysExProc = (UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> OSStatus ``` |

Modified [ScheduledAudioFileRegionCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregioncompletionproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias ScheduledAudioFileRegionCompletionProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<ScheduledAudioFileRegion>, OSStatus) -> Void)> ``` |
| To | ``` typealias ScheduledAudioFileRegionCompletionProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<ScheduledAudioFileRegion>, OSStatus) -> Void ``` |

Modified [ScheduledAudioSliceCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslicecompletionproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias ScheduledAudioSliceCompletionProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<ScheduledAudioSlice>) -> Void)> ``` |
| To | ``` typealias ScheduledAudioSliceCompletionProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<ScheduledAudioSlice>) -> Void ``` |

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
