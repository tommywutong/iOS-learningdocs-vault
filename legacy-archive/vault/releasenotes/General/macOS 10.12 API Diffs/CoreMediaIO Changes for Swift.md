---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/CoreMediaIO.html
archived_at: '2026-07-18T02:51:10.106591Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CoreMediaIO Changes for Swift

### CoreMediaIO

Removed CMIODeviceAVCCommand.init(mCommand: UnsafeMutablePointer<UInt8>, mCommandLength: UInt32, mResponse: UnsafeMutablePointer<UInt8>, mResponseLength: UInt32, mResponseUsed: UInt32)Removed CMIODeviceRS422Command.init(mCommand: UnsafeMutablePointer<UInt8>, mCommandLength: UInt32, mResponse: UnsafeMutablePointer<UInt8>, mResponseLength: UInt32, mResponseUsed: UInt32)Removed CMIODeviceSMPTETimeCallback.init(mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc!, mRefCon: UnsafeMutablePointer<Void>)Removed CMIOStreamScheduledOutputNotificationProcAndRefCon.init(scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc!, scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>)Added CMIODeviceAVCCommand.init(mCommand: UnsafeMutablePointer<UInt8>!, mCommandLength: UInt32, mResponse: UnsafeMutablePointer<UInt8>!, mResponseLength: UInt32, mResponseUsed: UInt32)Added CMIODeviceRS422Command.init(mCommand: UnsafeMutablePointer<UInt8>!, mCommandLength: UInt32, mResponse: UnsafeMutablePointer<UInt8>!, mResponseLength: UInt32, mResponseUsed: UInt32)Added CMIODeviceSMPTETimeCallback.init(mGetSMPTETimeProc: CoreMediaIO.CMIODeviceGetSMPTETimeProc!, mRefCon: UnsafeMutableRawPointer!)Added CMIOStreamScheduledOutputNotificationProcAndRefCon.init(scheduledOutputNotificationProc: CoreMediaIO.CMIOStreamScheduledOutputNotificationProc!, scheduledOutputNotificationRefCon: UnsafeMutableRawPointer!)Modified CMIODeviceAVCCommand [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIODeviceAVCCommand {     var mCommand: UnsafeMutablePointer<UInt8>     var mCommandLength: UInt32     var mResponse: UnsafeMutablePointer<UInt8>     var mResponseLength: UInt32     var mResponseUsed: UInt32     init()     init(mCommand mCommand: UnsafeMutablePointer<UInt8>, mCommandLength mCommandLength: UInt32, mResponse mResponse: UnsafeMutablePointer<UInt8>, mResponseLength mResponseLength: UInt32, mResponseUsed mResponseUsed: UInt32) } ``` |
| To | ``` struct CMIODeviceAVCCommand {     var mCommand: UnsafeMutablePointer<UInt8>!     var mCommandLength: UInt32     var mResponse: UnsafeMutablePointer<UInt8>!     var mResponseLength: UInt32     var mResponseUsed: UInt32     init()     init(mCommand mCommand: UnsafeMutablePointer<UInt8>!, mCommandLength mCommandLength: UInt32, mResponse mResponse: UnsafeMutablePointer<UInt8>!, mResponseLength mResponseLength: UInt32, mResponseUsed mResponseUsed: UInt32) } ``` |

Modified CMIODeviceAVCCommand.mCommand

|  | Declaration |
| --- | --- |
| From | ``` var mCommand: UnsafeMutablePointer<UInt8> ``` |
| To | ``` var mCommand: UnsafeMutablePointer<UInt8>! ``` |

Modified CMIODeviceAVCCommand.mResponse

|  | Declaration |
| --- | --- |
| From | ``` var mResponse: UnsafeMutablePointer<UInt8> ``` |
| To | ``` var mResponse: UnsafeMutablePointer<UInt8>! ``` |

Modified CMIODeviceRS422Command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIODeviceRS422Command {     var mCommand: UnsafeMutablePointer<UInt8>     var mCommandLength: UInt32     var mResponse: UnsafeMutablePointer<UInt8>     var mResponseLength: UInt32     var mResponseUsed: UInt32     init()     init(mCommand mCommand: UnsafeMutablePointer<UInt8>, mCommandLength mCommandLength: UInt32, mResponse mResponse: UnsafeMutablePointer<UInt8>, mResponseLength mResponseLength: UInt32, mResponseUsed mResponseUsed: UInt32) } ``` |
| To | ``` struct CMIODeviceRS422Command {     var mCommand: UnsafeMutablePointer<UInt8>!     var mCommandLength: UInt32     var mResponse: UnsafeMutablePointer<UInt8>!     var mResponseLength: UInt32     var mResponseUsed: UInt32     init()     init(mCommand mCommand: UnsafeMutablePointer<UInt8>!, mCommandLength mCommandLength: UInt32, mResponse mResponse: UnsafeMutablePointer<UInt8>!, mResponseLength mResponseLength: UInt32, mResponseUsed mResponseUsed: UInt32) } ``` |

Modified CMIODeviceRS422Command.mCommand

|  | Declaration |
| --- | --- |
| From | ``` var mCommand: UnsafeMutablePointer<UInt8> ``` |
| To | ``` var mCommand: UnsafeMutablePointer<UInt8>! ``` |

Modified CMIODeviceRS422Command.mResponse

|  | Declaration |
| --- | --- |
| From | ``` var mResponse: UnsafeMutablePointer<UInt8> ``` |
| To | ``` var mResponse: UnsafeMutablePointer<UInt8>! ``` |

Modified CMIODeviceSMPTETimeCallback [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIODeviceSMPTETimeCallback {     var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc!     var mRefCon: UnsafeMutablePointer<Void>     init()     init(mGetSMPTETimeProc mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc!, mRefCon mRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CMIODeviceSMPTETimeCallback {     var mGetSMPTETimeProc: CoreMediaIO.CMIODeviceGetSMPTETimeProc!     var mRefCon: UnsafeMutableRawPointer!     init()     init(mGetSMPTETimeProc mGetSMPTETimeProc: CoreMediaIO.CMIODeviceGetSMPTETimeProc!, mRefCon mRefCon: UnsafeMutableRawPointer!) } ``` |

Modified CMIODeviceSMPTETimeCallback.mGetSMPTETimeProc

|  | Declaration |
| --- | --- |
| From | ``` var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc! ``` |
| To | ``` var mGetSMPTETimeProc: CoreMediaIO.CMIODeviceGetSMPTETimeProc! ``` |

Modified CMIODeviceSMPTETimeCallback.mRefCon

|  | Declaration |
| --- | --- |
| From | ``` var mRefCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var mRefCon: UnsafeMutableRawPointer! ``` |

Modified CMIOStreamScheduledOutputNotificationProcAndRefCon [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIOStreamScheduledOutputNotificationProcAndRefCon {     var scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc!     var scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>     init()     init(scheduledOutputNotificationProc scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc!, scheduledOutputNotificationRefCon scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CMIOStreamScheduledOutputNotificationProcAndRefCon {     var scheduledOutputNotificationProc: CoreMediaIO.CMIOStreamScheduledOutputNotificationProc!     var scheduledOutputNotificationRefCon: UnsafeMutableRawPointer!     init()     init(scheduledOutputNotificationProc scheduledOutputNotificationProc: CoreMediaIO.CMIOStreamScheduledOutputNotificationProc!, scheduledOutputNotificationRefCon scheduledOutputNotificationRefCon: UnsafeMutableRawPointer!) } ``` |

Modified CMIOStreamScheduledOutputNotificationProcAndRefCon.scheduledOutputNotificationProc

|  | Declaration |
| --- | --- |
| From | ``` var scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc! ``` |
| To | ``` var scheduledOutputNotificationProc: CoreMediaIO.CMIOStreamScheduledOutputNotificationProc! ``` |

Modified CMIOStreamScheduledOutputNotificationProcAndRefCon.scheduledOutputNotificationRefCon

|  | Declaration |
| --- | --- |
| From | ``` var scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var scheduledOutputNotificationRefCon: UnsafeMutableRawPointer! ``` |

Modified CMIODeviceGetSMPTETimeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIODeviceGetSMPTETimeProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` typealias CMIODeviceGetSMPTETimeProc = (UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt64>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<UInt32>?) -> OSStatus ``` |

Modified CMIODeviceProcessAVCCommand(_: CMIODeviceID, _: UnsafeMutablePointer<CMIODeviceAVCCommand>!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIODeviceProcessAVCCommand(_ deviceID: CMIODeviceID, _ ioAVCCommand: UnsafeMutablePointer<CMIODeviceAVCCommand>) -> OSStatus ``` |
| To | ``` func CMIODeviceProcessAVCCommand(_ deviceID: CMIODeviceID, _ ioAVCCommand: UnsafeMutablePointer<CMIODeviceAVCCommand>!) -> OSStatus ``` |

Modified CMIODeviceProcessRS422Command(_: CMIODeviceID, _: UnsafeMutablePointer<CMIODeviceRS422Command>!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIODeviceProcessRS422Command(_ deviceID: CMIODeviceID, _ ioRS422Command: UnsafeMutablePointer<CMIODeviceRS422Command>) -> OSStatus ``` |
| To | ``` func CMIODeviceProcessRS422Command(_ deviceID: CMIODeviceID, _ ioRS422Command: UnsafeMutablePointer<CMIODeviceRS422Command>!) -> OSStatus ``` |

Modified CMIODeviceStreamQueueAlteredProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIODeviceStreamQueueAlteredProc = (CMIOStreamID, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CMIODeviceStreamQueueAlteredProc = (CMIOStreamID, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified CMIOObjectAddPropertyListener(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!, _: CoreMediaIO.CMIOObjectPropertyListenerProc!, _: UnsafeMutableRawPointer!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectAddPropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc!, _ clientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMIOObjectAddPropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ listener: CoreMediaIO.CMIOObjectPropertyListenerProc!, _ clientData: UnsafeMutableRawPointer!) -> OSStatus ``` |

Modified CMIOObjectAddPropertyListenerBlock(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!, _: DispatchQueue!, _: CoreMediaIO.CMIOObjectPropertyListenerBlock!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectAddPropertyListenerBlock(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ dispatchQueue: dispatch_queue_t!, _ listener: CMIOObjectPropertyListenerBlock!) -> OSStatus ``` |
| To | ``` func CMIOObjectAddPropertyListenerBlock(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ dispatchQueue: DispatchQueue!, _ listener: CoreMediaIO.CMIOObjectPropertyListenerBlock!) -> OSStatus ``` |

Modified CMIOObjectGetPropertyData(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!, _: UInt32, _: UnsafeRawPointer!, _: UInt32, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutableRawPointer!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectGetPropertyData(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: UnsafePointer<Void>, _ dataSize: UInt32, _ dataUsed: UnsafeMutablePointer<UInt32>, _ data: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMIOObjectGetPropertyData(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ qualifierDataSize: UInt32, _ qualifierData: UnsafeRawPointer!, _ dataSize: UInt32, _ dataUsed: UnsafeMutablePointer<UInt32>!, _ data: UnsafeMutableRawPointer!) -> OSStatus ``` |

Modified CMIOObjectGetPropertyDataSize(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!, _: UInt32, _: UnsafeRawPointer!, _: UnsafeMutablePointer<UInt32>!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectGetPropertyDataSize(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: UnsafePointer<Void>, _ dataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func CMIOObjectGetPropertyDataSize(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ qualifierDataSize: UInt32, _ qualifierData: UnsafeRawPointer!, _ dataSize: UnsafeMutablePointer<UInt32>!) -> OSStatus ``` |

Modified CMIOObjectHasProperty(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectHasProperty(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>) -> Bool ``` |
| To | ``` func CMIOObjectHasProperty(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!) -> Bool ``` |

Modified CMIOObjectIsPropertySettable(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!, _: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectIsPropertySettable(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ isSettable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |
| To | ``` func CMIOObjectIsPropertySettable(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ isSettable: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus ``` |

Modified CMIOObjectPropertyListenerBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIOObjectPropertyListenerBlock = (UInt32, UnsafePointer<CMIOObjectPropertyAddress>) -> Void ``` |
| To | ``` typealias CMIOObjectPropertyListenerBlock = (UInt32, UnsafePointer<CMIOObjectPropertyAddress>?) -> Swift.Void ``` |

Modified CMIOObjectPropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIOObjectPropertyListenerProc = (CMIOObjectID, UInt32, UnsafePointer<CMIOObjectPropertyAddress>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias CMIOObjectPropertyListenerProc = (CMIOObjectID, UInt32, UnsafePointer<CMIOObjectPropertyAddress>?, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified CMIOObjectRemovePropertyListener(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!, _: CoreMediaIO.CMIOObjectPropertyListenerProc!, _: UnsafeMutableRawPointer!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectRemovePropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc!, _ clientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMIOObjectRemovePropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ listener: CoreMediaIO.CMIOObjectPropertyListenerProc!, _ clientData: UnsafeMutableRawPointer!) -> OSStatus ``` |

Modified CMIOObjectRemovePropertyListenerBlock(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!, _: DispatchQueue!, _: CoreMediaIO.CMIOObjectPropertyListenerBlock!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectRemovePropertyListenerBlock(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ dispatchQueue: dispatch_queue_t!, _ listener: CMIOObjectPropertyListenerBlock!) -> OSStatus ``` |
| To | ``` func CMIOObjectRemovePropertyListenerBlock(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ dispatchQueue: DispatchQueue!, _ listener: CoreMediaIO.CMIOObjectPropertyListenerBlock!) -> OSStatus ``` |

Modified CMIOObjectSetPropertyData(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>!, _: UInt32, _: UnsafeRawPointer!, _: UInt32, _: UnsafeRawPointer!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectSetPropertyData(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: UnsafePointer<Void>, _ dataSize: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func CMIOObjectSetPropertyData(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ qualifierDataSize: UInt32, _ qualifierData: UnsafeRawPointer!, _ dataSize: UInt32, _ data: UnsafeRawPointer!) -> OSStatus ``` |

Modified CMIOStreamClockConvertHostTimeToDeviceTime(_: UInt64, _: CFTypeRef!) -> CMTime

|  | Declaration |
| --- | --- |
| From | ``` func CMIOStreamClockConvertHostTimeToDeviceTime(_ hostTime: UInt64, _ clock: AnyObject!) -> CMTime ``` |
| To | ``` func CMIOStreamClockConvertHostTimeToDeviceTime(_ hostTime: UInt64, _ clock: CFTypeRef!) -> CMTime ``` |

Modified CMIOStreamClockCreate(_: CFAllocator!, _: CFString!, _: UnsafeRawPointer!, _: CMTime, _: UInt32, _: UInt32, _: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOStreamClockCreate(_ allocator: CFAllocator!, _ clockName: CFString!, _ sourceIdentifier: UnsafePointer<Void>, _ getTimeCallMinimumInterval: CMTime, _ numberOfEventsForRateSmoothing: UInt32, _ numberOfAveragesForRateSmoothing: UInt32, _ clock: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func CMIOStreamClockCreate(_ allocator: CFAllocator!, _ clockName: CFString!, _ sourceIdentifier: UnsafeRawPointer!, _ getTimeCallMinimumInterval: CMTime, _ numberOfEventsForRateSmoothing: UInt32, _ numberOfAveragesForRateSmoothing: UInt32, _ clock: UnsafeMutablePointer<Unmanaged<CFTypeRef>?>!) -> OSStatus ``` |

Modified CMIOStreamClockInvalidate(_: CFTypeRef!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOStreamClockInvalidate(_ clock: AnyObject!) -> OSStatus ``` |
| To | ``` func CMIOStreamClockInvalidate(_ clock: CFTypeRef!) -> OSStatus ``` |

Modified CMIOStreamClockPostTimingEvent(_: CMTime, _: UInt64, _: Bool, _: CFTypeRef!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOStreamClockPostTimingEvent(_ eventTime: CMTime, _ hostTime: UInt64, _ resynchronize: Bool, _ clock: AnyObject!) -> OSStatus ``` |
| To | ``` func CMIOStreamClockPostTimingEvent(_ eventTime: CMTime, _ hostTime: UInt64, _ resynchronize: Bool, _ clock: CFTypeRef!) -> OSStatus ``` |

Modified CMIOStreamCopyBufferQueue(_: CMIOStreamID, _: CoreMediaIO.CMIODeviceStreamQueueAlteredProc!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOStreamCopyBufferQueue(_ streamID: CMIOStreamID, _ queueAlteredProc: CMIODeviceStreamQueueAlteredProc!, _ queueAlteredRefCon: UnsafeMutablePointer<Void>, _ queue: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus ``` |
| To | ``` func CMIOStreamCopyBufferQueue(_ streamID: CMIOStreamID, _ queueAlteredProc: CoreMediaIO.CMIODeviceStreamQueueAlteredProc!, _ queueAlteredRefCon: UnsafeMutableRawPointer!, _ queue: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>!) -> OSStatus ``` |

Modified CMIOStreamScheduledOutputNotificationProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIOStreamScheduledOutputNotificationProc = (UInt64, UInt64, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CMIOStreamScheduledOutputNotificationProc = (UInt64, UInt64, UnsafeMutableRawPointer?) -> Swift.Void ``` |

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
