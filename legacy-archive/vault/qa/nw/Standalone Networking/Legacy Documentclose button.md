---
title: Standalone Networking
apple_id: DTS10001471
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-03-15'
source_url: https://developer.apple.com/library/archive/qa/nw/nw59.html
archived_at: '2026-07-18T02:29:47.471887Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A NW59Standalone Networking |

|  |  |
| --- | --- |
| ---    ---   Q: I'm developing TCP/IP client/server applications and want to run the client and the server on the same machine. However, I'm not on an Ethernet network, so I don't have a constant Internet connection or a fixed IP address. How can I get TCP/IP to work on my standalone machine, without having to dial into my ISP every time?  A: The easiest way to set up a single-machine network is to tunnel TCP/IP through AppleTalk, and set AppleTalk to use a "null" connection that won't connect to the outside world. You can use this on a machine with dial-up Internet access (to avoid having to dial up just to test your apps) or even on a totally disconnected PowerBook in the middle of the Kalahari desert.  Here's how to set it up:   1.  Make sure you've installed Remote Access / PPP software -- this is an optional install in Mac OS 8.5. If you didn't install it, you can run the OS installer again and do a custom install, just selecting    that one option. (Actually, the only portion of this package that you need is the "Remote Only" extension, so if you already have that, you're set.) 2. Use a text editor like SimpleText to create a plain text file in your Preferences folder named "hosts". Put the    following lines in the "hosts" file:      |  |    | --- |    | ``` localhost CNAME foo.bar.com foo.bar.com A 127.0.0.1 ``` |      The domain name is arbitrary; the important part is the alias, which lets you use the standard TCP/IP convention of referring    to your machine by name as "`localhost`". 3. Open the AppleTalk control panel. If you have an existing AppleTalk configuration that you want to preserve, use the    Configurations menu command to create a new one first. Now set the "Connect Via:" pop-up to "Remote Only". (If you don't see the pop-up or that item, double-check that the Remote Only extension was installed by the Remote Access/PPP installer.) This will enable AppleTalk via a "loopback" so it won't need or    use a physical network connection. 4. Open the TCP/IP control panel. If you have an existing TCP/IP configuration that you want to preserve, use the Configurations menu command to create a new one first. Set "Connect Via:" to    "AppleTalk (MacIP)". Then set the "Configure:" pop-up to "Using MacIP Manually" and set the IP address to "192.168.1.1", which is in the range reserved for private    networks. You can leave the rest of the text fields in the control panel blank. Then press the button "Select Hosts File...", and choose your "hosts" file (in the Preferences folder) from the file dialog that appears.   You are now ready to set up TCP/IP connections between applications running on your machine, even if you have no actual network connection. The IP address to connect to is "`localhost`" or "`127.0.0.1`".  If you want to be able to switch between this and other networking configurations like PPP or Ethernet, you can create named configurations in the control panels and then set up multiple locations in the Location Manager control panel to switch between the configurations. It takes a little work to set up, but you can then use the Control Strip to switch configurations with a single mouse click. |

#### [Mar 15 1999]

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
