---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/CoreMIDI.html
archived_at: '2026-07-18T02:51:45.269533Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# CoreMIDI Changes for Swift

### CoreMIDI

Modified [MIDIDriverInterface [struct]](https://developer.apple.com/documentation/coremidi/mididriverinterface)

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var FindDevices: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!     var Start: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!     var Stop: ((MIDIDriverRef?) -> OSStatus)!     var Configure: ((MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!     var Send: ((MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!     var EnableSource: ((MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!     var Flush: ((MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!     var Monitor: ((MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, FindDevices FindDevices: (@escaping (MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Start Start: (@escaping (MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Stop Stop: (@escaping (MIDIDriverRef?) -> OSStatus)!, Configure Configure: (@escaping (MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!, Send Send: (@escaping (MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, EnableSource EnableSource: (@escaping (MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush Flush: (@escaping (MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, Monitor Monitor: (@escaping (MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!) } ``` |
| To | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var FindDevices: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!     var Start: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!     var Stop: ((MIDIDriverRef?) -> OSStatus)!     var Configure: ((MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!     var Send: ((MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!     var EnableSource: ((MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!     var Flush: ((MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!     var Monitor: ((MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, FindDevices FindDevices: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Start Start: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Stop Stop: ((MIDIDriverRef?) -> OSStatus)!, Configure Configure: ((MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!, Send Send: ((MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, EnableSource EnableSource: ((MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush Flush: ((MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, Monitor Monitor: ((MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!) } ``` |

Modified MIDIDriverInterface.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, FindDevices: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Start: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Stop: ((MIDIDriverRef?) -> OSStatus)!, Configure: ((MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!, Send: ((MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, EnableSource: ((MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush: ((MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, Monitor: ((MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!)

|  | Declaration |
| --- | --- |
| From | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, FindDevices FindDevices: (@escaping (MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Start Start: (@escaping (MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Stop Stop: (@escaping (MIDIDriverRef?) -> OSStatus)!, Configure Configure: (@escaping (MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!, Send Send: (@escaping (MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, EnableSource EnableSource: (@escaping (MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush Flush: (@escaping (MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, Monitor Monitor: (@escaping (MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!) ``` |
| To | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release Release: ((UnsafeMutableRawPointer?) -> ULONG)!, FindDevices FindDevices: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Start Start: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Stop Stop: ((MIDIDriverRef?) -> OSStatus)!, Configure Configure: ((MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!, Send Send: ((MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, EnableSource EnableSource: ((MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush Flush: ((MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, Monitor Monitor: ((MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!) ``` |

Modified [MIDIDestinationCreate(_: MIDIClientRef, _: CFString, _: CoreMIDI.MIDIReadProc, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495347-mididestinationcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString, _ readProc: CoreMIDI.MIDIReadProc, _ refCon: UnsafeMutableRawPointer?, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |
| To | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString, _ readProc: @escaping CoreMIDI.MIDIReadProc, _ refCon: UnsafeMutableRawPointer?, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |

Modified [MIDIDestinationCreateWithBlock(_: MIDIClientRef, _: CFString, _: UnsafeMutablePointer<MIDIEndpointRef>, _: CoreMIDI.MIDIReadBlock) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495247-mididestinationcreatewithblock)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDestinationCreateWithBlock(_ client: MIDIClientRef, _ name: CFString, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>, _ readBlock: CoreMIDI.MIDIReadBlock) -> OSStatus ``` |
| To | ``` func MIDIDestinationCreateWithBlock(_ client: MIDIClientRef, _ name: CFString, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>, _ readBlock: @escaping CoreMIDI.MIDIReadBlock) -> OSStatus ``` |

Modified [MIDIInputPortCreate(_: MIDIClientRef, _: CFString, _: CoreMIDI.MIDIReadProc, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495225-midiinputportcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString, _ readProc: CoreMIDI.MIDIReadProc, _ refCon: UnsafeMutableRawPointer?, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |
| To | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString, _ readProc: @escaping CoreMIDI.MIDIReadProc, _ refCon: UnsafeMutableRawPointer?, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |

Modified [MIDIInputPortCreateWithBlock(_: MIDIClientRef, _: CFString, _: UnsafeMutablePointer<MIDIPortRef>, _: CoreMIDI.MIDIReadBlock) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495333-midiinputportcreatewithblock)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIInputPortCreateWithBlock(_ client: MIDIClientRef, _ portName: CFString, _ outPort: UnsafeMutablePointer<MIDIPortRef>, _ readBlock: CoreMIDI.MIDIReadBlock) -> OSStatus ``` |
| To | ``` func MIDIInputPortCreateWithBlock(_ client: MIDIClientRef, _ portName: CFString, _ outPort: UnsafeMutablePointer<MIDIPortRef>, _ readBlock: @escaping CoreMIDI.MIDIReadBlock) -> OSStatus ``` |

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
