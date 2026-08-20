---
title: Foundation Release Notes for OS X v10.10 and iOS v8
apple_id: TP40016679
resource_type: Release Note
platform: iOS|macOS
topic: null
technology: Foundation
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation-v10.10/index.html
archived_at: '2026-07-18T02:50:31.170189Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


Document Generated: 2014-06-05 12:26:27 -0700
OS X Release Notes Copyright © 2014 Apple Inc. All Rights Reserved.

# OS X 10.10 Release Notes Cocoa Foundation Framework

The Foundation Framework is a library of Objective-C classes that provide the infrastructure for object-based applications with or without graphical user interfaces. It is available on OS X and iOS.

You can find release notes for the Application Kit as well as some notes on general backward compatibility issues, version handling, etc, [here](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation-v10.10/AppKit.html).

These notes cover many, but by no means all of the changes in the Foundation Kit in OS X 10.10.

#### Some of the major topics covered in this document:

- [Swift](#apple-geyf6mjqkn3wsztu)
- [NSString encoding detection](#apple-geyf6mjqkn2he2lom5cw4y3pmruw4z2emv2gky3unfxw4)
- [NSFormatter](#apple-geyf6mjqizxxe3lbor2gk4tt)
- [NSXPCConnection progress reporting](#apple-geyf6mjqjzjvqucd)
- [NSFileCoordinator](#apple-geyf6mjqizuwyzkdn5xxezdjnzqxi33s)
- [iCloud Document Storage](#apple-geyf6mjqnfbwy33vmq)
- [NSUserDefaults](#apple-geyf6mjqkvzwk4semvtgc5lmorzq)
- [Quality of Service](#apple-geyf6mjqkfxvg)

#### Swift

Swift is a new programming language for Cocoa and Cocoa Touch that provides many innovative features while also seamlessly operating with Cocoa APIs and Objective-C. You can find documentation, release notes, and other resources for Swift development on the Apple developer website.

Some items of note regarding the interaction of Swift with existing Cocoa APIs:

• Instance methods in Cocoa APIs come across to Swift pretty much as-is. A method such as:

```objc
- (BOOL)setResourceValue:(id)value forKey:(NSString *)key error:(NSError **)error;
```

in Swift looks like:

```swift
func setResourceValue(value:AnyObject?, forKey key:String?, error:NSErrorPointer) -> Bool
```

The first part of the Objective-C name appears as the first part of the Swift name, outside the parens, and the labels on the second and subsequent arguments appear as labels in Swift as well.

In both cases, "value" and "key" are simply the names of the local variable corresponding to the first and second arguments, and are not part of the method name.

Important to note that the Swift name of such a method includes the labels, so the name of such a method would be read as in ObjC, as "setResourceValue forKey error", not "setResourceValue." Removing the names of the arguments, the method signature is:

```swift
func setResourceValue(AnyObject?, forKey:String?, error:NSErrorPointer) -> Bool
```

So basically Objective-C instance method names are exposed automatically and without any changes in Swift.

init methods are also exposed automatically, but there is a mapping: Both init methods and convenience constructors are exposed in Swift as constructors. In such cases if present, "with" is dropped, and all the arguments, including the first one, have an explicit label. So a method such as:

```objc
- (instancetype)initWithTimeIntervalSinceNow:(NSTimeInterval)secs;
```

is exposed as:

```
convenience init(timeIntervalSinceNow secs: NSTimeInterval)
```

and the same thing happens with a convenience constructor such as:

```objc
+ (NSColor *)colorWithPatternImage:(NSImage *)image;
```

which appears as:

```
init(patternImage image: NSImage?)
```

• As you can see in the above examples, some Objective-C Cocoa types are mapped to their Swift counterparts, such as NSString/String above. Also note that by-ref NSError return arguments (NSError \*\*) appear as NSErrorPointer in Swift. id appears in Swift as AnyObject, and NSArray appears as AnyObject[]. NSInteger is mapped to Int, and in most cases so is NSUInteger.

• Cocoa structs such as NSRange and NSSize are available to Swift with custom constructors, such as:

```
let size = NSSize(width: 20, height: 40)
```

• To localize strings in your applications you can use the NSLocalizedString(key:tableName:bundle:value:comment:) function. This function provides default values for the tableName, bundle, and value arguments, so you can use it in a variety of forms, shortest being:

```
result = NSLocalizedString("Update", comment:"Title of button the user can click to update account info")
```

• Enums in Cocoa which follow the "common prefix" naming guideline (which applies to the more recent enums) appear in Swift with the common prefix removed. For instance:

```
typedef NS_ENUM(NSInteger, NSByteCountFormatterCountStyle) {    NSByteCountFormatterCountStyleFile,    NSByteCountFormatterCountStyleMemory,    NSByteCountFormatterCountStyleDecimal,    NSByteCountFormatterCountStyleBinary};
```

is exposed in Swift as:

```
enum NSByteCountFormatterCountStyle : Int {    case File    case Memory    case Decimal    case Binary}
```

and you can refer to the individual values as NSByteCountFormatterCountStyle.File or just .File in appropriate contexts.

• Objective-C selectors appear using the Selector type in Swift. You can construct a selector with a string literal, such as

```swift
let action: Selector = "updateAccountInfo:"
```


#### String Encoding Detection

NSString has added an API that can be used to detect the string encoding of an array of bytes. The API is:

```objc
+ (NSStringEncoding)stringEncodingForData:(NSData *)data                          encodingOptions:(NSDictionary *)opts                          convertedString:(NSString **)string                      usedLossyConversion:(BOOL *)usedLossyConversion;
```

This API is used to detect the string encoding of a given raw data. It can also do lossy string conversion. It converts the data to a string in the detected string encoding. The data object contains the raw bytes, and the option dictionary contains the hints and parameters for the analysis. The opts dictionary can be nil. If the string parameter is not NULL, the string created by the detected string encoding is returned. The lossy substitution string is emitted in the output string for characters that could not be converted when lossy conversion is enabled. The usedLossyConversion indicates if there is any lossy conversion in the resulted string. If no encoding can be detected, 0 is returned.

The possible key for the option dictionary and their values are:

• Key: NSStringEncodingDetectionSuggestedEncodingsKey; Value: an array of suggested string encodings (without specifying the 3rd option in this list, all string encodings are considered but the ones in the array will have a higher preference; moreover, the order of the encodings in the array is important: the first encoding has a higher preference than the second one in the array)
• Key: NSStringEncodingDetectionDisallowedEncodingsKey; Value: an array of string encodings not to use (the string encodings in this list will not be considered at all)
• Key: NSStringEncodingDetectionUseOnlySuggestedEncodingsKey; Value: a boolean option indicating whether only the suggested string encodings are consider
• Key: NSStringEncodingDetectionAllowLossyKey; Value: a boolean option indicating whether lossy is allowed
• Key: NSStringEncodingDetectionFromWindowsKey; Value: an option that gives a specific string to substitute for mystery bytes
• Key: NSStringEncodingDetectionLossySubstitutionKey; Value: the current user’s language
• Key: NSStringEncodingDetectionLikelyLanguageKey; Value: a boolean option indicating whether the data is generated by Windows

If the values in the dictionary have wrong types (for example, the value of NSStringEncodingDetectionSuggestedEncodingsKey is not an array), an exception is throw. If the values in the dictionary are unknown, (for example, the value in the array of suggested string encodings is not a valid encoding), the values will be ignored.

If the string encoding is known, +[NSString initWithData:encoding:] should be used to create the string. Use this new API to create a string only if the string encoding is unknown or lossy conversion is needed.

#### Date Interval Formatter

NSDateIntervalFormatter has been added in 10.10. It is used to format a date interval in a locale-sensitive way. A date interval is defined by two dates, for example, Sept 1st, 2013 - Oct 1st, 2013. In different countries and different regions, people use different languages and different formats to express a date interval. NSDateIntervalFormatter is designed to fulfill the need that we can easily format a date interval into a localized string.

NSDateIntervalFormatter is a subclass of NSFormatter. However, it does not support parsing. In addition, NSDateIntervalFormatter requires two objects to work on, so the base methods in NSFormatter such as stringForObjectValue: do not apply.

There is a single method in NSDateIntervalFormatter: -stringFromData:toDate:. How the dates are formatted is controlled by either the dateTemplate property or the dateStyle and timeStyle properties (just like NSDateFormatter). The dateTemplate property is different from the dateFormat property in NSDateFormatter. The position information of each unit in dateTemplate is ignored, and the value of the dateTemplate may be changed and normalized.

#### Date Components Formatter

Foundation now provides localized formatting of durations and quantities of time via the new NSDateComponentsFormatter class. The header file NSDateComponentsFormatter.h is extensively commented with examples, information, and usage guidelines. The ‘formattingContext’ property mentioned below is not yet implemented in the WWDC seed.

#### Unit Formatters

Three new unit formatters have been added in 10.10. They are NSMassFormatter, NSLengthFormatter, and NSEnergyFormatter. These formatters do not support either parsing or unit conversion. These formatters can format a combination of a value and a unit into a localized string. They can also be used to get a localized string of a unit, and if the unit is singular or plural is based on the given value.

NSMassFormatter has a special property called isForPersonMassUse. This property should be set to YES if the formatter is used to format a person’s mass.
NSEnergyFormatter has a special property called isForFoodEnergyUse. This property should be set to YES if the formatter is used to format values for food energy.

#### Formatting Context

A new property called formattingContext has been added to NSDateFormatter, NSNumberFormatter, NSDateComponentsFormatter, and NSByteCountFormatter to express the context information for data formatting. The context information is where the data will be displayed so that it can be capitalized appropriately. For example, a date or the date element could be for the beginning of a sentence, the middle of a sentence, for display in a UI list, or for standalone display. The date or the date element may have different capitalization for different context. The formatting context API gives a better control of how the data is capitalized.

There are 6 different values for formattingContext, and they are defined in NSFormatter.h.

NSFormattingContextDynamic should be used in most of the time. When NSFormattingContextDynamic is used, the capitalization context is determined dynamically from the set {NSFormattingContextStandalone, NSFormattingContextBeginningOfSentence, NSFormattingContextMiddleOfSentence}. For example, if a date is placed at the beginning of a sentence, NSFormattingContextBeginningOfSentence is used to format the string automatically. When this context is used, the formatter will return a string proxy that works like a normal string in most cases. After returning from the formatter, the string in the string proxy is formatted by using NSFormattingContextUnknown. When the string proxy is used in -[NSString stringWithFormat:], we can determine where the %@ is and then set the context accordingly. With the new context, the string in the string proxy will be formatted again and be put into the final string returned from -[NSString stringWithFormat:].

#### NSDateFormatter Bug Fix

The older 10.0-style NSDateFormatter implementation could log error messages even when being used correctly. This has been corrected, though it’s still preferable to transition to 10.4-style formatters.

#### NSCalendar

Two Islamic calendar variants have been added in 10.10:

```
// A simple tabular Islamic calendar using the astronomical/Thursday epoch of CE 622 July 15NSString * const NSCalendarIdentifierIslamicTabular;
```

```
// The Islamic Umm al-Qura calendar used in Saudi Arabia. This is based on astronomical calculation, instead of tabular behaviour.NSString * const NSCalendarIdentifierIslamicUmmAlQura;
```

They can be used to create NSCalendar objects with initWithCalendarIdentifier:.

Bug fix:
The following methods now work correctly in 10.10 when the NSDateComponents argument has isLeapMonth set for the Chinese calendar:

- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:
- nextDateAfterDate:matchingComponents:options:

Behavior change:
The behavior of the following methods has been changed in 10.10 with the NSCalendarMatchPreviousTimePreservingSmallerUnits option or the NSCalendarMatchNextTimePreservingSmallerUnits option:

- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:
- nextDateAfterDate:matchingComponents:options:

In 10.9, if the date that matches the giving components is missing, the methods will return the previous (or the next, depending on which option is specified) existing value of the highest unit with exists and preserves the lower units’ values. For example, giving 2014-01-01 11:11:11, if the components are Feb. 29, the methods will return Jan. 29 00:00:00 in 2014 giving the NSCalendarMatchPreviousTimePreservingSmallerUnits option.

In 10.10, the behavior has been changed: if the date that matches the giving components is missing, the methods will return the previous (or the next, depending on which option is specified) existing value of the missing unit and preserves the lower units’ values of the giving date. For example, giving 2014-01-01 11:11:11, if the components are Feb. 29, the methods will return Feb 28th 11:11:11 in 2014 giving the NSCalendarMatchPreviousTimePreservingSmallerUnits option.

#### NSXPCConnection and NSProgress

In OS X 10.10 and iOS 8.0, NSXPCConnection and NSProgress have been integrated to work together seamlessly.

To receive progress updates from work done in another process, simply make an NSProgress object current before calling out to your remoteObjectProxy. If the other side supports reporting progress, then the NSProgress object in your process will be updated as work is completed in the remote process.

For example, the following code is part of an application which asks an XPC helper service to download a file.

```objc
- (IBAction)fetch:(id)sender{    NSURL *urlToFetch = ...;
```

```
    NSProgress *progress = [NSProgress progressWithTotalUnitCount:1];    [progress becomeCurrentWithPendingUnitCount:1];
```

```
    // Create a connection to our fetch-service and ask it to download for us. The fetch-service will implement the 'Fetch' protocol.    NSXPCConnection *fetchServiceConnection = [[NSXPCConnection alloc] initWithServiceName:@"com.apple.SandboxedFetch.fetch-service"];    fetchServiceConnection.remoteObjectInterface = [NSXPCInterface interfaceWithProtocol:@protocol(Fetch)];    [fetchServiceConnection resume];
```

```
    // Send a message to the fetch service. Because there is a current progress object (‘progress’), it will be updated if the remote side reports progress.    [[fetchServiceConnection remoteObjectProxy] fetchURL:urlToFetch withReply:^(BOOL ok) {        // This block will be invoked when the helper service replies.    }];
```

```
    // Even if the work is done asynchronously, we can resignCurrent here.    [progress resignCurrent];}
```

In the service, which implements the fetchURL:withReply: method, a current progress object is already setup for us and we simply need to attach a new progress to it to represent the work that we will be doing.

```objc
- (void)fetchURL:(NSURL *)url withReply:(void (^)(BOOL))reply {    // Create a progress object to handle progress below    NSProgress *progress = [NSProgress progressWithTotalUnitCount:10];    progress.cancellationHandler = ^{        // handle a cancellation from the application    };
```

```
    // do work here, e.g.    progress.completedUnitCount = 1;    // more work    progress.completedUnitCount = 5;    // etc.
```

```
   reply(YES);}
```

#### Changing Filename Case with NSFileManager

In previous releases, the NSFileManager methods -moveItemAtPath:toPath:error: and -moveItemAtURL:toURL:error: would fail with NSFileWriteFileExistsError when both parameters refer to the same item on disk. This operation now succeeds, which on case-insensitive but case-preserving file systems (like HFS+ on OS X) will allow changing the case of a file’s name.

#### More NSSecureCoding Adoption

NSIndexSet and NSIndexPath now both implement the NSSecureCoding protocol, which allows them to be used with NSXPC APIs.

#### NSFilePresenter File Package Attribute Change Notifications

In previous releases, -presentedItemDidChange was not sent to NSFilePresenters of file packages when only attributes of that package were changed. This has been fixed on OS X 10.0 and iOS 8.0.

#### Bug Fix in NSMetadataItem

In OS X 10.9, creating an NSMetadataItem with a URL for which no file exists would cause a subsequent -valueForAttribute: message to crash. Instead of crashing, -initWithURL: will now return nil in this situation.

#### Increased Leniency for NSDataBase64DecodingIgnoreUnknownCharacters

In OS X 10.9, decoding a base 64 string with "=" characters before the end of the string would cause the entire decoding operation to fail. However, RFC 4648 specifically allows implementations to ignore these characters, treating them like other unknown characters. The NSData base 64 decoding algorithm has been updated to allow for this when NSDataBase64DecodingIgnoreUnknownCharacters is used.

#### NSFileCoordinatorReadingForUploading

NSFileCoordinator has a new reading option that is meant to facilitate uploading user documents to web services like web pages or mail servers that only understand regular files and not file packages.

To use this API, request a coordinated read on any user document, the same way you would for normal reading, except use NSFileCoordinatorReadingForUploading. Before your accessor block is invoked, NSFileCoordinator will check if the file is a directory or not. If it is, it will create a zip archive of that directory in a temporary folder that is accessible by your application. If the file is not a directory, then it will be copied to that directory instead. The URL to the newly created temporary file will be accessible within your accessor block.

For normal coordinated reads, other coordinated writes are made to wait until you return from the accessor block. However, when using this option, other processes will be able to resume accessing that file immediately after the temporary file is created. This will allow you to do whatever is necessary to prepare the file for uploading without blocking other processes for arbitrary lengths of time.

The temporary file NSFileCoordinator creates will be unlinked as soon as you return from the accessor block. If you need to retain access to that file outside of the block, then you can copy, move, or hardlink the file to another location, or keep an open file descriptor to it.

This API is not intended to be a general-use facility for creating zip archives of files. Use it only for uploading.

#### Asynchronous NSFileCoordinator Waiting

Prior to OS X 10.10 and iOS 8.0, the recommended way to asynchronously wait for a coordinated read or write was to dispatch a block to another queue that then calls -coordinateReadingItemAtURL:options:error:byAccessor: (or one of the three other similar methods), which then waits synchronously on that queue. However, this pattern was wasteful of threads and dispatch queues.

There is a new API available on NSFileCoordinator called -coordinateAccessWithIntents:queue:byAccessor: that will wait asynchronously for access to the requested URLs without consuming additional queues. When access has been granted, the method will invoke your accessor block on a queue that you specify.

Like the older methods, the accessor block passed to this method is still run synchronously—when you return from the block, coordinated access to the file will end. Unlike the older methods, this new API allows you to perform coordination for an arbitrary number of files by passing an array of NSFileAccessIntent objects. NSFileAccessIntent encapsulates the URL, whether the access is a read or a write, and the reading or writing options. When your accessor block is invoked, you should use the URL property on the NSFileAccessIntent object, not the NSURL object you used to create that NSFileAccessIntent. If a document you are trying to access is moved or renamed, then NSFileCoordinator will update the URL property of the NSFileAccessIntent with the new value. NSFileCoordinator is unable to modify any other URLs that you have captured with the accessor block. Here’s an example of proper usage of this API:

```
NSFileAccessIntent *srcIntent = [NSFileAccessIntent readingIntentWithURL:url1 options:NSFileCoordinatorWritingForMoving];NSFileAccessIntent *dstIntent = [NSFileAccessIntent writingIntentWithURL:url2 options:NSFileCoordinatorWritingForReplacing];[fileCoordinator coordinateAccessWithIntents:@[srcIntent, dstIntent] queue:myQueue byAccessor:^(NSError *error) {    BOOL success = error == nil;    if (success) {        success = [fileManager removeItemAtURL:dstIntent.URL error:&error];    }    if (success) {        success = [fileManager moveItemAtURL:srcIntent.URL toItemAtURL:dstIntent.URL error:&error];    }    if (!success) {        // present error on main queue    }}];
```

Note that if an error occurs, the NSError is passed to the accessor block instead of being returned by reference via an NSError \*\* parameter.

#### Debugging File Coordination Delays

With File Coordination, applications have several opportunities to block other applications from being able to gain coordinated access to files. For example, they can delay returning from an NSFileCoordinator accessor block, or delay invoking blocks passed to NSFilePresenter messages. Sometimes, bugs in these applications can cause these delays to become indefinitely long. Due to the asynchronous and inter-process nature of File Coordination, it can often be difficult to understand and debug these issues.

In OS X 10.10 and iOS 8.0, the NSFileCoordinator class now responds to a method called +(void)_printDebugInfo. This method will print all available information about each file or directory involved in File Coordination on your system, and each process that is interacting with it. This method is intended for use in the debugger, so do not use this method in shipping code. It is not declared in any headers and may be removed or renamed without notice.

The first section of the output will show a compressed hierarchy of files that the File Coordination daemon is tracking. It shows what processes have NSFilePresenters registered for these files, and which ones have claims outstanding or pending for them. When a claim is delayed for any reason, you will be able to see whether that claim is waiting for another conflicting claim to finish, or whether it is waiting for an NSFilePresenter to respond to the claim.

The second section of the output will show each process that is interacting with File Coordination. It shows NSFilePresenter activity, like what NSFilePresenter messages have been sent but not yet responded to, as well as NSDocument serialization info, if applicable.

Using all of this information, it should become much easier to understand and debug issues you may be experiencing with File Coordination. On OS X, all of this same information is provided in the archive created by the ‘sysdiagnose’ tool, which will aid you in debugging problems that occur on customer’s computers. Note that this information includes file and process names, but does not include any file contents.

#### NSFileCoordinator purpose identifiers

An NSFileCoordinator’s purpose identifier is a string that uniquely identifies the file access that will be done by the NSFileCoordinator. Every NSFileCoordinator has a unique purpose identifier that is created during initialization. Coordinated reads and writes performed by NSFileCoordinators with the same purpose identifier never block each other, even if they originate from different processes. If you are coordinating file access on behalf of an NSFilePresenter, you should use -initWithFilePresenter: and should not attempt to set a custom purpose identifier. Every NSFileCoordinator instance initialized with the same NSFilePresenter will have the same purpose identifier.

When using the NSFileProviderExtension API, you need to supply a ‘providerIdentifier’. Whenever the NSFileProviderExtension needs to do file coordination, it needs to set the NSFileCoordinator’s purpose identifier to the NSFileProviderExtension’s providerIdentifier. Otherwise, the coordination could trigger additional unexpected actions by your NSFileProviderExtension.

If you have multiple subsystems cooperating to perform one high-level operation, and each subsystem performs its own coordinated reads and writes, they should all use the same purpose identifier to avoid blocking on one another.

When creating custom purpose identifiers, you can use a reverse DNS style string, such as "com.mycompany.myapplication.mypurpose", or a UUID string. Nil and zero-length strings are not allowed.

Purpose identifiers can be set only once per NSFileCoordinator. If you attempt to set the purpose identifier of an NSFileCoordinator that you initialized with -initWithFilePresenter: or that you already assigned a purpose identifier, an exception will be thrown.

#### NSMetadataQuery and NSMetadataItem enhancements for ubiquitous items

When using one of the “ubiquitous” NSMetadataQuery scopes, you are now allowed to pass [NSPredicate predicateWithValue:YES] to easily match all files in the scope. This predicate is now also the default for ubiquitous scopes. An explicit predicate is still required on OS X for non-ubiquitous scopes.

The NSMetadataItemContentTypeKey and NSMetadataItemContentTypeTreeKey attributes are now available to use on NSMetadataItems created by queries with ubiquitous scopes.

The symbols NSMetadataQueryUpdateAddedItemsKey, NSMetadataQueryUpdateChangedItemsKey, and NSMetadataQueryUpdateRemovedItemsKey were originally declared to be available on iOS 7.0. However, the symbols did not exist on iOS until 8.0. The declaration in the header has been updated to reflect this fact.

#### Updating your iCloud application for OS X 10.10 and iOS 8.0

Prior to OS X 10.10 and iOS 8.0, iCloud files that the system knows about but hasn’t yet downloaded would be represented in an application’s ubiquity container with a special user-visible file. That file would have the same name as the file in iCloud, and could be used to get various metadata about the file. That file could also be moved, renamed, or deleted locally, and those changes would be reflected in the iCloud server state. This is no longer the case on OS X 10.10 or iOS 8.0 SDKs. Instead, unfulfilled files are represented with an invisible file in the same directory, the naming and contents of which are implementation details and subject to change. This change has two implications for applications:

1) It is not recommended to use directory enumeration APIs (e.g. NSDirectoryEnumerator, CFURLEnumerator, readdir, etc.) to enumerate the contents of a ubiquity container. Applications should instead use NSMetadataQuery with NSMetadataQueryUbiquitousDataScope or NSMetadataQueryUbiquitousDocumentsScope, which will list all known data or document files in the container. If you must enumerate the contents of the container, you must ignore any hidden files, or files with extensions your application does not recognize.

2) It is not possible to use the standard APIs for getting file attributes (e.g. NSURL resource values, NSFileManager, stat, getattrlist, etc.) on URLs of unfulfilled files, because there is no file present at the URL until the file has been downloaded. Applications should instead use new APIs designed for this purpose, which are explained below.

If your application already uses NSMetadataQuery to list iCloud files, only gets file attributes from NSMetadataItem, and always uses NSFileCoordinator to access iCloud files, then you shouldn’t need to change anything about your application to allow it to continue working with iCloud on OS X 10.10 and iOS 8.0.

If your application needs to access file metadata directly from the file system for files that may not yet be downloaded, then you can use the following APIs:

1. -[NSURL getPromisedItemResourceValue:forKey:error:] and -[NSURL promisedItemResourceValuesForKeys:error:]

These methods are versions of the existing NSURL APIs that understand how to get attributes from unfulfilled iCloud files. They can be used with any NSURL resource values that are not dependent on file contents being present (for example, NSURLGenerationIdentifierKey, NSURLContentAccessDateKey, and NSURLFileResourceIdentifierKey).

A coordinated read is not required to invoke this method. If you choose not to, you must be prepared for this method to fail. Listening to NSMetadataQuery or NSFilePresenter notifications will help you know when to retry invoking these methods.

2. NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly and NSFileCoordinatorWritingMetadataOnly

Normally, using NSFileCoordinator to perform a coordinated read will cause an unfulfilled iCloud file to be downloaded before the accessor block is invoked. If you just want to read file metadata, you can avoid waiting for the file to download by using this option in your coordinated read. When using this option you must still use the “PromisedItem” NSURL methods inside your accessor block in order to safely read metadata for files that are unfulfilled.

Similarly, when all you want to do is set some metadata on potentially unfulfilled iCloud files, you must use NSFileCoordinatorWritingContentIndependentMetadataOnly. There are no “PromisedItem” APIs for setting attributes, so you can use normal APIs like -[NSURL setResourceValue:forKey:error:]. As the name indicates, again setting only content independent metadata is supported,

To ease adoption of these new APIs, applications built using the OS X 10.9 or iOS 7.0 SDKs (or earlier) will have all files in their ubiquity container downloaded greedily.

NSFilePresenters for ubiquity container directories will continue to receive -presentedSubitemDidChangeAtURL: and -presentedSubitemAtURL:didMoveToURL: notifications for unfulfilled files. However, your application needs to be aware that for these unfulfilled files, there is nothing in the file system at those URLs, so you need to use NSFileCoordinator or the “PromisedItem” APIs to interact with them.

Finally, NSMetadataQuery objects with ubiquitous scopes will now report directories in the query results. If needed, you can use NSMetadataItemContentTypeKey in your query to filter out anything with the type ‘public.folder’.

#### iCloud Versions

iCloud applications on OS X and iOS can now access previous document versions in iCloud. These versions are automatically created by iCloud when changes are uploaded to the server. To discover these versions, invoke +[NSFileVersion getNonlocalVersionsOfItemAtURL:completionHandler:]. If successful, the completion handler will be passed an array of NSFileVersions.

Versions returned by this API will not initially have the version contents available locally. -[NSFileVersion hasLocalContents] will return NO to indicate this. Accessing these URLs is very much like accessing regular iCloud files. You can use NSURL’s “promisedItem” APIs to get metadata about the file, like its NSURLFileSizeKey or NSURLTypeIdentifierKey. In order to trigger the contents to be downloaded, you must use NSFileCoordinator to perform a coordinated read on the NSFileVersion’s URL property.

When a version’s contents are downloaded, it will be cached in a local NSFileVersion, meaning it will start appearing in the array returned by +[NSFileVersion otherVersionsOfItemAtURL:]. This local NSFileVersion will have a -persistentIdentifier identical that of the NSFileVersion previously returned by +getNonlocalVersionsOfItemAtURL:completionHandler:. You can take advantage of this fact to avoid duplicate versions.

If you want to present all versions available, both local and non-local, for a particular document, you need to do the following things to avoid potential races, which could result in duplicate or missing versions:

1. Perform a coordinated read on the desired file.
2. Register an NSFilePresenter with +[NSFileCoordinator addFilePresenter:]
3. Invoke +[NSFileVersion otherVersionsOfItemAtURL:] to get local versions
4. Invoke +[NSFileVersion getNonlocalVersionOfItemAtURL:completionHandler:] to get non-local versions.
5. In your NSFilePresenter’s implementation of -presentedItemDidGainVersion:, look for a version with the same -persistentIdentifier value as the passed-in NSFileVersion (or that matches with -isEqual:) and replace that version with the new one. In your NSFilePresenter’s implementation of -presentedItemDidLoseVersion:, look for an NSFileVersion matching the passed-in NSFileVersion, and remove it.

#### Ubiquitous external documents

If your iOS application uses UIDocumentPickerViewController, your application will be able to access documents from outside of your application’s ubiquity container. When a user grants your application access to a file from another application’s ubiquity container, your application will be allowed to reopen that document on any device using the same iCloud account without requiring the user to go through the document picker again. These previously opened external ubiquitous documents can be found with NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope.

NSMetadataItem results in this scope will return YES for the NSMetadataUbiquitousItemIsExternalDocumentKey attribute to indicate that they from outside the application’s container. Because these documents exist outside your application’s sandbox, the NSMetadataItemURLKey attribute of these items is a security-scoped URL. In order to access these documents, you must first invoke -[NSURL startAccessingSecurityScopedResource]. If this method returns YES, then when you’re done accessing the document you must invoke -[NSURL stopAccessingSecurityScopedResource].

If your iOS application wants to show external documents in its document picker UI together with other documents, you can use NSMetadataUbiquitousItemContainerDisplayNameKey to show the name of the container the document comes from.

External ubiquitous documents are also represented by a special file on disk. The location of these files is available with NSMetadataUbiquitousItemURLInLocalContainerKey. You may allow users to move these files into other directories within your application’s ubiquity container.

#### iCloud download requested state

You can now use NSURLUbiquitousItemDownloadRequestedKey or NSMetadataQueryUbiquitousItemDownloadRequestedKey to detect whether a download for an iCloud file has already been requested with either a coordinated read or -[NSFileManager startDownloadingUbiquitousItemAtURL:error:]. You can use this state in your UI to show users that the document has been requested and will be delivered as soon as iCloud can deliver it.

#### NSProcessInfo Operating System Version Checking

NSProcessInfo has a new API:

```objc
- (BOOL) isOperatingSystemAtLeastVersion:(NSOperatingSystemVersion)version
```

which allows programs to test whether they’re on a particular version of the OS or newer. Additionally, there’s a new property to get the version of the OS that the application is currently running on:

```objc
@property (readonly) NSOperatingSystemVersion operatingSystemVersion
```

#### +[NSLocale autoupdatingCurrentLocale] Bug Fix

Auto-updating NSLocales were not completely toll-free bridged with CFLocaleRef, resulting in crashes when passed to some methods (in particular lowercaseStringWithLocale:). This has been fixed.

#### -[NSUserDefaults synchronize] Changes

In earlier releases, the various ‘set’ methods on NSUserDefaults would wait several seconds before publishing the changes to other applications unless synchronized (though it has always been instant within a program). This delay has been removed. Additionally, iOS now matches Mac OS X’s behavior of automatically picking up external changes without needing to synchronize.

If you:

• Synchronized to avoid losing data if your app crashed
• Synchronized to read changed values from outside your process
• Synchronized because it made things work and you weren’t sure why

Then please don’t do so now. It should just work, and synchronizing will unnecessarily slow down your program.

If you synchronized because you immediately send out a notification to re-read preferences in another program after setting, and you wanted to be sure it will pick it up, then it may still be worth calling synchronize. You should probably restructure your program to use a real IPC mechanism (such as NSXPCConnection) to send the data to the other process though, rather than indirecting through the preferences system.

#### NSUserDefaults Plist Files

The on-disk property list files used by NSUserDefaults have always been a private implementation detail, but in previous releases of iOS, and significantly older releases of Mac OS X, directly modifying them has mostly worked (though there are some potential data-loss issues for applications that do so, even on previous systems). In iOS 8 and later, the NSUserDefaults daemon process (cfprefsd) will cache information from these files and asynchronously write to them. This means that directly modifying plist files is unlikely to have the expected results (new settings will not necessarily be read, and may even be overwritten). You should use the NSUserDefaults or CFPreferences APIs, or (on Mac OS X) the defaults(1) command, to interact with the preferences system.

#### NSUserDefaults Performance Tradeoffs

Reading from NSUserDefaults is extremely fast. It will cache values to avoid reading from the disk, and takes about 0.5 microseconds to do [[NSUserDefaults standardUserDefaults] boolForKey:] on a 2012 MacBook Pro. It’s generally unnecessary (and even undesirable since it prevents picking up new values) to cache the result of reading from preferences.

However, writing to NSUserDefaults is a bit slower. In general, expect it to take roughly as long as using NSPropertyListSerialization to convert your key and value to plist data, plus a few 10s of microseconds. For this reason, as well as memory usage, it’s generally best to store relatively small data in CFPreferences.

As with any and all performance guidelines, use Instruments to profile your application and evaluate the impact of various alternatives.

#### defaults(1) enhancements

The ‘defaults import’ and ‘defaults export’ commands now support stdin and stdout as targets, by passing ‘-‘ as the path.

#### NSQualityOfService

Several new Quality of Service (QoS) classifications have been added which map to the new underlying OS concept in OS X 10.10 and iOS 8. They are used to indicate to the system the nature and importance of work, and are used by the system to manage a variety of resources. Higher QoS classes receive more resources than lower ones during resource contention.

NSQualityOfServiceUserInteractive: this QoS is used for work directly involved in providing an interactive UI such as processing events or drawing to the screen.

NSQualityOfServiceUserInitiated: this QoS is used for performing work that has been explicitly requested by the user and for which results must be immediately presented in order to allow for further user interaction. For example, loading an email after a user has selected it in a message list.

NSQualityOfServiceUtility: this QoS is used for performing work which the user is unlikely to be immediately waiting for the results. This work may have been requested by the user or initiated automatically, does not prevent the user from further interaction, often operates at user-visible timescales and may have its progress indicated to the user by a non-modal progress indicator. This work will run in an energy-efficient manner, in deference to higher QoS work when resources are constrained. For example, periodic content updates or bulk file operations such as media import.

NSQualityOfServiceBackground: this QoS is used for work that is not user initiated or visible. In general, a user is unaware that this work is even happening and it will run in the most efficient manner while giving the most deference to higher QoS work. For example, pre-fetching content, search indexing, backups, and syncing of data with external systems.

NSQualityOfServiceDefault: this NSQualityOfService value indicates the absence of QoS information. Whenever possible QoS information will be inferred from other sources. If such inference is not possible, a QoS between UserInitiated and Utility will be used.

#### NSTask qualityOfService

NSTask has a new qualityOfService property.

You can change the qualityOfService property before launching the task, as much as you like, but it becomes immutable when the task is launched, and the value it has at that time is the value that is used:

• If the property has not been set, you get a default behavior from the OS.
• If the property has been set to NSQualityOfServiceDefault, you get a default behavior from the OS.
• If the property has been set to another value, that value is given to the OS when launching the new process.

NSTasks do not infer any QOS from any execution context, though the underlying OS behaviors might.

#### NSThread qualityOfService

NSThread has a new qualityOfService property.

You can change the qualityOfService property before starting the thread, as much as you like, but it becomes immutable when the thread is started, and the value it has at that time is the value that is used:

• If the property has not been set, you get a default behavior from the OS.
• If the property has been set to NSQualityOfServiceDefault, you get a default behavior from the OS.
• If the property has been set to another value, that value is given to the OS when starting the new thread.

Reading a thread's qualityOfService after the thread has started will read out its current value.

NSThreads do not infer any QOS from any execution context, though the underlying OS behaviors might.

If the deprecated NSThread threadPriority property is set, then any value that has been set in the qualityOfService property is cleared, as if the qualityOfService property had not been set. If the qualityOfService property is set, the threadPriority property is set back to its default state.

#### NSOperationQueue qualityOfService

NSOperationQueue has a new qualityOfService property.

You can change the qualityOfService property at any time.

When an operation is added to a queue, the queue's qualityOfService value at that time may affect the effective QOS that the operation will be run at:

• If the queue property has not been set, the operation is unaffected.
• If the queue property has been set to NSQualityOfServiceDefault, the operation is unaffected.
• If the queue property is set to another value, the operation is promoted to the queue's qualityOfService if its promotion QOS is not already at least that level.

If the qualityOfService property of a queue is changed while there are operations in the queue, the effective QOS of operations in the queue will be affected, just as the operations were when added to the queue. Thus, when the qualityOfService property of a queue is changed, all operations in the queue, running or not, have their effective QOS raised up to that level (if they were lower), and future additions to the queue are raised to that level (when they are lower). If the qualityOfService property is lowered from one level to another, only future additions will be affected by that new lower value. Operations' promotion or effective QOS is never lowered by the setting of, or the set value of, a queue's qualityOfService.

When an operation is added to a queue, the operation's effective QOS values at that time may affect the effective QOS of the operations which are already in the queue ("ahead of it"):

• The operations already ahead in the queue of the newly added operation, running or not, are promoted to the effective QOS of the operation being added.

Thus, if a high QOS operation is added to a queue, operations already in the queue are raised up to that level (if they were lower). Operations added after that high-QOS operation are not affected by its presence in the queue.

The meaning and interaction of operation promotion QOS and effective QOS is discussed in the section on NSOperation qualityOfService.

NSOperationQueues do not infer any QOS from any execution context.

If the (dispatch_queue_t) underlyingQueue property of an NSOperationQueue is set, qualityOfService property values of NSOperationQueues and NSOperations have no effect. The effective QOS of operations run by that queue is determined by the state of the dispatch_queue_t.

#### NSOperation qualityOfService

NSOperation has a new qualityOfService property.

You can change the qualityOfService property at any time.

There are various real and virtual QOS values that relate to how an operation runs:

• The qualityOfService property value
• An inferred QOS
• The promotion QOSes
• The effective QOS

When an operation object is created, an inferred QOS value is computed from the execution context:

• If either:
    • the operation is being created in the execution context of another operation (already running on that thread); or
    • the operation is being created in the execution context of a certain NSProcessInfo API;
then the nearest one of those to the current activation frame of the call stack of the current thread is used as the inferred QOS of the new operation:
    • that operation's effective QOS at the time it started running;
    • the NSProcessInfo API's values are mapped to a QOS value.
• If the operation is being created on the main thread, the inferred QOS is NSQualityOfServiceUserInitiated.
• Otherwise, the current thread's QOS (which may be none) is read and used as the inferred QOS of the new operation.

An operation can be promoted (have promotion QOSes applied to it) in several contexts:

• When the operation is added to a queue, or when the qualityOfService property of the queue the operation is in is changed
    • (as discussed in the NSOperationQueue section)
• When a different operation is added to a queue that the operation (in question) is already in
    • (as discussed in the NSOperationQueue section)
• When a different later (after the operation in question) operation in the same queue has its effective QOS raised
    • the effective QOS of the other operation promotes the operation
• When a different operation (a dependee) becomes dependent upon the operation in question
    • the effective QOS of the dependee promotes the operation
• When a dependee operation has its effective QOS raised
    • the new effective QOS of the dependee promotes the operation
• When the operation is waited upon, with the -waitUntilFinished method, or indirectly when the operation's queue's -waitUntilAllOperationsAreFinished method, is used
    • if the waiting thread is the main thread, the promotion QOS is taken to be NSQualityOfServiceUserInteractive;
    • otherwise if the waiting is done in the execution context of another operation, its effective QOS promotes the operation;
    • otherwise the QOS of the current thread promotes the operation.

These are all collectively called the promotion QOSes; or for the MAX() of all of them, just promotion QOS.

These various values are put together into the effective QOS. The effective QOS is the MAX() of all of these QOS values: {the inferred QOS, the promotion QOSes, the qualityOfService property value}, with these qualifications:

• If the operation's qualityOfService property has been explicitly set to anything, even NSQualityOfServiceDefault, the inferred QOS is ignored.
• If the operation's qualityOfService property has not been explicitly set to anything, it is ignored (as if no value exists).
• All QOS values of NSQualityOfServiceDefault are ignored.
• If there are no QOS values after all that ignoring, the effective QOS is NSQualityOfServiceDefault.

Thus, for example, if an operation is waited upon, its effective QOS may be raised by the waiting context, which may recursively raised all of its dependent operations and all operations ahead of it in the queue (and so on recursively outward in the tree of these relationships).

An operation's qualityOfService property value has no effect if the operation is started manually, rather than being put in an NSOperationQueue, unless the code which is starting it reads out that value and makes some appropriate use of it; that is outside the purview of Foundation.

#### NSOperation's threadPriority property

The threadPriority property has been deprecated. Move to using the "qualityOfService" property and concepts instead.

#### NSOperation name

NSOperation has a new name property. The operation's name will show up as part of the name of the underlying dispatch queue that the operation is running on, which shows up in some tools.

#### NSOperationQueue underlyingQueue

NSOperationQueue has a new underlyingQueue property. When set to, to run operations, the NSOperationQueue will dispatch a block to this dispatch queue which starts the operation, rather than NSOperationQueue making a dispatch queue choice itself.

An exception will be raised if the dispatchQueue is changed while operations are in the operation queue. It is just not advisable to attempt to do that. Set the value once, after creating the NSOperationQueue and before using it otherwise.

There is and will be no way to "find" an NSOperationQueue with a given dispatch queue.

For operations put into an NSOperationQueue with an assigned dispatch_queue_t, the qualityOfService property has no effect; the effective QOS of execution comes from the dispatch_queue_t.  The name property of the NSOperationQueue and NSOperation has no effect (the dispatch_queue_t has the name).

Note that this is not a queue which NSOperationQueue will use for its own "thread-safety" serialization; this is only "the dispatch queue to run the operations on".

#### NSString

NS/CFStrings now use a “tagged pointer” format where the string contents are stored in the pointer directly in some cases. This happens automatically thru the existing APIs that create strings, without need to use any new API.

This change will break any code which treats NS/CFStrings objects as pointers.

In addition, this change enables index and range checking to be performed more often when working with strings. So you may see runtime exceptions due to this change. In almost all cases these exceptions point to bugs in code, so please take them seriously.

There are other related changes in behavior due to this change. For instance, -UTFString and -cStringUsingEncoding: now need to manufacture the buffer that is returned as opposed to possibly returning an internal pointer (which was sometimes possible). The operation has been optimized so there isn’t a significant performance impact, but there is a behavior change nonetheless.

Do not make any assumptions on the kind and size of strings which can fit into the tagged pointer.

This change is enabled only for applications that link against the 10.10 SDK.

NSString now has the following two convenience methods:

```objc
- (BOOL)containsString:(NSString *)str;- (BOOL)localizedCaseInsensitiveContainsString:(NSString *)str;
```

containsString: returns YES if the target string is contained within the receiver. This is the same as calling rangeOfString:options: with no options, thus doing a case-sensitive, non-literal search. localizedCaseInsensitiveContainsString: is the case-insensitive variant. Note that it takes the current locale into effect as well. Locale-independent case-insensitive operation, and other needs can be achieved by calling rangeOfString:options:range:locale: directly.

Note that as is the case with the existing rangeOfString: method and variants, these methods will return NO if the target string is the empty string.

#### NSByteCountFormatter

A bug where non-adaptive, zero-padding formatter displaying byte counts would use decimal places (for instance displaying “12.0 bytes”) has been fixed.
