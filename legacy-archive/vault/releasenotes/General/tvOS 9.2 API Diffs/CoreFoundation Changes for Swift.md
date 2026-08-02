---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/CoreFoundation.html
archived_at: '2026-07-18T02:58:05.366742Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# CoreFoundation Changes for Swift

### CoreFoundation

Modified [CFAllocator](https://developer.apple.com/documentation/corefoundation/cfallocatorref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFAllocatorRef | ``` typealias CFAllocatorRef = CFAllocator ``` |
| To | CFAllocator | ``` class CFAllocator { } ``` |

Modified [CFArray](https://developer.apple.com/documentation/corefoundation/cfarray)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFArrayRef | ``` typealias CFArrayRef = CFArray ``` |
| To | CFArray | ``` class CFArray { } ``` |

Modified [CFAttributedString](https://developer.apple.com/documentation/corefoundation/cfattributedstringref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFAttributedStringRef | ``` typealias CFAttributedStringRef = CFAttributedString ``` |
| To | CFAttributedString | ``` class CFAttributedString { } ``` |

Modified [CFBag](https://developer.apple.com/documentation/corefoundation/cfbag)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFBagRef | ``` typealias CFBagRef = CFBag ``` |
| To | CFBag | ``` class CFBag { } ``` |

Modified [CFBinaryHeap](https://developer.apple.com/documentation/corefoundation/cfbinaryheapref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFBinaryHeapRef | ``` typealias CFBinaryHeapRef = CFBinaryHeap ``` |
| To | CFBinaryHeap | ``` class CFBinaryHeap { } ``` |

Modified [CFBitVector](https://developer.apple.com/documentation/corefoundation/cfbitvector)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFBitVectorRef | ``` typealias CFBitVectorRef = CFBitVector ``` |
| To | CFBitVector | ``` class CFBitVector { } ``` |

Modified [CFBoolean](https://developer.apple.com/documentation/corefoundation/cfbooleanref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFBooleanRef | ``` typealias CFBooleanRef = CFBoolean ``` |
| To | CFBoolean | ``` class CFBoolean { } ``` |

Modified [CFBundle](https://developer.apple.com/documentation/corefoundation/cfbundleref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFBundleRef | ``` typealias CFBundleRef = CFBundle ``` |
| To | CFBundle | ``` class CFBundle { } ``` |

Modified [CFCalendar](https://developer.apple.com/documentation/corefoundation/cfcalendar)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFCalendarRef | ``` typealias CFCalendarRef = CFCalendar ``` |
| To | CFCalendar | ``` class CFCalendar { } ``` |

Modified [CFCharacterSet](https://developer.apple.com/documentation/corefoundation/cfcharactersetref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFCharacterSetRef | ``` typealias CFCharacterSetRef = CFCharacterSet ``` |
| To | CFCharacterSet | ``` class CFCharacterSet { } ``` |

Modified [CFData](https://developer.apple.com/documentation/corefoundation/cfdataref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFDataRef | ``` typealias CFDataRef = CFData ``` |
| To | CFData | ``` class CFData { } ``` |

Modified [CFDate](https://developer.apple.com/documentation/corefoundation/cfdate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFDateRef | ``` typealias CFDateRef = CFDate ``` |
| To | CFDate | ``` class CFDate { } ``` |

Modified [CFDateFormatter](https://developer.apple.com/documentation/corefoundation/cfdateformatterref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFDateFormatterRef | ``` typealias CFDateFormatterRef = CFDateFormatter ``` |
| To | CFDateFormatter | ``` class CFDateFormatter { } ``` |

Modified [CFDictionary](https://developer.apple.com/documentation/corefoundation/cfdictionaryref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFDictionaryRef | ``` typealias CFDictionaryRef = CFDictionary ``` |
| To | CFDictionary | ``` class CFDictionary { } ``` |

Modified [CFError](https://developer.apple.com/documentation/corefoundation/cferror)

|  | Name | Declaration | Protocols |
| --- | --- | --- | --- |
| From | CFErrorRef | ``` typealias CFErrorRef = CFError ``` | -- |
| To | CFError | ``` class CFError { } extension CFError : ErrorType { } ``` | ErrorType |

Modified [CFFileDescriptor](https://developer.apple.com/documentation/corefoundation/cffiledescriptorref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFFileDescriptorRef | ``` typealias CFFileDescriptorRef = CFFileDescriptor ``` |
| To | CFFileDescriptor | ``` class CFFileDescriptor { } ``` |

Modified [CFFileSecurity](https://developer.apple.com/documentation/corefoundation/cffilesecurityref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFFileSecurityRef | ``` typealias CFFileSecurityRef = CFFileSecurity ``` |
| To | CFFileSecurity | ``` class CFFileSecurity { } ``` |

Modified [CFLocale](https://developer.apple.com/documentation/corefoundation/cflocale)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFLocaleRef | ``` typealias CFLocaleRef = CFLocale ``` |
| To | CFLocale | ``` class CFLocale { } ``` |

Modified [CFMachPort](https://developer.apple.com/documentation/corefoundation/cfmachportref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMachPortRef | ``` typealias CFMachPortRef = CFMachPort ``` |
| To | CFMachPort | ``` class CFMachPort { } ``` |

Modified [CFMessagePort](https://developer.apple.com/documentation/corefoundation/cfmessageportref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMessagePortRef | ``` typealias CFMessagePortRef = CFMessagePort ``` |
| To | CFMessagePort | ``` class CFMessagePort { } ``` |

Modified [CFMutableArray](https://developer.apple.com/documentation/corefoundation/cfmutablearrayref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableArrayRef | ``` typealias CFMutableArrayRef = CFMutableArray ``` |
| To | CFMutableArray | ``` class CFMutableArray { } ``` |

Modified [CFMutableAttributedString](https://developer.apple.com/documentation/corefoundation/cfmutableattributedstring)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableAttributedStringRef | ``` typealias CFMutableAttributedStringRef = CFMutableAttributedString ``` |
| To | CFMutableAttributedString | ``` class CFMutableAttributedString { } ``` |

Modified [CFMutableBag](https://developer.apple.com/documentation/corefoundation/cfmutablebagref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableBagRef | ``` typealias CFMutableBagRef = CFMutableBag ``` |
| To | CFMutableBag | ``` class CFMutableBag { } ``` |

Modified [CFMutableBitVector](https://developer.apple.com/documentation/corefoundation/cfmutablebitvectorref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableBitVectorRef | ``` typealias CFMutableBitVectorRef = CFMutableBitVector ``` |
| To | CFMutableBitVector | ``` class CFMutableBitVector { } ``` |

Modified [CFMutableCharacterSet](https://developer.apple.com/documentation/corefoundation/cfmutablecharactersetref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableCharacterSetRef | ``` typealias CFMutableCharacterSetRef = CFMutableCharacterSet ``` |
| To | CFMutableCharacterSet | ``` class CFMutableCharacterSet { } ``` |

Modified [CFMutableData](https://developer.apple.com/documentation/corefoundation/cfmutabledata)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableDataRef | ``` typealias CFMutableDataRef = CFMutableData ``` |
| To | CFMutableData | ``` class CFMutableData { } ``` |

Modified [CFMutableDictionary](https://developer.apple.com/documentation/corefoundation/cfmutabledictionaryref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableDictionaryRef | ``` typealias CFMutableDictionaryRef = CFMutableDictionary ``` |
| To | CFMutableDictionary | ``` class CFMutableDictionary { } ``` |

Modified [CFMutableSet](https://developer.apple.com/documentation/corefoundation/cfmutablesetref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableSetRef | ``` typealias CFMutableSetRef = CFMutableSet ``` |
| To | CFMutableSet | ``` class CFMutableSet { } ``` |

Modified [CFMutableString](https://developer.apple.com/documentation/corefoundation/cfmutablestring)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFMutableStringRef | ``` typealias CFMutableStringRef = CFMutableString ``` |
| To | CFMutableString | ``` class CFMutableString { } ``` |

Modified [CFNotificationCenter](https://developer.apple.com/documentation/corefoundation/cfnotificationcenterref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFNotificationCenterRef | ``` typealias CFNotificationCenterRef = CFNotificationCenter ``` |
| To | CFNotificationCenter | ``` class CFNotificationCenter { } ``` |

Modified [CFNull](https://developer.apple.com/documentation/corefoundation/cfnullref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFNullRef | ``` typealias CFNullRef = CFNull ``` |
| To | CFNull | ``` class CFNull { } ``` |

Modified [CFNumber](https://developer.apple.com/documentation/corefoundation/cfnumber)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFNumberRef | ``` typealias CFNumberRef = CFNumber ``` |
| To | CFNumber | ``` class CFNumber { } ``` |

Modified [CFNumberFormatter](https://developer.apple.com/documentation/corefoundation/cfnumberformatterref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFNumberFormatterRef | ``` typealias CFNumberFormatterRef = CFNumberFormatter ``` |
| To | CFNumberFormatter | ``` class CFNumberFormatter { } ``` |

Modified [CFPlugIn](https://developer.apple.com/documentation/corefoundation/cfplugin)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFPlugInRef | ``` typealias CFPlugInRef = CFPlugIn ``` |
| To | CFPlugIn | ``` class CFPlugIn { } ``` |

Modified [CFPlugInInstance](https://developer.apple.com/documentation/corefoundation/cfplugininstanceref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFPlugInInstanceRef | ``` typealias CFPlugInInstanceRef = CFPlugInInstance ``` |
| To | CFPlugInInstance | ``` class CFPlugInInstance { } ``` |

Modified [CFReadStream](https://developer.apple.com/documentation/corefoundation/cfreadstreamref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFReadStreamRef | ``` typealias CFReadStreamRef = CFReadStream ``` |
| To | CFReadStream | ``` class CFReadStream { } ``` |

Modified [CFRunLoop](https://developer.apple.com/documentation/corefoundation/cfrunloopref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFRunLoopRef | ``` typealias CFRunLoopRef = CFRunLoop ``` |
| To | CFRunLoop | ``` class CFRunLoop { } ``` |

Modified [CFRunLoopObserver](https://developer.apple.com/documentation/corefoundation/cfrunloopobserver)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFRunLoopObserverRef | ``` typealias CFRunLoopObserverRef = CFRunLoopObserver ``` |
| To | CFRunLoopObserver | ``` class CFRunLoopObserver { } ``` |

Modified [CFRunLoopSource](https://developer.apple.com/documentation/corefoundation/cfrunloopsource)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFRunLoopSourceRef | ``` typealias CFRunLoopSourceRef = CFRunLoopSource ``` |
| To | CFRunLoopSource | ``` class CFRunLoopSource { } ``` |

Modified [CFRunLoopTimer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimer)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFRunLoopTimerRef | ``` typealias CFRunLoopTimerRef = CFRunLoopTimer ``` |
| To | CFRunLoopTimer | ``` class CFRunLoopTimer { } ``` |

Modified [CFSet](https://developer.apple.com/documentation/corefoundation/cfsetref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFSetRef | ``` typealias CFSetRef = CFSet ``` |
| To | CFSet | ``` class CFSet { } ``` |

Modified [CFSocket](https://developer.apple.com/documentation/corefoundation/cfsocket)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFSocketRef | ``` typealias CFSocketRef = CFSocket ``` |
| To | CFSocket | ``` class CFSocket { } ``` |

Modified [CFSocketSignature [struct]](https://developer.apple.com/documentation/corefoundation/cfsocketsignature)

|  | Declaration |
| --- | --- |
| From | ``` struct CFSocketSignature {     var protocolFamily: Int32     var socketType: Int32     var `protocol`: Int32     var address: Unmanaged<CFData>!     init()     init(protocolFamily protocolFamily: Int32, socketType socketType: Int32, `protocol` `protocol`: Int32, address address: Unmanaged<CFData>!) } ``` |
| To | ``` struct CFSocketSignature {     var protocolFamily: Int32     var socketType: Int32     var `protocol`: Int32     var address: Unmanaged<CFData>!     init()     init(protocolFamily protocolFamily: Int32, socketType socketType: Int32, protocol protocol: Int32, address address: Unmanaged<CFData>!) } ``` |

Modified [CFSocketSignature.init(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Unmanaged<CFData>!)](https://developer.apple.com/documentation/corefoundation/cfsocketsignature/1542802-init)

|  | Declaration |
| --- | --- |
| From | ``` init(protocolFamily protocolFamily: Int32, socketType socketType: Int32, `protocol` `protocol`: Int32, address address: Unmanaged<CFData>!) ``` |
| To | ``` init(protocolFamily protocolFamily: Int32, socketType socketType: Int32, protocol protocol: Int32, address address: Unmanaged<CFData>!) ``` |

Modified [CFString](https://developer.apple.com/documentation/corefoundation/cfstringref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFStringRef | ``` typealias CFStringRef = CFString ``` |
| To | CFString | ``` class CFString { } ``` |

Modified [CFStringTokenizer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizer)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFStringTokenizerRef | ``` typealias CFStringTokenizerRef = CFStringTokenizer ``` |
| To | CFStringTokenizer | ``` class CFStringTokenizer { } ``` |

Modified [CFTimeZone](https://developer.apple.com/documentation/corefoundation/cftimezone)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFTimeZoneRef | ``` typealias CFTimeZoneRef = CFTimeZone ``` |
| To | CFTimeZone | ``` class CFTimeZone { } ``` |

Modified [CFTree](https://developer.apple.com/documentation/corefoundation/cftree)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFTreeRef | ``` typealias CFTreeRef = CFTree ``` |
| To | CFTree | ``` class CFTree { } ``` |

Modified [CFURL](https://developer.apple.com/documentation/corefoundation/cfurl)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFURLRef | ``` typealias CFURLRef = CFURL ``` |
| To | CFURL | ``` class CFURL { } ``` |

Modified [CFURLEnumerator](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFURLEnumeratorRef | ``` typealias CFURLEnumeratorRef = CFURLEnumerator ``` |
| To | CFURLEnumerator | ``` class CFURLEnumerator { } ``` |

Modified [CFUUID](https://developer.apple.com/documentation/corefoundation/cfuuidref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFUUIDRef | ``` typealias CFUUIDRef = CFUUID ``` |
| To | CFUUID | ``` class CFUUID { } ``` |

Modified [CFWriteStream](https://developer.apple.com/documentation/corefoundation/cfwritestreamref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CFWriteStreamRef | ``` typealias CFWriteStreamRef = CFWriteStream ``` |
| To | CFWriteStream | ``` class CFWriteStream { } ``` |

Modified [CFPlugInRegisterFactoryFunction(_: CFUUID!, _: CFPlugInFactoryFunction!) -> Bool](https://developer.apple.com/documentation/corefoundation/1493868-cfpluginregisterfactoryfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CFPlugInRegisterFactoryFunction(_ factoryUUID: CFUUID!, _ `func`: CFPlugInFactoryFunction!) -> Bool ``` |
| To | ``` func CFPlugInRegisterFactoryFunction(_ factoryUUID: CFUUID!, _ func: CFPlugInFactoryFunction!) -> Bool ``` |

Modified [CFSocketCreate(_: CFAllocator!, _: Int32, _: Int32, _: Int32, _: CFOptionFlags, _: CFSocketCallBack!, _: UnsafePointer<CFSocketContext>) -> CFSocket!](https://developer.apple.com/documentation/corefoundation/1543527-cfsocketcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ `protocol`: Int32, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |
| To | ``` func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ protocol: Int32, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>) -> CFSocket! ``` |

Modified [CFURLCreateCopyAppendingPathExtension(_: CFAllocator!, _: CFURL!, _: CFString!) -> CFURL!](https://developer.apple.com/documentation/corefoundation/1541648-cfurlcreatecopyappendingpathexte)

|  | Declaration |
| --- | --- |
| From | ``` func CFURLCreateCopyAppendingPathExtension(_ allocator: CFAllocator!, _ url: CFURL!, _ `extension`: CFString!) -> CFURL! ``` |
| To | ``` func CFURLCreateCopyAppendingPathExtension(_ allocator: CFAllocator!, _ url: CFURL!, _ extension: CFString!) -> CFURL! ``` |

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
