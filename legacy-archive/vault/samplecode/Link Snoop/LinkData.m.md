---
title: Link Snoop
apple_id: DTS10003593
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/LinkSnoop/Listings/LinkData_m.html
archived_at: '2026-07-18T03:13:32.060718Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Link Snoop](Link%20Snoop.md)


[Next](MyDocument.h.md)[Previous](LinkData.h.md)

# LinkData.m

```objc
// ======================================================================================================================
//  LinkData.m
// ======================================================================================================================


#import "LinkData.h"


@implementation LinkData
// ============================================================================================================= LinkData
// --------------------------------------------------------------------------------------------------- initWithAnnotation

- (id) initWithAnnotation: (PDFAnnotation *) annotation
{
    // Super.
    [super init];

    // Simple pointer (no retain or release).
    _annotation = annotation;

    return self;
}

// -------------------------------------------------------------------------------------------------------------- dealloc

- (void) dealloc
{
    // Instance vars.
    [_text release];

    // Call super.
    [super dealloc];
}

// ----------------------------------------------------------------------------------------------------------- annotation

- (PDFAnnotation *) annotation
{
    return _annotation;
}

// ----------------------------------------------------------------------------------------------------------------- text

- (NSString *) text
{
    // Evaluate lazily and retain.
    if (_text == NULL)
    {
        NSString        *boundedText;

        // Try to get the string enclosed by the annotation bounds - remove linefeeds and the like.
        boundedText = [[[self selection] string] stringByTrimmingCharactersInSet: [NSCharacterSet controlCharacterSet]];

        // If we got back nothing, then we presume there is no text bounded by the link - other wise return the text.
        if (boundedText == NULL)
            _text = [[NSString stringWithString: @"(no text bounded)"] retain];
        else
            _text = [[NSString stringWithString: boundedText] retain];
    }

    return _text;
}

// ------------------------------------------------------------------------------------------------------------ selection

- (PDFSelection *) selection
{
    // Create a PDFSelection using the link bounds (padded out an arbitrary amount so that text is more likely...
    // to fall within the selection/annotation bounds.
    return [[_annotation page] selectionForRect: NSInsetRect([_annotation bounds], -4.0, -4.0)];
}

// ------------------------------------------------------------------------------------------------------------ selection

- (PDFDestination *) destination
{
    PDFPage         *page;
    NSRect          bounds;
    PDFDestination  *dest = NULL;

    // Somehwat complicated ... we want to represent a point (for the destination) that is above the top-left...
    // corner of the annotation bounds.  If all PDF's were non-rotated this would be trivial.  Though unusual, here...
    // we account for rotations of 90, 180 and 270 as well.

    page = [_annotation page];
    bounds = [_annotation bounds];
    switch ([page rotation])
    {
        case 0:
        dest = [[PDFDestination alloc] initWithPage: page atPoint: NSMakePoint(NSMinX(bounds), NSMaxY(bounds) + 8.0)];
        break;

        case 90:
        dest = [[PDFDestination alloc] initWithPage: page atPoint: NSMakePoint(NSMaxX(bounds) + 8.0, NSMaxY(bounds))];
        break;

        case 180:
        dest = [[PDFDestination alloc] initWithPage: page atPoint: NSMakePoint(NSMaxX(bounds), NSMinY(bounds) - 8.0)];
        break;

        case 270:
        dest = [[PDFDestination alloc] initWithPage: page atPoint: NSMakePoint(NSMinX(bounds) - 8.0, NSMinY(bounds))];
        break;
    }

    return dest;
}

@end
```

[Next](MyDocument.h.md)[Previous](LinkData.h.md)

