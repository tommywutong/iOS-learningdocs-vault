---
title: Kanji & PostScript Printing
apple_id: DTS10001766
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-02-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd07.html
archived_at: '2026-07-18T02:38:35.520249Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD07Kanji & PostScript Printing |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: We are close to releasing the Kanji Macintosh version of our application, but we are experiencing some unexpected behavior when attempting to print Single Byte Characters (SBC) using a Double Byte Font (DB) on a PostScript printer.  We are trying to print vertically rotated text, which looks more or less like the following example (on the display), except that each letter is rotated 90 degrees (lying on its side):  - -  | T |  | E |  | X |  | T |  - - -  We are doing this by using the following pseudo code:   |  | | --- | | ``` 1. 	tTxtPicRec = [tJus=1; tFlip=0; tAngle=90; tAngleFixed=Integer2Fixed( 90 )] 2.	tCenterRec = [Integer2Fixed( ofX(offset), of Y(offset) ) ] 3.	PictComment( TextBegin, sizeof(TTxtPicRec), (Handle) tTxtPicRecH ); 4.	PictComment( TextCenter, sizeof(TCenterRec), (Handle) tCenterRecH ); 5.	DrawJustified (buffer, count, 0, smOnlyStyleRun, 1, 1 ); 6.	PictComment( TextEnd, NIL, NIL ); ``` |   When printing rotated single or double- byte characters to a postscript printer using a double- byte font, such as Osaka, we get the results that look something like this (except that each letter is also lying on its side):  - - - - - - - - - - - - - - - - - - - -  ||  | TEXT |  ||  - - - - - - - - - - - - - - - - - - - - -  In all cases, the rotated text displays properly on screen. The problem occurs while printing SB or DBC using a DB font. Printing rotated SBC using an SB font works properly. It appears that each character is rotated around its own center, rather than around the center given by the offset (for the box containing just the text).  Is this the proper approach?  A: The approach in your pseudo code looks correct, but there are other things you need to know about.  Two-byte characters don't print correctly when using the `TextBegin`, `TextCenter`, and `TextEnd PicComments`, due to the structure of the data that is in the comments. The LaserWriter driver uses the `PicComments` to rotate text, and it is not expecting the data in two-byte format. In some instances, the two-byte format looks like bitmap data to the driver, so this data is ignored, and nothing is printed. The driver is expecting the comments to contain only "normal" text.  There are some techniques you can use to avoid this limitation in the driver. These approaches reflect the methods that many developers are using to resolve this problem:  Rotating with `RotateBegin` and `RotateEnd PicComments`  Since the data is in bitmap format, you can use the `RotateBegin` and `RotateEnd PicComments` to perform the rotation, as shown below:   |  | | --- | | ``` RotateBegin       DrawString (...);  << To rotate your 2 byte Japanese characters RotateEnd ``` |   Bear in mind that you only need to use this approach when you are printing two-byte Japanese bitmap fonts. Therefore, you have to check the type of data that is to be printed, and send the appropriate `PicComments`.  Use the following `PicComments` to hide the QuickDraw representation of the rotated text:   |  | | --- | | ``` PostScriptBegin 	CopyBits (...);   << For the QuickDraw printers PostScriptEnd ``` |   The `PostScriptBegin` and `PostScriptEnd PicComments` are used to hide the `CopyBits` calls from the LaserWriter driver in a device-independent manner. These calls tell the LaserWriter driver to turn off all QuickDraw calls. The driver does not interpret any QuickDraw calls until it finds the `PostScriptEnd PicComment`. Since QuickDraw printer drivers do _not_ understand the `PostScriptBegin` and `PostScriptEnd PicComments`, they ignore the `PicComments`, and the `CopyBits` call performs the text rotation.  The technique described above has one problem -- if you record the previous `PicComments` in a picture and print it, everything prints exactly as expected, but if you display the picture in an on-screen window, you see the _unrotated_ version of the text. This is a known bug which, unfortunately, won't be fixed in the very near future.  For more information on using picture comments, see _Inside Macintosh: Imaging with QuickDraw,_ and the Macintosh Technote: [QD 10 - Picture Comments The Real Deal.](https://developer.apple.com/library/archive/technotes/qd/qd_10.html)  Rotating Characters Individually  When you rotate a string of Japanese characters 90 degrees, the orientation of the _characters_ stays the same. In other words, the entire _string_ rotates, but the characters _within_ the string retain the orientation they had before rotation. Therefore, each character in the string must be rotated back 90 degrees for it to be typographically correct.  Most developers need to do their own line layout for rotated DBC. That is, move to a position, draw a character, move to the next position, draw the next character, and so on until the string is complete. |

#### [May 01 1995]

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
