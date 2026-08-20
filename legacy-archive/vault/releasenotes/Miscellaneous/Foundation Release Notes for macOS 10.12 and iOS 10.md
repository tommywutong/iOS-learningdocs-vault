---
title: Foundation Release Notes for macOS 10.12 and iOS 10
apple_id: TP40017339
resource_type: Release Note
platform: iOS|macOS
topic: null
technology: Foundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/Miscellaneous/RN-Foundation-OSX10.12/index.html
archived_at: '2026-07-18T02:58:58.706900Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


Document Generated: 2016-06-08 09:51:56 -0700
macOS Release Notes Copyright © 2016 Apple Inc. All Rights Reserved.

# macOS 10.12 and iOS 10 Release Notes Cocoa Foundation Framework

The Foundation Framework is a library of APIs that provide the infrastructure for object-based applications with or without graphical user interfaces. It is available on macOS, iOS, tvOS, and watchOS. Parts of Foundation are also available in Swift Core Libraries, for other platforms.

These are the release notes for the WWDC 2016 developer seed of Foundation. Note that at this time these notes do not capture all of the changes.

Note that even though some APIs and descriptions refer to the APIs in Objective-C, and some others in Swift, in general all Foundation APIs are available in both Objective-C and Swift.

#### Overall API Updates

This release brings many continued API refinements to Foundation, taking advantage of new API features in Objective-C and enabling APIs to come across more naturally in Swift.

Some of the key API update areas include:
- Adoption of Swift 3 API design guidelines. Please refer to Swift Evolution document SE-0023, "API Design Guidelines."
- Value Types, where many Foundation classes are exposed as structs with value type semantics for Swift. This is described in Swift Evolution document SE-0069, "Mutability and Foundation Value Types."
- Introduction and adoption of string enumerations, with NS_STRING_ENUM and NS_EXTENSIBLE_STRING_ENUM.
- Introduction and adoption of NS_NOESCAPE to mark blocks whose execution completes before the API the block is passed in as an argument to.
- Dropping of "NS" prefix on certain Foundation classes and types, in both Swift and Objective-C.
- Continued fixes to nullability of values.
- Use of class properties, in both Swift as well as Objective-C, latter using the new "@property (class)" declaration.

