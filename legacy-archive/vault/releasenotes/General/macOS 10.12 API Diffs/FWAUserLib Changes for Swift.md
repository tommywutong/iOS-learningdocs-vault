---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/FWAUserLib.html
archived_at: '2026-07-18T02:51:17.359868Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# FWAUserLib Changes for Swift

### FWAUserLib

Modified [CreateAsyncWakePort(_: FWARef!, _: UnsafeMutablePointer<mach_port_t>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436640-createasyncwakeport)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func CreateAsyncWakePort(_ inRef: FWARef, _ notifyPort: UnsafeMutablePointer<mach_port_t>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func CreateAsyncWakePort(_ inRef: FWARef!, _ notifyPort: UnsafeMutablePointer<mach_port_t>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAAttachFWAudioMIDIStream(_: FWARef!, _: FWAMIDIStreamRef!, _: FWAIsochStreamRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437004-fwaattachfwaudiomidistream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAAttachFWAudioMIDIStream(_ inRef: FWARef, _ streamRef: FWAMIDIStreamRef, _ isochChannel: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAAttachFWAudioMIDIStream(_ inRef: FWARef!, _ streamRef: FWAMIDIStreamRef!, _ isochChannel: FWAIsochStreamRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAAttachFWAudioStream(_: FWARef!, _: FWAAudioStreamRef!, _: FWAIsochStreamRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436726-fwaattachfwaudiostream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAAttachFWAudioStream(_ inRef: FWARef, _ streamRef: FWAAudioStreamRef, _ isochChannel: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAAttachFWAudioStream(_ inRef: FWARef!, _ streamRef: FWAAudioStreamRef!, _ isochChannel: FWAIsochStreamRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAAudioPlugRef](https://developer.apple.com/documentation/fwauserlib/fwaaudioplugref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAAudioPlugRef = COpaquePointer ``` |
| To | ``` typealias FWAAudioPlugRef = OpaquePointer ``` |

Modified [FWAAudioStreamRef](https://developer.apple.com/documentation/fwauserlib/fwaaudiostreamref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAAudioStreamRef = COpaquePointer ``` |
| To | ``` typealias FWAAudioStreamRef = OpaquePointer ``` |

Modified [FWAClose(_: FWARef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436680-fwaclose)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAClose(_ inRef: FWARef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAClose(_ inRef: FWARef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACountDevices(_: UnsafeMutablePointer<UInt16>!, _: UnsafeMutablePointer<UInt16>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436510-fwacountdevices)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACountDevices(_ deviceNodeIDArray: UnsafeMutablePointer<UInt16>, _ deviceCount: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACountDevices(_ deviceNodeIDArray: UnsafeMutablePointer<UInt16>!, _ deviceCount: UnsafeMutablePointer<UInt16>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateAudioStream(_: FWARef!, _: UInt32, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436644-fwacreateaudiostream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateAudioStream(_ inRef: FWARef, _ audioIO: UInt32, _ audioStreamRef: UnsafeMutablePointer<UInt32>, _ sequenceNum: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateAudioStream(_ inRef: FWARef!, _ audioIO: UInt32, _ audioStreamRef: UnsafeMutablePointer<UInt32>!, _ sequenceNum: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateFWAudioDevice(_: FWARef!, _: UnsafePointer<Int8>!, _: UInt32, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<FWADeviceRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436773-fwacreatefwaudiodevice)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateFWAudioDevice(_ inRef: FWARef, _ deviceName: UnsafePointer<Int8>, _ vendorID: UInt32, _ guid: UnsafePointer<Int8>, _ device: UnsafeMutablePointer<FWADeviceRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateFWAudioDevice(_ inRef: FWARef!, _ deviceName: UnsafePointer<Int8>!, _ vendorID: UInt32, _ guid: UnsafePointer<Int8>!, _ device: UnsafeMutablePointer<FWADeviceRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateFWAudioEngine(_: FWARef!, _: FWADeviceRef!, _: Bool, _: Bool, _: UnsafeMutablePointer<FWAEngineRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436982-fwacreatefwaudioengine)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateFWAudioEngine(_ inRef: FWARef, _ owningDevice: FWADeviceRef, _ hasInput: Bool, _ hasOutput: Bool, _ engine: UnsafeMutablePointer<FWAEngineRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateFWAudioEngine(_ inRef: FWARef!, _ owningDevice: FWADeviceRef!, _ hasInput: Bool, _ hasOutput: Bool, _ engine: UnsafeMutablePointer<FWAEngineRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateFWAudioMIDIDeviceNub(_: FWARef!, _: FWADeviceRef!, _: UnsafePointer<Int8>!, _: UInt32, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UInt32, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<FWAMIDIDeviceNubRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437027-fwacreatefwaudiomididevicenub)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateFWAudioMIDIDeviceNub(_ inRef: FWARef, _ owningDevice: FWADeviceRef, _ deviceName: UnsafePointer<Int8>, _ vendorID: UInt32, _ guid: UnsafePointer<Int8>, _ iconFilePath: UnsafePointer<Int8>, _ modelID: UInt32, _ editorPath: UnsafePointer<Int8>, _ device: UnsafeMutablePointer<FWAMIDIDeviceNubRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateFWAudioMIDIDeviceNub(_ inRef: FWARef!, _ owningDevice: FWADeviceRef!, _ deviceName: UnsafePointer<Int8>!, _ vendorID: UInt32, _ guid: UnsafePointer<Int8>!, _ iconFilePath: UnsafePointer<Int8>!, _ modelID: UInt32, _ editorPath: UnsafePointer<Int8>!, _ device: UnsafeMutablePointer<FWAMIDIDeviceNubRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateFWAudioMIDIPlug(_: FWARef!, _: FWAMIDIStreamRef!, _: UInt8, _: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<UInt8>!, _: UnsafeMutablePointer<FWAMIDIPlugRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436666-fwacreatefwaudiomidiplug)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateFWAudioMIDIPlug(_ inRef: FWARef, _ owningMIDIStreamRef: FWAMIDIStreamRef, _ mpxID: UInt8, _ plugName: UnsafeMutablePointer<Int8>, _ plugIdent: UnsafeMutablePointer<UInt8>, _ streamRef: UnsafeMutablePointer<FWAMIDIPlugRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateFWAudioMIDIPlug(_ inRef: FWARef!, _ owningMIDIStreamRef: FWAMIDIStreamRef!, _ mpxID: UInt8, _ plugName: UnsafeMutablePointer<Int8>!, _ plugIdent: UnsafeMutablePointer<UInt8>!, _ streamRef: UnsafeMutablePointer<FWAMIDIPlugRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateFWAudioMIDIStream(_: FWARef!, _: FWAIsochStreamRef!, _: UInt32, _: UInt32, _: UnsafeMutablePointer<FWAMIDIStreamRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437292-fwacreatefwaudiomidistream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateFWAudioMIDIStream(_ inRef: FWARef, _ owningIsochStreamRef: FWAIsochStreamRef, _ sequenceNumber: UInt32, _ direction: UInt32, _ streamRef: UnsafeMutablePointer<FWAMIDIStreamRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateFWAudioMIDIStream(_ inRef: FWARef!, _ owningIsochStreamRef: FWAIsochStreamRef!, _ sequenceNumber: UInt32, _ direction: UInt32, _ streamRef: UnsafeMutablePointer<FWAMIDIStreamRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateFWAudioPlug(_: FWARef!, _: FWAAudioStreamRef!, _: UInt32, _: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<UInt8>!, _: UnsafeMutablePointer<FWAAudioPlugRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437282-fwacreatefwaudioplug)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateFWAudioPlug(_ inRef: FWARef, _ owningStream: FWAAudioStreamRef, _ channelID: UInt32, _ plugName: UnsafeMutablePointer<Int8>, _ plugIdent: UnsafeMutablePointer<UInt8>, _ streamRef: UnsafeMutablePointer<FWAAudioPlugRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateFWAudioPlug(_ inRef: FWARef!, _ owningStream: FWAAudioStreamRef!, _ channelID: UInt32, _ plugName: UnsafeMutablePointer<Int8>!, _ plugIdent: UnsafeMutablePointer<UInt8>!, _ streamRef: UnsafeMutablePointer<FWAAudioPlugRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateFWAudioStream(_: FWARef!, _: FWAIsochStreamRef!, _: UInt32, _: UInt32, _: UInt32, _: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<UInt8>!, _: UnsafeMutablePointer<FWAAudioStreamRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437558-fwacreatefwaudiostream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateFWAudioStream(_ inRef: FWARef, _ owningIsochStreamRef: FWAIsochStreamRef, _ channelNumber: UInt32, _ direction: UInt32, _ numAudioChannels: UInt32, _ streamName: UnsafeMutablePointer<Int8>, _ streamIdent: UnsafeMutablePointer<UInt8>, _ streamRef: UnsafeMutablePointer<FWAAudioStreamRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateFWAudioStream(_ inRef: FWARef!, _ owningIsochStreamRef: FWAIsochStreamRef!, _ channelNumber: UInt32, _ direction: UInt32, _ numAudioChannels: UInt32, _ streamName: UnsafeMutablePointer<Int8>!, _ streamIdent: UnsafeMutablePointer<UInt8>!, _ streamRef: UnsafeMutablePointer<FWAAudioStreamRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateIsochStream(_: FWARef!, _: UInt32, _: FWAStreamDirection, _: UInt32, _: UInt32, _: UnsafeMutablePointer<FWAIsochStreamRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436848-fwacreateisochstream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateIsochStream(_ inRef: FWARef, _ channelNumber: UInt32, _ direction: FWAStreamDirection, _ numAudioChannels: UInt32, _ numMIDIChannels: UInt32, _ isochStreamRef: UnsafeMutablePointer<FWAIsochStreamRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateIsochStream(_ inRef: FWARef!, _ channelNumber: UInt32, _ direction: FWAStreamDirection, _ numAudioChannels: UInt32, _ numMIDIChannels: UInt32, _ isochStreamRef: UnsafeMutablePointer<FWAIsochStreamRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWACreateMIDIStream(_: FWARef!, _: UInt32, _: UInt32, _: UnsafeMutableRawPointer!, _: UInt32, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437534-fwacreatemidistream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWACreateMIDIStream(_ inRef: FWARef, _ midiIO: UInt32, _ bufSizeInBytes: UInt32, _ buf: UnsafeMutablePointer<Void>, _ sequenceNum: UInt32, _ midiStreamRef: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWACreateMIDIStream(_ inRef: FWARef!, _ midiIO: UInt32, _ bufSizeInBytes: UInt32, _ buf: UnsafeMutableRawPointer!, _ sequenceNum: UInt32, _ midiStreamRef: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADeviceRef](https://developer.apple.com/documentation/fwauserlib/fwadeviceref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWADeviceRef = COpaquePointer ``` |
| To | ``` typealias FWADeviceRef = OpaquePointer ``` |

Modified [FWADisposeAudioStream(_: FWARef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436789-fwadisposeaudiostream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeAudioStream(_ inRef: FWARef, _ audioStreamRef: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeAudioStream(_ inRef: FWARef!, _ audioStreamRef: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeFWAudioDevice(_: FWARef!, _: FWADeviceRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436966-fwadisposefwaudiodevice)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeFWAudioDevice(_ inRef: FWARef, _ device: FWADeviceRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeFWAudioDevice(_ inRef: FWARef!, _ device: FWADeviceRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeFWAudioEngine(_: FWARef!, _: FWAEngineRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436690-fwadisposefwaudioengine)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeFWAudioEngine(_ inRef: FWARef, _ engine: FWAEngineRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeFWAudioEngine(_ inRef: FWARef!, _ engine: FWAEngineRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeFWAudioMIDIDeviceNub(_: FWARef!, _: FWAMIDIDeviceNubRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437124-fwadisposefwaudiomididevicenub)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeFWAudioMIDIDeviceNub(_ inRef: FWARef, _ device: FWAMIDIDeviceNubRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeFWAudioMIDIDeviceNub(_ inRef: FWARef!, _ device: FWAMIDIDeviceNubRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeFWAudioMIDIPlug(_: FWARef!, _: FWAMIDIPlugRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436710-fwadisposefwaudiomidiplug)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeFWAudioMIDIPlug(_ inRef: FWARef, _ plugRef: FWAMIDIPlugRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeFWAudioMIDIPlug(_ inRef: FWARef!, _ plugRef: FWAMIDIPlugRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeFWAudioMIDIStream(_: FWARef!, _: FWAMIDIStreamRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437010-fwadisposefwaudiomidistream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeFWAudioMIDIStream(_ inRef: FWARef, _ streamRef: FWAMIDIStreamRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeFWAudioMIDIStream(_ inRef: FWARef!, _ streamRef: FWAMIDIStreamRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeFWAudioPlug(_: FWARef!, _: FWAAudioPlugRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437391-fwadisposefwaudioplug)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeFWAudioPlug(_ inRef: FWARef, _ plugRef: FWAAudioPlugRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeFWAudioPlug(_ inRef: FWARef!, _ plugRef: FWAAudioPlugRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeFWAudioStream(_: FWARef!, _: FWAAudioStreamRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436988-fwadisposefwaudiostream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeFWAudioStream(_ inRef: FWARef, _ streamRef: FWAAudioStreamRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeFWAudioStream(_ inRef: FWARef!, _ streamRef: FWAAudioStreamRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeIsochStream(_: FWARef!, _: FWAIsochStreamRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437419-fwadisposeisochstream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeIsochStream(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeIsochStream(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWADisposeMIDIStream(_: FWARef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437359-fwadisposemidistream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWADisposeMIDIStream(_ inRef: FWARef, _ midiStreamRef: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWADisposeMIDIStream(_ inRef: FWARef!, _ midiStreamRef: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAEngineRef](https://developer.apple.com/documentation/fwauserlib/fwaengineref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAEngineRef = COpaquePointer ``` |
| To | ``` typealias FWAEngineRef = OpaquePointer ``` |

Modified [FWAExecuteAVC(_: FWARef!, _: UnsafeMutablePointer<UInt8>!, _: UInt32, _: UnsafeMutablePointer<UInt8>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437482-fwaexecuteavc)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAExecuteAVC(_ inRef: FWARef, _ cmd: UnsafeMutablePointer<UInt8>, _ cmdSize: UInt32, _ response: UnsafeMutablePointer<UInt8>, _ responseSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAExecuteAVC(_ inRef: FWARef!, _ cmd: UnsafeMutablePointer<UInt8>!, _ cmdSize: UInt32, _ response: UnsafeMutablePointer<UInt8>!, _ responseSize: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetAEvntSource(_: FWARef!) -> CFRunLoopSource!](https://developer.apple.com/documentation/fwauserlib/1437339-fwagetaevntsource)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetAEvntSource(_ inRef: FWARef) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.10 | -- |
| To | ``` func FWAGetAEvntSource(_ inRef: FWARef!) -> CFRunLoopSource! ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetClockSource(_: FWARef!, _: UnsafeMutablePointer<FWAIsochStreamRef?>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437215-fwagetclocksource)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetClockSource(_ inRef: FWARef, _ streamRef: UnsafeMutablePointer<FWAIsochStreamRef>, _ sequence: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetClockSource(_ inRef: FWARef!, _ streamRef: UnsafeMutablePointer<FWAIsochStreamRef?>!, _ sequence: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetCurrentIsochStreamRefs(_: FWARef!, _: UnsafeMutablePointer<FWAIsochStreamRef?>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436686-fwagetcurrentisochstreamrefs)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetCurrentIsochStreamRefs(_ inRef: FWARef, _ isochStreamRef: UnsafeMutablePointer<FWAIsochStreamRef>, _ count: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetCurrentIsochStreamRefs(_ inRef: FWARef!, _ isochStreamRef: UnsafeMutablePointer<FWAIsochStreamRef?>!, _ count: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetCycleTimeOffset(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436992-fwagetcycletimeoffset)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetCycleTimeOffset(_ inRef: FWARef, _ cycleTimeOffset: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetCycleTimeOffset(_ inRef: FWARef!, _ cycleTimeOffset: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetDeviceName(_: FWARef!, _: UnsafeMutablePointer<Int8>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437524-fwagetdevicename)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetDeviceName(_ inRef: FWARef, _ name: UnsafeMutablePointer<Int8>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetDeviceName(_ inRef: FWARef!, _ name: UnsafeMutablePointer<Int8>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetDeviceSampleRate(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436704-fwagetdevicesamplerate)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetDeviceSampleRate(_ inRef: FWARef, _ rate: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetDeviceSampleRate(_ inRef: FWARef!, _ rate: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetDeviceSendMode(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436668-fwagetdevicesendmode)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetDeviceSendMode(_ inRef: FWARef, _ mode: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetDeviceSendMode(_ inRef: FWARef!, _ mode: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetDeviceStatus(_: FWARef!, _: UnsafeMutableRawPointer!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437169-fwagetdevicestatus)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetDeviceStatus(_ inRef: FWARef, _ outData: UnsafeMutablePointer<Void>, _ inSize: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetDeviceStatus(_ inRef: FWARef!, _ outData: UnsafeMutableRawPointer!, _ inSize: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetDeviceStreamInfo(_: FWARef!, _: UInt32, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436779-fwagetdevicestreaminfo)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetDeviceStreamInfo(_ inRef: FWARef, _ audioStreamRef: UInt32, _ numInput: UnsafeMutablePointer<UInt32>, _ inputIsochChan: UnsafeMutablePointer<UInt32>, _ numOutput: UnsafeMutablePointer<UInt32>, _ outputIsochChan: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetDeviceStreamInfo(_ inRef: FWARef!, _ audioStreamRef: UInt32, _ numInput: UnsafeMutablePointer<UInt32>!, _ inputIsochChan: UnsafeMutablePointer<UInt32>!, _ numOutput: UnsafeMutablePointer<UInt32>!, _ outputIsochChan: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetFWAudioMIDIPlugChannel(_: FWARef!, _: FWAMIDIPlugRef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436870-fwagetfwaudiomidiplugchannel)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetFWAudioMIDIPlugChannel(_ inRef: FWARef, _ streamRef: FWAMIDIPlugRef, _ channelID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetFWAudioMIDIPlugChannel(_ inRef: FWARef!, _ streamRef: FWAMIDIPlugRef!, _ channelID: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetFWAudioPlugChannel(_: FWARef!, _: FWAAudioPlugRef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436517-fwagetfwaudioplugchannel)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetFWAudioPlugChannel(_ inRef: FWARef, _ streamRef: FWAAudioPlugRef, _ channelID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetFWAudioPlugChannel(_ inRef: FWARef!, _ streamRef: FWAAudioPlugRef!, _ channelID: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetGUID(_: FWARef!, _: UnsafeMutablePointer<UInt64>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437154-fwagetguid)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetGUID(_ inRef: FWARef, _ guid: UnsafeMutablePointer<UInt64>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetGUID(_ inRef: FWARef!, _ guid: UnsafeMutablePointer<UInt64>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIndexedFWAudioMIDIPlug(_: FWARef!, _: FWAMIDIDeviceNubRef!, _: UInt32, _: UInt32, _: UnsafeMutablePointer<FWAMIDIPlugRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436557-fwagetindexedfwaudiomidiplug)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIndexedFWAudioMIDIPlug(_ inRef: FWARef, _ device: FWAMIDIDeviceNubRef, _ index: UInt32, _ dir: UInt32, _ plugRef: UnsafeMutablePointer<FWAMIDIPlugRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIndexedFWAudioMIDIPlug(_ inRef: FWARef!, _ device: FWAMIDIDeviceNubRef!, _ index: UInt32, _ dir: UInt32, _ plugRef: UnsafeMutablePointer<FWAMIDIPlugRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIndexedFWAudioPlug(_: FWARef!, _: FWADeviceRef!, _: UInt32, _: UInt32, _: UnsafeMutablePointer<FWAAudioPlugRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436656-fwagetindexedfwaudioplug)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIndexedFWAudioPlug(_ inRef: FWARef, _ device: FWADeviceRef, _ index: UInt32, _ dir: UInt32, _ plugRef: UnsafeMutablePointer<FWAAudioPlugRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIndexedFWAudioPlug(_ inRef: FWARef!, _ device: FWADeviceRef!, _ index: UInt32, _ dir: UInt32, _ plugRef: UnsafeMutablePointer<FWAAudioPlugRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIsochStreamAudioSequenceCount(_: FWARef!, _: FWAIsochStreamRef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437105-fwagetisochstreamaudiosequenceco)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIsochStreamAudioSequenceCount(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ numAudioSequence: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIsochStreamAudioSequenceCount(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ numAudioSequence: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIsochStreamAudioType(_: FWARef!, _: FWAIsochStreamRef!, _: UnsafeMutablePointer<FWAudioType>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437029-fwagetisochstreamaudiotype)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIsochStreamAudioType(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ type: UnsafeMutablePointer<FWAudioType>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIsochStreamAudioType(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ type: UnsafeMutablePointer<FWAudioType>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIsochStreamChannelID(_: FWARef!, _: FWAIsochStreamRef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437231-fwagetisochstreamchannelid)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIsochStreamChannelID(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ channelID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIsochStreamChannelID(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ channelID: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIsochStreamDirection(_: FWARef!, _: FWAIsochStreamRef!, _: UnsafeMutablePointer<FWAStreamDirection>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436577-fwagetisochstreamdirection)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIsochStreamDirection(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ direction: UnsafeMutablePointer<FWAStreamDirection>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIsochStreamDirection(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ direction: UnsafeMutablePointer<FWAStreamDirection>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIsochStreamMIDISequenceCount(_: FWARef!, _: FWAIsochStreamRef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437304-fwagetisochstreammidisequencecou)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIsochStreamMIDISequenceCount(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ numMIDISequence: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIsochStreamMIDISequenceCount(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ numMIDISequence: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIsochStreamOutputSpeed(_: FWARef!, _: FWAIsochStreamRef!, _: UnsafeMutablePointer<IOFWSpeed>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436858-fwagetisochstreamoutputspeed)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIsochStreamOutputSpeed(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ speed: UnsafeMutablePointer<IOFWSpeed>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIsochStreamOutputSpeed(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ speed: UnsafeMutablePointer<IOFWSpeed>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIsochStreamSampleRate(_: FWARef!, _: FWAIsochStreamRef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436561-fwagetisochstreamsamplerate)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIsochStreamSampleRate(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ rate: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIsochStreamSampleRate(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ rate: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetIsochStreamState(_: FWARef!, _: FWAIsochStreamRef!, _: UnsafeMutablePointer<FWAStreamState>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437180-fwagetisochstreamstate)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetIsochStreamState(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ state: UnsafeMutablePointer<FWAStreamState>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetIsochStreamState(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ state: UnsafeMutablePointer<FWAStreamState>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetMacGUID(_: FWARef!, _: UnsafeMutablePointer<UInt64>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437318-fwagetmacguid)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetMacGUID(_ inRef: FWARef, _ guid: UnsafeMutablePointer<UInt64>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetMacGUID(_ inRef: FWARef!, _ guid: UnsafeMutablePointer<UInt64>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetMaxIsochChannels(_: FWARef!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436688-fwagetmaxisochchannels)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetMaxIsochChannels(_ inRef: FWARef, _ inChannels: UnsafeMutablePointer<UInt32>, _ outChannels: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetMaxIsochChannels(_ inRef: FWARef!, _ inChannels: UnsafeMutablePointer<UInt32>!, _ outChannels: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetMaxSequences(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436684-fwagetmaxsequences)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetMaxSequences(_ inRef: FWARef, _ numSequences: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetMaxSequences(_ inRef: FWARef!, _ numSequences: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetMaxSpeed(_: FWARef!, _: UnsafeMutablePointer<IOFWSpeed>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436898-fwagetmaxspeed)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetMaxSpeed(_ inRef: FWARef, _ speed: UnsafeMutablePointer<IOFWSpeed>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetMaxSpeed(_ inRef: FWARef!, _ speed: UnsafeMutablePointer<IOFWSpeed>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetNodeID(_: FWARef!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437314-fwagetnodeid)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetNodeID(_ inRef: FWARef, _ outNodeID: UnsafeMutablePointer<UInt32>, _ outGeneration: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetNodeID(_ inRef: FWARef!, _ outNodeID: UnsafeMutablePointer<UInt32>!, _ outGeneration: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetNumAudioInputPlugs(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437387-fwagetnumaudioinputplugs)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetNumAudioInputPlugs(_ inRef: FWARef, _ plugs: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetNumAudioInputPlugs(_ inRef: FWARef!, _ plugs: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetNumAudioOutputPlugs(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436494-fwagetnumaudiooutputplugs)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetNumAudioOutputPlugs(_ inRef: FWARef, _ plugs: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetNumAudioOutputPlugs(_ inRef: FWARef!, _ plugs: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetNumMIDIInputPlugs(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436531-fwagetnummidiinputplugs)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetNumMIDIInputPlugs(_ inRef: FWARef, _ plugs: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetNumMIDIInputPlugs(_ inRef: FWARef!, _ plugs: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetNumMIDIOutputPlugs(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436513-fwagetnummidioutputplugs)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetNumMIDIOutputPlugs(_ inRef: FWARef, _ plugs: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetNumMIDIOutputPlugs(_ inRef: FWARef!, _ plugs: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetProperty(_: FWARef!, _: UInt32, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436908-fwagetproperty)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetProperty(_ inRef: FWARef, _ propertyID: UInt32, _ data: UnsafeMutablePointer<Void>, _ size: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetProperty(_ inRef: FWARef!, _ propertyID: UInt32, _ data: UnsafeMutableRawPointer!, _ size: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetSessionRef(_: FWARef!, _: UnsafeMutablePointer<IOFireWireSessionRef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436882-fwagetsessionref)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetSessionRef(_ inRef: FWARef, _ sessionRef: UnsafeMutablePointer<IOFireWireSessionRef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetSessionRef(_ inRef: FWARef!, _ sessionRef: UnsafeMutablePointer<IOFireWireSessionRef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetSupportedAudioTypes(_: FWARef!, _: UnsafeMutablePointer<FWAudioType>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436945-fwagetsupportedaudiotypes)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetSupportedAudioTypes(_ inRef: FWARef, _ audioTypes: UnsafeMutablePointer<FWAudioType>, _ count: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetSupportedAudioTypes(_ inRef: FWARef!, _ audioTypes: UnsafeMutablePointer<FWAudioType>!, _ count: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetSupportedSampleRates(_: FWARef!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437411-fwagetsupportedsamplerates)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetSupportedSampleRates(_ inRef: FWARef, _ sampleRates: UnsafeMutablePointer<UInt32>, _ count: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetSupportedSampleRates(_ inRef: FWARef!, _ sampleRates: UnsafeMutablePointer<UInt32>!, _ count: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetVendorID(_: FWARef!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437325-fwagetvendorid)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetVendorID(_ inRef: FWARef, _ vendorID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetVendorID(_ inRef: FWARef!, _ vendorID: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAGetVendorName(_: FWARef!, _: UnsafeMutablePointer<Int8>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436772-fwagetvendorname)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAGetVendorName(_ inRef: FWARef, _ name: UnsafeMutablePointer<Int8>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAGetVendorName(_ inRef: FWARef!, _ name: UnsafeMutablePointer<Int8>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAInitAEvntSource(_: FWARef!, _: UnsafeMutablePointer<Unmanaged<CFRunLoopSource>?>!, _: UnsafeMutableRawPointer!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436587-fwainitaevntsource)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAInitAEvntSource(_ inRef: FWARef, _ source: UnsafeMutablePointer<Unmanaged<CFRunLoopSource>?>, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAInitAEvntSource(_ inRef: FWARef!, _ source: UnsafeMutablePointer<Unmanaged<CFRunLoopSource>?>!, _ refcon: UnsafeMutableRawPointer!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAIsMIDICapable(_: FWARef!, _: UnsafeMutablePointer<Bool>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437225-fwaismidicapable)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAIsMIDICapable(_ inRef: FWARef, _ supportsMIDI: UnsafeMutablePointer<Bool>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAIsMIDICapable(_ inRef: FWARef!, _ supportsMIDI: UnsafeMutablePointer<Bool>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAIsochStreamRef](https://developer.apple.com/documentation/fwauserlib/fwaisochstreamref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAIsochStreamRef = COpaquePointer ``` |
| To | ``` typealias FWAIsochStreamRef = OpaquePointer ``` |

Modified [FWAMIDIDeviceNubAttachMIDIPlug(_: FWARef!, _: FWAMIDIDeviceNubRef!, _: FWAMIDIPlugRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436791-fwamididevicenubattachmidiplug)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAMIDIDeviceNubAttachMIDIPlug(_ inRef: FWARef, _ midiDeviceNub: FWAMIDIDeviceNubRef, _ midiPlug: FWAMIDIPlugRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAMIDIDeviceNubAttachMIDIPlug(_ inRef: FWARef!, _ midiDeviceNub: FWAMIDIDeviceNubRef!, _ midiPlug: FWAMIDIPlugRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAMIDIDeviceNubDetachMIDIPlug(_: FWARef!, _: FWAMIDIPlugRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437191-fwamididevicenubdetachmidiplug)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAMIDIDeviceNubDetachMIDIPlug(_ inRef: FWARef, _ midiPlug: FWAMIDIPlugRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAMIDIDeviceNubDetachMIDIPlug(_ inRef: FWARef!, _ midiPlug: FWAMIDIPlugRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAMIDIDeviceNubRef](https://developer.apple.com/documentation/fwauserlib/fwamididevicenubref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAMIDIDeviceNubRef = COpaquePointer ``` |
| To | ``` typealias FWAMIDIDeviceNubRef = OpaquePointer ``` |

Modified [FWAMIDIPlugRef](https://developer.apple.com/documentation/fwauserlib/fwamidiplugref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAMIDIPlugRef = COpaquePointer ``` |
| To | ``` typealias FWAMIDIPlugRef = OpaquePointer ``` |

Modified [FWAMIDIStreamRef](https://developer.apple.com/documentation/fwauserlib/fwamidistreamref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAMIDIStreamRef = COpaquePointer ``` |
| To | ``` typealias FWAMIDIStreamRef = OpaquePointer ``` |

Modified [FWAOpen(_: UInt32, _: UnsafeMutablePointer<FWARef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436947-fwaopen)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAOpen(_ nodeID: UInt32, _ outRef: UnsafeMutablePointer<FWARef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAOpen(_ nodeID: UInt32, _ outRef: UnsafeMutablePointer<FWARef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAOpenLocal(_: UnsafeMutablePointer<FWARef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437455-fwaopenlocal)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAOpenLocal(_ outRef: UnsafeMutablePointer<FWARef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAOpenLocal(_ outRef: UnsafeMutablePointer<FWARef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAOpenLocalWithInterface(_: UInt64, _: UInt32, _: UnsafeMutablePointer<FWARef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436823-fwaopenlocalwithinterface)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAOpenLocalWithInterface(_ guid: UInt64, _ options: UInt32, _ outRef: UnsafeMutablePointer<FWARef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAOpenLocalWithInterface(_ guid: UInt64, _ options: UInt32, _ outRef: UnsafeMutablePointer<FWARef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAOpenWithService(_: io_service_t, _: UInt32, _: UnsafeMutablePointer<FWARef?>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436842-fwaopenwithservice)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAOpenWithService(_ _: io_service_t, _ options: UInt32, _ outRef: UnsafeMutablePointer<FWARef>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAOpenWithService(_ _: io_service_t, _ options: UInt32, _ outRef: UnsafeMutablePointer<FWARef?>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWARead(_: FWARef!, _: UInt8, _: UInt8, _: Int, _: UnsafeMutableRawPointer!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436949-fwaread)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWARead(_ inRef: FWARef, _ inAddress: UInt8, _ inSubAddress: UInt8, _ inDataSize: Int, _ inDataPtr: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWARead(_ inRef: FWARef!, _ inAddress: UInt8, _ inSubAddress: UInt8, _ inDataSize: Int, _ inDataPtr: UnsafeMutableRawPointer!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAReadBlock(_: FWARef!, _: FWAddressPtr!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt8>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437264-fwareadblock)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAReadBlock(_ inRef: FWARef, _ address: FWAddressPtr, _ size: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UInt8>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAReadBlock(_ inRef: FWARef!, _ address: FWAddressPtr!, _ size: UnsafeMutablePointer<UInt32>!, _ outData: UnsafeMutablePointer<UInt8>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAReadMIDIData(_: FWARef!, _: UInt32, _: UnsafeMutablePointer<FWAMIDIReadBuf>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437110-fwareadmididata)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAReadMIDIData(_ inRef: FWARef, _ midiStreamRef: UInt32, _ buf: UnsafeMutablePointer<FWAMIDIReadBuf>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAReadMIDIData(_ inRef: FWARef!, _ midiStreamRef: UInt32, _ buf: UnsafeMutablePointer<FWAMIDIReadBuf>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAReadMIDIDataAsync(_: FWARef!, _: UInt32, _: UInt32, _: IOKit.IOAsyncCallback2!, _: UnsafeMutableRawPointer!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436832-fwareadmididataasync)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAReadMIDIDataAsync(_ inRef: FWARef, _ midiStreamRef: UInt32, _ readBufSize: UInt32, _ callback: IOAsyncCallback2!, _ refCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAReadMIDIDataAsync(_ inRef: FWARef!, _ midiStreamRef: UInt32, _ readBufSize: UInt32, _ callback: IOKit.IOAsyncCallback2!, _ refCon: UnsafeMutableRawPointer!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAReadQuadlet(_: FWARef!, _: FWAddressPtr!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437161-fwareadquadlet)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAReadQuadlet(_ inRef: FWARef, _ address: FWAddressPtr, _ outData: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAReadQuadlet(_ inRef: FWARef!, _ address: FWAddressPtr!, _ outData: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWARef](https://developer.apple.com/documentation/fwauserlib/fwaref)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWARef = COpaquePointer ``` |
| To | ``` typealias FWARef = OpaquePointer ``` |

Modified [FWAReserveIsochSequences(_: FWARef!, _: FWAIsochStreamRef!, _: FWAudioType, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437512-fwareserveisochsequences)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAReserveIsochSequences(_ inRef: FWARef, _ isochStream: FWAIsochStreamRef, _ type: FWAudioType, _ count: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAReserveIsochSequences(_ inRef: FWARef!, _ isochStream: FWAIsochStreamRef!, _ type: FWAudioType, _ count: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetAutoLoad(_: FWARef!, _: Bool) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436616-fwasetautoload)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetAutoLoad(_ inRef: FWARef, _ enable: Bool) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetAutoLoad(_ inRef: FWARef!, _ enable: Bool) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetClockSource(_: FWARef!, _: FWAIsochStreamRef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436974-fwasetclocksource)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetClockSource(_ inRef: FWARef, _ streamRef: FWAIsochStreamRef, _ sequence: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetClockSource(_ inRef: FWARef!, _ streamRef: FWAIsochStreamRef!, _ sequence: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetCycleTimeOffset(_: FWARef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437165-fwasetcycletimeoffset)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetCycleTimeOffset(_ inRef: FWARef, _ cycleTimeOffset: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetCycleTimeOffset(_ inRef: FWARef!, _ cycleTimeOffset: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetDeviceStreamInfo(_: FWARef!, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: UInt32, _: Bool) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436951-fwasetdevicestreaminfo)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetDeviceStreamInfo(_ inRef: FWARef, _ audioStreamRef: UInt32, _ numInput: UInt32, _ inputIsochChan: UInt32, _ numOutput: UInt32, _ outputIsochChan: UInt32, _ update: Bool) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetDeviceStreamInfo(_ inRef: FWARef!, _ audioStreamRef: UInt32, _ numInput: UInt32, _ inputIsochChan: UInt32, _ numOutput: UInt32, _ outputIsochChan: UInt32, _ update: Bool) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetFWAudioMIDIPlugChannel(_: FWARef!, _: FWAMIDIPlugRef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436943-fwasetfwaudiomidiplugchannel)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetFWAudioMIDIPlugChannel(_ inRef: FWARef, _ streamRef: FWAMIDIPlugRef, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetFWAudioMIDIPlugChannel(_ inRef: FWARef!, _ streamRef: FWAMIDIPlugRef!, _ channelID: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetFWAudioMIDIPlugProperty(_: FWARef!, _: FWAMIDIPlugRef!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436734-fwasetfwaudiomidiplugproperty)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetFWAudioMIDIPlugProperty(_ inRef: FWARef, _ plugRef: FWAMIDIPlugRef, _ keyname: UnsafePointer<Int8>, _ keyvalue: UnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetFWAudioMIDIPlugProperty(_ inRef: FWARef!, _ plugRef: FWAMIDIPlugRef!, _ keyname: UnsafePointer<Int8>!, _ keyvalue: UnsafePointer<Int8>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetFWAudioPlugChannel(_: FWARef!, _: FWAAudioPlugRef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437308-fwasetfwaudioplugchannel)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetFWAudioPlugChannel(_ inRef: FWARef, _ streamRef: FWAAudioPlugRef, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetFWAudioPlugChannel(_ inRef: FWARef!, _ streamRef: FWAAudioPlugRef!, _ channelID: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetFWAudioPlugProperty(_: FWARef!, _: FWAAudioPlugRef!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437056-fwasetfwaudioplugproperty)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetFWAudioPlugProperty(_ inRef: FWARef, _ plugRef: FWAAudioPlugRef, _ keyname: UnsafePointer<Int8>, _ keyvalue: UnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetFWAudioPlugProperty(_ inRef: FWARef!, _ plugRef: FWAAudioPlugRef!, _ keyname: UnsafePointer<Int8>!, _ keyvalue: UnsafePointer<Int8>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetIsochStreamAudioSequenceCount(_: FWARef!, _: FWAIsochStreamRef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437496-fwasetisochstreamaudiosequenceco)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetIsochStreamAudioSequenceCount(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ numAudioSequence: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetIsochStreamAudioSequenceCount(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ numAudioSequence: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetIsochStreamAudioType(_: FWARef!, _: FWAIsochStreamRef!, _: FWAudioType) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436545-fwasetisochstreamaudiotype)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetIsochStreamAudioType(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ type: FWAudioType) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetIsochStreamAudioType(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ type: FWAudioType) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetIsochStreamChannelID(_: FWARef!, _: FWAIsochStreamRef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437246-fwasetisochstreamchannelid)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetIsochStreamChannelID(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ channelID: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetIsochStreamChannelID(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ channelID: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetIsochStreamMIDISequenceCount(_: FWARef!, _: FWAIsochStreamRef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436742-fwasetisochstreammidisequencecou)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetIsochStreamMIDISequenceCount(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ numMIDISequence: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetIsochStreamMIDISequenceCount(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ numMIDISequence: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetIsochStreamOutputSpeed(_: FWARef!, _: FWAIsochStreamRef!, _: IOFWSpeed) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436581-fwasetisochstreamoutputspeed)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetIsochStreamOutputSpeed(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ speed: IOFWSpeed) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetIsochStreamOutputSpeed(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ speed: IOFWSpeed) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetIsochStreamSampleRate(_: FWARef!, _: FWAIsochStreamRef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437171-fwasetisochstreamsamplerate)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetIsochStreamSampleRate(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef, _ rate: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetIsochStreamSampleRate(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!, _ rate: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetNumMIDIInputPlugs(_: FWARef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437417-fwasetnummidiinputplugs)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetNumMIDIInputPlugs(_ inRef: FWARef, _ plugs: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetNumMIDIInputPlugs(_ inRef: FWARef!, _ plugs: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetNumMIDIOutputPlugs(_: FWARef!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436632-fwasetnummidioutputplugs)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetNumMIDIOutputPlugs(_ inRef: FWARef, _ plugs: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetNumMIDIOutputPlugs(_ inRef: FWARef!, _ plugs: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetPluginPath(_: FWARef!, _: FWAEngineRef!, _: UInt32, _: UInt32, _: UnsafePointer<Int8>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436914-fwasetpluginpath)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetPluginPath(_ inRef: FWARef, _ engine: FWAEngineRef, _ vendorID: UInt32, _ modelID: UInt32, _ pluginPath: UnsafePointer<Int8>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetPluginPath(_ inRef: FWARef!, _ engine: FWAEngineRef!, _ vendorID: UInt32, _ modelID: UInt32, _ pluginPath: UnsafePointer<Int8>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWASetProperty(_: FWARef!, _: UInt32, _: UnsafeMutableRawPointer!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436732-fwasetproperty)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASetProperty(_ inRef: FWARef, _ propertyID: UInt32, _ data: UnsafeMutablePointer<Void>, _ size: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASetProperty(_ inRef: FWARef!, _ propertyID: UInt32, _ data: UnsafeMutableRawPointer!, _ size: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAStartFWAudioDevice(_: FWARef!, _: FWADeviceRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437095-fwastartfwaudiodevice)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAStartFWAudioDevice(_ inRef: FWARef, _ device: FWADeviceRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAStartFWAudioDevice(_ inRef: FWARef!, _ device: FWADeviceRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAStartIsochStream(_: FWARef!, _: FWAIsochStreamRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436519-fwastartisochstream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAStartIsochStream(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAStartIsochStream(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAStopFWAudioDevice(_: FWARef!, _: FWADeviceRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437557-fwastopfwaudiodevice)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAStopFWAudioDevice(_ inRef: FWARef, _ device: FWADeviceRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAStopFWAudioDevice(_ inRef: FWARef!, _ device: FWADeviceRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAStopIsochStream(_: FWARef!, _: FWAIsochStreamRef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436529-fwastopisochstream)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAStopIsochStream(_ inRef: FWARef, _ isochStreamRef: FWAIsochStreamRef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAStopIsochStream(_ inRef: FWARef!, _ isochStreamRef: FWAIsochStreamRef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAStreamNotificationProc](https://developer.apple.com/documentation/fwauserlib/fwastreamnotificationproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias FWAStreamNotificationProc = (UInt32, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias FWAStreamNotificationProc = (UInt32, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [FWASyncUpDevice(_: FWARef!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436515-fwasyncupdevice)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWASyncUpDevice(_ inRef: FWARef) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWASyncUpDevice(_ inRef: FWARef!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAWrite(_: FWARef!, _: UInt8, _: UInt8, _: Int, _: UnsafeRawPointer!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437097-fwawrite)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAWrite(_ inRef: FWARef, _ inAddress: UInt8, _ inSubAddress: UInt8, _ inDataSize: Int, _ inDataPtr: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAWrite(_ inRef: FWARef!, _ inAddress: UInt8, _ inSubAddress: UInt8, _ inDataSize: Int, _ inDataPtr: UnsafeRawPointer!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAWriteBlock(_: FWARef!, _: FWAddressPtr!, _: UInt32, _: UnsafePointer<UInt8>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437310-fwawriteblock)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAWriteBlock(_ inRef: FWARef, _ address: FWAddressPtr, _ size: UInt32, _ data: UnsafePointer<UInt8>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAWriteBlock(_ inRef: FWARef!, _ address: FWAddressPtr!, _ size: UInt32, _ data: UnsafePointer<UInt8>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAWriteMIDIData(_: FWARef!, _: UInt32, _: UInt32, _: UnsafeMutablePointer<UInt8>!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437327-fwawritemididata)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAWriteMIDIData(_ inRef: FWARef, _ midiStreamRef: UInt32, _ writeMsgLength: UInt32, _ buf: UnsafeMutablePointer<UInt8>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAWriteMIDIData(_ inRef: FWARef!, _ midiStreamRef: UInt32, _ writeMsgLength: UInt32, _ buf: UnsafeMutablePointer<UInt8>!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAWriteMIDIDataAsync(_: FWARef!, _: UInt32, _: UInt32, _: IOKit.IOAsyncCallback1!, _: UnsafeMutableRawPointer!) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1437329-fwawritemididataasync)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAWriteMIDIDataAsync(_ inRef: FWARef, _ midiStreamRef: UInt32, _ writeMsgLength: UInt32, _ callback: IOAsyncCallback1!, _ refCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAWriteMIDIDataAsync(_ inRef: FWARef!, _ midiStreamRef: UInt32, _ writeMsgLength: UInt32, _ callback: IOKit.IOAsyncCallback1!, _ refCon: UnsafeMutableRawPointer!) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

Modified [FWAWriteQuadlet(_: FWARef!, _: FWAddressPtr!, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/fwauserlib/1436930-fwawritequadlet)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func FWAWriteQuadlet(_ inRef: FWARef, _ address: FWAddressPtr, _ data: UInt32) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func FWAWriteQuadlet(_ inRef: FWARef!, _ address: FWAddressPtr!, _ data: UInt32) -> OSStatus ``` | OS X 10.4 | OS X 10.12 |

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
