---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/PubSub.html
archived_at: '2026-07-18T02:52:35.680409Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# PubSub Changes

## PubSub

Removed PSClientRemoved PSClient.addFeed(PSFeed!) -> BoolRemoved PSClient.addFeedWithURL(NSURL!) -> PSFeed!Removed PSClient.allClientBundleIdentifiers() -> [AnyObject]! [class]Removed PSClient.applicationClient() -> PSClient! [class]Removed PSClient.dateLastUpdatedRemoved PSClient.delegateRemoved PSClient.entryWithIdentifier(String!) -> PSEntry!Removed PSClient.feedWithIdentifier(String!) -> PSFeed!Removed PSClient.feedWithURL(NSURL!) -> PSFeed!Removed PSClient.feedsRemoved PSClient.init(forBundleIdentifier: String!)Removed PSClient.isPrivateRemoved PSClient.removeFeed(PSFeed!) -> BoolRemoved PSClient.sendChangesSinceDate(NSDate!)Removed PSClient.settingsRemoved PSClient.signatureRemoved PSFeedRemoved PSFeed.URLRemoved PSFeed.init(URL: NSURL!)Removed PSFeed.XMLRepresentation() -> NSXMLElement!Removed PSFeed.XMLRepresentationWithEntries(Bool) -> NSXMLElement!Removed PSFeed.alternateURLRemoved PSFeed.clientRemoved PSFeed.init(data: NSData!, URL: NSURL!)Removed PSFeed.dateUpdatedRemoved PSFeed.entriesRemoved PSFeed.entryEnumeratorSortedBy([AnyObject]!) -> NSEnumerator!Removed PSFeed.extensionXMLElementsUsingNamespace(String!) -> [AnyObject]!Removed PSFeed.feedFormatRemoved PSFeed.iconURLRemoved PSFeed.identifierRemoved PSFeed.lastErrorRemoved PSFeed.linksRemoved PSFeed.localDateUpdatedRemoved PSFeed.loginRemoved PSFeed.logoURLRemoved PSFeed.redirectedURLRemoved PSFeed.refresh(NSErrorPointer) -> BoolRemoved PSFeed.refreshingRemoved PSFeed.rightsRemoved PSFeed.setPassword(String!)Removed PSFeed.settingsRemoved PSFeed.subtitleRemoved PSFeed.timeZoneUpdatedRemoved PSFeed.titleRemoved PSFeed.unreadCountAdded NSObject.enclosure(PSEnclosure!, downloadStateDidChange: PSEnclosureDownloadState)Added NSObject.feed(PSFeed!, didAddEntries:[AnyObject]!)Added NSObject.feed(PSFeed!, didChangeFlagsInEntries:[AnyObject]!)Added NSObject.feed(PSFeed!, didRemoveEntriesWithIdentifiers:[AnyObject]!)Added NSObject.feed(PSFeed!, didUpdateEntries:[AnyObject]!)Added NSObject.feedDidBeginRefresh(PSFeed!)Added NSObject.feedDidEndRefresh(PSFeed!)

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
