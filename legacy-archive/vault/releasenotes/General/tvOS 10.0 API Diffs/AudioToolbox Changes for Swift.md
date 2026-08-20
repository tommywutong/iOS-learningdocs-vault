---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/AudioToolbox.html
archived_at: '2026-07-18T02:57:32.865740Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# AudioToolbox Changes for Swift

### AudioToolbox

Removed [MusicSequenceFileFlags.Default](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags/kmusicsequencefileflags_default)Added [AUAudioUnit.channelMap](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/2143054-channelmap)Added [AUAudioUnit.supportsMPE](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1823489-supportsmpe)Added [AUMIDIEvent.init(next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8, length: UInt16, cable: UInt8, data: (UInt8, UInt8, UInt8))](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1438938-init)Added [AUParameter.setValue(_: AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](https://developer.apple.com/documentation/audiotoolbox/auparameter/1644190-setvalue)Added [AUParameterAutomationEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationevent)Added [AUParameterAutomationEvent.address](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationevent/1644193-address)Added [AUParameterAutomationEvent.eventType](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationevent/1644185-eventtype)Added [AUParameterAutomationEvent.hostTime](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationevent/1644194-hosttime)Added [AUParameterAutomationEvent.init()](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationevent/1645624-init)Added [AUParameterAutomationEvent.init(hostTime: UInt64, address: AUParameterAddress, value: AUValue, eventType: AUParameterAutomationEventType, reserved: UInt64)](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationevent/1645633-init)Added [AUParameterAutomationEvent.reserved](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationevent/1644187-reserved)Added [AUParameterAutomationEvent.value](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationevent/1644191-value)Added [AUParameterAutomationEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationeventtype)Added [AUParameterAutomationEventType.release](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationeventtype/auparameterautomationeventtyperelease)Added [AUParameterAutomationEventType.touch](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationeventtype/auparameterautomationeventtypetouch)Added [AUParameterAutomationEventType.value](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationeventtype/auparameterautomationeventtypevalue)Added [AUParameterEvent.init(next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: (UInt8, UInt8, UInt8), rampDurationSampleFrames: AUAudioFrameCount, parameterAddress: AUParameterAddress, value: AUValue)](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1439312-init)Added [AUParameterNode.token(byAddingParameterAutomationObserver: AudioToolbox.AUParameterAutomationObserver) -> AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1644183-token)Added [AUPreset.init()](https://developer.apple.com/documentation/audiotoolbox/aupreset/1645581-init)Added [AUPreset.init(presetNumber: Int32, presetName: Unmanaged<CFString>?)](https://developer.apple.com/documentation/audiotoolbox/aupreset/1645768-init)Added [AURenderCallbackStruct.init()](https://developer.apple.com/documentation/audiotoolbox/aurendercallbackstruct/1645769-init)Added [AURenderCallbackStruct.init(inputProc: AudioToolbox.AURenderCallback?, inputProcRefCon: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/audiotoolbox/aurendercallbackstruct/1645460-init)Added [AURenderEventHeader.init(next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8)](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1438623-init)Added [HostCallbackInfo.init(hostUserData: UnsafeMutableRawPointer?, beatAndTempoProc: AudioToolbox.HostCallback_GetBeatAndTempo?, musicalTimeLocationProc: AudioToolbox.HostCallback_GetMusicalTimeLocation?, transportStateProc: AudioToolbox.HostCallback_GetTransportState?, transportStateProc2: AudioToolbox.HostCallback_GetTransportState2?)](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439353-init)Added [AudioQueueInputCallbackBlock](https://developer.apple.com/documentation/audiotoolbox/audioqueueinputcallbackblock)Added [AudioQueueNewInputWithDispatchQueue(_: UnsafeMutablePointer<AudioQueueRef?>, _: UnsafePointer<AudioStreamBasicDescription>, _: UInt32, _: DispatchQueue, _: AudioToolbox.AudioQueueInputCallbackBlock) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503196-audioqueuenewinputwithdispatchqu)Added [AudioQueueNewOutputWithDispatchQueue(_: UnsafeMutablePointer<AudioQueueRef?>, _: UnsafePointer<AudioStreamBasicDescription>, _: UInt32, _: DispatchQueue, _: AudioToolbox.AudioQueueOutputCallbackBlock) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503124-audioqueuenewoutputwithdispatchq)Added [AudioQueueOutputCallbackBlock](https://developer.apple.com/documentation/audiotoolbox/audioqueueoutputcallbackblock)Added [AUParameterAutomationObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterautomationobserver)Added [kAudioConverterSampleRateConverterComplexity_MinimumPhase](https://developer.apple.com/documentation/audiotoolbox/1559923-sample_rate_conversion_complexit/kaudioconvertersamplerateconvertercomplexity_minimumphase)Added [kAudioQueueErr_CannotStartYet](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_cannotstartyet)Added [kAudioServicesSystemSoundExceededMaximumDurationError](https://developer.apple.com/documentation/audiotoolbox/kaudioservicessystemsoundexceededmaximumdurationerror)Added [kAudioUnitErr_RenderTimeout](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_rendertimeout)Added [kAudioUnitProperty_InputAnchorTimeStamp](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_inputanchortimestamp)Added [kAudioUnitProperty_SupportsMPE](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_supportsmpe)Added [MIDIEndpointRef](https://developer.apple.com/documentation/audiotoolbox/midiendpointref)Modified [AU3DMixerAttenuationCurve [enum]](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Exponential](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_exponential)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Inverse](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_inverse)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Linear](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_linear)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerAttenuationCurve.k3DMixerAttenuationCurve_Power](https://developer.apple.com/documentation/audiotoolbox/au3dmixerattenuationcurve/k3dmixerattenuationcurve_power)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerRenderingFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` struct AU3DMixerRenderingFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var k3DMixerRenderingFlags_InterAuralDelay: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_DopplerShift: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_DistanceAttenuation: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_DistanceFilter: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_DistanceDiffusion: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_LinearDistanceAttenuation: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_ConstantReverbBlend: AU3DMixerRenderingFlags { get } } ``` | OptionSetType | AudioUnit |
| To | ``` struct AU3DMixerRenderingFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var k3DMixerRenderingFlags_InterAuralDelay: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_DopplerShift: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_DistanceAttenuation: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_DistanceFilter: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_DistanceDiffusion: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_LinearDistanceAttenuation: AU3DMixerRenderingFlags { get }     static var k3DMixerRenderingFlags_ConstantReverbBlend: AU3DMixerRenderingFlags { get }     func intersect(_ other: AU3DMixerRenderingFlags) -> AU3DMixerRenderingFlags     func exclusiveOr(_ other: AU3DMixerRenderingFlags) -> AU3DMixerRenderingFlags     mutating func unionInPlace(_ other: AU3DMixerRenderingFlags)     mutating func intersectInPlace(_ other: AU3DMixerRenderingFlags)     mutating func exclusiveOrInPlace(_ other: AU3DMixerRenderingFlags)     func isSubsetOf(_ other: AU3DMixerRenderingFlags) -> Bool     func isDisjointWith(_ other: AU3DMixerRenderingFlags) -> Bool     func isSupersetOf(_ other: AU3DMixerRenderingFlags) -> Bool     mutating func subtractInPlace(_ other: AU3DMixerRenderingFlags)     func isStrictSupersetOf(_ other: AU3DMixerRenderingFlags) -> Bool     func isStrictSubsetOf(_ other: AU3DMixerRenderingFlags) -> Bool } extension AU3DMixerRenderingFlags {     func union(_ other: AU3DMixerRenderingFlags) -> AU3DMixerRenderingFlags     func intersection(_ other: AU3DMixerRenderingFlags) -> AU3DMixerRenderingFlags     func symmetricDifference(_ other: AU3DMixerRenderingFlags) -> AU3DMixerRenderingFlags } extension AU3DMixerRenderingFlags {     func contains(_ member: AU3DMixerRenderingFlags) -> Bool     mutating func insert(_ newMember: AU3DMixerRenderingFlags) -> (inserted: Bool, memberAfterInsert: AU3DMixerRenderingFlags)     mutating func remove(_ member: AU3DMixerRenderingFlags) -> AU3DMixerRenderingFlags?     mutating func update(with newMember: AU3DMixerRenderingFlags) -> AU3DMixerRenderingFlags? } extension AU3DMixerRenderingFlags {     convenience init()     mutating func formUnion(_ other: AU3DMixerRenderingFlags)     mutating func formIntersection(_ other: AU3DMixerRenderingFlags)     mutating func formSymmetricDifference(_ other: AU3DMixerRenderingFlags) } extension AU3DMixerRenderingFlags {     convenience init<S : Sequence where S.Iterator.Element == AU3DMixerRenderingFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AU3DMixerRenderingFlags...)     mutating func subtract(_ other: AU3DMixerRenderingFlags)     func isSubset(of other: AU3DMixerRenderingFlags) -> Bool     func isSuperset(of other: AU3DMixerRenderingFlags) -> Bool     func isDisjoint(with other: AU3DMixerRenderingFlags) -> Bool     func subtracting(_ other: AU3DMixerRenderingFlags) -> AU3DMixerRenderingFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AU3DMixerRenderingFlags) -> Bool     func isStrictSubset(of other: AU3DMixerRenderingFlags) -> Bool } ``` | OptionSet | AudioToolbox |

Modified [AU3DMixerRenderingFlags.init(rawValue: UInt32)](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/1440166-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_ConstantReverbBlend](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_constantreverbblend)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_distanceattenuation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceDiffusion](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/1439784-k3dmixerrenderingflags_distanced)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DistanceFilter](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/1440885-k3dmixerrenderingflags_distancef)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_DopplerShift](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_dopplershift)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_InterAuralDelay](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_interauraldelay)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AU3DMixerRenderingFlags.k3DMixerRenderingFlags_LinearDistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/au3dmixerrenderingflags/k3dmixerrenderingflags_lineardistanceattenuation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounit)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class AUAudioUnit : NSObject {     convenience init()     init(componentDescription componentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions) throws     convenience init(componentDescription componentDescription: AudioComponentDescription) throws     class func instantiateWithComponentDescription(_ componentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions, completionHandler completionHandler: (AUAudioUnit?, NSError?) -> Void)     var componentDescription: AudioComponentDescription { get }     var component: AudioComponent { get }     var componentName: String? { get }     var audioUnitName: String? { get }     var manufacturerName: String? { get }     var componentVersion: UInt32 { get }     func allocateRenderResources() throws     func deallocateRenderResources()     var renderResourcesAllocated: Bool { get }     func reset()     var inputBusses: AUAudioUnitBusArray { get }     var outputBusses: AUAudioUnitBusArray { get }     var renderBlock: AURenderBlock { get }     var scheduleParameterBlock: AUScheduleParameterBlock { get }     func tokenByAddingRenderObserver(_ observer: AURenderObserver) -> Int     func removeRenderObserver(_ token: Int)     var maximumFramesToRender: AUAudioFrameCount     var parameterTree: AUParameterTree? { get }     func parametersForOverviewWithCount(_ count: Int) -> [NSNumber]     var allParameterValues: Bool { get }     var musicDeviceOrEffect: Bool { get }     var virtualMIDICableCount: Int { get }     var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock? { get }     var fullState: [String : AnyObject]?     var fullStateForDocument: [String : AnyObject]?     var factoryPresets: [AUAudioUnitPreset]? { get }     var currentPreset: AUAudioUnitPreset?     var latency: NSTimeInterval { get }     var tailTime: NSTimeInterval { get }     var renderQuality: Int     var shouldBypassEffect: Bool     var canProcessInPlace: Bool { get }     var renderingOffline: Bool     var channelCapabilities: [NSNumber]? { get }     var musicalContextBlock: AUHostMusicalContextBlock?     var transportStateBlock: AUHostTransportStateBlock?     var contextName: String? } extension AUAudioUnit {     var canPerformInput: Bool { get }     var canPerformOutput: Bool { get }     var inputEnabled: Bool     var outputEnabled: Bool     var outputProvider: AURenderPullInputBlock?     var inputHandler: AUInputHandler?     func startHardware() throws     func stopHardware() } extension AUAudioUnit {     class func registerSubclass(_ cls: AnyClass, asComponentDescription componentDescription: AudioComponentDescription, name name: String, version version: UInt32)     var internalRenderBlock: AUInternalRenderBlock { get }     func shouldChangeToFormat(_ format: AVAudioFormat, forBus bus: AUAudioUnitBus) -> Bool     func setRenderResourcesAllocated(_ flag: Bool) } ``` | -- | AudioUnit |
| To | ``` class AUAudioUnit : NSObject {     convenience init()     init(componentDescription componentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions = []) throws     convenience init(componentDescription componentDescription: AudioComponentDescription) throws     class func instantiate(with componentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions = [], completionHandler completionHandler: @escaping (AUAudioUnit?, Error?) -> Swift.Void)     var componentDescription: AudioComponentDescription { get }     var component: AudioComponent { get }     var componentName: String? { get }     var audioUnitName: String? { get }     var manufacturerName: String? { get }     var componentVersion: UInt32 { get }     func allocateRenderResources() throws     func deallocateRenderResources()     var renderResourcesAllocated: Bool { get }     func reset()     var inputBusses: AUAudioUnitBusArray { get }     var outputBusses: AUAudioUnitBusArray { get }     var renderBlock: AudioToolbox.AURenderBlock { get }     var scheduleParameterBlock: AudioToolbox.AUScheduleParameterBlock { get }     func token(byAddingRenderObserver observer: AudioToolbox.AURenderObserver) -> Int     func removeRenderObserver(_ token: Int)     var maximumFramesToRender: AUAudioFrameCount     var parameterTree: AUParameterTree? { get }     func parametersForOverview(withCount count: Int) -> [NSNumber]     var allParameterValues: Bool { get }     var isMusicDeviceOrEffect: Bool { get }     var virtualMIDICableCount: Int { get }     var scheduleMIDIEventBlock: AudioToolbox.AUScheduleMIDIEventBlock? { get }     var fullState: [String : Any]?     var fullStateForDocument: [String : Any]?     var factoryPresets: [AUAudioUnitPreset]? { get }     var currentPreset: AUAudioUnitPreset?     var latency: TimeInterval { get }     var tailTime: TimeInterval { get }     var renderQuality: Int     var shouldBypassEffect: Bool     var canProcessInPlace: Bool { get }     var isRenderingOffline: Bool     var channelCapabilities: [NSNumber]? { get }     var musicalContextBlock: AudioToolbox.AUHostMusicalContextBlock?     var transportStateBlock: AudioToolbox.AUHostTransportStateBlock?     var contextName: String?     var supportsMPE: Bool { get }     var channelMap: [NSNumber]?     class func registerSubclass(_ cls: Swift.AnyClass, as componentDescription: AudioComponentDescription, name name: String, version version: UInt32)     var internalRenderBlock: AudioToolbox.AUInternalRenderBlock { get }     func shouldChange(to format: AVAudioFormat, for bus: AUAudioUnitBus) -> Bool     func setRenderResourcesAllocated(_ flag: Bool)     var canPerformInput: Bool { get }     var canPerformOutput: Bool { get }     var isInputEnabled: Bool     var isOutputEnabled: Bool     var outputProvider: AudioToolbox.AURenderPullInputBlock?     var inputHandler: AudioToolbox.AUInputHandler?     func startHardware() throws     func stopHardware()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AUAudioUnit : CVarArg { } extension AUAudioUnit : Equatable, Hashable {     var hashValue: Int { get } } extension AUAudioUnit {     var canPerformInput: Bool { get }     var canPerformOutput: Bool { get }     var isInputEnabled: Bool     var isOutputEnabled: Bool     var outputProvider: AudioToolbox.AURenderPullInputBlock?     var inputHandler: AudioToolbox.AUInputHandler?     func startHardware() throws     func stopHardware() } extension AUAudioUnit {     class func registerSubclass(_ cls: Swift.AnyClass, as componentDescription: AudioComponentDescription, name name: String, version version: UInt32)     var internalRenderBlock: AudioToolbox.AUInternalRenderBlock { get }     func shouldChange(to format: AVAudioFormat, for bus: AUAudioUnitBus) -> Bool     func setRenderResourcesAllocated(_ flag: Bool) } ``` | CVarArg, Equatable, Hashable | AudioToolbox |

Modified [AUAudioUnit.allocateRenderResources() throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387620-allocaterenderresources)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.allParameterValues](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387679-allparametervalues)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.audioUnitName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387640-audiounitname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.canPerformInput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387551-canperforminput)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.canPerformOutput](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387656-canperformoutput)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.canProcessInPlace](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387583-canprocessinplace)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.channelCapabilities](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387685-channelcapabilities)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.component](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387535-component)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.componentDescription](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387568-componentdescription)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.componentName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387566-componentname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.componentVersion](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387555-componentversion)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.contextName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387553-contextname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.currentPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387668-currentpreset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.deallocateRenderResources()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387612-deallocaterenderresources)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.factoryPresets](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387526-factorypresets)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.fullState](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387500-fullstate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var fullState: [String : AnyObject]? ``` | AudioUnit |
| To | ``` var fullState: [String : Any]? ``` | AudioToolbox |

Modified [AUAudioUnit.fullStateForDocument](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387630-fullstatefordocument)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var fullStateForDocument: [String : AnyObject]? ``` | AudioUnit |
| To | ``` var fullStateForDocument: [String : Any]? ``` | AudioToolbox |

Modified [AUAudioUnit.init(componentDescription: AudioComponentDescription) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387570-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.init(componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387664-initwithcomponentdescription)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init(componentDescription componentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions) throws ``` | AudioUnit |
| To | ``` init(componentDescription componentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions = []) throws ``` | AudioToolbox |

Modified [AUAudioUnit.inputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387636-inputbusses)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.inputHandler](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387616-inputhandler)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var inputHandler: AUInputHandler? ``` | AudioUnit |
| To | ``` var inputHandler: AudioToolbox.AUInputHandler? ``` | AudioToolbox |

Modified [AUAudioUnit.instantiate(with: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AUAudioUnit?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387606-instantiate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func instantiateWithComponentDescription(_ componentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions, completionHandler completionHandler: (AUAudioUnit?, NSError?) -> Void) ``` | AudioUnit |
| To | ``` class func instantiate(with componentDescription: AudioComponentDescription, options options: AudioComponentInstantiationOptions = [], completionHandler completionHandler: @escaping (AUAudioUnit?, Error?) -> Swift.Void) ``` | AudioToolbox |

Modified [AUAudioUnit.internalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439864-internalrenderblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var internalRenderBlock: AUInternalRenderBlock { get } ``` | AudioUnit |
| To | ``` var internalRenderBlock: AudioToolbox.AUInternalRenderBlock { get } ``` | AudioToolbox |

Modified [AUAudioUnit.isInputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387660-inputenabled)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var inputEnabled: Bool ``` | AudioUnit |
| To | ``` var isInputEnabled: Bool ``` | AudioToolbox |

Modified [AUAudioUnit.isMusicDeviceOrEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387497-ismusicdeviceoreffect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var musicDeviceOrEffect: Bool { get } ``` | AudioUnit |
| To | ``` var isMusicDeviceOrEffect: Bool { get } ``` | AudioToolbox |

Modified [AUAudioUnit.isOutputEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387646-outputenabled)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var outputEnabled: Bool ``` | AudioUnit |
| To | ``` var isOutputEnabled: Bool ``` | AudioToolbox |

Modified [AUAudioUnit.isRenderingOffline](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387578-renderingoffline)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var renderingOffline: Bool ``` | AudioUnit |
| To | ``` var isRenderingOffline: Bool ``` | AudioToolbox |

Modified [AUAudioUnit.latency](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387675-latency)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var latency: NSTimeInterval { get } ``` | AudioUnit |
| To | ``` var latency: TimeInterval { get } ``` | AudioToolbox |

Modified [AUAudioUnit.manufacturerName](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387681-manufacturername)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.maximumFramesToRender](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387654-maximumframestorender)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.musicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387669-musicalcontextblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var musicalContextBlock: AUHostMusicalContextBlock? ``` | AudioUnit |
| To | ``` var musicalContextBlock: AudioToolbox.AUHostMusicalContextBlock? ``` | AudioToolbox |

Modified [AUAudioUnit.outputBusses](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387503-outputbusses)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.outputProvider](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387596-outputprovider)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var outputProvider: AURenderPullInputBlock? ``` | AudioUnit |
| To | ``` var outputProvider: AudioToolbox.AURenderPullInputBlock? ``` | AudioToolbox |

Modified [AUAudioUnit.parametersForOverview(withCount: Int) -> [NSNumber]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387549-parametersforoverview)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func parametersForOverviewWithCount(_ count: Int) -> [NSNumber] ``` | AudioUnit |
| To | ``` func parametersForOverview(withCount count: Int) -> [NSNumber] ``` | AudioToolbox |

Modified [AUAudioUnit.parameterTree](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387650-parametertree)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.registerSubclass(_: Swift.AnyClass, as: AudioComponentDescription, name: String, version: UInt32) [class]](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1438315-registersubclass)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func registerSubclass(_ cls: AnyClass, asComponentDescription componentDescription: AudioComponentDescription, name name: String, version version: UInt32) ``` | AudioUnit |
| To | ``` class func registerSubclass(_ cls: Swift.AnyClass, as componentDescription: AudioComponentDescription, name name: String, version version: UInt32) ``` | AudioToolbox |

Modified [AUAudioUnit.removeRenderObserver(_: Int)](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387564-removerenderobserver)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.renderBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387687-renderblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var renderBlock: AURenderBlock { get } ``` | AudioUnit |
| To | ``` var renderBlock: AudioToolbox.AURenderBlock { get } ``` | AudioToolbox |

Modified [AUAudioUnit.renderQuality](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387648-renderquality)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.renderResourcesAllocated](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387618-renderresourcesallocated)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.reset()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387658-reset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.scheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387576-schedulemidieventblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock? { get } ``` | AudioUnit |
| To | ``` var scheduleMIDIEventBlock: AudioToolbox.AUScheduleMIDIEventBlock? { get } ``` | AudioToolbox |

Modified [AUAudioUnit.scheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387677-scheduleparameterblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var scheduleParameterBlock: AUScheduleParameterBlock { get } ``` | AudioUnit |
| To | ``` var scheduleParameterBlock: AudioToolbox.AUScheduleParameterBlock { get } ``` | AudioToolbox |

Modified [AUAudioUnit.setRenderResourcesAllocated(_: Bool)](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1440830-setrenderresourcesallocated)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.shouldBypassEffect](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387545-shouldbypasseffect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1439999-shouldchange)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func shouldChangeToFormat(_ format: AVAudioFormat, forBus bus: AUAudioUnitBus) -> Bool ``` | AudioUnit |
| To | ``` func shouldChange(to format: AVAudioFormat, for bus: AUAudioUnitBus) -> Bool ``` | AudioToolbox |

Modified [AUAudioUnit.startHardware() throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387581-starthardware)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.stopHardware()](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387642-stophardware)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnit.tailTime](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387614-tailtime)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var tailTime: NSTimeInterval { get } ``` | AudioUnit |
| To | ``` var tailTime: TimeInterval { get } ``` | AudioToolbox |

Modified [AUAudioUnit.token(byAddingRenderObserver: AudioToolbox.AURenderObserver) -> Int](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387509-token)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func tokenByAddingRenderObserver(_ observer: AURenderObserver) -> Int ``` | AudioUnit |
| To | ``` func token(byAddingRenderObserver observer: AudioToolbox.AURenderObserver) -> Int ``` | AudioToolbox |

