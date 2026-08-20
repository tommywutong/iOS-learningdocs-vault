---
title: Using Ink Services in Your Application
apple_id: TP40000959
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2003-07-24'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/using_ink/ink_glossary/ink_glossary.html
archived_at: '2026-07-15T05:25:24.246617Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Using Ink Services in Your Application](Introduction%20to%20Using%20Ink%20Services%20in%20Your%20Application.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __deferred recognition__

  The process of recognizing an ink phrase that was drawn by the user at an earlier time.

- __event coalescing__

  See [mouse event coalescing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnbvfvbeeq2di5cegri).

- __gesture__

  A handwritten mark that is recognized as having a special meaning, such as, Select All, Cut, and Copy.

- __Ink__

  Raw data that represents the input drawn by the user with the stylus.

- __Ink pad__

  The part of the Ink window that provides a simple note pad interface where handwritten input is converted into editable text.

- __Ink phrase__

  The grouping of ink data created by the recognition system, based on the timing and spacing of the user's handwriting. In Roman languages, an ink phrase is typically a short string of characters with no spaces between them such as an individual character, several characters, a word, or, an entire URL. For most situations an Ink phrase is equivalent to a word.

- __Ink server__

  The component of Ink technology that manages the recognizer, the language model, and the Ink window.

- __Ink text__

  Words written in electronic ink.

- __Ink input method__

  A low-level task which takes the user input and then draws the appropriate data on the screen. In effect, converting physical pen strokes into electronic Ink.

- __Ink text object__

  An opaque object that contains information about an Ink phrase.

- __Ink toolbar__

  The toolbar that appears at the top of the Ink window.

- __Ink window__

  Comprised of the Ink toolbar and the Ink pad, allows the user to control various aspects of Ink and to enter Ink input.

- __Ink writing guides__

  The lines (alternating solid and broken) that appear when a user is writing directly into an application.

- __instant mousing area__

  An area in which stylus input is interpreted as mouse input; the system “instantly” interprets the stylus as a mouse in these special places and ink is not generated.

- __mouse event coalescing__

  A process that merges `mouseMoved` and `mouseDragged` events by checking to see if one of these events exists in the event queue, and if it does, updating the queue with the position and delta information from the more recently-generated event.

- __pen__

  See [stylus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnbvfvbeeq2ki5ceeqq).

- __pen event__

  A mouse event that contains tablet data.

- __phrase termination__

  Defines when Ink input should be processed by the recognizer.

- __recognized text__

  Ink words processed by the recognition system.

- __recognizer__

  The algorithmic component of Ink Services that identifies written text and gestures.

- __searchable Ink__

  Ink that remains visible to the user as ink, but for which recognition has taken place.

- __stroke__

  An array of points that define the path of the stylus, starting with a stylus-down event and ending when the stylus is lifted.

- __stylus__

  The hand held instrument used to enter data into the computer. Also referred to as a [pen](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnbvfvbeeq2kjjeucqq).

- __targeted gesture__

  A gesture that has a defined hot spot that an application can use to determine the area to which the gesture should apply.

- __tentative gesture__

  Ink that the system treats tentatively as a gesture until your application either confirms the Ink is indeed a gesture or informs the system the Ink is not a gesture. The Join gesture is the only tentative gesture.

- __termination mode__

  The conditions that define the end of an Ink phrase.

- __untargeted gesture__

  A gesture that does not have a defined hot spot. An application should apply the gesture to the current selection or insertion point.

[Previous](Document%20Revision%20History.md)

