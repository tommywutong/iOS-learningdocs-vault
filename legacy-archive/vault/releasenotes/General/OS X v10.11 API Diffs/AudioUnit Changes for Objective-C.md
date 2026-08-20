---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/AudioUnit.html
archived_at: '2026-07-18T02:52:55.845553Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AudioUnit Changes for Objective-C

### AudioUnit

#### AUAudioUnit.h (Added)

Added [AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounit)Added [-[AUAudioUnit allocateRenderResourcesAndReturnError:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387620-allocaterenderresourcesandreturn)Added [AUAudioUnit.allParameterValues](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387679-allparametervalues)Added [AUAudioUnit.audioUnitName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387640-audiounitname)Added [AUAudioUnit.canPerformInput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387551-canperforminput)Added [AUAudioUnit.canPerformOutput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387656-canperformoutput)Added [AUAudioUnit.canProcessInPlace](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387583-canprocessinplace)Added [AUAudioUnit.channelCapabilities](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387685-channelcapabilities)Added [AUAudioUnit.component](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387535-component)Added [AUAudioUnit.componentDescription](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387568-componentdescription)Added [AUAudioUnit.componentName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387566-componentname)Added [AUAudioUnit.componentVersion](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387555-componentversion)Added [AUAudioUnit.contextName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387553-contextname)Added [AUAudioUnit.currentPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387668-currentpreset)Added [-[AUAudioUnit deallocateRenderResources]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387612-deallocaterenderresources)Added [AUAudioUnit.deviceID](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387683-deviceid)Added [AUAudioUnit.factoryPresets](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387526-factorypresets)Added [AUAudioUnit.fullState](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387500-fullstate)Added [AUAudioUnit.fullStateForDocument](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387630-fullstatefordocument)Added [-[AUAudioUnit initWithComponentDescription:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387570-initwithcomponentdescription)Added [-[AUAudioUnit initWithComponentDescription:options:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387664-init)Added [AUAudioUnit.inputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387636-inputbusses)Added [AUAudioUnit.inputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387660-isinputenabled)Added [AUAudioUnit.inputHandler](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387616-inputhandler)Added [+[AUAudioUnit instantiateWithComponentDescription:options:completionHandler:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387606-instantiate)Added [AUAudioUnit.latency](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387675-latency)Added [AUAudioUnit.manufacturerName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387681-manufacturername)Added [AUAudioUnit.maximumFramesToRender](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387654-maximumframestorender)Added [AUAudioUnit.musicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387669-musicalcontextblock)Added [AUAudioUnit.musicDeviceOrEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387497-ismusicdeviceoreffect)Added [AUAudioUnit.outputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387503-outputbusses)Added [AUAudioUnit.outputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387646-isoutputenabled)Added [AUAudioUnit.outputProvider](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387596-outputprovider)Added [-[AUAudioUnit parametersForOverviewWithCount:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387549-parametersforoverviewwithcount)Added [AUAudioUnit.parameterTree](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387650-parametertree)Added [-[AUAudioUnit removeRenderObserver:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387564-removerenderobserver)Added [AUAudioUnit.renderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387687-renderblock)Added [AUAudioUnit.renderingOffline](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387578-isrenderingoffline)Added [AUAudioUnit.renderQuality](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387648-renderquality)Added [AUAudioUnit.renderResourcesAllocated](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387618-renderresourcesallocated)Added [-[AUAudioUnit reset]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387658-reset)Added [AUAudioUnit.scheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387576-schedulemidieventblock)Added [AUAudioUnit.scheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387677-scheduleparameterblock)Added [-[AUAudioUnit setDeviceID:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387608-setdeviceid)Added [AUAudioUnit.shouldBypassEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387545-shouldbypasseffect)Added [-[AUAudioUnit startHardwareAndReturnError:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387581-starthardware)Added [-[AUAudioUnit stopHardware]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387642-stophardware)Added [AUAudioUnit.tailTime](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387614-tailtime)Added [-[AUAudioUnit tokenByAddingRenderObserver:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387509-token)Added [AUAudioUnit.transportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387559-transportstateblock)Added [AUAudioUnit.virtualMIDICableCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387666-virtualmidicablecount)Added [AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus)Added [AUAudioUnitBus.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387524-bustype)Added [AUAudioUnitBus.contextPresentationLatency](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387547-contextpresentationlatency)Added [AUAudioUnitBus.enabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387634-isenabled)Added [AUAudioUnitBus.format](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387689-format)Added [AUAudioUnitBus.index](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387557-index)Added [AUAudioUnitBus.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387514-name)Added [AUAudioUnitBus.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387638-owneraudiounit)Added [-[AUAudioUnitBus setFormat:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387644-setformat)Added [AUAudioUnitBus.supportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387622-supportedchannellayouttags)Added [AUAudioUnitBusArray](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray)Added [-[AUAudioUnitBusArray addObserverToAllBusses:forKeyPath:options:context:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387520-addobserver)Added [AUAudioUnitBusArray.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387671-bustype)Added [AUAudioUnitBusArray.count](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387673-count)Added [AUAudioUnitBusArray.countChangeable](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387537-iscountchangeable)Added [-[AUAudioUnitBusArray initWithAudioUnit:busType:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387662-init)Added [-[AUAudioUnitBusArray initWithAudioUnit:busType:busses:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387516-initwithaudiounit)Added [-[AUAudioUnitBusArray objectAtIndexedSubscript:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387507-subscript)Added [AUAudioUnitBusArray.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387510-owneraudiounit)Added [-[AUAudioUnitBusArray removeObserverFromAllBusses:forKeyPath:context:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387505-removeobserver)Added [-[AUAudioUnitBusArray setBusCount:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387598-setbuscount)Added [AUAudioUnitPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset)Added [AUAudioUnitPreset.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387587-name)Added [AUAudioUnitPreset.number](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387626-number)Added [AUAudioChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiochannelcount)Added [AUAudioFrameCount](https://developer.apple.com/documentation/audiotoolbox/auaudioframecount)Added AUAudioUnit(AUAudioInputOutputUnit)Added [AUAudioUnitBusType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype)Added [AUAudioUnitBusTypeInput](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/input)Added [AUAudioUnitBusTypeOutput](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/auaudiounitbustypeoutput)Added [AUAudioUnitStatus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitstatus)Added [AUEventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aueventsampletime)Added [AUEventSampleTimeImmediate](https://developer.apple.com/documentation/audiotoolbox/1387633-aueventsampletime/aueventsampletimeimmediate)Added [AUHostMusicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auhostmusicalcontextblock)Added [AUHostTransportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateblock)Added [AUHostTransportStateChanged](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstatechanged)Added [AUHostTransportStateCycling](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstatecycling)Added [AUHostTransportStateFlags](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags)Added [AUHostTransportStateMoving](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387579-moving)Added [AUHostTransportStateRecording](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstaterecording)Added [AUInputHandler](https://developer.apple.com/documentation/audiotoolbox/auinputhandler)Added [AURenderBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderblock)Added [AURenderObserver](https://developer.apple.com/documentation/audiotoolbox/aurenderobserver)Added [AURenderPullInputBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderpullinputblock)Added [AUScheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auschedulemidieventblock)Added [AUScheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auscheduleparameterblock)

#### AUAudioUnitImplementation.h (Added)

Added [AUAudioUnit.internalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439864-internalrenderblock)Added [+[AUAudioUnit registerSubclass:asComponentDescription:name:version:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1438315-registersubclass)Added [-[AUAudioUnit setRenderResourcesAllocated:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1440830-setrenderresourcesallocated)Added [-[AUAudioUnit shouldChangeToFormat:forBus:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439999-shouldchangetoformat)Added [-[AUAudioUnitBus initWithFormat:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440039-initwithformat)Added [AUAudioUnitBus.maximumChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1439855-maximumchannelcount)Added [AUAudioUnitBus.supportedChannelCounts](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440352-supportedchannelcounts)Added [-[AUAudioUnitBusArray replaceBusses:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1440520-replacebusses)Added [AUAudioUnitFactory](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory)Added [-[AUAudioUnitFactory createAudioUnitWithComponentDescription:error:]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory/1440321-createaudiounitwithcomponentdesc)Added [AUAudioUnitV2Bridge](https://developer.apple.com/documentation/audiotoolbox/auaudiounitv2bridge)Added [AUParameterNode.implementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439427-implementordisplaynamewithlength)Added [AUParameterNode.implementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440045-implementorstringfromvaluecallba)Added [AUParameterNode.implementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439270-implementorvaluefromstringcallba)Added [AUParameterNode.implementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439658-implementorvalueobserver)Added [AUParameterNode.implementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439942-implementorvalueprovider)Added [+[AUParameterTree createGroupFromTemplate:identifier:name:addressOffset:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439822-creategroupfromtemplate)Added [+[AUParameterTree createGroupTemplate:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439912-creategrouptemplate)Added [+[AUParameterTree createGroupWithIdentifier:name:children:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439002-creategroupwithidentifier)Added [+[AUParameterTree createParameterWithIdentifier:name:address:min:max:unit:unitName:flags:valueStrings:dependentParameters:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1440598-createparameter)Added [+[AUParameterTree createTreeWithChildren:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438522-createtree)Added AUAudioUnit(AUAudioUnitImplementation)Added AUAudioUnitBus(AUAudioUnitImplementation)Added AUAudioUnitBusArray(AUAudioUnitBusImplementation)Added [AUImplementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementordisplaynamewithlengthcallback)Added [AUImplementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorstringfromvaluecallback)Added [AUImplementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorvaluefromstringcallback)Added [AUImplementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueobserver)Added [AUImplementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueprovider)Added [AUInternalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auinternalrenderblock)Added [AUMIDIEvent](https://developer.apple.com/documentation/audiotoolbox/aumidievent)Added [AUParameterEvent](https://developer.apple.com/documentation/audiotoolbox/auparameterevent)Added AUParameterNode(AUParameterNodeImplementation)Added AUParameterTree(Factory)Added [AURenderEvent](https://developer.apple.com/documentation/audiotoolbox/1440272-aurenderevent)Added [AURenderEventHeader](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader)Added [AURenderEventMIDI](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midi)Added [AURenderEventMIDISysEx](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midisysex)Added [AURenderEventParameter](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/aurendereventparameter)Added [AURenderEventParameterRamp](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/parameterramp)Added [AURenderEventType](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype)

#### AUCocoaUIView.h

Modified [-[AUCocoaUIBase uiViewForAudioUnit:withSize:]](https://developer.apple.com/documentation/audiotoolbox/aucocoauibase/1395992-uiviewforaudiounit)

|  | Declaration |
| --- | --- |
| From | ``` - (NSView *)uiViewForAudioUnit:(AudioUnit)inAudioUnit withSize:(NSSize)inPreferredSize ``` |
| To | ``` - (NSView * _Nullable)uiViewForAudioUnit:(AudioUnit _Nonnull)inAudioUnit withSize:(NSSize)inPreferredSize ``` |

#### AUComponent.h

Added #def AudioUnit_AUComponent_hAdded [kAudioComponentErr_InstanceInvalidated](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiocomponenterr_instanceinvalidated)Added [kAudioComponentInstanceInvalidationNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentinstanceinvalidationnotification)Added [kAudioComponentRegistrationsChangedNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentregistrationschangednotification)Added [kAudioUnitSubType_MultiSplitter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_multisplitter)Modified [AudioUnitAddPropertyListener()](https://developer.apple.com/documentation/audiotoolbox/1440111-audiounitaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitAddPropertyListener (     AudioUnit inUnit,     AudioUnitPropertyID inID,     AudioUnitPropertyListenerProc inProc,     void *inProcUserData ); ``` |
| To | ``` OSStatus AudioUnitAddPropertyListener (     AudioUnit _Nonnull inUnit,     AudioUnitPropertyID inID,     AudioUnitPropertyListenerProc _Nonnull inProc,     void * _Nullable inProcUserData ); ``` |

Modified [AudioUnitAddRenderNotify()](https://developer.apple.com/documentation/audiotoolbox/1440259-audiounitaddrendernotify)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitAddRenderNotify (     AudioUnit inUnit,     AURenderCallback inProc,     void *inProcUserData ); ``` |
| To | ``` OSStatus AudioUnitAddRenderNotify (     AudioUnit _Nonnull inUnit,     AURenderCallback _Nonnull inProc,     void * _Nullable inProcUserData ); ``` |

Modified [AudioUnitGetParameter()](https://developer.apple.com/documentation/audiotoolbox/1440055-audiounitgetparameter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitGetParameter (     AudioUnit inUnit,     AudioUnitParameterID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     AudioUnitParameterValue *outValue ); ``` |
| To | ``` OSStatus AudioUnitGetParameter (     AudioUnit _Nonnull inUnit,     AudioUnitParameterID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     AudioUnitParameterValue * _Nonnull outValue ); ``` |

Modified [AudioUnitGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1439840-audiounitgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitGetProperty (     AudioUnit inUnit,     AudioUnitPropertyID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     void *outData,     UInt32 *ioDataSize ); ``` |
| To | ``` OSStatus AudioUnitGetProperty (     AudioUnit _Nonnull inUnit,     AudioUnitPropertyID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     void * _Nonnull outData,     UInt32 * _Nonnull ioDataSize ); ``` |

Modified [AudioUnitGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1440663-audiounitgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitGetPropertyInfo (     AudioUnit inUnit,     AudioUnitPropertyID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     UInt32 *outDataSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioUnitGetPropertyInfo (     AudioUnit _Nonnull inUnit,     AudioUnitPropertyID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     UInt32 * _Nullable outDataSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioUnitInitialize()](https://developer.apple.com/documentation/audiotoolbox/1439851-audiounitinitialize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitInitialize (     AudioUnit inUnit ); ``` |
| To | ``` OSStatus AudioUnitInitialize (     AudioUnit _Nonnull inUnit ); ``` |

Modified [AudioUnitProcess()](https://developer.apple.com/documentation/audiotoolbox/1439630-audiounitprocess)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitProcess (     AudioUnit inUnit,     AudioUnitRenderActionFlags *ioActionFlags,     const AudioTimeStamp *inTimeStamp,     UInt32 inNumberFrames,     AudioBufferList *ioData ); ``` |
| To | ``` OSStatus AudioUnitProcess (     AudioUnit _Nonnull inUnit,     AudioUnitRenderActionFlags * _Nullable ioActionFlags,     const AudioTimeStamp * _Nonnull inTimeStamp,     UInt32 inNumberFrames,     AudioBufferList * _Nonnull ioData ); ``` |

Modified [AudioUnitProcessMultiple()](https://developer.apple.com/documentation/audiotoolbox/1440334-audiounitprocessmultiple)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitProcessMultiple (     AudioUnit inUnit,     AudioUnitRenderActionFlags *ioActionFlags,     const AudioTimeStamp *inTimeStamp,     UInt32 inNumberFrames,     UInt32 inNumberInputBufferLists,     const AudioBufferList **inInputBufferLists,     UInt32 inNumberOutputBufferLists,     AudioBufferList **ioOutputBufferLists ); ``` |
| To | ``` OSStatus AudioUnitProcessMultiple (     AudioUnit _Nonnull inUnit,     AudioUnitRenderActionFlags * _Nullable ioActionFlags,     const AudioTimeStamp * _Nonnull inTimeStamp,     UInt32 inNumberFrames,     UInt32 inNumberInputBufferLists,     const AudioBufferList * _Nonnull * _Nonnull inInputBufferLists,     UInt32 inNumberOutputBufferLists,     AudioBufferList * _Nonnull * _Nonnull ioOutputBufferLists ); ``` |

Modified AudioUnitRemovePropertyListener()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitRemovePropertyListener (     AudioUnit inUnit,     AudioUnitPropertyID inID,     AudioUnitPropertyListenerProc inProc ); ``` |
| To | ``` OSStatus AudioUnitRemovePropertyListener (     AudioUnit _Nonnull inUnit,     AudioUnitPropertyID inID,     AudioUnitPropertyListenerProc _Nonnull inProc ); ``` |

Modified [AudioUnitRemovePropertyListenerWithUserData()](https://developer.apple.com/documentation/audiotoolbox/1441010-audiounitremovepropertylistenerw)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitRemovePropertyListenerWithUserData (     AudioUnit inUnit,     AudioUnitPropertyID inID,     AudioUnitPropertyListenerProc inProc,     void *inProcUserData ); ``` |
| To | ``` OSStatus AudioUnitRemovePropertyListenerWithUserData (     AudioUnit _Nonnull inUnit,     AudioUnitPropertyID inID,     AudioUnitPropertyListenerProc _Nonnull inProc,     void * _Nullable inProcUserData ); ``` |

Modified [AudioUnitRemoveRenderNotify()](https://developer.apple.com/documentation/audiotoolbox/1440547-audiounitremoverendernotify)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitRemoveRenderNotify (     AudioUnit inUnit,     AURenderCallback inProc,     void *inProcUserData ); ``` |
| To | ``` OSStatus AudioUnitRemoveRenderNotify (     AudioUnit _Nonnull inUnit,     AURenderCallback _Nonnull inProc,     void * _Nullable inProcUserData ); ``` |

Modified [AudioUnitRender()](https://developer.apple.com/documentation/audiotoolbox/1438430-audiounitrender)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitRender (     AudioUnit inUnit,     AudioUnitRenderActionFlags *ioActionFlags,     const AudioTimeStamp *inTimeStamp,     UInt32 inOutputBusNumber,     UInt32 inNumberFrames,     AudioBufferList *ioData ); ``` |
| To | ``` OSStatus AudioUnitRender (     AudioUnit _Nonnull inUnit,     AudioUnitRenderActionFlags * _Nullable ioActionFlags,     const AudioTimeStamp * _Nonnull inTimeStamp,     UInt32 inOutputBusNumber,     UInt32 inNumberFrames,     AudioBufferList * _Nonnull ioData ); ``` |

Modified [AudioUnitReset()](https://developer.apple.com/documentation/audiotoolbox/1439607-audiounitreset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitReset (     AudioUnit inUnit,     AudioUnitScope inScope,     AudioUnitElement inElement ); ``` |
| To | ``` OSStatus AudioUnitReset (     AudioUnit _Nonnull inUnit,     AudioUnitScope inScope,     AudioUnitElement inElement ); ``` |

Modified [AudioUnitScheduleParameters()](https://developer.apple.com/documentation/audiotoolbox/1439670-audiounitscheduleparameters)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitScheduleParameters (     AudioUnit inUnit,     const AudioUnitParameterEvent *inParameterEvent,     UInt32 inNumParamEvents ); ``` |
| To | ``` OSStatus AudioUnitScheduleParameters (     AudioUnit _Nonnull inUnit,     const AudioUnitParameterEvent * _Nonnull inParameterEvent,     UInt32 inNumParamEvents ); ``` |

Modified [AudioUnitSetParameter()](https://developer.apple.com/documentation/audiotoolbox/1438454-audiounitsetparameter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitSetParameter (     AudioUnit inUnit,     AudioUnitParameterID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     AudioUnitParameterValue inValue,     UInt32 inBufferOffsetInFrames ); ``` |
| To | ``` OSStatus AudioUnitSetParameter (     AudioUnit _Nonnull inUnit,     AudioUnitParameterID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     AudioUnitParameterValue inValue,     UInt32 inBufferOffsetInFrames ); ``` |

Modified [AudioUnitSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1440371-audiounitsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitSetProperty (     AudioUnit inUnit,     AudioUnitPropertyID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     const void *inData,     UInt32 inDataSize ); ``` |
| To | ``` OSStatus AudioUnitSetProperty (     AudioUnit _Nonnull inUnit,     AudioUnitPropertyID inID,     AudioUnitScope inScope,     AudioUnitElement inElement,     const void * _Nullable inData,     UInt32 inDataSize ); ``` |

Modified [AudioUnitUninitialize()](https://developer.apple.com/documentation/audiotoolbox/1438415-audiounituninitialize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioUnitUninitialize (     AudioUnit inUnit ); ``` |
| To | ``` OSStatus AudioUnitUninitialize (     AudioUnit _Nonnull inUnit ); ``` |

Modified [kAudioUnitErr_IllegalInstrument](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_illegalinstrument)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kAudioUnitErr_InstrumentTypeNotFound](https://developer.apple.com/documentation/audiotoolbox/1584141-anonymous/kaudiouniterr_instrumenttypenotfound)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kAudioUnitSubType_3DMixer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_3dmixer)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.3 | OS X 10.10 |

#### AudioCodec.h

Added [AudioSettingsFlags](https://developer.apple.com/documentation/audiotoolbox/audiosettingsflags)Added #def AudioUnit_AudioCodec_hModified [AudioCodecAppendInputBufferList()](https://developer.apple.com/documentation/audiotoolbox/1439811-audiocodecappendinputbufferlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecAppendInputBufferList (     AudioCodec inCodec,     const AudioBufferList *inBufferList,     UInt32 *ioNumberPackets,     const AudioStreamPacketDescription *inPacketDescription,     UInt32 *outBytesConsumed ); ``` |
| To | ``` OSStatus AudioCodecAppendInputBufferList (     AudioCodec _Nonnull inCodec,     const AudioBufferList * _Nonnull inBufferList,     UInt32 * _Nonnull ioNumberPackets,     const AudioStreamPacketDescription * _Nullable inPacketDescription,     UInt32 * _Nonnull outBytesConsumed ); ``` |

Modified [AudioCodecAppendInputData()](https://developer.apple.com/documentation/audiotoolbox/1438536-audiocodecappendinputdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecAppendInputData (     AudioCodec inCodec,     const void *inInputData,     UInt32 *ioInputDataByteSize,     UInt32 *ioNumberPackets,     const AudioStreamPacketDescription *inPacketDescription ); ``` |
| To | ``` OSStatus AudioCodecAppendInputData (     AudioCodec _Nonnull inCodec,     const void * _Nonnull inInputData,     UInt32 * _Nonnull ioInputDataByteSize,     UInt32 * _Nonnull ioNumberPackets,     const AudioStreamPacketDescription * _Nullable inPacketDescription ); ``` |

Modified [AudioCodecGetProperty()](https://developer.apple.com/documentation/audiotoolbox/1439429-audiocodecgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecGetProperty (     AudioCodec inCodec,     AudioCodecPropertyID inPropertyID,     UInt32 *ioPropertyDataSize,     void *outPropertyData ); ``` |
| To | ``` OSStatus AudioCodecGetProperty (     AudioCodec _Nonnull inCodec,     AudioCodecPropertyID inPropertyID,     UInt32 * _Nonnull ioPropertyDataSize,     void * _Nonnull outPropertyData ); ``` |

Modified [AudioCodecGetPropertyInfo()](https://developer.apple.com/documentation/audiotoolbox/1439602-audiocodecgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecGetPropertyInfo (     AudioCodec inCodec,     AudioCodecPropertyID inPropertyID,     UInt32 *outSize,     Boolean *outWritable ); ``` |
| To | ``` OSStatus AudioCodecGetPropertyInfo (     AudioCodec _Nonnull inCodec,     AudioCodecPropertyID inPropertyID,     UInt32 * _Nullable outSize,     Boolean * _Nullable outWritable ); ``` |

Modified [AudioCodecInitialize()](https://developer.apple.com/documentation/audiotoolbox/1440177-audiocodecinitialize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecInitialize (     AudioCodec inCodec,     const AudioStreamBasicDescription *inInputFormat,     const AudioStreamBasicDescription *inOutputFormat,     const void *inMagicCookie,     UInt32 inMagicCookieByteSize ); ``` |
| To | ``` OSStatus AudioCodecInitialize (     AudioCodec _Nonnull inCodec,     const AudioStreamBasicDescription * _Nullable inInputFormat,     const AudioStreamBasicDescription * _Nullable inOutputFormat,     const void * _Nullable inMagicCookie,     UInt32 inMagicCookieByteSize ); ``` |

Modified [AudioCodecProduceOutputBufferList()](https://developer.apple.com/documentation/audiotoolbox/1439926-audiocodecproduceoutputbufferlis)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecProduceOutputBufferList (     AudioCodec inCodec,     AudioBufferList *ioBufferList,     UInt32 *ioNumberPackets,     AudioStreamPacketDescription *outPacketDescription,     UInt32 *outStatus ); ``` |
| To | ``` OSStatus AudioCodecProduceOutputBufferList (     AudioCodec _Nonnull inCodec,     AudioBufferList * _Nonnull ioBufferList,     UInt32 * _Nonnull ioNumberPackets,     AudioStreamPacketDescription * _Nullable outPacketDescription,     UInt32 * _Nonnull outStatus ); ``` |

Modified [AudioCodecProduceOutputPackets()](https://developer.apple.com/documentation/audiotoolbox/1440558-audiocodecproduceoutputpackets)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecProduceOutputPackets (     AudioCodec inCodec,     void *outOutputData,     UInt32 *ioOutputDataByteSize,     UInt32 *ioNumberPackets,     AudioStreamPacketDescription *outPacketDescription,     UInt32 *outStatus ); ``` |
| To | ``` OSStatus AudioCodecProduceOutputPackets (     AudioCodec _Nonnull inCodec,     void * _Nonnull outOutputData,     UInt32 * _Nonnull ioOutputDataByteSize,     UInt32 * _Nonnull ioNumberPackets,     AudioStreamPacketDescription * _Nullable outPacketDescription,     UInt32 * _Nonnull outStatus ); ``` |

Modified [AudioCodecReset()](https://developer.apple.com/documentation/audiotoolbox/1439087-audiocodecreset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecReset (     AudioCodec inCodec ); ``` |
| To | ``` OSStatus AudioCodecReset (     AudioCodec _Nonnull inCodec ); ``` |

Modified [AudioCodecSetProperty()](https://developer.apple.com/documentation/audiotoolbox/1439355-audiocodecsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecSetProperty (     AudioCodec inCodec,     AudioCodecPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void *inPropertyData ); ``` |
| To | ``` OSStatus AudioCodecSetProperty (     AudioCodec _Nonnull inCodec,     AudioCodecPropertyID inPropertyID,     UInt32 inPropertyDataSize,     const void * _Nonnull inPropertyData ); ``` |

Modified [AudioCodecUninitialize()](https://developer.apple.com/documentation/audiotoolbox/1439079-audiocodecuninitialize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioCodecUninitialize (     AudioCodec inCodec ); ``` |
| To | ``` OSStatus AudioCodecUninitialize (     AudioCodec _Nonnull inCodec ); ``` |

Modified [MagicCookieInfo](https://developer.apple.com/documentation/audiotoolbox/magiccookieinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### AudioComponent.h

Added [AudioComponentFlags](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags)Added [AudioComponentGetIcon()](https://developer.apple.com/documentation/audiotoolbox/1410443-audiocomponentgeticon)Added [AudioComponentInstantiate()](https://developer.apple.com/documentation/audiotoolbox/1410517-audiocomponentinstantiate)Added [AudioComponentInstantiationOptions](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions)Added [AudioComponentValidate()](https://developer.apple.com/documentation/audiotoolbox/1410466-audiocomponentvalidate)Added [AudioComponentValidationResult](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult)Added #def AudioUnit_AudioComponent_hAdded [#def kAudioComponentConfigurationInfo_ValidationResult](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentconfigurationinfo_validationresult)Added [kAudioComponentFlag_CanLoadInProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/1410506-canloadinprocess)Added [kAudioComponentFlag_IsV3AudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_isv3audiounit)Added [kAudioComponentFlag_RequiresAsyncInstantiation](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_requiresasyncinstantiation)Added [kAudioComponentInstantiation_LoadInProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions/1410490-loadinprocess)Added [kAudioComponentInstantiation_LoadOutOfProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions/kaudiocomponentinstantiation_loadoutofprocess)Added [#def kAudioComponentValidationParameter_ForceValidation](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_forcevalidation)Added [#def kAudioComponentValidationParameter_TimeOut](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_timeout)Added [kAudioComponentValidationResult_Failed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/failed)Added [kAudioComponentValidationResult_Passed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/passed)Added [kAudioComponentValidationResult_TimedOut](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/timedout)Added [kAudioComponentValidationResult_UnauthorizedError_Init](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/unauthorizederror_init)Added [kAudioComponentValidationResult_UnauthorizedError_Open](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_unauthorizederror_open)Added [kAudioComponentValidationResult_Unknown](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_unknown)Modified [AudioComponentCopyConfigurationInfo()](https://developer.apple.com/documentation/audiotoolbox/1410525-audiocomponentcopyconfigurationi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioComponentCopyConfigurationInfo (     AudioComponent inComponent,     CFDictionaryRef *outConfigurationInfo ); ``` |
| To | ``` OSStatus AudioComponentCopyConfigurationInfo (     AudioComponent _Nonnull inComponent,     CFDictionaryRef  _Nullable * _Nonnull outConfigurationInfo ); ``` |

Modified [AudioComponentCopyName()](https://developer.apple.com/documentation/audiotoolbox/1410519-audiocomponentcopyname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioComponentCopyName (     AudioComponent inComponent,     CFStringRef *outName ); ``` |
| To | ``` OSStatus AudioComponentCopyName (     AudioComponent _Nonnull inComponent,     CFStringRef  _Nullable * _Nonnull outName ); ``` |

Modified [AudioComponentCount()](https://developer.apple.com/documentation/audiotoolbox/1410476-audiocomponentcount)

|  | Declaration |
| --- | --- |
| From | ``` UInt32 AudioComponentCount (     const AudioComponentDescription *inDesc ); ``` |
| To | ``` UInt32 AudioComponentCount (     const AudioComponentDescription * _Nonnull inDesc ); ``` |

Modified [AudioComponentFindNext()](https://developer.apple.com/documentation/audiotoolbox/1410445-audiocomponentfindnext)

|  | Declaration |
| --- | --- |
| From | ``` AudioComponent AudioComponentFindNext (     AudioComponent inComponent,     const AudioComponentDescription *inDesc ); ``` |
| To | ``` AudioComponent _Nullable AudioComponentFindNext (     AudioComponent _Nullable inComponent,     const AudioComponentDescription * _Nonnull inDesc ); ``` |

Modified [AudioComponentGetDescription()](https://developer.apple.com/documentation/audiotoolbox/1410523-audiocomponentgetdescription)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioComponentGetDescription (     AudioComponent inComponent,     AudioComponentDescription *outDesc ); ``` |
| To | ``` OSStatus AudioComponentGetDescription (     AudioComponent _Nonnull inComponent,     AudioComponentDescription * _Nonnull outDesc ); ``` |

Modified [AudioComponentGetVersion()](https://developer.apple.com/documentation/audiotoolbox/1410441-audiocomponentgetversion)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioComponentGetVersion (     AudioComponent inComponent,     UInt32 *outVersion ); ``` |
| To | ``` OSStatus AudioComponentGetVersion (     AudioComponent _Nonnull inComponent,     UInt32 * _Nonnull outVersion ); ``` |

Modified [AudioComponentInstanceCanDo()](https://developer.apple.com/documentation/audiotoolbox/1410504-audiocomponentinstancecando)

|  | Declaration |
| --- | --- |
| From | ``` Boolean AudioComponentInstanceCanDo (     AudioComponentInstance inInstance,     SInt16 inSelectorID ); ``` |
| To | ``` Boolean AudioComponentInstanceCanDo (     AudioComponentInstance _Nonnull inInstance,     SInt16 inSelectorID ); ``` |

Modified [AudioComponentInstanceDispose()](https://developer.apple.com/documentation/audiotoolbox/1410508-audiocomponentinstancedispose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioComponentInstanceDispose (     AudioComponentInstance inInstance ); ``` |
| To | ``` OSStatus AudioComponentInstanceDispose (     AudioComponentInstance _Nonnull inInstance ); ``` |

Modified [AudioComponentInstanceGetComponent()](https://developer.apple.com/documentation/audiotoolbox/1410447-audiocomponentinstancegetcompone)

|  | Declaration |
| --- | --- |
| From | ``` AudioComponent AudioComponentInstanceGetComponent (     AudioComponentInstance inInstance ); ``` |
| To | ``` AudioComponent _Nonnull AudioComponentInstanceGetComponent (     AudioComponentInstance _Nonnull inInstance ); ``` |

Modified [AudioComponentInstanceNew()](https://developer.apple.com/documentation/audiotoolbox/1410465-audiocomponentinstancenew)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioComponentInstanceNew (     AudioComponent inComponent,     AudioComponentInstance *outInstance ); ``` |
| To | ``` OSStatus AudioComponentInstanceNew (     AudioComponent _Nonnull inComponent,     AudioComponentInstance  _Nullable * _Nonnull outInstance ); ``` |

Modified [AudioComponentRegister()](https://developer.apple.com/documentation/audiotoolbox/1410487-audiocomponentregister)

|  | Declaration |
| --- | --- |
| From | ``` AudioComponent AudioComponentRegister (     const AudioComponentDescription *inDesc,     CFStringRef inName,     UInt32 inVersion,     AudioComponentFactoryFunction inFactory ); ``` |
| To | ``` AudioComponent _Nonnull AudioComponentRegister (     const AudioComponentDescription * _Nonnull inDesc,     CFStringRef _Nonnull inName,     UInt32 inVersion,     AudioComponentFactoryFunction _Nonnull inFactory ); ``` |

Modified [kAudioComponentFlag_SandboxSafe](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_sandboxsafe)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.8 |

#### AudioOutputUnit.h

Added #def AudioUnit_AudioOutputUnit_hModified [AudioOutputUnitStart()](https://developer.apple.com/documentation/audiotoolbox/1439763-audiooutputunitstart)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioOutputUnitStart (     AudioUnit ci ); ``` |
| To | ``` OSStatus AudioOutputUnitStart (     AudioUnit _Nonnull ci ); ``` |

Modified [AudioOutputUnitStop()](https://developer.apple.com/documentation/audiotoolbox/1440513-audiooutputunitstop)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AudioOutputUnitStop (     AudioUnit ci ); ``` |
| To | ``` OSStatus AudioOutputUnitStop (     AudioUnit _Nonnull ci ); ``` |

#### AudioUnitCarbonView.h

Added #def AudioUnit_AudioUnitCarbonView_hModified AudioUnitCarbonViewCreate()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### AudioUnitParameters.h

Added #def AudioUnit_AudioUnitParameters_h

#### AudioUnitProperties.h

Removed [#def GetAudioUnitParameterDisplayType](https://developer.apple.com/documentation/audiounit/audio_unit_properties/getaudiounitparameterdisplaytype)Removed [#def SetAudioUnitParameterDisplayType](https://developer.apple.com/documentation/audiounit/audio_unit_properties/setaudiounitparameterdisplaytype)Added [AU3DMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve)Added [AU3DMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags)Added #def AudioUnit_AudioUnitProperties_hAdded [AudioUnitParameterOptions](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions)Added [AUParameterMIDIMappingFlags](https://developer.apple.com/documentation/audiotoolbox/auparametermidimappingflags)Added [AUReverbRoomType](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype)Added [AUScheduledAudioSliceFlags](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags)Added [AUSpatializationAlgorithm](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm)Added [AUSpatialMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve)Added [AUSpatialMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags)Added [GetAudioUnitParameterDisplayType()](https://developer.apple.com/documentation/audiotoolbox/1440794-getaudiounitparameterdisplaytype)Added [#def kAudioUnitConfigurationInfo_BusCountWritable](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_buscountwritable)Added [#def kAudioUnitConfigurationInfo_SupportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_supportedchannellayouttags)Added [kAudioUnitProperty_ParametersForOverview](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parametersforoverview)Added [kAudioUnitProperty_RequestViewController](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_requestviewcontroller)Added [SetAudioUnitParameterDisplayType()](https://developer.apple.com/documentation/audiotoolbox/1440769-setaudiounitparameterdisplaytype)Modified [AUDistanceAttenuationData](https://developer.apple.com/documentation/audiotoolbox/audistanceattenuationdata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kAudioUnitProperty_3DMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_3dmixerattenuationcurve)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.7 | OS X 10.11 |

Modified [kAudioUnitProperty_3DMixerDistanceAtten](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_3dmixerdistanceatten)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.7 | OS X 10.11 |

Modified [kAudioUnitProperty_3DMixerDistanceParams](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_3dmixerdistanceparams)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.3 | -- |
| To | OS X 10.7 | OS X 10.11 |

Modified [kAudioUnitProperty_3DMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_3dmixerrenderingflags)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.7 | OS X 10.11 |

Modified [kAudioUnitProperty_DistanceAttenuationData](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_distanceattenuationdata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kAudioUnitProperty_DopplerShift](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_dopplershift)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.2 | -- |
| To | OS X 10.7 | OS X 10.11 |

Modified [kAudioUnitProperty_ReverbPreset](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_reverbpreset)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.5 | -- |
| To | OS X 10.7 | OS X 10.11 |

Modified [kAUVoiceIOProperty_VoiceProcessingQuality](https://developer.apple.com/documentation/audiotoolbox/1534074-anonymous/kauvoiceioproperty_voiceprocessingquality)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

#### AUParameters.h (Added)

Added [AUParameter](https://developer.apple.com/documentation/audiotoolbox/auparameter)Added [AUParameter.address](https://developer.apple.com/documentation/audiotoolbox/auparameter/1441037-address)Added [AUParameter.dependentParameters](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440649-dependentparameters)Added [AUParameter.flags](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439938-flags)Added [AUParameter.maxValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438427-maxvalue)Added [AUParameter.minValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440270-minvalue)Added [-[AUParameter setValue:originator:]](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439968-setvalue)Added [-[AUParameter setValue:originator:atHostTime:]](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438450-setvalue)Added [-[AUParameter stringFromValue:]](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440901-string)Added [AUParameter.unit](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440698-unit)Added [AUParameter.unitName](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438490-unitname)Added [AUParameter.value](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439301-value)Added [-[AUParameter valueFromString:]](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440495-value)Added [AUParameter.valueStrings](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438358-valuestrings)Added [AUParameterGroup](https://developer.apple.com/documentation/audiotoolbox/auparametergroup)Added [AUParameterGroup.allParameters](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439439-allparameters)Added [AUParameterGroup.children](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439325-children)Added [AUParameterNode](https://developer.apple.com/documentation/audiotoolbox/auparameternode)Added [AUParameterNode.displayName](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440278-displayname)Added [-[AUParameterNode displayNameWithLength:]](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439449-displaynamewithlength)Added [AUParameterNode.identifier](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440186-identifier)Added [AUParameterNode.keyPath](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439420-keypath)Added [-[AUParameterNode removeParameterObserver:]](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439314-removeparameterobserver)Added [-[AUParameterNode tokenByAddingParameterObserver:]](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440811-token)Added [-[AUParameterNode tokenByAddingParameterRecordingObserver:]](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440903-tokenbyaddingparameterrecordingo)Added [AUParameterTree](https://developer.apple.com/documentation/audiotoolbox/auparametertree)Added [-[AUParameterTree parameterWithAddress:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439569-parameterwithaddress)Added [-[AUParameterTree parameterWithID:scope:element:]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438918-parameterwithid)Added [AUParameterAddress](https://developer.apple.com/documentation/audiotoolbox/auparameteraddress)Added [AUParameterObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterobserver)Added [AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameterobservertoken)Added [AUParameterRecordingObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterrecordingobserver)Added [AURecordedParameterEvent](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent)Added [AUValue](https://developer.apple.com/documentation/audiotoolbox/auvalue)

#### MusicDevice.h

Added #def AudioUnit_MusicDevice_hModified [MusicDeviceMIDIEvent()](https://developer.apple.com/documentation/audiotoolbox/1439861-musicdevicemidievent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicDeviceMIDIEvent (     MusicDeviceComponent inUnit,     UInt32 inStatus,     UInt32 inData1,     UInt32 inData2,     UInt32 inOffsetSampleFrame ); ``` |
| To | ``` OSStatus MusicDeviceMIDIEvent (     MusicDeviceComponent _Nonnull inUnit,     UInt32 inStatus,     UInt32 inData1,     UInt32 inData2,     UInt32 inOffsetSampleFrame ); ``` |

Modified [MusicDevicePrepareInstrument()](https://developer.apple.com/documentation/audiotoolbox/1473487-musicdeviceprepareinstrument)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicDevicePrepareInstrument (     MusicDeviceComponent inUnit,     MusicDeviceInstrumentID inInstrument ); ``` |
| To | ``` OSStatus MusicDevicePrepareInstrument (     MusicDeviceComponent _Nonnull inUnit,     MusicDeviceInstrumentID inInstrument ); ``` |

Modified [MusicDeviceReleaseInstrument()](https://developer.apple.com/documentation/audiotoolbox/1473475-musicdevicereleaseinstrument)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicDeviceReleaseInstrument (     MusicDeviceComponent inUnit,     MusicDeviceInstrumentID inInstrument ); ``` |
| To | ``` OSStatus MusicDeviceReleaseInstrument (     MusicDeviceComponent _Nonnull inUnit,     MusicDeviceInstrumentID inInstrument ); ``` |

Modified [MusicDeviceStartNote()](https://developer.apple.com/documentation/audiotoolbox/1440960-musicdevicestartnote)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicDeviceStartNote (     MusicDeviceComponent inUnit,     MusicDeviceInstrumentID inInstrument,     MusicDeviceGroupID inGroupID,     NoteInstanceID *outNoteInstanceID,     UInt32 inOffsetSampleFrame,     const MusicDeviceNoteParams *inParams ); ``` |
| To | ``` OSStatus MusicDeviceStartNote (     MusicDeviceComponent _Nonnull inUnit,     MusicDeviceInstrumentID inInstrument,     MusicDeviceGroupID inGroupID,     NoteInstanceID * _Nonnull outNoteInstanceID,     UInt32 inOffsetSampleFrame,     const MusicDeviceNoteParams * _Nonnull inParams ); ``` |

Modified [MusicDeviceStopNote()](https://developer.apple.com/documentation/audiotoolbox/1440390-musicdevicestopnote)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicDeviceStopNote (     MusicDeviceComponent inUnit,     MusicDeviceGroupID inGroupID,     NoteInstanceID inNoteInstanceID,     UInt32 inOffsetSampleFrame ); ``` |
| To | ``` OSStatus MusicDeviceStopNote (     MusicDeviceComponent _Nonnull inUnit,     MusicDeviceGroupID inGroupID,     NoteInstanceID inNoteInstanceID,     UInt32 inOffsetSampleFrame ); ``` |

Modified [MusicDeviceSysEx()](https://developer.apple.com/documentation/audiotoolbox/1438996-musicdevicesysex)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus MusicDeviceSysEx (     MusicDeviceComponent inUnit,     const UInt8 *inData,     UInt32 inLength ); ``` |
| To | ``` OSStatus MusicDeviceSysEx (     MusicDeviceComponent _Nonnull inUnit,     const UInt8 * _Nonnull inData,     UInt32 inLength ); ``` |

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