Modified [AUAudioUnit.transportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387559-transportstateblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var transportStateBlock: AUHostTransportStateBlock? ``` | AudioUnit |
| To | ``` var transportStateBlock: AudioToolbox.AUHostTransportStateBlock? ``` | AudioToolbox |

Modified [AUAudioUnit.virtualMIDICableCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/1387666-virtualmidicablecount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class AUAudioUnitBus : NSObject {     var format: AVAudioFormat { get }     func setFormat(_ format: AVAudioFormat) throws     var enabled: Bool     var name: String?     var index: Int { get }     var busType: AUAudioUnitBusType { get }     unowned(unsafe) var ownerAudioUnit: AUAudioUnit { get }     var supportedChannelLayoutTags: [NSNumber]? { get }     var contextPresentationLatency: NSTimeInterval } extension AUAudioUnitBus {     init(format format: AVAudioFormat) throws     var supportedChannelCounts: [NSNumber]?     var maximumChannelCount: AUAudioChannelCount } ``` | -- | AudioUnit |
| To | ``` class AUAudioUnitBus : NSObject {     var format: AVAudioFormat { get }     func setFormat(_ format: AVAudioFormat) throws     var isEnabled: Bool     var name: String?     var index: Int { get }     var busType: AUAudioUnitBusType { get }     unowned(unsafe) var ownerAudioUnit: AUAudioUnit { get }     var supportedChannelLayoutTags: [NSNumber]? { get }     var contextPresentationLatency: TimeInterval     init(format format: AVAudioFormat) throws     var supportedChannelCounts: [NSNumber]?     var maximumChannelCount: AUAudioChannelCount     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AUAudioUnitBus : CVarArg { } extension AUAudioUnitBus : Equatable, Hashable {     var hashValue: Int { get } } extension AUAudioUnitBus {     init(format format: AVAudioFormat) throws     var supportedChannelCounts: [NSNumber]?     var maximumChannelCount: AUAudioChannelCount } ``` | CVarArg, Equatable, Hashable | AudioToolbox |

Modified [AUAudioUnitBus.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387524-bustype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.contextPresentationLatency](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387547-contextpresentationlatency)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var contextPresentationLatency: NSTimeInterval ``` | AudioUnit |
| To | ``` var contextPresentationLatency: TimeInterval ``` | AudioToolbox |

Modified [AUAudioUnitBus.format](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387689-format)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.index](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387557-index)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.init(format: AVAudioFormat) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440039-initwithformat)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.isEnabled](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387634-isenabled)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var enabled: Bool ``` | AudioUnit |
| To | ``` var isEnabled: Bool ``` | AudioToolbox |

Modified [AUAudioUnitBus.maximumChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1439855-maximumchannelcount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387514-name)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387638-owneraudiounit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.setFormat(_: AVAudioFormat) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387644-setformat)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.supportedChannelCounts](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1440352-supportedchannelcounts)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBus.supportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/1387622-supportedchannellayouttags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBusArray](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class AUAudioUnitBusArray : NSObject, NSFastEnumeration {     convenience init()     init(audioUnit owner: AUAudioUnit, busType busType: AUAudioUnitBusType, busses busArray: [AUAudioUnitBus])     convenience init(audioUnit owner: AUAudioUnit, busType busType: AUAudioUnitBusType)     var count: Int { get }     subscript (_ index: Int) -> AUAudioUnitBus { get }     func objectAtIndexedSubscript(_ index: Int) -> AUAudioUnitBus     var countChangeable: Bool { get }     func setBusCount(_ count: Int) throws     func addObserverToAllBusses(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserverFromAllBusses(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     unowned(unsafe) var ownerAudioUnit: AUAudioUnit { get }     var busType: AUAudioUnitBusType { get } } extension AUAudioUnitBusArray {     func replaceBusses(_ busArray: [AUAudioUnitBus]) } ``` | NSFastEnumeration | AudioUnit |
| To | ``` class AUAudioUnitBusArray : NSObject, NSFastEnumeration {     convenience init()     init(audioUnit owner: AUAudioUnit, busType busType: AUAudioUnitBusType, busses busArray: [AUAudioUnitBus])     convenience init(audioUnit owner: AUAudioUnit, busType busType: AUAudioUnitBusType)     var count: Int { get }     subscript(_ index: Int) -> AUAudioUnitBus { get }     func objectAtIndexedSubscript(_ index: Int) -> AUAudioUnitBus     var isCountChangeable: Bool { get }     func setBusCount(_ count: Int) throws     func addObserver(toAllBusses observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(fromAllBusses observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     unowned(unsafe) var ownerAudioUnit: AUAudioUnit { get }     var busType: AUAudioUnitBusType { get }     func replaceBusses(_ busArray: [AUAudioUnitBus])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AUAudioUnitBusArray : CVarArg { } extension AUAudioUnitBusArray : Equatable, Hashable {     var hashValue: Int { get } } extension AUAudioUnitBusArray {     func replaceBusses(_ busArray: [AUAudioUnitBus]) } ``` | CVarArg, Equatable, Hashable, NSFastEnumeration | AudioToolbox |

Modified [AUAudioUnitBusArray.addObserver(toAllBusses: NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387520-addobservertoallbusses)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func addObserverToAllBusses(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>) ``` | AudioUnit |
| To | ``` func addObserver(toAllBusses observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?) ``` | AudioToolbox |

Modified [AUAudioUnitBusArray.busType](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387671-bustype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBusArray.count](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387673-count)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBusArray.init(audioUnit: AUAudioUnit, busType: AUAudioUnitBusType)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387662-initwithaudiounit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBusArray.init(audioUnit: AUAudioUnit, busType: AUAudioUnitBusType, busses: [AUAudioUnitBus])](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387516-initwithaudiounit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBusArray.isCountChangeable](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387537-countchangeable)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var countChangeable: Bool { get } ``` | AudioUnit |
| To | ``` var isCountChangeable: Bool { get } ``` | AudioToolbox |

Modified [AUAudioUnitBusArray.ownerAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387510-owneraudiounit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBusArray.removeObserver(fromAllBusses: NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387505-removeobserverfromallbusses)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func removeObserverFromAllBusses(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>) ``` | AudioUnit |
| To | ``` func removeObserver(fromAllBusses observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?) ``` | AudioToolbox |

Modified [AUAudioUnitBusArray.replaceBusses(_: [AUAudioUnitBus])](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1440520-replacebusses)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBusArray.setBusCount(_: Int) throws](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387598-setbuscount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitBusArray.subscript(_: Int) -> AUAudioUnitBus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/1387507-subscript)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` subscript (_ index: Int) -> AUAudioUnitBus { get } ``` | AudioUnit |
| To | ``` subscript(_ index: Int) -> AUAudioUnitBus { get } ``` | AudioToolbox |

Modified [AUAudioUnitBusType [enum]](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AUAudioUnitBusType : Int {     case Input     case Output } ``` | AudioUnit |
| To | ``` enum AUAudioUnitBusType : Int {     case input     case output } ``` | AudioToolbox |

Modified [AUAudioUnitBusType.input](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/input)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Input ``` | AudioUnit |
| To | ``` case input ``` | AudioToolbox |

Modified [AUAudioUnitBusType.output](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbustype/output)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Output ``` | AudioUnit |
| To | ``` case output ``` | AudioToolbox |

Modified [AUAudioUnitFactory](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` protocol AUAudioUnitFactory : NSExtensionRequestHandling {     func createAudioUnitWithComponentDescription(_ desc: AudioComponentDescription) throws -> AUAudioUnit } ``` | AudioUnit |
| To | ``` protocol AUAudioUnitFactory : NSExtensionRequestHandling {     func createAudioUnit(with desc: AudioComponentDescription) throws -> AUAudioUnit } ``` | AudioToolbox |

Modified [AUAudioUnitFactory.createAudioUnit(with: AudioComponentDescription) throws -> AUAudioUnit](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory/1440321-createaudiounitwithcomponentdesc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func createAudioUnitWithComponentDescription(_ desc: AudioComponentDescription) throws -> AUAudioUnit ``` | AudioUnit |
| To | ``` func createAudioUnit(with desc: AudioComponentDescription) throws -> AUAudioUnit ``` | AudioToolbox |

Modified [AUAudioUnitPreset](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class AUAudioUnitPreset : NSObject, NSSecureCoding {     var number: Int     var name: String } ``` | NSSecureCoding | AudioUnit |
| To | ``` class AUAudioUnitPreset : NSObject, NSSecureCoding {     var number: Int     var name: String     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AUAudioUnitPreset : CVarArg { } extension AUAudioUnitPreset : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding | AudioToolbox |

Modified [AUAudioUnitPreset.name](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387587-name)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitPreset.number](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset/1387626-number)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitV2Bridge](https://developer.apple.com/documentation/audiotoolbox/auaudiounitv2bridge)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class AUAudioUnitV2Bridge : AUAudioUnit { } ``` | -- | AudioUnit |
| To | ``` class AUAudioUnitV2Bridge : AUAudioUnit {     class func registerSubclass(_ cls: AnyClass, as componentDescription: AudioComponentDescription, name name: String, version version: UInt32)     var internalRenderBlock: AUInternalRenderBlock { get }     func shouldChange(to format: AVAudioFormat, for bus: AUAudioUnitBus) -> Bool     func setRenderResourcesAllocated(_ flag: Bool)     var canPerformInput: Bool { get }     var canPerformOutput: Bool { get }     var isInputEnabled: Bool     var isOutputEnabled: Bool     var outputProvider: AURenderPullInputBlock?     var inputHandler: AUInputHandler?     func startHardware() throws     func stopHardware()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AUAudioUnitV2Bridge : CVarArg { } extension AUAudioUnitV2Bridge : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | AudioToolbox |

Modified [AUChannelInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/auchannelinfo)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUChannelInfo.inChannels](https://developer.apple.com/documentation/audiotoolbox/auchannelinfo/1440887-inchannels)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUChannelInfo.init()](https://developer.apple.com/documentation/audiotoolbox/auchannelinfo/1438691-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUChannelInfo.init(inChannels: Int16, outChannels: Int16)](https://developer.apple.com/documentation/audiotoolbox/auchannelinfo/1438329-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUChannelInfo.outChannels](https://developer.apple.com/documentation/audiotoolbox/auchannelinfo/1439688-outchannels)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUDependentParameter [struct]](https://developer.apple.com/documentation/audiotoolbox/audependentparameter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUDependentParameter.init()](https://developer.apple.com/documentation/audiotoolbox/audependentparameter/1439320-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUDependentParameter.init(mScope: AudioUnitScope, mParameterID: AudioUnitParameterID)](https://developer.apple.com/documentation/audiotoolbox/audependentparameter/1440937-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUDependentParameter.mParameterID](https://developer.apple.com/documentation/audiotoolbox/audependentparameter/1440777-mparameterid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUDependentParameter.mScope](https://developer.apple.com/documentation/audiotoolbox/audependentparameter/1439343-mscope)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioBalanceFadeType [enum]](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype)

|  | Declaration |
| --- | --- |
| From | ``` enum AudioBalanceFadeType : UInt32 {     case MaxUnityGain     case EqualPower } ``` |
| To | ``` enum AudioBalanceFadeType : UInt32 {     case maxUnityGain     case equalPower } ``` |

Modified [AudioBalanceFadeType.equalPower](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype/equalpower)

|  | Declaration |
| --- | --- |
| From | ``` case EqualPower ``` |
| To | ``` case equalPower ``` |

Modified [AudioBalanceFadeType.maxUnityGain](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype/maxunitygain)

|  | Declaration |
| --- | --- |
| From | ``` case MaxUnityGain ``` |
| To | ``` case maxUnityGain ``` |

Modified [AudioBytePacketTranslationFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslationflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioBytePacketTranslationFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var BytePacketTranslationFlag_IsEstimate: AudioBytePacketTranslationFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioBytePacketTranslationFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var bytePacketTranslationFlag_IsEstimate: AudioBytePacketTranslationFlags { get }     func intersect(_ other: AudioBytePacketTranslationFlags) -> AudioBytePacketTranslationFlags     func exclusiveOr(_ other: AudioBytePacketTranslationFlags) -> AudioBytePacketTranslationFlags     mutating func unionInPlace(_ other: AudioBytePacketTranslationFlags)     mutating func intersectInPlace(_ other: AudioBytePacketTranslationFlags)     mutating func exclusiveOrInPlace(_ other: AudioBytePacketTranslationFlags)     func isSubsetOf(_ other: AudioBytePacketTranslationFlags) -> Bool     func isDisjointWith(_ other: AudioBytePacketTranslationFlags) -> Bool     func isSupersetOf(_ other: AudioBytePacketTranslationFlags) -> Bool     mutating func subtractInPlace(_ other: AudioBytePacketTranslationFlags)     func isStrictSupersetOf(_ other: AudioBytePacketTranslationFlags) -> Bool     func isStrictSubsetOf(_ other: AudioBytePacketTranslationFlags) -> Bool } extension AudioBytePacketTranslationFlags {     func union(_ other: AudioBytePacketTranslationFlags) -> AudioBytePacketTranslationFlags     func intersection(_ other: AudioBytePacketTranslationFlags) -> AudioBytePacketTranslationFlags     func symmetricDifference(_ other: AudioBytePacketTranslationFlags) -> AudioBytePacketTranslationFlags } extension AudioBytePacketTranslationFlags {     func contains(_ member: AudioBytePacketTranslationFlags) -> Bool     mutating func insert(_ newMember: AudioBytePacketTranslationFlags) -> (inserted: Bool, memberAfterInsert: AudioBytePacketTranslationFlags)     mutating func remove(_ member: AudioBytePacketTranslationFlags) -> AudioBytePacketTranslationFlags?     mutating func update(with newMember: AudioBytePacketTranslationFlags) -> AudioBytePacketTranslationFlags? } extension AudioBytePacketTranslationFlags {     convenience init()     mutating func formUnion(_ other: AudioBytePacketTranslationFlags)     mutating func formIntersection(_ other: AudioBytePacketTranslationFlags)     mutating func formSymmetricDifference(_ other: AudioBytePacketTranslationFlags) } extension AudioBytePacketTranslationFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioBytePacketTranslationFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioBytePacketTranslationFlags...)     mutating func subtract(_ other: AudioBytePacketTranslationFlags)     func isSubset(of other: AudioBytePacketTranslationFlags) -> Bool     func isSuperset(of other: AudioBytePacketTranslationFlags) -> Bool     func isDisjoint(with other: AudioBytePacketTranslationFlags) -> Bool     func subtracting(_ other: AudioBytePacketTranslationFlags) -> AudioBytePacketTranslationFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioBytePacketTranslationFlags) -> Bool     func isStrictSubset(of other: AudioBytePacketTranslationFlags) -> Bool } ``` | OptionSet |

Modified [AudioBytePacketTranslationFlags.bytePacketTranslationFlag_IsEstimate](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslationflags/kbytepackettranslationflag_isestimate)

|  | Declaration |
| --- | --- |
| From | ``` static var BytePacketTranslationFlag_IsEstimate: AudioBytePacketTranslationFlags { get } ``` |
| To | ``` static var bytePacketTranslationFlag_IsEstimate: AudioBytePacketTranslationFlags { get } ``` |

Modified [AudioComponentDescription [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentDescription.componentFlags](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/1410485-componentflags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentDescription.componentFlagsMask](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/1410469-componentflagsmask)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentDescription.componentManufacturer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/1410471-componentmanufacturer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentDescription.componentSubType](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/1410467-componentsubtype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentDescription.componentType](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/1410478-componenttype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentDescription.init()](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/1438471-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentDescription.init(componentType: OSType, componentSubType: OSType, componentManufacturer: OSType, componentFlags: UInt32, componentFlagsMask: UInt32)](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/1439820-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` struct AudioComponentFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Unsearchable: AudioComponentFlags { get }     static var SandboxSafe: AudioComponentFlags { get }     static var IsV3AudioUnit: AudioComponentFlags { get }     static var RequiresAsyncInstantiation: AudioComponentFlags { get }     static var CanLoadInProcess: AudioComponentFlags { get } } ``` | OptionSetType | AudioUnit |
| To | ``` struct AudioComponentFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var unsearchable: AudioComponentFlags { get }     static var sandboxSafe: AudioComponentFlags { get }     static var isV3AudioUnit: AudioComponentFlags { get }     static var requiresAsyncInstantiation: AudioComponentFlags { get }     static var canLoadInProcess: AudioComponentFlags { get }     func intersect(_ other: AudioComponentFlags) -> AudioComponentFlags     func exclusiveOr(_ other: AudioComponentFlags) -> AudioComponentFlags     mutating func unionInPlace(_ other: AudioComponentFlags)     mutating func intersectInPlace(_ other: AudioComponentFlags)     mutating func exclusiveOrInPlace(_ other: AudioComponentFlags)     func isSubsetOf(_ other: AudioComponentFlags) -> Bool     func isDisjointWith(_ other: AudioComponentFlags) -> Bool     func isSupersetOf(_ other: AudioComponentFlags) -> Bool     mutating func subtractInPlace(_ other: AudioComponentFlags)     func isStrictSupersetOf(_ other: AudioComponentFlags) -> Bool     func isStrictSubsetOf(_ other: AudioComponentFlags) -> Bool } extension AudioComponentFlags {     func union(_ other: AudioComponentFlags) -> AudioComponentFlags     func intersection(_ other: AudioComponentFlags) -> AudioComponentFlags     func symmetricDifference(_ other: AudioComponentFlags) -> AudioComponentFlags } extension AudioComponentFlags {     func contains(_ member: AudioComponentFlags) -> Bool     mutating func insert(_ newMember: AudioComponentFlags) -> (inserted: Bool, memberAfterInsert: AudioComponentFlags)     mutating func remove(_ member: AudioComponentFlags) -> AudioComponentFlags?     mutating func update(with newMember: AudioComponentFlags) -> AudioComponentFlags? } extension AudioComponentFlags {     convenience init()     mutating func formUnion(_ other: AudioComponentFlags)     mutating func formIntersection(_ other: AudioComponentFlags)     mutating func formSymmetricDifference(_ other: AudioComponentFlags) } extension AudioComponentFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioComponentFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioComponentFlags...)     mutating func subtract(_ other: AudioComponentFlags)     func isSubset(of other: AudioComponentFlags) -> Bool     func isSuperset(of other: AudioComponentFlags) -> Bool     func isDisjoint(with other: AudioComponentFlags) -> Bool     func subtracting(_ other: AudioComponentFlags) -> AudioComponentFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioComponentFlags) -> Bool     func isStrictSubset(of other: AudioComponentFlags) -> Bool } ``` | OptionSet | AudioToolbox |

Modified [AudioComponentFlags.canLoadInProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/1410506-canloadinprocess)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var CanLoadInProcess: AudioComponentFlags { get } ``` | AudioUnit |
| To | ``` static var canLoadInProcess: AudioComponentFlags { get } ``` | AudioToolbox |

Modified [AudioComponentFlags.init(rawValue: UInt32)](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/1439895-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentFlags.isV3AudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_isv3audiounit)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var IsV3AudioUnit: AudioComponentFlags { get } ``` | AudioUnit |
| To | ``` static var isV3AudioUnit: AudioComponentFlags { get } ``` | AudioToolbox |

Modified [AudioComponentFlags.requiresAsyncInstantiation](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_requiresasyncinstantiation)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var RequiresAsyncInstantiation: AudioComponentFlags { get } ``` | AudioUnit |
| To | ``` static var requiresAsyncInstantiation: AudioComponentFlags { get } ``` | AudioToolbox |

Modified [AudioComponentFlags.sandboxSafe](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_sandboxsafe)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var SandboxSafe: AudioComponentFlags { get } ``` | AudioUnit |
| To | ``` static var sandboxSafe: AudioComponentFlags { get } ``` | AudioToolbox |

Modified [AudioComponentFlags.unsearchable](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags/kaudiocomponentflag_unsearchable)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Unsearchable: AudioComponentFlags { get } ``` | AudioUnit |
| To | ``` static var unsearchable: AudioComponentFlags { get } ``` | AudioToolbox |

Modified [AudioComponentInstantiationOptions [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` struct AudioComponentInstantiationOptions : OptionSetType {     init(rawValue rawValue: UInt32)     static var LoadOutOfProcess: AudioComponentInstantiationOptions { get }     static var LoadInProcess: AudioComponentInstantiationOptions { get } } ``` | OptionSetType | AudioUnit |
| To | ``` struct AudioComponentInstantiationOptions : OptionSet {     init(rawValue rawValue: UInt32)     static var loadOutOfProcess: AudioComponentInstantiationOptions { get }     static var loadInProcess: AudioComponentInstantiationOptions { get }     func intersect(_ other: AudioComponentInstantiationOptions) -> AudioComponentInstantiationOptions     func exclusiveOr(_ other: AudioComponentInstantiationOptions) -> AudioComponentInstantiationOptions     mutating func unionInPlace(_ other: AudioComponentInstantiationOptions)     mutating func intersectInPlace(_ other: AudioComponentInstantiationOptions)     mutating func exclusiveOrInPlace(_ other: AudioComponentInstantiationOptions)     func isSubsetOf(_ other: AudioComponentInstantiationOptions) -> Bool     func isDisjointWith(_ other: AudioComponentInstantiationOptions) -> Bool     func isSupersetOf(_ other: AudioComponentInstantiationOptions) -> Bool     mutating func subtractInPlace(_ other: AudioComponentInstantiationOptions)     func isStrictSupersetOf(_ other: AudioComponentInstantiationOptions) -> Bool     func isStrictSubsetOf(_ other: AudioComponentInstantiationOptions) -> Bool } extension AudioComponentInstantiationOptions {     func union(_ other: AudioComponentInstantiationOptions) -> AudioComponentInstantiationOptions     func intersection(_ other: AudioComponentInstantiationOptions) -> AudioComponentInstantiationOptions     func symmetricDifference(_ other: AudioComponentInstantiationOptions) -> AudioComponentInstantiationOptions } extension AudioComponentInstantiationOptions {     func contains(_ member: AudioComponentInstantiationOptions) -> Bool     mutating func insert(_ newMember: AudioComponentInstantiationOptions) -> (inserted: Bool, memberAfterInsert: AudioComponentInstantiationOptions)     mutating func remove(_ member: AudioComponentInstantiationOptions) -> AudioComponentInstantiationOptions?     mutating func update(with newMember: AudioComponentInstantiationOptions) -> AudioComponentInstantiationOptions? } extension AudioComponentInstantiationOptions {     convenience init()     mutating func formUnion(_ other: AudioComponentInstantiationOptions)     mutating func formIntersection(_ other: AudioComponentInstantiationOptions)     mutating func formSymmetricDifference(_ other: AudioComponentInstantiationOptions) } extension AudioComponentInstantiationOptions {     convenience init<S : Sequence where S.Iterator.Element == AudioComponentInstantiationOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioComponentInstantiationOptions...)     mutating func subtract(_ other: AudioComponentInstantiationOptions)     func isSubset(of other: AudioComponentInstantiationOptions) -> Bool     func isSuperset(of other: AudioComponentInstantiationOptions) -> Bool     func isDisjoint(with other: AudioComponentInstantiationOptions) -> Bool     func subtracting(_ other: AudioComponentInstantiationOptions) -> AudioComponentInstantiationOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioComponentInstantiationOptions) -> Bool     func isStrictSubset(of other: AudioComponentInstantiationOptions) -> Bool } ``` | OptionSet | AudioToolbox |

Modified [AudioComponentInstantiationOptions.init(rawValue: UInt32)](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions/1439180-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentInstantiationOptions.loadOutOfProcess](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions/kaudiocomponentinstantiation_loadoutofprocess)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var LoadOutOfProcess: AudioComponentInstantiationOptions { get } ``` | AudioUnit |
| To | ``` static var loadOutOfProcess: AudioComponentInstantiationOptions { get } ``` | AudioToolbox |

Modified [AudioComponentPlugInInterface [struct]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct AudioComponentPlugInInterface {     var Open: (UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus     var Close: (UnsafeMutablePointer<Void>) -> OSStatus     var Lookup: (Int16) -> AudioComponentMethod     var reserved: UnsafeMutablePointer<Void> } ``` | AudioUnit |
| To | ``` struct AudioComponentPlugInInterface {     var Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus     var Close: (UnsafeMutableRawPointer) -> OSStatus     var Lookup: (Int16) -> AudioComponentMethod?     var reserved: UnsafeMutableRawPointer? } ``` | AudioToolbox |

Modified [AudioComponentPlugInInterface.Close](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/1410449-close)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var Close: (UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` var Close: (UnsafeMutableRawPointer) -> OSStatus ``` | AudioToolbox |

Modified [AudioComponentPlugInInterface.Lookup](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/1410481-lookup)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var Lookup: (Int16) -> AudioComponentMethod ``` | AudioUnit |
| To | ``` var Lookup: (Int16) -> AudioComponentMethod? ``` | AudioToolbox |

Modified [AudioComponentPlugInInterface.Open](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/1410462-open)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var Open: (UnsafeMutablePointer<Void>, AudioComponentInstance) -> OSStatus ``` | AudioUnit |
| To | ``` var Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus ``` | AudioToolbox |

Modified [AudioComponentPlugInInterface.reserved](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/1410439-reserved)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var reserved: UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` var reserved: UnsafeMutableRawPointer? ``` | AudioToolbox |

Modified [AudioComponentValidationResult [enum]](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AudioComponentValidationResult : UInt32 {     case Unknown     case Passed     case Failed     case TimedOut     case UnauthorizedError_Open     case UnauthorizedError_Init } ``` | AudioUnit |
| To | ``` enum AudioComponentValidationResult : UInt32 {     case unknown     case passed     case failed     case timedOut     case unauthorizedError_Open     case unauthorizedError_Init } ``` | AudioToolbox |

Modified [AudioComponentValidationResult.failed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/failed)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Failed ``` | AudioUnit |
| To | ``` case failed ``` | AudioToolbox |

Modified [AudioComponentValidationResult.passed](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_passed)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Passed ``` | AudioUnit |
| To | ``` case passed ``` | AudioToolbox |

Modified [AudioComponentValidationResult.timedOut](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/timedout)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case TimedOut ``` | AudioUnit |
| To | ``` case timedOut ``` | AudioToolbox |

Modified [AudioComponentValidationResult.unauthorizedError_Init](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/kaudiocomponentvalidationresult_unauthorizederror_init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case UnauthorizedError_Init ``` | AudioUnit |
| To | ``` case unauthorizedError_Init ``` | AudioToolbox |

Modified [AudioComponentValidationResult.unauthorizedError_Open](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/unauthorizederror_open)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case UnauthorizedError_Open ``` | AudioUnit |
| To | ``` case unauthorizedError_Open ``` | AudioToolbox |

Modified [AudioComponentValidationResult.unknown](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult/unknown)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Unknown ``` | AudioUnit |
| To | ``` case unknown ``` | AudioToolbox |

Modified [AudioFileFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofileflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioFileFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var EraseFile: AudioFileFlags { get }     static var DontPageAlignAudioData: AudioFileFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioFileFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var eraseFile: AudioFileFlags { get }     static var dontPageAlignAudioData: AudioFileFlags { get }     func intersect(_ other: AudioFileFlags) -> AudioFileFlags     func exclusiveOr(_ other: AudioFileFlags) -> AudioFileFlags     mutating func unionInPlace(_ other: AudioFileFlags)     mutating func intersectInPlace(_ other: AudioFileFlags)     mutating func exclusiveOrInPlace(_ other: AudioFileFlags)     func isSubsetOf(_ other: AudioFileFlags) -> Bool     func isDisjointWith(_ other: AudioFileFlags) -> Bool     func isSupersetOf(_ other: AudioFileFlags) -> Bool     mutating func subtractInPlace(_ other: AudioFileFlags)     func isStrictSupersetOf(_ other: AudioFileFlags) -> Bool     func isStrictSubsetOf(_ other: AudioFileFlags) -> Bool } extension AudioFileFlags {     func union(_ other: AudioFileFlags) -> AudioFileFlags     func intersection(_ other: AudioFileFlags) -> AudioFileFlags     func symmetricDifference(_ other: AudioFileFlags) -> AudioFileFlags } extension AudioFileFlags {     func contains(_ member: AudioFileFlags) -> Bool     mutating func insert(_ newMember: AudioFileFlags) -> (inserted: Bool, memberAfterInsert: AudioFileFlags)     mutating func remove(_ member: AudioFileFlags) -> AudioFileFlags?     mutating func update(with newMember: AudioFileFlags) -> AudioFileFlags? } extension AudioFileFlags {     convenience init()     mutating func formUnion(_ other: AudioFileFlags)     mutating func formIntersection(_ other: AudioFileFlags)     mutating func formSymmetricDifference(_ other: AudioFileFlags) } extension AudioFileFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioFileFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioFileFlags...)     mutating func subtract(_ other: AudioFileFlags)     func isSubset(of other: AudioFileFlags) -> Bool     func isSuperset(of other: AudioFileFlags) -> Bool     func isDisjoint(with other: AudioFileFlags) -> Bool     func subtracting(_ other: AudioFileFlags) -> AudioFileFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioFileFlags) -> Bool     func isStrictSubset(of other: AudioFileFlags) -> Bool } ``` | OptionSet |

Modified [AudioFileFlags.dontPageAlignAudioData](https://developer.apple.com/documentation/audiotoolbox/audiofileflags/1502812-dontpagealignaudiodata)

|  | Declaration |
| --- | --- |
| From | ``` static var DontPageAlignAudioData: AudioFileFlags { get } ``` |
| To | ``` static var dontPageAlignAudioData: AudioFileFlags { get } ``` |

Modified [AudioFileFlags.eraseFile](https://developer.apple.com/documentation/audiotoolbox/audiofileflags/kaudiofileflags_erasefile)

|  | Declaration |
| --- | --- |
| From | ``` static var EraseFile: AudioFileFlags { get } ``` |
| To | ``` static var eraseFile: AudioFileFlags { get } ``` |

Modified [AudioFilePermissions [enum]](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions)

|  | Declaration |
| --- | --- |
| From | ``` enum AudioFilePermissions : Int8 {     case ReadPermission     case WritePermission     case ReadWritePermission } ``` |
| To | ``` enum AudioFilePermissions : Int8 {     case readPermission     case writePermission     case readWritePermission } ``` |

Modified [AudioFilePermissions.readPermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/readpermission)

|  | Declaration |
| --- | --- |
| From | ``` case ReadPermission ``` |
| To | ``` case readPermission ``` |

Modified [AudioFilePermissions.readWritePermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/readwritepermission)

|  | Declaration |
| --- | --- |
| From | ``` case ReadWritePermission ``` |
| To | ``` case readWritePermission ``` |

Modified [AudioFilePermissions.writePermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/kaudiofilewritepermission)

|  | Declaration |
| --- | --- |
| From | ``` case WritePermission ``` |
| To | ``` case writePermission ``` |

Modified [AudioFileRegionFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioFileRegionFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var LoopEnable: AudioFileRegionFlags { get }     static var PlayForward: AudioFileRegionFlags { get }     static var PlayBackward: AudioFileRegionFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioFileRegionFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var loopEnable: AudioFileRegionFlags { get }     static var playForward: AudioFileRegionFlags { get }     static var playBackward: AudioFileRegionFlags { get }     func intersect(_ other: AudioFileRegionFlags) -> AudioFileRegionFlags     func exclusiveOr(_ other: AudioFileRegionFlags) -> AudioFileRegionFlags     mutating func unionInPlace(_ other: AudioFileRegionFlags)     mutating func intersectInPlace(_ other: AudioFileRegionFlags)     mutating func exclusiveOrInPlace(_ other: AudioFileRegionFlags)     func isSubsetOf(_ other: AudioFileRegionFlags) -> Bool     func isDisjointWith(_ other: AudioFileRegionFlags) -> Bool     func isSupersetOf(_ other: AudioFileRegionFlags) -> Bool     mutating func subtractInPlace(_ other: AudioFileRegionFlags)     func isStrictSupersetOf(_ other: AudioFileRegionFlags) -> Bool     func isStrictSubsetOf(_ other: AudioFileRegionFlags) -> Bool } extension AudioFileRegionFlags {     func union(_ other: AudioFileRegionFlags) -> AudioFileRegionFlags     func intersection(_ other: AudioFileRegionFlags) -> AudioFileRegionFlags     func symmetricDifference(_ other: AudioFileRegionFlags) -> AudioFileRegionFlags } extension AudioFileRegionFlags {     func contains(_ member: AudioFileRegionFlags) -> Bool     mutating func insert(_ newMember: AudioFileRegionFlags) -> (inserted: Bool, memberAfterInsert: AudioFileRegionFlags)     mutating func remove(_ member: AudioFileRegionFlags) -> AudioFileRegionFlags?     mutating func update(with newMember: AudioFileRegionFlags) -> AudioFileRegionFlags? } extension AudioFileRegionFlags {     convenience init()     mutating func formUnion(_ other: AudioFileRegionFlags)     mutating func formIntersection(_ other: AudioFileRegionFlags)     mutating func formSymmetricDifference(_ other: AudioFileRegionFlags) } extension AudioFileRegionFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioFileRegionFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioFileRegionFlags...)     mutating func subtract(_ other: AudioFileRegionFlags)     func isSubset(of other: AudioFileRegionFlags) -> Bool     func isSuperset(of other: AudioFileRegionFlags) -> Bool     func isDisjoint(with other: AudioFileRegionFlags) -> Bool     func subtracting(_ other: AudioFileRegionFlags) -> AudioFileRegionFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioFileRegionFlags) -> Bool     func isStrictSubset(of other: AudioFileRegionFlags) -> Bool } ``` | OptionSet |

Modified [AudioFileRegionFlags.loopEnable](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags/1503178-loopenable)

|  | Declaration |
| --- | --- |
| From | ``` static var LoopEnable: AudioFileRegionFlags { get } ``` |
| To | ``` static var loopEnable: AudioFileRegionFlags { get } ``` |

Modified [AudioFileRegionFlags.playBackward](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags/1502362-playbackward)

|  | Declaration |
| --- | --- |
| From | ``` static var PlayBackward: AudioFileRegionFlags { get } ``` |
| To | ``` static var playBackward: AudioFileRegionFlags { get } ``` |

Modified [AudioFileRegionFlags.playForward](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags/1503175-playforward)

|  | Declaration |
| --- | --- |
| From | ``` static var PlayForward: AudioFileRegionFlags { get } ``` |
| To | ``` static var playForward: AudioFileRegionFlags { get } ``` |

Modified [AudioFileStreamParseFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamparseflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioFileStreamParseFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Discontinuity: AudioFileStreamParseFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioFileStreamParseFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var discontinuity: AudioFileStreamParseFlags { get }     func intersect(_ other: AudioFileStreamParseFlags) -> AudioFileStreamParseFlags     func exclusiveOr(_ other: AudioFileStreamParseFlags) -> AudioFileStreamParseFlags     mutating func unionInPlace(_ other: AudioFileStreamParseFlags)     mutating func intersectInPlace(_ other: AudioFileStreamParseFlags)     mutating func exclusiveOrInPlace(_ other: AudioFileStreamParseFlags)     func isSubsetOf(_ other: AudioFileStreamParseFlags) -> Bool     func isDisjointWith(_ other: AudioFileStreamParseFlags) -> Bool     func isSupersetOf(_ other: AudioFileStreamParseFlags) -> Bool     mutating func subtractInPlace(_ other: AudioFileStreamParseFlags)     func isStrictSupersetOf(_ other: AudioFileStreamParseFlags) -> Bool     func isStrictSubsetOf(_ other: AudioFileStreamParseFlags) -> Bool } extension AudioFileStreamParseFlags {     func union(_ other: AudioFileStreamParseFlags) -> AudioFileStreamParseFlags     func intersection(_ other: AudioFileStreamParseFlags) -> AudioFileStreamParseFlags     func symmetricDifference(_ other: AudioFileStreamParseFlags) -> AudioFileStreamParseFlags } extension AudioFileStreamParseFlags {     func contains(_ member: AudioFileStreamParseFlags) -> Bool     mutating func insert(_ newMember: AudioFileStreamParseFlags) -> (inserted: Bool, memberAfterInsert: AudioFileStreamParseFlags)     mutating func remove(_ member: AudioFileStreamParseFlags) -> AudioFileStreamParseFlags?     mutating func update(with newMember: AudioFileStreamParseFlags) -> AudioFileStreamParseFlags? } extension AudioFileStreamParseFlags {     convenience init()     mutating func formUnion(_ other: AudioFileStreamParseFlags)     mutating func formIntersection(_ other: AudioFileStreamParseFlags)     mutating func formSymmetricDifference(_ other: AudioFileStreamParseFlags) } extension AudioFileStreamParseFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioFileStreamParseFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioFileStreamParseFlags...)     mutating func subtract(_ other: AudioFileStreamParseFlags)     func isSubset(of other: AudioFileStreamParseFlags) -> Bool     func isSuperset(of other: AudioFileStreamParseFlags) -> Bool     func isDisjoint(with other: AudioFileStreamParseFlags) -> Bool     func subtracting(_ other: AudioFileStreamParseFlags) -> AudioFileStreamParseFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioFileStreamParseFlags) -> Bool     func isStrictSubset(of other: AudioFileStreamParseFlags) -> Bool } ``` | OptionSet |

Modified [AudioFileStreamParseFlags.discontinuity](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamparseflags/1391547-discontinuity)

|  | Declaration |
| --- | --- |
| From | ``` static var Discontinuity: AudioFileStreamParseFlags { get } ``` |
| To | ``` static var discontinuity: AudioFileStreamParseFlags { get } ``` |

Modified [AudioFileStreamPropertyFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioFileStreamPropertyFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var PropertyIsCached: AudioFileStreamPropertyFlags { get }     static var CacheProperty: AudioFileStreamPropertyFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioFileStreamPropertyFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var propertyIsCached: AudioFileStreamPropertyFlags { get }     static var cacheProperty: AudioFileStreamPropertyFlags { get }     func intersect(_ other: AudioFileStreamPropertyFlags) -> AudioFileStreamPropertyFlags     func exclusiveOr(_ other: AudioFileStreamPropertyFlags) -> AudioFileStreamPropertyFlags     mutating func unionInPlace(_ other: AudioFileStreamPropertyFlags)     mutating func intersectInPlace(_ other: AudioFileStreamPropertyFlags)     mutating func exclusiveOrInPlace(_ other: AudioFileStreamPropertyFlags)     func isSubsetOf(_ other: AudioFileStreamPropertyFlags) -> Bool     func isDisjointWith(_ other: AudioFileStreamPropertyFlags) -> Bool     func isSupersetOf(_ other: AudioFileStreamPropertyFlags) -> Bool     mutating func subtractInPlace(_ other: AudioFileStreamPropertyFlags)     func isStrictSupersetOf(_ other: AudioFileStreamPropertyFlags) -> Bool     func isStrictSubsetOf(_ other: AudioFileStreamPropertyFlags) -> Bool } extension AudioFileStreamPropertyFlags {     func union(_ other: AudioFileStreamPropertyFlags) -> AudioFileStreamPropertyFlags     func intersection(_ other: AudioFileStreamPropertyFlags) -> AudioFileStreamPropertyFlags     func symmetricDifference(_ other: AudioFileStreamPropertyFlags) -> AudioFileStreamPropertyFlags } extension AudioFileStreamPropertyFlags {     func contains(_ member: AudioFileStreamPropertyFlags) -> Bool     mutating func insert(_ newMember: AudioFileStreamPropertyFlags) -> (inserted: Bool, memberAfterInsert: AudioFileStreamPropertyFlags)     mutating func remove(_ member: AudioFileStreamPropertyFlags) -> AudioFileStreamPropertyFlags?     mutating func update(with newMember: AudioFileStreamPropertyFlags) -> AudioFileStreamPropertyFlags? } extension AudioFileStreamPropertyFlags {     convenience init()     mutating func formUnion(_ other: AudioFileStreamPropertyFlags)     mutating func formIntersection(_ other: AudioFileStreamPropertyFlags)     mutating func formSymmetricDifference(_ other: AudioFileStreamPropertyFlags) } extension AudioFileStreamPropertyFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioFileStreamPropertyFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioFileStreamPropertyFlags...)     mutating func subtract(_ other: AudioFileStreamPropertyFlags)     func isSubset(of other: AudioFileStreamPropertyFlags) -> Bool     func isSuperset(of other: AudioFileStreamPropertyFlags) -> Bool     func isDisjoint(with other: AudioFileStreamPropertyFlags) -> Bool     func subtracting(_ other: AudioFileStreamPropertyFlags) -> AudioFileStreamPropertyFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioFileStreamPropertyFlags) -> Bool     func isStrictSubset(of other: AudioFileStreamPropertyFlags) -> Bool } ``` | OptionSet |

Modified [AudioFileStreamPropertyFlags.cacheProperty](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags/1391561-cacheproperty)

|  | Declaration |
| --- | --- |
| From | ``` static var CacheProperty: AudioFileStreamPropertyFlags { get } ``` |
| To | ``` static var cacheProperty: AudioFileStreamPropertyFlags { get } ``` |

Modified [AudioFileStreamPropertyFlags.propertyIsCached](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags/kaudiofilestreampropertyflag_propertyiscached)

|  | Declaration |
| --- | --- |
| From | ``` static var PropertyIsCached: AudioFileStreamPropertyFlags { get } ``` |
| To | ``` static var propertyIsCached: AudioFileStreamPropertyFlags { get } ``` |

Modified [AudioFileStreamSeekFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamseekflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioFileStreamSeekFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var OffsetIsEstimated: AudioFileStreamSeekFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioFileStreamSeekFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var offsetIsEstimated: AudioFileStreamSeekFlags { get }     func intersect(_ other: AudioFileStreamSeekFlags) -> AudioFileStreamSeekFlags     func exclusiveOr(_ other: AudioFileStreamSeekFlags) -> AudioFileStreamSeekFlags     mutating func unionInPlace(_ other: AudioFileStreamSeekFlags)     mutating func intersectInPlace(_ other: AudioFileStreamSeekFlags)     mutating func exclusiveOrInPlace(_ other: AudioFileStreamSeekFlags)     func isSubsetOf(_ other: AudioFileStreamSeekFlags) -> Bool     func isDisjointWith(_ other: AudioFileStreamSeekFlags) -> Bool     func isSupersetOf(_ other: AudioFileStreamSeekFlags) -> Bool     mutating func subtractInPlace(_ other: AudioFileStreamSeekFlags)     func isStrictSupersetOf(_ other: AudioFileStreamSeekFlags) -> Bool     func isStrictSubsetOf(_ other: AudioFileStreamSeekFlags) -> Bool } extension AudioFileStreamSeekFlags {     func union(_ other: AudioFileStreamSeekFlags) -> AudioFileStreamSeekFlags     func intersection(_ other: AudioFileStreamSeekFlags) -> AudioFileStreamSeekFlags     func symmetricDifference(_ other: AudioFileStreamSeekFlags) -> AudioFileStreamSeekFlags } extension AudioFileStreamSeekFlags {     func contains(_ member: AudioFileStreamSeekFlags) -> Bool     mutating func insert(_ newMember: AudioFileStreamSeekFlags) -> (inserted: Bool, memberAfterInsert: AudioFileStreamSeekFlags)     mutating func remove(_ member: AudioFileStreamSeekFlags) -> AudioFileStreamSeekFlags?     mutating func update(with newMember: AudioFileStreamSeekFlags) -> AudioFileStreamSeekFlags? } extension AudioFileStreamSeekFlags {     convenience init()     mutating func formUnion(_ other: AudioFileStreamSeekFlags)     mutating func formIntersection(_ other: AudioFileStreamSeekFlags)     mutating func formSymmetricDifference(_ other: AudioFileStreamSeekFlags) } extension AudioFileStreamSeekFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioFileStreamSeekFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioFileStreamSeekFlags...)     mutating func subtract(_ other: AudioFileStreamSeekFlags)     func isSubset(of other: AudioFileStreamSeekFlags) -> Bool     func isSuperset(of other: AudioFileStreamSeekFlags) -> Bool     func isDisjoint(with other: AudioFileStreamSeekFlags) -> Bool     func subtracting(_ other: AudioFileStreamSeekFlags) -> AudioFileStreamSeekFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioFileStreamSeekFlags) -> Bool     func isStrictSubset(of other: AudioFileStreamSeekFlags) -> Bool } ``` | OptionSet |

Modified [AudioFileStreamSeekFlags.offsetIsEstimated](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamseekflags/1391553-offsetisestimated)

|  | Declaration |
| --- | --- |
| From | ``` static var OffsetIsEstimated: AudioFileStreamSeekFlags { get } ``` |
| To | ``` static var offsetIsEstimated: AudioFileStreamSeekFlags { get } ``` |

Modified [AudioFormatInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audioformatinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32 } ``` |
| To | ``` struct AudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafeRawPointer     var mMagicCookieSize: UInt32 } ``` |

