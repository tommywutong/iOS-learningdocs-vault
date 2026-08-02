---
title: Foundation Release Notes for iOS
apple_id: TP40011691
resource_type: Release Note
platform: watchOS|iOS
topic: null
technology: Foundation
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation-iOS/Foundation_iOS5.html
archived_at: '2026-07-18T02:50:30.988905Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


iOS Release Notes Copyright © 2011 Apple Inc. All Rights Reserved.

# iOS 5 Release Notes Foundation Framework

The Foundation Framework is a library of Objective-C classes that provide the infrastructure for object-based applications. It is available on Mac OS X and iOS.

#### Backward Compatibility

One backward compatibility mechanism that is occasionally used in the frameworks is to check for the version of the system an application was built against, and if an older system, modify the behavior to be more compatible. This is done in cases where bad incompatibility problems are predicted or discovered; and most of these are listed below in these notes.

Typically we detect where an application was built by looking at the version of the system frameworks the application was linked against. Thus, as a result of relinking your application on iOS 5, you might notice different behaviors, some of which might cause incompatibilities. In these cases because the application is being rebuilt, we expect you to address these issues at the same time as well. For this reason, if you are doing a small incremental update of your application to address a few bugs, it's usually best to continue building on the same build environment and libraries used originally.

In some cases, we provide defaults (preferences) settings which can be used to get the old or new behavior, independent of what system an application was built against. Often these preferences are provided for debugging purposes only; in some cases the preferences can be used to globally modify the behavior of an application by registering the values (do it somewhere very early, with -[NSUserDefaults registerDefaults:]).

#### JSON Support in Foundation

The new NSJSONSerialization class in Foundation has support for serializing Foundation objects to JSON and deserializing JSON into Foundation objects. Reading and writing from both data objects and streams is supported. Please see the NSJSONSerialization.h header for more information about the new class and methods.

#### NSValue objects with common structure types now support keyed archiving

An NSValue object with an NSPoint, NSRect, NSSize, NSRange, CGAffineTransform, NSEdgeInsets, or UIEdgeInsets structure type may now be archived and unarchived using NSKeyedArchiver. The value will only unarchive on iOS 5 or later.

#### New Availability Macros in Foundation headers

The header files for classes that are new in iOS 5 use a new macro, NS_CLASS_AVAILABLE(_MacOSIntro, _iOSIntro), to indicate the availability of the class. Classes decorated in this manner may be nil-checked for existence in future versions of Mac OS X or iOS, like this:

```
if ([NSNewClass class]) { /* ... */ }
```

Methods, functions, and exported values also use a new macro, NS_AVAILABLE(_MacOSIntro, _iOSIntro).

#### NSFilePresenter

iOS 5 includes a new mechanism that allows file presenters, which are objects that present the contents of files or directories to the user for viewing or editing, to take an active role in operations that access those files or directories, even operations performed by other processes in the system. It's an important part of the implementation of the iOS 5 modernized document model.

An application uses this mechanism by creating and registering a file presenter for each document file or file package whose contents is being presented to the user. When some other process uses the file coordination mechanism described in the next section to read from or write to the presented file system item, that coordinated reading or writing is made to wait while the file presenter is given a chance to do various things first. The set of things that a file presenter can do while coordinated reading and writing is made to wait is defined by the NSFilePresenter protocol, which is declared in <Foundation/NSFilePresenter.h>. You use this protocol in your application by instantiating classes that conform to it and registering those instances with the NSFileCoordinator class, which is introduced in the next section and declared in <Foundation/NSFileCoordinator.h>. See the comments in those files for details.

For example, in a typical "shoebox" application like iPhoto, which doesn't readily expose the notion of files to the user but nonetheless stores the user's data in files somewhere on the user's computer, you might make the class of the application delegate object conform to this protocol if the files are all in one directory tree. The application delegate would register itself as an NSFilePresenter in its -applicationWillFinishLaunching: method. If the files are in multiple directory trees then you would probably make some class of your own design conform to this protocol and instantiate it on the basis of one per directory tree, and each of those instances would be registered.

Every NSFilePresenter is responsible for keeping track of what file system item it's presenting, and providing a URL for it on command:

```objc
@property (readonly) NSURL *presentedItemURL;
```

When your application registers an NSFilePresenter it asserts "ownership" of the presented file or directory. Nothing else in the system that uses file coordination appropriately will be able to read from or write to the presented item without your NSFilePresenter being given the opportunity to prepare for the file access beforehand and notified of its completion afterward. There are two main methods your NSFilePresenter can implement to get that opportunity:

```objc
- (void)relinquishPresentedItemToReader:(void (^)(void (^reacquirer)(void)))reader;- (void)relinquishPresentedItemToWriter:(void (^)(void (^reacquirer)(void)))writer;
```

What sort of preparation needs to be done depends on the application. In particular, it depends on how strong of an ownership model your application requires. A very weak ownership model is possible if your application is able to use coordinated reading and writing for all of its access to the presented file or directory, instead of merely depending on other processes to do coordinated reading and writing.

Asserting ownership of a presented file or directory is just one of several reasons for an application to register a file presenter. For example, there's a method your NSFilePresenter can implement to be given the opportunity to make sure the presented file or directory is up to date before another process using coordinated reading reads from it:

