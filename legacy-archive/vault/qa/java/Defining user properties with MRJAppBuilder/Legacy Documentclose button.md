---
title: Defining user properties with MRJAppBuilder
apple_id: DTS10001399
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-04-17'
source_url: https://developer.apple.com/library/archive/qa/java/java24.html
archived_at: '2026-07-18T02:29:42.379374Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA24Defining user properties with MRJAppBuilder |

|  |  |
| --- | --- |
| ---   Q: In JBindery there was a Properties panel that allowed me to enter in my own environment properties, but I see nothing like this when using MRJAppBuilder. How do I specify my own properties when using the MRJAppBuilder tool?  A: MRJAppBuilder does not present an interface like JBindery to handle user properties, but it is a trivial matter to add your own properties. Simply add your properties as "name = value" pairs to the MRJAppBuilder properties (configuration) file. For example, look at this sample properties file:   |  | | --- | | ``` # MRJApp.properties # # This file is intended for use with the MRJAppBuilder tool # to create a double-clickable launcher for this application. # MRJAppBuilder is part of the MRJ SDK. # # Version 1.0 03/22/2000  # Class containing 'main' com.apple.mrj.application.main = MainFrame # Add our jar to the classpath com.apple.mrj.application.classpath = $APPLICATION/MRJApp.jar # We have no parameters to main #com.apple.mrj.application.parameters = # Where to send stdout com.apple.mrj.application.stdout = $CONSOLE # Perhaps to a file? #com.apple.mrj.application.stdout = out.txt #com.apple.mrj.application.stdout.append = false # Where to send stderr com.apple.mrj.application.stderr = $CONSOLE # Perhaps to a file? #com.apple.mrj.application.stderr = err.txt #com.apple.mrj.application.stderr.append = false  # Any user properties mywebsite = http://developer.apple.com/java/ myfavoritecolor = green # etc.      ``` |    Once the application is built using this properties file, the custom properties can be accessed in the standard Java way using `System.getProperty("propertyname")`.  For more information on what MRJAppBuilder properties are available, or on how to use the MRJAppBuilder in general, please refer to the documentation included in the [MRJ SDK](https://developer.apple.com/java/text/download.html#sdk). [Apr 17 2000] |

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