Modified [AudioFormatInfo.mMagicCookie](https://developer.apple.com/documentation/audiotoolbox/audioformatinfo/1502595-mmagiccookie)

|  | Declaration |
| --- | --- |
| From | ``` var mMagicCookie: UnsafePointer<Void> ``` |
| To | ``` var mMagicCookie: UnsafeRawPointer ``` |

Modified [AudioOutputUnitMIDICallbacks [struct]](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct AudioOutputUnitMIDICallbacks {     var userData: UnsafeMutablePointer<Void>     var MIDIEventProc: (UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void     var MIDISysExProc: (UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void } ``` | AudioUnit |
| To | ``` struct AudioOutputUnitMIDICallbacks {     var userData: UnsafeMutableRawPointer?     var MIDIEventProc: (UnsafeMutableRawPointer?, UInt32, UInt32, UInt32, UInt32) -> Swift.Void     var MIDISysExProc: (UnsafeMutableRawPointer?, UnsafePointer<UInt8>, UInt32) -> Swift.Void } ``` | AudioToolbox |

Modified [AudioOutputUnitMIDICallbacks.MIDIEventProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks/1620297-midieventproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var MIDIEventProc: (UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> Void ``` | AudioUnit |
| To | ``` var MIDIEventProc: (UnsafeMutableRawPointer?, UInt32, UInt32, UInt32, UInt32) -> Swift.Void ``` | AudioToolbox |

Modified [AudioOutputUnitMIDICallbacks.MIDISysExProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks/1620298-midisysexproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var MIDISysExProc: (UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> Void ``` | AudioUnit |
| To | ``` var MIDISysExProc: (UnsafeMutableRawPointer?, UnsafePointer<UInt8>, UInt32) -> Swift.Void ``` | AudioToolbox |

Modified [AudioOutputUnitMIDICallbacks.userData](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks/1620287-userdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var userData: UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` var userData: UnsafeMutableRawPointer? ``` | AudioToolbox |

Modified [AudioOutputUnitStartAtTimeParams [struct]](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartattimeparams)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioOutputUnitStartAtTimeParams.init()](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartattimeparams/1440724-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioOutputUnitStartAtTimeParams.init(mTimestamp: AudioTimeStamp, mFlags: UInt32)](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartattimeparams/1440446-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioOutputUnitStartAtTimeParams.mFlags](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartattimeparams/1440665-mflags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioOutputUnitStartAtTimeParams.mTimestamp](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartattimeparams/1438423-mtimestamp)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioPanningMode [enum]](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode)

|  | Declaration |
| --- | --- |
| From | ``` enum AudioPanningMode : UInt32 {     case PanningMode_SoundField     case PanningMode_VectorBasedPanning } ``` |
| To | ``` enum AudioPanningMode : UInt32 {     case panningMode_SoundField     case panningMode_VectorBasedPanning } ``` |

Modified [AudioPanningMode.panningMode_SoundField](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode/panningmode_soundfield)

|  | Declaration |
| --- | --- |
| From | ``` case PanningMode_SoundField ``` |
| To | ``` case panningMode_SoundField ``` |

Modified [AudioPanningMode.panningMode_VectorBasedPanning](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode/kpanningmode_vectorbasedpanning)

|  | Declaration |
| --- | --- |
| From | ``` case PanningMode_VectorBasedPanning ``` |
| To | ``` case panningMode_VectorBasedPanning ``` |

Modified [AudioQueueBuffer [struct]](https://developer.apple.com/documentation/audiotoolbox/audioqueuebuffer)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioQueueBuffer {     var mAudioDataBytesCapacity: UInt32     var mAudioData: UnsafeMutablePointer<Void>     var mAudioDataByteSize: UInt32     var mUserData: UnsafeMutablePointer<Void>     var mPacketDescriptionCapacity: UInt32     var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>     var mPacketDescriptionCount: UInt32 } ``` |
| To | ``` struct AudioQueueBuffer {     var mAudioDataBytesCapacity: UInt32     var mAudioData: UnsafeMutableRawPointer     var mAudioDataByteSize: UInt32     var mUserData: UnsafeMutableRawPointer?     var mPacketDescriptionCapacity: UInt32     var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?     var mPacketDescriptionCount: UInt32 } ``` |

Modified [AudioQueueBuffer.mAudioData](https://developer.apple.com/documentation/audiotoolbox/audioqueuebuffer/1502113-maudiodata)

|  | Declaration |
| --- | --- |
| From | ``` var mAudioData: UnsafeMutablePointer<Void> ``` |
| To | ``` var mAudioData: UnsafeMutableRawPointer ``` |

Modified [AudioQueueBuffer.mPacketDescriptions](https://developer.apple.com/documentation/audiotoolbox/audioqueuebuffer/1501775-mpacketdescriptions)

|  | Declaration |
| --- | --- |
| From | ``` var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription> ``` |
| To | ``` var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>? ``` |

Modified [AudioQueueBuffer.mUserData](https://developer.apple.com/documentation/audiotoolbox/audioqueuebuffer/1501712-muserdata)

|  | Declaration |
| --- | --- |
| From | ``` var mUserData: UnsafeMutablePointer<Void> ``` |
| To | ``` var mUserData: UnsafeMutableRawPointer? ``` |

Modified [AudioQueueProcessingTapFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AudioQueueProcessingTapFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var PreEffects: AudioQueueProcessingTapFlags { get }     static var PostEffects: AudioQueueProcessingTapFlags { get }     static var Siphon: AudioQueueProcessingTapFlags { get }     static var StartOfStream: AudioQueueProcessingTapFlags { get }     static var EndOfStream: AudioQueueProcessingTapFlags { get } } ``` | OptionSetType |
| To | ``` struct AudioQueueProcessingTapFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var preEffects: AudioQueueProcessingTapFlags { get }     static var postEffects: AudioQueueProcessingTapFlags { get }     static var siphon: AudioQueueProcessingTapFlags { get }     static var startOfStream: AudioQueueProcessingTapFlags { get }     static var endOfStream: AudioQueueProcessingTapFlags { get }     func intersect(_ other: AudioQueueProcessingTapFlags) -> AudioQueueProcessingTapFlags     func exclusiveOr(_ other: AudioQueueProcessingTapFlags) -> AudioQueueProcessingTapFlags     mutating func unionInPlace(_ other: AudioQueueProcessingTapFlags)     mutating func intersectInPlace(_ other: AudioQueueProcessingTapFlags)     mutating func exclusiveOrInPlace(_ other: AudioQueueProcessingTapFlags)     func isSubsetOf(_ other: AudioQueueProcessingTapFlags) -> Bool     func isDisjointWith(_ other: AudioQueueProcessingTapFlags) -> Bool     func isSupersetOf(_ other: AudioQueueProcessingTapFlags) -> Bool     mutating func subtractInPlace(_ other: AudioQueueProcessingTapFlags)     func isStrictSupersetOf(_ other: AudioQueueProcessingTapFlags) -> Bool     func isStrictSubsetOf(_ other: AudioQueueProcessingTapFlags) -> Bool } extension AudioQueueProcessingTapFlags {     func union(_ other: AudioQueueProcessingTapFlags) -> AudioQueueProcessingTapFlags     func intersection(_ other: AudioQueueProcessingTapFlags) -> AudioQueueProcessingTapFlags     func symmetricDifference(_ other: AudioQueueProcessingTapFlags) -> AudioQueueProcessingTapFlags } extension AudioQueueProcessingTapFlags {     func contains(_ member: AudioQueueProcessingTapFlags) -> Bool     mutating func insert(_ newMember: AudioQueueProcessingTapFlags) -> (inserted: Bool, memberAfterInsert: AudioQueueProcessingTapFlags)     mutating func remove(_ member: AudioQueueProcessingTapFlags) -> AudioQueueProcessingTapFlags?     mutating func update(with newMember: AudioQueueProcessingTapFlags) -> AudioQueueProcessingTapFlags? } extension AudioQueueProcessingTapFlags {     convenience init()     mutating func formUnion(_ other: AudioQueueProcessingTapFlags)     mutating func formIntersection(_ other: AudioQueueProcessingTapFlags)     mutating func formSymmetricDifference(_ other: AudioQueueProcessingTapFlags) } extension AudioQueueProcessingTapFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioQueueProcessingTapFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioQueueProcessingTapFlags...)     mutating func subtract(_ other: AudioQueueProcessingTapFlags)     func isSubset(of other: AudioQueueProcessingTapFlags) -> Bool     func isSuperset(of other: AudioQueueProcessingTapFlags) -> Bool     func isDisjoint(with other: AudioQueueProcessingTapFlags) -> Bool     func subtracting(_ other: AudioQueueProcessingTapFlags) -> AudioQueueProcessingTapFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioQueueProcessingTapFlags) -> Bool     func isStrictSubset(of other: AudioQueueProcessingTapFlags) -> Bool } ``` | OptionSet |

Modified [AudioQueueProcessingTapFlags.endOfStream](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_endofstream)

|  | Declaration |
| --- | --- |
| From | ``` static var EndOfStream: AudioQueueProcessingTapFlags { get } ``` |
| To | ``` static var endOfStream: AudioQueueProcessingTapFlags { get } ``` |

Modified [AudioQueueProcessingTapFlags.postEffects](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_posteffects)

|  | Declaration |
| --- | --- |
| From | ``` static var PostEffects: AudioQueueProcessingTapFlags { get } ``` |
| To | ``` static var postEffects: AudioQueueProcessingTapFlags { get } ``` |

Modified [AudioQueueProcessingTapFlags.preEffects](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1502092-preeffects)

|  | Declaration |
| --- | --- |
| From | ``` static var PreEffects: AudioQueueProcessingTapFlags { get } ``` |
| To | ``` static var preEffects: AudioQueueProcessingTapFlags { get } ``` |

Modified [AudioQueueProcessingTapFlags.siphon](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1502728-siphon)

|  | Declaration |
| --- | --- |
| From | ``` static var Siphon: AudioQueueProcessingTapFlags { get } ``` |
| To | ``` static var siphon: AudioQueueProcessingTapFlags { get } ``` |

Modified [AudioQueueProcessingTapFlags.startOfStream](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1503320-startofstream)

|  | Declaration |
| --- | --- |
| From | ``` static var StartOfStream: AudioQueueProcessingTapFlags { get } ``` |
| To | ``` static var startOfStream: AudioQueueProcessingTapFlags { get } ``` |

Modified [AudioUnitConnection [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitconnection)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitConnection.destInputNumber](https://developer.apple.com/documentation/audiotoolbox/audiounitconnection/1439799-destinputnumber)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitConnection.sourceAudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiounitconnection/1438983-sourceaudiounit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitConnection.sourceOutputNumber](https://developer.apple.com/documentation/audiotoolbox/audiounitconnection/1440326-sourceoutputnumber)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitExternalBuffer [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitexternalbuffer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitExternalBuffer.buffer](https://developer.apple.com/documentation/audiotoolbox/audiounitexternalbuffer/1440788-buffer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitExternalBuffer.size](https://developer.apple.com/documentation/audiotoolbox/audiounitexternalbuffer/1438671-size)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitFrequencyResponseBin [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitfrequencyresponsebin)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitFrequencyResponseBin.init()](https://developer.apple.com/documentation/audiotoolbox/audiounitfrequencyresponsebin/1438492-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitFrequencyResponseBin.init(mFrequency: Float64, mMagnitude: Float64)](https://developer.apple.com/documentation/audiotoolbox/audiounitfrequencyresponsebin/1438955-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitFrequencyResponseBin.mFrequency](https://developer.apple.com/documentation/audiotoolbox/audiounitfrequencyresponsebin/1438362-mfrequency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitFrequencyResponseBin.mMagnitude](https://developer.apple.com/documentation/audiotoolbox/audiounitfrequencyresponsebin/1438425-mmagnitude)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitMeterClipping [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitMeterClipping.init()](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping/1440818-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitMeterClipping.init(peakValueSinceLastCall: Float32, sawInfinity: DarwinBoolean, sawNotANumber: DarwinBoolean)](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping/1440075-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitMeterClipping.peakValueSinceLastCall](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping/1439318-peakvaluesincelastcall)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitMeterClipping.sawInfinity](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping/1438398-sawinfinity)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitMeterClipping.sawNotANumber](https://developer.apple.com/documentation/audiotoolbox/audiounitmeterclipping/1439628-sawnotanumber)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameter [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameter.mAudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiounitparameter/1439553-maudiounit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameter.mElement](https://developer.apple.com/documentation/audiotoolbox/audiounitparameter/1440880-melement)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameter.mParameterID](https://developer.apple.com/documentation/audiotoolbox/audiounitparameter/1438652-mparameterid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameter.mScope](https://developer.apple.com/documentation/audiotoolbox/audiounitparameter/1439535-mscope)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterEvent.element](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1440132-element)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterEvent.eventType](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1439949-eventtype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterEvent.eventValues](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1439066-eventvalues)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterEvent.init()](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1440571-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterEvent.init(scope: AudioUnitScope, element: AudioUnitElement, parameter: AudioUnitParameterID, eventType: AUParameterEventType, eventValues: AudioUnitParameterEvent.__Unnamed_union_eventValues)](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1438724-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterEvent.parameter](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1440425-parameter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterEvent.scope](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/1438297-scope)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterHistoryInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterhistoryinfo)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterHistoryInfo.historyDurationInSeconds](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterhistoryinfo/1439496-historydurationinseconds)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterHistoryInfo.init()](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterhistoryinfo/1440232-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterHistoryInfo.init(updatesPerSecond: Float32, historyDurationInSeconds: Float32)](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterhistoryinfo/1438900-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterHistoryInfo.updatesPerSecond](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterhistoryinfo/1440851-updatespersecond)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.cfNameString](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439972-cfnamestring)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.clumpID](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439747-clumpid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.defaultValue](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1438864-defaultvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.flags](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1440939-flags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.init()](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1440008-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.init(name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), unitName: Unmanaged<CFString>?, clumpID: UInt32, cfNameString: Unmanaged<CFString>?, unit: AudioUnitParameterUnit, minValue: AudioUnitParameterValue, maxValue: AudioUnitParameterValue, defaultValue: AudioUnitParameterValue, flags: AudioUnitParameterOptions)](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439445-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.maxValue](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439413-maxvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.minValue](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439884-minvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.name](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439753-name)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.unit](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1440889-unit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterInfo.unitName](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterinfo/1439337-unitname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterNameInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteridname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterNameInfo.inDesiredLength](https://developer.apple.com/documentation/audiotoolbox/audiounitparameternameinfo/1438507-indesiredlength)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterNameInfo.inID](https://developer.apple.com/documentation/audiotoolbox/audiounitparameternameinfo/1440431-inid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterNameInfo.init()](https://developer.apple.com/documentation/audiotoolbox/audiounitparameternameinfo/1438356-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterNameInfo.init(inID: AudioUnitParameterID, inDesiredLength: Int32, outName: Unmanaged<CFString>?)](https://developer.apple.com/documentation/audiotoolbox/audiounitparameternameinfo/1439899-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterNameInfo.outName](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteridname/1440656-outname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterOptions [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` struct AudioUnitParameterOptions : OptionSetType {     init(rawValue rawValue: UInt32)     static var Flag_CFNameRelease: AudioUnitParameterOptions { get }     static var Flag_OmitFromPresets: AudioUnitParameterOptions { get }     static var Flag_PlotHistory: AudioUnitParameterOptions { get }     static var Flag_MeterReadOnly: AudioUnitParameterOptions { get }     static var Flag_DisplayMask: AudioUnitParameterOptions { get }     static var Flag_DisplaySquareRoot: AudioUnitParameterOptions { get }     static var Flag_DisplaySquared: AudioUnitParameterOptions { get }     static var Flag_DisplayCubed: AudioUnitParameterOptions { get }     static var Flag_DisplayCubeRoot: AudioUnitParameterOptions { get }     static var Flag_DisplayExponential: AudioUnitParameterOptions { get }     static var Flag_HasClump: AudioUnitParameterOptions { get }     static var Flag_ValuesHaveStrings: AudioUnitParameterOptions { get }     static var Flag_DisplayLogarithmic: AudioUnitParameterOptions { get }     static var Flag_IsHighResolution: AudioUnitParameterOptions { get }     static var Flag_NonRealTime: AudioUnitParameterOptions { get }     static var Flag_CanRamp: AudioUnitParameterOptions { get }     static var Flag_ExpertMode: AudioUnitParameterOptions { get }     static var Flag_HasCFNameString: AudioUnitParameterOptions { get }     static var Flag_IsGlobalMeta: AudioUnitParameterOptions { get }     static var Flag_IsElementMeta: AudioUnitParameterOptions { get }     static var Flag_IsReadable: AudioUnitParameterOptions { get }     static var Flag_IsWritable: AudioUnitParameterOptions { get } } ``` | OptionSetType | AudioUnit |
| To | ``` struct AudioUnitParameterOptions : OptionSet {     init(rawValue rawValue: UInt32)     static var flag_CFNameRelease: AudioUnitParameterOptions { get }     static var flag_OmitFromPresets: AudioUnitParameterOptions { get }     static var flag_PlotHistory: AudioUnitParameterOptions { get }     static var flag_MeterReadOnly: AudioUnitParameterOptions { get }     static var flag_DisplayMask: AudioUnitParameterOptions { get }     static var flag_DisplaySquareRoot: AudioUnitParameterOptions { get }     static var flag_DisplaySquared: AudioUnitParameterOptions { get }     static var flag_DisplayCubed: AudioUnitParameterOptions { get }     static var flag_DisplayCubeRoot: AudioUnitParameterOptions { get }     static var flag_DisplayExponential: AudioUnitParameterOptions { get }     static var flag_HasClump: AudioUnitParameterOptions { get }     static var flag_ValuesHaveStrings: AudioUnitParameterOptions { get }     static var flag_DisplayLogarithmic: AudioUnitParameterOptions { get }     static var flag_IsHighResolution: AudioUnitParameterOptions { get }     static var flag_NonRealTime: AudioUnitParameterOptions { get }     static var flag_CanRamp: AudioUnitParameterOptions { get }     static var flag_ExpertMode: AudioUnitParameterOptions { get }     static var flag_HasCFNameString: AudioUnitParameterOptions { get }     static var flag_IsGlobalMeta: AudioUnitParameterOptions { get }     static var flag_IsElementMeta: AudioUnitParameterOptions { get }     static var flag_IsReadable: AudioUnitParameterOptions { get }     static var flag_IsWritable: AudioUnitParameterOptions { get }     func intersect(_ other: AudioUnitParameterOptions) -> AudioUnitParameterOptions     func exclusiveOr(_ other: AudioUnitParameterOptions) -> AudioUnitParameterOptions     mutating func unionInPlace(_ other: AudioUnitParameterOptions)     mutating func intersectInPlace(_ other: AudioUnitParameterOptions)     mutating func exclusiveOrInPlace(_ other: AudioUnitParameterOptions)     func isSubsetOf(_ other: AudioUnitParameterOptions) -> Bool     func isDisjointWith(_ other: AudioUnitParameterOptions) -> Bool     func isSupersetOf(_ other: AudioUnitParameterOptions) -> Bool     mutating func subtractInPlace(_ other: AudioUnitParameterOptions)     func isStrictSupersetOf(_ other: AudioUnitParameterOptions) -> Bool     func isStrictSubsetOf(_ other: AudioUnitParameterOptions) -> Bool } extension AudioUnitParameterOptions {     func union(_ other: AudioUnitParameterOptions) -> AudioUnitParameterOptions     func intersection(_ other: AudioUnitParameterOptions) -> AudioUnitParameterOptions     func symmetricDifference(_ other: AudioUnitParameterOptions) -> AudioUnitParameterOptions } extension AudioUnitParameterOptions {     func contains(_ member: AudioUnitParameterOptions) -> Bool     mutating func insert(_ newMember: AudioUnitParameterOptions) -> (inserted: Bool, memberAfterInsert: AudioUnitParameterOptions)     mutating func remove(_ member: AudioUnitParameterOptions) -> AudioUnitParameterOptions?     mutating func update(with newMember: AudioUnitParameterOptions) -> AudioUnitParameterOptions? } extension AudioUnitParameterOptions {     convenience init()     mutating func formUnion(_ other: AudioUnitParameterOptions)     mutating func formIntersection(_ other: AudioUnitParameterOptions)     mutating func formSymmetricDifference(_ other: AudioUnitParameterOptions) } extension AudioUnitParameterOptions {     convenience init<S : Sequence where S.Iterator.Element == AudioUnitParameterOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioUnitParameterOptions...)     mutating func subtract(_ other: AudioUnitParameterOptions)     func isSubset(of other: AudioUnitParameterOptions) -> Bool     func isSuperset(of other: AudioUnitParameterOptions) -> Bool     func isDisjoint(with other: AudioUnitParameterOptions) -> Bool     func subtracting(_ other: AudioUnitParameterOptions) -> AudioUnitParameterOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioUnitParameterOptions) -> Bool     func isStrictSubset(of other: AudioUnitParameterOptions) -> Bool } ``` | OptionSet | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_CanRamp](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_canramp)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_CanRamp: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_CanRamp: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_CFNameRelease](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439788-flag_cfnamerelease)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_CFNameRelease: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_CFNameRelease: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_DisplayCubed](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439330-flag_displaycubed)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_DisplayCubed: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_DisplayCubed: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_DisplayCubeRoot](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440958-flag_displaycuberoot)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_DisplayCubeRoot: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_DisplayCubeRoot: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_DisplayExponential](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displayexponential)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_DisplayExponential: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_DisplayExponential: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_DisplayLogarithmic](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displaylogarithmic)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_DisplayLogarithmic: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_DisplayLogarithmic: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_DisplayMask](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_displaymask)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_DisplayMask: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_DisplayMask: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_DisplaySquared](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440750-flag_displaysquared)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_DisplaySquared: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_DisplaySquared: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_DisplaySquareRoot](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1441018-flag_displaysquareroot)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_DisplaySquareRoot: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_DisplaySquareRoot: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_ExpertMode](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_expertmode)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_ExpertMode: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_ExpertMode: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_HasCFNameString](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_hascfnamestring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_HasCFNameString: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_HasCFNameString: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_HasClump](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_hasclump)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_HasClump: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_HasClump: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_IsElementMeta](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439961-flag_iselementmeta)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_IsElementMeta: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_IsElementMeta: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_IsGlobalMeta](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_isglobalmeta)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_IsGlobalMeta: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_IsGlobalMeta: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_IsHighResolution](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_ishighresolution)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_IsHighResolution: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_IsHighResolution: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_IsReadable](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1438604-flag_isreadable)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_IsReadable: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_IsReadable: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_IsWritable](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440477-flag_iswritable)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_IsWritable: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_IsWritable: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_MeterReadOnly](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1439379-flag_meterreadonly)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_MeterReadOnly: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_MeterReadOnly: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_NonRealTime](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_nonrealtime)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_NonRealTime: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_NonRealTime: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_OmitFromPresets](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_omitfrompresets)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_OmitFromPresets: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_OmitFromPresets: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_PlotHistory](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/kaudiounitparameterflag_plothistory)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_PlotHistory: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_PlotHistory: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.flag_ValuesHaveStrings](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440179-flag_valueshavestrings)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Flag_ValuesHaveStrings: AudioUnitParameterOptions { get } ``` | AudioUnit |
| To | ``` static var flag_ValuesHaveStrings: AudioUnitParameterOptions { get } ``` | AudioToolbox |

Modified [AudioUnitParameterOptions.init(rawValue: UInt32)](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/1440981-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterStringFromValue [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterstringfromvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterStringFromValue.inParamID](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterstringfromvalue/1438396-inparamid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterStringFromValue.inValue](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterstringfromvalue/1438851-invalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterStringFromValue.outString](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterstringfromvalue/1439491-outstring)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterUnit [enum]](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AudioUnitParameterUnit : UInt32 {     case Generic     case Indexed     case Boolean     case Percent     case Seconds     case SampleFrames     case Phase     case Rate     case Hertz     case Cents     case RelativeSemiTones     case MIDINoteNumber     case MIDIController     case Decibels     case LinearGain     case Degrees     case EqualPowerCrossfade     case MixerFaderCurve1     case Pan     case Meters     case AbsoluteCents     case Octaves     case BPM     case Beats     case Milliseconds     case Ratio     case CustomUnit } ``` | AudioUnit |
| To | ``` enum AudioUnitParameterUnit : UInt32 {     case generic     case indexed     case boolean     case percent     case seconds     case sampleFrames     case phase     case rate     case hertz     case cents     case relativeSemiTones     case midiNoteNumber     case midiController     case decibels     case linearGain     case degrees     case equalPowerCrossfade     case mixerFaderCurve1     case pan     case meters     case absoluteCents     case octaves     case BPM     case beats     case milliseconds     case ratio     case customUnit } ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.absoluteCents](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_absolutecents)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case AbsoluteCents ``` | AudioUnit |
| To | ``` case absoluteCents ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.beats](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/beats)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Beats ``` | AudioUnit |
| To | ``` case beats ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.boolean](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_boolean)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Boolean ``` | AudioUnit |
| To | ``` case boolean ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.BPM](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_bpm)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterUnit.cents](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_cents)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Cents ``` | AudioUnit |
| To | ``` case cents ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.customUnit](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/customunit)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case CustomUnit ``` | AudioUnit |
| To | ``` case customUnit ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.decibels](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_decibels)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Decibels ``` | AudioUnit |
| To | ``` case decibels ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.degrees](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_degrees)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Degrees ``` | AudioUnit |
| To | ``` case degrees ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.equalPowerCrossfade](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_equalpowercrossfade)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case EqualPowerCrossfade ``` | AudioUnit |
| To | ``` case equalPowerCrossfade ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.generic](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/generic)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Generic ``` | AudioUnit |
| To | ``` case generic ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.hertz](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/hertz)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Hertz ``` | AudioUnit |
| To | ``` case hertz ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.indexed](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/indexed)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Indexed ``` | AudioUnit |
| To | ``` case indexed ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.linearGain](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_lineargain)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case LinearGain ``` | AudioUnit |
| To | ``` case linearGain ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.meters](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/meters)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Meters ``` | AudioUnit |
| To | ``` case meters ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.midiController](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/midicontroller)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case MIDIController ``` | AudioUnit |
| To | ``` case midiController ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.midiNoteNumber](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/midinotenumber)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case MIDINoteNumber ``` | AudioUnit |
| To | ``` case midiNoteNumber ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.milliseconds](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/milliseconds)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Milliseconds ``` | AudioUnit |
| To | ``` case milliseconds ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.mixerFaderCurve1](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/mixerfadercurve1)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case MixerFaderCurve1 ``` | AudioUnit |
| To | ``` case mixerFaderCurve1 ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.octaves](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_octaves)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Octaves ``` | AudioUnit |
| To | ``` case octaves ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.pan](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_pan)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Pan ``` | AudioUnit |
| To | ``` case pan ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.percent](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_percent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Percent ``` | AudioUnit |
| To | ``` case percent ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.phase](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_phase)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Phase ``` | AudioUnit |
| To | ``` case phase ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.rate](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_rate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Rate ``` | AudioUnit |
| To | ``` case rate ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.ratio](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/ratio)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Ratio ``` | AudioUnit |
| To | ``` case ratio ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.relativeSemiTones](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_relativesemitones)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case RelativeSemiTones ``` | AudioUnit |
| To | ``` case relativeSemiTones ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.sampleFrames](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_sampleframes)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SampleFrames ``` | AudioUnit |
| To | ``` case sampleFrames ``` | AudioToolbox |

Modified [AudioUnitParameterUnit.seconds](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/kaudiounitparameterunit_seconds)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Seconds ``` | AudioUnit |
| To | ``` case seconds ``` | AudioToolbox |

Modified [AudioUnitParameterValueFromString [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluefromstring)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterValueFromString.inParamID](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluefromstring/1438920-inparamid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterValueFromString.inString](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluefromstring/1440393-instring)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterValueFromString.outValue](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervaluefromstring/1440783-outvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitProperty [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitproperty)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitProperty.mAudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiounitproperty/1440388-maudiounit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitProperty.mElement](https://developer.apple.com/documentation/audiotoolbox/audiounitproperty/1440667-melement)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitProperty.mPropertyID](https://developer.apple.com/documentation/audiotoolbox/audiounitproperty/1440799-mpropertyid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitProperty.mScope](https://developer.apple.com/documentation/audiotoolbox/audiounitproperty/1439219-mscope)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitRemoteControlEvent [enum]](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AudioUnitRemoteControlEvent : UInt32 {     case TogglePlayPause     case ToggleRecord     case Rewind } ``` | AudioUnit |
| To | ``` enum AudioUnitRemoteControlEvent : UInt32 {     case togglePlayPause     case toggleRecord     case rewind } ``` | AudioToolbox |

Modified [AudioUnitRemoteControlEvent.rewind](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/kaudiounitremotecontrolevent_rewind)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Rewind ``` | AudioUnit |
| To | ``` case rewind ``` | AudioToolbox |

Modified [AudioUnitRemoteControlEvent.togglePlayPause](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/toggleplaypause)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case TogglePlayPause ``` | AudioUnit |
| To | ``` case togglePlayPause ``` | AudioToolbox |

Modified [AudioUnitRemoteControlEvent.toggleRecord](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontrolevent/togglerecord)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ToggleRecord ``` | AudioUnit |
| To | ``` case toggleRecord ``` | AudioToolbox |

Modified [AudioUnitRenderActionFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` struct AudioUnitRenderActionFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var UnitRenderAction_PreRender: AudioUnitRenderActionFlags { get }     static var UnitRenderAction_PostRender: AudioUnitRenderActionFlags { get }     static var UnitRenderAction_OutputIsSilence: AudioUnitRenderActionFlags { get }     static var OfflineUnitRenderAction_Preflight: AudioUnitRenderActionFlags { get }     static var OfflineUnitRenderAction_Render: AudioUnitRenderActionFlags { get }     static var OfflineUnitRenderAction_Complete: AudioUnitRenderActionFlags { get }     static var UnitRenderAction_PostRenderError: AudioUnitRenderActionFlags { get }     static var UnitRenderAction_DoNotCheckRenderArgs: AudioUnitRenderActionFlags { get } } ``` | OptionSetType | AudioUnit |
| To | ``` struct AudioUnitRenderActionFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var unitRenderAction_PreRender: AudioUnitRenderActionFlags { get }     static var unitRenderAction_PostRender: AudioUnitRenderActionFlags { get }     static var unitRenderAction_OutputIsSilence: AudioUnitRenderActionFlags { get }     static var offlineUnitRenderAction_Preflight: AudioUnitRenderActionFlags { get }     static var offlineUnitRenderAction_Render: AudioUnitRenderActionFlags { get }     static var offlineUnitRenderAction_Complete: AudioUnitRenderActionFlags { get }     static var unitRenderAction_PostRenderError: AudioUnitRenderActionFlags { get }     static var unitRenderAction_DoNotCheckRenderArgs: AudioUnitRenderActionFlags { get }     func intersect(_ other: AudioUnitRenderActionFlags) -> AudioUnitRenderActionFlags     func exclusiveOr(_ other: AudioUnitRenderActionFlags) -> AudioUnitRenderActionFlags     mutating func unionInPlace(_ other: AudioUnitRenderActionFlags)     mutating func intersectInPlace(_ other: AudioUnitRenderActionFlags)     mutating func exclusiveOrInPlace(_ other: AudioUnitRenderActionFlags)     func isSubsetOf(_ other: AudioUnitRenderActionFlags) -> Bool     func isDisjointWith(_ other: AudioUnitRenderActionFlags) -> Bool     func isSupersetOf(_ other: AudioUnitRenderActionFlags) -> Bool     mutating func subtractInPlace(_ other: AudioUnitRenderActionFlags)     func isStrictSupersetOf(_ other: AudioUnitRenderActionFlags) -> Bool     func isStrictSubsetOf(_ other: AudioUnitRenderActionFlags) -> Bool } extension AudioUnitRenderActionFlags {     func union(_ other: AudioUnitRenderActionFlags) -> AudioUnitRenderActionFlags     func intersection(_ other: AudioUnitRenderActionFlags) -> AudioUnitRenderActionFlags     func symmetricDifference(_ other: AudioUnitRenderActionFlags) -> AudioUnitRenderActionFlags } extension AudioUnitRenderActionFlags {     func contains(_ member: AudioUnitRenderActionFlags) -> Bool     mutating func insert(_ newMember: AudioUnitRenderActionFlags) -> (inserted: Bool, memberAfterInsert: AudioUnitRenderActionFlags)     mutating func remove(_ member: AudioUnitRenderActionFlags) -> AudioUnitRenderActionFlags?     mutating func update(with newMember: AudioUnitRenderActionFlags) -> AudioUnitRenderActionFlags? } extension AudioUnitRenderActionFlags {     convenience init()     mutating func formUnion(_ other: AudioUnitRenderActionFlags)     mutating func formIntersection(_ other: AudioUnitRenderActionFlags)     mutating func formSymmetricDifference(_ other: AudioUnitRenderActionFlags) } extension AudioUnitRenderActionFlags {     convenience init<S : Sequence where S.Iterator.Element == AudioUnitRenderActionFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AudioUnitRenderActionFlags...)     mutating func subtract(_ other: AudioUnitRenderActionFlags)     func isSubset(of other: AudioUnitRenderActionFlags) -> Bool     func isSuperset(of other: AudioUnitRenderActionFlags) -> Bool     func isDisjoint(with other: AudioUnitRenderActionFlags) -> Bool     func subtracting(_ other: AudioUnitRenderActionFlags) -> AudioUnitRenderActionFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AudioUnitRenderActionFlags) -> Bool     func isStrictSubset(of other: AudioUnitRenderActionFlags) -> Bool } ``` | OptionSet | AudioToolbox |

Modified [AudioUnitRenderActionFlags.init(rawValue: UInt32)](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1438349-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitRenderActionFlags.offlineUnitRenderAction_Complete](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudioofflineunitrenderaction_complete)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var OfflineUnitRenderAction_Complete: AudioUnitRenderActionFlags { get } ``` | AudioUnit |
| To | ``` static var offlineUnitRenderAction_Complete: AudioUnitRenderActionFlags { get } ``` | AudioToolbox |

Modified [AudioUnitRenderActionFlags.offlineUnitRenderAction_Preflight](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudioofflineunitrenderaction_preflight)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var OfflineUnitRenderAction_Preflight: AudioUnitRenderActionFlags { get } ``` | AudioUnit |
| To | ``` static var offlineUnitRenderAction_Preflight: AudioUnitRenderActionFlags { get } ``` | AudioToolbox |

Modified [AudioUnitRenderActionFlags.offlineUnitRenderAction_Render](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1439632-offlineunitrenderaction_render)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var OfflineUnitRenderAction_Render: AudioUnitRenderActionFlags { get } ``` | AudioUnit |
| To | ``` static var offlineUnitRenderAction_Render: AudioUnitRenderActionFlags { get } ``` | AudioToolbox |

Modified [AudioUnitRenderActionFlags.unitRenderAction_DoNotCheckRenderArgs](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_donotcheckrenderargs)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var UnitRenderAction_DoNotCheckRenderArgs: AudioUnitRenderActionFlags { get } ``` | AudioUnit |
| To | ``` static var unitRenderAction_DoNotCheckRenderArgs: AudioUnitRenderActionFlags { get } ``` | AudioToolbox |

Modified [AudioUnitRenderActionFlags.unitRenderAction_OutputIsSilence](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_outputissilence)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var UnitRenderAction_OutputIsSilence: AudioUnitRenderActionFlags { get } ``` | AudioUnit |
| To | ``` static var unitRenderAction_OutputIsSilence: AudioUnitRenderActionFlags { get } ``` | AudioToolbox |

Modified [AudioUnitRenderActionFlags.unitRenderAction_PostRender](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1440615-unitrenderaction_postrender)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var UnitRenderAction_PostRender: AudioUnitRenderActionFlags { get } ``` | AudioUnit |
| To | ``` static var unitRenderAction_PostRender: AudioUnitRenderActionFlags { get } ``` | AudioToolbox |

Modified [AudioUnitRenderActionFlags.unitRenderAction_PostRenderError](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/kaudiounitrenderaction_postrendererror)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var UnitRenderAction_PostRenderError: AudioUnitRenderActionFlags { get } ``` | AudioUnit |
| To | ``` static var unitRenderAction_PostRenderError: AudioUnitRenderActionFlags { get } ``` | AudioToolbox |

Modified [AudioUnitRenderActionFlags.unitRenderAction_PreRender](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags/1440530-unitrenderaction_prerender)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var UnitRenderAction_PreRender: AudioUnitRenderActionFlags { get } ``` | AudioUnit |
| To | ``` static var unitRenderAction_PreRender: AudioUnitRenderActionFlags { get } ``` | AudioToolbox |

Modified [AUHostTransportStateFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` struct AUHostTransportStateFlags : OptionSetType {     init(rawValue rawValue: UInt)     static var Changed: AUHostTransportStateFlags { get }     static var Moving: AUHostTransportStateFlags { get }     static var Recording: AUHostTransportStateFlags { get }     static var Cycling: AUHostTransportStateFlags { get } } ``` | OptionSetType | AudioUnit |
| To | ``` struct AUHostTransportStateFlags : OptionSet {     init(rawValue rawValue: UInt)     static var changed: AUHostTransportStateFlags { get }     static var moving: AUHostTransportStateFlags { get }     static var recording: AUHostTransportStateFlags { get }     static var cycling: AUHostTransportStateFlags { get }     func intersect(_ other: AUHostTransportStateFlags) -> AUHostTransportStateFlags     func exclusiveOr(_ other: AUHostTransportStateFlags) -> AUHostTransportStateFlags     mutating func unionInPlace(_ other: AUHostTransportStateFlags)     mutating func intersectInPlace(_ other: AUHostTransportStateFlags)     mutating func exclusiveOrInPlace(_ other: AUHostTransportStateFlags)     func isSubsetOf(_ other: AUHostTransportStateFlags) -> Bool     func isDisjointWith(_ other: AUHostTransportStateFlags) -> Bool     func isSupersetOf(_ other: AUHostTransportStateFlags) -> Bool     mutating func subtractInPlace(_ other: AUHostTransportStateFlags)     func isStrictSupersetOf(_ other: AUHostTransportStateFlags) -> Bool     func isStrictSubsetOf(_ other: AUHostTransportStateFlags) -> Bool } extension AUHostTransportStateFlags {     func union(_ other: AUHostTransportStateFlags) -> AUHostTransportStateFlags     func intersection(_ other: AUHostTransportStateFlags) -> AUHostTransportStateFlags     func symmetricDifference(_ other: AUHostTransportStateFlags) -> AUHostTransportStateFlags } extension AUHostTransportStateFlags {     func contains(_ member: AUHostTransportStateFlags) -> Bool     mutating func insert(_ newMember: AUHostTransportStateFlags) -> (inserted: Bool, memberAfterInsert: AUHostTransportStateFlags)     mutating func remove(_ member: AUHostTransportStateFlags) -> AUHostTransportStateFlags?     mutating func update(with newMember: AUHostTransportStateFlags) -> AUHostTransportStateFlags? } extension AUHostTransportStateFlags {     convenience init()     mutating func formUnion(_ other: AUHostTransportStateFlags)     mutating func formIntersection(_ other: AUHostTransportStateFlags)     mutating func formSymmetricDifference(_ other: AUHostTransportStateFlags) } extension AUHostTransportStateFlags {     convenience init<S : Sequence where S.Iterator.Element == AUHostTransportStateFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AUHostTransportStateFlags...)     mutating func subtract(_ other: AUHostTransportStateFlags)     func isSubset(of other: AUHostTransportStateFlags) -> Bool     func isSuperset(of other: AUHostTransportStateFlags) -> Bool     func isDisjoint(with other: AUHostTransportStateFlags) -> Bool     func subtracting(_ other: AUHostTransportStateFlags) -> AUHostTransportStateFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AUHostTransportStateFlags) -> Bool     func isStrictSubset(of other: AUHostTransportStateFlags) -> Bool } ``` | OptionSet | AudioToolbox |

Modified [AUHostTransportStateFlags.changed](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387572-changed)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Changed: AUHostTransportStateFlags { get } ``` | AudioUnit |
| To | ``` static var changed: AUHostTransportStateFlags { get } ``` | AudioToolbox |

Modified [AUHostTransportStateFlags.cycling](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/auhosttransportstatecycling)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Cycling: AUHostTransportStateFlags { get } ``` | AudioUnit |
| To | ``` static var cycling: AUHostTransportStateFlags { get } ``` | AudioToolbox |

Modified [AUHostTransportStateFlags.init(rawValue: UInt)](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1440808-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUHostTransportStateFlags.moving](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387579-moving)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Moving: AUHostTransportStateFlags { get } ``` | AudioUnit |
| To | ``` static var moving: AUHostTransportStateFlags { get } ``` | AudioToolbox |

Modified [AUHostTransportStateFlags.recording](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/1387591-recording)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var Recording: AUHostTransportStateFlags { get } ``` | AudioUnit |
| To | ``` static var recording: AUHostTransportStateFlags { get } ``` | AudioToolbox |

Modified [AUInputSamplesInOutputCallbackStruct [struct]](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallbackstruct)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AUInputSamplesInOutputCallback     var userData: UnsafeMutablePointer<Void> } ``` | AudioUnit |
| To | ``` struct AUInputSamplesInOutputCallbackStruct {     var inputToOutputCallback: AudioToolbox.AUInputSamplesInOutputCallback     var userData: UnsafeMutableRawPointer? } ``` | AudioToolbox |

