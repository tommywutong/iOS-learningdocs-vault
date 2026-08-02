---
title: Creating serialVersionUIDs using MRJ
apple_id: DTS10001388
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/java/java13.html
archived_at: '2026-07-18T02:29:41.376158Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA13Creating serialVersionUIDs using MRJ |

|  |  |  |
| --- | --- | --- |
| ---   Q: Is there a tool to generate the `serialVersionUID` for a class on the Mac? (`serialver` is part of the JDK on windows).  A: Yes there is. The classes for it are included as part of the standard MRJ install. To run the `SerialVer` program you will need to use JBindery (part of the [MRJ SDK](https://developer.apple.com/sdk/index.html)).  To create a JBound application to run the `SerialVer` program:  Launch JBindery.  In the Command panel set the class name to:   |  | | --- | | ``` sun.tools.serialver.SerialVer ``` |   set the optional parameters to:   |  | | --- | | ``` -show ``` |  You will need to add the classes you are concerned with to the classpath. This can be done in a couple ways:   1. Add your jar file or classes to the "MRJClasses" folder (located at StartupDisk:System Folder:Extensions:MRJ Libraries:MRJClasses). 2. Modify the classpath in JBindery. To do this, you choose the Classpath panel in JBindery and add your classes. See the    [JBindery    documentation](https://developer.apple.com/documentation/java/MacOSandJava/JBindery/JBindery.html) for more information on the different ways to accomplish this.   Once you are done configuring the settings in JBindery, save the settings as an application, and use this resulting JBound application to launch the `SerialVer` program from the Finder.  As an example, I added a manual entry of `file:///$APPLICATION/` to my classpath. This adds the folder the JBound application is in to the classpath and is useful because the target classes can be moved into the folder, and then accessed from the `SerialVer` program.  By adding a manual entry of `file:///$APPLICATION/` to the classpath, the Java environment will look in this folder (the application's folder) for classes it needs to load. This requires the classes be ".class" files, and not ".zip" or ".jar "files, and it requires the classes to be placed in a directory structure which represents the package the class belongs to. For instance, if I wanted the application to be able to see my class named `Foo` which has been defined to be in the `levi.random.misc.stuff` package then I would arrange my files like this: |

|  |
| --- |
| arrangement example [May 17 1999] |

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
