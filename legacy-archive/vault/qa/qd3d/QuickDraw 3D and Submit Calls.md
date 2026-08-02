---
title: QuickDraw 3D and Submit Calls
apple_id: DTS10001813
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d15.html
archived_at: '2026-07-18T02:38:39.994516Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD3D15QuickDraw 3D and Submit Calls |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  Q: The code for drawing and writing files is very similar to the submit call. Why is it necessary to have the `Startxxx` and `Endxxx` calls? They require two procedure codes -- one for drawing and one for writing.  A: The submit calls for drawing and picking are in the following routine:   |  | | --- | | ``` //------------------------------------------------------------------ // Submit the scene for rendering/fileIO and picking TQ3Status SubmitScene( DocumentPtr theDocument )  {		 	TQ3Vector3D				globalScale; 	TQ3Vector3D				globalTranslate; 	 	globalScale.x = globalScale.y = globalScale.z = theDocument->fGroupScale; 	globalTranslate = *(TQ3Vector3D *)&theDocument->fGroupCenter; 	Q3Vector3D_Scale(&globalTranslate, -1, &globalTranslate); 	Q3Style_Submit(theDocument->fInterpolation, theDocument->fView); 	Q3Style_Submit(theDocument->fBackFacing , theDocument->fView); 	Q3Style_Submit(theDocument->fFillStyle, theDocument->fView); 		 	Q3MatrixTransform_Submit( &theDocument->fRotation, theDocument->fView); 		 	Q3ScaleTransform_Submit(&globalScale, theDocument->fView); 	Q3TranslateTransform_Submit(&globalTranslate, theDocument->fView); 	Q3DisplayGroup_Submit( theDocument->fModel, theDocument->fView); 	 	return kQ3Success ; } ``` |   You can use the same routine for drawing and picking. For picking, or in this instance, for calculating the bounding box of the geometry being displayed as the main group, do the following:   |  | | --- | | ``` 	TQ3Status		status; 	TQ3ViewStatus	viewStatus ; 	 	status = Q3View_StartBoundingBox( theDocument->fView,                                             kQ3ComputeBoundsApproximate ); 	do { 		status = SubmitScene( theDocument ) ; 	} while((viewStatus = Q3View_EndBoundingBox( theDocument->fView,  	&viewBBox ))                                           == kQ3ViewStatusRetraverse ); ``` |   For drawing, do the following:   |  | | --- | | ``` 	TQ3Status theStatus ;	 	 	Q3View_StartRendering(theDocument->fView) ; 	do { 		theStatus = SubmitScene( theDocument ) ; 	} while (Q3View_EndRendering(theDocument->fView)  	== kQ3ViewStatusRetraverse ); ``` |   The code to write to a file is complicated slightly by the need to write the viewhints to the file. However, it is a simple matter to perform this operation with the following code:   |  | | --- | | ``` 	TQ3SharedObject		viewHints; 	TQ3ViewStatus		fileStatus; 	 	if (Q3File_OpenWrite(file, kQ3FileModeNormal | kQ3FileModeText) == kQ3Success ) 	{ 	 		Q3View_StartWriting(theView, file); 		if (theView == NULL) 			viewHints = NULL; 		else 			viewHints = Q3ViewHints_New(theView); 			 		if (viewHints != NULL) 		{ 			if (Q3Object_Submit(viewHints, theView) == kQ3Failure) 			{ 				Q3File_Cancel(file); 				return; 			} 		} 			 		do { 				theStatus = SubmitScene( theDocument ) ; 		} while ((fileStatus = Q3View_EndWriting(theView)) ==                                         kQ3ViewStatusRetraverse); 			 		if( Q3File_Close(file) == kQ3Failure ) { 			return; 		} 	} ``` |   In some instances, you should avoid nesting groups repetitively. For example, if you create a new display group and add an existing group to it. This implies that when you write the new group to the file, the existing group remains nested inside. However, the file you write is not the same as the file you read in, in that an extra level of nesting has been introduced. To avoid this, use the following code to write objects to a file (this code avoids the nesting problem):   |  | | --- | | ``` void WriteGroupToFile( TQ3FileObject file, TQ3GroupObject theData,  TQ3ViewObject theView) { 	TQ3GroupPosition	gPos; 	TQ3Object			object; 	TQ3SharedObject		viewHints; 	TQ3ViewStatus		fileStatus; 	 	if (Q3File_OpenWrite(file, kQ3FileModeNormal | kQ3FileModeText) == kQ3Success ) 	{ 	 		Q3View_StartWriting(theView, file); 		if (theView == NULL) 			viewHints = NULL; 		else 			viewHints = Q3ViewHints_New(theView); 			 		if (viewHints != NULL) 		{ 			if (Q3Object_Submit(viewHints, theView) == kQ3Failure) 			{ 				Q3File_Cancel(file); 				return; 			} 		} 			 		do { 			if (theData != NULL) 			{ 				TQ3Status status; 				 				status = Q3Group_GetFirstPosition(theData, &gPos); 				 				while (gPos != NULL && status == kQ3Success) 				{ 					 					Q3Group_GetPositionObject(theData, gPos, &object); 					status = Q3Object_Submit(object, theView); 					Q3Object_Dispose(object); 					 					if (status != kQ3Failure) 					{ 						Q3Group_GetNextPosition(theData, &gPos); 					} 				} 			} 	 		} while ((fileStatus = Q3View_EndWriting(theView)) ==                                               kQ3ViewStatusRetraverse); 			 		if( Q3File_Close(file) == kQ3Failure ) { 			return; 		} 	} 	return ; } ``` |   It's probably best to use a submit function to perform picking and drawing, but you should use different code to write to a file to avoid the possibility of groups becoming more deeply nested each time the file is saved. |

#### [Jun 01 1995]

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