Modified [AUInputSamplesInOutputCallbackStruct.inputToOutputCallback](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallbackstruct/1438564-inputtooutputcallback)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var inputToOutputCallback: AUInputSamplesInOutputCallback ``` | AudioUnit |
| To | ``` var inputToOutputCallback: AudioToolbox.AUInputSamplesInOutputCallback ``` | AudioToolbox |

Modified [AUInputSamplesInOutputCallbackStruct.userData](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallbackstruct/1439494-userdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var userData: UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` var userData: UnsafeMutableRawPointer? ``` | AudioToolbox |

Modified [AUMIDIEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aumidievent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct AUMIDIEvent {     var next: UnsafeMutablePointer<AURenderEvent>     var eventSampleTime: AUEventSampleTime     var eventType: AURenderEventType     var reserved: UInt8     var length: UInt16     var cable: UInt8     var data: (UInt8, UInt8, UInt8)     init()     init(next next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime eventSampleTime: AUEventSampleTime, eventType eventType: AURenderEventType, reserved reserved: UInt8, length length: UInt16, cable cable: UInt8, data data: (UInt8, UInt8, UInt8)) } ``` | AudioUnit |
| To | ``` struct AUMIDIEvent {     var next: UnsafeMutablePointer<AURenderEvent>?     var eventSampleTime: AUEventSampleTime     var eventType: AURenderEventType     var reserved: UInt8     var length: UInt16     var cable: UInt8     var data: (UInt8, UInt8, UInt8)     init()     init(next next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime eventSampleTime: AUEventSampleTime, eventType eventType: AURenderEventType, reserved reserved: UInt8, length length: UInt16, cable cable: UInt8, data data: (UInt8, UInt8, UInt8)) } ``` | AudioToolbox |

Modified [AUMIDIEvent.cable](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439751-cable)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUMIDIEvent.data](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1438814-data)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUMIDIEvent.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440373-eventsampletime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUMIDIEvent.eventType](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440184-eventtype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUMIDIEvent.init()](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1438663-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUMIDIEvent.length](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439101-length)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUMIDIEvent.next](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1439283-next)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var next: UnsafeMutablePointer<AURenderEvent> ``` | AudioUnit |
| To | ``` var next: UnsafeMutablePointer<AURenderEvent>? ``` | AudioToolbox |

Modified [AUMIDIEvent.reserved](https://developer.apple.com/documentation/audiotoolbox/aumidievent/1440361-reserved)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter](https://developer.apple.com/documentation/audiotoolbox/auparameter)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class AUParameter : AUParameterNode, NSSecureCoding {     var minValue: AUValue { get }     var maxValue: AUValue { get }     var unit: AudioUnitParameterUnit { get }     var unitName: String? { get }     var flags: AudioUnitParameterOptions { get }     var address: AUParameterAddress { get }     var valueStrings: [String]? { get }     var dependentParameters: [NSNumber]? { get }     var value: AUValue     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken)     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken, atHostTime hostTime: UInt64)     func stringFromValue(_ value: UnsafePointer<AUValue>) -> String     func valueFromString(_ string: String) -> AUValue } ``` | NSSecureCoding | AudioUnit |
| To | ``` class AUParameter : AUParameterNode, NSSecureCoding {     var minValue: AUValue { get }     var maxValue: AUValue { get }     var unit: AudioUnitParameterUnit { get }     var unitName: String? { get }     var flags: AudioUnitParameterOptions { get }     var address: AUParameterAddress { get }     var valueStrings: [String]? { get }     var dependentParameters: [NSNumber]? { get }     var value: AUValue     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken?)     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken?, atHostTime hostTime: UInt64)     func setValue(_ value: AUValue, originator originator: AUParameterObserverToken?, atHostTime hostTime: UInt64, eventType eventType: AUParameterAutomationEventType)     func string(fromValue value: UnsafePointer<AUValue>?) -> String     func value(from string: String) -> AUValue     var implementorValueObserver: AUImplementorValueObserver     var implementorValueProvider: AUImplementorValueProvider     var implementorStringFromValueCallback: AUImplementorStringFromValueCallback     var implementorValueFromStringCallback: AUImplementorValueFromStringCallback     var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AUParameter : CVarArg { } extension AUParameter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding | AudioToolbox |

Modified [AUParameter.address](https://developer.apple.com/documentation/audiotoolbox/auparameter/1441037-address)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter.dependentParameters](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440649-dependentparameters)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter.flags](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439938-flags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter.maxValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438427-maxvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter.minValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440270-minvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter.setValue(_: AUValue, originator: AUParameterObserverToken?)](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439968-setvalue)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func setValue(_ value: AUValue, originator originator: AUParameterObserverToken) ``` | AudioUnit |
| To | ``` func setValue(_ value: AUValue, originator originator: AUParameterObserverToken?) ``` | AudioToolbox |

Modified [AUParameter.setValue(_: AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438450-setvalue)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func setValue(_ value: AUValue, originator originator: AUParameterObserverToken, atHostTime hostTime: UInt64) ``` | AudioUnit |
| To | ``` func setValue(_ value: AUValue, originator originator: AUParameterObserverToken?, atHostTime hostTime: UInt64) ``` | AudioToolbox |

Modified [AUParameter.string(fromValue: UnsafePointer<AUValue>?) -> String](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440901-stringfromvalue)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func stringFromValue(_ value: UnsafePointer<AUValue>) -> String ``` | AudioUnit |
| To | ``` func string(fromValue value: UnsafePointer<AUValue>?) -> String ``` | AudioToolbox |

Modified [AUParameter.unit](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440698-unit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter.unitName](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438490-unitname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter.value](https://developer.apple.com/documentation/audiotoolbox/auparameter/1439301-value)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameter.value(from: String) -> AUValue](https://developer.apple.com/documentation/audiotoolbox/auparameter/1440495-valuefromstring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func valueFromString(_ string: String) -> AUValue ``` | AudioUnit |
| To | ``` func value(from string: String) -> AUValue ``` | AudioToolbox |

Modified [AUParameter.valueStrings](https://developer.apple.com/documentation/audiotoolbox/auparameter/1438358-valuestrings)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/auparameterevent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct AUParameterEvent {     var next: UnsafeMutablePointer<AURenderEvent>     var eventSampleTime: AUEventSampleTime     var eventType: AURenderEventType     var reserved: (UInt8, UInt8, UInt8)     var rampDurationSampleFrames: AUAudioFrameCount     var parameterAddress: AUParameterAddress     var value: AUValue     init()     init(next next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime eventSampleTime: AUEventSampleTime, eventType eventType: AURenderEventType, reserved reserved: (UInt8, UInt8, UInt8), rampDurationSampleFrames rampDurationSampleFrames: AUAudioFrameCount, parameterAddress parameterAddress: AUParameterAddress, value value: AUValue) } ``` | AudioUnit |
| To | ``` struct AUParameterEvent {     var next: UnsafeMutablePointer<AURenderEvent>?     var eventSampleTime: AUEventSampleTime     var eventType: AURenderEventType     var reserved: (UInt8, UInt8, UInt8)     var rampDurationSampleFrames: AUAudioFrameCount     var parameterAddress: AUParameterAddress     var value: AUValue     init()     init(next next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime eventSampleTime: AUEventSampleTime, eventType eventType: AURenderEventType, reserved reserved: (UInt8, UInt8, UInt8), rampDurationSampleFrames rampDurationSampleFrames: AUAudioFrameCount, parameterAddress parameterAddress: AUParameterAddress, value value: AUValue) } ``` | AudioToolbox |

Modified [AUParameterEvent.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440912-eventsampletime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterEvent.eventType](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1438332-eventtype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterEvent.init()](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1438641-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterEvent.next](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440983-next)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var next: UnsafeMutablePointer<AURenderEvent> ``` | AudioUnit |
| To | ``` var next: UnsafeMutablePointer<AURenderEvent>? ``` | AudioToolbox |

Modified [AUParameterEvent.parameterAddress](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440605-parameteraddress)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterEvent.rampDurationSampleFrames](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1439037-rampdurationsampleframes)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterEvent.reserved](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1439165-reserved)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterEvent.value](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/1440528-value)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AUParameterEventType : UInt32 {     case ParameterEvent_Immediate     case ParameterEvent_Ramped } ``` | AudioUnit |
| To | ``` enum AUParameterEventType : UInt32 {     case parameterEvent_Immediate     case parameterEvent_Ramped } ``` | AudioToolbox |

Modified [AUParameterEventType.parameterEvent_Immediate](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype/parameterevent_immediate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ParameterEvent_Immediate ``` | AudioUnit |
| To | ``` case parameterEvent_Immediate ``` | AudioToolbox |

Modified [AUParameterEventType.parameterEvent_Ramped](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype/kparameterevent_ramped)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ParameterEvent_Ramped ``` | AudioUnit |
| To | ``` case parameterEvent_Ramped ``` | AudioToolbox |

Modified [AUParameterGroup](https://developer.apple.com/documentation/audiotoolbox/auparametergroup)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class AUParameterGroup : AUParameterNode, NSSecureCoding {     var children: [AUParameterNode] { get }     var allParameters: [AUParameter] { get } } ``` | NSSecureCoding | AudioUnit |
| To | ``` class AUParameterGroup : AUParameterNode, NSSecureCoding {     var children: [AUParameterNode] { get }     var allParameters: [AUParameter] { get }     var implementorValueObserver: AUImplementorValueObserver     var implementorValueProvider: AUImplementorValueProvider     var implementorStringFromValueCallback: AUImplementorStringFromValueCallback     var implementorValueFromStringCallback: AUImplementorValueFromStringCallback     var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AUParameterGroup : CVarArg { } extension AUParameterGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding | AudioToolbox |

Modified [AUParameterGroup.allParameters](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439439-allparameters)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterGroup.children](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/1439325-children)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterNode](https://developer.apple.com/documentation/audiotoolbox/auparameternode)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class AUParameterNode : NSObject {     var identifier: String { get }     var keyPath: String { get }     var displayName: String { get }     func displayNameWithLength(_ maximumLength: Int) -> String     func tokenByAddingParameterObserver(_ observer: AUParameterObserver) -> AUParameterObserverToken     func tokenByAddingParameterRecordingObserver(_ observer: AUParameterRecordingObserver) -> AUParameterObserverToken     func removeParameterObserver(_ token: AUParameterObserverToken) } extension AUParameterNode {     var implementorValueObserver: AUImplementorValueObserver     var implementorValueProvider: AUImplementorValueProvider     var implementorStringFromValueCallback: AUImplementorStringFromValueCallback     var implementorValueFromStringCallback: AUImplementorValueFromStringCallback     var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback } ``` | -- | AudioUnit |
| To | ``` class AUParameterNode : NSObject {     var identifier: String { get }     var keyPath: String { get }     var displayName: String { get }     func displayName(withLength maximumLength: Int) -> String     func token(byAddingParameterObserver observer: AudioToolbox.AUParameterObserver) -> AUParameterObserverToken     func token(byAddingParameterRecordingObserver observer: AudioToolbox.AUParameterRecordingObserver) -> AUParameterObserverToken     func token(byAddingParameterAutomationObserver observer: AudioToolbox.AUParameterAutomationObserver) -> AUParameterObserverToken     func removeParameterObserver(_ token: AUParameterObserverToken)     var implementorValueObserver: AudioToolbox.AUImplementorValueObserver     var implementorValueProvider: AudioToolbox.AUImplementorValueProvider     var implementorStringFromValueCallback: AudioToolbox.AUImplementorStringFromValueCallback     var implementorValueFromStringCallback: AudioToolbox.AUImplementorValueFromStringCallback     var implementorDisplayNameWithLengthCallback: AudioToolbox.AUImplementorDisplayNameWithLengthCallback     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AUParameterNode {     var implementorValueObserver: AudioToolbox.AUImplementorValueObserver     var implementorValueProvider: AudioToolbox.AUImplementorValueProvider     var implementorStringFromValueCallback: AudioToolbox.AUImplementorStringFromValueCallback     var implementorValueFromStringCallback: AudioToolbox.AUImplementorValueFromStringCallback     var implementorDisplayNameWithLengthCallback: AudioToolbox.AUImplementorDisplayNameWithLengthCallback } extension AUParameterNode : CVarArg { } extension AUParameterNode : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | AudioToolbox |

Modified [AUParameterNode.displayName](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440278-displayname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterNode.displayName(withLength: Int) -> String](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439449-displaynamewithlength)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func displayNameWithLength(_ maximumLength: Int) -> String ``` | AudioUnit |
| To | ``` func displayName(withLength maximumLength: Int) -> String ``` | AudioToolbox |

Modified [AUParameterNode.identifier](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440186-identifier)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterNode.implementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439427-implementordisplaynamewithlength)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback ``` | AudioUnit |
| To | ``` var implementorDisplayNameWithLengthCallback: AudioToolbox.AUImplementorDisplayNameWithLengthCallback ``` | AudioToolbox |

Modified [AUParameterNode.implementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440045-implementorstringfromvaluecallba)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var implementorStringFromValueCallback: AUImplementorStringFromValueCallback ``` | AudioUnit |
| To | ``` var implementorStringFromValueCallback: AudioToolbox.AUImplementorStringFromValueCallback ``` | AudioToolbox |

Modified [AUParameterNode.implementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439270-implementorvaluefromstringcallba)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var implementorValueFromStringCallback: AUImplementorValueFromStringCallback ``` | AudioUnit |
| To | ``` var implementorValueFromStringCallback: AudioToolbox.AUImplementorValueFromStringCallback ``` | AudioToolbox |

Modified [AUParameterNode.implementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439658-implementorvalueobserver)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var implementorValueObserver: AUImplementorValueObserver ``` | AudioUnit |
| To | ``` var implementorValueObserver: AudioToolbox.AUImplementorValueObserver ``` | AudioToolbox |

Modified [AUParameterNode.implementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439942-implementorvalueprovider)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var implementorValueProvider: AUImplementorValueProvider ``` | AudioUnit |
| To | ``` var implementorValueProvider: AudioToolbox.AUImplementorValueProvider ``` | AudioToolbox |

Modified [AUParameterNode.keyPath](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439420-keypath)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterNode.removeParameterObserver(_: AUParameterObserverToken)](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1439314-removeparameterobserver)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterNode.token(byAddingParameterObserver: AudioToolbox.AUParameterObserver) -> AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440811-token)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func tokenByAddingParameterObserver(_ observer: AUParameterObserver) -> AUParameterObserverToken ``` | AudioUnit |
| To | ``` func token(byAddingParameterObserver observer: AudioToolbox.AUParameterObserver) -> AUParameterObserverToken ``` | AudioToolbox |

Modified [AUParameterNode.token(byAddingParameterRecordingObserver: AudioToolbox.AUParameterRecordingObserver) -> AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameternode/1440903-tokenbyaddingparameterrecordingo)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func tokenByAddingParameterRecordingObserver(_ observer: AUParameterRecordingObserver) -> AUParameterObserverToken ``` | AudioUnit |
| To | ``` func token(byAddingParameterRecordingObserver observer: AudioToolbox.AUParameterRecordingObserver) -> AUParameterObserverToken ``` | AudioToolbox |

Modified [AUParameterTree](https://developer.apple.com/documentation/audiotoolbox/auparametertree)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class AUParameterTree : AUParameterGroup, NSSecureCoding {     func parameterWithAddress(_ address: AUParameterAddress) -> AUParameter?     func parameterWithID(_ paramID: AudioUnitParameterID, scope scope: AudioUnitScope, element element: AudioUnitElement) -> AUParameter? } extension AUParameterTree {     class func createParameterWithIdentifier(_ identifier: String, name name: String, address address: AUParameterAddress, min min: AUValue, max max: AUValue, unit unit: AudioUnitParameterUnit, unitName unitName: String?, flags flags: AudioUnitParameterOptions, valueStrings valueStrings: [String]?, dependentParameters dependentParameters: [NSNumber]?) -> AUParameter     class func createGroupWithIdentifier(_ identifier: String, name name: String, children children: [AUParameterNode]) -> AUParameterGroup     class func createGroupTemplate(_ children: [AUParameterNode]) -> AUParameterGroup     class func createGroupFromTemplate(_ templateGroup: AUParameterGroup, identifier identifier: String, name name: String, addressOffset addressOffset: AUParameterAddress) -> AUParameterGroup     class func createTreeWithChildren(_ children: [AUParameterNode]) -> AUParameterTree } ``` | AudioUnit |
| To | ``` class AUParameterTree : AUParameterGroup, NSSecureCoding {     func parameter(withAddress address: AUParameterAddress) -> AUParameter?     func parameter(withID paramID: AudioUnitParameterID, scope scope: AudioUnitScope, element element: AudioUnitElement) -> AUParameter?     class func createParameter(withIdentifier identifier: String, name name: String, address address: AUParameterAddress, min min: AUValue, max max: AUValue, unit unit: AudioUnitParameterUnit, unitName unitName: String?, flags flags: AudioUnitParameterOptions = [], valueStrings valueStrings: [String]?, dependentParameters dependentParameters: [NSNumber]?) -> AUParameter     class func createGroup(withIdentifier identifier: String, name name: String, children children: [AUParameterNode]) -> AUParameterGroup     class func createGroupTemplate(_ children: [AUParameterNode]) -> AUParameterGroup     class func createGroup(fromTemplate templateGroup: AUParameterGroup, identifier identifier: String, name name: String, addressOffset addressOffset: AUParameterAddress) -> AUParameterGroup     class func createTree(withChildren children: [AUParameterNode]) -> AUParameterTree } extension AUParameterTree {     class func createParameter(withIdentifier identifier: String, name name: String, address address: AUParameterAddress, min min: AUValue, max max: AUValue, unit unit: AudioUnitParameterUnit, unitName unitName: String?, flags flags: AudioUnitParameterOptions = [], valueStrings valueStrings: [String]?, dependentParameters dependentParameters: [NSNumber]?) -> AUParameter     class func createGroup(withIdentifier identifier: String, name name: String, children children: [AUParameterNode]) -> AUParameterGroup     class func createGroupTemplate(_ children: [AUParameterNode]) -> AUParameterGroup     class func createGroup(fromTemplate templateGroup: AUParameterGroup, identifier identifier: String, name name: String, addressOffset addressOffset: AUParameterAddress) -> AUParameterGroup     class func createTree(withChildren children: [AUParameterNode]) -> AUParameterTree } ``` | AudioToolbox |

Modified [AUParameterTree.createGroup(fromTemplate: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439822-creategroupfromtemplate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func createGroupFromTemplate(_ templateGroup: AUParameterGroup, identifier identifier: String, name name: String, addressOffset addressOffset: AUParameterAddress) -> AUParameterGroup ``` | AudioUnit |
| To | ``` class func createGroup(fromTemplate templateGroup: AUParameterGroup, identifier identifier: String, name name: String, addressOffset addressOffset: AUParameterAddress) -> AUParameterGroup ``` | AudioToolbox |

Modified [AUParameterTree.createGroup(withIdentifier: String, name: String, children: [AUParameterNode]) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439002-creategroupwithidentifier)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func createGroupWithIdentifier(_ identifier: String, name name: String, children children: [AUParameterNode]) -> AUParameterGroup ``` | AudioUnit |
| To | ``` class func createGroup(withIdentifier identifier: String, name name: String, children children: [AUParameterNode]) -> AUParameterGroup ``` | AudioToolbox |

Modified [AUParameterTree.createGroupTemplate(_: [AUParameterNode]) -> AUParameterGroup [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439912-creategrouptemplate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterTree.createParameter(withIdentifier: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1440598-createparameter)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func createParameterWithIdentifier(_ identifier: String, name name: String, address address: AUParameterAddress, min min: AUValue, max max: AUValue, unit unit: AudioUnitParameterUnit, unitName unitName: String?, flags flags: AudioUnitParameterOptions, valueStrings valueStrings: [String]?, dependentParameters dependentParameters: [NSNumber]?) -> AUParameter ``` | AudioUnit |
| To | ``` class func createParameter(withIdentifier identifier: String, name name: String, address address: AUParameterAddress, min min: AUValue, max max: AUValue, unit unit: AudioUnitParameterUnit, unitName unitName: String?, flags flags: AudioUnitParameterOptions = [], valueStrings valueStrings: [String]?, dependentParameters dependentParameters: [NSNumber]?) -> AUParameter ``` | AudioToolbox |

Modified [AUParameterTree.createTree(withChildren: [AUParameterNode]) -> AUParameterTree [class]](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438522-createtree)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func createTreeWithChildren(_ children: [AUParameterNode]) -> AUParameterTree ``` | AudioUnit |
| To | ``` class func createTree(withChildren children: [AUParameterNode]) -> AUParameterTree ``` | AudioToolbox |

Modified [AUParameterTree.parameter(withAddress: AUParameterAddress) -> AUParameter?](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1439569-parameter)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func parameterWithAddress(_ address: AUParameterAddress) -> AUParameter? ``` | AudioUnit |
| To | ``` func parameter(withAddress address: AUParameterAddress) -> AUParameter? ``` | AudioToolbox |

Modified [AUParameterTree.parameter(withID: AudioUnitParameterID, scope: AudioUnitScope, element: AudioUnitElement) -> AUParameter?](https://developer.apple.com/documentation/audiotoolbox/auparametertree/1438918-parameter)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func parameterWithID(_ paramID: AudioUnitParameterID, scope scope: AudioUnitScope, element element: AudioUnitElement) -> AUParameter? ``` | AudioUnit |
| To | ``` func parameter(withID paramID: AudioUnitParameterID, scope scope: AudioUnitScope, element element: AudioUnitElement) -> AUParameter? ``` | AudioToolbox |

Modified [AUPreset [struct]](https://developer.apple.com/documentation/audiotoolbox/aupreset)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct AUPreset {     var presetNumber: Int32     var presetName: Unmanaged<CFString> } ``` | AudioUnit |
| To | ``` struct AUPreset {     var presetNumber: Int32     var presetName: Unmanaged<CFString>?     init()     init(presetNumber presetNumber: Int32, presetName presetName: Unmanaged<CFString>?) } ``` | AudioToolbox |

Modified [AUPreset.presetName](https://developer.apple.com/documentation/audiotoolbox/aupreset/1440636-presetname)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var presetName: Unmanaged<CFString> ``` | AudioUnit |
| To | ``` var presetName: Unmanaged<CFString>? ``` | AudioToolbox |

Modified [AUPreset.presetNumber](https://developer.apple.com/documentation/audiotoolbox/aupreset/1439357-presetnumber)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURecordedParameterEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURecordedParameterEvent.address](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1438335-address)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURecordedParameterEvent.hostTime](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1440955-hosttime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURecordedParameterEvent.init()](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1439006-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURecordedParameterEvent.init(hostTime: UInt64, address: AUParameterAddress, value: AUValue)](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1438326-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURecordedParameterEvent.value](https://developer.apple.com/documentation/audiotoolbox/aurecordedparameterevent/1440438-value)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderCallbackStruct [struct]](https://developer.apple.com/documentation/audiotoolbox/aurendercallbackstruct)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct AURenderCallbackStruct {     var inputProc: AURenderCallback     var inputProcRefCon: UnsafeMutablePointer<Void> } ``` | AudioUnit |
| To | ``` struct AURenderCallbackStruct {     var inputProc: AudioToolbox.AURenderCallback?     var inputProcRefCon: UnsafeMutableRawPointer?     init()     init(inputProc inputProc: AudioToolbox.AURenderCallback?, inputProcRefCon inputProcRefCon: UnsafeMutableRawPointer?) } ``` | AudioToolbox |

Modified [AURenderCallbackStruct.inputProc](https://developer.apple.com/documentation/audiotoolbox/aurendercallbackstruct/1438593-inputproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var inputProc: AURenderCallback ``` | AudioUnit |
| To | ``` var inputProc: AudioToolbox.AURenderCallback? ``` | AudioToolbox |

Modified [AURenderCallbackStruct.inputProcRefCon](https://developer.apple.com/documentation/audiotoolbox/aurendercallbackstruct/1438345-inputprocrefcon)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var inputProcRefCon: UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` var inputProcRefCon: UnsafeMutableRawPointer? ``` | AudioToolbox |

Modified [AURenderEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aurenderevent)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEvent.head](https://developer.apple.com/documentation/audiotoolbox/1440272-aurenderevent/1440028-head)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEvent.init()](https://developer.apple.com/documentation/audiotoolbox/aurenderevent/1440823-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEvent.init(head: AURenderEventHeader)](https://developer.apple.com/documentation/audiotoolbox/aurenderevent/1439000-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEvent.init(MIDI: AUMIDIEvent)](https://developer.apple.com/documentation/audiotoolbox/aurenderevent/1438429-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEvent.init(parameter: AUParameterEvent)](https://developer.apple.com/documentation/audiotoolbox/aurenderevent/1440070-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEvent.MIDI](https://developer.apple.com/documentation/audiotoolbox/1440272-aurenderevent/1438519-midi)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEvent.parameter](https://developer.apple.com/documentation/audiotoolbox/1440272-aurenderevent/1439668-parameter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEventHeader [struct]](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct AURenderEventHeader {     var next: UnsafeMutablePointer<AURenderEvent>     var eventSampleTime: AUEventSampleTime     var eventType: AURenderEventType     var reserved: UInt8     init()     init(next next: UnsafeMutablePointer<AURenderEvent>, eventSampleTime eventSampleTime: AUEventSampleTime, eventType eventType: AURenderEventType, reserved reserved: UInt8) } ``` | AudioUnit |
| To | ``` struct AURenderEventHeader {     var next: UnsafeMutablePointer<AURenderEvent>?     var eventSampleTime: AUEventSampleTime     var eventType: AURenderEventType     var reserved: UInt8     init()     init(next next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime eventSampleTime: AUEventSampleTime, eventType eventType: AURenderEventType, reserved reserved: UInt8) } ``` | AudioToolbox |

Modified [AURenderEventHeader.eventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440010-eventsampletime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEventHeader.eventType](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440946-eventtype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEventHeader.init()](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1438971-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEventHeader.next](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1439936-next)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var next: UnsafeMutablePointer<AURenderEvent> ``` | AudioUnit |
| To | ``` var next: UnsafeMutablePointer<AURenderEvent>? ``` | AudioToolbox |

Modified [AURenderEventHeader.reserved](https://developer.apple.com/documentation/audiotoolbox/aurendereventheader/1440587-reserved)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEventType [enum]](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AURenderEventType : UInt8 {     case Parameter     case ParameterRamp     case MIDI     case MIDISysEx } ``` | AudioUnit |
| To | ``` enum AURenderEventType : UInt8 {     case parameter     case parameterRamp     case MIDI     case midiSysEx } ``` | AudioToolbox |

Modified [AURenderEventType.MIDI](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midi)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AURenderEventType.midiSysEx](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/midisysex)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case MIDISysEx ``` | AudioUnit |
| To | ``` case midiSysEx ``` | AudioToolbox |

Modified [AURenderEventType.parameter](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/parameter)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Parameter ``` | AudioUnit |
| To | ``` case parameter ``` | AudioToolbox |

Modified [AURenderEventType.parameterRamp](https://developer.apple.com/documentation/audiotoolbox/aurendereventtype/parameterramp)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ParameterRamp ``` | AudioUnit |
| To | ``` case parameterRamp ``` | AudioToolbox |

Modified [AUReverbRoomType [enum]](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AUReverbRoomType : UInt32 {     case ReverbRoomType_SmallRoom     case ReverbRoomType_MediumRoom     case ReverbRoomType_LargeRoom     case ReverbRoomType_MediumHall     case ReverbRoomType_LargeHall     case ReverbRoomType_Plate     case ReverbRoomType_MediumChamber     case ReverbRoomType_LargeChamber     case ReverbRoomType_Cathedral     case ReverbRoomType_LargeRoom2     case ReverbRoomType_MediumHall2     case ReverbRoomType_MediumHall3     case ReverbRoomType_LargeHall2 } ``` | AudioUnit |
| To | ``` enum AUReverbRoomType : UInt32 {     case reverbRoomType_SmallRoom     case reverbRoomType_MediumRoom     case reverbRoomType_LargeRoom     case reverbRoomType_MediumHall     case reverbRoomType_LargeHall     case reverbRoomType_Plate     case reverbRoomType_MediumChamber     case reverbRoomType_LargeChamber     case reverbRoomType_Cathedral     case reverbRoomType_LargeRoom2     case reverbRoomType_MediumHall2     case reverbRoomType_MediumHall3     case reverbRoomType_LargeHall2 } ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_Cathedral](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_cathedral)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_Cathedral ``` | AudioUnit |
| To | ``` case reverbRoomType_Cathedral ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_LargeChamber](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largechamber)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_LargeChamber ``` | AudioUnit |
| To | ``` case reverbRoomType_LargeChamber ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_LargeHall](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largehall)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_LargeHall ``` | AudioUnit |
| To | ``` case reverbRoomType_LargeHall ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_LargeHall2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largehall2)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_LargeHall2 ``` | AudioUnit |
| To | ``` case reverbRoomType_LargeHall2 ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_LargeRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_largeroom)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_LargeRoom ``` | AudioUnit |
| To | ``` case reverbRoomType_LargeRoom ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_LargeRoom2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_largeroom2)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_LargeRoom2 ``` | AudioUnit |
| To | ``` case reverbRoomType_LargeRoom2 ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_MediumChamber](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_mediumchamber)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_MediumChamber ``` | AudioUnit |
| To | ``` case reverbRoomType_MediumChamber ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_MediumHall](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_MediumHall ``` | AudioUnit |
| To | ``` case reverbRoomType_MediumHall ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_MediumHall2](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall2)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_MediumHall2 ``` | AudioUnit |
| To | ``` case reverbRoomType_MediumHall2 ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_MediumHall3](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumhall3)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_MediumHall3 ``` | AudioUnit |
| To | ``` case reverbRoomType_MediumHall3 ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_MediumRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/kreverbroomtype_mediumroom)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_MediumRoom ``` | AudioUnit |
| To | ``` case reverbRoomType_MediumRoom ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_Plate](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_plate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_Plate ``` | AudioUnit |
| To | ``` case reverbRoomType_Plate ``` | AudioToolbox |

Modified [AUReverbRoomType.reverbRoomType_SmallRoom](https://developer.apple.com/documentation/audiotoolbox/aureverbroomtype/reverbroomtype_smallroom)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ReverbRoomType_SmallRoom ``` | AudioUnit |
| To | ``` case reverbRoomType_SmallRoom ``` | AudioToolbox |

Modified [AUSamplerBankPresetData [struct]](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerBankPresetData.bankLSB](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata/1439236-banklsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerBankPresetData.bankMSB](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata/1439575-bankmsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerBankPresetData.bankURL](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata/1438574-bankurl)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerBankPresetData.presetID](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata/1438317-presetid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerBankPresetData.reserved](https://developer.apple.com/documentation/audiotoolbox/ausamplerbankpresetdata/1438818-reserved)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerInstrumentData [struct]](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerInstrumentData.bankLSB](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata/1439470-banklsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerInstrumentData.bankMSB](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata/1439984-bankmsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerInstrumentData.fileURL](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata/1439725-fileurl)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerInstrumentData.instrumentType](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata/1438669-instrumenttype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSamplerInstrumentData.presetID](https://developer.apple.com/documentation/audiotoolbox/ausamplerinstrumentdata/1440897-presetid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUScheduledAudioSliceFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` struct AUScheduledAudioSliceFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var ScheduledAudioSliceFlag_Complete: AUScheduledAudioSliceFlags { get }     static var ScheduledAudioSliceFlag_BeganToRender: AUScheduledAudioSliceFlags { get }     static var ScheduledAudioSliceFlag_BeganToRenderLate: AUScheduledAudioSliceFlags { get }     static var ScheduledAudioSliceFlag_Loop: AUScheduledAudioSliceFlags { get }     static var ScheduledAudioSliceFlag_Interrupt: AUScheduledAudioSliceFlags { get }     static var ScheduledAudioSliceFlag_InterruptAtLoop: AUScheduledAudioSliceFlags { get } } ``` | OptionSetType | AudioUnit |
| To | ``` struct AUScheduledAudioSliceFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var scheduledAudioSliceFlag_Complete: AUScheduledAudioSliceFlags { get }     static var scheduledAudioSliceFlag_BeganToRender: AUScheduledAudioSliceFlags { get }     static var scheduledAudioSliceFlag_BeganToRenderLate: AUScheduledAudioSliceFlags { get }     static var scheduledAudioSliceFlag_Loop: AUScheduledAudioSliceFlags { get }     static var scheduledAudioSliceFlag_Interrupt: AUScheduledAudioSliceFlags { get }     static var scheduledAudioSliceFlag_InterruptAtLoop: AUScheduledAudioSliceFlags { get }     func intersect(_ other: AUScheduledAudioSliceFlags) -> AUScheduledAudioSliceFlags     func exclusiveOr(_ other: AUScheduledAudioSliceFlags) -> AUScheduledAudioSliceFlags     mutating func unionInPlace(_ other: AUScheduledAudioSliceFlags)     mutating func intersectInPlace(_ other: AUScheduledAudioSliceFlags)     mutating func exclusiveOrInPlace(_ other: AUScheduledAudioSliceFlags)     func isSubsetOf(_ other: AUScheduledAudioSliceFlags) -> Bool     func isDisjointWith(_ other: AUScheduledAudioSliceFlags) -> Bool     func isSupersetOf(_ other: AUScheduledAudioSliceFlags) -> Bool     mutating func subtractInPlace(_ other: AUScheduledAudioSliceFlags)     func isStrictSupersetOf(_ other: AUScheduledAudioSliceFlags) -> Bool     func isStrictSubsetOf(_ other: AUScheduledAudioSliceFlags) -> Bool } extension AUScheduledAudioSliceFlags {     func union(_ other: AUScheduledAudioSliceFlags) -> AUScheduledAudioSliceFlags     func intersection(_ other: AUScheduledAudioSliceFlags) -> AUScheduledAudioSliceFlags     func symmetricDifference(_ other: AUScheduledAudioSliceFlags) -> AUScheduledAudioSliceFlags } extension AUScheduledAudioSliceFlags {     func contains(_ member: AUScheduledAudioSliceFlags) -> Bool     mutating func insert(_ newMember: AUScheduledAudioSliceFlags) -> (inserted: Bool, memberAfterInsert: AUScheduledAudioSliceFlags)     mutating func remove(_ member: AUScheduledAudioSliceFlags) -> AUScheduledAudioSliceFlags?     mutating func update(with newMember: AUScheduledAudioSliceFlags) -> AUScheduledAudioSliceFlags? } extension AUScheduledAudioSliceFlags {     convenience init()     mutating func formUnion(_ other: AUScheduledAudioSliceFlags)     mutating func formIntersection(_ other: AUScheduledAudioSliceFlags)     mutating func formSymmetricDifference(_ other: AUScheduledAudioSliceFlags) } extension AUScheduledAudioSliceFlags {     convenience init<S : Sequence where S.Iterator.Element == AUScheduledAudioSliceFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AUScheduledAudioSliceFlags...)     mutating func subtract(_ other: AUScheduledAudioSliceFlags)     func isSubset(of other: AUScheduledAudioSliceFlags) -> Bool     func isSuperset(of other: AUScheduledAudioSliceFlags) -> Bool     func isDisjoint(with other: AUScheduledAudioSliceFlags) -> Bool     func subtracting(_ other: AUScheduledAudioSliceFlags) -> AUScheduledAudioSliceFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AUScheduledAudioSliceFlags) -> Bool     func isStrictSubset(of other: AUScheduledAudioSliceFlags) -> Bool } ``` | OptionSet | AudioToolbox |

Modified [AUScheduledAudioSliceFlags.init(rawValue: UInt32)](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1438517-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUScheduledAudioSliceFlags.scheduledAudioSliceFlag_BeganToRender](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_begantorender)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var ScheduledAudioSliceFlag_BeganToRender: AUScheduledAudioSliceFlags { get } ``` | AudioUnit |
| To | ``` static var scheduledAudioSliceFlag_BeganToRender: AUScheduledAudioSliceFlags { get } ``` | AudioToolbox |

Modified [AUScheduledAudioSliceFlags.scheduledAudioSliceFlag_BeganToRenderLate](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1438581-scheduledaudiosliceflag_begantor)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var ScheduledAudioSliceFlag_BeganToRenderLate: AUScheduledAudioSliceFlags { get } ``` | AudioUnit |
| To | ``` static var scheduledAudioSliceFlag_BeganToRenderLate: AUScheduledAudioSliceFlags { get } ``` | AudioToolbox |

Modified [AUScheduledAudioSliceFlags.scheduledAudioSliceFlag_Complete](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1440491-scheduledaudiosliceflag_complete)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var ScheduledAudioSliceFlag_Complete: AUScheduledAudioSliceFlags { get } ``` | AudioUnit |
| To | ``` static var scheduledAudioSliceFlag_Complete: AUScheduledAudioSliceFlags { get } ``` | AudioToolbox |

Modified [AUScheduledAudioSliceFlags.scheduledAudioSliceFlag_Interrupt](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_interrupt)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var ScheduledAudioSliceFlag_Interrupt: AUScheduledAudioSliceFlags { get } ``` | AudioUnit |
| To | ``` static var scheduledAudioSliceFlag_Interrupt: AUScheduledAudioSliceFlags { get } ``` | AudioToolbox |

Modified [AUScheduledAudioSliceFlags.scheduledAudioSliceFlag_InterruptAtLoop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/1441008-scheduledaudiosliceflag_interrup)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var ScheduledAudioSliceFlag_InterruptAtLoop: AUScheduledAudioSliceFlags { get } ``` | AudioUnit |
| To | ``` static var scheduledAudioSliceFlag_InterruptAtLoop: AUScheduledAudioSliceFlags { get } ``` | AudioToolbox |

Modified [AUScheduledAudioSliceFlags.scheduledAudioSliceFlag_Loop](https://developer.apple.com/documentation/audiotoolbox/auscheduledaudiosliceflags/kscheduledaudiosliceflag_loop)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var ScheduledAudioSliceFlag_Loop: AUScheduledAudioSliceFlags { get } ``` | AudioUnit |
| To | ``` static var scheduledAudioSliceFlag_Loop: AUScheduledAudioSliceFlags { get } ``` | AudioToolbox |

Modified [AUSpatializationAlgorithm [enum]](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AUSpatializationAlgorithm : UInt32 {     case SpatializationAlgorithm_EqualPowerPanning     case SpatializationAlgorithm_SphericalHead     case SpatializationAlgorithm_HRTF     case SpatializationAlgorithm_SoundField     case SpatializationAlgorithm_VectorBasedPanning     case SpatializationAlgorithm_StereoPassThrough } ``` | AudioUnit |
| To | ``` enum AUSpatializationAlgorithm : UInt32 {     case spatializationAlgorithm_EqualPowerPanning     case spatializationAlgorithm_SphericalHead     case spatializationAlgorithm_HRTF     case spatializationAlgorithm_SoundField     case spatializationAlgorithm_VectorBasedPanning     case spatializationAlgorithm_StereoPassThrough } ``` | AudioToolbox |

Modified [AUSpatializationAlgorithm.spatializationAlgorithm_EqualPowerPanning](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_equalpowerpanning)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatializationAlgorithm_EqualPowerPanning ``` | AudioUnit |
| To | ``` case spatializationAlgorithm_EqualPowerPanning ``` | AudioToolbox |

Modified [AUSpatializationAlgorithm.spatializationAlgorithm_HRTF](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/kspatializationalgorithm_hrtf)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatializationAlgorithm_HRTF ``` | AudioUnit |
| To | ``` case spatializationAlgorithm_HRTF ``` | AudioToolbox |

Modified [AUSpatializationAlgorithm.spatializationAlgorithm_SoundField](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/kspatializationalgorithm_soundfield)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatializationAlgorithm_SoundField ``` | AudioUnit |
| To | ``` case spatializationAlgorithm_SoundField ``` | AudioToolbox |

Modified [AUSpatializationAlgorithm.spatializationAlgorithm_SphericalHead](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_sphericalhead)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatializationAlgorithm_SphericalHead ``` | AudioUnit |
| To | ``` case spatializationAlgorithm_SphericalHead ``` | AudioToolbox |

Modified [AUSpatializationAlgorithm.spatializationAlgorithm_StereoPassThrough](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_stereopassthrough)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatializationAlgorithm_StereoPassThrough ``` | AudioUnit |
| To | ``` case spatializationAlgorithm_StereoPassThrough ``` | AudioToolbox |

Modified [AUSpatializationAlgorithm.spatializationAlgorithm_VectorBasedPanning](https://developer.apple.com/documentation/audiotoolbox/auspatializationalgorithm/spatializationalgorithm_vectorbasedpanning)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatializationAlgorithm_VectorBasedPanning ``` | AudioUnit |
| To | ``` case spatializationAlgorithm_VectorBasedPanning ``` | AudioToolbox |

Modified [AUSpatialMixerAttenuationCurve [enum]](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum AUSpatialMixerAttenuationCurve : UInt32 {     case SpatialMixerAttenuationCurve_Power     case SpatialMixerAttenuationCurve_Exponential     case SpatialMixerAttenuationCurve_Inverse     case SpatialMixerAttenuationCurve_Linear } ``` | AudioUnit |
| To | ``` enum AUSpatialMixerAttenuationCurve : UInt32 {     case spatialMixerAttenuationCurve_Power     case spatialMixerAttenuationCurve_Exponential     case spatialMixerAttenuationCurve_Inverse     case spatialMixerAttenuationCurve_Linear } ``` | AudioToolbox |

Modified [AUSpatialMixerAttenuationCurve.spatialMixerAttenuationCurve_Exponential](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_exponential)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatialMixerAttenuationCurve_Exponential ``` | AudioUnit |
| To | ``` case spatialMixerAttenuationCurve_Exponential ``` | AudioToolbox |

Modified [AUSpatialMixerAttenuationCurve.spatialMixerAttenuationCurve_Inverse](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_inverse)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatialMixerAttenuationCurve_Inverse ``` | AudioUnit |
| To | ``` case spatialMixerAttenuationCurve_Inverse ``` | AudioToolbox |

Modified [AUSpatialMixerAttenuationCurve.spatialMixerAttenuationCurve_Linear](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/spatialmixerattenuationcurve_linear)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatialMixerAttenuationCurve_Linear ``` | AudioUnit |
| To | ``` case spatialMixerAttenuationCurve_Linear ``` | AudioToolbox |

Modified [AUSpatialMixerAttenuationCurve.spatialMixerAttenuationCurve_Power](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerattenuationcurve/kspatialmixerattenuationcurve_power)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case SpatialMixerAttenuationCurve_Power ``` | AudioUnit |
| To | ``` case spatialMixerAttenuationCurve_Power ``` | AudioToolbox |

Modified [AUSpatialMixerRenderingFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` struct AUSpatialMixerRenderingFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var SpatialMixerRenderingFlags_InterAuralDelay: AUSpatialMixerRenderingFlags { get }     static var SpatialMixerRenderingFlags_DistanceAttenuation: AUSpatialMixerRenderingFlags { get } } ``` | OptionSetType | AudioUnit |
| To | ``` struct AUSpatialMixerRenderingFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var spatialMixerRenderingFlags_InterAuralDelay: AUSpatialMixerRenderingFlags { get }     static var spatialMixerRenderingFlags_DistanceAttenuation: AUSpatialMixerRenderingFlags { get }     func intersect(_ other: AUSpatialMixerRenderingFlags) -> AUSpatialMixerRenderingFlags     func exclusiveOr(_ other: AUSpatialMixerRenderingFlags) -> AUSpatialMixerRenderingFlags     mutating func unionInPlace(_ other: AUSpatialMixerRenderingFlags)     mutating func intersectInPlace(_ other: AUSpatialMixerRenderingFlags)     mutating func exclusiveOrInPlace(_ other: AUSpatialMixerRenderingFlags)     func isSubsetOf(_ other: AUSpatialMixerRenderingFlags) -> Bool     func isDisjointWith(_ other: AUSpatialMixerRenderingFlags) -> Bool     func isSupersetOf(_ other: AUSpatialMixerRenderingFlags) -> Bool     mutating func subtractInPlace(_ other: AUSpatialMixerRenderingFlags)     func isStrictSupersetOf(_ other: AUSpatialMixerRenderingFlags) -> Bool     func isStrictSubsetOf(_ other: AUSpatialMixerRenderingFlags) -> Bool } extension AUSpatialMixerRenderingFlags {     func union(_ other: AUSpatialMixerRenderingFlags) -> AUSpatialMixerRenderingFlags     func intersection(_ other: AUSpatialMixerRenderingFlags) -> AUSpatialMixerRenderingFlags     func symmetricDifference(_ other: AUSpatialMixerRenderingFlags) -> AUSpatialMixerRenderingFlags } extension AUSpatialMixerRenderingFlags {     func contains(_ member: AUSpatialMixerRenderingFlags) -> Bool     mutating func insert(_ newMember: AUSpatialMixerRenderingFlags) -> (inserted: Bool, memberAfterInsert: AUSpatialMixerRenderingFlags)     mutating func remove(_ member: AUSpatialMixerRenderingFlags) -> AUSpatialMixerRenderingFlags?     mutating func update(with newMember: AUSpatialMixerRenderingFlags) -> AUSpatialMixerRenderingFlags? } extension AUSpatialMixerRenderingFlags {     convenience init()     mutating func formUnion(_ other: AUSpatialMixerRenderingFlags)     mutating func formIntersection(_ other: AUSpatialMixerRenderingFlags)     mutating func formSymmetricDifference(_ other: AUSpatialMixerRenderingFlags) } extension AUSpatialMixerRenderingFlags {     convenience init<S : Sequence where S.Iterator.Element == AUSpatialMixerRenderingFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AUSpatialMixerRenderingFlags...)     mutating func subtract(_ other: AUSpatialMixerRenderingFlags)     func isSubset(of other: AUSpatialMixerRenderingFlags) -> Bool     func isSuperset(of other: AUSpatialMixerRenderingFlags) -> Bool     func isDisjoint(with other: AUSpatialMixerRenderingFlags) -> Bool     func subtracting(_ other: AUSpatialMixerRenderingFlags) -> AUSpatialMixerRenderingFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AUSpatialMixerRenderingFlags) -> Bool     func isStrictSubset(of other: AUSpatialMixerRenderingFlags) -> Bool } ``` | OptionSet | AudioToolbox |

Modified [AUSpatialMixerRenderingFlags.init(rawValue: UInt32)](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/1438846-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUSpatialMixerRenderingFlags.spatialMixerRenderingFlags_DistanceAttenuation](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_distanceattenuation)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var SpatialMixerRenderingFlags_DistanceAttenuation: AUSpatialMixerRenderingFlags { get } ``` | AudioUnit |
| To | ``` static var spatialMixerRenderingFlags_DistanceAttenuation: AUSpatialMixerRenderingFlags { get } ``` | AudioToolbox |

Modified [AUSpatialMixerRenderingFlags.spatialMixerRenderingFlags_InterAuralDelay](https://developer.apple.com/documentation/audiotoolbox/auspatialmixerrenderingflags/kspatialmixerrenderingflags_interauraldelay)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` static var SpatialMixerRenderingFlags_InterAuralDelay: AUSpatialMixerRenderingFlags { get } ``` | AudioUnit |
| To | ``` static var spatialMixerRenderingFlags_InterAuralDelay: AUSpatialMixerRenderingFlags { get } ``` | AudioToolbox |

Modified [CAFFormatFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/cafformatflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CAFFormatFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var LinearPCMFormatFlagIsFloat: CAFFormatFlags { get }     static var LinearPCMFormatFlagIsLittleEndian: CAFFormatFlags { get } } ``` | OptionSetType |
| To | ``` struct CAFFormatFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var linearPCMFormatFlagIsFloat: CAFFormatFlags { get }     static var linearPCMFormatFlagIsLittleEndian: CAFFormatFlags { get }     func intersect(_ other: CAFFormatFlags) -> CAFFormatFlags     func exclusiveOr(_ other: CAFFormatFlags) -> CAFFormatFlags     mutating func unionInPlace(_ other: CAFFormatFlags)     mutating func intersectInPlace(_ other: CAFFormatFlags)     mutating func exclusiveOrInPlace(_ other: CAFFormatFlags)     func isSubsetOf(_ other: CAFFormatFlags) -> Bool     func isDisjointWith(_ other: CAFFormatFlags) -> Bool     func isSupersetOf(_ other: CAFFormatFlags) -> Bool     mutating func subtractInPlace(_ other: CAFFormatFlags)     func isStrictSupersetOf(_ other: CAFFormatFlags) -> Bool     func isStrictSubsetOf(_ other: CAFFormatFlags) -> Bool } extension CAFFormatFlags {     func union(_ other: CAFFormatFlags) -> CAFFormatFlags     func intersection(_ other: CAFFormatFlags) -> CAFFormatFlags     func symmetricDifference(_ other: CAFFormatFlags) -> CAFFormatFlags } extension CAFFormatFlags {     func contains(_ member: CAFFormatFlags) -> Bool     mutating func insert(_ newMember: CAFFormatFlags) -> (inserted: Bool, memberAfterInsert: CAFFormatFlags)     mutating func remove(_ member: CAFFormatFlags) -> CAFFormatFlags?     mutating func update(with newMember: CAFFormatFlags) -> CAFFormatFlags? } extension CAFFormatFlags {     convenience init()     mutating func formUnion(_ other: CAFFormatFlags)     mutating func formIntersection(_ other: CAFFormatFlags)     mutating func formSymmetricDifference(_ other: CAFFormatFlags) } extension CAFFormatFlags {     convenience init<S : Sequence where S.Iterator.Element == CAFFormatFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CAFFormatFlags...)     mutating func subtract(_ other: CAFFormatFlags)     func isSubset(of other: CAFFormatFlags) -> Bool     func isSuperset(of other: CAFFormatFlags) -> Bool     func isDisjoint(with other: CAFFormatFlags) -> Bool     func subtracting(_ other: CAFFormatFlags) -> CAFFormatFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CAFFormatFlags) -> Bool     func isStrictSubset(of other: CAFFormatFlags) -> Bool } ``` | OptionSet |

Modified [CAFFormatFlags.linearPCMFormatFlagIsFloat](https://developer.apple.com/documentation/audiotoolbox/cafformatflags/kcaflinearpcmformatflagisfloat)

|  | Declaration |
| --- | --- |
| From | ``` static var LinearPCMFormatFlagIsFloat: CAFFormatFlags { get } ``` |
| To | ``` static var linearPCMFormatFlagIsFloat: CAFFormatFlags { get } ``` |

Modified [CAFFormatFlags.linearPCMFormatFlagIsLittleEndian](https://developer.apple.com/documentation/audiotoolbox/cafformatflags/kcaflinearpcmformatflagislittleendian)

|  | Declaration |
| --- | --- |
| From | ``` static var LinearPCMFormatFlagIsLittleEndian: CAFFormatFlags { get } ``` |
| To | ``` static var linearPCMFormatFlagIsLittleEndian: CAFFormatFlags { get } ``` |

Modified [CAFRegionFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/cafregionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CAFRegionFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var LoopEnable: CAFRegionFlags { get }     static var PlayForward: CAFRegionFlags { get }     static var PlayBackward: CAFRegionFlags { get } } ``` | OptionSetType |
| To | ``` struct CAFRegionFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var loopEnable: CAFRegionFlags { get }     static var playForward: CAFRegionFlags { get }     static var playBackward: CAFRegionFlags { get }     func intersect(_ other: CAFRegionFlags) -> CAFRegionFlags     func exclusiveOr(_ other: CAFRegionFlags) -> CAFRegionFlags     mutating func unionInPlace(_ other: CAFRegionFlags)     mutating func intersectInPlace(_ other: CAFRegionFlags)     mutating func exclusiveOrInPlace(_ other: CAFRegionFlags)     func isSubsetOf(_ other: CAFRegionFlags) -> Bool     func isDisjointWith(_ other: CAFRegionFlags) -> Bool     func isSupersetOf(_ other: CAFRegionFlags) -> Bool     mutating func subtractInPlace(_ other: CAFRegionFlags)     func isStrictSupersetOf(_ other: CAFRegionFlags) -> Bool     func isStrictSubsetOf(_ other: CAFRegionFlags) -> Bool } extension CAFRegionFlags {     func union(_ other: CAFRegionFlags) -> CAFRegionFlags     func intersection(_ other: CAFRegionFlags) -> CAFRegionFlags     func symmetricDifference(_ other: CAFRegionFlags) -> CAFRegionFlags } extension CAFRegionFlags {     func contains(_ member: CAFRegionFlags) -> Bool     mutating func insert(_ newMember: CAFRegionFlags) -> (inserted: Bool, memberAfterInsert: CAFRegionFlags)     mutating func remove(_ member: CAFRegionFlags) -> CAFRegionFlags?     mutating func update(with newMember: CAFRegionFlags) -> CAFRegionFlags? } extension CAFRegionFlags {     convenience init()     mutating func formUnion(_ other: CAFRegionFlags)     mutating func formIntersection(_ other: CAFRegionFlags)     mutating func formSymmetricDifference(_ other: CAFRegionFlags) } extension CAFRegionFlags {     convenience init<S : Sequence where S.Iterator.Element == CAFRegionFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CAFRegionFlags...)     mutating func subtract(_ other: CAFRegionFlags)     func isSubset(of other: CAFRegionFlags) -> Bool     func isSuperset(of other: CAFRegionFlags) -> Bool     func isDisjoint(with other: CAFRegionFlags) -> Bool     func subtracting(_ other: CAFRegionFlags) -> CAFRegionFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CAFRegionFlags) -> Bool     func isStrictSubset(of other: CAFRegionFlags) -> Bool } ``` | OptionSet |

Modified [CAFRegionFlags.loopEnable](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/1502336-loopenable)

|  | Declaration |
| --- | --- |
| From | ``` static var LoopEnable: CAFRegionFlags { get } ``` |
| To | ``` static var loopEnable: CAFRegionFlags { get } ``` |

Modified [CAFRegionFlags.playBackward](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/1501777-playbackward)

|  | Declaration |
| --- | --- |
| From | ``` static var PlayBackward: CAFRegionFlags { get } ``` |
| To | ``` static var playBackward: CAFRegionFlags { get } ``` |

Modified [CAFRegionFlags.playForward](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/kcafregionflag_playforward)

|  | Declaration |
| --- | --- |
| From | ``` static var PlayForward: CAFRegionFlags { get } ``` |
| To | ``` static var playForward: CAFRegionFlags { get } ``` |

Modified [ExtendedAudioFormatInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/extendedaudioformatinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct ExtendedAudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     var mClassDescription: AudioClassDescription } ``` |
| To | ``` struct ExtendedAudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafeRawPointer     var mMagicCookieSize: UInt32     var mClassDescription: AudioClassDescription } ``` |

Modified [ExtendedAudioFormatInfo.mMagicCookie](https://developer.apple.com/documentation/audiotoolbox/extendedaudioformatinfo/1503054-mmagiccookie)

|  | Declaration |
| --- | --- |
| From | ``` var mMagicCookie: UnsafePointer<Void> ``` |
| To | ``` var mMagicCookie: UnsafeRawPointer ``` |

Modified [HostCallbackInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct HostCallbackInfo {     var hostUserData: UnsafeMutablePointer<Void>     var beatAndTempoProc: HostCallback_GetBeatAndTempo?     var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation?     var transportStateProc: HostCallback_GetTransportState?     var transportStateProc2: HostCallback_GetTransportState2?     init()     init(hostUserData hostUserData: UnsafeMutablePointer<Void>, beatAndTempoProc beatAndTempoProc: HostCallback_GetBeatAndTempo?, musicalTimeLocationProc musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation?, transportStateProc transportStateProc: HostCallback_GetTransportState?, transportStateProc2 transportStateProc2: HostCallback_GetTransportState2?) } ``` | AudioUnit |
| To | ``` struct HostCallbackInfo {     var hostUserData: UnsafeMutableRawPointer?     var beatAndTempoProc: AudioToolbox.HostCallback_GetBeatAndTempo?     var musicalTimeLocationProc: AudioToolbox.HostCallback_GetMusicalTimeLocation?     var transportStateProc: AudioToolbox.HostCallback_GetTransportState?     var transportStateProc2: AudioToolbox.HostCallback_GetTransportState2?     init()     init(hostUserData hostUserData: UnsafeMutableRawPointer?, beatAndTempoProc beatAndTempoProc: AudioToolbox.HostCallback_GetBeatAndTempo?, musicalTimeLocationProc musicalTimeLocationProc: AudioToolbox.HostCallback_GetMusicalTimeLocation?, transportStateProc transportStateProc: AudioToolbox.HostCallback_GetTransportState?, transportStateProc2 transportStateProc2: AudioToolbox.HostCallback_GetTransportState2?) } ``` | AudioToolbox |

