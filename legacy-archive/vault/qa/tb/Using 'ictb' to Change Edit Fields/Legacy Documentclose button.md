---
title: Using 'ictb' to Change Edit Fields
apple_id: DTS10002210
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-10-25'
source_url: https://developer.apple.com/library/archive/qa/tb/tb24.html
archived_at: '2026-07-18T02:38:56.515366Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB24Using 'ictb' to Change Edit Fields |

|  |
| --- |
| Q I have created a dialog box that has two edit text fields in it and have used an 'ictb' resource to change the font and the size of the fields to 10 point Geneva. When I move the insertion point into the second field and delete a character, the character just before the one I deleted drops down a couple of pixels and overwrites itself. What can be done about this?   A You have run into a problem with the Dialog Manager's support of 'ictb'. The Dialog Manager forgets to reset some of the fields of the TextEdit record when it swaps the font and font size information stored in the 'ictb'. You need to reset the fontAscent and lineHeight fields of the TextEdit Record to match the size of the font specified in the 'ictb'. By default those fields are set to the lineHeight and fontAssent of 12 point Chicago. Below is code that shows how to set up the TextEdit record.   ``` //------------------------------------------------------------------ static void SetUpEditField (DialogRef dlog,short fontNum,short fontSize) //------------------------------------------------------------------ {   FontInfo  info;   DialogPeek  dpeek = (DialogPeek)dlog;    if (dpeek != nil) {     TEHandle te = dpeek->textH;       //get the TEHandle      if (te != nil) {       short oldFont = dlog->txFont;   //save old info       short oldSize = dlog->txSize;        TextFont(fontNum);              //set the port to correct font info       TextSize(fontSize);        GetFontInfo(&info);        // ok lets fix the TE record since the dialog manager left it at 12 point        te[0]->txFont   = fontNum;        // set font       te[0]->txSize     = fontSize;       te[0]->lineHeight = info.ascent + info.descent + info.leading; //calculate the correct info       te[0]->fontAscent = info.ascent ;       TextFont(oldFont);  //reset the font info       TextSize(oldSize);     }   } }  //------------------------------------------------------------------ static  short DoDialog(short resID) //------------------------------------------------------------------ {   DialogRef   dlog;   GrafPtr   oldPort;   short   itemHit = 0;    GetPort(&oldPort);   dlog = GetNewDialog(resID,nil,(WindowRef)-1);   if (dlog) {     SetPort(dlog);     SelectDialogItemText(dlog,2,0x8000,0x8000); //set the cursor     SetUpEditField(dlog,geneva,10);             // set the edit field     (void)SetDialogDefaultItem(dlog,1);         // hilight the ok button     ShowWindow(dlog);                           // show the dialog     while (itemHit != ok) {       ModalDialog(nil,&itemHit);     }     SetPort(oldPort);     DisposeDialog(dlog);   }   return itemHit; } ```  [Oct 25 1996] |

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
