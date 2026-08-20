---
title: How to use URL Access with proxy servers
apple_id: DTS10001626
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-10-02'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1074.html
archived_at: '2026-07-18T02:38:06.625244Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A QA1074How to use URL Access with proxy servers |

|  |
| --- |
| ---   Q: How do I use URL Access in combination with a proxy server?  A: To use URL Access with proxy servers, nothing in your source code needs to change. URL Access uses the Internet Config APIs on both Mac OS 9 and Mac OS X in order to determine your proxy server settings. All you need to do is specify your proxy server address and port number. When running on Mac OS 9, you can set this programmatically by using the Internet Config APIs or manually by using the Internet control panel.  Just launch the control panel and select the 'Advanced' tab and then scroll down to the 'Firewalls' section. If your Internet control panel doesn't have an 'Advanced' tab, simply select the 'User Mode' menu item located in the 'Edit' menu and then choose 'Advanced'.        When running on Mac OS X, you can use the Internet Config APIs to read the values for proxy server settings, however, to change these settings, you must use the SystemConfiguration.framework APIs.  Alternatively, you can configure your proxy server settings using the Network panel inside the System Preferences application. First, select the device that you need to use the proxy server with (most likely Built-in Ethernet), and then click the 'Proxies' tab. Just enter your proxy server address in the 'Web Proxy' field and you're all set.     ---  [Oct 02 2001] |
|  |

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