Modified [HostCallbackInfo.beatAndTempoProc](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439047-beatandtempoproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var beatAndTempoProc: HostCallback_GetBeatAndTempo? ``` | AudioUnit |
| To | ``` var beatAndTempoProc: AudioToolbox.HostCallback_GetBeatAndTempo? ``` | AudioToolbox |

Modified [HostCallbackInfo.hostUserData](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439756-hostuserdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var hostUserData: UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` var hostUserData: UnsafeMutableRawPointer? ``` | AudioToolbox |

Modified [HostCallbackInfo.init()](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439533-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [HostCallbackInfo.musicalTimeLocationProc](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1440190-musicaltimelocationproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation? ``` | AudioUnit |
| To | ``` var musicalTimeLocationProc: AudioToolbox.HostCallback_GetMusicalTimeLocation? ``` | AudioToolbox |

Modified [HostCallbackInfo.transportStateProc](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439276-transportstateproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var transportStateProc: HostCallback_GetTransportState? ``` | AudioUnit |
| To | ``` var transportStateProc: AudioToolbox.HostCallback_GetTransportState? ``` | AudioToolbox |

Modified [HostCallbackInfo.transportStateProc2](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo/1439489-transportstateproc2)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var transportStateProc2: HostCallback_GetTransportState2? ``` | AudioUnit |
| To | ``` var transportStateProc2: AudioToolbox.HostCallback_GetTransportState2? ``` | AudioToolbox |

Modified [MixerDistanceParams [struct]](https://developer.apple.com/documentation/audiotoolbox/mixerdistanceparams)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MixerDistanceParams.init()](https://developer.apple.com/documentation/audiotoolbox/mixerdistanceparams/1439739-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MixerDistanceParams.init(mReferenceDistance: Float32, mMaxDistance: Float32, mMaxAttenuation: Float32)](https://developer.apple.com/documentation/audiotoolbox/mixerdistanceparams/1438679-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MixerDistanceParams.mMaxAttenuation](https://developer.apple.com/documentation/audiotoolbox/mixerdistanceparams/1440728-mmaxattenuation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MixerDistanceParams.mMaxDistance](https://developer.apple.com/documentation/audiotoolbox/mixerdistanceparams/1439422-mmaxdistance)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MixerDistanceParams.mReferenceDistance](https://developer.apple.com/documentation/audiotoolbox/mixerdistanceparams/1440385-mreferencedistance)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceNoteParams [struct]](https://developer.apple.com/documentation/audiotoolbox/musicdevicenoteparams)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceNoteParams.argCount](https://developer.apple.com/documentation/audiotoolbox/musicdevicenoteparams/1439846-argcount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceNoteParams.init()](https://developer.apple.com/documentation/audiotoolbox/musicdevicenoteparams/1439712-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceNoteParams.init(argCount: UInt32, mPitch: Float32, mVelocity: Float32, mControls: (NoteParamsControlValue))](https://developer.apple.com/documentation/audiotoolbox/musicdevicenoteparams/1438301-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceNoteParams.mControls](https://developer.apple.com/documentation/audiotoolbox/musicdevicenoteparams/1440140-mcontrols)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceNoteParams.mPitch](https://developer.apple.com/documentation/audiotoolbox/musicdevicenoteparams/1439555-mpitch)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceNoteParams.mVelocity](https://developer.apple.com/documentation/audiotoolbox/musicdevicenoteparams/1440066-mvelocity)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceStdNoteParams [struct]](https://developer.apple.com/documentation/audiotoolbox/musicdevicestdnoteparams)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceStdNoteParams.argCount](https://developer.apple.com/documentation/audiotoolbox/musicdevicestdnoteparams/1439981-argcount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceStdNoteParams.init()](https://developer.apple.com/documentation/audiotoolbox/musicdevicestdnoteparams/1438585-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceStdNoteParams.init(argCount: UInt32, mPitch: Float32, mVelocity: Float32)](https://developer.apple.com/documentation/audiotoolbox/musicdevicestdnoteparams/1440545-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceStdNoteParams.mPitch](https://developer.apple.com/documentation/audiotoolbox/musicdevicestdnoteparams/1438974-mpitch)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceStdNoteParams.mVelocity](https://developer.apple.com/documentation/audiotoolbox/musicdevicestdnoteparams/1440347-mvelocity)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicSequenceFileFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MusicSequenceFileFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Default: MusicSequenceFileFlags { get }     static var EraseFile: MusicSequenceFileFlags { get } } ``` | OptionSetType |
| To | ``` struct MusicSequenceFileFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var `default`: MusicSequenceFileFlags { get }     static var eraseFile: MusicSequenceFileFlags { get }     func intersect(_ other: MusicSequenceFileFlags) -> MusicSequenceFileFlags     func exclusiveOr(_ other: MusicSequenceFileFlags) -> MusicSequenceFileFlags     mutating func unionInPlace(_ other: MusicSequenceFileFlags)     mutating func intersectInPlace(_ other: MusicSequenceFileFlags)     mutating func exclusiveOrInPlace(_ other: MusicSequenceFileFlags)     func isSubsetOf(_ other: MusicSequenceFileFlags) -> Bool     func isDisjointWith(_ other: MusicSequenceFileFlags) -> Bool     func isSupersetOf(_ other: MusicSequenceFileFlags) -> Bool     mutating func subtractInPlace(_ other: MusicSequenceFileFlags)     func isStrictSupersetOf(_ other: MusicSequenceFileFlags) -> Bool     func isStrictSubsetOf(_ other: MusicSequenceFileFlags) -> Bool } extension MusicSequenceFileFlags {     func union(_ other: MusicSequenceFileFlags) -> MusicSequenceFileFlags     func intersection(_ other: MusicSequenceFileFlags) -> MusicSequenceFileFlags     func symmetricDifference(_ other: MusicSequenceFileFlags) -> MusicSequenceFileFlags } extension MusicSequenceFileFlags {     func contains(_ member: MusicSequenceFileFlags) -> Bool     mutating func insert(_ newMember: MusicSequenceFileFlags) -> (inserted: Bool, memberAfterInsert: MusicSequenceFileFlags)     mutating func remove(_ member: MusicSequenceFileFlags) -> MusicSequenceFileFlags?     mutating func update(with newMember: MusicSequenceFileFlags) -> MusicSequenceFileFlags? } extension MusicSequenceFileFlags {     convenience init()     mutating func formUnion(_ other: MusicSequenceFileFlags)     mutating func formIntersection(_ other: MusicSequenceFileFlags)     mutating func formSymmetricDifference(_ other: MusicSequenceFileFlags) } extension MusicSequenceFileFlags {     convenience init<S : Sequence where S.Iterator.Element == MusicSequenceFileFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MusicSequenceFileFlags...)     mutating func subtract(_ other: MusicSequenceFileFlags)     func isSubset(of other: MusicSequenceFileFlags) -> Bool     func isSuperset(of other: MusicSequenceFileFlags) -> Bool     func isDisjoint(with other: MusicSequenceFileFlags) -> Bool     func subtracting(_ other: MusicSequenceFileFlags) -> MusicSequenceFileFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: MusicSequenceFileFlags) -> Bool     func isStrictSubset(of other: MusicSequenceFileFlags) -> Bool } ``` | OptionSet |

Modified [MusicSequenceFileFlags.eraseFile](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags/kmusicsequencefileflags_erasefile)

|  | Declaration |
| --- | --- |
| From | ``` static var EraseFile: MusicSequenceFileFlags { get } ``` |
| To | ``` static var eraseFile: MusicSequenceFileFlags { get } ``` |

Modified [MusicSequenceFileTypeID [enum]](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid)

|  | Declaration |
| --- | --- |
| From | ``` enum MusicSequenceFileTypeID : UInt32 {     case AnyType     case MIDIType     case iMelodyType } ``` |
| To | ``` enum MusicSequenceFileTypeID : UInt32 {     case anyType     case midiType     case iMelodyType } ``` |

Modified [MusicSequenceFileTypeID.anyType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/anytype)

|  | Declaration |
| --- | --- |
| From | ``` case AnyType ``` |
| To | ``` case anyType ``` |

Modified [MusicSequenceFileTypeID.midiType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/kmusicsequencefile_miditype)

|  | Declaration |
| --- | --- |
| From | ``` case MIDIType ``` |
| To | ``` case midiType ``` |

Modified [MusicSequenceLoadFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MusicSequenceLoadFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var SMF_PreserveTracks: MusicSequenceLoadFlags { get }     static var SMF_ChannelsToTracks: MusicSequenceLoadFlags { get } } ``` | OptionSetType |
| To | ``` struct MusicSequenceLoadFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var smf_PreserveTracks: MusicSequenceLoadFlags { get }     static var smf_ChannelsToTracks: MusicSequenceLoadFlags { get }     func intersect(_ other: MusicSequenceLoadFlags) -> MusicSequenceLoadFlags     func exclusiveOr(_ other: MusicSequenceLoadFlags) -> MusicSequenceLoadFlags     mutating func unionInPlace(_ other: MusicSequenceLoadFlags)     mutating func intersectInPlace(_ other: MusicSequenceLoadFlags)     mutating func exclusiveOrInPlace(_ other: MusicSequenceLoadFlags)     func isSubsetOf(_ other: MusicSequenceLoadFlags) -> Bool     func isDisjointWith(_ other: MusicSequenceLoadFlags) -> Bool     func isSupersetOf(_ other: MusicSequenceLoadFlags) -> Bool     mutating func subtractInPlace(_ other: MusicSequenceLoadFlags)     func isStrictSupersetOf(_ other: MusicSequenceLoadFlags) -> Bool     func isStrictSubsetOf(_ other: MusicSequenceLoadFlags) -> Bool } extension MusicSequenceLoadFlags {     func union(_ other: MusicSequenceLoadFlags) -> MusicSequenceLoadFlags     func intersection(_ other: MusicSequenceLoadFlags) -> MusicSequenceLoadFlags     func symmetricDifference(_ other: MusicSequenceLoadFlags) -> MusicSequenceLoadFlags } extension MusicSequenceLoadFlags {     func contains(_ member: MusicSequenceLoadFlags) -> Bool     mutating func insert(_ newMember: MusicSequenceLoadFlags) -> (inserted: Bool, memberAfterInsert: MusicSequenceLoadFlags)     mutating func remove(_ member: MusicSequenceLoadFlags) -> MusicSequenceLoadFlags?     mutating func update(with newMember: MusicSequenceLoadFlags) -> MusicSequenceLoadFlags? } extension MusicSequenceLoadFlags {     convenience init()     mutating func formUnion(_ other: MusicSequenceLoadFlags)     mutating func formIntersection(_ other: MusicSequenceLoadFlags)     mutating func formSymmetricDifference(_ other: MusicSequenceLoadFlags) } extension MusicSequenceLoadFlags {     convenience init<S : Sequence where S.Iterator.Element == MusicSequenceLoadFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MusicSequenceLoadFlags...)     mutating func subtract(_ other: MusicSequenceLoadFlags)     func isSubset(of other: MusicSequenceLoadFlags) -> Bool     func isSuperset(of other: MusicSequenceLoadFlags) -> Bool     func isDisjoint(with other: MusicSequenceLoadFlags) -> Bool     func subtracting(_ other: MusicSequenceLoadFlags) -> MusicSequenceLoadFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: MusicSequenceLoadFlags) -> Bool     func isStrictSubset(of other: MusicSequenceLoadFlags) -> Bool } ``` | OptionSet |

Modified [MusicSequenceLoadFlags.smf_ChannelsToTracks](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags/kmusicsequenceloadsmf_channelstotracks)

|  | Declaration |
| --- | --- |
| From | ``` static var SMF_ChannelsToTracks: MusicSequenceLoadFlags { get } ``` |
| To | ``` static var smf_ChannelsToTracks: MusicSequenceLoadFlags { get } ``` |

Modified [MusicSequenceLoadFlags.smf_PreserveTracks](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags/kmusicsequenceloadsmf_preservetracks)

|  | Declaration |
| --- | --- |
| From | ``` static var SMF_PreserveTracks: MusicSequenceLoadFlags { get } ``` |
| To | ``` static var smf_PreserveTracks: MusicSequenceLoadFlags { get } ``` |

Modified [MusicSequenceType [enum]](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype)

|  | Declaration |
| --- | --- |
| From | ``` enum MusicSequenceType : UInt32 {     case Beats     case Seconds     case Samples } ``` |
| To | ``` enum MusicSequenceType : UInt32 {     case beats     case seconds     case samples } ``` |

Modified [MusicSequenceType.beats](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/beats)

|  | Declaration |
| --- | --- |
| From | ``` case Beats ``` |
| To | ``` case beats ``` |

Modified [MusicSequenceType.samples](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/samples)

|  | Declaration |
| --- | --- |
| From | ``` case Samples ``` |
| To | ``` case samples ``` |

Modified [MusicSequenceType.seconds](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/seconds)

|  | Declaration |
| --- | --- |
| From | ``` case Seconds ``` |
| To | ``` case seconds ``` |

Modified [NoteParamsControlValue [struct]](https://developer.apple.com/documentation/audiotoolbox/noteparamscontrolvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [NoteParamsControlValue.init()](https://developer.apple.com/documentation/audiotoolbox/noteparamscontrolvalue/1440442-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [NoteParamsControlValue.init(mID: AudioUnitParameterID, mValue: AudioUnitParameterValue)](https://developer.apple.com/documentation/audiotoolbox/noteparamscontrolvalue/1440567-init)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [NoteParamsControlValue.mID](https://developer.apple.com/documentation/audiotoolbox/noteparamscontrolvalue/1440248-mid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [NoteParamsControlValue.mValue](https://developer.apple.com/documentation/audiotoolbox/noteparamscontrolvalue/1440240-mvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioFileRegion [struct]](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct ScheduledAudioFileRegion {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioFileRegionCompletionProc?     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mAudioFile: COpaquePointer     var mLoopCount: UInt32     var mStartFrame: Int64     var mFramesToPlay: UInt32 } ``` | AudioUnit |
| To | ``` struct ScheduledAudioFileRegion {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: AudioToolbox.ScheduledAudioFileRegionCompletionProc?     var mCompletionProcUserData: UnsafeMutableRawPointer?     var mAudioFile: OpaquePointer     var mLoopCount: UInt32     var mStartFrame: Int64     var mFramesToPlay: UInt32 } ``` | AudioToolbox |

Modified [ScheduledAudioFileRegion.mAudioFile](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion/1440018-maudiofile)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var mAudioFile: COpaquePointer ``` | AudioUnit |
| To | ``` var mAudioFile: OpaquePointer ``` | AudioToolbox |

Modified [ScheduledAudioFileRegion.mCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion/1440737-mcompletionproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var mCompletionProc: ScheduledAudioFileRegionCompletionProc? ``` | AudioUnit |
| To | ``` var mCompletionProc: AudioToolbox.ScheduledAudioFileRegionCompletionProc? ``` | AudioToolbox |

