---
title: Using stdin on the Macintosh
apple_id: DTS10001377
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-07'
source_url: https://developer.apple.com/library/archive/qa/java/java02.html
archived_at: '2026-07-18T02:29:40.618261Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA02Using stdin on the Macintosh |

|  |
| --- |
| ---   Q: How do I use `stdin` to get user input on the Macintosh?  A: To use standard in on the Mac you will need to use JBindery (part of the [MRJ SDK](https://developer.apple.com/sdk/index.html)) to make a double-clickable Macintosh application out of your class. Make sure you are using version 2.1 EA3 (or later) of the SDK. This will only work with an application (no applets), so your code will need a `static public void main(String args[])` method defined as the entry point. Once you create your class as an application, you drag-and-drop the `.class` file on the JBindery application in the MRJ SDK. It will present you with a multitude of options. The ones we care about for this case are in the "Command" section (the one that comes up by default). Use the "Redirect stdin:" popup to change it to "Message Window". Then click on the "Save Settings..." button and save your settings as an application using the standard save dialog presented. Once this is done, you can run your application by double-clicking on the newly saved app, and use the messages window for `stdin` and `stdout`. For more detailed information about this or about using JBindery in general, please refer to the JBindery documentation in the MRJ SDK. |

#### [Dec 07 1998]

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
