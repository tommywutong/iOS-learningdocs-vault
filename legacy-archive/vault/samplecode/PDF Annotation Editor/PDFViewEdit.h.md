---
title: PDF Annotation Editor
apple_id: DTS10004035
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/samplecode/PDFAnnotationEditor/Listings/PDFViewEdit_h.html
archived_at: '2026-07-18T03:18:25.092957Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDF Annotation Editor](PDF%20Annotation%20Editor.md)


[Next](MyWindowController.h.md)[Previous](Annotation%20Panel-AnnotationPanel.m.md)

# PDFViewEdit.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This file drive the users interaction with PDFAnnotation Editor at the
         PDFView level. This includes: interacting with the menu bar such as saving the
         current document, printing the document, and adding new annotations to the view;
         interacting with annotations such as selecting, dragging and resizing the current
         annotation; and interacting with the font manager.
*/

// =====================================================================================================================
//  PDFViewEdit.h
// =====================================================================================================================


#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>


@interface PDFViewEdit : PDFView
{
    PDFAnnotation   *_activeAnnotation;
    NSPoint         _mouseDownLoc;
    NSPoint         _clickDelta;
    NSRect          _wasBounds;
    BOOL            _mouseDownInAnnotation;
    BOOL            _dragging;
    BOOL            _resizing;
    BOOL            _editMode;
}

- (void) saveDocument: (id) sender;
- (void) saveDocumentAs: (id) sender;
- (void) transformContextForPage: (PDFPage *) page;
- (void) selectAnnotation: (PDFAnnotation *) annotation;
- (void) annotationChanged;

- (void) setEditMode: (BOOL) edit;

- (void) delete: (id) sender;

- (void) reflectFont;
- (NSRect) resizeThumbForRect: (NSRect) rect rotation: (NSInteger) rotation;

@end
```

[Next](MyWindowController.h.md)[Previous](Annotation%20Panel-AnnotationPanel.m.md)