```objc
- (void)savePresentedItemChangesWithCompletionHandler:(void (^)(NSError *errorOrNil))completionHandler;
```

NSFilePresenter has other methods. See the comments in <Foundation/NSFilePresenter.h> for details.

#### NSFileCoordinator

iOS 5 includes a new mechanism called file coordination. In addition to triggering work by file presenters, as described in the previous section and the comments in <Foundation/NSFilePresenter.h>, it allows your application to access files and directories in a way that is serialized with other process' access of the same files and directories so that inconsistencies due to overlapping reading and writing don't occur.

File coordination is performed by instances of the new NSFileCoordinator class. There are two main NSFileCoordinator methods:

```objc
- (void)coordinateReadingItemAtURL:(NSURL *)url                           options:(NSFileCoordinatorReadingOptions)options                             error:(NSError **)outError                        byAccessor:(void (^)(NSURL *newURL))reader;- (void)coordinateWritingItemAtURL:(NSURL *)url                           options:(NSFileCoordinatorWritingOptions)options                             error:(NSError **)outError                        byAccessor:(void (^)(NSURL *newURL))writer;
```

You use these methods by putting your application's reading or writing of some files and directories (definitely not all, more on this in below) in blocks and passing the blocks to invocations of these methods. Each time you invoke one of these methods it will synchronously wait if appropriate until other processes that also use NSFileCoordinator finish accessing the same file system item, and in some cases other file system items. Your block will be invoked. While your block is being invoked other processes that also use NSFileCoordinator and access the same file system item, and in some cases other file system items, will be made to wait. When your block returns, one or more of those other processes will stop waiting as appropriate. See the comments in <Foundation/NSFileCoordinator.h> for details.

Your application need not use file coordination when the serialization of its file access with other process' file access would not be useful. For example, there is typically no benefit to using file coordination for private cache and temporary files because typically there are no other processes with which your application must coordinate.

NSFileCoordinator is designed to accommodate the fact that files and directories may be moved or renamed while your process is waiting to access them; notice the NSURL that is passed to file accessor blocks. If your application renames a file while saving it then then your application must announce that it is doing so, using this NSFileCoordinator method:

```objc
- (void)itemAtURL:(NSURL *)oldURL didMoveToURL:(NSURL *)newURL;
```

The need to use this method is rare but arises, for example, in TextEdit when a file's name extension must be changed from .rtf to .rtfd because the user has added attachments to a rich text document and a different file format must be used for it.

NSFileCoordinator has other methods, and there are options you can choose to control coordinated reading and writing. See the comments in <Foundation/NSFileCoordinator.h> for details.

This mechanism is different from traditional BSD advisory file locking in that:
• It does not require that your application do everything it needs to do to a file for a particular user operation within one open()/flock()/reading or writing/close() sequence to enforce consistency. This is important in the context of a Cocoa Touch application because most Cocoa Touch methods deal in NSURLs, not file descriptors or even NSFileHandles.
• It has a few features that BSD advisory file locking does not have (and would not even be appropriate to put at that level). One important example of this is that coordinated reading of a file can actually trigger writing to that file by another process, while your reading waits, to help implement the iOS 5 modernized document model that is described in the AppKit release notes. Coordinated writing can also trigger actions in other processes, while your writer waits. These are described in the previous section.
• It takes file packages into account automatically.
• There is no equivalent of flock()'s LOCK_NB option or EWOULDBLOCK error code. This mechanism is for use when the file access is being commanded by a user and presenting the user with an error about an inability to take a lock would be unacceptably bad UI because that is such a technical concept.
• The methods we have published to expose this mechanism are structured so as to make it difficult for you to accidentally make other processes wait to access files longer than you intend. You don't lock and unlock, you do coordinated reading or writing, passing our methods blocks of code that do the reading or writing. When one of those blocks returns or throws an Objective-C exception, or your application crashes of course, your application definitely stops making other processes wait.

#### More Precise Removal of Key-Value Observers

Since the introduction of key-value observing (KVO), there have been methods to register and deregister one object as the observer of a keyed value in another, but the NSObject(NSKeyValueObserverRegistration) deregistration method, -removeObserver:forKeyPath:, suffered from the flaw of not allowing you to specify the same context pointer that you had passed to -addObserver:forKeyPath:options:context:. When the same observer is registered for the same key path multiple times, but with different context pointers each time, -removeObserver:forKeyPath: has to guess at the context pointer when deciding what exactly to remove, and it can guess wrong. This is particularly galling given our advice to check the context pointer when receiving a KVO notification to discriminate among different purposes for observing in the first place. A surprising and difficult to debug example of this is code in a subclass observing the same keyed value in the same object as code in a superclass.

To let you more precisely specify your intent when removing an observer a new NSObject(NSKeyValueObserverRegistration) method has been added in iOS 5:

```objc
- (void)removeObserver:(NSObject *)observer forKeyPath:(NSString *)keyPath context:(void *)context;
```

The same issue applies to batched key-value observer deregistration, so a new NSArray(NSKeyValueObserverRegistration) method has also been added:

