---
title: Using the QuickTime for Java libraries on OS X
apple_id: DTS10001610
resource_type: QA
platform: Java
topic: Languages & Utilities
technology: null
published: '2002-04-08'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1058.html
archived_at: '2026-07-18T02:38:06.168307Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > QuickTime](https://developer.apple.com/referencelibrary/Java/idxQuickTime-date.html)

|  |
| --- |
| Technical Q&A QA1058Using the QuickTime for Java libraries on OS X |

|  |
| --- |
| ---   Q: I'm writing a QuickTime for Java application and receive "class not found" errors for the QTJ classes at compile-time. Isn't QTJ installed with OS X?  A: Yes, the QuickTime for Java libraries are installed by default with Mac OS X. They are not, however, included in the bootclasspath for the system, which is used by most IDEs such as ProjectBuilder or JBuilder when building and running Java projects.  The QuickTime for Java libraries are stored in:  `/System/Library/Java/Extensions/QTJava.zip`  And they will need to be referenced by your IDE in order for them to be recognized in your import statements. To add the QTJ libraries in Project Builder, for example:     1. Select "Add Files..." from the "Project"    menu 2. Navigate to the path above, select QTJava.zip 3. Click "Open".   Project Builder should now recognize your use of the QTJ classes. It is not necessary to include the actual JAR file in your compiled app, as its location in the system extensions area of the JavaVM Framework will have it included during runtime automatically. These steps are only necessary for compile-time recognition of the QuickTime for Java libraries.   ---  [Apr 08 2002] |

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
