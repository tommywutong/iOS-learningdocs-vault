---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Objective-C/Foundation.html
archived_at: '2026-07-18T02:57:04.811310Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Foundation Changes for Objective-C

### Foundation

#### NSExpression.h

Modified [NSExpression.expressionBlock](https://developer.apple.com/documentation/foundation/nsexpression/1409139-expressionblock)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonnull) id  (^ _Nonnull)(id _Nullable, NSArray * _Nonnull, NSMutableDictionary * _Nullable) expressionBlock ``` |
| To | ``` @property(readonly, copy, nonnull) id  (^expressionBlock)(id, NSArray *, NSMutableDictionary *) ``` |

#### NSFileCoordinator.h

Modified [-[NSFileCoordinator prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:]](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1412420-prepareforreadingitemsaturls)

|  | Declaration |
| --- | --- |
| From | ``` - (void)prepareForReadingItemsAtURLs:(NSArray<NSURL *> * _Nonnull)readingURLs options:(NSFileCoordinatorReadingOptions)readingOptions writingItemsAtURLs:(NSArray<NSURL *> * _Nonnull)writingURLs options:(NSFileCoordinatorWritingOptions)writingOptions error:(NSError * _Nullable * _Nullable)outError byAccessor:(void (^ _Nonnull)(void (^ _Nonnull)(void) completionHandler))batchAccessor ``` |
| To | ``` - (void)prepareForReadingItemsAtURLs:(NSArray<NSURL *> *)readingURLs options:(NSFileCoordinatorReadingOptions)readingOptions writingItemsAtURLs:(NSArray<NSURL *> *)writingURLs options:(NSFileCoordinatorWritingOptions)writingOptions error:(NSError * _Nullable *)outError byAccessor:(void (^)(void (^completionHandler)(void)))batchAccessor ``` |

#### NSFilePresenter.h

Modified [-[NSFilePresenter relinquishPresentedItemToReader:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1410743-relinquishpresenteditemtoreader)

|  | Declaration |
| --- | --- |
| From | ``` - (void)relinquishPresentedItemToReader:(void (^ _Nonnull)(void (^ _Nullable)(void) reacquirer))reader ``` |
| To | ``` - (void)relinquishPresentedItemToReader:(void (^)(void (^reacquirer)(void)))reader ``` |

Modified [-[NSFilePresenter relinquishPresentedItemToWriter:]](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413688-relinquishpresenteditemtowriter)

|  | Declaration |
| --- | --- |
| From | ``` - (void)relinquishPresentedItemToWriter:(void (^ _Nonnull)(void (^ _Nullable)(void) reacquirer))writer ``` |
| To | ``` - (void)relinquishPresentedItemToWriter:(void (^)(void (^reacquirer)(void)))writer ``` |

#### NSPointerFunctions.h

Modified [NSPointerFunctions.acquireFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1410537-acquirefunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonnull) void * (* _Nullable)(const void * _Nonnull src, NSUInteger (* _Nullablesize)(const void * _Nonnull item), BOOL shouldCopy) acquireFunction ``` |
| To | ``` @property(nonnull) void * (*acquireFunction)(const void *src, NSUInteger (*size)(const void *item), BOOL shouldCopy) ``` |

Modified [NSPointerFunctions.descriptionFunction](https://developer.apple.com/documentation/foundation/nspointerfunctions/1415200-descriptionfunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(nullable) NSString * (* _Nullable)(const void * _Nonnull item) descriptionFunction ``` |
| To | ``` @property(nullable) NSString * (*descriptionFunction)(const void *item) ``` |

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