```objc
- (void)removeObserver:(NSObject *)observer fromObjectsAtIndexes:(NSIndexSet *)indexes            forKeyPath:(NSString *)keyPath context:(void *)context;
```

#### Bug Fix in Key-Value Observing

In iOS 4 there was a bug in key-value observing in which one observer observing a key path like "commonObject.value" from two different objects, where the value for "commonObject" of the two objects was the same object, could cause a variety of crashes, exceptions, and malfunctions. Whether or not the bug actually manifested itself depended on a variety of factors, like the order of observer adding and removing and whether the context pointer for the two observations was the same. This bug has been fixed in iOS 5.

#### Improved Error Handling and Reporting in NSFileManager

Several changes have been made to NSFileManager in iOS 5 to improve error handling and reporting.

For applications linked on or after iOS 5, the delegate method -fileManager:shouldProceedAfterError:movingItemAtURL:toURL: will now be called when an item at the destination URL already exists. If the delegate returns YES, the operation will proceed, which will likely result in overwriting the item at the destination. Errors reported by NSFileManager's copy, move, remove, and link methods are now more consistent about returning NSErrors in the Cocoa error domain with POSIX domain underlying errors. NSFileManager's copy, move, and link methods now report errors with the new NSFileWriteFileExistsError Cocoa domain error code when the destination file already exists.

For applications linked on or after iOS 5, the delegate method -fileManager:shouldProceedAfterError:linkingItemAtURL:toURL: will now properly be called when NSFileManager encounters an error during a link operation. Before iOS 5, NSFileManager mistakingly called -fileManager:shouldProceedAfterError:copyingItemAtURL:toURL: instead.

#### New NSURL-based NSFileManager API

In iOS 4, many NSFileManager APIs were modified to take NSURLs as parameters instead of NSString paths to promote file system efficiency. In iOS 5, two additional methods now have NSURL-taking versions. The new methods are:

```objc
- (BOOL)createDirectoryAtURL:(NSURL *)url         withIntermediateDirectories:(BOOL)createIntermediates                          attributes:(NSDictionary *)attributes                               error:(NSError **)error;
```

```objc
- (BOOL)createSymbolicLinkAtURL:(NSURL *)url             withDestinationURL:(NSURL *)destURL                          error:(NSError **)error;
```

The semantics of these new methods are identical to their NSString-taking counterparts.

In order to create a relative symbolic link, the destinationURL should be created using [NSURL URLWithString:relativePath relativeToURL:nil].

Range Enumeration of NSIndexSet NSIndexSet is an abstraction of, as the name indicates, a set of indexes. It is also often used as a set of non-contiguous ranges. Before iOS 5, there was no API for accessing the ranges of indexes stored in an index set; ranges could only be accessed by using the index-based primitives. Since this is not trivial, iOS 5 has new convenience API for enumerating an NSIndexSet's non-contiguous ranges.

```objc
- (void)enumerateRangesUsingBlock:(void (^)(NSRange range, BOOL *stop))block;- (void)enumerateRangesWithOptions:(NSEnumerationOptions)opts usingBlock:(void (^)(NSRange range, BOOL *stop))block;- (void)enumerateRangesInRange:(NSRange)range options:(NSEnumerationOptions)opts usingBlock:(void (^)(NSRange range, BOOL *stop))block;
```

If the range passed into the last method intersects a range of the receiver's indexes, then that intersection will be passed to the block.

These methods are only guaranteed to perform as well as if they were implemented with -enumerateIndexesInRange:options:usingBlock:. However, if the receiver's implementation permits, it may perform better than that.

#### Safe File Mapping for NSData

Before iOS 5, specifying NSDataReadingMapped (or NSMappedRead) for -initWithContentsOfFile:options:error: would cause NSData to always attempt to map in the specified file. However, in some situations, mapping a file can be dangerous. For example, when NSData maps a file from a USB device or over the network the existence of said file can't be guaranteed for the lifetime of the object. Accessing the NSData's bytes after the mapped file disappears will likely cause unpredictable crashes in your application.

For applications linked on iOS 5 or later, NSDataReadingMapped will now only map the requested file if it can determine that mapping the file will be relatively safe. To reflect this change, NSDataReadingMapped has been deprecated and is now an alias for NSDataReadingMappedIfSafe.

The methods -dataWithContentsOfMappedFile: and -initWithContentsOfMappedFile: have been deprecated. In the very rare event that your application needs to map a file regardless of safety, you may use the NSDataReadingMappedAlways option.

#### More flexible version of NSIntegralRect

Foundation already provides NSIntegralRect, which takes a rectangle and pushes each edge outward to the nearest integer. For iOS 5 we add NSIntegralRectWithOptions, a version that gives you some control over how the rect is massaged into being integral.

Each edge of the rect or its width and height can be pushed inward, outward, or to the nearest integer.

#### NSUserDefaults and Threading

In earlier releases of iOS, NSUserDefaults (and CFPreferences) serialized all access; if you've been avoiding using the preferences system in heavily threaded apps due to contention, this should be greatly improved.

Additionally, automatic synchronization is now non-blocking in most cases. You should consider any calls to NSUserDefaults -synchronize carefully to see if they're really necessary, as you can avoid blocking IO by removing them.

