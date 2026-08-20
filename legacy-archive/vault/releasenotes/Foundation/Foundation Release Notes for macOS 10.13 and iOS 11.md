---
title: Foundation Release Notes for macOS 10.13 and iOS 11
apple_id: TP30000742
resource_type: Release Note
platform: watchOS|tvOS|iOS|macOS
topic: null
technology: Foundation
published: '2017-06-22'
source_url: https://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation/index.html
archived_at: '2026-07-18T02:50:31.240656Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# macOS 10.13 and iOS 11 Release Notes Cocoa Foundation Framework

The Foundation framework is a library of APIs that provide the infrastructure for object-based applications with or without graphical user interfaces. It is available on macOS, iOS, tvOS, and watchOS. Parts of Foundation are also available in Swift Core Libraries, for other platforms.

Note that at this time these notes do not capture all of the changes.

Release notes for earlier versions of Foundation can be found [here](https://developer.apple.com/library/content/releasenotes/Foundation/RN-FoundationOlderNotes/index.html).

Note that even though some APIs and descriptions refer to the APIs in Objective-C, and some others in Swift, in general all Foundation APIs are available in both Objective-C and Swift. There are a number of Foundation APIs that are available in Swift as both a reference type that is bridged to its Objective-C counterpart, and value type. For instance, NSData and Data. In general, the value type is the more appropriate API to use in Swift, but in cases where it’s important to preserve bridging or reference behaviors, then the reference type can also be used instead.

#### Key Path and KVO Improvements in Swift

We now have a new Swift syntax for key paths, new types to represent them, and block-based key value observing. Please refer to WWDC 2017 session 212, “What’s New in Foundation,” for an in-depth discussion of these features.

#### Archiving in Swift

We have a new protocol, Codable, for archiving and unarchiving in Swift. It provides powerful archiving features for Swift types, and also enables automatic JSON encoding. Please refer to WWDC 2017 session 212, “What’s New in Foundation,” for an in-depth discussion.

#### NSDistributedNotificationCenter

Observers added to NSDistributedNotificationCenters will now be stored weakly similarly to the NSNotificationCenter storage. This behavior is conditional upon being linked to the latest Foundation. Previously compiled applications will not have this behavior.

#### NSMapTable

The function NSMapMember now appropriately handles null key and value parameters.

#### NSNumber

Bridging NSNumbers in swift to numeric types now uniformly limits the cases of as? cast no matter how the NSNumber was created. Casting NSNumbers to numeric types will return nil if the number cannot be safely represented as the target type.

```
let n = NSNumber(value: UInt32(543))let v = n as? UInt32// v is UInt32(543)
```

```swift
let v: UInt32 = 543let n = v as NSNumber// n == NSNumber(value: 543)
```

```
let n = NSNumber(value: UInt32(543))let v = n as? Int16// v is Int16(543)
```

```
// Failures when casting that losses the value storedlet n = NSNumber(value: UInt32(543))let v = n as? Int8// v is nil
```

#### NSOperation

NSOperation now responds to KVO and KVC for representing the finished, cancelled, executing and ready states as the strings @“finished”, @“cancelled”, @“executing” and @“ready” in addition to the older versions like @“isReady”.

NSOperation completionBlock now uniformly is set to nil upon completion of an operation to avoid circular references to operations.

#### NSOperationQueue

NSOperationQueue will no longer create a serial backing dispatch queue for each operation. Instead it now shares a single concurrent dispatch queue.

Quality of service for NSOperations when enqueued to an operation will no longer be calculated in advance, instead the quality of service for an operation is only applied if it is requested upon the execution of an operation. If a NSOperationQueue specifies a quality of service, the backing dispatch queue will have that specified quality of service. Any operations run upon that queue will inherit the effective quality of service if they do not have a quality of service specified. However if an NSOperation has a quality of service specified it will enforce that quality of service when running upon the NSOperationQueue’s backing dispatch queue.

Quality of service overrides now only apply when waiting for operations to finish. This means that the work done to calculate the effective quality of service is not paid up-front but instead calculated when waiting is invoked.

NSOperationQueueDefaultMaxConcurrentOperationCount should no longer hit thread exhaustion states.

#### NSTask

NSTask now has two new methods to allow for launching processes and returning an error instead of throwing an exception. Additionally the executable path is now exposed as a NSURL via the property executableURL and the current working directory for launching is exposed as a NSURL via currentDirectoryURL.

#### NSThread

Setting the stack size for NSThreads will now raise an invalid argument exception when the stack size is not appropriate.

#### NSRange

NSRange in Swift conforms to Equatable, Hashable and CustomStringConvertible.

```
let ranges = Set<NSRange>([NSRange(location: 4, length: 10), NSRange(location: 2, length: 3)])print(ranges) // prints [{4, 10}, {2, 3}]
```

#### NSXPCConnection support for discrete NSProgress

In order to provide an easier and more discoverable solution for updating progress over an NSXPCConnection, void will no longer be the only allowed return type. NSProgress \* will now also work:

```objc
@protocol ServerProtocol// This is a traditional callback- (void)remoteCallWithReply:(void (^)(BOOL success))reply;
```

```
// This is the newly allowed style- (NSProgress *)remoteCallWithProgressAndReply:(void (^)(BOOL success))reply;@end
```

On the caller side, they simply compose the result NSProgress \* into their tree using the existing NSProgress API.

When a call is made to the proxy using a selector that returns NSProgress, NSXPCConnection will create a local stand-in for the remote side and return it. The call does not become synchronous.

Only methods which have a reply block are allowed to return NSProgress \*.

On the remote side, when the called method returns an NSProgress, NSXPCConnection will hook the result up to the progress object it handed out on the local side of the connection.

The following example shows a simple use case.

Shared Code

```objc
@protocol ProgressReportingService <NSObject>- (NSProgress *)performRequestWithReply:(void (^)(BOOL success))reply;@end
```

Server Code

```objc
- (NSProgress *)performRequestWithReply:(void (^)(BOOL))reply {    NSProgress * progress = [NSProgress progressWithTotalUnitCount:30];    dispatch_async(dispatch_get_global_queue(0, 0), ^{        progress.completedUnitCount = 10;        usleep(100000);        progress.completedUnitCount = 20;        usleep(100000);        progress.completedUnitCount = 30;        usleep(100000);        reply(YES);    });    return progress;}
```

Client Code

```objc
- (void)callRequest {    NSProgress *localProgress = [[NSProgress alloc] init];    localProgress.totalUnitCount = 1;
```

```
    id proxy = [_connection remoteObjectProxy];    NSProgress *remoteProgress = [proxy performRequestWithReply:^(BOOL success) {        /* Operation is finished here */    }];    [localProgress addChild:remoteProgress withPendingUnitCount:1];
```

```
    // At this point, localProgress will update as remoteProgress is updated. You may observe it as usual.}
```

#### NSLinguisticTagger

NSLinguisticTagger now has the notion of a unit, which may be word, sentence, paragraph, or the entire document, as represented by NSLinguisticTaggerUnit.  A number of APIs now have variants which take a unit, allowing certain types of tagging (such as language) to be performed at the word, sentence, paragraph, or document level.  Not all types of tagging are available for all units, and +availableTagSchemesForUnit:language: can be used to determine which tag schemes are available for a given unit and language.

The -dominantLanguage and +dominantLanguageForString: methods are also available as a convenience, the equivalent of the language scheme as applied to the document unit.  These are the preferred methods for determining the language of a string as a whole.

For Swift 4, NSLinguisticTagScheme and NSLinguisticTag have become named types rather than strings, and the methods that take them have been adjusted appropriately.

#### NSOrthography

NSOrthography has a new method, +defaultOrthographyForLanguage:, designed to make it easier to construct an NSOrthography instance, given only a single dominant language.  This method will pick a default script for the specified language and construct an NSOrthography instance based on that.

#### NSRegularExpression/NSTextCheckingResult

The regular expression syntax used by NSRegularExpression supports named capture groups, and there is now support for that in the API via a new rangeWithName: method on NSTextCheckingResult.

For Swift 4, the keys for NSTextCheckingResult component dictionaries have been converted from strings into a named type.  The Swift 4 naming of some NSTextCheckingResult methods has also been adjusted slightly to conform to standard conventions.

#### NSURL

NSURL has the following new volume resource property keys:

```
NSURLVolumeSupportsImmutableFilesKeyNSURLVolumeSupportsAccessPermissionsKeyNSURLVolumeAvailableCapacityForImportantUsageKeyNSURLVolumeAvailableCapacityForOpportunisticUsageKey
```

Please refer to NSURL.h for more info on these.

NSURLLocalizedNameKey now correctly handles filenames containing Right-To-Left characters (such as Arabic or Hebrew letters) by inserting the appropriate Unicode control characters.

#### NSURLComponents

The hash method is now correctly implemented, so NSURLComponent objects may now be used as dictionary keys.

The percentEncodedQueryItems property was added. This allows callers to get NSURLQueryItem name-value pairs with all percent-encoding intact, and to set NSURLQueryItem name-value pairs with additional characters percent-encoded (characters that are not required to be percent-encoded in the URL query component).

#### NSURLSession Adaptable Connectivity API

New in macOS, iOS, watchOS, and tvOS is URLSession Adaptable Connectivity API. This API enables URLSession clients to have tasks automatically monitor and wait for satisfactory network connectivity, rather than immediately failing with an error when connectivity is unsatisfactory. This simplifies developer adoption of networking functionality by mitigating the need to manually monitor network conditions and retry requests.

This new functionality is made available through the ‘waitsForConnectivity’ URLSessionConfiguration property and the ‘URLSession:taskIsWaitingForConnectivity:’ method of the URLSessionTaskDelegate protocol. Further details can be found in the NSURLSession.h header of the Foundation project.

#### NSURLSession ProgressReporting

New in macOS, iOS, watchOS, and tvOS is URLSessionTask adoption of the ProgressReporting protocol.

It provides a platform API consistent mechanism for URLSession clients to track the progress of URLSessionTask that allows all clients of URLSessionTask to provide a consistent and meaningful measure of progress for a given task.

URLSessionTask implements a new ‘progress’ property of Progress type to make this new functionality available.

#### NSURLSession brotli support

New in macOS, iOS, watchOS, and tvOS is URLSession support for HTTP brotli content encoding (). HTTP requests by default will contain a “br” value (in addition to gzip and deflate) for the “Accept-Encoding” HTTP header; this informs the web server that the user agent supports brotli encoding. The web server can send an HTTP body with “Content-Encoding: br” HTTP header to indicate that the content is brotli-encoded. URLSession will automatically decompress the HTTP body data — passing the decoded data back to the client in didReceiveData delegate callbacks or via a Data object for the convenience URLSession APIs — just like it does for “Content-Encoding: gzip” content.

For binary compatibility reasons, URLSession brotli support is enabled only for apps linked against the macOS 10.13 / iOS 11 SDKs and later.

#### NSURLSessionTask Scheduling API

New in macOS, iOS, watchOS, and tvOS is URLSessionTask Scheduling API. This API allows background URLSession clients to schedule tasks in the future, enabling easy background app refresh semantics for apps, watchOS complications, and more. The API also allows developers to update requests before transmission to address cases where the request has become stale when scheduled in the future.

The new API is expressed by three URLSessionTask properties: ‘earliestBeginDate’, ‘countOfBytesClientExpectsToSend’, and ‘countOfBytesClientExpectsToReceive’ and a new method for the URLSessionTaskDelegate protocol, ‘URLSession:task:willBeginDelayedRequest:completionHandler’. Further details can be found in the NSURLSession.h header of the Foundation project.

#### NSURLSessionStreamTask proxy support

New in macOS, iOS, and tvOS is URLSessionStreamTask support for HTTPS proxies requiring authentication. Currently there is a known issue where reads and writes on a secure connection through an HTTPS proxy will hang. However, proxy support for non-secure endpoints is currently supported for apps linked against the macOS 10.13 / iOS 11 SDKs and later.

#### Collection Copy-on-Write

NSArray, NSDictionary, and NSSet now implement “copy on write” (CoW), which means that a copy of a mutable instance will often not be a full copy, but a much cheaper, O(1) operation. A full copy is done only when either one of the objects (the original or the copy) is mutated down the line.

Please see WWDC 2017 session 244 “Efficient Interactions with Frameworks” for more info on this.

#### Collection conveniences

NSArray and NSDictionary have new APIs for more convenient reading/writing with an NSError return. The writing is performed atomically:

NSArray:

```objc
- (BOOL)writeToURL:(NSURL *)url error:(NSError **)error;- (nullable NSArray<ObjectType> *)initWithContentsOfURL:(NSURL *)url error:(NSError **)error;+ (nullable NSArray<ObjectType> *)arrayWithContentsOfURL:(NSURL *)url error:(NSError **)error;
```

NSDictionary:

```objc
- (BOOL)writeToURL:(NSURL *)url error:(NSError **)error;- (nullable NSDictionary<NSString *, ObjectType> *)initWithContentsOfURL:(NSURL *)url error:(NSError **)error;+ (nullable NSDictionary<NSString *, ObjectType> *)dictionaryWithContentsOfURL:(NSURL *)url error:(NSError **)error;
```

#### Collection getObjects: APIs

-[NSArray getObjects:] and -[NSDictionary getObjects:andKeys:] are now hard-deprecated. Use the variants that take range or count arguments.

#### NSJSONSerialization

NSJSONSerialization now encodes and decodes a wider range of numbers. Although the JSON spec allows any JSON parsing implementation to place limits on the range and representation of the numbers it parses, NSJSONSerialization should now be able to encode and decode the full range of numbers representable by native floats and doubles, as well as numbers representable by NSDecimalNumber.

NSJSONSerialization also offers a new NSJSONWritingSortedKeys option to sort object keys alphabetically for more human-readable output.

#### plutil

plutil -p now sorts property list dictionary keys alphabetically for more human-readable output.

#### Relaxed Key-Value Observing Unregistration Requirements

Prior to 10.13, KVO would throw an exception if any observers were still registered after an autonotifying object's -dealloc finished running. Additionally, if all observers were removed, but some were removed from another thread during dealloc, the exception would incorrectly still be thrown. This requirement has been relaxed in 10.13, subject to two conditions:

• The object must be using KVO autonotifying, rather than manually calling -will and -didChangeValueForKey: (i.e. it should not return NO from +automaticallyNotifiesObserversForKey:)
• The object must not override the (private) accessors for internal KVO state

If all of these are true, any remaining observers after -dealloc returns will be cleaned up by KVO; this is also somewhat more efficient than repeatedly calling -removeObserver methods.

#### NSUserDefaults KVO improvements (New since Seed 1)

Starting in iOS 9.3, and in subsequent releases of iOS and macOS, key-value observation of NSUserDefaults would deliver notifications asynchronously. This had several downsides including poor -registerDefaults: performance, and compatibility issues with some apps, so has now been scaled back to only delivering notifications of changes from other processes asynchronously. Changes within a process are now delivered synchronously as they were in older versions of the OS. This should also correct duplicate notifications of some changes being delivered to observers.

#### NSUserDefaults Data Loss Fix

Starting in iOS 9.3, and in subsequent releases of iOS and macOS, NSUserDefaults could fail to load data if more than roughly 250 separate apps (including separate reinstalls of the same app) had been launched since the last reboot. This has been corrected.

#### NSFileHandle readabilityHandler Behavior Change

For applications linked using the latest SDK, NSFileHandle will now correctly call its readabilityHandler when a file handle is readable but has zero bytes to read.

#### NSPropertyListSerialization Old-Style Property List Memory Use Reduction (New since Seed 1)

Parsing NeXT-style plists uses roughly half as much memory as in earlier releases.

#### Swift KeyPath Adoption in Foundation APIs

Several Foundation methods (including KVO) now have versions that take the new Swift KeyPaths, for improved type safety and usability.

#### Improved NSUserDefaults Handling of Invalid Files

In earlier versions, if an NSUserDefaults/CFPreferences backing plist file was replaced with a file that was not a valid property list with a dictionary as its root key, it could cause various problems. NSUserDefaults now detects this and deletes the invalid file to recover.

#### Improved Handling of Mis-nested Key-Value Observing Calls

When a KVO callout caused another KVO callout, and the willChange/didChange calls were incorrectly nested, a variety of problems could happen including crashes and bugs in seemingly unrelated code. This has been corrected, though it's still recommended that you avoid getting into this situation.

#### CFLocaleCopyCurrent() Concurrency Improvements

Calling CFLocaleCopyCurrent() on many threads at once (for example, searching many NSStrings in parallel, when passing NULL for the locale) is dramatically faster.

#### UserDefaults nil Handling Fix

Setting a default to nil in Swift, or calling -setURL: nil forKey: … in Objective-C would fail to remove the previous value. This has been corrected.

#### NSXMLParser Invalid Data Handling Improvement

XML documents with a UTF-8 byte-order mark embedded in an attribute name could cause crashes. This has been fixed.

#### NSXMLDocument xmlns + NSXMLNodePreservePrefixes Fix

Specifying NSXMLNodePreservePrefixes on a document with an xmlns attribute could omit the closing `"` when creating an XML string. This has been corrected.

#### NSError

NSError now has a new key, NSLocalizedFailureErrorKey. The value for this userInfo key captures what failed as a complete sentence, but not why. This is meant for being specified by a higher level API that returns a CF/NSError from a lower level API, allowing the higher level to customize the what went wrong while keeping the failure reason intact. This should be a complete sentence, including period at the end of the sentence (for localizations where that makes sense).

As an example, for Foundation error code NSFileWriteOutOfSpaceError, setting the value of this key to "The image library could not be saved." will allow the localizedDescription of the error to come out as "The image library could not be saved. The volume Macintosh HD is out of space." rather than the default (say) “You can't save the file ImgDatabaseV2 because the volume Macintosh HD is out of space."

As a clarification, here are the steps taken by NSError.localizedDescription to compute the its value:

 1. Look for NSLocalizedDescriptionKey in userInfo, use value as-is if present. This allows the localizedDescription of any error to be easily customized by an app for presentation.
 2. Look for NSLocalizedFailureErrorKey in userInfo. If present, use, combining with value for NSLocalizedFailureReasonErrorKey if available. This allows an app to customize the operation that failed while keeping the failure reason provided by lower level intact, as described above.
 3. Fetch NSLocalizedDescriptionKey from userInfoValueProvider, use value as-is if present. This is done after step 2 to allow the userInfo entry for NSLocalizedFailureErrorKey to take precedence.
 4. Fetch NSLocalizedFailureErrorKey from userInfoValueProvider. If present, use, combining with value for NSLocalizedFailureReasonErrorKey if available.
 5. Look for NSLocalizedFailureReasonErrorKey in userInfo or from userInfoValueProvider; combine with generic "Operation failed" message.
 6. Last resort localized but barely-presentable string manufactured from domain and code. The result is never nil.

Given this, an error producer can either provide a value for NSLocalizedDescriptionKey or values for NSLocalizedFailureErrorKey and NSLocalizedFailureReasonErrorKey. Just NSLocalizedDescriptionKey by itself allows more flexibility in the language of the message; the other two enable more customizability in the final output, but the results are simply appended and appear as two distinct sentences.

Higher level API that gets an NSError and passes it on for possible presentation can set either the NSLocalizedDescriptionKey or NSLocalizedFailureErrorKey to customize the error message.

Release Notes Copyright © 2017 Apple Inc. All Rights Reserved.
