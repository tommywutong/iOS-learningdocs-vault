---
title: Supporting QuickDraw GX with EPS
apple_id: DTS10001210
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-10-27'
source_url: https://developer.apple.com/library/archive/qa/gx/gx05.html
archived_at: '2026-07-18T02:29:30.949580Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GX05Supporting QuickDraw GX with EPS |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: What is the correct way to support EPS files using QuickDraw GX? Converting the QuickDraw preview into a GX shape and attaching a tag containing the PostScript code looks OK, but results in a vertically flipped PostScript image when printed. This is presumably because of the difference in orientation between GX and PostScript. Is it necessary to modify the PostScript code to solve this problem?  A: It's true that when using PostScript synonyms, you need to account for the QD coordinate space. QD defines 0,0 as the top-left corner of the page, while PostScript defines 0,0 as the bottom-left coordinate. There is a small note on page 4-13 of the 'Quickdraw GX Printing' manual that mentions this.  There are many ways to handle this. One method is to use translate and scale to switch the coordinate system back. If, for example, the page is 760 pixels tall, you could use:   |  | | --- | | ```     0 760 translate     1 -1 scale     newpath ``` |   to translate 0,0 back to the bottom left corner of the page. The rest of your PostScript code can then be sent as-is. Be sure to undo the effects of the translate and scale operations before attempting to draw any GX objects, or they will be upside-down as well.  Q: The method you suggested is a fine way of supporting EPS in QuickDraw GX for many applications, assuming that they do not allow users to export the EPS. However, we need to support EPS as a position-independent shape (as part of a flattened picture shape). Since the method below relies on knowledge of the page height, it does not work for exchanging data between applications (for example, 'qdgx' clipboard and file formats).  I tried to enclose the EPS preview shape within a picture shape. The EPS synonym tag was attached to the picture shape, and a vertical reflection mapping was applied both to the preview shape and the picture shape itself. The idea was that the PostScript would be reflected once vertically (and thus print correctly) while the enclosed preview shape would be reflected twice vertically (and thus display correctly). Unfortunately, the PostScript did not print in the correct place, while the preview shape displayed correctly, but glacially. I'd appreciate any suggestions as to how to handle this in a position-independent manner.  A: We've provided a function called EPStoShape that is an example of how to encapsulate your EPS into a GX shape. This sample is very simple, and it needs to be extended for use in a real application.  There are two cases that the sample code cannot handle:   1. With large EPS files, the EPStoShape routine reads the entire EPS file into a single handle, which is added to the shape as a 'post' collection. This works fine for small sample files, but to support larger EPS files, you should modify this routine to read the file in sections, adding multiple, smaller collections to the shape. This reduces the memory requirements at print time. 2. The EPStoShape function looks for the %%BoundingBox comment in the EPS file to determine the size of the document/shape. This comment is usually found just before the actual document data, and it is followed by 4 integers representing the top,left,bottom,right of the bounding box. However, to make writing EPS files easier, the format of this comment was extended. Now, do the following:  |  | | --- | | ```    %% BoundingBox: (atend)     <Actual Document Data>     %% BoundingBox: 0 0 10 10 ``` |   In this case, the '(atend)' tells the reader that the actual bounding box can be found at-end of document data. The EPStoShape function assumes that the first BoundingBox comment has the four coordinates and generates bogus PostScript code if the (atend) keyword is found instead. To use this routine in your application, you should modify it to check for the (atend) construct and to look for the second BoundingBox comment, if it is found.  Both of these modifications should be easy to implement. Routine: EPSFileToShape Reads in an EPS file and makes a shape out of it. If there was a PICT resource in it, it translates it to Skia, if there is no PICT resource, it will make a rectangle shape the width and height of the bounding box from the EPS BoundingBox:: comment with first point at 0,0.  In either case, the EPS file will be attached to the shape with 'post' tag synonyms.  Additional PostScript will be attached to make it so the PostScript renders through the shape's transform (obviously, no perspective allowed here) properly when printing through the Skia-PostScript Imaging System.  The algorithm for this comes from the _PostScript Language Reference Manual, 2nd edition_. Page 724.   3. left bottom translate %% where left,bottom is left, bottom of QD shape's bounds. 4. 1 -1 scale %% Put us back in PostScript space, we were in Skia. 5. -x1 -y1 translate %% Put the origin at the EPS bounding box's lower left.   Routine does not check for the validity of the EPS data or version. It assumes the PostScript is valid EPS with bounding box comment. /\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/  |  | | --- | | ``` gxShape EPSFileToShape(Str255 fName, short vRefNum)     {         OSErr               status;         PicHandle       thePict;         Rect                theRect;         Point               patStretch = {1,1};         gxShape             theShape = nil;         short               refNum;         gxTag                   synTag;         long                size;         Handle          hPsData;         long                startComment, endComment;         Str32               num1;         char                tagString[300];         long                tagSize, pieceSize;          gxTranslationStatistic              seanStats;          /** Now get the PostScript data **/          status = FSOpen(fName, vRefNum, &refNum);         ncheck(status);          GetEOF(refNum, &size);         hPsData = NewHandle(size);         HLock(hPsData);           /** Read in the whole EPS file **/         status = FSRead(refNum, &size, *hPsData);         ncheck(status);         FSClose(refNum);          /** Find the bounding box comment (Numbers only) **/         startComment = Munger(hPsData, 0, "%%BoundingBox:", 14, nil, 0) + 14;         endComment = Munger(hPsData , startComment, "\n", 1, nil, 0);         refNum = OpenRFPerm(fName, vRefNum, 0);          thePict = (PicHandle)GetResource('PICT', 256);         if (thePict != nil) {              theRect = (*thePict)->picFrame;              theShape = GXNewShape(gxPictureType);              (void) GXConvertPICTToShape(thePict, gxDefaultOptionsTranslation,              &theRect, &theRect, patStretch,              theShape, &seanStats);              status = GXGetGraphicsError(nil);              ncheck(status);              ReleaseResource((Handle)thePict);          } else {              float            x1, y1, x2, y2;             gxRectangle  theRectangle;              sscanf(*hPsData + startComment, "%f %f %f %f", &x1, &y1,             &x2, &y2);             theRectangle.top = 0;             theRectangle.left = 0;             theRectangle.right = X2Fix(x2 - x1);             theRectangle.bottom = X2Fix(y2 - y1);              /** We need the QuickDraw rectangle for the             embedded PostScript origin translage **/              theRect.top = 0;             theRect.left = 0;             theRect.bottom= theRectangle.bottom >> 16;             theRect.right = theRectangle.right >> 16;              theShape = GXNewRectangle(&theRectangle);          }//end if          CloseResFile(refNum);          /** translate to Left Bottom of QuickDraw rectangle **/          tagSize = 0;         NumToString(theRect.left, num1);         num1[(unsigned char)num1[0] + 1] = ' ';         pieceSize = (unsigned char)num1[0] + 1;         BlockMove(&(num1[1]), tagString, pieceSize);         tagSize += pieceSize;          NumToString(theRect.bottom, num1);         pieceSize = (unsigned char)num1[0];         BlockMove(&(num1[1]), tagString + tagSize, pieceSize);         tagSize += pieceSize;         BlockMove(" translate\n", tagString + tagSize, 11);         tagSize += 11;          /** flip y axis **/         BlockMove(" 1 -1 scale\n", tagString + tagSize, 12);         tagSize += 12;         synTag = GXNewTag( gxPostScriptTag, tagSize, tagString);         GXSetShapeTags(theShape, gxPostScriptTag, 0, 0, 1, &synTag);         GXDisposeTag(synTag);         /** Translate to -(LLx) -(LLy) **/          // 4 bbox numbers from operand comment string on operand stack         synTag = GXNewTag( gxPostScriptTag, endComment - startComment + 1,         *hPsData + startComment);         GXSetShapeTags(theShape, gxPostScriptTag, 0, 0, 1, &synTag);         GXDisposeTag(synTag);          // Pop the second two, translate to negative of first two.         synTag  = GXNewTag( gxPostScriptTag, 36,         "pop pop neg exch neg exch translate\n");         GXSetShapeTags(theShape, gxPostScriptTag, 0, 0, 1,         &synTag);         GXDisposeTag(synTag);          /** The PostScript Synonym itself **/          synTag = GXNewTag( gxPostScriptTag, size, *hPsData);         GXSetShapeTags(theShape, gxPostScriptTag, 0, 0, 1, &synTag);         GXDisposeTag(synTag);          DisposHandle(hPsData);          check(theShape);         return(theShape);      }//EPSFileToShape ``` | |

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
