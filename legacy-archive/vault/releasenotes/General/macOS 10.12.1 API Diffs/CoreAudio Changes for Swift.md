---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/CoreAudio.html
archived_at: '2026-07-18T02:51:44.845491Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# CoreAudio Changes for Swift

### CoreAudio

Modified [AudioDeviceCreateIOProcID(_: AudioObjectID, _: CoreAudio.AudioDeviceIOProc, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1423215-audiodevicecreateioprocid)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: CoreAudio.AudioDeviceIOProc, _ inClientData: UnsafeMutableRawPointer?, _ outIOProcID: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>) -> OSStatus ``` |
| To | ``` func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: @escaping CoreAudio.AudioDeviceIOProc, _ inClientData: UnsafeMutableRawPointer?, _ outIOProcID: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>) -> OSStatus ``` |

Modified [AudioDeviceCreateIOProcIDWithBlock(_: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>, _: AudioObjectID, _: DispatchQueue?, _: CoreAudio.AudioDeviceIOBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422986-audiodevicecreateioprocidwithblo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceCreateIOProcIDWithBlock(_ outIOProcID: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>, _ inDevice: AudioObjectID, _ inDispatchQueue: DispatchQueue?, _ inIOBlock: CoreAudio.AudioDeviceIOBlock) -> OSStatus ``` |
| To | ``` func AudioDeviceCreateIOProcIDWithBlock(_ outIOProcID: UnsafeMutablePointer<CoreAudio.AudioDeviceIOProcID?>, _ inDevice: AudioObjectID, _ inDispatchQueue: DispatchQueue?, _ inIOBlock: @escaping CoreAudio.AudioDeviceIOBlock) -> OSStatus ``` |

Modified [AudioDeviceDestroyIOProcID(_: AudioObjectID, _: CoreAudio.AudioDeviceIOProcID) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422982-audiodevicedestroyioprocid)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceDestroyIOProcID(_ inDevice: AudioObjectID, _ inIOProcID: CoreAudio.AudioDeviceIOProcID) -> OSStatus ``` |
| To | ``` func AudioDeviceDestroyIOProcID(_ inDevice: AudioObjectID, _ inIOProcID: @escaping CoreAudio.AudioDeviceIOProcID) -> OSStatus ``` |

Modified [AudioObjectAddPropertyListener(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: CoreAudio.AudioObjectPropertyListenerProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422472-audioobjectaddpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: CoreAudio.AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus ``` |
| To | ``` func AudioObjectAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: @escaping CoreAudio.AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioObjectAddPropertyListenerBlock(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: DispatchQueue?, _: CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422686-audioobjectaddpropertylistenerbl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: DispatchQueue?, _ inListener: CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus ``` |
| To | ``` func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: DispatchQueue?, _ inListener: @escaping CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus ``` |

Modified [AudioObjectRemovePropertyListener(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: CoreAudio.AudioObjectPropertyListenerProc, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422593-audioobjectremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectRemovePropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: CoreAudio.AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus ``` |
| To | ``` func AudioObjectRemovePropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: @escaping CoreAudio.AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [AudioObjectRemovePropertyListenerBlock(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: DispatchQueue?, _: CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1421640-audioobjectremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectRemovePropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: DispatchQueue?, _ inListener: CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus ``` |
| To | ``` func AudioObjectRemovePropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: DispatchQueue?, _ inListener: @escaping CoreAudio.AudioObjectPropertyListenerBlock) -> OSStatus ``` |

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
