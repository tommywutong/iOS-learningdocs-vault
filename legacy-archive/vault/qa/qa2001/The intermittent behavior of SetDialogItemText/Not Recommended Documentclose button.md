---
title: The intermittent behavior of SetDialogItemText
apple_id: DTS10001634
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-10-30'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1082.html
archived_at: '2026-07-18T02:38:11.664439Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Human Interface Toolbox](https://developer.apple.com/library/archive/technicalqas/Carbon/idxHumanInterfaceToolbox-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A QA1082The intermittent behavior of SetDialogItemText |

|  |  |
| --- | --- |
| ---   Q: While updating some 'Classic' Dialog Manager code for Carbon I have noticed odd behavior with `SetDialogItemText`. Sometimes it works, other times it doesn't. I haven't been able to find a pattern for the misbehavior and I'm vexed. Will exorcism help?  A: Although a little exorcism never hurt anyone, our bet is it's not going to solve your problem. What you need to do is ask yourself the question, "Do I have an embedding hierarchy in my dialog?"  When embedding is on, you must pass the `ControlRef` returned by `GetDialogItemAsControl` to `SetDialogItemText`, not the item Handle returned by `GetDialogItem`.   |  | | --- | | ``` ControlRef theControlRef;  GetDialogItemAsControl(theDialog, theDItem, &theControlRef); SetDialogItemText((Handle)theControlRef, theText); ``` |     This is one of those often missed, sometimes forgotten facts. Documentation for this behavior can be found in the Inside Carbon Dialog Manager Reference under the section "[Handling Text in Alert and Dialog Boxes.](https://developer.apple.com/documentation/Carbon/HumanInterfaceToolbox/DialogManager/Dialog_Manager/Functions/Handling_Tex_Dialog_Boxes.html)"  Note: The current Appearance savy way to set text is by using the `SetControlData` API with the `kControlEditTextTextTag` tag then calling `DrawOneControl` to draw the item.   - [Dialog   Manager](https://developer.apple.com/documentation/Carbon/HumanInterfaceToolbox/DialogManager/dialogmanager.html)    - [SetControlData](https://developer.apple.com/documentation/Carbon/HumanInterfaceToolbox/ControlManager/Control_Manager/Functions/Accessing_Co_ngs_and_Data.html#//apple_ref/C/func/SetControlData) - [Editable   Text Control Data Tag Constants](https://developer.apple.com/documentation/Carbon/HumanInterfaceToolbox/ControlManager/Control_Manager/Enumerations/Editable_Tex_ag_Constants.html)  ---  [Oct 30 2001] |

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
