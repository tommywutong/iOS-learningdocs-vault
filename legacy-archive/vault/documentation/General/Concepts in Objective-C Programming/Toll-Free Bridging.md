---
title: Concepts in Objective-C Programming
apple_id: TP40010810
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html
archived_at: '2026-07-15T07:33:45.634229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Concepts in Objective-C Programming](About%20the%20Basic%20Programming%20Concepts%20for%20Cocoa%20and%20Cocoa%20Touch.md)


[Next](Document%20Revision%20History.md)[Previous](Target-Action.md)

# Toll-Free Bridging

There are a number of data types in the Core Foundation framework and the Foundation framework that can be used interchangeably. This capability, called _toll-free bridging_, means that you can use the same data type as the parameter to a Core Foundation function call or as the receiver of an Objective-C message. For example, `NSLocale` (see _[NSLocale Class Reference](https://developer.apple.com/documentation/foundation/nslocale)_) is interchangeable with its Core Foundation counterpart, CFLocale (see _[CFLocale Reference](https://developer.apple.com/documentation/corefoundation/cflocale)_). Therefore, in a method where you see an `NSLocale *` parameter, you can pass a `CFLocaleRef`, and in a function where you see a `CFLocaleRef` parameter, you can pass an `NSLocale` instance. You cast one type to the other to suppress compiler warnings, as illustrated in the following example.

```
NSLocale *gbNSLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_GB"];
CFLocaleRef gbCFLocale = (CFLocaleRef) gbNSLocale;
CFStringRef cfIdentifier = CFLocaleGetIdentifier (gbCFLocale);
NSLog(@"cfIdentifier: %@", (NSString *)cfIdentifier);
// logs: "cfIdentifier: en_GB"
CFRelease((CFLocaleRef) gbNSLocale);

CFLocaleRef myCFLocale = CFLocaleCopyCurrent();
NSLocale * myNSLocale = (NSLocale *) myCFLocale;
[myNSLocale autorelease];
NSString *nsIdentifier = [myNSLocale localeIdentifier];
CFShow((CFStringRef) [@"nsIdentifier: " stringByAppendingString:nsIdentifier]);
// logs identifier for current locale
```

Note from the example that the memory management functions and methods are also interchangeable—you can use [CFRelease](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) with a Cocoa object and [release](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release) and [autorelease](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/autorelease) with a Core Foundation object.

Toll-free bridging has been available since OS X v10.0. Table 13-1 provides a list of the data types that are interchangeable between Core Foundation and Foundation. For each pair, the table also lists the version of OS X in which toll-free bridging between them became available.

__Table 13-1__  Data types that can be used interchangeably between Core Foundation and Foundation

| Core Foundation type | Foundation class | Availability |
| [CFArrayRef](https://developer.apple.com/documentation/corefoundation/cfarray) | [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) | OS X 10.0 |
| [CFAttributedStringRef](https://developer.apple.com/documentation/corefoundation/cfattributedstringref) | [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString) | OS X 10.4 |
| [CFBooleanRef](https://developer.apple.com/documentation/corefoundation/cfbooleanref) | [NSNumber](https://developer.apple.com/documentation/foundation/nsnumber) | OS X 10.0 |
| [CFCalendarRef](https://developer.apple.com/documentation/corefoundation/cfcalendarref) | [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar) | OS X 10.4 |
| [CFCharacterSetRef](https://developer.apple.com/documentation/corefoundation/cfcharactersetref) | [NSCharacterSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/cl/NSCharacterSet) | OS X 10.0 |
| [CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata) | [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) | OS X 10.0 |
| [CFDateRef](https://developer.apple.com/documentation/corefoundation/cfdateref) | [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate) | OS X 10.0 |
| [CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref) | [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) | OS X 10.0 |
| [CFErrorRef](https://developer.apple.com/documentation/corefoundation/cferror) | [NSError](https://developer.apple.com/documentation/foundation/nserror) | OS X 10.5 |
| [CFLocaleRef](https://developer.apple.com/documentation/corefoundation/cflocale) | [NSLocale](https://developer.apple.com/documentation/foundation/nslocale) | OS X 10.4 |
| [CFMutableArrayRef](https://developer.apple.com/documentation/corefoundation/cfmutablearray) | [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray) | OS X 10.0 |
| [CFMutableAttributedStringRef](https://developer.apple.com/documentation/corefoundation/cfmutableattributedstring) | [NSMutableAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSMutableAttributedString) | OS X 10.4 |
| [CFMutableCharacterSetRef](https://developer.apple.com/documentation/corefoundation/cfmutablecharacterset) | [NSMutableCharacterSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCharacterSetClstr/Description.html#//apple_ref/occ/cl/NSMutableCharacterSet) | OS X 10.0 |
| [CFMutableDataRef](https://developer.apple.com/documentation/corefoundation/cfmutabledataref) | [NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) | OS X 10.0 |
| [CFMutableDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfmutabledictionaryref) | [NSMutableDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSMutableDictionary) | OS X 10.0 |
| [CFMutableSetRef](https://developer.apple.com/documentation/corefoundation/cfmutableset) | [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) | OS X 10.0 |
| [CFMutableStringRef](https://developer.apple.com/documentation/corefoundation/cfmutablestringref) | [NSMutableString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSMutableString) | OS X 10.0 |
| [CFNullRef](https://developer.apple.com/documentation/corefoundation/cfnullref) | [NSNull](https://developer.apple.com/documentation/foundation/nsnull) | OS X 10.2 |
| [CFNumberRef](https://developer.apple.com/documentation/corefoundation/cfnumberref) | [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) | OS X 10.0 |
| [CFReadStreamRef](https://developer.apple.com/documentation/corefoundation/cfreadstream) | [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) | OS X 10.0 |
| [CFRunLoopTimerRef](https://developer.apple.com/documentation/corefoundation/cfrunlooptimerref) | [NSTimer](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/cl/NSTimer) | OS X 10.0 |
| [CFSetRef](https://developer.apple.com/documentation/corefoundation/cfset) | [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet) | OS X 10.0 |
| [CFStringRef](https://developer.apple.com/documentation/corefoundation/cfstringref) | [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) | OS X 10.0 |
| [CFTimeZoneRef](https://developer.apple.com/documentation/corefoundation/cftimezone) | [NSTimeZone](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimeZoneClassCluster/Description.html#//apple_ref/occ/cl/NSTimeZone) | OS X 10.0 |
| [CFURLRef](https://developer.apple.com/documentation/corefoundation/cfurl) | [NSURL](https://developer.apple.com/documentation/foundation/nsurl) | OS X 10.0 |
| [CFWriteStreamRef](https://developer.apple.com/documentation/corefoundation/cfwritestreamref) | [NSOutputStream](https://developer.apple.com/documentation/foundation/nsoutputstream) | OS X 10.0 |

[Next](Document%20Revision%20History.md)[Previous](Target-Action.md)

