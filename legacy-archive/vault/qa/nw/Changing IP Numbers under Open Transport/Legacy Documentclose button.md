---
title: Changing IP Numbers under Open Transport
apple_id: DTS10001455
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-11-27'
source_url: https://developer.apple.com/library/archive/qa/nw/nw43.html
archived_at: '2026-07-18T02:29:46.623224Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A NW43Changing IP Numbers under Open Transport |

|  |
| --- |
| ---   Q: If my web server is running along happily under OT (1.1 or 1.1.1), and the listener was bound to address 0.0.0.0, what happens when someone uses the control panel and changes the IP number? Right now it appears to just make the listener go deaf. I don't appear to receive connections on the new IP number, and if I use the control panel a second time to switch back to the original IP number, I don't get connections for that IP number either.  Is there some event that gets sent to the listener that I'm not looking for that tells me when this happens?  A: When an port changes its IP number, it is actually closing and re-opening. When OT closes a port, any endpoint that is plumbed to it is also closed, hence you will get no further events on that endpoint.  The first thing you need to do is check for the provider events such as `kOTProviderWillClose` and `kOTProviderIsClosed`.  You should also use the `OTRegisterAsClient` call and register a notifier for client events, such as `kOTPortDisabled`, `kOTPortEnabled`, `kOTPortOffline`, `kOTPortOnline`, `kOTClosePortRequest`, `kOTYieldPortRequest`, `kOTNewPortRegistered`.  You need to close up your endpoints and rebind them when the interface changes.  Q: How does any of this relate to eventual multi-homing? I assumed that if I bound to 0.0.0.0, I would be active on all interfaces and all their IP numbers for the life of the listener endpoint... doesn't look like that would be the case.  A: As far as multi-homing is concerned, we will have to wait for OT 1.5 to be certain about how that will behave. |

#### [Nov 27 1996]

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

---
