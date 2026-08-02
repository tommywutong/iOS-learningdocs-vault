---
title: Using AppleScript to send an email with an attachment
apple_id: DTS10001572
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-01-04'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1018.html
archived_at: '2026-07-18T02:38:01.829474Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [Calling an AppleScript and providing parameters from an Application](qa1111.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Scripting & Automation](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxScripting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Scripting & Automation > Internet & Web](https://developer.apple.com/referencelibrary/ScriptingAutomation/idxInternetWeb-date.html)

|  |
| --- |
| Technical Q&A QA1018Using AppleScript to send an email with an attachment |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: How can I write an AppleScript to tell the Mail program in Mac OS X to send an email with an attachment?  A: The Mail program in Mac OS X is AppleScript aware. The example script presented in Listing 1 allows the user to choose a text file that will be attached to an outgoing email message.     |  | | --- | | ``` tell application "Mail"     (* MAIL APPLICATION VERSION *)     set mailversion to version as string      (* SPECIFY DISPLAY OR SEND OPERATION - if displayForManualSend     is true, then the message is prepared and displayed in a window     for the user to send it.  if displayForManualSend is false, then     the message is sent right away.*)     set displayForManualSend to true      (* SPECIFY GENERAL CONTENT OF MESSAGE *)     set bodyvar to return & return & "Test body."     set addrVar to "bogus@apple.com"     set addrNameVar to "Guinea Pig"      (* SPECIFY ATTACHMENTS *)     (* This list of files represents another setting of *)     (* the SendMail scriptstep. *)      (* NOTE: A "mailto" URL does not allow for *)     (* the specifying of attachments... *)     set fileAttachThis to choose file of type "TEXT"     set fileList to {fileAttachThis}      (* DEFINE THE SUBJECT LINE *)     set subjectvar to "Test Message From AppleScript with Attachment!"      (* CREATE THE MESSAGE *)     set composeMessage to (a reference to (make new compose message ¬         at beginning of compose messages))     tell composeMessage         make new to recipient at beginning of to recipients ¬             with properties {address:addrVar, display name:addrNameVar}         set the subject to subjectvar         set the content to bodyvar         tell content             repeat with aFile in fileList                 make new text attachment ¬                     with properties {file name:aFile} ¬                     at before the first word of the ¬                     first paragraph             end repeat         end tell     end tell      (* SEND OR DISPLAY THE MESSAGE *)     if displayForManualSend then         set messageEditor to make new message editor ¬             at beginning of message editors          (* the following is a work around for a bug fixed in later         versions of the Mail application that was present in versions         1.0 and 1.1.  *)         if mailversion is "1.0" or mailversion is "1.1" then             set compose message of last message editor to composeMessage         else             set compose message of first message editor to composeMessage         end if     else         send composeMessage     end if end tell ``` | |  | | __Listing 1__. AppleScript for sending an email with an attachment. |       ---  [Jan 04 2002] |

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
