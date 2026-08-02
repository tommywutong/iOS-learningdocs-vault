---
title: Using the MRJ with IE 5
apple_id: DTS10001401
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-08-14'
source_url: https://developer.apple.com/library/archive/qa/java/java26.html
archived_at: '2026-07-18T02:29:42.971302Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > User Experience](https://developer.apple.com/referencelibrary/Java/idxUserExperience-date.html)

|  |
| --- |
| Technical Q&A JAVA26Using the MRJ with IE 5 |

|  |  |  |
| --- | --- | --- |
| ---   Q: I am running an applet with Internet Explorer 5 and MRJ 2.2, and when my code attempts to connect to our server using `URLConnection`, the applet crashes. After this crash, the next interaction with the browser crashes the browser, and JNI panic messages show up in the Java Message Log. The call to `URL.openStream()` is in the call stack in the JNI panic message. I've verified that the URL is valid and correct in all cases. What is going on here?  A: MRJ 2.2 uses a new feature in IE 5 which allows the MRJ to use Internet Explorer's networking stack for network communication. This allows IE to provide applet caching and cookie support to MRJ hosted Java applets.  Unfortunately, due to some interoperability problems with this new applet caching code, you may run into problems with applets that make network connections. At the time of this writing, these issues are scheduled to be resolved with the release of MRJ 2.2.3. In the meanwhile, you can work around these issues by using one of two methods.  Perhaps the easiest way to work around this problem is to change Internet Explorer's cache settings by choosing __Preferences__ from the __Edit__ menu and going to the Advanced page. Select the Update pages: Always radio button under the Cache section of the preference dialog and then click __OK__. (See image, below.)    preferences  __Figure 1__. Internet Explorer preferences  The following is a description of these cache settings:  __Cache Once Per Session__   Checks for updated content only if you return to a Web page you visited in a previous Internet Explorer session. If the page has changed, Internet Explorer displays the newer version of the page and stores a copy in the cache.  __Never__   Displays Web pages you previously visited by downloading their content from the Web.  __Always__   Checks for updated content each time you return to a Web page. If the page has changed, Internet Explorer displays the newer version of the page and stores a copy in the cache.  In our case, we use __Always__ to prevent IE from caching the .jar file. This technique may be a little intrusive for the user, and it also has the side effect of turning off caching for web pages as well as applets. A second solution involves a code change to the applet, but does not require the user to modify these IE Preference settings:   |  |  | | --- | --- | | __Listing 1__. Replacing IE's `URLConnection` handler with a generic socket mechanism   |  | | --- | | ``` Instead of:      URLConnection httpConn = myUrl.openConnection(); use this code:     URLConnection httpConn =         new sun.net.www.protocol.http.HttpURLConnection(             url, url.getHost(), url.getPort()); ``` | |    If you choose to use this source code, for security purposes you will have to sign your applet. Instructions for applet signing can be found in [Technote 1175: Applet Signing with MRJ and JavaKey](https://developer.apple.com/technotes/tn/tn1175.html).  Again, these workarounds are only to be used if you are having problems with reliability of your Applet under MRJ 2.2.x and IE 5.0. If it ain't broke, don't fix it. A future release of the MRJ will address these issues more completely.  [Aug 14 2000] |

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
