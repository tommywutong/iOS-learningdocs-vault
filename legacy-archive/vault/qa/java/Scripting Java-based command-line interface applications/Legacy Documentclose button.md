---
title: Scripting Java-based command-line interface applications
apple_id: DTS10001391
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/java/java16.html
archived_at: '2026-07-18T02:29:41.752608Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA16Scripting Java-based command-line interface applications |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: How do I run a command-line Java application from AppleScript without getting a timeout? Since I have no interface components, the supplied MRJ `'aete'` doesn't help. When I ask to generate a dictionary for the command-line class, MyParser, I just get a "MyParser" Class without methods, i.e., there is no "main" verb corresponding to the main method.  So I put the command-line parameters into JBindery and tell the JBound application to run. The JBound "MyParser" application runs fine and quits, but nothing is returned to the calling AppleScript. As a result, the event times out. How do I make this work correctly?  A: The [MRJ scripting model](https://developer.apple.com/documentation/mac/IAC/IAC-307.html) is very similar to scripting an ordinary scriptable Mac application. You have a scriptable application running and you send scripting commands to it. Typically, you would make a JBound application, launch it, and script it by addressing one of its AWT-based windows.  If you are working with a command-line-based Java application that doesn't create any AWT windows, then your application is not following the typical MRJ scripting model. To script your application, you will need to follow a few extra steps in order to be able to use scripting.  First, you need a Java shell application that is running to send scripting commands. You can write a trivial application that has an empty `main()`, or you can use any existing Java application and treat it as a shell.  The next requirement is to ensure that the jar file that contains `main()` used by the command-line application is on the class path. If the jar file is already in the "MRJClasses" folder, you don't need to do anything. If your jar is not in the "MRJClasses" folder, you will need to add it to the classpath using the following script:   |  | | --- | | ``` tell application "myJavaShell"    start tool alias "HD:myJavaStuff:TrivialClass.jar" selecting null end tell ``` |   Now you can invoke main:   |  | | --- | | ``` tell application "myJavaShell"    apply to class "com.xyz.TrivialClass" java method "main" parameters { "alpha", "beta"} end tell ``` |   But you still will not get any result since your class is declared to return void:   |  | | --- | | ``` static void main(String args[]){...} ``` |   If you want to get the output of the console window, you can do the following:   |  | | --- | | ``` tell application "myJavaShell"     get text content of text area 1 of window 1 end tell ``` |  [Apr 27 1999] |

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
