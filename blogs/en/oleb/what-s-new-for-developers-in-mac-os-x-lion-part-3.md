---
title: 'What''s New for Developers in Mac OS X Lion (Part 3)'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/08/whats-new-for-developers-in-lion-part-3/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:36ecacaf9f9d19c8'
translated: false
---

> 原文：[What's New for Developers in Mac OS X Lion (Part 3)](https://oleb.net/blog/2011/08/whats-new-for-developers-in-lion-part-3/)　·　Ole Begemann

# What's New for Developers in Mac OS X Lion (Part 3)

This is the third and final article in my little series covering the new developer APIs in Lion. Check out parts one and two if you haven’t done so already:

- [Part 1](https://oleb.net/blog/2011/07/whats-new-for-developers-in-lion-part-1/): Major new features: Application persistence, automatic document saving, versioning, file coordination, Cocoa autolayout, full-screen apps, popover windows, sandboxing, push notifications.
- [Part 2](https://oleb.net/blog/2011/08/whats-new-for-developers-in-lion-part-2/): New frameworks: AV Foundation, Store Kit (in-app purchasing) and IMServicePlugIn. Changes in AppKit.
- Part 3: Changes in Core Data, Core Foundation, Core Location, Foundation, QTKit, Quartz and Quartz Core.

# Core Data

## Formalized Concurrency Model

Working with Core Data on a background thread involves manually managing two separate managed object contexts and their associated object graphs, taking care that you do not pass managed object from one thread/context to another. You should never access a managed object context outside the thread or dispatch queue that created it. This is still true in Lion, and the system now lets you formalize this agreement by creating a context with [`initWithConcurrenceType:NSConfinementConcurrencyType`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW40).

If you pass `NSPrivateQueueConcurrencyType` to `initWithConcurrencyType:`, the context creates and manages a private dispatch queue to operate on. To send any message to such a context, you must use the new methods [`performBlock:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW45) or [`performBlockAndWait:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW46). The context will then execute the passed blocks on its own queue.

`NSMainQueueConcurrencyType` creates a context that is associated with the main dispatch queue and thus the main thread. Use such a context to link it to controllers and UI objects that are required to run on the main thread.

## Support for Nested Managed Object Contexts

In earlier releases of OS X, a managed object context is always directly associated with a “parent” persistent store coordinator. In Lion, rather than having a persistent store coordinator, a context can also have another managed object context as its parent. This nested relationship between managed object contexts has two very useful use cases:

1. Fetches and saves are mediated by the second context, which can execute these time-consuming operations in the background, thereby avoiding blocking the UI.
2. Allow discardable edits that go away by simply throwing away the second context.

Use the [`-setParentContext:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW42) method to assign a parent context to your managed object context.

## Ordered Relationships

To-many relationships in Core Data can now optionally have an order. This much-awaited feature should save many people a lot of tedious manual work that is involved in manually maintaining an order attribute for the items in the relationship. See the [`isOrdered`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSRelationshipDescription_Class/NSRelationshipDescription.html#//apple_ref/doc/uid/TP30001176-SW3) attribute of `NSRelationshipDescription`.

In code, ordered relationships are represented by the new [`NSOrderedSet`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSOrderedSet_Class/) class (see below). Note that ordered relationships are significantly less efficient than unordered ones. You should only use them if a relationship has an intrinsic order. Do not use ordered relationships just because you want to avoid sorting your fetch results.

## External Storage for Attributes

Another area where many developers had to invest manual work was when the Core Data store was designed to hold references to large amounts of binary data that were usually stored in external files (such as images). Developers had to generate unique filenames, create these files, store the filenames in the data store and delete the files when the associated managed object was deleted.

In Lion, managed objects support optional external storage for attribute values. If you specify in the Core Data editor that the value of a certain attribute (typically a BLOB) may be stored externally, Core Data uses internal heuristics (probably based on the size of the BLOB) to decide whether to store the data directly in the database or in a separate external file. As a developer, you don’t have to care either way. See the [`allowsExternalBinaryDataStorage`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSAttributeDescription_Class/reference.html#//apple_ref/doc/uid/TP30001175-SW25) attribute of `NSAttributeDescription`. I think this is a great feature.

## Fetch Requests

[`NSFetchRequest`](http://developer.apple.com/library/mac/#documentation/Cocoa/Reference/CoreDataFramework/Classes/NSFetchRequest_Class/NSFetchRequest.html) got a few new features in Lion:

- Initializing a fetch request with the new [`initWithEntityName:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSFetchRequest_Class/NSFetchRequest.html#//apple_ref/occ/instm/NSFetchRequest/initWithEntityName:) method saves you a separate call to `setEntity:` and the hassle of first retrieving the `NSEntityDescription`.
- If you configure your fetch request [to return dictionaries](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSFetchRequest_Class/NSFetchRequest.html#//apple_ref/c/econst/NSDictionaryResultType), it supports `GROUP BY` ([`setPropertiesToGroupBy:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSFetchRequest_Class/NSFetchRequest.html#//apple_ref/occ/instm/NSFetchRequest/setPropertiesToGroupBy:)) and `HAVING` ([`setHavingPredicate:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSFetchRequest_Class/NSFetchRequest.html#//apple_ref/occ/instm/NSFetchRequest/setHavingPredicate:)) clauses.

## Implement Your Own Incremental Stores

Two new classes, [`NSIncrementalStore`](http://developer.apple.com/library/mac/documentation/CoreData/Reference/NSIncrementalStore_Class/Reference/NSIncrementalStore.html#//apple_ref/occ/cl/NSIncrementalStore) and [`NSIncrementalStoreNode`](http://developer.apple.com/library/mac/documentation/CoreData/Reference/NSIncrementalStoreNode_Class/Reference/NSIncrementalStoreNode.html#//apple_ref/occ/cl/NSIncrementalStoreNode), allow you to add support for other non-atomic persistent stores besides the existing SQLite store. (Writing custom atomic persistent stores was already supported in earlier versions of OS X.)

One cool possibility would be to write a Core Data interface to a web service backend such as [CouchDB](http://couchdb.apache.org/).

The [Core Data Release Notes](http://developer.apple.com/library/mac/#releasenotes/DataManagement/RN-CoreData/_index.html) offer the best overview of the new features in Apple’s documentation.

# Core Foundation

With the `CFStringGetHyphenationLocationBeforeIndex()` function it is now possible to locate potential hyphenation points within a word. Since hyphenation is language-specific, you have to pass the locale of the string you are inspecting to the function. Do not forget to check whether the system supports hyphenation for that locale beforehand by calling `CFStringIsHyphenationAvailableForLocale()`

See the [Core Foundation Release Notes](http://developer.apple.com/library/mac/#releasenotes/CoreFoundation/CoreFoundation.html) for details on this and more changes in Core Foundation.

# Core Location

The Core Location framework originated on iOS and was introduced to OS X with Snow Leopard. In Lion, Apple brought the header files up to par with iOS. They even added stuff like `CLHeading` that doesn’t make a lot of sense on a computer but who knows when the first laptop with a built-in compass will come out? The same goes for the [`CLDeviceOrientation`](https://developer.apple.com/reference/corelocation/cldeviceorientation) enum, which includes values for portrait, landscape, face up and face down orientations.

The most useful addition to the framework seems to be region monitoring. Start the [`CLLocationManager`](https://developer.apple.com/reference/corelocation/cllocationmanager) by sending it a `startMonitoringForRegion:desiredAccuracy:` message to be alerted when the computer enters a specific area, or use `startMonitoringSignificantLocationChanges` to be notified whenever the computer’s location changes.

# Foundation

As usual, the [Foundation Release Notes for Lion](http://developer.apple.com/library/mac/#releasenotes/Cocoa/Foundation.html) give the best explanation of the new features in Apple’s documentation. It is unfortunate that it is so hard to discover these release notes documents for the particular frameworks as they are not linked from either [What’s New in Lion](http://developer.apple.com/library/mac/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_7.html#//apple_ref/doc/uid/TP40010355-SW5) or the [API Diffs](http://developer.apple.com/library/mac/releasenotes/General/MacOSXLionAPIDiffs/index.html#//apple_ref/doc/uid/TP40010630).

## Native JSON Support

With [`NSJSONSerialization`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSJSONSerialization_Class/Reference/Reference.html#//apple_ref/occ/cl/NSJSONSerialization), OS X gets native reading and writing support for JSON, which has become the _de facto_ data format for web APIs.

The [`+JSONObjectWithData:options:error:`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSJSONSerialization_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40010946-CH1-SW2) class method takes JSON data that you received from a network request and converts it into a hierarchy of Foundation objects (`NSDictionary`, `NSArray`, `NSString`, `NSNumber`, `NSNull`). Two useful options, `NSJSONReadingMutableContainers` and `NSJSONReadingMutableLeaves` let you specify whether the resulting Foundation objects should be immutable (the default) or mutable. The class also offers a variant to read the data directly from an `NSInputStream`: [`+JSONObjectWithStream:options:error:`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSJSONSerialization_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40010946-CH1-SW3).

To convert an object graph into UTF-8-encoded JSON, call the [`+dataWithJSONObject:options:error:`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSJSONSerialization_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40010946-CH1-SW4) class method. By default, the resulting JSON data will be as compact as possible. Passing `NSJSONWritingPrettyPrinted` as an option to the method allows you to generate more readable output.

## Key-Value Observing

The new method [`removeObserver:forKeyPath:context:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Protocols/NSKeyValueObserving_Protocol/Reference/Reference.html#//apple_ref/occ/instm/NSObject/removeObserver:forKeyPath:context:) allows you to more precisely remove a key-value observer by passing the same `context` pointer you used when adding the observer with [`addObserver:forKeyPath:options:context:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Protocols/NSKeyValueObserving_Protocol/Reference/Reference.html#//apple_ref/occ/instm/NSObject/removeObserver:forKeyPath:context:). Using the old `removeObserver:forKeyPath:` method could possibly lead to problems.

## `NSURLConnection`

Before Lion, asynchronous [`NSURLConnection`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSURLConnection_Class/)s always required a running runloop, making the class a bit difficult to use with operation or dispatch queues. Queue support was added in Lion. Setting an `NSOperationQueue` with the [`setDelegateQueue:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSURLConnection_Class/Reference/Reference.html#//apple_ref/doc/uid/20001697-SW3) method will deliver the delegate messages on the specified queue.

The new [`sendAsynchronousRequest:queue:completionHandler:`](https://developer.apple.com/reference/foundation/nsurlconnection/1418125-sendasynchronousrequest) convenience method will start an asynchronous connection and execute the `completionHandler` block on the specified queue once the request has finished either successfully or with an error. It frees the developer from implementing any [`NSURLConnectionDelegate`](https://developer.apple.com/reference/foundation/nsurlconnectiondelegate) methods if special handling of the connection, continuous progress reports etc. are not required. Very handy.

## Linguistic Tagging

With the new [`NSLinguisticTagger`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSLinguisticTagger_Class/Reference/Reference.html#//apple_ref/occ/cl/NSLinguisticTagger) class, developers can easily analyze natural-language text and identify different grammatical parts of speech. For example, given the sentence “Steve Jobs just resigned as CEO.” and configured to use the tag scheme [`NSLinguisticTagSchemeLexicalClass`](https://developer.apple.com/reference/foundation/nslinguistictagger/1661617-nslinguistictagschemelexicalclas), `NSLinguisticTagger` can identify the words “Steve”, “Jobs” and “CEO” as nouns, the word “just” as an adverb, and the word “as” as a preposition.

Other possible tag schemes include [`NSLinguisticTagSchemeLemma`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSLinguisticTagger_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSLinguisticTagSchemeLemma) to identify stem forms of words, [`NSLinguisticTagSchemeLanguage`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSLinguisticTagger_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSLinguisticTagSchemeLanguage) to identify the language and [`NSLinguisticTagSchemeScript`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSLinguisticTagger_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSLinguisticTagSchemeScript) to identify the script (Latin, Cyrillic, etc.).

The tagging works very well for English. Other languages might not support all tag schemes or might not be supported at all. Call the [`availableTagSchemesForLanguage:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSLinguisticTagger_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40009799-CH1-SW21) class method to determine the level of support for a language.

To do the analysis, create an instance of `NSLinguisticTagger` and pass it a string with `setString:`. Then call [`enumerateTagsInRange:scheme:options:usingBlock:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSLinguisticTagger_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40009799-CH1-SW17) to iterate over all tags the linguistic tagger found.

## Ordered Sets

[`NSOrderedSet`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSOrderedSet_Class/) and [`NSMutableOrderedSet`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSMutableOrderedSet_Class/) are new collection classes that combine the advantages of `NSArray` (ordered collection, fast index-based access) and `NSSet` (unique contents, fast access to objects). Note that `NSOrderedSet` inherits neither from `NSArray` nor from `NSSet`.

The class also offers two interesting methods, `-(NSArray *)array` and `- (NSSet *)set`. These return proxy objects for the underlying ordered set that act like an array or set without actually being one. If the underlying ordered set is mutable, changes to it will directly pass through to the proxy objects and these “immutable” collections will appear to outside code to be changing.

## Regular Expressions and Data Detectors

Two new Lion developer features that you may already know from iOS are built-in regular expression support and data detectors.

The [`NSRegularExpression`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSRegularExpression_Class/Reference/Reference.html#//apple_ref/occ/cl/NSRegularExpression) class represents a regular expression that you can apply to a string. After creating a regex instance ([`+regularExpressionWithPattern:options:error:`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSRegularExpression_Class/Reference/Reference.html#//apple_ref/occ/clm/NSRegularExpression/regularExpressionWithPattern:options:error:)), you use the Block iterator method [`enumerateMatchesInString:options:range:usingBlock:`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSRegularExpression_Class/Reference/Reference.html#//apple_ref/occ/instm/NSRegularExpression/enumerateMatchesInString:options:range:usingBlock:) to enumerate all matches in the specified string. Each match is represented by an [`NSTextCheckingResult`](http://developer.apple.com/library/mac/documentation/AppKit/Reference/NSTextCheckingResult_Class/Reference/Reference.html#//apple_ref/occ/cl/NSTextCheckingResult) instance.

To use regular expressions for searching and replacing text, use the [`stringByReplacingMatchesInString:options:range:withTemplate:`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSRegularExpression_Class/Reference/Reference.html#//apple_ref/occ/instm/NSRegularExpression/stringByReplacingMatchesInString:options:range:withTemplate:) method.

The class reference documentation for `NSRegularExpression` has a very detailed overview about the supported regex syntax.

[`NSDataDetector`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSDataDetector_Class/Reference/Reference.html#//apple_ref/occ/cl/NSDataDetector) is a subclass of `NSRegularExpression` that offers pre-configured regular expressions to identify patterns such as dates, addresses, phone numbers, or URLs.

## Miscellaneous

- The [`NSUserDefaults`)](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSUserDefaults_Class/) API now has better performance if accessed concurrently from multiple threads.
- `NSURLRequest` now supports HTTP pipelining with the `setHTTPShouldUsePipelining:` method. You can also specify a so-called network service type (`setNetworkServiceType:`) such as voice or video, supposedly to give the networking subsystem a hint how to prioritize the request.
- [`NSIndexSet`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSIndexSet_Class/Reference/Reference.html#//apple_ref/occ/cl/NSIndexSet) got three new methods to enumerate the non-contiguous ranges in the set rather than every single index. See `enumerateRangesUsingBlock:`.
- [`NSXMLParser`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSXMLParser_Class/Reference/Reference.html#//apple_ref/occ/cl/NSXMLParser) now has a streaming mode where parsing of a document can begin before its entire contents have been downloaded. You had to use libxml2 directly if you wanted to do this before. See the [`initWithStream:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSXMLParser_Class/Reference/Reference.html#//apple_ref/doc/uid/20001984-SW104) method. In addition, `NSXMLParser` is now thread-safe.
- `NSBundle` has a new method [`appStoreReceiptURL`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSBundle_Class/Reference/Reference.html#//apple_ref/doc/uid/20000214-DontLinkElementID_1) to get the location of the App Store receipt file without hard-coding relative paths in your bundle.

# OpenGL 3.2

Lion now supports OpenGL 3.2. Developers should select a specific OpenGL profile to tell the system which version of OpenGL an app is designed for. The current options are either `kCGLOGLPVersion_3_2_Core` for Open GL 3.2 or `kCGLOGLPVersion_Legacy`, which provides the same functionality found in earlier versions of Mac OS X.

See the [OpenGL Profiles section](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_pixelformats/opengl_pixelformats.html#//apple_ref/doc/uid/TP40001987-CH214-SW13) in Apple’s OpenGL Programming Guide for details.

# QTKit

[QTKit](https://developer.apple.com/reference/qtkit) provides two new classes that make it easier to export movies in different formats. It also features new APIs for reading movie metadata without having to use the QuickTime C API, which is not available in 64-bit apps.

The new `QTExportSession` class (not yet documented) represents an export process that produces a transcoded output from a given `QTMovie` source. The properties of the exported movie are specified by an instance of `QTExportOptions`. The initializer for an export session is the self-explaining `initWithMovie:exportOptions:outputURL:error:` method. After you have created the export session instance and set a delegate, send it a `run` message to start the export operation asynchronously. The session will inform its delegate about success (`exportSessionDidSucceed:`) or failure (`exportSession:didFailWithError:`) of the operation. It also informs regularly about progress while the operation is running (`exportSession:didReachProgress:`).

The export settings in the `QTExportOptions` class are specified by instantiating the class with one of the available format constants: `QTExportOptionsAppleM4VCellular`, `QTExportOptionsAppleM4V480pSD`, `QTExportOptionsAppleM4ViPod`, `QTExportOptionsAppleM4VAppleTV`, `QTExportOptionsAppleM4VWiFi`, `QTExportOptionsAppleM4V720pHD`, `QTExportOptionsQuickTimeMovie480p`, `QTExportOptionsQuickTimeMovie720p`, `QTExportOptionsQuickTimeMovie1080p`, `QTExportOptionsAppleM4A`. It does not seem possible to configure the export options in a more granular manner. See the `QTExportSession.h` and `QTExportOptions.h` header files for details.

The new metadata reading capabilities are based on the `QTMetadataItem` class. The `QTMovie` and `QTTrack` classes have been extended by new methods that return these metadata items. The `commonMetadata` method returns an array of `QTMetadataItem` objects for each common metadata key for which a value for the current locale is available.

Metadata can be available in several formats, including `QTMetadataFormatQuickTimeUserData`, `QTMetadataFormatQuickTimeMetadata`, `QTMetadataFormatiTunesMetadata` and `QTMetadataFormatID3Metadata`. The `availableMetadataFormats` method returns an array of those formats available for the current movie or track while the `metadataForFormat:` method lets you retrieve the metadata for a specific format.

# Quartz

`QLPreviewView` is a new class that allows you to embed a Quick Look preview into your own view hierarchy. Its designated initializer is `initWithFrame:style:`, giving you the option of two styles, `QLPreviewViewStyleNormal` and `QLPreviewViewStyleCompact`. After creating the view, just assign the item to preview (which must implement the `QLPreviewItem` protocol) to its `previewItem` property and add the view to your view hierarchy just as you would with any other view.

# Quartz Core

## Core Animation

### New Features from iOS

Several Core Animation classes inherited new properties that were introduced before in iOS 4. Examples:

- `CALayer` now has [`contentsScale`](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CALayer_class/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004500-CH1-SW158) and [`rasterizationScale`](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CALayer_class/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004500-CH1-SW157) properties. Setting the new [`shouldRasterize`](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CALayer_class/Introduction/Introduction.html#//apple_ref/occ/instp/CALayer/shouldRasterize) property to `YES` can improve rendering performance in some cases (especially during animations). [`shadowPath`](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CALayer_class/Introduction/Introduction.html#//apple_ref/occ/instp/CALayer/shadowPath) allows you to modify the shape of a layer’s drop shadow.
- `CAShapeLayer`: Use the [`strokeStart`](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html#//apple_ref/occ/instp/CAShapeLayer/strokeStart) and [`strokeEnd`](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html#//apple_ref/occ/instp/CAShapeLayer/strokeEnd) properties to restrict the region where the shape layer’s path is rendered to a subregion of the total.
- `CAKeyframeAnimation` has two new calculation modes for intermediate frames of a keyframe animation: [`kCAAnimationCubic`](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CAKeyframeAnimation_class/Introduction/Introduction.html#//apple_ref/c/data/kCAAnimationCubic) and [`kCAAnimationCubicPaced`](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CAKeyframeAnimation_class/Introduction/Introduction.html#//apple_ref/c/data/kCAAnimationCubic).

  > Intermediate frames are computed using a Catmull-Rom spline that passes through the keyframes. You can adjust the shape of the spline by specifying an optional set of [tension](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CAKeyframeAnimation_class/Introduction/Introduction.html#//apple_ref/occ/instp/CAKeyframeAnimation/tensionValues), [continuity](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CAKeyframeAnimation_class/Introduction/Introduction.html#//apple_ref/occ/instp/CAKeyframeAnimation/continuityValues), and [bias](http://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/CAKeyframeAnimation_class/Introduction/Introduction.html#//apple_ref/occ/instp/CAKeyframeAnimation/biasValues) values, which modify the spline using the standard Kochanek-Bartels form.

  Right. Got that?

### Remote Layer Clients and Servers

The new (not yet documented) classes `CARemoteLayerServer` and `CARemoteLayerClient` seem to allow one process to render a layer tree that is then displayed by another process. I guess this was introduced for the new XPC interprocess communication framework.

## Core Image Face Detection

One of the coolest new features of Lion is a public face detection API. Don’t confuse face detection (identifying the position and size of faces in an image) with face recognition (being able to tell if two faces show the same person or not). iPhoto can do the latter while the new API is “only” capable of the former.

Face detection is part of Core Image and therefore works on `CIImage` objects. The API is very easy to use, provided that you have converted the image you want to analyze into a `CIImage`. The source can either be a still image or a frame of a video.

The central class for face detection is `CIDetector`. Although it can only detect faces at the moment, Apple has designed the API in a generalized manner so that other detection algorithms can be easily added in the future. To detect faces, instatiate a `CIDetector` with the `+detectorOfType:context:options:` class method, passing `CIDetectorTypeFace` as the type. The `context` argument may be `nil` but you can improve performance if you pass in a `CIContext` instance that already has uploaded the image to be processed to the GPU. The `options` dictionary allows you to opt for higher accuracy or higher speed of the detection, depending on your needs.

Sending the detector instance a `featuresInImage:` method starts the detection process and returns an array of `CIFaceFeature` objects if any faces were found. Each face is describes by its `bounds` as well as the `leftEyePosition`, `rightEyePosition` and `mouthPosition`.
