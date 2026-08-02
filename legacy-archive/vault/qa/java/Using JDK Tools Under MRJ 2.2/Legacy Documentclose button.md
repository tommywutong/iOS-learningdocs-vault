---
title: Using JDK Tools Under MRJ 2.2
apple_id: DTS10001398
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-02-02'
source_url: https://developer.apple.com/library/archive/qa/java/java23.html
archived_at: '2026-07-18T02:29:42.159323Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA23Using JDK Tools Under MRJ 2.2 |

|  |  |
| --- | --- |
| ---   Q: When I try to use tools from the MRJ SDK 2.2, I cannot get them to run because it thinks I don't have the right classes installed. What's the problem? This used to work just fine under MRJ 2.1.4 and earlier.  A: You are most likely seeing a either a dialog similar to this:  launch error  or a message in the console similar to this:   |  | | --- | | ``` java.lang.NoClassDefFoundError: sun/tools/javac/Main     at com.apple.mrj.sdk.apps.Javac.invokeCoreTool(Javac.java)     at com.apple.mrj.sdk.apps.JDKTool.executeTool(JDKTool.java)     at com.apple.mrj.sdk.apps.JDKTool$1.actionPerformed(JDKTool.java)     at java.awt.Button.processActionEvent(Button.java)     at java.awt.Button.processEvent(Button.java)     at java.awt.Component.dispatchEventImpl(Component.java)     at java.awt.Component.dispatchEvent(Component.java)     at java.awt.EventDispatchThread.run(EventDispatchThread.java) ``` |    The dialog is a result of not having the "MRJSDKClasses.zip" in your MRJClasses folder and MRJ cannot locate the main class from which to launch the tool.  The console stack trace message is a result of not having the "JDKToolsClasses.zip" in your MRJClasses folder, and MRJ cannot locate the underlying support classes for the tool.  In order to make the MRJ installation more streamlined in MRJ 2.2, the most commonly used classes are installed automatically, while some of the more abstract, or developer-level, classes have been separated out into additional zip files. The "MRJSDK:Extensions" folder contains Java classes you may need at runtime. MRJ does not use these classes for normal applications and applets. They include "MRJSDKClasses.zip", "JDKToolsClasses.zip", and "JDKI18nClasses.zip."  __MRJSDKClasses.zip__  MRJSDKClasses.zip is required for running the JDK tools.  __JDKToolsClasses.zip__  JDKToolsClasses.zip is required for running the JDK tools. The classes in this file were formerly included in the MRJ 2.1.x installation.  __JDKI18nClasses.zip__  You will need this file only if you want to use Sun's char-to-byte and byte-to-char converter classes directly for various localized scripts. The classes in this file were formerly included in the MRJ 2.1.x installation.  Earlier versions of the MRJ SDK 2.1 Installer installed two files which are no longer needed. If they still exist on your system, you need to remove them manually. They include:   - "Properties.zip" (remove from the MRJ Libraries:MRJClasses folder) - "MRJSDKLib" (remove from the MRJ Libraries folder)   The MRJ SDK 2.2 installer will automatically place the "MRJSDKClasses.zip" and "JDKToolsClasses.zip" in the MRJClasses folder of the active System folder. [Feb 02 2000] |

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
