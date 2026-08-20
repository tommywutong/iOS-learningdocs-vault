---
title: Using .zip and .jar Files With Applets
apple_id: DTS10001379
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-02-22'
source_url: https://developer.apple.com/library/archive/qa/java/java04.html
archived_at: '2026-07-18T02:29:40.739511Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA04Using .zip and .jar Files With Applets |

|  |
| --- |
| ---   Q: Normally, when you run an applet, you have several class files, and an html file that calls your main class like this:  `<APPLET CODE="MyMainClass.class" WIDTH=200 HEIGHT=200>< /APPLET>`  What if I want to have all my classes in a .jar or .zip file? If this is possible, what html code do I now use to call the applet?  A: To load your applet classes from a .jar or .zip file, you need to use the " ARCHIVE" tag in your applet statement. An example of this would be:  `<APPLET ARCHIVE="classes.jar" CODE="MyMainClass.class" WIDTH=200 HEIGHT=200>< /APPLET>`  where "classes.jar" would be the name of your .jar or .zip file containing the "MyMainClass.class" and its supporting class files. |

#### [Feb 22 1999]

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
