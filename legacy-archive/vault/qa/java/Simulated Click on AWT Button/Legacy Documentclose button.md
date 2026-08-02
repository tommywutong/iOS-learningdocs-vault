---
title: Simulated Click on AWT Button
apple_id: DTS10001376
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-07'
source_url: https://developer.apple.com/library/archive/qa/java/java01.html
archived_at: '2026-07-18T02:29:40.562578Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA01Simulated Click on AWT Button |

|  |  |
| --- | --- |
| ---   Q: How do I programmatically make my `java.awt.Button` behave as if it were clicked on by the user?  A: This is typically desired when implementing default buttons and giving feedback that the default button action was performed when the Enter or Return key was pressed. There are other instances where this makes good sense from a user interface standpoint. The Macintosh Runtime for Java (MRJ) has provisions for this behavior built in. To get this behavior you need to pass a key-pressed event to the target button. Here is an example of how this could be achieved:   |  | | --- | | ``` import java.awt.Button; import java.awt.Toolkit; import java.awt.event.KeyEvent; public class SimulateClick {      /**      * A function to simulate a click on the target button.      * This will make the button draw as if it had been pressed and      * released, and the button will fire an Action event as if      * the button were pressed.      * For use with the Apple MRJ 2.1 EA3 and later.      */     static protected void simulateClick(Button target)     {         if (target != null)         {             KeyEvent keyEvent =     new KeyEvent(target, KeyEvent.KEY_PRESSED,        System.currentTimeMillis(), 0, KeyEvent.VK_ENTER,        (char)KeyEvent.VK_ENTER);             target.dispatchEvent(keyEvent);         }     } }    ``` | |

#### [Feb 03 1999]

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
