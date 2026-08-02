---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Controller_OutlineViewController_mm.html
archived_at: '2026-07-18T03:18:12.854732Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-View-AppDelegate.h.md)[Previous](Sources-Frameworks-Controller-OutlineViewController.h.md)

# Sources/Frameworks/Controller/OutlineViewController.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller object for OpenGL query features' outline.
 */

#import "OutlineViewController.h"

@implementation OutlineViewController
{
@private
    QueryDataSource* mpQuery;
}

#pragma mark -
#pragma mark Public - Initializer

- (instancetype) init
{
    self = [super init];

    if(self)
    {
        mpQuery = [QueryDataSource new];
    } // if

    return self;
} // init

#pragma mark -
#pragma mark Public - Delegates

- (BOOL) allowFirstDisplayToExpand
{
    return YES;
} // allowFirstDisplayToExpand

- (BOOL) outlineView:(NSOutlineView *)outlineView
  shouldCollapseItem:(id)item
{
    return YES;
} // outlineView

- (BOOL) outlineView:(NSOutlineView *)outlineView
    isItemExpandable:(id)item
{
    if([item isKindOfClass:[NSDictionary class]] || [item isKindOfClass:[NSArray class]])
    {
        return YES;
    } // if
    else
    {
        return NO;
    } // else
} // outlineView

- (NSInteger) outlineView:(NSOutlineView *)outlineView
   numberOfChildrenOfItem:(id)item
{
    if(item == nil)
    {
        return mpQuery.data.count;
    } // if

    if([item isKindOfClass:[NSDictionary class]])
    {
        NSDictionary* children = item[@"children"];

        return children.count;
    } // if

    return 0;
} // outlineView

- (id) outlineView:(NSOutlineView *)outlineView
             child:(NSInteger)index
            ofItem:(id)item
{
    if(item == nil)
    {
        return mpQuery.data[index];
    } // if

    if([item isKindOfClass:[NSDictionary class]])
    {
        NSArray* children = item[@"children"];

        return children[index];
    } // if

    return nil;
} // outlineView

- (id)          outlineView:(NSOutlineView *)outlineView
  objectValueForTableColumn:(NSTableColumn *)theColumn
                     byItem:(id)item
{

    if([[theColumn identifier] isEqualToString:@"children"])
    {
        if([item isKindOfClass:[NSDictionary class]])
        {
            return [NSString stringWithFormat:@"%ld items",[item[@"children"] count]];
        } // if

        return item;
    } // if
    else
    {
        if([item isKindOfClass:[NSDictionary class]])
        {
            return item[@"parent"];
        } // if
    } // else

    return nil;
} // outlineView

- (BOOL) outlineView:(NSOutlineView *)outlineView
    shouldExpandItem:(id)item
{
    BOOL bFound = NO;

    if([item isKindOfClass:[NSDictionary class]])
    {
        NSAttributedString *pAttrStr = item[@"parent"];

        if(pAttrStr)
        {
            bFound = [mpQuery isParent:pAttrStr.string];
        } // if
    } // if

    return bFound;
} // outlineView

#pragma mark -
#pragma mark Public - Destructor

- (void) dealloc
{
    if(mpQuery)
    {
        [mpQuery release];

        mpQuery = nil;
    } // if

    [super dealloc];
} // dealloc

@end
```

[Next](Sources-Frameworks-View-AppDelegate.h.md)[Previous](Sources-Frameworks-Controller-OutlineViewController.h.md)

