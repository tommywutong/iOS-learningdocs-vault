---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/FinderSync.html
archived_at: '2026-07-18T02:52:24.545437Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# FinderSync Changes

## FinderSync

Removed FIFinderSyncController.setBadgeImage(NSImage!, forBadgeIdentifier: String!)Added FIFinderSyncAdded FIFinderSyncController.setBadgeImage(NSImage!, label: String!, forBadgeIdentifier: String!)Modified FIFinderSyncController

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | NSExtensionContext |

Modified FIFinderSyncController.directoryURLs

|  | Declaration |
| --- | --- |
| From | ``` var directoryURLs: NSSet! ``` |
| To | ``` var directoryURLs: Set<NSObject>! ``` |

Modified FIFinderSyncProtocol

|  | Name | Protocols |
| --- | --- | --- |
| From | FIFinderSync | NSObjectProtocol |
| To | FIFinderSyncProtocol | -- |

Modified FIFinderSyncProtocol.beginObservingDirectoryAtURL(NSURL!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified FIFinderSyncProtocol.endObservingDirectoryAtURL(NSURL!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified FIFinderSyncProtocol.menuForMenuKind(FIMenuKind) -> NSMenu!

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified FIFinderSyncProtocol.requestBadgeIdentifierForURL(NSURL!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified FIFinderSyncProtocol.toolbarItemImage

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional var toolbarItemImage: NSImage! { get } ``` | -- |
| To | ``` @NSCopying optional var toolbarItemImage: NSImage! { get } ``` | yes |

Modified FIFinderSyncProtocol.toolbarItemName

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified FIFinderSyncProtocol.toolbarItemToolTip

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

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
