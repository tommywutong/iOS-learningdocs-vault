---
title: Reserved Key Combinations
apple_id: DTS10002227
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/tb/tb41.html
archived_at: '2026-07-18T02:38:57.157228Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB41Reserved Key Combinations |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: I've noticed that when I type certain key combinations (particularly those involving the Shift and Option keys), nothing comes through to my application's event loop. These key combinations don't seem to be documented as reserved. What's happening?  A: You're probably running your app while a multi-byte script system's input method is active. It turns out that certain key combinations are reserved as meta-keys for communication with input methods, in addition to the usual assortment of reserved keys.  No, these input method meta-keys have not been documented before now.  So that the information will all be in one place, here is a complete list of key combinations we know of which may require avoidance or special handling on the part of an application:   | key combination | reserved by/for | effect/purpose | notes | | --- | --- | --- | --- | | Option-Shift  and  Option-Control | multi-byte script system input methods | meta-communication between the user and the input method | You can avoid conflicts with input methods by choosing not to pass the relevant key combinations to `TSMEvent`. However, this means input method users may not be able to perform essential tasks. | | Option | some third-party input methods | meta-communication between the user and the input method | This is not an error; some third-party input methods do indeed use key combinations involving the Option key with no other modifier key. | | Option-Control-Shift-Tab | Kotoeri (Japanese) input method | shows About Box | This behavior will be removed in a future release. | | Command-Tab | Mac OS 8.5  and later | switches to the next application | In Mac OS 8.5, the Application Switcher system extension reserves this combination, but in the future it may be built into the System file. | | Command-Space | System 7.0  and later | rotates to the default keyboard layout or input method in the next script | For details, see: Tech Info Library Articles 16481, [Keyboard Layouts: Availability and Installation](http://til.info.apple.com/techinfo.nsf/artnum/n16481), and 16378, [Command-Option-Space bar Application Conflict](http://til.info.apple.com/techinfo.nsf/artnum/n16378) | | Command-Option-Space | System 7.0  and later | rotates to the next keyboard layout or input method in the active script | For details, see: Tech Info Library Articles 16481, [Keyboard Layouts: Availability and Installation](http://til.info.apple.com/techinfo.nsf/artnum/n16481), and 16378, [Command-Option-Space bar Application Conflict](http://til.info.apple.com/techinfo.nsf/artnum/n16378) | | Command-Option-Escape | System 7.0  and later | performs "force quit" on current application | For details, see: Tech Info Library Article 7110, [How to Quit from an Application That Hangs](http://til.info.apple.com/techinfo.nsf/artnum/n7110) | | Command-Shift-<digit> | Mac OS  (all versions) | invokes system function or Fkey code resource | For details, see: Inside Macintosh / Macintosh Toolbox Essentials / Chapter 2 - Event Manager / Using the Event Manager / [Responding to Keyboard Events](https://developer.apple.com/documentation/mac/Toolbox/Toolbox-40.html#HEADING40-39) | | Command-/  and  Command-? | System 7.0  and later | invokes Apple Guide |  | | Control-[, ], @, \ or + | Kotoeri (Japanese) input method | none | Due to a problem with `'itlk'` resources in Mac OS-J, these control key combinations do not always generate events. The `'itlk'` resources will be fixed in a future release. |   This document deliberately omits mention of the Power key because:     - Third-party applications don't need or want to respond to it,   nor should they. - Responding to it doesn't involve `keyDown`   events.  [May 17 1999] |

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
