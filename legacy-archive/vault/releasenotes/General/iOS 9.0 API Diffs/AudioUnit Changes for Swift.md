---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/AudioUnit.html
archived_at: '2026-07-18T02:56:41.165363Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AudioUnit Changes for Swift

### AudioUnit

Removed AudioComponentPlugInInterface.init()Removed AudioComponentPlugInInterface.init(Open: CFunctionPointer<((UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus)>, Close: CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)>, Lookup: CFunctionPointer<((Int16) -> AudioComponentMethod)>, reserved: UnsafeMutablePointer<Void>)Removed AudioOutputUnitMIDICallbacks.init()Removed AudioOutputUnitMIDICallbacks.init(userData: UnsafeMutablePointer<Void>, MIDIEventProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void)>, MIDISysExProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void)>)Removed AudioUnitConnection.init()Removed AudioUnitConnection.init(sourceAudioUnit: AudioUnit, sourceOutputNumber: UInt32, destInputNumber: UInt32)Removed AudioUnitExternalBuffer.init()Removed AudioUnitExternalBuffer.init(buffer: UnsafeMutablePointer<UInt8>, size: UInt32)Removed AudioUnitMeterClipping.init(peakValueSinceLastCall: Float32, sawInfinity: Boolean, sawNotANumber: Boolean)Removed AudioUnitParameter.init()Removed AudioUnitParameter.init(mAudioUnit: AudioUnit, mParameterID: AudioUnitParameterID, mScope: AudioUnitScope, mElement: AudioUnitElement)Removed AudioUnitParameterInfo.init(name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName: Unmanaged<CFString>!, clumpID: UInt32, cfNameString: Unmanaged<CFString>!, unit: AudioUnitParameterUnit, minValue: AudioUnitParameterValue, maxValue: AudioUnitParameterValue, defaultValue: AudioUnitParameterValue, flags: UInt32)Removed AudioUnitParameterNameInfo.init(inID: AudioUnitParameterID, inDesiredLength: Int32, outName: Unmanaged<CFString>!)Removed AudioUnitParameterStringFromValue.init()Removed AudioUnitParameterStringFromValue.init(inParamID: AudioUnitParameterID, inValue: UnsafePointer<AudioUnitParameterValue>, outString: Unmanaged<CFString>!)Removed AudioUnitParameterValueFromString.init()Removed AudioUnitParameterValueFromString.init(inParamID: AudioUnitParameterID, inString: Unmanaged<CFString>!, outValue: AudioUnitParameterValue)Removed AudioUnitProperty.init()Removed AudioUnitProperty.init(mAudioUnit: AudioUnit, mPropertyID: AudioUnitPropertyID, mScope: AudioUnitScope, mElement: AudioUnitElement)Removed AUInputSamplesInOutputCallbackStruct.init()Removed AUInputSamplesInOutputCallbackStruct.init(inputToOutputCallback: AUInputSamplesInOutputCallback, userData: UnsafeMutablePointer<Void>)Removed AUPreset.init()Removed AUPreset.init(presetNumber: Int32, presetName: Unmanaged<CFString>!)Removed AURenderCallbackStruct.init()Removed AURenderCallbackStruct.init(inputProc: AURenderCallback, inputProcRefCon: UnsafeMutablePointer<Void>)Removed AUSamplerBankPresetData.init()Removed AUSamplerBankPresetData.init(bankURL: Unmanaged<CFURL>!, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8, reserved: UInt8)Removed AUSamplerInstrumentData.init()Removed AUSamplerInstrumentData.init(fileURL: Unmanaged<CFURL>!, instrumentType: UInt8, bankMSB: UInt8, bankLSB: UInt8, presetID: UInt8)Removed HostCallbackInfo.init(hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc: HostCallback_GetBeatAndTempo, musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation, transportStateProc: HostCallback_GetTransportState, transportStateProc2: HostCallback_GetTransportState2)Removed ScheduledAudioFileRegion.init()Removed ScheduledAudioSlice.init()Removed ScheduledAudioSlice.init(mTimeStamp: AudioTimeStamp, mCompletionProc: ScheduledAudioSliceCompletionProc, mCompletionProcUserData: UnsafeMutablePointer<Void>, mFlags: UInt32, mReserved: UInt32, mReserved2: UnsafeMutablePointer<Void>, mNumberFrames: UInt32, mBufferList: UnsafeMutablePointer<AudioBufferList>)Removed AudioUnitParameterUnitRemoved AudioUnitRemoteControlEventRemoved AudioUnitRenderActionFlagsRemoved AUParameterEventTypeRemoved k3DMixerAttenuationCurve_ExponentialRemoved k3DMixerAttenuationCurve_InverseRemoved k3DMixerAttenuationCurve_LinearRemoved k3DMixerAttenuationCurve_PowerRemoved k3DMixerRenderingFlags_ConstantReverbBlendRemoved k3DMixerRenderingFlags_DistanceAttenuationRemoved k3DMixerRenderingFlags_DistanceDiffusionRemoved k3DMixerRenderingFlags_DistanceFilterRemoved k3DMixerRenderingFlags_DopplerShiftRemoved k3DMixerRenderingFlags_InterAuralDelayRemoved k3DMixerRenderingFlags_LinearDistanceAttenuationRemoved kAudioComponentFlag_SandboxSafeRemoved kAudioComponentFlag_UnsearchableRemoved kAudioOfflineUnitRenderAction_CompleteRemoved kAudioOfflineUnitRenderAction_PreflightRemoved kAudioOfflineUnitRenderAction_RenderRemoved kAudioUnitParameterFlag_CanRampRemoved kAudioUnitParameterFlag_CFNameReleaseRemoved kAudioUnitParameterFlag_DisplayCubedRemoved kAudioUnitParameterFlag_DisplayCubeRootRemoved kAudioUnitParameterFlag_DisplayExponentialRemoved kAudioUnitParameterFlag_DisplayLogarithmicRemoved kAudioUnitParameterFlag_DisplayMaskRemoved kAudioUnitParameterFlag_DisplaySquaredRemoved kAudioUnitParameterFlag_DisplaySquareRootRemoved kAudioUnitParameterFlag_ExpertModeRemoved kAudioUnitParameterFlag_HasCFNameStringRemoved kAudioUnitParameterFlag_HasClumpRemoved kAudioUnitParameterFlag_IsElementMetaRemoved kAudioUnitParameterFlag_IsGlobalMetaRemoved kAudioUnitParameterFlag_IsHighResolutionRemoved kAudioUnitParameterFlag_IsReadableRemoved kAudioUnitParameterFlag_IsWritableRemoved kAudioUnitParameterFlag_MeterReadOnlyRemoved kAudioUnitParameterFlag_NonRealTimeRemoved kAudioUnitParameterFlag_OmitFromPresetsRemoved kAudioUnitParameterFlag_PlotHistoryRemoved kAudioUnitParameterFlag_ValuesHaveStringsRemoved kAudioUnitParameterUnit_AbsoluteCentsRemoved kAudioUnitParameterUnit_BeatsRemoved kAudioUnitParameterUnit_BooleanRemoved kAudioUnitParameterUnit_BPMRemoved kAudioUnitParameterUnit_CentsRemoved kAudioUnitParameterUnit_CustomUnitRemoved kAudioUnitParameterUnit_DecibelsRemoved kAudioUnitParameterUnit_DegreesRemoved kAudioUnitParameterUnit_EqualPowerCrossfadeRemoved kAudioUnitParameterUnit_GenericRemoved kAudioUnitParameterUnit_HertzRemoved kAudioUnitParameterUnit_IndexedRemoved kAudioUnitParameterUnit_LinearGainRemoved kAudioUnitParameterUnit_MetersRemoved kAudioUnitParameterUnit_MIDIControllerRemoved kAudioUnitParameterUnit_MIDINoteNumberRemoved kAudioUnitParameterUnit_MillisecondsRemoved kAudioUnitParameterUnit_MixerFaderCurve1Removed kAudioUnitParameterUnit_OctavesRemoved kAudioUnitParameterUnit_PanRemoved kAudioUnitParameterUnit_PercentRemoved kAudioUnitParameterUnit_PhaseRemoved kAudioUnitParameterUnit_RateRemoved kAudioUnitParameterUnit_RatioRemoved kAudioUnitParameterUnit_RelativeSemiTonesRemoved kAudioUnitParameterUnit_SampleFramesRemoved kAudioUnitParameterUnit_SecondsRemoved kAudioUnitRemoteControlEvent_RewindRemoved kAudioUnitRemoteControlEvent_TogglePlayPauseRemoved kAudioUnitRemoteControlEvent_ToggleRecordRemoved kAudioUnitRenderAction_DoNotCheckRenderArgsRemoved kAudioUnitRenderAction_OutputIsSilenceRemoved kAudioUnitRenderAction_PostRenderRemoved kAudioUnitRenderAction_PostRenderErrorRemoved kAudioUnitRenderAction_PreRenderRemoved kParameterEvent_ImmediateRemoved kParameterEvent_RampedRemoved kReverbRoomType_CathedralRemoved kReverbRoomType_LargeChamberRemoved kReverbRoomType_LargeHallRemoved kReverbRoomType_LargeHall2Removed kReverbRoomType_LargeRoomRemoved kReverbRoomType_LargeRoom2Removed kReverbRoomType_MediumChamberRemoved kReverbRoomType_MediumHallRemoved kReverbRoomType_MediumHall2Removed kReverbRoomType_MediumHall3Removed kReverbRoomType_MediumRoomRemoved kReverbRoomType_PlateRemoved kReverbRoomType_SmallRoomRemoved kScheduledAudioSliceFlag_BeganToRenderRemoved kScheduledAudioSliceFlag_BeganToRenderLateRemoved kScheduledAudioSliceFlag_CompleteRemoved kScheduledAudioSliceFlag_InterruptRemoved kScheduledAudioSliceFlag_InterruptAtLoopRemoved kScheduledAudioSliceFlag_LoopRemoved kSpatializationAlgorithm_EqualPowerPanningRemoved kSpatializationAlgorithm_HRTFRemoved kSpatializationAlgorithm_SoundFieldRemoved kSpatializationAlgorithm_SphericalHeadRemoved kSpatializationAlgorithm_StereoPassThroughRemoved kSpatializationAlgorithm_VectorBasedPanningRemoved kSpatialMixerAttenuationCurve_ExponentialRemoved kSpatialMixerAttenuationCurve_InverseRemoved kSpatialMixerAttenuationCurve_LinearRemoved kSpatialMixerAttenuationCurve_PowerRemoved kSpatialMixerRenderingFlags_DistanceAttenuationRemoved kSpatialMixerRenderingFlags_InterAuralDelayAdded [AU3DMixerAttenuationCurve [enum]](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve)Added [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Exponential](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_exponential)Added [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Inverse](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_inverse)Added [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Linear](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_linear)Added [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Power](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_power)Added [AU3DMixerRenderingFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags)Added AU3DMixerRenderingFlags.init(rawValue: UInt32)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_ConstantReverbBlend](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_constantreverbblend)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_distanceattenuation)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceDiffusion](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/1439784-k3dmixerrenderingflags_distanced)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceFilter](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/1440885-k3dmixerrenderingflags_distancef)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DopplerShift](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_dopplershift)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_InterAuralDelay](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_interauraldelay)Added [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_LinearDistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_lineardistanceattenuation)Added [AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounit)Added [AUAudioUnit.allocateRenderResources() throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387620-allocaterenderresources)Added [AUAudioUnit.allParameterValues](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387679-allparametervalues)Added [AUAudioUnit.audioUnitName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387640-audiounitname)Added [AUAudioUnit.canPerformInput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387551-canperforminput)Added [AUAudioUnit.canPerformOutput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387656-canperformoutput)Added [AUAudioUnit.canProcessInPlace](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387583-canprocessinplace)Added [AUAudioUnit.channelCapabilities](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387685-channelcapabilities)Added [AUAudioUnit.component](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387535-component)Added [AUAudioUnit.componentDescription](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387568-componentdescription)Added [AUAudioUnit.componentName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387566-componentname)Added [AUAudioUnit.componentVersion](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387555-componentversion)Added [AUAudioUnit.contextName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387553-contextname)Added [AUAudioUnit.currentPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387668-currentpreset)Added [AUAudioUnit.deallocateRenderResources()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387612-deallocaterenderresources)Added [AUAudioUnit.factoryPresets](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387526-factorypresets)Added [AUAudioUnit.fullState](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387500-fullstate)Added [AUAudioUnit.fullStateForDocument](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387630-fullstatefordocument)Added [AUAudioUnit.init(componentDescription: AudioComponentDescription) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387570-init)Added [AUAudioUnit.init(componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387664-initwithcomponentdescription)Added [AUAudioUnit.inputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387636-inputbusses)Added [AUAudioUnit.inputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387660-inputenabled)Added [AUAudioUnit.inputHandler](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387616-inputhandler)Added [AUAudioUnit.instantiateWithComponentDescription(_: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AUAudioUnit?, NSError?) -> Void) [class]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387606-instantiate)Added [AUAudioUnit.internalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439864-internalrenderblock)Added [AUAudioUnit.latency](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387675-latency)Added [AUAudioUnit.manufacturerName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387681-manufacturername)Added [AUAudioUnit.maximumFramesToRender](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387654-maximumframestorender)Added [AUAudioUnit.musicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387669-musicalcontextblock)Added [AUAudioUnit.musicDeviceOrEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387497-ismusicdeviceoreffect)Added [AUAudioUnit.outputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387503-outputbusses)Added [AUAudioUnit.outputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387646-outputenabled)Added [AUAudioUnit.outputProvider](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387596-outputprovider)Added [AUAudioUnit.parametersForOverviewWithCount(_: Int) -> [NSNumber]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387549-parametersforoverview)Added [AUAudioUnit.parameterTree](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387650-parametertree)Added [AUAudioUnit.registerSubclass(_: AnyClass, asComponentDescription: AudioComponentDescription, name: String, version: UInt32) [class]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1438315-registersubclass)Added [AUAudioUnit.removeRenderObserver(_: Int)](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387564-removerenderobserver)Added [AUAudioUnit.renderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387687-renderblock)Added [AUAudioUnit.renderingOffline](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387578-renderingoffline)Added [AUAudioUnit.renderQuality](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387648-renderquality)Added [AUAudioUnit.renderResourcesAllocated](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387618-renderresourcesallocated)Added [AUAudioUnit.reset()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387658-reset)Added [AUAudioUnit.scheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387576-schedulemidieventblock)Added [AUAudioUnit.scheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387677-scheduleparameterblock)Added [AUAudioUnit.setRenderResourcesAllocated(_: Bool)](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1440830-setrenderresourcesallocated)Added [AUAudioUnit.shouldBypassEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387545-shouldbypasseffect)Added [AUAudioUnit.shouldChangeToFormat(_: AVAudioFormat, forBus: AUAudioUnitBus) -> Bool](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439999-shouldchange)Added [AUAudioUnit.startHardware() throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387581-starthardware)Added [AUAudioUnit.stopHardware()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387642-stophardware)Added [AUAudioUnit.tailTime](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387614-tailtime)Added [AUAudioUnit.tokenByAddingRenderObserver(_: AURenderObserver) -> Int](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387509-token)Added [AUAudioUnit.transportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387559-transportstateblock)Added [AUAudioUnit.virtualMIDICableCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387666-virtualmidicablecount)Added [AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus)Added [AUAudioUnitBus.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387524-bustype)Added [AUAudioUnitBus.contextPresentationLatency](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387547-contextpresentationlatency)Added [AUAudioUnitBus.enabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387634-isenabled)Added [AUAudioUnitBus.format](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387689-format)Added [AUAudioUnitBus.index](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387557-index)Added [AUAudioUnitBus.init(format: AVAudioFormat) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440039-initwithformat)Added [AUAudioUnitBus.maximumChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1439855-maximumchannelcount)Added [AUAudioUnitBus.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387514-name)Added [AUAudioUnitBus.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387638-owneraudiounit)Added [AUAudioUnitBus.setFormat(_: AVAudioFormat) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387644-setformat)Added [AUAudioUnitBus.supportedChannelCounts](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440352-supportedchannelcounts)Added [AUAudioUnitBus.supportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387622-supportedchannellayouttags)Added [AUAudioUnitBusArray](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray)Added [AUAudioUnitBusArray.addObserverToAllBusses(_: NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387520-addobservertoallbusses)Added [AUAudioUnitBusArray.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387671-bustype)Added [AUAudioUnitBusArray.count](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387673-count)Added [AUAudioUnitBusArray.countChangeable](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387537-countchangeable)Added [AUAudioUnitBusArray.init(audioUnit: AUAudioUnit, busType: AUAudioUnitBusType)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387662-initwithaudiounit)Added [AUAudioUnitBusArray.init(audioUnit: AUAudioUnit, busType: AUAudioUnitBusType, busses: [AUAudioUnitBus])](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387516-initwithaudiounit)Added [AUAudioUnitBusArray.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387510-owneraudiounit)Added [AUAudioUnitBusArray.removeObserverFromAllBusses(_: NSObject, forKeyPath: String, context: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387505-removeobserverfromallbusses)Added [AUAudioUnitBusArray.replaceBusses(_: [AUAudioUnitBus])](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1440520-replacebusses)Added [AUAudioUnitBusArray.setBusCount(_: Int) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387598-setbuscount)Added [AUAudioUnitBusArray.subscript(_: Int) -> AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387507-subscript)Added [AUAudioUnitBusType [enum]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype)Added [AUAudioUnitBusType.Input](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/input)Added [AUAudioUnitBusType.Output](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/output)Added [AUAudioUnitFactory](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory)Added [AUAudioUnitFactory.createAudioUnitWithComponentDescription(_: AudioComponentDescription) throws -> AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory/1440321-createaudiounitwithcomponentdesc)Added [AUAudioUnitPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset)Added [AUAudioUnitPreset.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387587-name)Added [AUAudioUnitPreset.number](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387626-number)Added [AUAudioUnitV2Bridge](https://developer.apple.com/documentation/audiotoolbox/auaudiounitv2bridge)Added [AudioComponentFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags)Added [AudioComponentFlags.CanLoadInProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/1410506-canloadinprocess)Added AudioComponentFlags.init(rawValue: UInt32)Added [AudioComponentFlags.IsV3AudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_isv3audiounit)Added [AudioComponentFlags.RequiresAsyncInstantiation](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_requiresasyncinstantiation)Added [AudioComponentFlags.SandboxSafe](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_sandboxsafe)Added [AudioComponentFlags.Unsearchable](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_unsearchable)Added [AudioComponentInstantiationOptions [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions)Added AudioComponentInstantiationOptions.init(rawValue: UInt32)Added [AudioComponentInstantiationOptions.LoadOutOfProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions/kaudiocomponentinstantiation_loadoutofprocess)Added [AudioComponentValidationResult [enum]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult)Added [AudioComponentValidationResult.Failed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/failed)Added [AudioComponentValidationResult.Passed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_passed)Added [AudioComponentValidationResult.TimedOut](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/timedout)Added [AudioComponentValidationResult.UnauthorizedError_Init](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_unauthorizederror_init)Added [AudioComponentValidationResult.UnauthorizedError_Open](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/unauthorizederror_open)Added [AudioComponentValidationResult.Unknown](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/unknown)Added AudioUnitMeterClipping.init(peakValueSinceLastCall: Float32, sawInfinity: DarwinBoolean, sawNotANumber: DarwinBoolean)Added AudioUnitParameterInfo.init(name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName: Unmanaged<CFString>?, clumpID: UInt32, cfNameString: Unmanaged<CFString>?, unit: AudioUnitParameterUnit, minValue: AudioUnitParameterValue, maxValue: AudioUnitParameterValue, defaultValue: AudioUnitParameterValue, flags: AudioUnitParameterOptions)Added AudioUnitParameterNameInfo.init(inID: AudioUnitParameterID, inDesiredLength: Int32, outName: Unmanaged<CFString>?)Added [AudioUnitParameterOptions [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions)Added [AudioUnitParameterOptions.Flag_CanRamp](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_canramp)Added [AudioUnitParameterOptions.Flag_CFNameRelease](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439788-flag_cfnamerelease)Added [AudioUnitParameterOptions.Flag_DisplayCubed](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439330-flag_displaycubed)Added [AudioUnitParameterOptions.Flag_DisplayCubeRoot](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440958-flag_displaycuberoot)Added [AudioUnitParameterOptions.Flag_DisplayExponential](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displayexponential)Added [AudioUnitParameterOptions.Flag_DisplayLogarithmic](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displaylogarithmic)Added [AudioUnitParameterOptions.Flag_DisplayMask](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displaymask)Added [AudioUnitParameterOptions.Flag_DisplaySquared](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440750-flag_displaysquared)Added [AudioUnitParameterOptions.Flag_DisplaySquareRoot](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1441018-flag_displaysquareroot)Added [AudioUnitParameterOptions.Flag_ExpertMode](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_expertmode)Added [AudioUnitParameterOptions.Flag_HasCFNameString](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_hascfnamestring)Added [AudioUnitParameterOptions.Flag_HasClump](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_hasclump)Added [AudioUnitParameterOptions.Flag_IsElementMeta](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439961-flag_iselementmeta)Added [AudioUnitParameterOptions.Flag_IsGlobalMeta](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_isglobalmeta)Added [AudioUnitParameterOptions.Flag_IsHighResolution](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_ishighresolution)Added [AudioUnitParameterOptions.Flag_IsReadable](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1438604-flag_isreadable)Added [AudioUnitParameterOptions.Flag_IsWritable](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440477-flag_iswritable)Added [AudioUnitParameterOptions.Flag_MeterReadOnly](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439379-flag_meterreadonly)Added [AudioUnitParameterOptions.Flag_NonRealTime](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_nonrealtime)Added [AudioUnitParameterOptions.Flag_OmitFromPresets](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_omitfrompresets)Added [AudioUnitParameterOptions.Flag_PlotHistory](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_plothistory)Added [AudioUnitParameterOptions.Flag_ValuesHaveStrings](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440179-flag_valueshavestrings)Added AudioUnitParameterOptions.init(rawValue: UInt32)Added [AudioUnitParameterUnit [enum]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit)Added [AudioUnitParameterUnit.AbsoluteCents](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_absolutecents)Added [AudioUnitParameterUnit.Beats](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/beats)Added [AudioUnitParameterUnit.Boolean](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_boolean)Added [AudioUnitParameterUnit.BPM](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_bpm)Added [AudioUnitParameterUnit.Cents](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_cents)Added [AudioUnitParameterUnit.CustomUnit](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/customunit)Added [AudioUnitParameterUnit.Decibels](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_decibels)Added [AudioUnitParameterUnit.Degrees](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_degrees)Added [AudioUnitParameterUnit.EqualPowerCrossfade](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_equalpowercrossfade)Added [AudioUnitParameterUnit.Generic](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/generic)Added [AudioUnitParameterUnit.Hertz](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/hertz)Added [AudioUnitParameterUnit.Indexed](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/indexed)Added [AudioUnitParameterUnit.LinearGain](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_lineargain)Added [AudioUnitParameterUnit.Meters](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/meters)Added [AudioUnitParameterUnit.MIDIController](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/midicontroller)Added [AudioUnitParameterUnit.MIDINoteNumber](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/midinotenumber)Added [AudioUnitParameterUnit.Milliseconds](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/milliseconds)Added [AudioUnitParameterUnit.MixerFaderCurve1](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/mixerfadercurve1)Added [AudioUnitParameterUnit.Octaves](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_octaves)Added [AudioUnitParameterUnit.Pan](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_pan)Added [AudioUnitParameterUnit.Percent](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_percent)Added [AudioUnitParameterUnit.Phase](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_phase)Added [AudioUnitParameterUnit.Rate](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_rate)Added [AudioUnitParameterUnit.Ratio](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/ratio)Added [AudioUnitParameterUnit.RelativeSemiTones](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_relativesemitones)Added [AudioUnitParameterUnit.SampleFrames](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_sampleframes)Added [AudioUnitParameterUnit.Seconds](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_seconds)Added [AudioUnitRemoteControlEvent [enum]](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent)Added [AudioUnitRemoteControlEvent.Rewind](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/kaudiounitremotecontrolevent_rewind)Added [AudioUnitRemoteControlEvent.TogglePlayPause](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/toggleplaypause)Added [AudioUnitRemoteControlEvent.ToggleRecord](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/togglerecord)Added [AudioUnitRenderActionFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags)Added AudioUnitRenderActionFlags.init(rawValue: UInt32)Added [AudioUnitRenderActionFlags.OfflineUnitRenderAction_Complete](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudioofflineunitrenderaction_complete)Added [AudioUnitRenderActionFlags.OfflineUnitRenderAction_Preflight](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudioofflineunitrenderaction_preflight)Added [AudioUnitRenderActionFlags.OfflineUnitRenderAction_Render](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1439632-offlineunitrenderaction_render)Added [AudioUnitRenderActionFlags.UnitRenderAction_DoNotCheckRenderArgs](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_donotcheckrenderargs)Added [AudioUnitRenderActionFlags.UnitRenderAction_OutputIsSilence](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_outputissilence)Added [AudioUnitRenderActionFlags.UnitRenderAction_PostRender](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1440615-unitrenderaction_postrender)Added [AudioUnitRenderActionFlags.UnitRenderAction_PostRenderError](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_postrendererror)Added [AudioUnitRenderActionFlags.UnitRenderAction_PreRender](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1440530-unitrenderaction_prerender)Added [AUHostTransportStateFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags)Added [AUHostTransportStateFlags.Changed](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387572-changed)Added [AUHostTransportStateFlags.Cycling](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstatecycling)Added AUHostTransportStateFlags.init(rawValue: UInt)Added [AUHostTransportStateFlags.Moving](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387579-moving)Added [AUHostTransportStateFlags.Recording](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387591-recording)Added [AUMIDIEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aumidievent)Added [AUMIDIEvent.cable](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439751-cable)Added [AUMIDIEvent.data](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1438814-data)Added [AUMIDIEvent.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440373-eventsampletime)Added [AUMIDIEvent.eventType](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440184-eventtype)Added AUMIDIEvent.init()Added AUMIDIEvent.init(next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8, length: UInt16, cable: UInt8, data: (UInt8, UInt8, UInt8))Added [AUMIDIEvent.length](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439101-length)Added [AUMIDIEvent.next](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439283-next)Added [AUMIDIEvent.reserved](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440361-reserved)Added [AUParameter](https://developer.apple.com/documentation/audiotoolbox/auparameter)Added [AUParameter.address](https://developer.apple.com/documentation/audiotoolbox/auparameter/1441037-address)Added [AUParameter.dependentParameters](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440649-dependentparameters)Added [AUParameter.flags](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439938-flags)Added [AUParameter.maxValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438427-maxvalue)Added [AUParameter.minValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440270-minvalue)Added [AUParameter.setValue(_: AUValue, originator: AUParameterObserverToken)](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439968-setvalue)Added [AUParameter.setValue(_: AUValue, originator: AUParameterObserverToken, atHostTime: UInt64)](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438450-setvalue)Added [AUParameter.stringFromValue(_: UnsafePointer<AUValue>) -> String](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440901-stringfromvalue)Added [AUParameter.unit](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440698-unit)Added [AUParameter.unitName](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438490-unitname)Added [AUParameter.value](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439301-value)Added [AUParameter.valueFromString(_: String) -> AUValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440495-valuefromstring)Added [AUParameter.valueStrings](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438358-valuestrings)Added [AUParameterEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/auparameterevent)Added [AUParameterEvent.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440912-eventsampletime)Added [AUParameterEvent.eventType](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1438332-eventtype)Added AUParameterEvent.init()Added AUParameterEvent.init(next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: (UInt8, UInt8, UInt8), rampDurationSampleFrames: AUAudioFrameCount, parameterAddress: AUParameterAddress, value: AUValue)Added [AUParameterEvent.next](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440983-next)Added [AUParameterEvent.parameterAddress](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440605-parameteraddress)Added [AUParameterEvent.rampDurationSampleFrames](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1439037-rampdurationsampleframes)Added [AUParameterEvent.reserved](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1439165-reserved)Added [AUParameterEvent.value](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440528-value)Added [AUParameterEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype)Added [AUParameterEventType.ParameterEvent_Immediate](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype/parameterevent_immediate)Added [AUParameterEventType.ParameterEvent_Ramped](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype/kparameterevent_ramped)Added [AUParameterGroup](https://developer.apple.com/documentation/audiotoolbox/auparametergroup)Added [AUParameterGroup.allParameters](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439439-allparameters)Added [AUParameterGroup.children](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439325-children)Added [AUParameterNode](https://developer.apple.com/documentation/audiotoolbox/auparameternode)Added [AUParameterNode.displayName](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440278-displayname)Added [AUParameterNode.displayNameWithLength(_: Int) -> String](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439449-displaynamewithlength)Added [AUParameterNode.identifier](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440186-identifier)Added [AUParameterNode.implementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439427-implementordisplaynamewithlength)Added [AUParameterNode.implementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440045-implementorstringfromvaluecallba)Added [AUParameterNode.implementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439270-implementorvaluefromstringcallba)Added [AUParameterNode.implementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439658-implementorvalueobserver)Added [AUParameterNode.implementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439942-implementorvalueprovider)Added [AUParameterNode.keyPath](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439420-keypath)Added [AUParameterNode.removeParameterObserver(_: AUParameterObserverToken)](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439314-removeparameterobserver)Added [AUParameterNode.tokenByAddingParameterObserver(_: AUParameterObserver) -> AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440811-token)Added [AUParameterNode.tokenByAddingParameterRecordingObserver(_: AUParameterRecordingObserver) -> AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440903-tokenbyaddingparameterrecordingo)Added [AUParameterTree](https://developer.apple.com/documentation/audiotoolbox/auparametertree)Added [AUParameterTree.createGroupFromTemplate(_: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439822-creategroupfromtemplate)Added [AUParameterTree.createGroupTemplate(_: [AUParameterNode]) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439912-creategrouptemplate)Added [AUParameterTree.createGroupWithIdentifier(_: String, name: String, children: [AUParameterNode]) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439002-creategroupwithidentifier)Added [AUParameterTree.createParameterWithIdentifier(_: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1440598-createparameter)Added [AUParameterTree.createTreeWithChildren(_: [AUParameterNode]) -> AUParameterTree [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438522-createtree)Added [AUParameterTree.parameterWithAddress(_: AUParameterAddress) -> AUParameter?](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439569-parameter)Added [AUParameterTree.parameterWithID(_: AudioUnitParameterID, scope: AudioUnitScope, element: AudioUnitElement) -> AUParameter?](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438918-parameter)Added [AURecordedParameterEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent)Added [AURecordedParameterEvent.address](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1438335-address)Added [AURecordedParameterEvent.hostTime](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1440955-hosttime)Added AURecordedParameterEvent.init()Added AURecordedParameterEvent.init(hostTime: UInt64, address: AUParameterAddress, value: AUValue)Added [AURecordedParameterEvent.value](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1440438-value)Added [AURenderEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aurenderevent)Added AURenderEvent.init()Added [AURenderEventHeader [struct]](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader)Added [AURenderEventHeader.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440010-eventsampletime)Added [AURenderEventHeader.eventType](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440946-eventtype)Added AURenderEventHeader.init()Added AURenderEventHeader.init(next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8)Added [AURenderEventHeader.next](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1439936-next)Added [AURenderEventHeader.reserved](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440587-reserved)Added [AURenderEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype)Added [AURenderEventType.MIDI](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midi)Added [AURenderEventType.MIDISysEx](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midisysex)Added [AURenderEventType.Parameter](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/parameter)Added [AURenderEventType.ParameterRamp](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/parameterramp)Added [AUReverbRoomType [enum]](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype)Added [AUReverbRoomType.ReverbRoomType_Cathedral](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_cathedral)Added [AUReverbRoomType.ReverbRoomType_LargeChamber](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largechamber)Added [AUReverbRoomType.ReverbRoomType_LargeHall](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largehall)Added [AUReverbRoomType.ReverbRoomType_LargeHall2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largehall2)Added [AUReverbRoomType.ReverbRoomType_LargeRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largeroom)Added [AUReverbRoomType.ReverbRoomType_LargeRoom2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largeroom2)Added [AUReverbRoomType.ReverbRoomType_MediumChamber](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_mediumchamber)Added [AUReverbRoomType.ReverbRoomType_MediumHall](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall)Added [AUReverbRoomType.ReverbRoomType_MediumHall2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall2)Added [AUReverbRoomType.ReverbRoomType_MediumHall3](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall3)Added [AUReverbRoomType.ReverbRoomType_MediumRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumroom)Added [AUReverbRoomType.ReverbRoomType_Plate](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_plate)Added [AUReverbRoomType.ReverbRoomType_SmallRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_smallroom)Added [AUScheduledAudioSliceFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags)Added AUScheduledAudioSliceFlags.init(rawValue: UInt32)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_BeganToRender](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_begantorender)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_BeganToRenderLate](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1438581-scheduledaudiosliceflag_begantor)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_Complete](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1440491-scheduledaudiosliceflag_complete)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_Interrupt](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_interrupt)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_InterruptAtLoop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1441008-scheduledaudiosliceflag_interrup)Added [AUScheduledAudioSliceFlags.ScheduledAudioSliceFlag_Loop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_loop)Added [AUSpatializationAlgorithm [enum]](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_EqualPowerPanning](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_equalpowerpanning)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_HRTF](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/kspatializationalgorithm_hrtf)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_SoundField](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/kspatializationalgorithm_soundfield)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_SphericalHead](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_sphericalhead)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_StereoPassThrough](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_stereopassthrough)Added [AUSpatializationAlgorithm.SpatializationAlgorithm_VectorBasedPanning](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_vectorbasedpanning)Added [AUSpatialMixerAttenuationCurve [enum]](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve)Added [AUSpatialMixerAttenuationCurve.SpatialMixerAttenuationCurve_Exponential](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_exponential)Added [AUSpatialMixerAttenuationCurve.SpatialMixerAttenuationCurve_Inverse](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_inverse)Added [AUSpatialMixerAttenuationCurve.SpatialMixerAttenuationCurve_Linear](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/spatialmixerattenuationcurve_linear)Added [AUSpatialMixerAttenuationCurve.SpatialMixerAttenuationCurve_Power](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_power)Added [AUSpatialMixerRenderingFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags)Added AUSpatialMixerRenderingFlags.init(rawValue: UInt32)Added [AUSpatialMixerRenderingFlags.SpatialMixerRenderingFlags_DistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_distanceattenuation)Added [AUSpatialMixerRenderingFlags.SpatialMixerRenderingFlags_InterAuralDelay](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_interauraldelay)Added HostCallbackInfo.init(hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc: HostCallback_GetBeatAndTempo?, musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation?, transportStateProc: HostCallback_GetTransportState?, transportStateProc2: HostCallback_GetTransportState2?)Added [AUAudioChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiochannelcount)Added [AUAudioFrameCount](https://developer.apple.com/documentation/audiotoolbox/auaudioframecount)Added [AUAudioUnitStatus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitstatus)Added [AudioComponentInstantiate(_: AudioComponent, _: AudioComponentInstantiationOptions, _: (AudioComponentInstance, OSStatus) -> Void)](https://developer.apple.com/documentation/audiotoolbox/1410517-audiocomponentinstantiate)Added [AUEventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aueventsampletime)Added AUEventSampleTimeImmediateAdded [AUHostMusicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auhostmusicalcontextblock)Added [AUHostTransportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateblock)Added [AUImplementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementordisplaynamewithlengthcallback)Added [AUImplementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorstringfromvaluecallback)Added [AUImplementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorvaluefromstringcallback)Added [AUImplementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueobserver)Added [AUImplementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueprovider)Added [AUInputHandler](https://developer.apple.com/documentation/audiotoolbox/auinputhandler)Added [AUInternalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auinternalrenderblock)Added [AUParameterAddress](https://developer.apple.com/documentation/audiotoolbox/auparameteraddress)Added [AUParameterObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterobserver)Added [AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameterobservertoken)Added [AUParameterRecordingObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterrecordingobserver)Added [AURenderBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderblock)Added [AURenderObserver](https://developer.apple.com/documentation/audiotoolbox/aurenderobserver)Added [AURenderPullInputBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderpullinputblock)Added [AUScheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auschedulemidieventblock)Added [AUScheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auscheduleparameterblock)Added [AUValue](https://developer.apple.com/documentation/audiotoolbox/auvalue)Added [GetAudioUnitParameterDisplayType(_: AudioUnitParameterOptions) -> AudioUnitParameterOptions](https://developer.apple.com/documentation/audiotoolbox/1440794-getaudiounitparameterdisplaytype)Added [kAudioComponentConfigurationInfo_ValidationResult](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentconfigurationinfo_validationresult)Added [kAudioComponentInstanceInvalidationNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentinstanceinvalidationnotification)Added [kAudioComponentValidationParameter_ForceValidation](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_forcevalidation)Added [kAudioComponentValidationParameter_TimeOut](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_timeout)Added [kAudioUnitConfigurationInfo_BusCountWritable](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_buscountwritable)Added [kAudioUnitConfigurationInfo_SupportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_supportedchannellayouttags)Added kAudioUnitProperty_ClassInfoFromDocumentAdded kAudioUnitProperty_ContextNameAdded kAudioUnitProperty_ParameterClumpNameAdded kAudioUnitProperty_ParametersForOverviewAdded kAudioUnitProperty_PresentationLatencyAdded kAudioUnitProperty_RequestViewControllerAdded kAudioUnitSubType_MultiSplitterAdded [SetAudioUnitParameterDisplayType(_: AudioUnitParameterOptions, _: AudioUnitParameterOptions) -> AudioUnitParameterOptions](https://developer.apple.com/documentation/audiotoolbox/1440769-setaudiounitparameterdisplaytype)Modified [AudioComponentPlugInInterface [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface)

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

Modified [AudioOutputUnitMIDICallbacks [struct]](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioOutputUnitMIDICallbacks {     var userData: UnsafeMutablePointer<Void>     var MIDIEventProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void)>     var MIDISysExProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void)>     init()     init(userData userData: UnsafeMutablePointer<Void>, MIDIEventProc MIDIEventProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void)>, MIDISysExProc MIDISysExProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void)>) } ``` |
| To | ``` struct AudioOutputUnitMIDICallbacks {     var userData: UnsafeMutablePointer<Void>     var MIDIEventProc: (UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void     var MIDISysExProc: (UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void } ``` |

Modified [AudioOutputUnitMIDICallbacks.MIDIEventProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks/1620297-midieventproc)

|  | Declaration |
| --- | --- |
| From | ``` var MIDIEventProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void)> ``` |
| To | ``` var MIDIEventProc: (UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void ``` |

Modified [AudioOutputUnitMIDICallbacks.MIDISysExProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks/1620298-midisysexproc)

|  | Declaration |
| --- | --- |
| From | ``` var MIDISysExProc: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void)> ``` |
| To | ``` var MIDISysExProc: (UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void ``` |

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

Modified [AudioUnitProperty [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitproperty)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitProperty {     var mAudioUnit: AudioUnit     var mPropertyID: AudioUnitPropertyID     var mScope: AudioUnitScope     var mElement: AudioUnitElement     init()     init(mAudioUnit mAudioUnit: AudioUnit, mPropertyID mPropertyID: AudioUnitPropertyID, mScope mScope: AudioUnitScope, mElement mElement: AudioUnitElement) } ``` |
| To | ``` struct AudioUnitProperty {     var mAudioUnit: AudioUnit     var mPropertyID: AudioUnitPropertyID     var mScope: AudioUnitScope     var mElement: AudioUnitElement } ``` |

Modified [AUInputSamplesInOutputCallbackStruct [struct]](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallbackstruct)

|  | Declaration |
| --- | --- |
| From | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafeMutablePointer<Void>     init()     init(inputToOutputCallback inputToOutputCallback: AUInputSamplesInOutputCallback, userData userData: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafeMutablePointer<Void> } ``` |

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

Modified [AudioComponentFactoryFunction](https://developer.apple.com/documentation/audiotoolbox/audiocomponentfactoryfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioComponentFactoryFunction = CFunctionPointer<((UnsafePointer<AudioComponentDescription>) -> UnsafeMutablePointer<AudioComponentPlugInInterface>)> ``` |
| To | ``` typealias AudioComponentFactoryFunction = (UnsafePointer<AudioComponentDescription>) -> UnsafeMutablePointer<AudioComponentPlugInInterface> ``` |

Modified [AudioComponentGetIcon(_: AudioComponent, _: Float) -> UIImage?](https://developer.apple.com/documentation/audiotoolbox/1410443-audiocomponentgeticon)

|  | Declaration |
| --- | --- |
| From | ``` func AudioComponentGetIcon(_ comp: AudioComponent, _ desiredPointSize: Float) -> UIImage! ``` |
| To | ``` func AudioComponentGetIcon(_ comp: AudioComponent, _ desiredPointSize: Float) -> UIImage? ``` |

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

Modified [AudioOutputUnitGetHostIcon(_: AudioUnit, _: Float) -> UIImage?](https://developer.apple.com/documentation/audiotoolbox/1619491-audiooutputunitgethosticon)

|  | Declaration |
| --- | --- |
| From | ``` func AudioOutputUnitGetHostIcon(_ au: AudioUnit, _ desiredPointSize: Float) -> UIImage! ``` |
| To | ``` func AudioOutputUnitGetHostIcon(_ au: AudioUnit, _ desiredPointSize: Float) -> UIImage? ``` |

Modified [AudioOutputUnitPublish(_: UnsafePointer<AudioComponentDescription>, _: CFString, _: UInt32, _: AudioUnit) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1619489-audiooutputunitpublish)

|  | Declaration |
| --- | --- |
| From | ``` func AudioOutputUnitPublish(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString!, _ inVersion: UInt32, _ inOutputUnit: AudioUnit) -> OSStatus ``` |
| To | ``` func AudioOutputUnitPublish(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString, _ inVersion: UInt32, _ inOutputUnit: AudioUnit) -> OSStatus ``` |

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

Modified k3DMixerParam_Enable

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_Enable: Int { get } ``` |
| To | ``` var k3DMixerParam_Enable: AudioUnitParameterID { get } ``` |

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

Modified k3DMixerParam_ReverbBlend

|  | Declaration |
| --- | --- |
| From | ``` var k3DMixerParam_ReverbBlend: Int { get } ``` |
| To | ``` var k3DMixerParam_ReverbBlend: AudioUnitParameterID { get } ``` |

Modified kAudioComponentErr_DuplicateDescription

|  | Declaration |
| --- | --- |
| From | ``` var kAudioComponentErr_DuplicateDescription: Int { get } ``` |
| To | ``` var kAudioComponentErr_DuplicateDescription: OSStatus { get } ``` |

Modified kAudioComponentErr_InitializationTimedOut

|  | Declaration |
| --- | --- |
| From | ``` var kAudioComponentErr_InitializationTimedOut: Int { get } ``` |
| To | ``` var kAudioComponentErr_InitializationTimedOut: OSStatus { get } ``` |

Modified [kAudioComponentErr_InstanceInvalidated](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponenterr_instanceinvalidated)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioComponentErr_InstanceInvalidated: Int { get } ``` |
| To | ``` var kAudioComponentErr_InstanceInvalidated: OSStatus { get } ``` |

Modified kAudioComponentErr_InvalidFormat

|  | Declaration |
| --- | --- |
| From | ``` var kAudioComponentErr_InvalidFormat: Int { get } ``` |
| To | ``` var kAudioComponentErr_InvalidFormat: OSStatus { get } ``` |

Modified kAudioComponentErr_NotPermitted

|  | Declaration |
| --- | --- |
| From | ``` var kAudioComponentErr_NotPermitted: Int { get } ``` |
| To | ``` var kAudioComponentErr_NotPermitted: OSStatus { get } ``` |

Modified kAudioComponentErr_TooManyInstances

|  | Declaration |
| --- | --- |
| From | ``` var kAudioComponentErr_TooManyInstances: Int { get } ``` |
| To | ``` var kAudioComponentErr_TooManyInstances: OSStatus { get } ``` |

Modified kAudioComponentErr_UnsupportedType

|  | Declaration |
| --- | --- |
| From | ``` var kAudioComponentErr_UnsupportedType: Int { get } ``` |
| To | ``` var kAudioComponentErr_UnsupportedType: OSStatus { get } ``` |

Modified [kAudioComponentRegistrationsChangedNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentregistrationschangednotification)

|  | Declaration |
| --- | --- |
| From | ``` let kAudioComponentRegistrationsChangedNotification: CFString! ``` |
| To | ``` let kAudioComponentRegistrationsChangedNotification: CFString ``` |

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

Modified kAudioOutputUnitProperty_HostReceivesRemoteControlEvents

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_HostReceivesRemoteControlEvents: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_HostReceivesRemoteControlEvents: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_HostTransportState

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_HostTransportState: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_HostTransportState: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_IsRunning

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_IsRunning: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_IsRunning: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_MIDICallbacks

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_MIDICallbacks: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_MIDICallbacks: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_NodeComponentDescription

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_NodeComponentDescription: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_NodeComponentDescription: AudioUnitPropertyID { get } ``` |

Modified kAudioOutputUnitProperty_RemoteControlToHost

|  | Declaration |
| --- | --- |
| From | ``` var kAudioOutputUnitProperty_RemoteControlToHost: Int { get } ``` |
| To | ``` var kAudioOutputUnitProperty_RemoteControlToHost: AudioUnitPropertyID { get } ``` |

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

Modified kAudioUnitProperty_AudioChannelLayout

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_AudioChannelLayout: Int { get } ``` |
| To | ``` var kAudioUnitProperty_AudioChannelLayout: AudioUnitPropertyID { get } ``` |

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

Modified kAudioUnitProperty_FrequencyResponse

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_FrequencyResponse: Int { get } ``` |
| To | ``` var kAudioUnitProperty_FrequencyResponse: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_HostCallbacks

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_HostCallbacks: Int { get } ``` |
| To | ``` var kAudioUnitProperty_HostCallbacks: AudioUnitPropertyID { get } ``` |

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

Modified kAudioUnitProperty_IsInterAppConnected

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_IsInterAppConnected: Int { get } ``` |
| To | ``` var kAudioUnitProperty_IsInterAppConnected: AudioUnitPropertyID { get } ``` |

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

Modified kAudioUnitProperty_ParameterValueStrings

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_ParameterValueStrings: Int { get } ``` |
| To | ``` var kAudioUnitProperty_ParameterValueStrings: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_PeerURL

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_PeerURL: Int { get } ``` |
| To | ``` var kAudioUnitProperty_PeerURL: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_PresentPreset

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_PresentPreset: Int { get } ``` |
| To | ``` var kAudioUnitProperty_PresentPreset: AudioUnitPropertyID { get } ``` |

Modified kAudioUnitProperty_RemoteControlEventListener

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitProperty_RemoteControlEventListener: Int { get } ``` |
| To | ``` var kAudioUnitProperty_RemoteControlEventListener: AudioUnitPropertyID { get } ``` |

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

Modified kAudioUnitSubType_AU3DMixerEmbedded

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var kAudioUnitSubType_AU3DMixerEmbedded: Int { get } ``` | -- |
| To | ``` var kAudioUnitSubType_AU3DMixerEmbedded: UInt32 { get } ``` | iOS 9.0 |

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

Modified kAudioUnitSubType_AUiPodEQ

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_AUiPodEQ: Int { get } ``` |
| To | ``` var kAudioUnitSubType_AUiPodEQ: UInt32 { get } ``` |

Modified kAudioUnitSubType_AUiPodTime

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_AUiPodTime: Int { get } ``` |
| To | ``` var kAudioUnitSubType_AUiPodTime: UInt32 { get } ``` |

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

Modified kAudioUnitSubType_RemoteIO

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_RemoteIO: Int { get } ``` |
| To | ``` var kAudioUnitSubType_RemoteIO: UInt32 { get } ``` |

Modified kAudioUnitSubType_Reverb2

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Reverb2: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Reverb2: UInt32 { get } ``` |

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

Modified kAudioUnitSubType_SpatialMixer

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_SpatialMixer: Int { get } ``` |
| To | ``` var kAudioUnitSubType_SpatialMixer: UInt32 { get } ``` |

Modified kAudioUnitSubType_Splitter

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Splitter: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Splitter: UInt32 { get } ``` |

Modified kAudioUnitSubType_Varispeed

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitSubType_Varispeed: Int { get } ``` |
| To | ``` var kAudioUnitSubType_Varispeed: UInt32 { get } ``` |

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

Modified kAudioUnitType_RemoteEffect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_RemoteEffect: Int { get } ``` |
| To | ``` var kAudioUnitType_RemoteEffect: UInt32 { get } ``` |

Modified kAudioUnitType_RemoteGenerator

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_RemoteGenerator: Int { get } ``` |
| To | ``` var kAudioUnitType_RemoteGenerator: UInt32 { get } ``` |

Modified kAudioUnitType_RemoteInstrument

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_RemoteInstrument: Int { get } ``` |
| To | ``` var kAudioUnitType_RemoteInstrument: UInt32 { get } ``` |

Modified kAudioUnitType_RemoteMusicEffect

|  | Declaration |
| --- | --- |
| From | ``` var kAudioUnitType_RemoteMusicEffect: Int { get } ``` |
| To | ``` var kAudioUnitType_RemoteMusicEffect: UInt32 { get } ``` |

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

Modified kAUVoiceIOProperty_BypassVoiceProcessing

|  | Declaration |
| --- | --- |
| From | ``` var kAUVoiceIOProperty_BypassVoiceProcessing: Int { get } ``` |
| To | ``` var kAUVoiceIOProperty_BypassVoiceProcessing: AudioUnitPropertyID { get } ``` |

Modified kAUVoiceIOProperty_DuckNonVoiceAudio

|  | Declaration |
| --- | --- |
| From | ``` var kAUVoiceIOProperty_DuckNonVoiceAudio: Int { get } ``` |
| To | ``` var kAUVoiceIOProperty_DuckNonVoiceAudio: AudioUnitPropertyID { get } ``` |

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

Modified kMusicDeviceProperty_BankName

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_BankName: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_BankName: AudioUnitPropertyID { get } ``` |

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

Modified kMusicDeviceProperty_SoundBankURL

|  | Declaration |
| --- | --- |
| From | ``` var kMusicDeviceProperty_SoundBankURL: Int { get } ``` |
| To | ``` var kMusicDeviceProperty_SoundBankURL: AudioUnitPropertyID { get } ``` |

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

Modified kReverb2Param_DecayTimeAt0Hz

|  | Declaration |
| --- | --- |
| From | ``` var kReverb2Param_DecayTimeAt0Hz: Int { get } ``` |
| To | ``` var kReverb2Param_DecayTimeAt0Hz: AudioUnitParameterID { get } ``` |

Modified kReverb2Param_DecayTimeAtNyquist

|  | Declaration |
| --- | --- |
| From | ``` var kReverb2Param_DecayTimeAtNyquist: Int { get } ``` |
| To | ``` var kReverb2Param_DecayTimeAtNyquist: AudioUnitParameterID { get } ``` |

Modified kReverb2Param_DryWetMix

|  | Declaration |
| --- | --- |
| From | ``` var kReverb2Param_DryWetMix: Int { get } ``` |
| To | ``` var kReverb2Param_DryWetMix: AudioUnitParameterID { get } ``` |

Modified kReverb2Param_Gain

|  | Declaration |
| --- | --- |
| From | ``` var kReverb2Param_Gain: Int { get } ``` |
| To | ``` var kReverb2Param_Gain: AudioUnitParameterID { get } ``` |

Modified kReverb2Param_MaxDelayTime

|  | Declaration |
| --- | --- |
| From | ``` var kReverb2Param_MaxDelayTime: Int { get } ``` |
| To | ``` var kReverb2Param_MaxDelayTime: AudioUnitParameterID { get } ``` |

Modified kReverb2Param_MinDelayTime

|  | Declaration |
| --- | --- |
| From | ``` var kReverb2Param_MinDelayTime: Int { get } ``` |
| To | ``` var kReverb2Param_MinDelayTime: AudioUnitParameterID { get } ``` |

Modified kReverb2Param_RandomizeReflections

|  | Declaration |
| --- | --- |
| From | ``` var kReverb2Param_RandomizeReflections: Int { get } ``` |
| To | ``` var kReverb2Param_RandomizeReflections: AudioUnitParameterID { get } ``` |

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
