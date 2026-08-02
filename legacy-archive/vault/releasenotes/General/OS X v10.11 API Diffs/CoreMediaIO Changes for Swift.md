---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreMediaIO.html
archived_at: '2026-07-18T02:53:28.749738Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreMediaIO Changes for Swift

### CoreMediaIO

Removed CMIODeviceSMPTETimeCallback.init(mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc, mRefCon: UnsafeMutablePointer<Void>)Removed CMIOStreamScheduledOutputNotificationProcAndRefCon.init(scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc, scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>)Added CMIODeviceSMPTETimeCallback.init(mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc!, mRefCon: UnsafeMutablePointer<Void>)Added CMIOStreamScheduledOutputNotificationProcAndRefCon.init(scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc!, scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>)Modified CMIODeviceSMPTETimeCallback [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIODeviceSMPTETimeCallback {     var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc     var mRefCon: UnsafeMutablePointer<Void>     init()     init(mGetSMPTETimeProc mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc, mRefCon mRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CMIODeviceSMPTETimeCallback {     var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc!     var mRefCon: UnsafeMutablePointer<Void>     init()     init(mGetSMPTETimeProc mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc!, mRefCon mRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified CMIODeviceSMPTETimeCallback.mGetSMPTETimeProc

|  | Declaration |
| --- | --- |
| From | ``` var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc ``` |
| To | ``` var mGetSMPTETimeProc: CMIODeviceGetSMPTETimeProc! ``` |

Modified CMIOStreamScheduledOutputNotificationProcAndRefCon [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMIOStreamScheduledOutputNotificationProcAndRefCon {     var scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc     var scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>     init()     init(scheduledOutputNotificationProc scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc, scheduledOutputNotificationRefCon scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CMIOStreamScheduledOutputNotificationProcAndRefCon {     var scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc!     var scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>     init()     init(scheduledOutputNotificationProc scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc!, scheduledOutputNotificationRefCon scheduledOutputNotificationRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified CMIOStreamScheduledOutputNotificationProcAndRefCon.scheduledOutputNotificationProc

|  | Declaration |
| --- | --- |
| From | ``` var scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc ``` |
| To | ``` var scheduledOutputNotificationProc: CMIOStreamScheduledOutputNotificationProc! ``` |

Modified CMIODeviceGetSMPTETimeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIODeviceGetSMPTETimeProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias CMIODeviceGetSMPTETimeProc = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt64>, UnsafeMutablePointer<DarwinBoolean>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified CMIODeviceStreamQueueAlteredProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIODeviceStreamQueueAlteredProc = CFunctionPointer<((CMIOStreamID, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CMIODeviceStreamQueueAlteredProc = (CMIOStreamID, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified CMIOObjectAddPropertyListener(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>, _: CMIOObjectPropertyListenerProc!, _: UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectAddPropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc, _ clientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMIOObjectAddPropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc!, _ clientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified CMIOObjectHasProperty(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectHasProperty(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>) -> Boolean ``` |
| To | ``` func CMIOObjectHasProperty(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>) -> Bool ``` |

Modified CMIOObjectIsPropertySettable(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectIsPropertySettable(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ isSettable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func CMIOObjectIsPropertySettable(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ isSettable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified CMIOObjectPropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIOObjectPropertyListenerProc = CFunctionPointer<((CMIOObjectID, UInt32, UnsafePointer<CMIOObjectPropertyAddress>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias CMIOObjectPropertyListenerProc = (CMIOObjectID, UInt32, UnsafePointer<CMIOObjectPropertyAddress>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified CMIOObjectRemovePropertyListener(_: CMIOObjectID, _: UnsafePointer<CMIOObjectPropertyAddress>, _: CMIOObjectPropertyListenerProc!, _: UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOObjectRemovePropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc, _ clientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMIOObjectRemovePropertyListener(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>, _ listener: CMIOObjectPropertyListenerProc!, _ clientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified CMIOStreamClockPostTimingEvent(_: CMTime, _: UInt64, _: Bool, _: AnyObject!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOStreamClockPostTimingEvent(_ eventTime: CMTime, _ hostTime: UInt64, _ resynchronize: Boolean, _ clock: AnyObject!) -> OSStatus ``` |
| To | ``` func CMIOStreamClockPostTimingEvent(_ eventTime: CMTime, _ hostTime: UInt64, _ resynchronize: Bool, _ clock: AnyObject!) -> OSStatus ``` |

Modified CMIOStreamCopyBufferQueue(_: CMIOStreamID, _: CMIODeviceStreamQueueAlteredProc!, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOStreamCopyBufferQueue(_ streamID: CMIOStreamID, _ queueAlteredProc: CMIODeviceStreamQueueAlteredProc, _ queueAlteredRefCon: UnsafeMutablePointer<Void>, _ queue: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus ``` |
| To | ``` func CMIOStreamCopyBufferQueue(_ streamID: CMIOStreamID, _ queueAlteredProc: CMIODeviceStreamQueueAlteredProc!, _ queueAlteredRefCon: UnsafeMutablePointer<Void>, _ queue: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus ``` |

Modified CMIOStreamDeckCueTo(_: CMIOStreamID, _: UInt64, _: Bool) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMIOStreamDeckCueTo(_ streamID: CMIOStreamID, _ frameNumber: UInt64, _ playOnCue: Boolean) -> OSStatus ``` |
| To | ``` func CMIOStreamDeckCueTo(_ streamID: CMIOStreamID, _ frameNumber: UInt64, _ playOnCue: Bool) -> OSStatus ``` |

Modified CMIOStreamScheduledOutputNotificationProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CMIOStreamScheduledOutputNotificationProc = CFunctionPointer<((UInt64, UInt64, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CMIOStreamScheduledOutputNotificationProc = (UInt64, UInt64, UnsafeMutablePointer<Void>) -> Void ``` |

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
