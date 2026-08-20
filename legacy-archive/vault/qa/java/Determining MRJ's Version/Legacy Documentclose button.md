---
title: Determining MRJ's Version
apple_id: DTS10001392
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-09-27'
source_url: https://developer.apple.com/library/archive/qa/java/java17.html
archived_at: '2026-07-18T02:29:41.817235Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA17Determining MRJ's Version |

|  |  |
| --- | --- |
| ---   Q: How can I tell what version of MRJ I am currently using?  A: There are a couple ways to determine what version of MRJ is active. At run time you can look for the `mrj.version` property as shown below. If the property is not found, the System will return null, which is why we test for this case in the code:   |  | | --- | | ``` String version = System.getProperty("mrj.version"); if (version == null)     System.out.println("Not running with MRJ"); else     System.out.println("mrj.version: " + version); ``` |    Unfortunately, versions of MRJ prior to 2.2 EA2 have a security manager which does not allow un-trusted Applets to access this property, meaning there is no guaranteed runtime version checking available for Applets running under older versions of MRJ.  Alternatively, you can use the __Get Info__ command in the Finder to look at the version information of the MRJLib file. The MRJLib file is located in the "MRJ Libraries" folder inside the "Extensions" folder of your active System Folder.  Keep in mind, however, that MRJ gets loaded using the normal Shared Library loading methods. This means that if there is a copy of MRJ in the same folder as the application using it, the application will find and use the MRJ in its folder rather than the one in the System Folder. Using the `mrj.version` property is a foolproof method to determine which version is currently running. [Sep 27 1999] |

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