Modified [ScheduledAudioFileRegion.mCompletionProcUserData](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion/1439064-mcompletionprocuserdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var mCompletionProcUserData: UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` var mCompletionProcUserData: UnsafeMutableRawPointer? ``` | AudioToolbox |

Modified [ScheduledAudioFileRegion.mFramesToPlay](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion/1440651-mframestoplay)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioFileRegion.mLoopCount](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion/1439526-mloopcount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioFileRegion.mStartFrame](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion/1438528-mstartframe)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioFileRegion.mTimeStamp](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregion/1440275-mtimestamp)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioSlice [struct]](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` struct ScheduledAudioSlice {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: ScheduledAudioSliceCompletionProc?     var mCompletionProcUserData: UnsafeMutablePointer<Void>     var mFlags: AUScheduledAudioSliceFlags     var mReserved: UInt32     var mReserved2: UnsafeMutablePointer<Void>     var mNumberFrames: UInt32     var mBufferList: UnsafeMutablePointer<AudioBufferList> } ``` | AudioUnit |
| To | ``` struct ScheduledAudioSlice {     var mTimeStamp: AudioTimeStamp     var mCompletionProc: AudioToolbox.ScheduledAudioSliceCompletionProc?     var mCompletionProcUserData: UnsafeMutableRawPointer     var mFlags: AUScheduledAudioSliceFlags     var mReserved: UInt32     var mReserved2: UnsafeMutableRawPointer?     var mNumberFrames: UInt32     var mBufferList: UnsafeMutablePointer<AudioBufferList> } ``` | AudioToolbox |

Modified [ScheduledAudioSlice.mBufferList](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1439547-mbufferlist)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioSlice.mCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1440285-mcompletionproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var mCompletionProc: ScheduledAudioSliceCompletionProc? ``` | AudioUnit |
| To | ``` var mCompletionProc: AudioToolbox.ScheduledAudioSliceCompletionProc? ``` | AudioToolbox |

Modified [ScheduledAudioSlice.mCompletionProcUserData](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1439461-mcompletionprocuserdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var mCompletionProcUserData: UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` var mCompletionProcUserData: UnsafeMutableRawPointer ``` | AudioToolbox |

Modified [ScheduledAudioSlice.mFlags](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1438587-mflags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioSlice.mNumberFrames](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1440953-mnumberframes)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioSlice.mReserved](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1438307-mreserved)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioSlice.mReserved2](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1440188-mreserved2)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var mReserved2: UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` var mReserved2: UnsafeMutableRawPointer? ``` | AudioToolbox |

Modified [ScheduledAudioSlice.mTimeStamp](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslice/1440307-mtimestamp)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioChannelCount](https://developer.apple.com/documentation/audiotoolbox/auaudiochannelcount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioFrameCount](https://developer.apple.com/documentation/audiotoolbox/auaudioframecount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUAudioUnitStatus](https://developer.apple.com/documentation/audiotoolbox/auaudiounitstatus)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUDIO_UNIT_VERSION](https://developer.apple.com/documentation/audiotoolbox/audio_unit_version)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponent](https://developer.apple.com/documentation/audiotoolbox/audiocomponent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioComponent = COpaquePointer ``` | AudioUnit |
| To | ``` typealias AudioComponent = OpaquePointer ``` | AudioToolbox |

Modified [AudioComponentCopyName(_: AudioComponent, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1410519-audiocomponentcopyname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentCount(_: UnsafePointer<AudioComponentDescription>) -> UInt32](https://developer.apple.com/documentation/audiotoolbox/1410476-audiocomponentcount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentFactoryFunction](https://developer.apple.com/documentation/audiotoolbox/audiocomponentfactoryfunction)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioComponentFactoryFunction = (UnsafePointer<AudioComponentDescription>) -> UnsafeMutablePointer<AudioComponentPlugInInterface> ``` | AudioUnit |
| To | ``` typealias AudioComponentFactoryFunction = (UnsafePointer<AudioComponentDescription>) -> UnsafeMutablePointer<AudioComponentPlugInInterface>? ``` | AudioToolbox |

Modified [AudioComponentFindNext(_: AudioComponent?, _: UnsafePointer<AudioComponentDescription>) -> AudioComponent?](https://developer.apple.com/documentation/audiotoolbox/1410445-audiocomponentfindnext)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioComponentFindNext(_ inComponent: AudioComponent, _ inDesc: UnsafePointer<AudioComponentDescription>) -> AudioComponent ``` | AudioUnit |
| To | ``` func AudioComponentFindNext(_ inComponent: AudioComponent?, _ inDesc: UnsafePointer<AudioComponentDescription>) -> AudioComponent? ``` | AudioToolbox |

Modified [AudioComponentGetDescription(_: AudioComponent, _: UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1410523-audiocomponentgetdescription)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentGetIcon(_: AudioComponent, _: Float) -> UIImage?](https://developer.apple.com/documentation/audiotoolbox/1410443-audiocomponentgeticon)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentGetLastActiveTime(_: AudioComponent) -> CFAbsoluteTime](https://developer.apple.com/documentation/audiotoolbox/1619499-audiocomponentgetlastactivetime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentGetVersion(_: AudioComponent, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1410441-audiocomponentgetversion)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentInstance](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstance)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioComponentInstance = COpaquePointer ``` | AudioUnit |
| To | ``` typealias AudioComponentInstance = OpaquePointer ``` | AudioToolbox |

Modified [AudioComponentInstanceCanDo(_: AudioComponentInstance, _: Int16) -> Bool](https://developer.apple.com/documentation/audiotoolbox/1410504-audiocomponentinstancecando)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentInstanceDispose(_: AudioComponentInstance) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1410508-audiocomponentinstancedispose)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentInstanceGetComponent(_: AudioComponentInstance) -> AudioComponent](https://developer.apple.com/documentation/audiotoolbox/1410447-audiocomponentinstancegetcompone)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioComponentInstanceNew(_: AudioComponent, _: UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1410465-audiocomponentinstancenew)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioComponentInstanceNew(_ inComponent: AudioComponent, _ outInstance: UnsafeMutablePointer<AudioComponentInstance>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioComponentInstanceNew(_ inComponent: AudioComponent, _ outInstance: UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus ``` | AudioToolbox |

Modified [AudioComponentInstantiate(_: AudioComponent, _: AudioComponentInstantiationOptions, _: (AudioComponentInstance?, OSStatus) -> Swift.Void)](https://developer.apple.com/documentation/audiotoolbox/1410517-audiocomponentinstantiate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioComponentInstantiate(_ inComponent: AudioComponent, _ inOptions: AudioComponentInstantiationOptions, _ inCompletionHandler: (AudioComponentInstance, OSStatus) -> Void) ``` | AudioUnit |
| To | ``` func AudioComponentInstantiate(_ inComponent: AudioComponent, _ inOptions: AudioComponentInstantiationOptions, _ inCompletionHandler: @escaping (AudioComponentInstance?, OSStatus) -> Swift.Void) ``` | AudioToolbox |

Modified [AudioComponentMethod](https://developer.apple.com/documentation/audiotoolbox/audiocomponentmethod)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioComponentMethod = COpaquePointer ``` | AudioUnit |
| To | ``` typealias AudioComponentMethod = OpaquePointer ``` | AudioToolbox |

Modified [AudioComponentRegister(_: UnsafePointer<AudioComponentDescription>, _: CFString, _: UInt32, _: AudioToolbox.AudioComponentFactoryFunction) -> AudioComponent](https://developer.apple.com/documentation/audiotoolbox/1410487-audiocomponentregister)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioComponentRegister(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString, _ inVersion: UInt32, _ inFactory: AudioComponentFactoryFunction) -> AudioComponent ``` | AudioUnit |
| To | ``` func AudioComponentRegister(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString, _ inVersion: UInt32, _ inFactory: AudioToolbox.AudioComponentFactoryFunction) -> AudioComponent ``` | AudioToolbox |

Modified [AudioConverterComplexInputDataProc](https://developer.apple.com/documentation/audiotoolbox/audioconvertercomplexinputdataproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterComplexInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias AudioConverterComplexInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>?>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioConverterConvertBuffer(_: AudioConverterRef, _: UInt32, _: UnsafeRawPointer, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503345-audioconverterconvertbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func AudioConverterConvertBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataSize: UInt32, _ inInputData: UnsafePointer<Void>, _ ioOutputDataSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioConverterConvertBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataSize: UInt32, _ inInputData: UnsafeRawPointer, _ ioOutputDataSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [AudioConverterFillComplexBuffer(_: AudioConverterRef, _: AudioToolbox.AudioConverterComplexInputDataProc, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<AudioBufferList>, _: UnsafeMutablePointer<AudioStreamPacketDescription>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503098-audioconverterfillcomplexbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func AudioConverterFillComplexBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataProc: AudioConverterComplexInputDataProc, _ inInputDataProcUserData: UnsafeMutablePointer<Void>, _ ioOutputDataPacketSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>) -> OSStatus ``` |
| To | ``` func AudioConverterFillComplexBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataProc: AudioToolbox.AudioConverterComplexInputDataProc, _ inInputDataProcUserData: UnsafeMutableRawPointer?, _ ioOutputDataPacketSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>?) -> OSStatus ``` |

Modified [AudioConverterGetProperty(_: AudioConverterRef, _: AudioConverterPropertyID, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502731-audioconvertergetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioConverterGetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioConverterGetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [AudioConverterGetPropertyInfo(_: AudioConverterRef, _: AudioConverterPropertyID, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502563-audioconvertergetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [AudioConverterInputDataProc](https://developer.apple.com/documentation/audiotoolbox/audioconverterinputdataproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias AudioConverterInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutableRawPointer>, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioConverterNew(_: UnsafePointer<AudioStreamBasicDescription>, _: UnsafePointer<AudioStreamBasicDescription>, _: UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502936-audioconverternew)

|  | Declaration |
| --- | --- |
| From | ``` func AudioConverterNew(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef>) -> OSStatus ``` |
| To | ``` func AudioConverterNew(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus ``` |

Modified [AudioConverterNewSpecific(_: UnsafePointer<AudioStreamBasicDescription>, _: UnsafePointer<AudioStreamBasicDescription>, _: UInt32, _: UnsafePointer<AudioClassDescription>, _: UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503356-audioconverternewspecific)

|  | Declaration |
| --- | --- |
| From | ``` func AudioConverterNewSpecific(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ inNumberClassDescriptions: UInt32, _ inClassDescriptions: UnsafePointer<AudioClassDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef>) -> OSStatus ``` |
| To | ``` func AudioConverterNewSpecific(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ inNumberClassDescriptions: UInt32, _ inClassDescriptions: UnsafePointer<AudioClassDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus ``` |

Modified [AudioConverterRef](https://developer.apple.com/documentation/audiotoolbox/audioconverterref)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterRef = COpaquePointer ``` |
| To | ``` typealias AudioConverterRef = OpaquePointer ``` |

Modified [AudioConverterSetProperty(_: AudioConverterRef, _: AudioConverterPropertyID, _: UInt32, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501675-audioconvertersetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioConverterSetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioConverterSetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus ``` |

Modified [AudioFile_GetSizeProc](https://developer.apple.com/documentation/audiotoolbox/audiofile_getsizeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_GetSizeProc = (UnsafeMutablePointer<Void>) -> Int64 ``` |
| To | ``` typealias AudioFile_GetSizeProc = (UnsafeMutableRawPointer) -> Int64 ``` |

Modified [AudioFile_ReadProc](https://developer.apple.com/documentation/audiotoolbox/audiofile_readproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_ReadProc = (UnsafeMutablePointer<Void>, Int64, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` typealias AudioFile_ReadProc = (UnsafeMutableRawPointer, Int64, UInt32, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioFile_SetSizeProc](https://developer.apple.com/documentation/audiotoolbox/audiofile_setsizeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_SetSizeProc = (UnsafeMutablePointer<Void>, Int64) -> OSStatus ``` |
| To | ``` typealias AudioFile_SetSizeProc = (UnsafeMutableRawPointer, Int64) -> OSStatus ``` |

Modified [AudioFile_WriteProc](https://developer.apple.com/documentation/audiotoolbox/audiofile_writeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_WriteProc = (UnsafeMutablePointer<Void>, Int64, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` typealias AudioFile_WriteProc = (UnsafeMutableRawPointer, Int64, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioFileCreateWithURL(_: CFURL, _: AudioFileTypeID, _: UnsafePointer<AudioStreamBasicDescription>, _: AudioFileFlags, _: UnsafeMutablePointer<AudioFileID?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502333-audiofilecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileCreateWithURL(_ inFileRef: CFURL, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: AudioFileFlags, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |
| To | ``` func AudioFileCreateWithURL(_ inFileRef: CFURL, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: AudioFileFlags, _ outAudioFile: UnsafeMutablePointer<AudioFileID?>) -> OSStatus ``` |

Modified [AudioFileGetGlobalInfo(_: AudioFilePropertyID, _: UInt32, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501938-audiofilegetglobalinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileGetGlobalInfo(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeMutablePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileGetGlobalInfo(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeMutableRawPointer?, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [AudioFileGetGlobalInfoSize(_: AudioFilePropertyID, _: UInt32, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502463-audiofilegetglobalinfosize)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileGetGlobalInfoSize(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeMutablePointer<Void>, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func AudioFileGetGlobalInfoSize(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeMutableRawPointer?, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioFileGetProperty(_: AudioFileID, _: AudioFilePropertyID, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502718-audiofilegetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileGetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileGetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [AudioFileGetPropertyInfo(_: AudioFileID, _: AudioFilePropertyID, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501691-audiofilegetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileGetPropertyInfo(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ outDataSize: UnsafeMutablePointer<UInt32>, _ isWritable: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func AudioFileGetPropertyInfo(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ outDataSize: UnsafeMutablePointer<UInt32>?, _ isWritable: UnsafeMutablePointer<UInt32>?) -> OSStatus ``` |

Modified [AudioFileGetUserData(_: AudioFileID, _: UInt32, _: UInt32, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501911-audiofilegetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileGetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileGetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [AudioFileID](https://developer.apple.com/documentation/audiotoolbox/audiofileid)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileID = COpaquePointer ``` |
| To | ``` typealias AudioFileID = OpaquePointer ``` |

Modified [AudioFileInitializeWithCallbacks(_: UnsafeMutableRawPointer, _: AudioToolbox.AudioFile_ReadProc, _: AudioToolbox.AudioFile_WriteProc, _: AudioToolbox.AudioFile_GetSizeProc, _: AudioToolbox.AudioFile_SetSizeProc, _: AudioFileTypeID, _: UnsafePointer<AudioStreamBasicDescription>, _: AudioFileFlags, _: UnsafeMutablePointer<AudioFileID?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502895-audiofileinitializewithcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileInitializeWithCallbacks(_ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: AudioFileFlags, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |
| To | ``` func AudioFileInitializeWithCallbacks(_ inClientData: UnsafeMutableRawPointer, _ inReadFunc: AudioToolbox.AudioFile_ReadProc, _ inWriteFunc: AudioToolbox.AudioFile_WriteProc, _ inGetSizeFunc: AudioToolbox.AudioFile_GetSizeProc, _ inSetSizeFunc: AudioToolbox.AudioFile_SetSizeProc, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: AudioFileFlags, _ outAudioFile: UnsafeMutablePointer<AudioFileID?>) -> OSStatus ``` |

Modified [AudioFileOpenURL(_: CFURL, _: AudioFilePermissions, _: AudioFileTypeID, _: UnsafeMutablePointer<AudioFileID?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502304-audiofileopenurl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileOpenURL(_ inFileRef: CFURL, _ inPermissions: AudioFilePermissions, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |
| To | ``` func AudioFileOpenURL(_ inFileRef: CFURL, _ inPermissions: AudioFilePermissions, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID?>) -> OSStatus ``` |

Modified [AudioFileOpenWithCallbacks(_: UnsafeMutableRawPointer, _: AudioToolbox.AudioFile_ReadProc, _: AudioToolbox.AudioFile_WriteProc?, _: AudioToolbox.AudioFile_GetSizeProc, _: AudioToolbox.AudioFile_SetSizeProc?, _: AudioFileTypeID, _: UnsafeMutablePointer<AudioFileID?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502746-audiofileopenwithcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileOpenWithCallbacks(_ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc?, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc?, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |
| To | ``` func AudioFileOpenWithCallbacks(_ inClientData: UnsafeMutableRawPointer, _ inReadFunc: AudioToolbox.AudioFile_ReadProc, _ inWriteFunc: AudioToolbox.AudioFile_WriteProc?, _ inGetSizeFunc: AudioToolbox.AudioFile_GetSizeProc, _ inSetSizeFunc: AudioToolbox.AudioFile_SetSizeProc?, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID?>) -> OSStatus ``` |

Modified [AudioFileReadBytes(_: AudioFileID, _: Bool, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503247-audiofilereadbytes)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileReadBytes(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileReadBytes(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [AudioFileReadPacketData(_: AudioFileID, _: Bool, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<AudioStreamPacketDescription>?, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502788-audiofilereadpacketdata)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileReadPacketData(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileReadPacketData(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioFileReadPackets(_: AudioFileID, _: Bool, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<AudioStreamPacketDescription>?, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503274-audiofilereadpackets)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileReadPackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileReadPackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioFileSetProperty(_: AudioFileID, _: AudioFilePropertyID, _: UInt32, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503020-audiofilesetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileSetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ inDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileSetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ inDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus ``` |

Modified [AudioFileSetUserData(_: AudioFileID, _: UInt32, _: UInt32, _: UInt32, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502308-audiofilesetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileSetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inUserDataSize: UInt32, _ inUserData: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileSetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inUserDataSize: UInt32, _ inUserData: UnsafeRawPointer) -> OSStatus ``` |

Modified [AudioFileStream_PacketsProc](https://developer.apple.com/documentation/audiotoolbox/audiofilestream_packetsproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileStream_PacketsProc = (UnsafeMutablePointer<Void>, UInt32, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<AudioStreamPacketDescription>) -> Void ``` |
| To | ``` typealias AudioFileStream_PacketsProc = (UnsafeMutableRawPointer, UInt32, UInt32, UnsafeRawPointer, UnsafeMutablePointer<AudioStreamPacketDescription>) -> Swift.Void ``` |

Modified [AudioFileStream_PropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiofilestream_propertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileStream_PropertyListenerProc = (UnsafeMutablePointer<Void>, AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<AudioFileStreamPropertyFlags>) -> Void ``` |
| To | ``` typealias AudioFileStream_PropertyListenerProc = (UnsafeMutableRawPointer, AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<AudioFileStreamPropertyFlags>) -> Swift.Void ``` |

Modified [AudioFileStreamGetProperty(_: AudioFileStreamID, _: AudioFileStreamPropertyID, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1391490-audiofilestreamgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileStreamGetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileStreamGetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [AudioFileStreamGetPropertyInfo(_: AudioFileStreamID, _: AudioFileStreamPropertyID, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1391500-audiofilestreamgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileStreamGetPropertyInfo(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func AudioFileStreamGetPropertyInfo(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [AudioFileStreamID](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamid)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileStreamID = COpaquePointer ``` |
| To | ``` typealias AudioFileStreamID = OpaquePointer ``` |

Modified [AudioFileStreamOpen(_: UnsafeMutableRawPointer?, _: AudioToolbox.AudioFileStream_PropertyListenerProc, _: AudioToolbox.AudioFileStream_PacketsProc, _: AudioFileTypeID, _: UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1391498-audiofilestreamopen)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileStreamOpen(_ inClientData: UnsafeMutablePointer<Void>, _ inPropertyListenerProc: AudioFileStream_PropertyListenerProc, _ inPacketsProc: AudioFileStream_PacketsProc, _ inFileTypeHint: AudioFileTypeID, _ outAudioFileStream: UnsafeMutablePointer<AudioFileStreamID>) -> OSStatus ``` |
| To | ``` func AudioFileStreamOpen(_ inClientData: UnsafeMutableRawPointer?, _ inPropertyListenerProc: AudioToolbox.AudioFileStream_PropertyListenerProc, _ inPacketsProc: AudioToolbox.AudioFileStream_PacketsProc, _ inFileTypeHint: AudioFileTypeID, _ outAudioFileStream: UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus ``` |

Modified [AudioFileStreamParseBytes(_: AudioFileStreamID, _: UInt32, _: UnsafeRawPointer, _: AudioFileStreamParseFlags) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1391492-audiofilestreamparsebytes)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileStreamParseBytes(_ inAudioFileStream: AudioFileStreamID, _ inDataByteSize: UInt32, _ inData: UnsafePointer<Void>, _ inFlags: AudioFileStreamParseFlags) -> OSStatus ``` |
| To | ``` func AudioFileStreamParseBytes(_ inAudioFileStream: AudioFileStreamID, _ inDataByteSize: UInt32, _ inData: UnsafeRawPointer, _ inFlags: AudioFileStreamParseFlags) -> OSStatus ``` |

Modified [AudioFileStreamSetProperty(_: AudioFileStreamID, _: AudioFileStreamPropertyID, _: UInt32, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1391576-audiofilestreamsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileStreamSetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileStreamSetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus ``` |

Modified [AudioFileWriteBytes(_: AudioFileID, _: Bool, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502379-audiofilewritebytes)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileWriteBytes(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileWriteBytes(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafeRawPointer) -> OSStatus ``` |

Modified [AudioFileWritePackets(_: AudioFileID, _: Bool, _: UInt32, _: UnsafePointer<AudioStreamPacketDescription>?, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502135-audiofilewritepackets)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileWritePackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileWritePackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafeRawPointer) -> OSStatus ``` |

Modified [AudioFormatGetProperty(_: AudioFormatPropertyID, _: UInt32, _: UnsafeRawPointer?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501860-audioformatgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFormatGetProperty(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFormatGetProperty(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>?, _ outPropertyData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioFormatGetPropertyInfo(_: AudioFormatPropertyID, _: UInt32, _: UnsafeRawPointer?, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502065-audioformatgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFormatGetPropertyInfo(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func AudioFormatGetPropertyInfo(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioOutputUnitGetHostIcon(_: AudioUnit, _: Float) -> UIImage?](https://developer.apple.com/documentation/audiotoolbox/1619491-audiooutputunitgethosticon)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioOutputUnitPublish(_: UnsafePointer<AudioComponentDescription>, _: CFString, _: UInt32, _: AudioUnit) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1619489-audiooutputunitpublish)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioOutputUnitStart(_: AudioUnit) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1439763-audiooutputunitstart)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioOutputUnitStartProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioOutputUnitStartProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioOutputUnitStartProc = (UnsafeMutableRawPointer) -> OSStatus ``` | AudioToolbox |

Modified [AudioOutputUnitStop(_: AudioUnit) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440513-audiooutputunitstop)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioOutputUnitStopProc](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstopproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioOutputUnitStopProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioOutputUnitStopProc = (UnsafeMutableRawPointer) -> OSStatus ``` | AudioToolbox |

Modified [AudioQueueAddPropertyListener(_: AudioQueueRef, _: AudioQueuePropertyID, _: AudioToolbox.AudioQueuePropertyListenerProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502091-audioqueueaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueAddPropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioQueueAddPropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioToolbox.AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioQueueAllocateBuffer(_: AudioQueueRef, _: UInt32, _: UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502248-audioqueueallocatebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueAllocateBuffer(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus ``` |
| To | ``` func AudioQueueAllocateBuffer(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus ``` |

Modified [AudioQueueAllocateBufferWithPacketDescriptions(_: AudioQueueRef, _: UInt32, _: UInt32, _: UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502389-audioqueueallocatebufferwithpack)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueAllocateBufferWithPacketDescriptions(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ inNumberPacketDescriptions: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus ``` |
| To | ``` func AudioQueueAllocateBufferWithPacketDescriptions(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ inNumberPacketDescriptions: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus ``` |

Modified [AudioQueueCreateTimeline(_: AudioQueueRef, _: UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501704-audioqueuecreatetimeline)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueCreateTimeline(_ inAQ: AudioQueueRef, _ outTimeline: UnsafeMutablePointer<AudioQueueTimelineRef>) -> OSStatus ``` |
| To | ``` func AudioQueueCreateTimeline(_ inAQ: AudioQueueRef, _ outTimeline: UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus ``` |

Modified [AudioQueueEnqueueBuffer(_: AudioQueueRef, _: AudioQueueBufferRef, _: UInt32, _: UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502779-audioqueueenqueuebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueEnqueueBuffer(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` |
| To | ``` func AudioQueueEnqueueBuffer(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus ``` |

Modified [AudioQueueEnqueueBufferWithParameters(_: AudioQueueRef, _: AudioQueueBufferRef, _: UInt32, _: UnsafePointer<AudioStreamPacketDescription>?, _: UInt32, _: UInt32, _: UInt32, _: UnsafePointer<AudioQueueParameterEvent>?, _: UnsafePointer<AudioTimeStamp>?, _: UnsafeMutablePointer<AudioTimeStamp>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503258-audioqueueenqueuebufferwithparam)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueEnqueueBufferWithParameters(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>, _ inTrimFramesAtStart: UInt32, _ inTrimFramesAtEnd: UInt32, _ inNumParamValues: UInt32, _ inParamValues: UnsafePointer<AudioQueueParameterEvent>, _ inStartTime: UnsafePointer<AudioTimeStamp>, _ outActualStartTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` |
| To | ``` func AudioQueueEnqueueBufferWithParameters(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>?, _ inTrimFramesAtStart: UInt32, _ inTrimFramesAtEnd: UInt32, _ inNumParamValues: UInt32, _ inParamValues: UnsafePointer<AudioQueueParameterEvent>?, _ inStartTime: UnsafePointer<AudioTimeStamp>?, _ outActualStartTime: UnsafeMutablePointer<AudioTimeStamp>?) -> OSStatus ``` |

Modified [AudioQueueGetCurrentTime(_: AudioQueueRef, _: AudioQueueTimelineRef?, _: UnsafeMutablePointer<AudioTimeStamp>?, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502244-audioqueuegetcurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueGetCurrentTime(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outTimelineDiscontinuity: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func AudioQueueGetCurrentTime(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef?, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>?, _ outTimelineDiscontinuity: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [AudioQueueGetProperty(_: AudioQueueRef, _: AudioQueuePropertyID, _: UnsafeMutableRawPointer, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502998-audioqueuegetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueGetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ outData: UnsafeMutablePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func AudioQueueGetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ outData: UnsafeMutableRawPointer, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioQueueInputCallback](https://developer.apple.com/documentation/audiotoolbox/audioqueueinputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueInputCallback = (UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> Void ``` |
| To | ``` typealias AudioQueueInputCallback = (UnsafeMutableRawPointer?, AudioQueueRef, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>?) -> Swift.Void ``` |

Modified [AudioQueueNewInput(_: UnsafePointer<AudioStreamBasicDescription>, _: AudioToolbox.AudioQueueInputCallback, _: UnsafeMutableRawPointer?, _: CFRunLoop?, _: CFString?, _: UInt32, _: UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501687-audioqueuenewinput)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueNewInput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueInputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop?, _ inCallbackRunLoopMode: CFString?, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` |
| To | ``` func AudioQueueNewInput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioToolbox.AudioQueueInputCallback, _ inUserData: UnsafeMutableRawPointer?, _ inCallbackRunLoop: CFRunLoop?, _ inCallbackRunLoopMode: CFString?, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus ``` |

Modified [AudioQueueNewOutput(_: UnsafePointer<AudioStreamBasicDescription>, _: AudioToolbox.AudioQueueOutputCallback, _: UnsafeMutableRawPointer?, _: CFRunLoop?, _: CFString?, _: UInt32, _: UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503207-audioqueuenewoutput)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueNewOutput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueOutputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop?, _ inCallbackRunLoopMode: CFString?, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` |
| To | ``` func AudioQueueNewOutput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioToolbox.AudioQueueOutputCallback, _ inUserData: UnsafeMutableRawPointer?, _ inCallbackRunLoop: CFRunLoop?, _ inCallbackRunLoopMode: CFString?, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus ``` |

Modified [AudioQueueOutputCallback](https://developer.apple.com/documentation/audiotoolbox/audioqueueoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueOutputCallback = (UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef) -> Void ``` |
| To | ``` typealias AudioQueueOutputCallback = (UnsafeMutableRawPointer?, AudioQueueRef, AudioQueueBufferRef) -> Swift.Void ``` |

Modified [AudioQueuePrime(_: AudioQueueRef, _: UInt32, _: UnsafeMutablePointer<UInt32>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503220-audioqueueprime)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueuePrime(_ inAQ: AudioQueueRef, _ inNumberOfFramesToPrepare: UInt32, _ outNumberOfFramesPrepared: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func AudioQueuePrime(_ inAQ: AudioQueueRef, _ inNumberOfFramesToPrepare: UInt32, _ outNumberOfFramesPrepared: UnsafeMutablePointer<UInt32>?) -> OSStatus ``` |

Modified [AudioQueueProcessingTapCallback](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueProcessingTapCallback = (UnsafeMutablePointer<Void>, AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioQueueProcessingTapFlags>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> Void ``` |
| To | ``` typealias AudioQueueProcessingTapCallback = (UnsafeMutableRawPointer, AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioQueueProcessingTapFlags>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> Swift.Void ``` |

Modified [AudioQueueProcessingTapNew(_: AudioQueueRef, _: AudioToolbox.AudioQueueProcessingTapCallback, _: UnsafeMutableRawPointer?, _: AudioQueueProcessingTapFlags, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<AudioStreamBasicDescription>, _: UnsafeMutablePointer<AudioQueueProcessingTapRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503209-audioqueueprocessingtapnew)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueProcessingTapNew(_ inAQ: AudioQueueRef, _ inCallback: AudioQueueProcessingTapCallback, _ inClientData: UnsafeMutablePointer<Void>, _ inFlags: AudioQueueProcessingTapFlags, _ outMaxFrames: UnsafeMutablePointer<UInt32>, _ outProcessingFormat: UnsafeMutablePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafeMutablePointer<AudioQueueProcessingTapRef>) -> OSStatus ``` |
| To | ``` func AudioQueueProcessingTapNew(_ inAQ: AudioQueueRef, _ inCallback: AudioToolbox.AudioQueueProcessingTapCallback, _ inClientData: UnsafeMutableRawPointer?, _ inFlags: AudioQueueProcessingTapFlags, _ outMaxFrames: UnsafeMutablePointer<UInt32>, _ outProcessingFormat: UnsafeMutablePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafeMutablePointer<AudioQueueProcessingTapRef?>) -> OSStatus ``` |

Modified [AudioQueueProcessingTapRef](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapref)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueProcessingTapRef = COpaquePointer ``` |
| To | ``` typealias AudioQueueProcessingTapRef = OpaquePointer ``` |

Modified [AudioQueuePropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audioqueuepropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueuePropertyListenerProc = (UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueuePropertyID) -> Void ``` |
| To | ``` typealias AudioQueuePropertyListenerProc = (UnsafeMutableRawPointer?, AudioQueueRef, AudioQueuePropertyID) -> Swift.Void ``` |

Modified [AudioQueueRef](https://developer.apple.com/documentation/audiotoolbox/audioqueueref)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueRef = COpaquePointer ``` |
| To | ``` typealias AudioQueueRef = OpaquePointer ``` |

Modified [AudioQueueRemovePropertyListener(_: AudioQueueRef, _: AudioQueuePropertyID, _: AudioToolbox.AudioQueuePropertyListenerProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502357-audioqueueremovepropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueRemovePropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioQueueRemovePropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioToolbox.AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioQueueSetOfflineRenderFormat(_: AudioQueueRef, _: UnsafePointer<AudioStreamBasicDescription>?, _: UnsafePointer<AudioChannelLayout>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502289-audioqueuesetofflinerenderformat)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueSetOfflineRenderFormat(_ inAQ: AudioQueueRef, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inLayout: UnsafePointer<AudioChannelLayout>) -> OSStatus ``` |
| To | ``` func AudioQueueSetOfflineRenderFormat(_ inAQ: AudioQueueRef, _ inFormat: UnsafePointer<AudioStreamBasicDescription>?, _ inLayout: UnsafePointer<AudioChannelLayout>?) -> OSStatus ``` |

Modified [AudioQueueSetProperty(_: AudioQueueRef, _: AudioQueuePropertyID, _: UnsafeRawPointer, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503282-audioqueuesetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueSetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inData: UnsafePointer<Void>, _ inDataSize: UInt32) -> OSStatus ``` |
| To | ``` func AudioQueueSetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inData: UnsafeRawPointer, _ inDataSize: UInt32) -> OSStatus ``` |

Modified [AudioQueueStart(_: AudioQueueRef, _: UnsafePointer<AudioTimeStamp>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502689-audioqueuestart)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueStart(_ inAQ: AudioQueueRef, _ inStartTime: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` |
| To | ``` func AudioQueueStart(_ inAQ: AudioQueueRef, _ inStartTime: UnsafePointer<AudioTimeStamp>?) -> OSStatus ``` |

Modified [AudioQueueTimelineRef](https://developer.apple.com/documentation/audiotoolbox/audioqueuetimelineref)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueTimelineRef = COpaquePointer ``` |
| To | ``` typealias AudioQueueTimelineRef = OpaquePointer ``` |

Modified [AudioServicesAddSystemSoundCompletion(_: SystemSoundID, _: CFRunLoop?, _: CFString?, _: AudioToolbox.AudioServicesSystemSoundCompletionProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1405244-audioservicesaddsystemsoundcompl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesAddSystemSoundCompletion(_ inSystemSoundID: SystemSoundID, _ inRunLoop: CFRunLoop?, _ inRunLoopMode: CFString?, _ inCompletionRoutine: AudioServicesSystemSoundCompletionProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioServicesAddSystemSoundCompletion(_ inSystemSoundID: SystemSoundID, _ inRunLoop: CFRunLoop?, _ inRunLoopMode: CFString?, _ inCompletionRoutine: AudioToolbox.AudioServicesSystemSoundCompletionProc, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioServicesGetProperty(_: AudioServicesPropertyID, _: UInt32, _: UnsafeRawPointer?, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1405206-audioservicesgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesGetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioServicesGetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioServicesGetPropertyInfo(_: AudioServicesPropertyID, _: UInt32, _: UnsafeRawPointer?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1405258-audioservicesgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesGetPropertyInfo(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func AudioServicesGetPropertyInfo(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [AudioServicesPlayAlertSoundWithCompletion(_: SystemSoundID, _: ( () -> Swift.Void)?)](https://developer.apple.com/documentation/audiotoolbox/1405238-audioservicesplayalertsoundwithc)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesPlayAlertSoundWithCompletion(_ inSystemSoundID: SystemSoundID, _ inCompletionBlock: (() -> Void)?) ``` |
| To | ``` func AudioServicesPlayAlertSoundWithCompletion(_ inSystemSoundID: SystemSoundID, _ inCompletionBlock: (@escaping () -> Swift.Void)?) ``` |

Modified [AudioServicesPlaySystemSoundWithCompletion(_: SystemSoundID, _: ( () -> Swift.Void)?)](https://developer.apple.com/documentation/audiotoolbox/1405210-audioservicesplaysystemsoundwith)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesPlaySystemSoundWithCompletion(_ inSystemSoundID: SystemSoundID, _ inCompletionBlock: (() -> Void)?) ``` |
| To | ``` func AudioServicesPlaySystemSoundWithCompletion(_ inSystemSoundID: SystemSoundID, _ inCompletionBlock: (@escaping () -> Swift.Void)?) ``` |

Modified [AudioServicesSetProperty(_: AudioServicesPropertyID, _: UInt32, _: UnsafeRawPointer?, _: UInt32, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1405226-audioservicessetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesSetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioServicesSetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus ``` |

Modified [AudioServicesSystemSoundCompletionProc](https://developer.apple.com/documentation/audiotoolbox/audioservicessystemsoundcompletionproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioServicesSystemSoundCompletionProc = (SystemSoundID, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias AudioServicesSystemSoundCompletionProc = (SystemSoundID, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [AudioUnit](https://developer.apple.com/documentation/audiotoolbox/audiounit)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitAddPropertyListener(_: AudioUnit, _: AudioUnitPropertyID, _: AudioToolbox.AudioUnitPropertyListenerProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440111-audiounitaddpropertylistener)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitAddPropertyListener(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioUnitPropertyListenerProc, _ inProcUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitAddPropertyListener(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioToolbox.AudioUnitPropertyListenerProc, _ inProcUserData: UnsafeMutableRawPointer?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitAddPropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiounitaddpropertylistenerproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitAddPropertyListenerProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitAddPropertyListenerProc = (UnsafeMutableRawPointer, AudioUnitPropertyID, AudioToolbox.AudioUnitPropertyListenerProc, UnsafeMutableRawPointer) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitAddRenderNotify(_: AudioUnit, _: AudioToolbox.AURenderCallback, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440259-audiounitaddrendernotify)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitAddRenderNotify(_ inUnit: AudioUnit, _ inProc: AURenderCallback, _ inProcUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitAddRenderNotify(_ inUnit: AudioUnit, _ inProc: AudioToolbox.AURenderCallback, _ inProcUserData: UnsafeMutableRawPointer?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitAddRenderNotifyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitaddrendernotifyproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitAddRenderNotifyProc = (UnsafeMutablePointer<Void>, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitAddRenderNotifyProc = (UnsafeMutableRawPointer, AudioToolbox.AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitComplexRenderProc](https://developer.apple.com/documentation/audiotoolbox/audiounitcomplexrenderproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitComplexRenderProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitComplexRenderProc = (UnsafeMutableRawPointer, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitElement](https://developer.apple.com/documentation/audiotoolbox/audiounitelement)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitGetParameter(_: AudioUnit, _: AudioUnitParameterID, _: AudioUnitScope, _: AudioUnitElement, _: UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440055-audiounitgetparameter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitGetParameterProc](https://developer.apple.com/documentation/audiotoolbox/audiounitgetparameterproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitGetParameterProc = (UnsafeMutablePointer<Void>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitGetParameterProc = (UnsafeMutableRawPointer, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitGetProperty(_: AudioUnit, _: AudioUnitPropertyID, _: AudioUnitScope, _: AudioUnitElement, _: UnsafeMutableRawPointer, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1439840-audiounitgetproperty)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitGetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outData: UnsafeMutablePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitGetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outData: UnsafeMutableRawPointer, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitGetPropertyInfo(_: AudioUnit, _: AudioUnitPropertyID, _: AudioUnitScope, _: AudioUnitElement, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440663-audiounitgetpropertyinfo)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitGetPropertyInfo(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitGetPropertyInfo(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outDataSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitGetPropertyInfoProc](https://developer.apple.com/documentation/audiotoolbox/audiounitgetpropertyinfoproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitGetPropertyInfoProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitGetPropertyInfoProc = (UnsafeMutableRawPointer, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitGetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitgetpropertyproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitGetPropertyProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitGetPropertyProc = (UnsafeMutableRawPointer, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitInitialize(_: AudioUnit) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1439851-audiounitinitialize)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitInitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiounitinitializeproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitInitializeProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitInitializeProc = (UnsafeMutableRawPointer) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitParameterID](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterIDName](https://developer.apple.com/documentation/audiotoolbox/audiounitparameternameinfo)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitParameterValue](https://developer.apple.com/documentation/audiotoolbox/audiounitparametervalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitProcess(_: AudioUnit, _: UnsafeMutablePointer<AudioUnitRenderActionFlags>?, _: UnsafePointer<AudioTimeStamp>, _: UInt32, _: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1439630-audiounitprocess)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitProcess(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitProcess(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>?, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitProcessMultiple(_: AudioUnit, _: UnsafeMutablePointer<AudioUnitRenderActionFlags>?, _: UnsafePointer<AudioTimeStamp>, _: UInt32, _: UInt32, _: UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, _: UInt32, _: UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440334-audiounitprocessmultiple)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitProcessMultiple(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ inNumberInputBufferLists: UInt32, _ inInputBufferLists: UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, _ inNumberOutputBufferLists: UInt32, _ ioOutputBufferLists: UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitProcessMultiple(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>?, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ inNumberInputBufferLists: UInt32, _ inInputBufferLists: UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, _ inNumberOutputBufferLists: UInt32, _ ioOutputBufferLists: UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitProcessMultipleProc](https://developer.apple.com/documentation/audiotoolbox/audiounitprocessmultipleproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitProcessMultipleProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitProcessMultipleProc = (UnsafeMutableRawPointer, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitProcessProc](https://developer.apple.com/documentation/audiotoolbox/audiounitprocessproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitProcessProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitProcessProc = (UnsafeMutableRawPointer, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitPropertyID](https://developer.apple.com/documentation/audiotoolbox/audiounitpropertyid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitPropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiounitpropertylistenerproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitPropertyListenerProc = (UnsafeMutablePointer<Void>, AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement) -> Void ``` | AudioUnit |
| To | ``` typealias AudioUnitPropertyListenerProc = (UnsafeMutableRawPointer, AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement) -> Swift.Void ``` | AudioToolbox |

Modified [AudioUnitRemoteControlEventListener](https://developer.apple.com/documentation/audiotoolbox/audiounitremotecontroleventlistener)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitRemoteControlEventListener = (AudioUnitRemoteControlEvent) -> Void ``` | AudioUnit |
| To | ``` typealias AudioUnitRemoteControlEventListener = (AudioUnitRemoteControlEvent) -> Swift.Void ``` | AudioToolbox |

Modified [AudioUnitRemovePropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremovepropertylistenerproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitRemovePropertyListenerProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitRemovePropertyListenerProc = (UnsafeMutableRawPointer, AudioUnitPropertyID, AudioToolbox.AudioUnitPropertyListenerProc) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitRemovePropertyListenerWithUserData(_: AudioUnit, _: AudioUnitPropertyID, _: AudioToolbox.AudioUnitPropertyListenerProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1441010-audiounitremovepropertylistenerw)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitRemovePropertyListenerWithUserData(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioUnitPropertyListenerProc, _ inProcUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitRemovePropertyListenerWithUserData(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioToolbox.AudioUnitPropertyListenerProc, _ inProcUserData: UnsafeMutableRawPointer?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitRemovePropertyListenerWithUserDataProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremovepropertylistenerwithuserdataproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitRemovePropertyListenerWithUserDataProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitRemovePropertyListenerWithUserDataProc = (UnsafeMutableRawPointer, AudioUnitPropertyID, AudioToolbox.AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitRemoveRenderNotify(_: AudioUnit, _: AudioToolbox.AURenderCallback, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440547-audiounitremoverendernotify)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitRemoveRenderNotify(_ inUnit: AudioUnit, _ inProc: AURenderCallback, _ inProcUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitRemoveRenderNotify(_ inUnit: AudioUnit, _ inProc: AudioToolbox.AURenderCallback, _ inProcUserData: UnsafeMutableRawPointer?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitRemoveRenderNotifyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitremoverendernotifyproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitRemoveRenderNotifyProc = (UnsafeMutablePointer<Void>, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitRemoveRenderNotifyProc = (UnsafeMutableRawPointer, AudioToolbox.AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitRender(_: AudioUnit, _: UnsafeMutablePointer<AudioUnitRenderActionFlags>?, _: UnsafePointer<AudioTimeStamp>, _: UInt32, _: UInt32, _: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1438430-audiounitrender)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitRender(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inOutputBusNumber: UInt32, _ inNumberFrames: UInt32, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitRender(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>?, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inOutputBusNumber: UInt32, _ inNumberFrames: UInt32, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitRenderProc](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitRenderProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitRenderProc = (UnsafeMutableRawPointer, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitReset(_: AudioUnit, _: AudioUnitScope, _: AudioUnitElement) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1439607-audiounitreset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitResetProc](https://developer.apple.com/documentation/audiotoolbox/audiounitresetproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitResetProc = (UnsafeMutablePointer<Void>, AudioUnitScope, AudioUnitElement) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitResetProc = (UnsafeMutableRawPointer, AudioUnitScope, AudioUnitElement) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitScheduleParameters(_: AudioUnit, _: UnsafePointer<AudioUnitParameterEvent>, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1439670-audiounitscheduleparameters)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitScheduleParametersProc](https://developer.apple.com/documentation/audiotoolbox/audiounitscheduleparametersproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitScheduleParametersProc = (UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitScheduleParametersProc = (UnsafeMutableRawPointer, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitScope](https://developer.apple.com/documentation/audiotoolbox/audiounitscope)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitSetParameter(_: AudioUnit, _: AudioUnitParameterID, _: AudioUnitScope, _: AudioUnitElement, _: AudioUnitParameterValue, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1438454-audiounitsetparameter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitSetParameterProc](https://developer.apple.com/documentation/audiotoolbox/audiounitsetparameterproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitSetParameterProc = (UnsafeMutablePointer<Void>, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitSetParameterProc = (UnsafeMutableRawPointer, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitSetProperty(_: AudioUnit, _: AudioUnitPropertyID, _: AudioUnitScope, _: AudioUnitElement, _: UnsafeRawPointer?, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440371-audiounitsetproperty)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func AudioUnitSetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ inData: UnsafePointer<Void>, _ inDataSize: UInt32) -> OSStatus ``` | AudioUnit |
| To | ``` func AudioUnitSetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ inData: UnsafeRawPointer?, _ inDataSize: UInt32) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitSetPropertyProc](https://developer.apple.com/documentation/audiotoolbox/audiounitsetpropertyproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitSetPropertyProc = (UnsafeMutablePointer<Void>, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafePointer<Void>, UInt32) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitSetPropertyProc = (UnsafeMutableRawPointer, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeRawPointer, UInt32) -> OSStatus ``` | AudioToolbox |

Modified [AudioUnitUninitialize(_: AudioUnit) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1438415-audiounituninitialize)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AudioUnitUninitializeProc](https://developer.apple.com/documentation/audiotoolbox/audiounituninitializeproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AudioUnitUninitializeProc = (UnsafeMutablePointer<Void>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AudioUnitUninitializeProc = (UnsafeMutableRawPointer) -> OSStatus ``` | AudioToolbox |

Modified [AUEventSampleTime](https://developer.apple.com/documentation/audiotoolbox/aueventsampletime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUEventSampleTimeImmediate](https://developer.apple.com/documentation/audiotoolbox/1387633-aueventsampletime/aueventsampletimeimmediate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUGraph](https://developer.apple.com/documentation/audiotoolbox/augraph)

|  | Declaration |
| --- | --- |
| From | ``` typealias AUGraph = COpaquePointer ``` |
| To | ``` typealias AUGraph = OpaquePointer ``` |

Modified [AUGraphAddRenderNotify(_: AUGraph, _: AudioToolbox.AURenderCallback, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501636-augraphaddrendernotify)

|  | Declaration |
| --- | --- |
| From | ``` func AUGraphAddRenderNotify(_ inGraph: AUGraph, _ inCallback: AURenderCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AUGraphAddRenderNotify(_ inGraph: AUGraph, _ inCallback: AudioToolbox.AURenderCallback, _ inRefCon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AUGraphNodeInfo(_: AUGraph, _: AUNode, _: UnsafeMutablePointer<AudioComponentDescription>?, _: UnsafeMutablePointer<AudioUnit?>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502407-augraphnodeinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AUGraphNodeInfo(_ inGraph: AUGraph, _ inNode: AUNode, _ outDescription: UnsafeMutablePointer<AudioComponentDescription>, _ outAudioUnit: UnsafeMutablePointer<AudioUnit>) -> OSStatus ``` |
| To | ``` func AUGraphNodeInfo(_ inGraph: AUGraph, _ inNode: AUNode, _ outDescription: UnsafeMutablePointer<AudioComponentDescription>?, _ outAudioUnit: UnsafeMutablePointer<AudioUnit?>?) -> OSStatus ``` |

Modified [AUGraphRemoveRenderNotify(_: AUGraph, _: AudioToolbox.AURenderCallback, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503352-augraphremoverendernotify)

|  | Declaration |
| --- | --- |
| From | ``` func AUGraphRemoveRenderNotify(_ inGraph: AUGraph, _ inCallback: AURenderCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AUGraphRemoveRenderNotify(_ inGraph: AUGraph, _ inCallback: AudioToolbox.AURenderCallback, _ inRefCon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AUGraphUpdate(_: AUGraph, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502855-augraphupdate)

|  | Declaration |
| --- | --- |
| From | ``` func AUGraphUpdate(_ inGraph: AUGraph, _ outIsUpdated: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func AUGraphUpdate(_ inGraph: AUGraph, _ outIsUpdated: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [AUHostMusicalContextBlock](https://developer.apple.com/documentation/audiotoolbox/auhostmusicalcontextblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUHostMusicalContextBlock = (UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Double>) -> Bool ``` | AudioUnit |
| To | ``` typealias AUHostMusicalContextBlock = (UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Double>?) -> Bool ``` | AudioToolbox |

Modified [AUHostTransportStateBlock](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUHostTransportStateBlock = (UnsafeMutablePointer<AUHostTransportStateFlags>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>) -> Bool ``` | AudioUnit |
| To | ``` typealias AUHostTransportStateBlock = (UnsafeMutablePointer<AUHostTransportStateFlags>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?, UnsafeMutablePointer<Double>?) -> Bool ``` | AudioToolbox |

Modified [AUImplementorDisplayNameWithLengthCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementordisplaynamewithlengthcallback)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUImplementorStringFromValueCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorstringfromvaluecallback)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUImplementorStringFromValueCallback = (AUParameter, UnsafePointer<AUValue>) -> String ``` | AudioUnit |
| To | ``` typealias AUImplementorStringFromValueCallback = (AUParameter, UnsafePointer<AUValue>?) -> String ``` | AudioToolbox |

Modified [AUImplementorValueFromStringCallback](https://developer.apple.com/documentation/audiotoolbox/auimplementorvaluefromstringcallback)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUImplementorValueObserver](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueobserver)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUImplementorValueObserver = (AUParameter, AUValue) -> Void ``` | AudioUnit |
| To | ``` typealias AUImplementorValueObserver = (AUParameter, AUValue) -> Swift.Void ``` | AudioToolbox |

Modified [AUImplementorValueProvider](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueprovider)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUInputHandler](https://developer.apple.com/documentation/audiotoolbox/auinputhandler)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUInputHandler = (UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int) -> Void ``` | AudioUnit |
| To | ``` typealias AUInputHandler = (UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int) -> Swift.Void ``` | AudioToolbox |

Modified [AUInputSamplesInOutputCallback](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallback)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUInputSamplesInOutputCallback = (UnsafeMutablePointer<Void>, UnsafePointer<AudioTimeStamp>, Float64, Float64) -> Void ``` | AudioUnit |
| To | ``` typealias AUInputSamplesInOutputCallback = (UnsafeMutableRawPointer, UnsafePointer<AudioTimeStamp>, Float64, Float64) -> Swift.Void ``` | AudioToolbox |

Modified [AUInternalRenderBlock](https://developer.apple.com/documentation/audiotoolbox/auinternalrenderblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUInternalRenderBlock = (UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AURenderEvent>, AURenderPullInputBlock?) -> AUAudioUnitStatus ``` | AudioUnit |
| To | ``` typealias AUInternalRenderBlock = (UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AURenderEvent>?, AudioToolbox.AURenderPullInputBlock?) -> AUAudioUnitStatus ``` | AudioToolbox |

Modified [AUParameterAddress](https://developer.apple.com/documentation/audiotoolbox/auparameteraddress)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUParameterObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterobserver)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUParameterObserver = (AUParameterAddress, AUValue) -> Void ``` | AudioUnit |
| To | ``` typealias AUParameterObserver = (AUParameterAddress, AUValue) -> Swift.Void ``` | AudioToolbox |

Modified [AUParameterObserverToken](https://developer.apple.com/documentation/audiotoolbox/auparameterobservertoken)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUParameterObserverToken = UnsafeMutablePointer<Void> ``` | AudioUnit |
| To | ``` typealias AUParameterObserverToken = UnsafeMutableRawPointer ``` | AudioToolbox |

Modified [AUParameterRecordingObserver](https://developer.apple.com/documentation/audiotoolbox/auparameterrecordingobserver)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUParameterRecordingObserver = (Int, UnsafePointer<AURecordedParameterEvent>) -> Void ``` | AudioUnit |
| To | ``` typealias AUParameterRecordingObserver = (Int, UnsafePointer<AURecordedParameterEvent>) -> Swift.Void ``` | AudioToolbox |

Modified [AURenderBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AURenderBlock = (UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int, UnsafeMutablePointer<AudioBufferList>, AURenderPullInputBlock?) -> AUAudioUnitStatus ``` | AudioUnit |
| To | ``` typealias AURenderBlock = (UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int, UnsafeMutablePointer<AudioBufferList>, AudioToolbox.AURenderPullInputBlock?) -> AUAudioUnitStatus ``` | AudioToolbox |

Modified [AURenderCallback](https://developer.apple.com/documentation/audiotoolbox/aurendercallback)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AURenderCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias AURenderCallback = (UnsafeMutableRawPointer, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>?) -> OSStatus ``` | AudioToolbox |

Modified [AURenderObserver](https://developer.apple.com/documentation/audiotoolbox/aurenderobserver)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AURenderObserver = (AudioUnitRenderActionFlags, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int) -> Void ``` | AudioUnit |
| To | ``` typealias AURenderObserver = (AudioUnitRenderActionFlags, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int) -> Swift.Void ``` | AudioToolbox |

Modified [AURenderPullInputBlock](https://developer.apple.com/documentation/audiotoolbox/aurenderpullinputblock)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [AUScheduleMIDIEventBlock](https://developer.apple.com/documentation/audiotoolbox/auschedulemidieventblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUScheduleMIDIEventBlock = (AUEventSampleTime, UInt8, Int, UnsafePointer<UInt8>) -> Void ``` | AudioUnit |
| To | ``` typealias AUScheduleMIDIEventBlock = (AUEventSampleTime, UInt8, Int, UnsafePointer<UInt8>) -> Swift.Void ``` | AudioToolbox |

Modified [AUScheduleParameterBlock](https://developer.apple.com/documentation/audiotoolbox/auscheduleparameterblock)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias AUScheduleParameterBlock = (AUEventSampleTime, AUAudioFrameCount, AUParameterAddress, AUValue) -> Void ``` | AudioUnit |
| To | ``` typealias AUScheduleParameterBlock = (AUEventSampleTime, AUAudioFrameCount, AUParameterAddress, AUValue) -> Swift.Void ``` | AudioToolbox |

Modified [AUValue](https://developer.apple.com/documentation/audiotoolbox/auvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [CAShow(_: UnsafeMutableRawPointer)](https://developer.apple.com/documentation/audiotoolbox/1475988-cashow)

|  | Declaration |
| --- | --- |
| From | ``` func CAShow(_ inObject: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CAShow(_ inObject: UnsafeMutableRawPointer) ``` |

Modified [CAShowFile(_: UnsafeMutableRawPointer, _: UnsafeMutablePointer<FILE>)](https://developer.apple.com/documentation/audiotoolbox/1475990-cashowfile)

|  | Declaration |
| --- | --- |
| From | ``` func CAShowFile(_ inObject: UnsafeMutablePointer<Void>, _ inFile: UnsafeMutablePointer<FILE>) ``` |
| To | ``` func CAShowFile(_ inObject: UnsafeMutableRawPointer, _ inFile: UnsafeMutablePointer<FILE>) ``` |

Modified [ExtAudioFileCreateWithURL(_: CFURL, _: AudioFileTypeID, _: UnsafePointer<AudioStreamBasicDescription>, _: UnsafePointer<AudioChannelLayout>?, _: UInt32, _: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486878-extaudiofilecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileCreateWithURL(_ inURL: CFURL, _ inFileType: AudioFileTypeID, _ inStreamDesc: UnsafePointer<AudioStreamBasicDescription>, _ inChannelLayout: UnsafePointer<AudioChannelLayout>, _ inFlags: UInt32, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |
| To | ``` func ExtAudioFileCreateWithURL(_ inURL: CFURL, _ inFileType: AudioFileTypeID, _ inStreamDesc: UnsafePointer<AudioStreamBasicDescription>, _ inChannelLayout: UnsafePointer<AudioChannelLayout>?, _ inFlags: UInt32, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus ``` |

Modified [ExtAudioFileGetProperty(_: ExtAudioFileRef, _: ExtAudioFilePropertyID, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutableRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486840-extaudiofilegetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileGetProperty(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func ExtAudioFileGetProperty(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus ``` |

Modified [ExtAudioFileGetPropertyInfo(_: ExtAudioFileRef, _: ExtAudioFilePropertyID, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486871-extaudiofilegetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileGetPropertyInfo(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func ExtAudioFileGetPropertyInfo(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ outSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus ``` |

Modified [ExtAudioFileOpenURL(_: CFURL, _: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486873-extaudiofileopenurl)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileOpenURL(_ inURL: CFURL, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |
| To | ``` func ExtAudioFileOpenURL(_ inURL: CFURL, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus ``` |

Modified [ExtAudioFileRef](https://developer.apple.com/documentation/audiotoolbox/extaudiofileref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ExtAudioFileRef = COpaquePointer ``` |
| To | ``` typealias ExtAudioFileRef = OpaquePointer ``` |

Modified [ExtAudioFileSetProperty(_: ExtAudioFileRef, _: ExtAudioFilePropertyID, _: UInt32, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486884-extaudiofilesetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileSetProperty(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func ExtAudioFileSetProperty(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus ``` |

Modified [ExtAudioFileWrapAudioFileID(_: AudioFileID, _: Bool, _: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486852-extaudiofilewrapaudiofileid)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileWrapAudioFileID(_ inFileID: AudioFileID, _ inForWriting: Bool, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |
| To | ``` func ExtAudioFileWrapAudioFileID(_ inFileID: AudioFileID, _ inForWriting: Bool, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef?>) -> OSStatus ``` |

Modified [ExtAudioFileWriteAsync(_: ExtAudioFileRef, _: UInt32, _: UnsafePointer<AudioBufferList>?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486834-extaudiofilewriteasync)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileWriteAsync(_ inExtAudioFile: ExtAudioFileRef, _ inNumberFrames: UInt32, _ ioData: UnsafePointer<AudioBufferList>) -> OSStatus ``` |
| To | ``` func ExtAudioFileWriteAsync(_ inExtAudioFile: ExtAudioFileRef, _ inNumberFrames: UInt32, _ ioData: UnsafePointer<AudioBufferList>?) -> OSStatus ``` |

Modified [GetAudioUnitParameterDisplayType(_: AudioUnitParameterOptions) -> AudioUnitParameterOptions](https://developer.apple.com/documentation/audiotoolbox/1440794-getaudiounitparameterdisplaytype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [HostCallback_GetBeatAndTempo](https://developer.apple.com/documentation/audiotoolbox/hostcallback_getbeatandtempo)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias HostCallback_GetBeatAndTempo = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias HostCallback_GetBeatAndTempo = (UnsafeMutableRawPointer?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<Float64>?) -> OSStatus ``` | AudioToolbox |

Modified [HostCallback_GetMusicalTimeLocation](https://developer.apple.com/documentation/audiotoolbox/hostcallback_getmusicaltimelocation)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias HostCallback_GetMusicalTimeLocation = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Float32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Float64>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias HostCallback_GetMusicalTimeLocation = (UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<Float32>?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<Float64>?) -> OSStatus ``` | AudioToolbox |

Modified [HostCallback_GetTransportState](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias HostCallback_GetTransportState = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias HostCallback_GetTransportState = (UnsafeMutableRawPointer?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<Float64>?) -> OSStatus ``` | AudioToolbox |

Modified [HostCallback_GetTransportState2](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate2)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias HostCallback_GetTransportState2 = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<Float64>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias HostCallback_GetTransportState2 = (UnsafeMutableRawPointer?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<Float64>?) -> OSStatus ``` | AudioToolbox |

Modified [k3DMixerParam_Azimuth](https://developer.apple.com/documentation/audiotoolbox/k3dmixerparam_azimuth)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_Distance](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_distance)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_Elevation](https://developer.apple.com/documentation/audiotoolbox/k3dmixerparam_elevation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_Enable](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_enable)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_Gain](https://developer.apple.com/documentation/audiotoolbox/k3dmixerparam_gain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_GlobalReverbGain](https://developer.apple.com/documentation/audiotoolbox/k3dmixerparam_globalreverbgain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_MaxGain](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_maxgain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_MinGain](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_mingain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_ObstructionAttenuation](https://developer.apple.com/documentation/audiotoolbox/k3dmixerparam_obstructionattenuation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_OcclusionAttenuation](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_occlusionattenuation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_PlaybackRate](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_playbackrate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [k3DMixerParam_ReverbBlend](https://developer.apple.com/documentation/audiotoolbox/1389763-3d_mixer_unit_parameters/k3dmixerparam_reverbblend)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentConfigurationInfo_ValidationResult](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentconfigurationinfo_validationresult)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentErr_DuplicateDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponenterr_duplicatedescription)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentErr_InitializationTimedOut](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponenterr_initializationtimedout)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentErr_InstanceInvalidated](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiocomponenterr_instanceinvalidated)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentErr_InvalidFormat](https://developer.apple.com/documentation/audiotoolbox/1619490-anonymous/kaudiocomponenterr_invalidformat)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentErr_NotPermitted](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponenterr_notpermitted)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentErr_TooManyInstances](https://developer.apple.com/documentation/audiotoolbox/1619490-anonymous/kaudiocomponenterr_toomanyinstances)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentErr_UnsupportedType](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponenterr_unsupportedtype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentInstanceInvalidationNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentinstanceinvalidationnotification)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentRegistrationsChangedNotification](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentregistrationschangednotification)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentValidationParameter_ForceValidation](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_forcevalidation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioComponentValidationParameter_TimeOut](https://developer.apple.com/documentation/audiotoolbox/kaudiocomponentvalidationparameter_timeout)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_ChannelMap](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitproperty_channelmap)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_CurrentDevice](https://developer.apple.com/documentation/audiotoolbox/1534116-i_o_audio_unit_properties/kaudiooutputunitproperty_currentdevice)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_EnableIO](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitproperty_enableio)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_HasIO](https://developer.apple.com/documentation/audiotoolbox/1534116-i_o_audio_unit_properties/kaudiooutputunitproperty_hasio)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_HostReceivesRemoteControlEvents](https://developer.apple.com/documentation/audiotoolbox/1621039-anonymous/kaudiooutputunitproperty_hostreceivesremotecontrolevents)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_HostTransportState](https://developer.apple.com/documentation/audiotoolbox/1621039-anonymous/kaudiooutputunitproperty_hosttransportstate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_IsRunning](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitproperty_isrunning)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_MIDICallbacks](https://developer.apple.com/documentation/audiotoolbox/1621039-anonymous/kaudiooutputunitproperty_midicallbacks)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_NodeComponentDescription](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitproperty_nodecomponentdescription)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_RemoteControlToHost](https://developer.apple.com/documentation/audiotoolbox/1621039-anonymous/kaudiooutputunitproperty_remotecontroltohost)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_SetInputCallback](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitproperty_setinputcallback)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_StartTime](https://developer.apple.com/documentation/audiotoolbox/1534116-i_o_audio_unit_properties/kaudiooutputunitproperty_starttime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitProperty_StartTimestampsAtZero](https://developer.apple.com/documentation/audiotoolbox/1534116-i_o_audio_unit_properties/kaudiooutputunitproperty_starttimestampsatzero)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitRange](https://developer.apple.com/documentation/audiotoolbox/1585807-i_o_audio_unit_function_selector/kaudiooutputunitrange)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitStartSelect](https://developer.apple.com/documentation/audiotoolbox/1585807-i_o_audio_unit_function_selector/kaudiooutputunitstartselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioOutputUnitStopSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitstopselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitAddPropertyListenerSelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitaddpropertylistenerselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitAddRenderNotifySelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitaddrendernotifyselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitClumpID_System](https://developer.apple.com/documentation/audiotoolbox/1533986-reserved_audio_unit_clump_identi/kaudiounitclumpid_system)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitComplexRenderSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitcomplexrenderselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitConfigurationInfo_BusCountWritable](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_buscountwritable)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitConfigurationInfo_ChannelConfigurations](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_channelconfigurations)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitConfigurationInfo_HasCustomView](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_hascustomview)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitConfigurationInfo_IconURL](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_iconurl)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitConfigurationInfo_InitialInputs](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_initialinputs)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitConfigurationInfo_InitialOutputs](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_initialoutputs)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitConfigurationInfo_SupportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/kaudiounitconfigurationinfo_supportedchannellayouttags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_CannotDoInCurrentContext](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_cannotdoincurrentcontext)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_FailedInitialization](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_failedinitialization)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_FileNotSpecified](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_filenotspecified)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_FormatNotSupported](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_formatnotsupported)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_IllegalInstrument](https://developer.apple.com/documentation/audiotoolbox/1584141-anonymous/kaudiouniterr_illegalinstrument)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_Initialized](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_initialized)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_InstrumentTypeNotFound](https://developer.apple.com/documentation/audiotoolbox/1584141-anonymous/kaudiouniterr_instrumenttypenotfound)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_InvalidElement](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_invalidelement)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_InvalidFile](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_invalidfile)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_InvalidOfflineRender](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_invalidofflinerender)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_InvalidParameter](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_invalidparameter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_InvalidProperty](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_invalidproperty)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_InvalidPropertyValue](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_invalidpropertyvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_InvalidScope](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_invalidscope)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_NoConnection](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_noconnection)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_PropertyNotInUse](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_propertynotinuse)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_PropertyNotWritable](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_propertynotwritable)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_TooManyFramesToProcess](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_toomanyframestoprocess)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_Unauthorized](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_unauthorized)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_Uninitialized](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_uninitialized)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitErr_UnknownFileType](https://developer.apple.com/documentation/audiotoolbox/1584138-anonymous/kaudiouniterr_unknownfiletype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitGetParameterSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitgetparameterselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitGetPropertyInfoSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitgetpropertyinfoselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitGetPropertySelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitgetpropertyselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitInitializeSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitinitializeselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitManufacturer_Apple](https://developer.apple.com/documentation/audiotoolbox/1584143-audio_unit_manufacturer_identifi/kaudiounitmanufacturer_apple)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitParameterName_Full](https://developer.apple.com/documentation/audiotoolbox/kaudiounitparametername_full)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProcessMultipleSelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitprocessmultipleselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProcessSelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitprocessselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_3DMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_3dmixerattenuationcurve)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_3DMixerDistanceAtten](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_3dmixerdistanceatten)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_3DMixerDistanceParams](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_3dmixerdistanceparams)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_3DMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_3dmixerrenderingflags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_AudioChannelLayout](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_audiochannellayout)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_BypassEffect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_bypasseffect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ClassInfo](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_classinfo)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ClassInfoFromDocument](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_classinfofromdocument)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ContextName](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_contextname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_CPULoad](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_cpuload)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_CurrentPlayTime](https://developer.apple.com/documentation/audiotoolbox/1534024-anonymous/kaudiounitproperty_currentplaytime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_DeferredRendererExtraLatency](https://developer.apple.com/documentation/audiotoolbox/1534061-anonymous/kaudiounitproperty_deferredrendererextralatency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_DeferredRendererPullSize](https://developer.apple.com/documentation/audiotoolbox/1534061-anonymous/kaudiounitproperty_deferredrendererpullsize)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_DeferredRendererWaitFrames](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_deferredrendererwaitframes)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_DependentParameters](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_dependentparameters)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_DopplerShift](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_dopplershift)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ElementCount](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_elementcount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ElementName](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_elementname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_FactoryPresets](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_factorypresets)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_FrequencyResponse](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_frequencyresponse)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_HostCallbacks](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_hostcallbacks)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_InPlaceProcessing](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_inplaceprocessing)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_InputSamplesInOutput](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_inputsamplesinoutput)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_IsInterAppConnected](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_isinterappconnected)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_LastRenderError](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_lastrendererror)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_Latency](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_latency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_MakeConnection](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_makeconnection)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_MatrixDimensions](https://developer.apple.com/documentation/audiotoolbox/1534041-mixer_audio_unit_properties/kaudiounitproperty_matrixdimensions)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_MatrixLevels](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_matrixlevels)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_MaximumFramesPerSlice](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_maximumframesperslice)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_MeterClipping](https://developer.apple.com/documentation/audiotoolbox/1534041-mixer_audio_unit_properties/kaudiounitproperty_meterclipping)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_MeteringMode](https://developer.apple.com/documentation/audiotoolbox/1534041-mixer_audio_unit_properties/kaudiounitproperty_meteringmode)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_NickName](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_nickname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_OfflineRender](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_offlinerender)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParameterClumpName](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parameterclumpname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParameterHistoryInfo](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_parameterhistoryinfo)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParameterIDName](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_parameteridname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParameterInfo](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parameterinfo)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParameterList](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_parameterlist)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParametersForOverview](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parametersforoverview)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParameterStringFromValue](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_parameterstringfromvalue)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParameterValueFromString](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parametervaluefromstring)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ParameterValueStrings](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_parametervaluestrings)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_PeerURL](https://developer.apple.com/documentation/audiotoolbox/1621038-anonymous/kaudiounitproperty_peerurl)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_PresentationLatency](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_presentationlatency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_PresentPreset](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_presentpreset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_RemoteControlEventListener](https://developer.apple.com/documentation/audiotoolbox/1621038-anonymous/kaudiounitproperty_remotecontroleventlistener)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_RenderQuality](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_renderquality)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_RequestViewController](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_requestviewcontroller)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ReverbPreset](https://developer.apple.com/documentation/audiotoolbox/1534063-3d_mixer_audio_unit_properties/kaudiounitproperty_reverbpreset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ReverbRoomType](https://developer.apple.com/documentation/audiotoolbox/1534150-anonymous/kaudiounitproperty_reverbroomtype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SampleRate](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_samplerate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SampleRateConverterComplexity](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_samplerateconvertercomplexity)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ScheduleAudioSlice](https://developer.apple.com/documentation/audiotoolbox/1534024-anonymous/kaudiounitproperty_scheduleaudioslice)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ScheduledFileBufferSizeFrames](https://developer.apple.com/documentation/audiotoolbox/1534079-anonymous/kaudiounitproperty_scheduledfilebuffersizeframes)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ScheduledFileIDs](https://developer.apple.com/documentation/audiotoolbox/1534079-anonymous/kaudiounitproperty_scheduledfileids)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ScheduledFileNumberBuffers](https://developer.apple.com/documentation/audiotoolbox/1534079-anonymous/kaudiounitproperty_scheduledfilenumberbuffers)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ScheduledFilePrime](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_scheduledfileprime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ScheduledFileRegion](https://developer.apple.com/documentation/audiotoolbox/1534079-anonymous/kaudiounitproperty_scheduledfileregion)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ScheduleStartTimeStamp](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_schedulestarttimestamp)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SetRenderCallback](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_setrendercallback)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_ShouldAllocateBuffer](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_shouldallocatebuffer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SpatializationAlgorithm](https://developer.apple.com/documentation/audiotoolbox/1534150-anonymous/kaudiounitproperty_spatializationalgorithm)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SpatialMixerAttenuationCurve](https://developer.apple.com/documentation/audiotoolbox/1534150-anonymous/kaudiounitproperty_spatialmixerattenuationcurve)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SpatialMixerDistanceParams](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_spatialmixerdistanceparams)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SpatialMixerRenderingFlags](https://developer.apple.com/documentation/audiotoolbox/1534150-anonymous/kaudiounitproperty_spatialmixerrenderingflags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_StreamFormat](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_streamformat)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SupportedChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_supportedchannellayouttags)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_SupportedNumChannels](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_supportednumchannels)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_TailTime](https://developer.apple.com/documentation/audiotoolbox/1534199-generic_audio_unit_properties/kaudiounitproperty_tailtime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitProperty_UsesInternalReverb](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_usesinternalreverb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitRange](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitrange)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitRemovePropertyListenerSelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitremovepropertylistenerselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitRemovePropertyListenerWithUserDataSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitremovepropertylistenerwithuserdataselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitRemoveRenderNotifySelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitremoverendernotifyselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitRenderSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitrenderselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitResetSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitresetselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSampleRateConverterComplexity_Linear](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsamplerateconvertercomplexity_linear)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSampleRateConverterComplexity_Mastering](https://developer.apple.com/documentation/audiotoolbox/1534173-audio_unit_sample_rate_converter/kaudiounitsamplerateconvertercomplexity_mastering)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSampleRateConverterComplexity_Normal](https://developer.apple.com/documentation/audiotoolbox/1534173-audio_unit_sample_rate_converter/kaudiounitsamplerateconvertercomplexity_normal)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScheduleParametersSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscheduleparametersselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScope_Global](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_global)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScope_Group](https://developer.apple.com/documentation/audiotoolbox/1534214-audio_unit_scopes/kaudiounitscope_group)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScope_Input](https://developer.apple.com/documentation/audiotoolbox/1534214-audio_unit_scopes/kaudiounitscope_input)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScope_Layer](https://developer.apple.com/documentation/audiotoolbox/1534214-audio_unit_scopes/kaudiounitscope_layer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScope_LayerItem](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_layeritem)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScope_Note](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_note)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScope_Output](https://developer.apple.com/documentation/audiotoolbox/1534214-audio_unit_scopes/kaudiounitscope_output)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitScope_Part](https://developer.apple.com/documentation/audiotoolbox/kaudiounitscope_part)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSetParameterSelect](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsetparameterselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSetPropertySelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounitsetpropertyselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_AU3DMixerEmbedded](https://developer.apple.com/documentation/audiotoolbox/1619479-anonymous/kaudiounitsubtype_au3dmixerembedded)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_AUConverter](https://developer.apple.com/documentation/audiotoolbox/1584145-converter_audio_unit_subtypes/kaudiounitsubtype_auconverter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_AudioFilePlayer](https://developer.apple.com/documentation/audiotoolbox/1584155-anonymous/kaudiounitsubtype_audiofileplayer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_AUiPodEQ](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_auipodeq)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_AUiPodTime](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_auipodtime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_AUiPodTimeOther](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_auipodtimeother)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_BandPassFilter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_bandpassfilter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_DeferredRenderer](https://developer.apple.com/documentation/audiotoolbox/1584145-converter_audio_unit_subtypes/kaudiounitsubtype_deferredrenderer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_Delay](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_delay)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_Distortion](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_distortion)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_DynamicsProcessor](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_dynamicsprocessor)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_GenericOutput](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_genericoutput)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_HighPassFilter](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_highpassfilter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_HighShelfFilter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_highshelffilter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_LowPassFilter](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_lowpassfilter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_LowShelfFilter](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_lowshelffilter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_MatrixMixer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_matrixmixer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_Merger](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_merger)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_MIDISynth](https://developer.apple.com/documentation/audiotoolbox/1619498-anonymous/kaudiounitsubtype_midisynth)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_MultiChannelMixer](https://developer.apple.com/documentation/audiotoolbox/1584150-mixer_audio_unit_subtypes/kaudiounitsubtype_multichannelmixer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_MultiSplitter](https://developer.apple.com/documentation/audiotoolbox/1584145-converter_audio_unit_subtypes/kaudiounitsubtype_multisplitter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_NBandEQ](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_nbandeq)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_NewTimePitch](https://developer.apple.com/documentation/audiotoolbox/1584145-converter_audio_unit_subtypes/kaudiounitsubtype_newtimepitch)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_ParametricEQ](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_parametriceq)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_PeakLimiter](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_peaklimiter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_RemoteIO](https://developer.apple.com/documentation/audiotoolbox/1619485-anonymous/kaudiounitsubtype_remoteio)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_Reverb2](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_reverb2)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_RoundTripAAC](https://developer.apple.com/documentation/audiotoolbox/1584145-converter_audio_unit_subtypes/kaudiounitsubtype_roundtripaac)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_SampleDelay](https://developer.apple.com/documentation/audiotoolbox/1584154-effect_audio_unit_subtypes/kaudiounitsubtype_sampledelay)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_Sampler](https://developer.apple.com/documentation/audiotoolbox/1584149-music_instrument_audio_unit_subt/kaudiounitsubtype_sampler)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_ScheduledSoundPlayer](https://developer.apple.com/documentation/audiotoolbox/1619493-generator_audio_unit_subtypes/kaudiounitsubtype_scheduledsoundplayer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_SpatialMixer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_spatialmixer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_Splitter](https://developer.apple.com/documentation/audiotoolbox/1584145-converter_audio_unit_subtypes/kaudiounitsubtype_splitter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_Varispeed](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_varispeed)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitSubType_VoiceProcessingIO](https://developer.apple.com/documentation/audiotoolbox/1584139-input_output_audio_unit_subtypes/kaudiounitsubtype_voiceprocessingio)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_Effect](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_effect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_FormatConverter](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_formatconverter)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_Generator](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_generator)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_MIDIProcessor](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_midiprocessor)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_Mixer](https://developer.apple.com/documentation/audiotoolbox/kaudiounittype_mixer)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_MusicDevice](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_musicdevice)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_MusicEffect](https://developer.apple.com/documentation/audiotoolbox/kaudiounittype_musiceffect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_OfflineEffect](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_offlineeffect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_Output](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_output)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_Panner](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types/kaudiounittype_panner)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_RemoteEffect](https://developer.apple.com/documentation/audiotoolbox/1619501-anonymous/kaudiounittype_remoteeffect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_RemoteGenerator](https://developer.apple.com/documentation/audiotoolbox/kaudiounittype_remotegenerator)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_RemoteInstrument](https://developer.apple.com/documentation/audiotoolbox/kaudiounittype_remoteinstrument)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitType_RemoteMusicEffect](https://developer.apple.com/documentation/audiotoolbox/1619501-anonymous/kaudiounittype_remotemusiceffect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAudioUnitUninitializeSelect](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele/kaudiounituninitializeselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_AllNotesOff](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_allnotesoff)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_AllSoundOff](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_allsoundoff)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_ChannelPressure](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_channelpressure)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_DataEntry](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_dataentry)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_DataEntry_LSB](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_dataentry_lsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Expression](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_expression)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Expression_LSB](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_expression_lsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Foot](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_foot)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Foot_LSB](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_foot_lsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_KeyPressure](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_keypressure)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_KeyPressure_FirstKey](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_keypressure_firstkey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_KeyPressure_LastKey](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_keypressure_lastkey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_ModWheel](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_modwheel)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_ModWheel_LSB](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_modwheel_lsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Pan](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_pan)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Pan_LSB](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_pan_lsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_PitchBend](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_pitchbend)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_ResetAllControllers](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_resetallcontrollers)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Sostenuto](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_sostenuto)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Sustain](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_sustain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Volume](https://developer.apple.com/documentation/audiotoolbox/1389613-midi_audio_unit_parameters/kaugroupparameterid_volume)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUGroupParameterID_Volume_LSB](https://developer.apple.com/documentation/audiotoolbox/kaugroupparameterid_volume_lsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAULowShelfParam_CutoffFrequency](https://developer.apple.com/documentation/audiotoolbox/1389995-low_shelf_filter_unit_parameters/kaulowshelfparam_cutofffrequency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAULowShelfParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1389995-low_shelf_filter_unit_parameters/kaulowshelfparam_gain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUMIDISynthProperty_EnablePreload](https://developer.apple.com/documentation/audiotoolbox/1534190-anonymous/kaumidisynthproperty_enablepreload)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_2ndOrderButterworthHighPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_2ndorderbutterworthhighpass)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_2ndOrderButterworthLowPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_2ndorderbutterworthlowpass)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_BandPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_bandpass)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_BandStop](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_bandstop)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_HighShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_highshelf)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_LowShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_lowshelf)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_Parametric](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_parametric)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_ResonantHighPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_resonanthighpass)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_ResonantHighShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_resonanthighshelf)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_ResonantLowPass](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_resonantlowpass)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQFilterType_ResonantLowShelf](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqfiltertype_resonantlowshelf)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQParam_Bandwidth](https://developer.apple.com/documentation/audiotoolbox/1389745-anonymous/kaunbandeqparam_bandwidth)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQParam_BypassBand](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_bypassband)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQParam_FilterType](https://developer.apple.com/documentation/audiotoolbox/1389745-anonymous/kaunbandeqparam_filtertype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQParam_Frequency](https://developer.apple.com/documentation/audiotoolbox/1389745-anonymous/kaunbandeqparam_frequency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1389745-anonymous/kaunbandeqparam_gain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQParam_GlobalGain](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqparam_globalgain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQProperty_BiquadCoefficients](https://developer.apple.com/documentation/audiotoolbox/1534022-anonymous/kaunbandeqproperty_biquadcoefficients)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQProperty_MaxNumberOfBands](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqproperty_maxnumberofbands)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUNBandEQProperty_NumberOfBands](https://developer.apple.com/documentation/audiotoolbox/kaunbandeqproperty_numberofbands)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetCPULoadKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetcpuloadkey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetDataKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetdatakey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetElementNameKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetelementnamekey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetExternalFileRefs](https://developer.apple.com/documentation/audiotoolbox/kaupresetexternalfilerefs)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetManufacturerKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetmanufacturerkey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetNameKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetnamekey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetPartKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetpartkey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetRenderQualityKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetrenderqualitykey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetSubtypeKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetsubtypekey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetTypeKey](https://developer.apple.com/documentation/audiotoolbox/kaupresettypekey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUPresetVersionKey](https://developer.apple.com/documentation/audiotoolbox/kaupresetversionkey)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSampler_DefaultBankLSB](https://developer.apple.com/documentation/audiotoolbox/1534086-anonymous/kausampler_defaultbanklsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSampler_DefaultMelodicBankMSB](https://developer.apple.com/documentation/audiotoolbox/1534086-anonymous/kausampler_defaultmelodicbankmsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSampler_DefaultPercussionBankMSB](https://developer.apple.com/documentation/audiotoolbox/kausampler_defaultpercussionbankmsb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSamplerParam_CoarseTuning](https://developer.apple.com/documentation/audiotoolbox/kausamplerparam_coarsetuning)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSamplerParam_FineTuning](https://developer.apple.com/documentation/audiotoolbox/1389769-anonymous/kausamplerparam_finetuning)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSamplerParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1389769-anonymous/kausamplerparam_gain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSamplerParam_Pan](https://developer.apple.com/documentation/audiotoolbox/1389769-anonymous/kausamplerparam_pan)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSamplerProperty_BankAndPreset](https://developer.apple.com/documentation/audiotoolbox/kausamplerproperty_bankandpreset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSamplerProperty_LoadAudioFiles](https://developer.apple.com/documentation/audiotoolbox/1533959-anonymous/kausamplerproperty_loadaudiofiles)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSamplerProperty_LoadInstrument](https://developer.apple.com/documentation/audiotoolbox/1533959-anonymous/kausamplerproperty_loadinstrument)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUSamplerProperty_LoadPresetFromBank](https://developer.apple.com/documentation/audiotoolbox/kausamplerproperty_loadpresetfrombank)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUVoiceIOProperty_BypassVoiceProcessing](https://developer.apple.com/documentation/audiotoolbox/1534007-voice_processing_i_o_audio_unit_/kauvoiceioproperty_bypassvoiceprocessing)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUVoiceIOProperty_DuckNonVoiceAudio](https://developer.apple.com/documentation/audiotoolbox/1621044-anonymous/kauvoiceioproperty_ducknonvoiceaudio)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUVoiceIOProperty_MuteOutput](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioproperty_muteoutput)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUVoiceIOProperty_VoiceProcessingEnableAGC](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioproperty_voiceprocessingenableagc)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kAUVoiceIOProperty_VoiceProcessingQuality](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioproperty_voiceprocessingquality)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kBandpassParam_Bandwidth](https://developer.apple.com/documentation/audiotoolbox/1390144-bandpass_unit_parameters/kbandpassparam_bandwidth)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kBandpassParam_CenterFrequency](https://developer.apple.com/documentation/audiotoolbox/kbandpassparam_centerfrequency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDelayParam_DelayTime](https://developer.apple.com/documentation/audiotoolbox/1390010-anonymous/kdelayparam_delaytime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDelayParam_Feedback](https://developer.apple.com/documentation/audiotoolbox/1390010-anonymous/kdelayparam_feedback)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDelayParam_LopassCutoff](https://developer.apple.com/documentation/audiotoolbox/1390010-anonymous/kdelayparam_lopasscutoff)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDelayParam_WetDryMix](https://developer.apple.com/documentation/audiotoolbox/1390010-anonymous/kdelayparam_wetdrymix)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_CubicTerm](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_cubicterm)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_Decay](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_decay)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_Decimation](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_decimation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_DecimationMix](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_decimationmix)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_Delay](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_delay)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_DelayMix](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_delaymix)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_FinalMix](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_finalmix)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_LinearTerm](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_linearterm)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_PolynomialMix](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_polynomialmix)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_RingModBalance](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_ringmodbalance)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_RingModFreq1](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_ringmodfreq1)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_RingModFreq2](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_ringmodfreq2)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_RingModMix](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_ringmodmix)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_Rounding](https://developer.apple.com/documentation/audiotoolbox/kdistortionparam_rounding)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_SoftClipGain](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_softclipgain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDistortionParam_SquaredTerm](https://developer.apple.com/documentation/audiotoolbox/1390086-anonymous/kdistortionparam_squaredterm)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_AttackTime](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_attacktime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_CompressionAmount](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_compressionamount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_ExpansionRatio](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_expansionratio)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_ExpansionThreshold](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_expansionthreshold)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_HeadRoom](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_headroom)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_InputAmplitude](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_inputamplitude)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_MasterGain](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_mastergain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_OutputAmplitude](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_outputamplitude)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_ReleaseTime](https://developer.apple.com/documentation/audiotoolbox/kdynamicsprocessorparam_releasetime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kDynamicsProcessorParam_Threshold](https://developer.apple.com/documentation/audiotoolbox/1389787-dynamics_processor_unit_paramete/kdynamicsprocessorparam_threshold)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kHALOutputParam_Volume](https://developer.apple.com/documentation/audiotoolbox/1389916-output_unit_parameters/khaloutputparam_volume)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kHighShelfParam_CutOffFrequency](https://developer.apple.com/documentation/audiotoolbox/khighshelfparam_cutofffrequency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kHighShelfParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1389967-high_shelf_filter_unit_parameter/khighshelfparam_gain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kHipassParam_CutoffFrequency](https://developer.apple.com/documentation/audiotoolbox/1389948-highpass_unit_parameters/khipassparam_cutofffrequency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kHipassParam_Resonance](https://developer.apple.com/documentation/audiotoolbox/khipassparam_resonance)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kInstrumentType_Audiofile](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_audiofile)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kInstrumentType_AUPreset](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_aupreset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kInstrumentType_DLSPreset](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_dlspreset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kInstrumentType_EXS24](https://developer.apple.com/documentation/audiotoolbox/kinstrumenttype_exs24)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kInstrumentType_SF2Preset](https://developer.apple.com/documentation/audiotoolbox/1534202-anonymous/kinstrumenttype_sf2preset)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kLimiterParam_AttackTime](https://developer.apple.com/documentation/audiotoolbox/klimiterparam_attacktime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kLimiterParam_DecayTime](https://developer.apple.com/documentation/audiotoolbox/1389597-peak_limiter_unit_parameters/klimiterparam_decaytime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kLimiterParam_PreGain](https://developer.apple.com/documentation/audiotoolbox/1389597-peak_limiter_unit_parameters/klimiterparam_pregain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kLowPassParam_CutoffFrequency](https://developer.apple.com/documentation/audiotoolbox/1389999-lowpass_unit_parameters/klowpassparam_cutofffrequency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kLowPassParam_Resonance](https://developer.apple.com/documentation/audiotoolbox/klowpassparam_resonance)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_Enable](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_enable)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_PostAveragePower](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_postaveragepower)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_PostAveragePowerLinear](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_postaveragepowerlinear)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_PostPeakHoldLevel](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_postpeakholdlevel)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_PostPeakHoldLevelLinear](https://developer.apple.com/documentation/audiotoolbox/kmatrixmixerparam_postpeakholdlevellinear)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_PreAveragePower](https://developer.apple.com/documentation/audiotoolbox/kmatrixmixerparam_preaveragepower)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_PreAveragePowerLinear](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_preaveragepowerlinear)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_PrePeakHoldLevel](https://developer.apple.com/documentation/audiotoolbox/1390003-anonymous/kmatrixmixerparam_prepeakholdlevel)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_PrePeakHoldLevelLinear](https://developer.apple.com/documentation/audiotoolbox/kmatrixmixerparam_prepeakholdlevellinear)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMatrixMixerParam_Volume](https://developer.apple.com/documentation/audiotoolbox/kmatrixmixerparam_volume)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMultiChannelMixerParam_Enable](https://developer.apple.com/documentation/audiotoolbox/1389739-multichannel_mixer_unit_paramete/kmultichannelmixerparam_enable)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMultiChannelMixerParam_Pan](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_pan)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMultiChannelMixerParam_PostAveragePower](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_postaveragepower)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMultiChannelMixerParam_PostPeakHoldLevel](https://developer.apple.com/documentation/audiotoolbox/1389739-multichannel_mixer_unit_paramete/kmultichannelmixerparam_postpeakholdlevel)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMultiChannelMixerParam_PreAveragePower](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_preaveragepower)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMultiChannelMixerParam_PrePeakHoldLevel](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_prepeakholdlevel)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMultiChannelMixerParam_Volume](https://developer.apple.com/documentation/audiotoolbox/1389739-multichannel_mixer_unit_paramete/kmultichannelmixerparam_volume)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceMIDIEventSelect](https://developer.apple.com/documentation/audiotoolbox/1473469-anonymous/kmusicdevicemidieventselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDevicePrepareInstrumentSelect](https://developer.apple.com/documentation/audiotoolbox/1473469-anonymous/kmusicdeviceprepareinstrumentselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceProperty_BankName](https://developer.apple.com/documentation/audiotoolbox/1533930-anonymous/kmusicdeviceproperty_bankname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceProperty_InstrumentCount](https://developer.apple.com/documentation/audiotoolbox/kmusicdeviceproperty_instrumentcount)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceProperty_InstrumentName](https://developer.apple.com/documentation/audiotoolbox/1533931-anonymous/kmusicdeviceproperty_instrumentname)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceProperty_InstrumentNumber](https://developer.apple.com/documentation/audiotoolbox/kmusicdeviceproperty_instrumentnumber)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceProperty_SoundBankURL](https://developer.apple.com/documentation/audiotoolbox/kmusicdeviceproperty_soundbankurl)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceRange](https://developer.apple.com/documentation/audiotoolbox/1473469-anonymous/kmusicdevicerange)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceReleaseInstrumentSelect](https://developer.apple.com/documentation/audiotoolbox/kmusicdevicereleaseinstrumentselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceStartNoteSelect](https://developer.apple.com/documentation/audiotoolbox/kmusicdevicestartnoteselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceStopNoteSelect](https://developer.apple.com/documentation/audiotoolbox/1473469-anonymous/kmusicdevicestopnoteselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicDeviceSysExSelect](https://developer.apple.com/documentation/audiotoolbox/kmusicdevicesysexselect)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicNoteEvent_Unused](https://developer.apple.com/documentation/audiotoolbox/1473494-anonymous/kmusicnoteevent_unused)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kMusicNoteEvent_UseGroupInstrument](https://developer.apple.com/documentation/audiotoolbox/kmusicnoteevent_usegroupinstrument)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kNewTimePitchParam_EnablePeakLocking](https://developer.apple.com/documentation/audiotoolbox/1389643-anonymous/knewtimepitchparam_enablepeaklocking)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kNewTimePitchParam_Overlap](https://developer.apple.com/documentation/audiotoolbox/1389643-anonymous/knewtimepitchparam_overlap)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kNewTimePitchParam_Pitch](https://developer.apple.com/documentation/audiotoolbox/1389643-anonymous/knewtimepitchparam_pitch)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kNewTimePitchParam_Rate](https://developer.apple.com/documentation/audiotoolbox/1389643-anonymous/knewtimepitchparam_rate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kNumAUNBandEQFilterTypes](https://developer.apple.com/documentation/audiotoolbox/1389965-mutitype_eq_unit_filter_types/knumaunbandeqfiltertypes)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kNumberOfResponseFrequencies](https://developer.apple.com/documentation/audiotoolbox/1534092-frequency_response_constants/knumberofresponsefrequencies)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kParametricEQParam_CenterFreq](https://developer.apple.com/documentation/audiotoolbox/1389950-parametric_eq_unit_parameters/kparametriceqparam_centerfreq)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kParametricEQParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1389950-parametric_eq_unit_parameters/kparametriceqparam_gain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kParametricEQParam_Q](https://developer.apple.com/documentation/audiotoolbox/1389950-parametric_eq_unit_parameters/kparametriceqparam_q)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRandomParam_BoundA](https://developer.apple.com/documentation/audiotoolbox/1389639-anonymous/krandomparam_bounda)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRandomParam_BoundB](https://developer.apple.com/documentation/audiotoolbox/1389639-anonymous/krandomparam_boundb)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRandomParam_Curve](https://developer.apple.com/documentation/audiotoolbox/1389639-anonymous/krandomparam_curve)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRenderQuality_High](https://developer.apple.com/documentation/audiotoolbox/krenderquality_high)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRenderQuality_Low](https://developer.apple.com/documentation/audiotoolbox/1534177-renderquality/krenderquality_low)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRenderQuality_Max](https://developer.apple.com/documentation/audiotoolbox/1534177-renderquality/krenderquality_max)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRenderQuality_Medium](https://developer.apple.com/documentation/audiotoolbox/1534177-renderquality/krenderquality_medium)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRenderQuality_Min](https://developer.apple.com/documentation/audiotoolbox/krenderquality_min)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverb2Param_DecayTimeAt0Hz](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_decaytimeat0hz)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverb2Param_DecayTimeAtNyquist](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_decaytimeatnyquist)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverb2Param_DryWetMix](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_drywetmix)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverb2Param_Gain](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_gain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverb2Param_MaxDelayTime](https://developer.apple.com/documentation/audiotoolbox/1615024-reverb_unit_parameters/kreverb2param_maxdelaytime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverb2Param_MinDelayTime](https://developer.apple.com/documentation/audiotoolbox/kreverb2param_mindelaytime)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverb2Param_RandomizeReflections](https://developer.apple.com/documentation/audiotoolbox/kreverb2param_randomizereflections)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverbParam_FilterBandwidth](https://developer.apple.com/documentation/audiotoolbox/kreverbparam_filterbandwidth)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverbParam_FilterEnable](https://developer.apple.com/documentation/audiotoolbox/1390119-additional_reverb_parameters/kreverbparam_filterenable)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverbParam_FilterFrequency](https://developer.apple.com/documentation/audiotoolbox/1390119-additional_reverb_parameters/kreverbparam_filterfrequency)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverbParam_FilterGain](https://developer.apple.com/documentation/audiotoolbox/kreverbparam_filtergain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kReverbParam_FilterType](https://developer.apple.com/documentation/audiotoolbox/kreverbparam_filtertype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRoundTripAACParam_EncodingStrategy](https://developer.apple.com/documentation/audiotoolbox/kroundtripaacparam_encodingstrategy)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRoundTripAACParam_Format](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_format)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kRoundTripAACParam_RateOrQuality](https://developer.apple.com/documentation/audiotoolbox/1389808-anonymous/kroundtripaacparam_rateorquality)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_Azimuth](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_azimuth)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_Distance](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_distance)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_Elevation](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_elevation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_Enable](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_enable)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_Gain](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_gain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_GlobalReverbGain](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_globalreverbgain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_MaxGain](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_maxgain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_MinGain](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_mingain)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_ObstructionAttenuation](https://developer.apple.com/documentation/audiotoolbox/kspatialmixerparam_obstructionattenuation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_OcclusionAttenuation](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_occlusionattenuation)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_PlaybackRate](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_playbackrate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kSpatialMixerParam_ReverbBlend](https://developer.apple.com/documentation/audiotoolbox/1390073-anonymous/kspatialmixerparam_reverbblend)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kTimePitchParam_Rate](https://developer.apple.com/documentation/audiotoolbox/1389946-autimepitch_autimepitch_offline_/ktimepitchparam_rate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kVarispeedParam_PlaybackCents](https://developer.apple.com/documentation/audiotoolbox/1390014-varispeed_unit_parameters/kvarispeedparam_playbackcents)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [kVarispeedParam_PlaybackRate](https://developer.apple.com/documentation/audiotoolbox/1390014-varispeed_unit_parameters/kvarispeedparam_playbackrate)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceComponent](https://developer.apple.com/documentation/audiotoolbox/musicdevicecomponent)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceGroupID](https://developer.apple.com/documentation/audiotoolbox/musicdevicegroupid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceInstrumentID](https://developer.apple.com/documentation/audiotoolbox/musicdeviceinstrumentid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceMIDIEvent(_: MusicDeviceComponent, _: UInt32, _: UInt32, _: UInt32, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1439861-musicdevicemidievent)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceMIDIEventProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicemidieventproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias MusicDeviceMIDIEventProc = (UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UInt32) -> OSStatus ``` | AudioUnit |
| To | ``` typealias MusicDeviceMIDIEventProc = (UnsafeMutableRawPointer, UInt32, UInt32, UInt32, UInt32) -> OSStatus ``` | AudioToolbox |

Modified [MusicDeviceStartNote(_: MusicDeviceComponent, _: MusicDeviceInstrumentID, _: MusicDeviceGroupID, _: UnsafeMutablePointer<NoteInstanceID>, _: UInt32, _: UnsafePointer<MusicDeviceNoteParams>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440960-musicdevicestartnote)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceStartNoteProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicestartnoteproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias MusicDeviceStartNoteProc = (UnsafeMutablePointer<Void>, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus ``` | AudioUnit |
| To | ``` typealias MusicDeviceStartNoteProc = (UnsafeMutableRawPointer, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus ``` | AudioToolbox |

Modified [MusicDeviceStopNote(_: MusicDeviceComponent, _: MusicDeviceGroupID, _: NoteInstanceID, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1440390-musicdevicestopnote)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceStopNoteProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicestopnoteproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias MusicDeviceStopNoteProc = (UnsafeMutablePointer<Void>, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus ``` | AudioUnit |
| To | ``` typealias MusicDeviceStopNoteProc = (UnsafeMutableRawPointer, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus ``` | AudioToolbox |

Modified [MusicDeviceSysEx(_: MusicDeviceComponent, _: UnsafePointer<UInt8>, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1438996-musicdevicesysex)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [MusicDeviceSysExProc](https://developer.apple.com/documentation/audiotoolbox/musicdevicesysexproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias MusicDeviceSysExProc = (UnsafeMutablePointer<Void>, UnsafePointer<UInt8>, UInt32) -> OSStatus ``` | AudioUnit |
| To | ``` typealias MusicDeviceSysExProc = (UnsafeMutableRawPointer, UnsafePointer<UInt8>, UInt32) -> OSStatus ``` | AudioToolbox |

Modified [MusicEventIterator](https://developer.apple.com/documentation/audiotoolbox/musiceventiterator)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicEventIterator = COpaquePointer ``` |
| To | ``` typealias MusicEventIterator = OpaquePointer ``` |

Modified [MusicEventIteratorGetEventInfo(_: MusicEventIterator, _: UnsafeMutablePointer<MusicTimeStamp>, _: UnsafeMutablePointer<MusicEventType>, _: UnsafeMutablePointer<UnsafeRawPointer?>, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501702-musiceventiteratorgeteventinfo)

|  | Declaration |
| --- | --- |
| From | ``` func MusicEventIteratorGetEventInfo(_ inIterator: MusicEventIterator, _ outTimeStamp: UnsafeMutablePointer<MusicTimeStamp>, _ outEventType: UnsafeMutablePointer<MusicEventType>, _ outEventData: UnsafeMutablePointer<UnsafePointer<Void>>, _ outEventDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func MusicEventIteratorGetEventInfo(_ inIterator: MusicEventIterator, _ outTimeStamp: UnsafeMutablePointer<MusicTimeStamp>, _ outEventType: UnsafeMutablePointer<MusicEventType>, _ outEventData: UnsafeMutablePointer<UnsafeRawPointer?>, _ outEventDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [MusicEventIteratorSetEventInfo(_: MusicEventIterator, _: MusicEventType, _: UnsafeRawPointer) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503101-musiceventiteratorseteventinfo)

|  | Declaration |
| --- | --- |
| From | ``` func MusicEventIteratorSetEventInfo(_ inIterator: MusicEventIterator, _ inEventType: MusicEventType, _ inEventData: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func MusicEventIteratorSetEventInfo(_ inIterator: MusicEventIterator, _ inEventType: MusicEventType, _ inEventData: UnsafeRawPointer) -> OSStatus ``` |

Modified [MusicPlayer](https://developer.apple.com/documentation/audiotoolbox/musicplayer)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicPlayer = COpaquePointer ``` |
| To | ``` typealias MusicPlayer = OpaquePointer ``` |

Modified [MusicPlayerGetSequence(_: MusicPlayer, _: UnsafeMutablePointer<MusicSequence?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502355-musicplayergetsequence)

|  | Declaration |
| --- | --- |
| From | ``` func MusicPlayerGetSequence(_ inPlayer: MusicPlayer, _ outSequence: UnsafeMutablePointer<MusicSequence>) -> OSStatus ``` |
| To | ``` func MusicPlayerGetSequence(_ inPlayer: MusicPlayer, _ outSequence: UnsafeMutablePointer<MusicSequence?>) -> OSStatus ``` |

Modified [MusicPlayerSetSequence(_: MusicPlayer, _: MusicSequence?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502518-musicplayersetsequence)

|  | Declaration |
| --- | --- |
| From | ``` func MusicPlayerSetSequence(_ inPlayer: MusicPlayer, _ inSequence: MusicSequence) -> OSStatus ``` |
| To | ``` func MusicPlayerSetSequence(_ inPlayer: MusicPlayer, _ inSequence: MusicSequence?) -> OSStatus ``` |

Modified [MusicSequence](https://developer.apple.com/documentation/audiotoolbox/musicsequence)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicSequence = COpaquePointer ``` |
| To | ``` typealias MusicSequence = OpaquePointer ``` |

Modified [MusicSequenceGetAUGraph(_: MusicSequence, _: UnsafeMutablePointer<AUGraph?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502317-musicsequencegetaugraph)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceGetAUGraph(_ inSequence: MusicSequence, _ outGraph: UnsafeMutablePointer<AUGraph>) -> OSStatus ``` |
| To | ``` func MusicSequenceGetAUGraph(_ inSequence: MusicSequence, _ outGraph: UnsafeMutablePointer<AUGraph?>) -> OSStatus ``` |

Modified [MusicSequenceGetIndTrack(_: MusicSequence, _: UInt32, _: UnsafeMutablePointer<MusicTrack?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501623-musicsequencegetindtrack)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceGetIndTrack(_ inSequence: MusicSequence, _ inTrackIndex: UInt32, _ outTrack: UnsafeMutablePointer<MusicTrack>) -> OSStatus ``` |
| To | ``` func MusicSequenceGetIndTrack(_ inSequence: MusicSequence, _ inTrackIndex: UInt32, _ outTrack: UnsafeMutablePointer<MusicTrack?>) -> OSStatus ``` |

Modified [MusicSequenceGetTempoTrack(_: MusicSequence, _: UnsafeMutablePointer<MusicTrack?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502277-musicsequencegettempotrack)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceGetTempoTrack(_ inSequence: MusicSequence, _ outTrack: UnsafeMutablePointer<MusicTrack>) -> OSStatus ``` |
| To | ``` func MusicSequenceGetTempoTrack(_ inSequence: MusicSequence, _ outTrack: UnsafeMutablePointer<MusicTrack?>) -> OSStatus ``` |

Modified [MusicSequenceNewTrack(_: MusicSequence, _: UnsafeMutablePointer<MusicTrack?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503090-musicsequencenewtrack)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceNewTrack(_ inSequence: MusicSequence, _ outTrack: UnsafeMutablePointer<MusicTrack>) -> OSStatus ``` |
| To | ``` func MusicSequenceNewTrack(_ inSequence: MusicSequence, _ outTrack: UnsafeMutablePointer<MusicTrack?>) -> OSStatus ``` |

Modified [MusicSequenceSetAUGraph(_: MusicSequence, _: AUGraph?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503097-musicsequencesetaugraph)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceSetAUGraph(_ inSequence: MusicSequence, _ inGraph: AUGraph) -> OSStatus ``` |
| To | ``` func MusicSequenceSetAUGraph(_ inSequence: MusicSequence, _ inGraph: AUGraph?) -> OSStatus ``` |

Modified [MusicSequenceSetUserCallback(_: MusicSequence, _: AudioToolbox.MusicSequenceUserCallback?, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503188-musicsequencesetusercallback)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceSetUserCallback(_ inSequence: MusicSequence, _ inCallback: MusicSequenceUserCallback?, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func MusicSequenceSetUserCallback(_ inSequence: MusicSequence, _ inCallback: AudioToolbox.MusicSequenceUserCallback?, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [MusicSequenceUserCallback](https://developer.apple.com/documentation/audiotoolbox/musicsequenceusercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicSequenceUserCallback = (UnsafeMutablePointer<Void>, MusicSequence, MusicTrack, MusicTimeStamp, UnsafePointer<MusicEventUserData>, MusicTimeStamp, MusicTimeStamp) -> Void ``` |
| To | ``` typealias MusicSequenceUserCallback = (UnsafeMutableRawPointer?, MusicSequence, MusicTrack, MusicTimeStamp, UnsafePointer<MusicEventUserData>, MusicTimeStamp, MusicTimeStamp) -> Swift.Void ``` |

Modified [MusicTrack](https://developer.apple.com/documentation/audiotoolbox/musictrack)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicTrack = COpaquePointer ``` |
| To | ``` typealias MusicTrack = OpaquePointer ``` |

Modified [MusicTrackGetProperty(_: MusicTrack, _: UInt32, _: UnsafeMutableRawPointer, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503210-musictrackgetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MusicTrackGetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ outData: UnsafeMutablePointer<Void>, _ ioLength: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func MusicTrackGetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ outData: UnsafeMutableRawPointer, _ ioLength: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [MusicTrackGetSequence(_: MusicTrack, _: UnsafeMutablePointer<MusicSequence?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502453-musictrackgetsequence)

|  | Declaration |
| --- | --- |
| From | ``` func MusicTrackGetSequence(_ inTrack: MusicTrack, _ outSequence: UnsafeMutablePointer<MusicSequence>) -> OSStatus ``` |
| To | ``` func MusicTrackGetSequence(_ inTrack: MusicTrack, _ outSequence: UnsafeMutablePointer<MusicSequence?>) -> OSStatus ``` |

Modified [MusicTrackSetProperty(_: MusicTrack, _: UInt32, _: UnsafeMutableRawPointer, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501688-musictracksetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func MusicTrackSetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ inData: UnsafeMutablePointer<Void>, _ inLength: UInt32) -> OSStatus ``` |
| To | ``` func MusicTrackSetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ inData: UnsafeMutableRawPointer, _ inLength: UInt32) -> OSStatus ``` |

Modified [NewAUGraph(_: UnsafeMutablePointer<AUGraph?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502296-newaugraph)

|  | Declaration |
| --- | --- |
| From | ``` func NewAUGraph(_ outGraph: UnsafeMutablePointer<AUGraph>) -> OSStatus ``` |
| To | ``` func NewAUGraph(_ outGraph: UnsafeMutablePointer<AUGraph?>) -> OSStatus ``` |

Modified [NewMusicEventIterator(_: MusicTrack, _: UnsafeMutablePointer<MusicEventIterator?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502076-newmusiceventiterator)

|  | Declaration |
| --- | --- |
| From | ``` func NewMusicEventIterator(_ inTrack: MusicTrack, _ outIterator: UnsafeMutablePointer<MusicEventIterator>) -> OSStatus ``` |
| To | ``` func NewMusicEventIterator(_ inTrack: MusicTrack, _ outIterator: UnsafeMutablePointer<MusicEventIterator?>) -> OSStatus ``` |

Modified [NewMusicPlayer(_: UnsafeMutablePointer<MusicPlayer?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503211-newmusicplayer)

|  | Declaration |
| --- | --- |
| From | ``` func NewMusicPlayer(_ outPlayer: UnsafeMutablePointer<MusicPlayer>) -> OSStatus ``` |
| To | ``` func NewMusicPlayer(_ outPlayer: UnsafeMutablePointer<MusicPlayer?>) -> OSStatus ``` |

Modified [NewMusicSequence(_: UnsafeMutablePointer<MusicSequence?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502634-newmusicsequence)

|  | Declaration |
| --- | --- |
| From | ``` func NewMusicSequence(_ outSequence: UnsafeMutablePointer<MusicSequence>) -> OSStatus ``` |
| To | ``` func NewMusicSequence(_ outSequence: UnsafeMutablePointer<MusicSequence?>) -> OSStatus ``` |

Modified [NoteInstanceID](https://developer.apple.com/documentation/audiotoolbox/noteinstanceid)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

Modified [ScheduledAudioFileRegionCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudiofileregioncompletionproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias ScheduledAudioFileRegionCompletionProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<ScheduledAudioFileRegion>, OSStatus) -> Void ``` | AudioUnit |
| To | ``` typealias ScheduledAudioFileRegionCompletionProc = (UnsafeMutableRawPointer?, UnsafeMutablePointer<ScheduledAudioFileRegion>, OSStatus) -> Swift.Void ``` | AudioToolbox |

Modified [ScheduledAudioSliceCompletionProc](https://developer.apple.com/documentation/audiotoolbox/scheduledaudioslicecompletionproc)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` typealias ScheduledAudioSliceCompletionProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<ScheduledAudioSlice>) -> Void ``` | AudioUnit |
| To | ``` typealias ScheduledAudioSliceCompletionProc = (UnsafeMutableRawPointer?, UnsafeMutablePointer<ScheduledAudioSlice>) -> Swift.Void ``` | AudioToolbox |

Modified [SetAudioUnitParameterDisplayType(_: AudioUnitParameterOptions, _: AudioUnitParameterOptions) -> AudioUnitParameterOptions](https://developer.apple.com/documentation/audiotoolbox/1440769-setaudiounitparameterdisplaytype)

|  | Module |
| --- | --- |
| From | AudioUnit |
| To | AudioToolbox |

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
