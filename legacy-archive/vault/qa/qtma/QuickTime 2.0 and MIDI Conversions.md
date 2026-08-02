---
title: QuickTime 2.0 and MIDI Conversions
apple_id: DTS10001941
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtma/qtma04.html
archived_at: '2026-07-18T02:38:46.382141Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Audio](https://developer.apple.com/referencelibrary/QuickTime/idxMusicAudio-date.html)

|  |
| --- |
| Technical Q&A QTMA04QuickTime 2.0 and MIDI Conversions |

|  |
| --- |
| Q Is there a bug in QuickTime's conversion utilities? I am using QuickTime 2.0, the QuickTime PowerPlug, and Apple Multimedia Tuner 2.0 with System 7.5, PowerTalk. I observe the problem when I use StandardGetFilePreview to allow the user to select a QT Movie (the problem manifests itself in any application that can open movies). This is what happens. When I select a MIDI file and then select Convert... and Save _without first going into the options dialog_, the MIDI file is imported as a Text Movie. More often than not, I don't even get this far, as my app crashes with a Type-25 system error in TESetText. However, if I select Options from the SFPutFile dialog before selecting Convert and Save (whether I make any changes in the Options dialog or not), the Midi file converts correctly.  I have also seen PICS files do the same thing, unless you go into Options before converting and saving, the PICS files either import incorrectly or the app crashes. Until recently, I never had this problem. Can you tell me what's wrong? A If the file name has a dot in it (such as MIDIMU.VIS), MoviePlayer assumes that it is a text file, so it tries to use the text importer. You may see the same problem with PICT files that have a .PIC (or similar) postfix. Until there is a new version of QuickTime available that removes this bug, the only workaround is to write a filter for the StandardFile dialog that removes the extension from the filename on-the-fly. [May 01 1995] |

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
