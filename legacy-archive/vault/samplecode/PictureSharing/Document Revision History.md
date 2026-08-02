---
title: PictureSharing
apple_id: DTS10000712
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2013-08-15'
source_url: https://developer.apple.com/library/archive/samplecode/PictureSharing/History/History.html
archived_at: '2026-07-18T03:19:00.907033Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PictureSharing](PictureSharing.md)


[Previous](Server-ServerAppDelegate.m.md)

# Document Revision History

This table describes the changes to _PictureSharing_.

| __Date__ | __Notes__ |
| 2013-08-15 | A relatively minor update to adopt the latest techniques and fix two developer-reported bugs (r. 10081345) (r. 12682482). |
| 2010-12-01 | Fixed a small but significant bug in the handling of the moreComing flag in the browser (r. 8667473). Also, to reduce confusion when there are two services of the same name, the browser now displays the domain of each service and lets you cancel a download by simply clicking on another service to start a new download. |
| 2010-08-06 | A major rewrite to bring the code in line with the latest best practices. Specifically, this release merged the PictureSharing and PictureSharingBrowser samples, added IPv6 support, adopted bindings, adopted NSOperation to encapsulate the async file transfer, added a simple protocol to detect file transfer errors, eliminated pointless Bonjour resolves, added support for automatic Bonjour service renaming and persistence, and eliminated NSFileHandle in favour of NSStream. |
| 2009-06-04 | Base SDK changed to 10.6. |
| 2005-02-08 | Upgraded project to use native Xcode target |

[Previous](Server-ServerAppDelegate.m.md)