#### NSProcessInfo Thread Safety

NSProcessInfo is now threadsafe. Additionally it now correctly protects its encapsulation; this may lead to different object lifetimes for the return values of -arguments, -environment, etc… If your code is following the normal Cocoa Touch memory management rules correctly, this won't matter for you.

#### NSXMLParser Stream API

NSXMLParser has a new method, -initWithStream:. This allows constructing an NSXMLParser that will parse data incrementally as it appears, rather than collecting all available data and then parsing it all at once. This can very significantly reduce the peak amount of memory used by the parser. -initWithContentsOfURL: has been modified to use streams internally when parsing file:// URLs.

#### NSXMLParser Thread Safety

NSXMLParser is now threadsafe. However, it is not reentrant on a given thread; don't call -parse on an NSXMLParser from within a delegate callback of another NSXMLParser.

#### NSXMLDocument External Entity Restriction API

External entities in XML files can be a security concern (see http://www.securityfocus.com/archive/1/297714/2002-10-27/2002-11-02/0 for an example). To mitigate this concern, NSXMLDocument has new API for controlling how external entities are loaded.

The following mutually exclusive options can be passed when creating the NSXMLDocument:

```
NSXMLNodeLoadExternalEntitiesAlways
```

    This is identical to the behavior in iOS 4 and earlier

```
NSXMLNodeLoadExternalEntitiesSameOriginOnly
```

    This only applies when a URL has been provided. It loads entities with target URLs that match the host, scheme, and port of the document URL.

```
NSXMLNodeLoadExternalEntitiesNever
```

    This disables loading external entities

If no options are specified, the system-default behavior is used. For applications linked on iOS 4 and earlier, this is NSXMLNodeLoadExternalEntitiesAlways. For applications linked on iOS 5 or later, all entities that don't require network access are loaded.

If an external entity fails to load, the document is invalid and the parse is aborted with an error. Since many uses of NSXMLDocument expect a small set of known external entities (DTDs being the most common), a new init method has been added that accepts an NSSet of URLs that always load regardless of the above options:

```objc
- (id)initWithData:(NSData *)data options:(NSUInteger)mask validExternalEntityURLs:(NSSet *)validURLs error:(NSError **)error;
```

#### NSBundle -bundlePath/-bundleURL fixes

For applications linked on iOS 5 or later, NSBundle now returns full paths for -bundlePath/-bundleURL even if the bundle was created with a relative path. Additionally, NSBundle no longer directly returns internal state from -bundlePath, which results in different object lifetimes for those return values. If your code is following the normal Cocoa Touch memory management rules correctly, this won't matter for you.

#### NSBundle App Store Receipt Support

NSBundle now has API for retrieving the URL to the location for the receipt file from the App Store:

```objc
- (NSURL *)appStoreReceiptURL;
```

This allows you to use the receipt file without hard-coding relative paths in your bundle. Note that this will always return a URL, even if the receipt file is not present.

#### NSFileHandle block-based readability/writeability API

NSFileHandle now has the following new API:

```objc
@property (copy) void (^readabilityHandler)(NSFileHandle *);@property (copy) void (^writeabilityHandler)(NSFileHandle *);
```

The handler blocks will be called when the underlying file descriptor for the NSFileHandle in question becomes readable or writeable respectively. They will be called on an implementation-defined queue, so if you need them to execute in a particular context you should arrange for them to do that (via dispatch_sync or similar). Note that as soon as the handler returns, it will be called again if the file descriptor being monitored continues to be writeable; so, if you only want to write once, you should set the writeabilityHandler to nil before returning from the block. To avoid retain cycles, handler blocks should access their associated NSFileHandle via their argument, not by capturing it.

#### NSRegularExpression

NSRegularExpression is a new class used to represent and apply regular expressions. An instance of this class is an immutable representation of a compiled regular expression pattern and various option flags. The pattern syntax currently supported is that specified by ICU (described at http://userguide.icu-project.org/strings/regexp). The supported options are as follows:

```
enum {   NSRegularExpressionCaseInsensitive            = 1 << 0, // Match letters in the pattern independent of case.   NSRegularExpressionAllowCommentsAndWhitespace = 1 << 1, // Ignore whitespace and #-prefixed comments in the pattern.   NSRegularExpressionIgnoreMetacharacters       = 1 << 2, // Treat the entire pattern as a literal string.   NSRegularExpressionDotMatchesLineSeparators   = 1 << 3, // Allow . to match any character, including line separators.   NSRegularExpressionAnchorsMatchLines          = 1 << 4, // Allow ^ and $ to match the start and end of lines.   NSRegularExpressionUseUnixLineSeparators      = 1 << 5, // Treat only \n as a line separator (otherwise, all standard                                                           //   line separators are used).   NSRegularExpressionUseUnicodeWordBoundaries   = 1 << 6  // Use Unicode TR#29 to specify word boundaries (otherwise,                                                           //   traditional regular expression word boundaries are used).};typedef NSUInteger NSRegularExpressionOptions;
```

The fundamental matching method on NSRegularExpression is a block iterator. There are several additional convenience methods, for returning all matches at once, the number of matches, the first match, or the range of the first match. Each match is specified by an instance of NSTextCheckingResult (of type NSTextCheckingTypeRegularExpression) in which the overall match range is given by the range property (equivalent to rangeAtIndex:0) and any capture group ranges are given by rangeAtIndex: for indexes from 1 to numberOfCaptureGroups. {NSNotFound, 0} is used if a particular capture group does not participate in the match. Note that some regular expressions may successfully match zero-length ranges, in which case the location of the range would be significant; this differs from the case of matching literal strings, in which a length of 0 would imply a failure to match. The options that may be supplied to matching methods are as follows:

```
enum {   NSMatchingReportProgress           = 1 << 0,  // Call the block periodically during long-running match operations.   NSMatchingReportCompletion         = 1 << 1,  // Call the block once after the completion of any matching.   NSMatchingAnchored                 = 1 << 2,  // Limit matches to those at the start of the search range.   NSMatchingWithTransparentBounds    = 1 << 3,  // Allow matching to look beyond the bounds of the search range.   NSMatchingWithoutAnchoringBounds   = 1 << 4   // Prevent ^ and $ from automatically matching the beginning and end of the search range.};typedef NSUInteger NSMatchingOptions;
```

By default, the block iterator method calls the block precisely once for each match, with a non-nil result and appropriate flags. The client may then stop the operation by setting the contents of stop to YES. If the NSMatchingReportProgress option is specified, the block will also be called periodically during long-running match operations, with nil result and NSMatchingProgress set in the flags, at which point the client may again stop the operation by setting the contents of stop to YES. If the NSMatchingReportCompletion option is specified, the block will be called once after matching is complete, with nil result and NSMatchingCompleted set in the flags, plus any additional relevant flags from among NSMatchingHitEnd, NSMatchingRequiredEnd, or NSMatchingInternalError. NSMatchingReportProgress and NSMatchingReportCompletion have no effect for methods other than the block iterator. The flags that may be passed to the block are as follows:

```
enum {   NSMatchingProgress      = 1 << 0,  // Set when the block is called to report progress during a long-running match operation.   NSMatchingCompleted     = 1 << 1,  // Set when the block is called after completion of any matching.   NSMatchingHitEnd        = 1 << 2,  // Set when the current match operation reached the end of the search range.   NSMatchingRequiredEnd   = 1 << 3,  // Set when the current match depended on the location of the end of the search range.   NSMatchingInternalError = 1 << 4   // Set when matching failed due to an internal error.};typedef NSUInteger NSMatchingFlags;
```

NSMatchingHitEnd is set in the flags passed to the block if the current match operation reached the end of the search range. NSMatchingRequiredEnd is set in the flags passed to the block if the current match depended on the location of the end of the search range. NSMatchingInternalError is set in the flags passed to the block if matching failed due to an internal error (such as an expression requiring exponential memory allocations) without examining the entire search range.

NSMatchingAnchored, NSMatchingWithTransparentBounds, and NSMatchingWithoutAnchoringBounds can apply to any match or replace method. If NSMatchingAnchored is specified, matches are limited to those at the start of the search range. If NSMatchingWithTransparentBounds is specified, matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc. If NSMatchingWithoutAnchoringBounds is specified, ^ and $ will not automatically match the beginning and end of the search range (but will still match the beginning and end of the entire string). NSMatchingWithTransparentBounds and NSMatchingWithoutAnchoringBounds have no effect if the search range covers the entire string.

NSRegularExpression is designed to be immutable and threadsafe, so that a single instance can be used in matching operations on multiple threads at once. However, the string on which it is operating should not be mutated during the course of a matching operation (whether from another thread or from within the block used in the iteration).

NSRegularExpression also provides find-and-replace methods for both immutable and mutable strings. The replacement is treated as a template, with $0 being replaced by the contents of the matched range, $1 by the contents of the first capture group, and so on. Additional digits beyond the maximum required to represent the number of capture groups will be treated as ordinary characters, as will a $ not followed by digits. Backslash will escape both $ and itself. For clients implementing their own replace functionality, there is also a method to perform the template substitution for a single result, given the string from which the result was matched, an offset to be added to the location of the result in the string (for example, in case modifications to the string moved the result since it was matched), and a replacement template.

#### Regular Expression Additions to NSString

In addition to the NSRegularExpression class, some convenience functionality has been added for using regular expressions with NSString directly. This takes the form of an additional option in NSStringCompareOptions, NSRegularExpressionSearch. The NSRegularExpressionSearch option applies only to methods of the form rangeOfString:..., stringByReplacingOccurrencesOfString:..., or replaceOccurrencesOfString:..., and it precludes all other options except for NSCaseInsensitiveSearch and NSAnchoredSearch.

The behavior is equivalent to that of NSRegularExpression with no options specified, except NSRegularExpressionCaseInsensitive (if NSCaseInsensitiveSearch is specified), or NSMatchingAnchored (if NSAnchoredSearch is specified). Note that some regular expressions may successfully match zero-length ranges, in which case the location of the range would be significant; this differs from the case of matching literal strings, in which a length of 0 would imply a failure to match.

In the stringByReplacingOccurrencesOfString:... and replaceOccurrencesOfString:... methods, the replacement string is treated as a template, as in the corresponding NSRegularExpression methods, with $0 being replaced by the contents of the matched range, $1 by the contents of the first capture group, and so on. +[NSRegularExpression escapedTemplateForString:] can be used to escape a string so that template characters will be treated literally.

#### NSDataDetector

NSDataDetector is a specialized subclass of NSRegularExpression. Instead of finding matches to regular expression patterns, it matches items identified by Data Detectors, such as dates, addresses, and URLs. The checkingTypes argument should contain one or more of the types NSTextCheckingTypeDate, NSTextCheckingTypeAddress, NSTextCheckingTypeLink, NSTextCheckingTypePhoneNumber, and NSTextCheckingTypeTransitInformation. The NSTextCheckingResult instances returned will be of the appropriate types from that list.

#### Additions to NSTextCheckingResult

As part of the effort to support NSRegularExpression and NSDataDetector, there are some additions to NSTextCheckingResult. First, there is a new type, NSTextCheckingTypeRegularExpression, used for regular expression results. Second, results may now optionally have additional ranges beyond the overall range they have always had. For this, there is a new property and method:

```objc
@property (readonly) NSUInteger numberOfRanges;- (NSRange)rangeAtIndex:(NSUInteger)idx;
```

The numberOfRanges should always be at least 1, and the rangeAtIndex:0 should always match the existing range property. NSTextCheckingTypeRegularExpression uses rangeAtIndex:n to represent the range corresponding to the nth capture group.

There is a new method

```objc
- (NSTextCheckingResult *)resultByAdjustingRangesWithOffset:(NSInteger)offset;
```

that allows clients to produce a result modified by offseting all of its ranges, for example to adjust for the offset of a substring within a larger string.

NSTextCheckingTypePhoneNumber and NSTextCheckingTypeTransitInformation are new types for NSTextCheckingResult, for use with NSDataDetector. These have associated with them new creation methods

```objc
+ (NSTextCheckingResult *)phoneNumberCheckingResultWithRange:(NSRange)range phoneNumber:(NSString *)phoneNumber;+ (NSTextCheckingResult *)transitInformationCheckingResultWithRange:(NSRange)range components:(NSDictionary *)components;
```

Phone number results have a property

```objc
@property (readonly) NSString *phoneNumber;
```

and transit information results have a property

```objc
@property (readonly) NSDictionary *components;
```

with keys currently NSTextCheckingAirlineKey and NSTextCheckingFlightKey for airline flight information. The old addressComponents property for address results is also being replaced by the new components property, although addressComponents will continue to work for compatibility.

#### NSLinguisticTagger

NSLinguisticTagger is a new class used to automatically segment natural-language text and tag it with information such as parts of speech. An instance of this class is assigned a string to tag, and clients can then obtain tags and ranges for tokens in that string appropriate to a given tag scheme.

A number of tag schemes are currently available: NSLinguisticTagSchemeTokenType, which is a tag scheme that classifies tokens according to their broad type: word, punctuation, whitespace, etc.; NSLinguisticTagSchemeLexicalClass, which classifies tokens according to class: part of speech for words, type of punctuation or whitespace, etc.; NSLinguisticTagSchemeNameType, which classifies tokens as to whether they are part of named entities of various types or not; NSLinguisticTagSchemeNameTypeOrLexicalClass, which follows NSLinguisticTagSchemeNameType for names, NSLinguisticTagSchemeLexicalClass for all other tokens; NSLinguisticTagSchemeLemma, which supplies a stem form for each word token (if known); NSLinguisticTagSchemeLanguage, which tags tokens according to their most likely language (if known); and NSLinguisticTagSchemeScript, which tags tokens according to their script. NSLinguisticTagSchemeTokenType, NSLinguisticTagSchemeLexicalClass, NSLinguisticTagSchemeNameType, and NSLinguisticTagSchemeNameTypeOrLexicalClass use tags from a specified list of string constants (clients may use == comparison). Tags for NSLinguisticTagSchemeLemma are lemmas from the language. Tags for NSLinguisticTagSchemeLanguage are standard language abbreviations. Tags for NSLinguisticTagSchemeScript are standard script abbreviations.

Not all languages can be handled by the tagger, and not all tag schemes are available for any given language. availableTagSchemesForLanguage: is provided for runtime determination of the schemes available for a particular language. The current languages for which parts-of-speech tagging is available are English, French, and German.

An instance of NSLinguisticTagger is created using initWithTagSchemes:options: with an array of tag schemes. The tagger will be able to supply tags corresponding to any of the schemes in this array. Once a string has been provided to the tagger using setString:, the tagger will segment the string as needed into sentences and tokens, and return those ranges along with a tag for any scheme in its array of tag schemes. The fundamental tagging method on NSLinguisticTagger is a block iterator, enumerateTagsInRange:scheme:options:usingBlock:, that iterates over all tokens intersecting a given range, supplying tags and ranges. There are several additional convenience methods, for obtaining a sentence range, information about a single token, or for obtaining information about all tokens intersecting a given range at once, in arrays.

Option flags are available that allow clients to control which types of tokens are returned in the results. By default all tokens will be returned, but if the options flag corresponding to omitting a given type is specified, then tokens of that general type (word, punctuation, whitespace, or other) will be omitted from the tokens returned in the results. For NSLinguisticTagSchemeNameType and NSLinguisticTagSchemeNameTypeOrLexicalClass, there is an option controlling whether a multi-word name will be returned as a single token, or as a separate token for each word of the name (the default).

If clients know the orthography for a given portion of the string, they may supply it to the tagger via setOrthography:range:. Otherwise, the tagger will infer the language from the contents of the text. If the string attached to the tagger is mutable, the client must inform the tagger whenever the string changes, via stringEditedInRange:changeInLength:. A given instance of NSLinguisticTagger should not be used from more than one thread simultaneously.

There are also some related convenience APIs on NSString. Clients wishing to analyze a given string once may use these NSString APIs without having to create an instance of NSLinguisticTagger. If more than one tagging operation is needed on a given string, it is more efficient to use an explicit NSLinguisticTagger instance.

#### NSURLConnection

The NSURLConnection class now has queue support, enabling delegate callbacks without requiring the running of a runloop.

This method supports performing asynchronous loading of URL requests where the results of the request are delivered to a block via an NSOperationQueue:

```objc
- (void)setDelegateQueue:(NSOperationQueue *)queue;
```

This is a convenience routine that allows for asynchronous loading of a URL-based resource.

```objc
+ (void)sendAsynchronousRequest:(NSURLRequest *)request              queue:(NSOperationQueue *)queue                completionHandler:(void (^)(NSURLResponse *, NSData *, NSError *))handler;
```

There is a new delegate method for NSURLConnection:

```objc
- (void)connection: (NSURLConnection *) connection        willSendRequestForAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge;
```

This new delegate combines the functionality of the existing three delegate methods didReceiveAuthenticationChallenge:, canAuthenticateAgainstProtectionSpace:, and connectionShouldUseCredentialStorage: . This delegate is always called when a challenge is given, even when credentials exist on the system that could be used to satisfy the current challenge. This gives the delegate the opportunity to validate the credentials being used (if any) and allow, deny, or provide alternate credentials for the current transaction.

If a delegate implements this new callback, the delegate callbacks didReceiveAuthenticationChallenge:, canAuthenticateAgainstProtectionSpace:, and connectionShouldUseCredentialStorage: will not be called.

In association to the new delegate callback on NSURLConnection, the protocol NSURLAuthenticationChallengeSender has been extended to include two new optional methods:

```
@optional- (void)performDefaultHandlingForAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge;- (void)rejectProtectionSpaceAndContinueWithChallenge:(NSURLAuthenticationChallenge *)challenge;
```

These two new protocol methods of NSURLAuthenticationChallengeSender allow implementors of NSURLConnection's delegate callback, willSendRequestForAuthenticationChallenge:, to direct NSURLConnection to perform default processing of the given authentication challenge. This allows NSURLConnection to handle new authentication protocols and delegates of NSURLConnection do not have to have special knowledge of the new authentication protocols. Additionally, calling rejectProtectionSpaceAndContinueWithChallenge: from willSendRequestForAuthenticationChallenge: will skip the current NSURLProtectionSpace included in the offered NSURLAuthenticationChallenge object. If another NSURLProtectionSpace exists for the NSURLAuthenticationChallenge, the willSendRequestForAuthenticationChallenge: will be called again with the new NSURLProtectionSpace in the offered challenge parameter. If there are no more NSURLProtectionSpace objects, NSURLConnection will treat this similar to calling cancel: on the challenge.

#### NSURLRequest

NSURLRequest has a new method for network service types:

```objc
- (NSURLRequestNetworkServiceType)networkServiceType;- (void)setNetworkServiceType:(NSURLRequestNetworkServiceType)networkServiceType;
```

Network Service Types provide the networking subsystems a hint as to the intended purpose of the request. The current list of network services types includes voice-control, voice-data, video, and background.

Support for HTTP pipelining has been added:

```objc
- (BOOL)HTTPShouldUsePipelining;- (void)setHTTPShouldUsePipelining:(BOOL)shouldUsePipelining;
```

HTTP Pipelining allows for the transmission of multiple concurrent HTTP requests without waiting for a response, which improves performance over high-latency networks.
Enabling pipelining is a hint which may be discarded when the server or proxy involved does not support pipelining.

#### NSHTTPCookieStorage

There is a new method

```objc
- (NSArray *)sortedCookiesUsingDescriptors:(NSArray *)sortOrder;
```

that avoids expensive string conversion and supports sorting the cookies based on a sort order. This method is preferred over the more generic:

```objc
- (NSArray *)cookies;
```

#### New collection class

There is a new collection class in Foundation, NSOrderedSet. An NSOrderedSet is an ordered collection, accessed by index, like an NSArray, but also offers NSSet-like operations.

NSOrderedSet has three primitives, two of which are the same as NSArray:

```objc
- (NSUInteger)count;- (id)objectAtIndex:(NSUInteger)idx;
```

and adds a third:

```objc
- (NSUInteger)indexOfObject:(id)object;
```

which is the basis of the Set operations. The latter returns the index of the given object, as you might guess. All of these [in a subclass] must be quick "constant time" operations for NSOrderedSet to perform well.

The -isEqual: method is the basis for object comparison (e.g., is an object in the ordered set or not). The -hash method must also be well-implemented on the objects put in an ordered set, and the hash/isEqual invariant maintained, since some ordered set implementations may wish to use hashing techniques to implement the primitives.

NSMutableOrderedSet has three additional primitives, which mostly act like NSMutableArray's primitives:

```objc
- (void)insertObject:(id)object atIndex:(NSUInteger)idx;- (void)replaceObjectAtIndex:(NSUInteger)idx withObject:(id)object;- (void)removeObjectAtIndex:(NSUInteger)idx;
```

The differences are that insertObject:atIndex: does nothing if a matching object is already in the NSMutableOrderedSet, and replaceObjectAtIndex:withObject: does nothing if a matching object is already in the ordered set at a different index.

The other available methods operate by using the primitives, of course, in a way that should seem to naturally follow from the behavior of the primitive.

There are two methods in NSOrderedSet that warrant special attention:

```objc
- (NSArray *)array;- (NSSet *)set;
```

These two methods return proxy or facade objects for the underlying ordered set, acting like, respectively, an immutable array or immutable set. These are useful in situations where you have an NSOrderedSet but need an NSArray to pass into some API. Note that these returned facades are not copies of the ordered set, and while you cannot change an ordered set through them, if the original ordered set is mutable, direct mutations to it will show through the facade objects and the "immutable" collection will appear to spontaneously be changing. The effect of apparent changes to those objects, to code which has received them, can be subtle. A simple example would be this:

```
[aMutableOrderedSet removeObjectsInArray:[aMutableOrderedSet array]]
```

Here, the array object given as parameter to removeObjectsInArray: will be changing while removeObjectsInArray: is iterating over it, possibly causing a crash or plain mis-behavior. The safer thing, when you know a mutable ordered set is the receiver of -array or -set, and you know it will be mutating further, is to make a copy of the ordered set into an array or set.

Currently the simplest way to make an NSArray from an NSOrderedSet is to copy the return value of -array:

```
[[anOrderedSet array] copy];
```

Currently the simplest way to make an NSSet from an NSOrderedSet is to copy the return value of -set:

```
[[anOrderedSet set] copy];
```

#### NSCalendar

The NSCalendar algorithms have several differences depending on which OS SDK version you build your app against. -rangeOfUnit:inUnit:forDate: can produce materially different results for iOS 2, 3, and 4/5. -ordinalityOfUnit:inUnit:forDate: can produce materially different results for iOS 2/3 and iOS 4/5. -dateFromComponents: can produce different results on iOS 5 than previously when working with Week units.

But of course, most of the algorithms can produce different results between OS releases, as bugs are fixed or changes made, either in Foundation or CoreFoundation or in libraries beneath them. The differences noted in the previous paragraph are the significant ones.

There are three new Week-related unit/component constants in NSCalendar:

NSWeekOfMonthCalendarUnit, NSWeekOfYearCalendarUnit, NSYearForWeekOfYearCalendarUnit

and the values of these quantities are week numbers or amounts relating to the month or the year that the week is in, and the year number for week-based interpretations of a calendar, such as the ISO 8601 calendar.

For many operations, there is no difference in meaning between NSWeekOfMonthCalendarUnit and NSWeekOfYearCalendarUnit, but for some there is a difference. Obviously getting the ordinality of a week with the month will usually give a different answer than the ordinality of the week within the year. The NSWeekCalendarUnit constant is not yet officially deprecated, but its use in new code is discouraged. It has a behavior like either NSWeekOfMonthCalendarUnit or NSWeekOfYearCalendarUnit, as the case may be, to give it behavior like it had prior to iOS 5.

#### iCloud

Foundation in iOS 5 includes APIs to enable applications to store configuration information and documents in the iCloud:

NSFileManager has APIs to put a document in the cloud or take it out, and to explicitly initiate a download.

NSMetadataQuery provides APIs to enumerate documents in the cloud.

NSURL has additional keys to query attributes of documents in the cloud, even if the documents have not yet been downloaded.

NSFileVersion enables querying information about different versions of a document, including those which had conflicts as a result of synchronizing changes from the cloud. Applications can use choose to do more sophisticated conflict resolution.

Finally, NSUbiquitousKeyValueStore allows saving configuration information in the cloud. This should typically be limited to small amount of data, such as high scores, user settings, etc.

#### Strings File Handling

In iOS 5, strings files in the system have been converted to binary property list format for performance reasons. It's rare for strings files to be accessed directly (without going through CF/NSBundle), and it's even less common for the system strings files to be accessed directly by third party applications; however, if they are, then they will no longer open properly if accessed with -[NSString propertyListFromStringsFileFormat] or -[NSString propertyList], which first require loading the file in as an NSString, the converting to a property list. Instead the APIs in NSPropertyListSerialization should be used to open strings files directly.

NSString methods -propertyList and -propertyListFromStringsFileFormat will be deprecated in a future release.
