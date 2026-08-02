---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html
archived_at: '2026-07-15T07:22:26.690456Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Foundation Design Concepts](Introduction%20to%20Core%20Foundation%20Design%20Concepts.md)


[Next](Document%20Revision%20History.md)[Previous](Inspecting%20Objects.md)

# Toll-Free Bridged Types

There are a number of data types in the Core Foundation framework and the Foundation framework that can be used interchangeably. Data types that can be used interchangeably are also referred to as _toll-free bridged_ data types. This means that you can use the same data structure as the argument to a Core Foundation function call or as the receiver of an Objective-C message invocation. For example, `NSLocale` (see _[NSLocale Class Reference](https://developer.apple.com/documentation/foundation/nslocale)_) is interchangeable with its Core Foundation counterpart, CFLocale (see _[CFLocale Reference](https://developer.apple.com/documentation/corefoundation/cflocale)_).

Not all data types are toll-free bridged, even though their names might suggest that they are. For example, `NSRunLoop` is not toll-free bridged to CFRunLoop, `NSBundle` is not toll-free bridged to CFBundle, and `NSDateFormatter` is not toll-free bridged to CFDateFormatter. Table 1 provides a list of the data types that support toll-free bridging.

Through toll-free bridging, in a method where you see for example an `NSLocale *` parameter, you can pass a `CFLocaleRef`, and in a function where you see a `CFLocaleRef` parameter, you can pass an `NSLocale` instance. You also have to provide other information for the compiler: first, you have to cast one type to the other; in addition, you may have to indicate the object lifetime semantics.

The compiler understands Objective-C methods that return Core Foundation types and follow the historical Cocoa naming conventions (see _[Advanced Memory Management Programming Guide](../../Cocoa/Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_). For example, the compiler knows that, in iOS, the CGColor returned by the `CGColor` method of `UIColor` is not owned. You must still use an appropriate type cast, as illustrated by this example:

```
NSMutableArray *colors = [NSMutableArray arrayWithObject:(id)[[UIColor darkGrayColor] CGColor]];
[colors addObject:(id)[[UIColor lightGrayColor] CGColor]];
```

The compiler does not automatically manage the lifetimes of Core Foundation objects. You tell the compiler about the ownership semantics of objects using either a cast (defined in `objc/runtime.h`) or a Core Foundation-style macro (defined in `NSObject.h`):

- `__bridge` transfers a pointer between Objective-C and Core Foundation with no transfer of ownership.
- `__bridge_retained` or `CFBridgingRetain` casts an Objective-C pointer to a Core Foundation pointer and also transfers ownership to you.

  You are responsible for calling `CFRelease` or a related function to relinquish ownership of the object.
- `__bridge_transfer` or `CFBridgingRelease` moves a non-Objective-C pointer to Objective-C and also transfers ownership to ARC.

  ARC is responsible for relinquishing ownership of the object.

Some of these are shown in the following example:

```
NSLocale *gbNSLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_GB"];
CFLocaleRef gbCFLocale = (__bridge CFLocaleRef)gbNSLocale;
CFStringRef cfIdentifier = CFLocaleGetIdentifier(gbCFLocale);
NSLog(@"cfIdentifier: %@", (__bridge NSString *)cfIdentifier);
// Logs: "cfIdentifier: en_GB"

CFLocaleRef myCFLocale = CFLocaleCopyCurrent();
NSLocale *myNSLocale = (NSLocale *)CFBridgingRelease(myCFLocale);
NSString *nsIdentifier = [myNSLocale localeIdentifier];
CFShow((CFStringRef)[@"nsIdentifier: " stringByAppendingString:nsIdentifier]);
// Logs identifier for current locale
```

The next example shows the use of Core Foundation memory management functions where dictated by the Core Foundation memory management rules:

```objc
- (void)drawRect:(CGRect)rect {

    CGContextRef ctx = UIGraphicsGetCurrentContext();
    CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceGray();
    CGFloat locations[2] = {0.0, 1.0};
    NSMutableArray *colors = [NSMutableArray arrayWithObject:(id)[[UIColor darkGrayColor] CGColor]];
    [colors addObject:(id)[[UIColor lightGrayColor] CGColor]];
    CGGradientRef gradient = CGGradientCreateWithColors(colorSpace, (__bridge CFArrayRef)colors, locations);
    CGColorSpaceRelease(colorSpace);  // Release owned Core Foundation object.

    CGPoint startPoint = CGPointMake(0.0, 0.0);
    CGPoint endPoint = CGPointMake(CGRectGetMaxX(self.bounds), CGRectGetMaxY(self.bounds));
    CGContextDrawLinearGradient(ctx, gradient, startPoint, endPoint,
                                kCGGradientDrawsBeforeStartLocation | kCGGradientDrawsAfterEndLocation);
    CGGradientRelease(gradient);  // Release owned Core Foundation object.
}
```


Table 1 provides a list of the data types that are interchangeable between Core Foundation and Foundation. For each pair, the table also lists the version of OS X in which toll-free bridging between them became available.

__Table 1__  Data types that can be used interchangeably between Core Foundation and Foundation

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

[Next](Document%20Revision%20History.md)[Previous](Inspecting%20Objects.md)

