---
title: Carbon-Cocoa Integration Guide
apple_id: TP30000893
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CarbonCocoaDoc/Articles/InterchangeableDataTypes.html
archived_at: '2026-07-15T07:11:56.989876Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon-Cocoa Integration Guide](Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md)


[Next](Using%20Carbon%20and%20Cocoa%20in%20the%20Same%20Application.md)[Previous](Preprocessing%20Mixed-Language%20Code.md)

# Interchangeable Data Types

There are a number of data types in the Core Foundation framework (Carbon) and the Foundation framework (Cocoa) that can be used interchangeably. This means that you can use the same data structure as the argument to a Core Foundation function call or as the receiver of an Objective-C message invocation. For example, `NSLocale` (see _[NSLocale Class Reference](https://developer.apple.com/documentation/foundation/nslocale)_) is interchangeable with its Core Foundation counterpart, CFLocale (see _[CFLocale Reference](https://developer.apple.com/documentation/corefoundation/cflocale)_). Therefore, in a method where you see an `NSLocale *` parameter, you can pass a `CFLocaleRef`, and in a function where you see a `CFLocaleRef` parameter, you can pass an `NSLocale` instance. You cast one type to the other to suppress compiler warnings, as illustrated in the following example.

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

Data types that can be used interchangeably are also referred to as _toll-free bridged_ data types. Toll-free bridging has been available since Mac OS X v10.0. Table 1 provides a list of the data types that are interchangeable between Core Foundation and Foundation. For each pair, the table also lists the version of Mac OS X in which toll-free bridging between them became available.

__Table 1__  Data types that can be used interchangeably between Core Foundation and Foundation

| Core Foundation type | Foundation class | Availability |
| `CFArrayRef` | `NSArray` | Mac OS X v10.0 |
| `CFAttributedStringRef` | `NSAttributedString` | Mac OS X v10.4 |
| `CFCalendarRef` | `NSCalendar` | Mac OS X v10.4 |
| `CFCharacterSetRef` | `NSCharacterSet` | Mac OS X v10.0 |
| `CFDataRef` | `NSData` | Mac OS X v10.0 |
| `CFDateRef` | `NSDate` | Mac OS X v10.0 |
| `CFDictionaryRef` | `NSDictionary` | Mac OS X v10.0 |
| `CFErrorRef` | `NSError` | Mac OS X v10.5 |
| `CFLocaleRef` | `NSLocale` | Mac OS X v10.4 |
| `CFMutableArrayRef` | `NSMutableArray` | Mac OS X v10.0 |
| `CFMutableAttributedStringRef` | `NSMutableAttributedString` | Mac OS X v10.4 |
| `CFMutableCharacterSetRef` | `NSMutableCharacterSet` | Mac OS X v10.0 |
| `CFMutableDataRef` | `NSMutableData` | Mac OS X v10.0 |
| `CFMutableDictionaryRef` | `NSMutableDictionary` | Mac OS X v10.0 |
| `CFMutableSetRef` | `NSMutableSet` | Mac OS X v10.0 |
| `CFMutableStringRef` | `NSMutableString` | Mac OS X v10.0 |
| `CFNumberRef` | `NSNumber` | Mac OS X v10.0 |
| `CFReadStreamRef` | `NSInputStream` | Mac OS X v10.0 |
| `CFRunLoopTimerRef` | `NSTimer` | Mac OS X v10.0 |
| `CFSetRef` | `NSSet` | Mac OS X v10.0 |
| `CFStringRef` | `NSString` | Mac OS X v10.0 |
| `CFTimeZoneRef` | `NSTimeZone` | Mac OS X v10.0 |
| `CFURLRef` | `NSURL` | Mac OS X v10.0 |
| `CFWriteStreamRef` | `NSOutputStream` | Mac OS X v10.0 |

[Next](Using%20Carbon%20and%20Cocoa%20in%20the%20Same%20Application.md)[Previous](Preprocessing%20Mixed-Language%20Code.md)