The above topics and more will be covered during the following sessions at WWDC, which you can watch on videos at [Apple's Developer Site](https://developer.apple.com/):
- Swift API Design Guidelines
- What's New in Cocoa
- What's New in Foundation for Swift

We intend to do continued refinements to the API throughout upcoming seeds.

#### API Availability Macros

Foundation has switched to new availability macros for ObjC that enable much more flexibility in identifying each platform independently. These new macros are API_AVAILABLE, API_DEPRECATED, API_DEPRECATED_WITH_REPLACEMENT, and API_UNAVAILABLE. Sample use cases:

```
FOUNDATION_EXPORT NSURLResourceKey const NSURLCanonicalPathKey API_AVAILABLE(macosx(10.12), ios(10.0), watchos(3.0), tvos(10.0));
```

```objc
@property BOOL usesStrongWriteBarrier API_DEPRECATED("Garbage collection no longer supported",                                                          macosx(10.5, 10.12), ios(2.0, 10.0), watchos(2.0, 3.0), tvos(9.0, 10.0));
```

```
static const NSWindowStyleMask NSResizableWindowMask API_DEPRECATED_WITH_REPLACEMENT("NSWindowStyleMaskResizable",                                                          macosx(10.0, 10.12)) = NSWindowStyleMaskResizable;
```

#### Measurements and Units

This release brings a number of new APIs to Foundation that enable representing measured amounts. The primary APIs are:

NSUnit - The abstract superclass of units, such as miles, km/h, degrees Fahrenheit.

NSDimension - Subclass of NSUnit representing unit families, such as length, speed, temperature. This class has many subclasses such as NSUnitLength, representing the different unit families.

NSUnitConverter - Helper class to make it easy to convert between units in a unit value.

NSMeasurement - A unit and a value, representing a measured quantity. For instance 10 miles, 42 km/h, 72 degrees Fahrenheit.

NSMeasurementFormatter - A new formatter to display measurements in localized fashion.

#### NSISO8601DateFormatter

A new formatter to format and parse ISO8601 dates. By default uses RFC3339, but can be configured by setting various options.

#### NSDateInterval

A new class to represent a date interval. Used by NSDateIntervalFormatter.

#### NSURL

NSURL objects are immutable and must have a URL string. So, [NSURL init] makes no sense because there is no URL string supplied. In past versions of the OS, [NSURL init] released self and returned nil. However, to keep [NSURL init] from failing, [NSURL init] will now initialize the NSURL object with an empty string. This behavior change (obviously) also affects [NSURL new].

#### NSURLComponents

The NSURLComponents path and percentEncodedPath properties now return an empty path instead of nil.

#### NSPathUtilities

The NSPathUtilities pathExtension and stringByDeletingPathExtension properties now determine valid path extensions using the same logic as the rest of the OS. This may lead to small changes in behavior.

#### Property List Serialization

Now properly supports round tripping of +/- INF values.

Fixes -xml / -json decode to allow dot-escaping. In particular you should again be able to mutate deeply nested json/xml plists via plutil again.

Various crash fixes.

#### Deprecate GC NSPointerFunctions

The 'usesStrongWriteBarrier' and 'usesWeakReadAndWriteBarriers' properties have been deprecated.

#### -[NSFastEnumeration countByEnumeratingWithState:objects:count:]

Nullability is now correct for this API.

#### NSLog / CFLog

NSLog is now just a shim to os_log in most circumstances.

#### Array / Dictionary / OrderedSet / Set

Fix nullability of the C-array based designated initializers for all collections.

NSArray and NSDictionary now have high performance special-cased one-element instances.

Special case empty ranges in subarrayWithRange.

#### NSMutableArray

Performance improvements for creation and mutable copies, especially for internally contiguous arrays.

#### NSDictionary

Ensure that the sharedKey based dictionaries have reasonably performant -hash functions. Also, make sure that the sharedKey implementation works well on 64-bit platforms. Also make sharedKey based dictionaries fully support NSSecureCoding.

#### NSMutableDictionary

Detect and HALT on degenerate cases where we would otherwise infinite-loop during rehash. This should be very rare, we've only seen evidence of it happening once.

Fixed a few potential crashes.

#### NSFastEnumeration

Should once again be possible to fast-enumerate a given collection on multiple threads at the same time (please don't mutate on multiple threads though, there lies pain!)

#### NSKeyedUnarchiver

Ensure that the array of classes provided to -decodeObjectOfClasses:key: is actually an array of classes

Fix to ensure that we preserve the original exception stack trace during object decode.

Various performance improvements during decode. Also, numerous leak fixes during error/exception throws.

We now enforce the set-once-to-YES convention of setRequiresSecureCoding.

NSKeyedUnarchiver no longer uses mmap for the data in + (id)unarchiveObjectWithFile:(NSString \*)path.

#### NSMapTable

Fix potential infinite loop for certain kinds of input.

#### NSCache

When deallocating an NSCache, we no longer pass a moribund object to delegate -willEvictObject: call outs during -dealloc. Instead we now send out a special sentinel NSCache instance (to keep in spirit of nullability of the delegate).

#### NSRunLoop / CFRunLoop

Performance optimization for runloop-less threads when checking if a given run-loop is current. Prior to macOS v10.12 we'd create a RunLoop if it hadn't been before just to check if it was current. We now treat the non-existence of a run-loop as != without needing to create it.

Introduce new breakpoint function, _CFRunLoopError_MainThreadHasExited that can be used to help catch circumstances when work is being schedule on a main-runloop that will never run (for instance when running with dispatch_main, or other circumstances where you let the main thread exit).

#### CFSocket

Remove SOCK_SEQPACKET; Darwin platforms have never supported it.

#### CFMachPort

Greatly improved internal mechanism by which mach ports are cleaned up, should be more performant now, with less blocking threads/semaphore waits.

#### CFPasteboard

Various changes to support new continuity features, including new pasteboard subsystem: com.apple.CFPasteboard that can be useful to explore when debugging pasteboard related issues.

Various performance and crash fixes.

#### CoreFoundation <-> Foundation Bridging Performance

Many types in Foundation and CF are bridged such that they have a C interface exposed by CF, and an Objective-C class interface exposed by Foundation. In previous releases of macOS and iOS, which of these has better performance has been somewhat unintuitive, and has varied over the years. In macOS 10.12 and iOS 10.0, we’ve simplified this: the recommended API (Foundation) is also the fastest API in nearly all cases now.

In particular, places to re-evaluate performance tradeoffs in your code include:

• Creating arrays and dictionaries of Objective-C objects is significantly faster, especially for objects that don’t override the -retain and -release methods
• The speed of -retain, -release, -isEqual:, and -hash on CF types have improved to the point of actually being faster than the corresponding CF functions in most cases.
• Using NSArray/NSMutableArray methods to operate on objects created via CFArrayCreate\* on iOS is significantly faster now.
• The performance penalty for passing Objective-C objects to CF functions has been significantly reduced, and in some cases eliminated
• Objective-C collection literals now correctly special-case small and empty collections as the regular allocation methods do
• NSMutableDictionary’s memory footprint and performance have been improved vs CFMutableDictionaryRef
• NSDictionary’s memory usage was already significantly better than CFDictionaryRef’s, but it’s now further improved

Additionally, most methods and functions on the core collection and value types in both CF and Foundation are faster in general (rather than relative to each other), in some cases significantly so. As always, using performance tools such as Instruments is essential to making informed performance-related decisions about your code.

#### NSUserDefaults detects folder deletion

Deleting a folder of preferences (say, the container of an application you’re testing), should now correctly update the defaults system, rather than leaving it in an invalid and difficult to recover from state.

#### NSXMLParser fix with compatibility implications

When running in applications built using the 10.12 SDK, NSXMLParser will no longer artificially extend the lifetime of the ‘attributes’ dictionary passed to the -parser:didStartElement:namespaceURI:qualifiedName:attributes: method. This change reduces memory footprint significantly, but may cause incorrectly written applications to crash after switching to the new SDK and rebuilding. If you see a crash like this, make sure you’re keeping a strong reference to the attributes dictionary if you need to use it after the method returns.

#### Key-Value Observing is less sensitive to certain combinations of arguments

In OS X 10.11.0, And to a lesser extent in 10.6-10.10, certain combinations of arguments to the -addObserver:forKeyPath:withOptions:context: method could cause unusually bad performance. Many of these cases were fixed in 10.11.3, and all known remaining ones are fixed in 10.12. If you found that you needed to avoid NSKeyValueObservingOptionInitial, or avoid using particular context parameters, you can revisit those decisions.

#### Key-Value Observing and NSUserDefaults

In previous releases, KVO could only be used on the instance of NSUserDefaults returned by the +standardUserDefaults method. Additionally, changes from other processes (such as defaults(1), extensions, or other apps in an app group) were ignored by KVO. These limitations have both been corrected. Changes from other processes will be delivered asynchronously on the main queue, and ignore NSKeyValueObservingOptionPrior.

#### Key-Value Coding and weak properties

KVC now supports accessing weak object-typed properties correctly, as well as being somewhat faster.

#### -[NSUserDefaults registerDefaults:] and NSURLs

Calling -registerDefaults: with a dictionary containing NSURLs now encodes them the same way as -setURL:forKey:, so they’ll work properly with -URLForKey:.

#### WWDC Seed: Running multiple iOS simulators can cause NSUserDefaults to not work

Running an iOS 8 or 9 simulator followed by an iOS 10 simulator will cause NSUserDefaults to stop working in the simulator. This can be worked around by rebooting the host Mac.

#### -[NSLocale calendar] bug fix

The NSCalendar returned by -[NSLocale calendar] is now correctly copy-on-write and thread-safe, like NSCalendar instances created directly.

#### Localized String Formatting

Localized formatting of strings (localizedFormatWithString: and variants, as well as initWithFormat:locale: and CFStringCreateWithFormat() when a non-nil locale argument is provided) now surround %@ arguments with the Unicode isolate formatting characters FSI and PDI, if the resulting string contains any strong right-to-left characters. This addresses number of issues in the layout and display of text with mixed directionality.

Note that in the WWDC seed this happens all the time. In the next seed we intend to change this to happen only for applications linked against the latest SDKs.
