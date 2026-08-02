---
title: Normal Line of Object Pick
apple_id: DTS10001812
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d14.html
archived_at: '2026-07-18T02:38:39.914118Z'
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
| Technical Q&A QD3D14Normal Line of Object Pick |

|  |  |  |
| --- | --- | --- |
|  Q: How can I display a line representing the normal of a pick on an object? With no transformations applied to the entire model, this works properly, but if any intermediate transformations are applied, it doesn't.  A: Try inserting the "normal" line into the document group after the object for which the normal is the pick point (you'll have to work out what the normal is in geometry coordinates). All of the transforms should be applied correctly, and the object should be drawn in the right place.   |  | | --- | | ``` +-------------+ | translate 1 | +-------------+ | rotation 1  | +-------------+ | geometry 1  | +-------------+ | *NORMAL*    | <------- Insert normal line here for pick on geometry 1. +-------------+ | translate 2 | +-------------+ | rotation 2  | +-------------+ | geometry 2  | +-------------+ ``` |   If you are only trying to show picking, you can highlight just the picked face. This is considerably easier, and once you have the picking code implemented, it only requires setting the highlight attribute on for the face attribute. The following routine shows how to select an object (you'll have to refine this to select a face):   |  | | --- | | ``` static void RenderPickAndCheckForHits( 	void) { 	register unsigned 	long i; 	register char		*a, *b; 	unsigned long		count; 	unsigned long		numPicked; 	unsigned long		numPicked2; 	TQ3HitData			hitData; 	TQ3HitData			hitData2; 	TQ3Vector3D			scaleVec; 	TQ3Status			whatHappened; 	TQ3Vector3D			translate; 	TQ3Vector3D		tmp; 	 	Q3Vector3D_Set(&scaleVec, gZoom, gZoom, gZoom); 	Q3Vector3D_Scale(&scaleVec, gGlobalScale, &scaleVec); 	 	Q3Vector3D_Set(&tmp, gXTranslate, gYTranslate, gZTranslate); 	translate = gGlobalTranslate; 	Q3Vector3D_Add(&translate, &tmp, &translate); 	Q3View_StartPicking(gTransformationsView); 	Q3ScaleTransform_Submit(&scaleVec, gTransformationsView); 	Q3TranslateTransform_Submit(&translate, gTransformationsView); 	Q3Style_Submit(gSubdivControl, gTransformationsView); 	Q3PickIDStyle_Submit(32, gTransformationsView); 	whatHappened = ErDisplayGroup_Pick(gGroup,  pickObject, gTransformationsView); 	Q3View_EndPicking(gTransformationsView); 	 	if (!Q3Pick_GetNumHits(pickObject, &numPicked) || (numPicked == 0)) { 		Q3Object_Dispose(pickObject); 		return; 	} 	 #if 0 	count = 0; 	for (	whatHappened = ErPick_GetFirstHit(pickObject, &hitData); 			whatHappened == kQ3Success; 			whatHappened = ErPick_GetNextHit(pickObject, &hitData)) { 		if (whatHappened != kQ3Success) 			break; 		SysBeep(10); 		Q3Hit_EmptyData(&hitData); 		count++; 	} 	if (count != numPicked) 		DebugStr("\pSOMETHING SUCKS IN PICKING"); 		 #else 	/* 		This code highlights the objects that were picked. 		However, the code can't be enabled until geometries 		stop returning the decomp as the object picked, which produces 		a crash. 	*/ 	count = 0; 	for (	whatHappened = ErPick_GetFirstHit(pickObject, &hitData); 			whatHappened == kQ3Success; 			whatHappened = ErPick_GetNextHit(pickObject, &hitData)) { 		if (whatHappened != kQ3Success) 			break; 		SysBeep(10); 		count++; 		 		if( Q3Object_IsType(hitData.object, kQ3ShapeTypeGeometry)) { 			TQ3Switch		highlightSwitch = kQ3On; 			TQ3AttributeSet 	attribSet; 			Q3Geometry_GetAttributeSet(hitData.object, &attribSet); 			 			if( !attribSet ) { 				attribSet = Q3AttributeSet_New(); 				Q3Geometry_SetAttributeSet(hitData.object, attribSet); 				Q3Object_Dispose(attribSet); 			} 			 			Q3AttributeSet_Add(attribSet,  							   kQ3AttributeTypeHighlightState, 							   &highlightSwitch); 		} 		Q3Hit_EmptyData(&hitData); 	} 	if (count != numPicked) 		DebugStr("\pSOMETHING SUCKS IN PICKING"); 	 	UpdateScreen(); 	for (	whatHappened = ErPick_GetFirstHit(pickObject, &hitData); 			whatHappened == kQ3Success; 			whatHappened = ErPick_GetNextHit(pickObject, &hitData)) { 		if (whatHappened != kQ3Success) 			break; 		 		if( Q3Object_IsType(hitData.object, kQ3ShapeTypeGeometry)) { 			TQ3Switch		highlightSwitch = kQ3Off; 			TQ3AttributeSet 	attribSet; 			Q3Geometry_GetAttributeSet(hitData.object, &attribSet); 			 			if( attribSet ) 				Q3AttributeSet_Add(attribSet, kQ3AttributeTypeHighlightState, 					&highlightSwitch); 		} 		Q3Hit_EmptyData(&hitData); 	}	 #endif 	 	Q3Object_Dispose(pickObject); } #endif ``` | |

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
