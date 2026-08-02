---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/FinderSync.html
archived_at: '2026-07-18T02:53:02.234999Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# FinderSync Changes for Objective-C

### FinderSync

#### FinderSync.h

Modified [-[FIFinderSync beginObservingDirectoryAtURL:]](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501578-beginobservingdirectory)

|  | Declaration |
| --- | --- |
| From | ``` - (void)beginObservingDirectoryAtURL:(NSURL *)url ``` |
| To | ``` - (void)beginObservingDirectoryAtURL:(NSURL * _Nonnull)url ``` |

Modified [-[FIFinderSync endObservingDirectoryAtURL:]](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501582-endobservingdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` - (void)endObservingDirectoryAtURL:(NSURL *)url ``` |
| To | ``` - (void)endObservingDirectoryAtURL:(NSURL * _Nonnull)url ``` |

Modified [-[FIFinderSync menuForMenuKind:]](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501585-menu)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMenu *)menuForMenuKind:(FIMenuKind)menu ``` |
| To | ``` - (NSMenu * _Nullable)menuForMenuKind:(FIMenuKind)menu ``` |

Modified [-[FIFinderSync requestBadgeIdentifierForURL:]](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501589-requestbadgeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestBadgeIdentifierForURL:(NSURL *)url ``` |
| To | ``` - (void)requestBadgeIdentifierForURL:(NSURL * _Nonnull)url ``` |

Modified [FIFinderSync.toolbarItemImage](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501580-toolbaritemimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSImage *toolbarItemImage ``` |
| To | ``` @property(copy, readonly, nonnull) NSImage *toolbarItemImage ``` |

Modified [FIFinderSync.toolbarItemName](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501574-toolbaritemname)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSString *toolbarItemName ``` |
| To | ``` @property(copy, readonly, nonnull) NSString *toolbarItemName ``` |

Modified [FIFinderSync.toolbarItemToolTip](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501590-toolbaritemtooltip)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSString *toolbarItemToolTip ``` |
| To | ``` @property(copy, readonly, nonnull) NSString *toolbarItemToolTip ``` |

Modified [+[FIFinderSyncController defaultController]](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501588-default)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)defaultController ``` |
| To | ``` + (instancetype _Nonnull)defaultController ``` |

Modified [FIFinderSyncController.directoryURLs](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501579-directoryurls)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSSet *directoryURLs ``` |
| To | ``` @property(copy) NSSet<NSURL *> * _Null_unspecified directoryURLs ``` |

Modified [-[FIFinderSyncController selectedItemURLs]](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501575-selecteditemurls)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)selectedItemURLs ``` |
| To | ``` - (NSArray<NSURL *> * _Nullable)selectedItemURLs ``` |

Modified [-[FIFinderSyncController setBadgeIdentifier:forURL:]](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501577-setbadgeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setBadgeIdentifier:(NSString *)badgeID forURL:(NSURL *)url ``` |
| To | ``` - (void)setBadgeIdentifier:(NSString * _Nonnull)badgeID forURL:(NSURL * _Nonnull)url ``` |

Modified [-[FIFinderSyncController setBadgeImage:label:forBadgeIdentifier:]](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501583-setbadgeimage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setBadgeImage:(NSImage *)image label:(NSString *)label forBadgeIdentifier:(NSString *)badgeID ``` |
| To | ``` - (void)setBadgeImage:(NSImage * _Nonnull)image label:(NSString * _Nullable)label forBadgeIdentifier:(NSString * _Nonnull)badgeID ``` |

Modified [-[FIFinderSyncController targetedURL]](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501595-targetedurl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSURL *)targetedURL ``` |
| To | ``` - (NSURL * _Nullable)targetedURL ``` |

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
