---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/AVKit.html
archived_at: '2026-07-18T02:57:22.591686Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# AVKit Changes for Objective-C

### AVKit

#### AVContentProposal.h (Added)

Added [AVContentProposal](https://developer.apple.com/documentation/avkit/avcontentproposal)Added [AVContentProposal.automaticAcceptanceInterval](https://developer.apple.com/documentation/avkit/avcontentproposal/1650963-automaticacceptanceinterval)Added [AVContentProposal.contentTimeForTransition](https://developer.apple.com/documentation/avkit/avcontentproposal/1650952-contenttimefortransition)Added [-[AVContentProposal initWithContentTimeForTransition:title:previewImage:]](https://developer.apple.com/documentation/avkit/avcontentproposal/1650945-init)Added [AVContentProposal.metadata](https://developer.apple.com/documentation/avkit/avcontentproposal/1650962-metadata)Added [AVContentProposal.previewImage](https://developer.apple.com/documentation/avkit/avcontentproposal/1650959-previewimage)Added [AVContentProposal.title](https://developer.apple.com/documentation/avkit/avcontentproposal/1650948-title)Added [AVContentProposal.URL](https://developer.apple.com/documentation/avkit/avcontentproposal/1650972-url)Added [AVPlayerItem.nextContentProposal](https://developer.apple.com/documentation/avfoundation/avplayeritem/1650942-nextcontentproposal)Added AVPlayerItem(AVContentProposal)

#### AVContentProposalViewController.h (Added)

Added [AVContentProposalViewController](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller)Added [AVContentProposalViewController.contentProposal](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/1650964-contentproposal)Added [AVContentProposalViewController.dateOfAutomaticAcceptance](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/1650975-dateofautomaticacceptance)Added [-[AVContentProposalViewController dismissContentProposalForAction:animated:completion:]](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/1650973-dismisscontentproposal)Added [AVContentProposalViewController.playerLayoutGuide](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/1650956-playerlayoutguide)Added [AVContentProposalViewController.playerViewController](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/1650967-playerviewcontroller)Added [AVContentProposalViewController.preferredPlayerViewFrame](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/1650954-preferredplayerviewframe)Added [AVPlayerViewController.contentProposalViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1650965-contentproposalviewcontroller)Added [AVContentProposalAction](https://developer.apple.com/documentation/avkit/avcontentproposalaction)Added [AVContentProposalActionAccept](https://developer.apple.com/documentation/avkit/avcontentproposalaction/avcontentproposalactionaccept)Added [AVContentProposalActionDefer](https://developer.apple.com/documentation/avkit/avcontentproposalaction/defer)Added [AVContentProposalActionReject](https://developer.apple.com/documentation/avkit/avcontentproposalaction/reject)Added AVPlayerViewController(AVContentProposalViewController)

#### AVPlayerViewController.h

Added [AVPlayerViewController.skipBackwardEnabled](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1650958-isskipbackwardenabled)Added [AVPlayerViewController.skipForwardEnabled](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1650953-isskipforwardenabled)Added [AVPlayerViewController.skippingBehavior](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1650947-skippingbehavior)Added [-[AVPlayerViewControllerDelegate playerViewController:didAcceptContentProposal:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/2181733-playerviewcontroller)Added [-[AVPlayerViewControllerDelegate playerViewController:didRejectContentProposal:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/2181735-playerviewcontroller)Added [-[AVPlayerViewControllerDelegate playerViewController:shouldPresentContentProposal:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/2181734-playerviewcontroller)Added [-[AVPlayerViewControllerDelegate playerViewController:timeToSeekAfterUserNavigatedFromTime:toTime:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1650960-playerviewcontroller)Added [-[AVPlayerViewControllerDelegate skipToNextItemForPlayerViewController:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1650950-skiptonextitem)Added [-[AVPlayerViewControllerDelegate skipToPreviousItemForPlayerViewController:]](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1650944-skiptopreviousitem)Added AVPlayerViewController(AVPlayerViewControllerSkippingBehavior)Added [AVPlayerViewControllerSkippingBehavior](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerskippingbehavior)Added [AVPlayerViewControllerSkippingBehaviorDefault](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerskippingbehavior/avplayerviewcontrollerskippingbehaviordefault)Added [AVPlayerViewControllerSkippingBehaviorSkipItem](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerskippingbehavior/skipitem)

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
