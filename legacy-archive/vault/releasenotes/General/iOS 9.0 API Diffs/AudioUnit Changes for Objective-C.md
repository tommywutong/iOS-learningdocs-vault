---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/AudioUnit.html
archived_at: '2026-07-18T02:56:30.634562Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AudioUnit Changes for Objective-C

### AudioUnit

#### AUAudioUnit.h (Added)

Added [AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounit)Added [-[AUAudioUnit allocateRenderResourcesAndReturnError:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387620-allocaterenderresourcesandreturn)Added [AUAudioUnit.allParameterValues](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387679-allparametervalues)Added [AUAudioUnit.audioUnitName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387640-audiounitname)Added [AUAudioUnit.canPerformInput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387551-canperforminput)Added [AUAudioUnit.canPerformOutput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387656-canperformoutput)Added [AUAudioUnit.canProcessInPlace](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387583-canprocessinplace)Added [AUAudioUnit.channelCapabilities](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387685-channelcapabilities)Added [AUAudioUnit.component](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387535-component)Added [AUAudioUnit.componentDescription](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387568-componentdescription)Added [AUAudioUnit.componentName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387566-componentname)Added [AUAudioUnit.componentVersion](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387555-componentversion)Added [AUAudioUnit.contextName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387553-contextname)Added [AUAudioUnit.currentPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387668-currentpreset)Added [-[AUAudioUnit deallocateRenderResources]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387612-deallocaterenderresources)Added [AUAudioUnit.factoryPresets](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387526-factorypresets)Added [AUAudioUnit.fullState](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387500-fullstate)Added [AUAudioUnit.fullStateForDocument](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387630-fullstatefordocument)Added [-[AUAudioUnit initWithComponentDescription:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387570-initwithcomponentdescription)Added [-[AUAudioUnit initWithComponentDescription:options:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387664-init)Added [AUAudioUnit.inputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387636-inputbusses)Added [AUAudioUnit.inputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387660-isinputenabled)Added [AUAudioUnit.inputHandler](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387616-inputhandler)Added [+[AUAudioUnit instantiateWithComponentDescription:options:completionHandler:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387606-instantiate)Added [AUAudioUnit.latency](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387675-latency)Added [AUAudioUnit.manufacturerName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387681-manufacturername)Added [AUAudioUnit.maximumFramesToRender](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387654-maximumframestorender)Added [AUAudioUnit.musicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387669-musicalcontextblock)Added [AUAudioUnit.musicDeviceOrEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387497-ismusicdeviceoreffect)Added [AUAudioUnit.outputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387503-outputbusses)Added [AUAudioUnit.outputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387646-isoutputenabled)Added [AUAudioUnit.outputProvider](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387596-outputprovider)Added [-[AUAudioUnit parametersForOverviewWithCount:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387549-parametersforoverviewwithcount)Added [AUAudioUnit.parameterTree](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387650-parametertree)Added [-[AUAudioUnit removeRenderObserver:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387564-removerenderobserver)Added [AUAudioUnit.renderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387687-renderblock)Added [AUAudioUnit.renderingOffline](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387578-isrenderingoffline)Added [AUAudioUnit.renderQuality](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387648-renderquality)Added [AUAudioUnit.renderResourcesAllocated](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387618-renderresourcesallocated)Added [-[AUAudioUnit reset]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387658-reset)Added [AUAudioUnit.scheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387576-schedulemidieventblock)Added [AUAudioUnit.scheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387677-scheduleparameterblock)Added [AUAudioUnit.shouldBypassEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387545-shouldbypasseffect)Added [-[AUAudioUnit startHardwareAndReturnError:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387581-starthardware)Added [-[AUAudioUnit stopHardware]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387642-stophardware)Added [AUAudioUnit.tailTime](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387614-tailtime)Added [-[AUAudioUnit tokenByAddingRenderObserver:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387509-token)Added [AUAudioUnit.transportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387559-transportstateblock)Added [AUAudioUnit.virtualMIDICableCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387666-virtualmidicablecount)Added [AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus)Added [AUAudioUnitBus.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387524-bustype)Added [AUAudioUnitBus.contextPresentationLatency](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387547-contextpresentationlatency)Added [AUAudioUnitBus.enabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387634-isenabled)Added [AUAudioUnitBus.format](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387689-format)Added [AUAudioUnitBus.index](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387557-index)Added [AUAudioUnitBus.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387514-name)Added [AUAudioUnitBus.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387638-owneraudiounit)Added [-[AUAudioUnitBus setFormat:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387644-setformat)Added [AUAudioUnitBus.supportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387622-supportedchannellayouttags)Added [AUAudioUnitBusArray](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray)Added [-[AUAudioUnitBusArray addObserverToAllBusses:forKeyPath:options:context:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387520-addobserver)Added [AUAudioUnitBusArray.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387671-bustype)Added [AUAudioUnitBusArray.count](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387673-count)Added [AUAudioUnitBusArray.countChangeable](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387537-iscountchangeable)Added [-[AUAudioUnitBusArray initWithAudioUnit:busType:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387662-init)Added [-[AUAudioUnitBusArray initWithAudioUnit:busType:busses:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387516-initwithaudiounit)Added [-[AUAudioUnitBusArray objectAtIndexedSubscript:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387507-subscript)Added [AUAudioUnitBusArray.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387510-owneraudiounit)Added [-[AUAudioUnitBusArray removeObserverFromAllBusses:forKeyPath:context:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387505-removeobserver)Added [-[AUAudioUnitBusArray setBusCount:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387598-setbuscount)Added [AUAudioUnitPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset)Added [AUAudioUnitPreset.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387587-name)Added [AUAudioUnitPreset.number](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387626-number)Added [AUAudioChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiochannelcount)Added [AUAudioFrameCount](https://developer.apple.com/documentation/audiotoolbox/auaudioframecount)Added AUAudioUnit(AUAudioInputOutputUnit)Added [AUAudioUnitBusType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype)Added [AUAudioUnitBusTypeInput](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/input)Added [AUAudioUnitBusTypeOutput](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/auaudiounitbustypeoutput)Added [AUAudioUnitStatus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitstatus)Added [AUEventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aueventsampletime)Added [AUEventSampleTimeImmediate](https://developer.apple.com/documentation/audiotoolbox/1387633-aueventsampletime/aueventsampletimeimmediate)Added [AUHostMusicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auhostmusicalcontextblock)Added [AUHostTransportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateblock)Added [AUHostTransportStateChanged](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstatechanged)Added [AUHostTransportStateCycling](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstatecycling)Added [AUHostTransportStateFlags](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags)Added [AUHostTransportStateMoving](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387579-moving)Added [AUHostTransportStateRecording](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstaterecording)Added [AUInputHandler](https://developer.apple.com/documentation/audiotoolbox/auinputhandler)Added [AURenderBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderblock)Added [AURenderObserver](https://developer.apple.com/documentation/audiotoolbox/aurenderobserver)Added [AURenderPullInputBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderpullinputblock)Added [AUScheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auschedulemidieventblock)Added [AUScheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auscheduleparameterblock)

#### AUAudioUnitImplementation.h (Added)

Added [AUAudioUnit.internalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439864-internalrenderblock)Added [+[AUAudioUnit registerSubclass:asComponentDescription:name:version:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1438315-registersubclass)Added [-[AUAudioUnit setRenderResourcesAllocated:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1440830-setrenderresourcesallocated)Added [-[AUAudioUnit shouldChangeToFormat:forBus:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439999-shouldchangetoformat)Added [-[AUAudioUnitBus initWithFormat:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440039-initwithformat)Added [AUAudioUnitBus.maximumChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1439855-maximumchannelcount)Added [AUAudioUnitBus.supportedChannelCounts](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440352-supportedchannelcounts)Added [-[AUAudioUnitBusArray replaceBusses:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1440520-replacebusses)Added [AUAudioUnitFactory](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory)Added [-[AUAudioUnitFactory createAudioUnitWithComponentDescription:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory/1440321-createaudiounitwithcomponentdesc)Added [AUAudioUnitV2Bridge](https://developer.apple.com/documentation/audiotoolbox/auaudiounitv2bridge)Added [AUParameterNode.implementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439427-implementordisplaynamewithlength)Added [AUParameterNode.implementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440045-implementorstringfromvaluecallba)Added [AUParameterNode.implementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439270-implementorvaluefromstringcallba)Added [AUParameterNode.implementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439658-implementorvalueobserver)Added [AUParameterNode.implementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439942-implementorvalueprovider)Added [+[AUParameterTree createGroupFromTemplate:identifier:name:addressOffset:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439822-creategroupfromtemplate)Added [+[AUParameterTree createGroupTemplate:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439912-creategrouptemplate)Added [+[AUParameterTree createGroupWithIdentifier:name:children:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439002-creategroupwithidentifier)Added [+[AUParameterTree createParameterWithIdentifier:name:address:min:max:unit:unitName:flags:valueStrings:dependentParameters:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1440598-createparameter)Added [+[AUParameterTree createTreeWithChildren:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438522-createtree)Added AUAudioUnit(AUAudioUnitImplementation)Added AUAudioUnitBus(AUAudioUnitImplementation)Added AUAudioUnitBusArray(AUAudioUnitBusImplementation)Added [AUImplementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementordisplaynamewithlengthcallback)Added [AUImplementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorstringfromvaluecallback)Added [AUImplementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorvaluefromstringcallback)Added [AUImplementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueobserver)Added [AUImplementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueprovider)Added [AUInternalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auinternalrenderblock)Added [AUMIDIEvent](https://developer.apple.com/documentation/audiotoolbox/aumidievent)Added [AUParameterEvent](https://developer.apple.com/documentation/audiotoolbox/auparameterevent)Added AUParameterNode(AUParameterNodeImplementation)Added AUParameterTree(Factory)Added [AURenderEvent](https://developer.apple.com/documentation/audiotoolbox/1440272-aurenderevent)Added [AURenderEventHeader](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader)Added [AURenderEventMIDI](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midi)Added [AURenderEventMIDISysEx](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midisysex)Added [AURenderEventParameter](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/aurendereventparameter)Added [AURenderEventParameterRamp](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/parameterramp)Added [AURenderEventType](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype)

#### AUComponent.h

Added #def AudioUnit_AUComponent_hAdded [kAudioComponentInstanceInvalidationNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentinstanceinvalidationnotification)Added [kAudioUnitSubType_MultiSplitter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_multisplitter)Modified [kAudioUnitErr_IllegalInstrument](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_illegalinstrument)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kAudioUnitErr_InstrumentTypeNotFound](https://developer.apple.com/documentation/audiotoolbox/1584141-anonymous/kaudiouniterr_instrumenttypenotfound)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [kAudioUnitSubType_AU3DMixerEmbedded](https://developer.apple.com/documentation/audiotoolbox/1619479-anonymous/kaudiounitsubtype_au3dmixerembedded)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### AudioComponent.h

Added [AudioComponentFlags](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags)Added [AudioComponentInstantiate()](https://developer.apple.com/documentation/audiotoolbox/1410517-audiocomponentinstantiate)Added [AudioComponentInstantiationOptions](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions)Added [AudioComponentValidationResult](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult)Added #def AudioUnit_AudioComponent_hAdded [#def kAudioComponentConfigurationInfo_ValidationResult](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentconfigurationinfo_validationresult)Added [kAudioComponentFlag_CanLoadInProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/1410506-canloadinprocess)Added [kAudioComponentFlag_IsV3AudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_isv3audiounit)Added [kAudioComponentFlag_RequiresAsyncInstantiation](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_requiresasyncinstantiation)Added [kAudioComponentInstantiation_LoadOutOfProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions/kaudiocomponentinstantiation_loadoutofprocess)Added [#def kAudioComponentValidationParameter_ForceValidation](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_forcevalidation)Added [#def kAudioComponentValidationParameter_TimeOut](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_timeout)Added [kAudioComponentValidationResult_Failed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/failed)Added [kAudioComponentValidationResult_Passed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/passed)Added [kAudioComponentValidationResult_TimedOut](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/timedout)Added [kAudioComponentValidationResult_UnauthorizedError_Init](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/unauthorizederror_init)Added [kAudioComponentValidationResult_UnauthorizedError_Open](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_unauthorizederror_open)Added [kAudioComponentValidationResult_Unknown](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_unknown)Modified [kAudioComponentFlag_SandboxSafe](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_sandboxsafe)

|  | Introduction |
| --- | --- |
| From | iOS 7.0 |
| To | iOS 6.0 |

#### AudioOutputUnit.h

Added #def AudioUnit_AudioOutputUnit_h

#### AudioUnitParameters.h

Added #def AudioUnit_AudioUnitParameters_h

#### AudioUnitProperties.h

Removed [#def GetAudioUnitParameterDisplayType](https://developer.apple.com/documentation/audiounit/audio_unit_properties/getaudiounitparameterdisplaytype)Removed [#def SetAudioUnitParameterDisplayType](https://developer.apple.com/documentation/audiounit/audio_unit_properties/setaudiounitparameterdisplaytype)Added [AU3DMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve)Added [AU3DMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags)Added #def AudioUnit_AudioUnitProperties_hAdded [AudioUnitParameterOptions](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions)Added [AUReverbRoomType](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype)Added [AUScheduledAudioSliceFlags](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags)Added [AUSpatializationAlgorithm](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm)Added [AUSpatialMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve)Added [AUSpatialMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags)Added [GetAudioUnitParameterDisplayType()](https://developer.apple.com/documentation/audiotoolbox/1440794-getaudiounitparameterdisplaytype)Added [#def kAudioUnitConfigurationInfo_BusCountWritable](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_buscountwritable)Added [#def kAudioUnitConfigurationInfo_SupportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_supportedchannellayouttags)Added [kAudioUnitProperty_ClassInfoFromDocument](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_classinfofromdocument)Added [kAudioUnitProperty_ContextName](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_contextname)Added [kAudioUnitProperty_ParameterClumpName](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parameterclumpname)Added [kAudioUnitProperty_ParametersForOverview](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parametersforoverview)Added [kAudioUnitProperty_PresentationLatency](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_presentationlatency)Added [kAudioUnitProperty_RequestViewController](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_requestviewcontroller)Added [SetAudioUnitParameterDisplayType()](https://developer.apple.com/documentation/audiotoolbox/1440769-setaudiounitparameterdisplaytype)Modified [kAudioUnitProperty_3DMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_3dmixerattenuationcurve)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 2.0 | -- |
| To | iOS 3.0 | iOS 9.0 |

Modified [kAudioUnitProperty_3DMixerDistanceAtten](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_3dmixerdistanceatten)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 2.0 | -- |
| To | iOS 3.0 | iOS 9.0 |

Modified [kAudioUnitProperty_3DMixerDistanceParams](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_3dmixerdistanceparams)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 2.0 | -- |
| To | iOS 3.0 | iOS 9.0 |

Modified [kAudioUnitProperty_3DMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_3dmixerrenderingflags)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 2.0 | -- |
| To | iOS 3.0 | iOS 9.0 |

Modified [kAudioUnitProperty_DopplerShift](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_dopplershift)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 2.0 | -- |
| To | iOS 3.0 | iOS 9.0 |

Modified [kAudioUnitProperty_ReverbPreset](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_reverbpreset)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 2.0 | -- |
| To | iOS 3.0 | iOS 9.0 |

Modified [kAUVoiceIOProperty_DuckNonVoiceAudio](https://developer.apple.com/documentation/audiotoolbox/1621044-anonymous/kauvoiceioproperty_ducknonvoiceaudio)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [kAUVoiceIOProperty_VoiceProcessingQuality](https://developer.apple.com/documentation/audiotoolbox/1534074-anonymous/kauvoiceioproperty_voiceprocessingquality)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 3.0 | iOS 7.0 |

#### AUParameters.h (Added)

Added [AUParameter](https://developer.apple.com/documentation/audiotoolbox/auparameter)Added [AUParameter.address](https://developer.apple.com/documentation/audiotoolbox/auparameter/1441037-address)Added [AUParameter.dependentParameters](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440649-dependentparameters)Added [AUParameter.flags](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439938-flags)Added [AUParameter.maxValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438427-maxvalue)Added [AUParameter.minValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440270-minvalue)Added [-[AUParameter setValue:originator:]](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439968-setvalue)Added [-[AUParameter setValue:originator:atHostTime:]](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438450-setvalue)Added [-[AUParameter stringFromValue:]](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440901-string)Added [AUParameter.unit](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440698-unit)Added [AUParameter.unitName](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438490-unitname)Added [AUParameter.value](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439301-value)Added [-[AUParameter valueFromString:]](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440495-value)Added [AUParameter.valueStrings](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438358-valuestrings)Added [AUParameterGroup](https://developer.apple.com/documentation/audiotoolbox/auparametergroup)Added [AUParameterGroup.allParameters](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439439-allparameters)Added [AUParameterGroup.children](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439325-children)Added [AUParameterNode](https://developer.apple.com/documentation/audiotoolbox/auparameternode)Added [AUParameterNode.displayName](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440278-displayname)Added [-[AUParameterNode displayNameWithLength:]](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439449-displaynamewithlength)Added [AUParameterNode.identifier](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440186-identifier)Added [AUParameterNode.keyPath](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439420-keypath)Added [-[AUParameterNode removeParameterObserver:]](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439314-removeparameterobserver)Added [-[AUParameterNode tokenByAddingParameterObserver:]](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440811-token)Added [-[AUParameterNode tokenByAddingParameterRecordingObserver:]](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440903-tokenbyaddingparameterrecordingo)Added [AUParameterTree](https://developer.apple.com/documentation/audiotoolbox/auparametertree)Added [-[AUParameterTree parameterWithAddress:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439569-parameterwithaddress)Added [-[AUParameterTree parameterWithID:scope:element:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438918-parameterwithid)Added [AUParameterAddress](https://developer.apple.com/documentation/audiotoolbox/auparameteraddress)Added [AUParameterObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterobserver)Added [AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameterobservertoken)Added [AUParameterRecordingObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterrecordingobserver)Added [AURecordedParameterEvent](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent)Added [AUValue](https://developer.apple.com/documentation/audiotoolbox/auvalue)

#### MusicDevice.h

Added #def AudioUnit_MusicDevice_h

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
