---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreMediaIO.html
archived_at: '2026-07-18T02:52:14.031475Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreMediaIO Changes

## CoreMediaIO

Added CMIODeviceAVCCommand.init()Added CMIODeviceAVCCommand.init(mCommand: UnsafeMutablePointer<UInt8>, mCommandLength: UInt32, mResponse: UnsafeMutablePointer<UInt8>, mResponseLength: UInt32, mResponseUsed: UInt32)Added CMIODeviceRS422Command.init()Added CMIODeviceRS422Command.init(mCommand: UnsafeMutablePointer<UInt8>, mCommandLength: UInt32, mResponse: UnsafeMutablePointer<UInt8>, mResponseLength: UInt32, mResponseUsed: UInt32)Added CMIODeviceSMPTETimeCallback.init()Added CMIODeviceSMPTETimeCallback.init(mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc, mRefCon: UnsafeMutablePointer<Void>)Added CMIODeviceStreamConfiguration.init()Added CMIOObjectPropertyAddress.init()Added CMIOObjectPropertyAddress.init(mSelector: CMIOObjectPropertySelector, mScope: CMIOObjectPropertyScope, mElement: CMIOObjectPropertyElement)Added CMIOStreamDeck.init()Added CMIOStreamDeck.init(mStatus: UInt32, mState: UInt32, mState2: UInt32)Added CMIOStreamScheduledOutputNotificationProcAndRefCon.init()Added CMIOStreamScheduledOutputNotificationProcAndRefCon.init(scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc, scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>)Modified CMIODeviceAVCCommand [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIODeviceAVCCommand {     var mCommand: UnsafePointer<UInt8>     var mCommandLength: UInt32     var mResponse: UnsafePointer<UInt8>     var mResponseLength: UInt32     var mResponseUsed: UInt32 } ``` |
| To | ``` struct CMIODeviceAVCCommand {     var mCommand: UnsafeMutablePointer<UInt8>     var mCommandLength: UInt32     var mResponse: UnsafeMutablePointer<UInt8>     var mResponseLength: UInt32     var mResponseUsed: UInt32     init()     init(mCommand mCommand: UnsafeMutablePointer<UInt8>, mCommandLength mCommandLength: UInt32, mResponse mResponse: UnsafeMutablePointer<UInt8>, mResponseLength mResponseLength: UInt32, mResponseUsed mResponseUsed: UInt32) } ``` |

Modified CMIODeviceAVCCommand.mCommand

|  | Declaration |
| --- | --- |
| From | ``` var mCommand: UnsafePointer<UInt8> ``` |
| To | ``` var mCommand: UnsafeMutablePointer<UInt8> ``` |

Modified CMIODeviceAVCCommand.mResponse

|  | Declaration |
| --- | --- |
| From | ``` var mResponse: UnsafePointer<UInt8> ``` |
| To | ``` var mResponse: UnsafeMutablePointer<UInt8> ``` |

Modified CMIODeviceRS422Command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIODeviceRS422Command {     var mCommand: UnsafePointer<UInt8>     var mCommandLength: UInt32     var mResponse: UnsafePointer<UInt8>     var mResponseLength: UInt32     var mResponseUsed: UInt32 } ``` |
| To | ``` struct CMIODeviceRS422Command {     var mCommand: UnsafeMutablePointer<UInt8>     var mCommandLength: UInt32     var mResponse: UnsafeMutablePointer<UInt8>     var mResponseLength: UInt32     var mResponseUsed: UInt32     init()     init(mCommand mCommand: UnsafeMutablePointer<UInt8>, mCommandLength mCommandLength: UInt32, mResponse mResponse: UnsafeMutablePointer<UInt8>, mResponseLength mResponseLength: UInt32, mResponseUsed mResponseUsed: UInt32) } ``` |

Modified CMIODeviceRS422Command.mCommand

|  | Declaration |
| --- | --- |
| From | ``` var mCommand: UnsafePointer<UInt8> ``` |
| To | ``` var mCommand: UnsafeMutablePointer<UInt8> ``` |

Modified CMIODeviceRS422Command.mResponse

|  | Declaration |
| --- | --- |
| From | ``` var mResponse: UnsafePointer<UInt8> ``` |
| To | ``` var mResponse: UnsafeMutablePointer<UInt8> ``` |

Modified CMIODeviceSMPTETimeCallback [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIODeviceSMPTETimeCallback {     var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc     var mRefCon: UnsafePointer<()> } ``` |
| To | ``` struct CMIODeviceSMPTETimeCallback {     var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc     var mRefCon: UnsafeMutablePointer<Void>     init()     init(mGetSMPTETimeProc mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc, mRefCon mRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified CMIODeviceSMPTETimeCallback.mRefCon

|  | Declaration |
| --- | --- |
| From | ``` var mRefCon: UnsafePointer<()> ``` |
| To | ``` var mRefCon: UnsafeMutablePointer<Void> ``` |

Modified CMIODeviceStreamConfiguration [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIODeviceStreamConfiguration {     var mNumberStreams: UInt32 } ``` |
| To | ``` struct CMIODeviceStreamConfiguration {     var mNumberStreams: UInt32     init() } ``` |

Modified CMIOObjectPropertyAddress [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIOObjectPropertyAddress {     var mSelector: CMIOObjectPropertySelector     var mScope: CMIOObjectPropertyScope     var mElement: CMIOObjectPropertyElement } ``` |
| To | ``` struct CMIOObjectPropertyAddress {     var mSelector: CMIOObjectPropertySelector     var mScope: CMIOObjectPropertyScope     var mElement: CMIOObjectPropertyElement     init()     init(mSelector mSelector: CMIOObjectPropertySelector, mScope mScope: CMIOObjectPropertyScope, mElement mElement: CMIOObjectPropertyElement) } ``` |

Modified CMIOStreamDeck [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIOStreamDeck {     var mStatus: UInt32     var mState: UInt32     var mState2: UInt32 } ``` |
| To | ``` struct CMIOStreamDeck {     var mStatus: UInt32     var mState: UInt32     var mState2: UInt32     init()     init(mStatus mStatus: UInt32, mState mState: UInt32, mState2 mState2: UInt32) } ``` |

Modified CMIOStreamScheduledOutputNotificationProcAndRefCon [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIOStreamScheduledOutputNotificationProcAndRefCon {     var scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc     var scheduledOutputNotificationRefCon: UnsafePointer<()> } ``` |
| To | ``` struct CMIOStreamScheduledOutputNotificationProcAndRefCon {     var scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc     var scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>     init()     init(scheduledOutputNotificationProc scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc, scheduledOutputNotificationRefCon scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified CMIOStreamScheduledOutputNotificationProcAndRefCon.scheduledOutputNotificationRefCon

|  | Declaration |
| --- | --- |
| From | ``` var scheduledOutputNotificationRefCon: UnsafePointer<()> ``` |
| To | ``` var scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void> ``` |

Modified CMIODeviceGetSMPTETimeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIODeviceGetSMPTETimeProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<UInt64>, UnsafePointer<Boolean>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias CMIODeviceGetSMPTETimeProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified CMIODeviceProcessAVCCommand(CMIODeviceID, UnsafeMutablePointer<CMIODeviceAVCCommand>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIODeviceProcessAVCCommand(_ deviceID: CMIODeviceID, _ ioAVCCommand: UnsafePointer<CMIODeviceAVCCommand>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIODeviceProcessAVCCommand(_ deviceID: CMIODeviceID, _ ioAVCCommand: UnsafeMutablePointer<CMIODeviceAVCCommand>) -> OSStatus ``` | OS X 10.7 |

Modified CMIODeviceProcessRS422Command(CMIODeviceID, UnsafeMutablePointer<CMIODeviceRS422Command>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIODeviceProcessRS422Command(_ deviceID: CMIODeviceID, _ ioRS422Command: UnsafePointer<CMIODeviceRS422Command>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIODeviceProcessRS422Command(_ deviceID: CMIODeviceID, _ ioRS422Command: UnsafeMutablePointer<CMIODeviceRS422Command>) -> OSStatus ``` | OS X 10.7 |

Modified CMIODeviceStartStream(CMIODeviceID, CMIOStreamID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIODeviceStopStream(CMIODeviceID, CMIOStreamID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIODeviceStreamQueueAlteredProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIODeviceStreamQueueAlteredProc = CFunctionPointer<((CMIOStreamID, UnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CMIODeviceStreamQueueAlteredProc = CFunctionPointer<((CMIOStreamID, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CMIOObjectAddPropertyListener(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>, CMIOObjectPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectAddPropertyListener(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc, _ clientData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOObjectAddPropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc, _ clientData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMIOObjectAddPropertyListenerBlock(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>, dispatch_queue_t!, CMIOObjectPropertyListenerBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectAddPropertyListenerBlock(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>, _ dispatchQueue: dispatch_queue_t!, _ listener: CMIOObjectPropertyListenerBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOObjectAddPropertyListenerBlock(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ dispatchQueue: dispatch_queue_t!, _ listener: CMIOObjectPropertyListenerBlock!) -> OSStatus ``` | OS X 10.8 |

Modified CMIOObjectGetPropertyData(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectGetPropertyData(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: ConstUnsafePointer<()>, _ dataSize: UInt32, _ dataUsed: UnsafePointer<UInt32>, _ data: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOObjectGetPropertyData(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: UnsafePointer<Void>, _ dataSize: UInt32, _ dataUsed: UnsafeMutablePointer<UInt32>, _ data: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMIOObjectGetPropertyDataSize(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectGetPropertyDataSize(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: ConstUnsafePointer<()>, _ dataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOObjectGetPropertyDataSize(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: UnsafePointer<Void>, _ dataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.7 |

Modified CMIOObjectHasProperty(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectHasProperty(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CMIOObjectHasProperty(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>) -> Boolean ``` | OS X 10.7 |

Modified CMIOObjectIsPropertySettable(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectIsPropertySettable(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>, _ isSettable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOObjectIsPropertySettable(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ isSettable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.7 |

Modified CMIOObjectPropertyListenerBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIOObjectPropertyListenerBlock = (UInt32, ConstUnsafePointer<CMIOObjectPropertyAddress>) -> Void ``` |
| To | ``` typealias CMIOObjectPropertyListenerBlock = (UInt32, UnsafePointer<CMIOObjectPropertyAddress>) -> Void ``` |

Modified CMIOObjectPropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIOObjectPropertyListenerProc = CFunctionPointer<((CMIOObjectID, UInt32, ConstUnsafePointer<CMIOObjectPropertyAddress>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias CMIOObjectPropertyListenerProc = CFunctionPointer<((CMIOObjectID, UInt32, UnsafePointer<CMIOObjectPropertyAddress>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified CMIOObjectRemovePropertyListener(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>, CMIOObjectPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectRemovePropertyListener(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc, _ clientData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOObjectRemovePropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc, _ clientData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMIOObjectRemovePropertyListenerBlock(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>, dispatch_queue_t!, CMIOObjectPropertyListenerBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectRemovePropertyListenerBlock(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>, _ dispatchQueue: dispatch_queue_t!, _ listener: CMIOObjectPropertyListenerBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOObjectRemovePropertyListenerBlock(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ dispatchQueue: dispatch_queue_t!, _ listener: CMIOObjectPropertyListenerBlock!) -> OSStatus ``` | OS X 10.8 |

Modified CMIOObjectSetPropertyData(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOObjectSetPropertyData(_ objectID: CMIOObjectID, _ address: ConstUnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: ConstUnsafePointer<()>, _ dataSize: UInt32, _ data: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOObjectSetPropertyData(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ qualifierDataSize: UInt32, _ qualifierData: UnsafePointer<Void>, _ dataSize: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMIOObjectShow(CMIOObjectID)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIOStreamClockConvertHostTimeToDeviceTime(UInt64, AnyObject!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIOStreamClockCreate(CFAllocator!, CFString!, UnsafePointer<Void>, CMTime, UInt32, UInt32, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOStreamClockCreate(_ allocator: CFAllocator!, _ clockName: CFString!, _ sourceIdentifier: ConstUnsafePointer<()>, _ getTimeCallMinimumInterval: CMTime, _ numberOfEventsForRateSmoothing: UInt32, _ numberOfAveragesForRateSmoothing: UInt32, _ clock: UnsafePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOStreamClockCreate(_ allocator: CFAllocator!, _ clockName: CFString!, _ sourceIdentifier: UnsafePointer<Void>, _ getTimeCallMinimumInterval: CMTime, _ numberOfEventsForRateSmoothing: UInt32, _ numberOfAveragesForRateSmoothing: UInt32, _ clock: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMIOStreamClockInvalidate(AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIOStreamClockPostTimingEvent(CMTime, UInt64, Boolean, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIOStreamCopyBufferQueue(CMIOStreamID, CMIODeviceStreamQueueAlteredProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMIOStreamCopyBufferQueue(_ streamID: CMIOStreamID, _ queueAlteredProc: CMIODeviceStreamQueueAlteredProc, _ queueAlteredRefCon: UnsafePointer<()>, _ queue: UnsafePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMIOStreamCopyBufferQueue(_ streamID: CMIOStreamID, _ queueAlteredProc: CMIODeviceStreamQueueAlteredProc, _ queueAlteredRefCon: UnsafeMutablePointer<Void>, _ queue: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMIOStreamDeckCueTo(CMIOStreamID, UInt64, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIOStreamDeckJog(CMIOStreamID, Int32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIOStreamDeckPlay(CMIOStreamID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIOStreamDeckStop(CMIOStreamID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMIOStreamScheduledOutputNotificationProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIOStreamScheduledOutputNotificationProc = CFunctionPointer<((UInt64, UInt64, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CMIOStreamScheduledOutputNotificationProc = CFunctionPointer<((UInt64, UInt64, UnsafeMutablePointer<Void>) -> Void)> ``` |

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
