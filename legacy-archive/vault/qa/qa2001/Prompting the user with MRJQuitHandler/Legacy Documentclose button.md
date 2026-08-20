---
title: Prompting the user with MRJQuitHandler
apple_id: DTS10001716
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-08-15'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1187.html
archived_at: '2026-07-18T02:38:17.397750Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > User Experience](https://developer.apple.com/referencelibrary/Java/idxUserExperience-date.html)

|  |
| --- |
| Technical Q&A QA1187Prompting the user with MRJQuitHandler |

|  |  |  |
| --- | --- | --- |
| ---   Q: My application needs to perform some closing actions when the user tries to quit using Command-Q or the application menu. How should I do that?  A: The expected behavior of any application on Mac OS X is to exit when encountering selection of the "Quit" item from the application menu, or its Command-Q keyboard equivalent. To satisfy such a requirement, all graphical Java applications on Mac OS X have this functionality provided automatically. It is possible, however, to execute code prior to the application's exit. To do so, you will need to register a class that implements the `com.apple.mrj.MRJQuitHandler` interface with your application. The class must provide an implementation of the `handleQuit()` method, and be registered with a call to `MRJApplicationUtils.registerQuitHandler()`.  To prompt the user before quitting, whether it be to save unchanged work or to simply confirm the quit action as a safeguard, a dialog can be brought up from within `handleQuit()`. Based on the user's response, you must either:   1. Quit the application by calling `System.exit()` 2. Abort the quit process by throwing `IllegalStateException`   A problem existed on versions of Mac OS X prior to 10.2 where showing a modal dialog from `handleQuit()` resulted in a hang if both an `MRJQuitHandler` and an `MRJAboutHandler` were registered. The workaround for those earlier versions is to show the dialog on a separate thread. Note that this is not a problem on 10.2, and the workaround is not necessary (see below for more).  Please note that the `handleQuit()` method is for executing code __before exiting__. It should be assumed that when execution of `handleQuit()` completes, the application will exit. The [javadocs](https://developer.apple.com/documentation/Java/Reference/Java/index.html) for `MRJQuitHandler` state that to abort the quit, `IllegalStateException` must be thrown. This includes waiting on any pending execution on a separate thread, such as the workaround above. This way, you can control exactly when the application exits with `System.exit()`. If all of your cleanup logic is to be performed within `handleQuit()`, and there is no need to abort or delay the exit, there should be no need to throw `IllegalStateException`.  The code below demonstrates a sample application that properly implements the `MRJQuitHandler` and safely prompts the user for a quit confirmation on Mac OS X 10.1 and 10.2. Note that `IllegalStateException` is thrown in the example below to abort the quit while the separate thread allows the user input to determine whether `System.exit(0)` should be called.     |  | | --- | | ``` import javax.swing.*; import java.awt.*; import com.apple.mrj.*;  public class MRJHandlerTest extends JFrame implements MRJQuitHandler {      public MRJHandlerTest() {         super("TestProject");         getContentPane().add(new JLabel(             "<HTML><CENTER>To test the MRJQuitHandler, " +             "select \"Quit MRJHandlerTest\" " +             "from the application menu.</CENTER></HTML>"));         MRJApplicationUtils.registerQuitHandler(this);     }      public void handleQuit() {         // Workaround for 2868805:  show modal dialogs in a separate thread.         // This encapsulation is not necessary in 10.2,          // but will not break either.         SwingUtilities.invokeLater(new Runnable() {             public void run() {                 // Show the dialog and act accordingly.                 int result = JOptionPane.showConfirmDialog(null,                     "Do you really want to quit?",                     "Really Quit?",                     JOptionPane.YES_NO_OPTION,                     JOptionPane.QUESTION_MESSAGE);                 if (result == JOptionPane.YES_OPTION) {                     System.exit(0);                 }             }         });          // Throw IllegalStateException so new thread can execute.           // If showing dialog on this thread in 10.2, we would throw         // upon JOptionPane.NO_OPTION         throw new IllegalStateException("Quit Pending User Confirmation");     }      public static void main(String[] args) {         new MRJHandlerTest().setVisible(true);     } } ``` | | __Listing 1__. Proper use of `MRJQuitHandler`. |       ---  [Aug 13 2002] |

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
