---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Outline_CustomOutlineView_m.html
archived_at: '2026-07-18T03:00:36.810780Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Outline-CustomOutlineView.swift.md)[Previous](AccessibilityUIExamples-SearchField-CustomSearchField.swift.md)

# AccessibilityUIExamples/Outline/CustomOutlineView.m

```objc
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
Category for adoption on NSAccessibilityOutline.
*/

#import "AccessibilityUIExamples-Swift.h"

@interface CustomOutlineView (Accessibility) <NSAccessibilityOutline>
@end

@implementation CustomOutlineView (Accessibility)

- (NSArray *)accessibilityRows
{
    NSMutableArray *accessibilityRows = [[NSMutableArray alloc] init];
    NSArray *visibleNodes = [self visibleNodes];

    for (OutlineViewNode *node in visibleNodes) {
        NSAccessibilityElement *element = [self accessibilityElementForNodeWithNode:node];
        [accessibilityRows addObject:element];
    }

    return accessibilityRows;
}

- (NSArray *)accessibilitySelectedRows {
    NSArray *accessibilityRows = [self accessibilityRows];
    return @[accessibilityRows[self.selectedRow]];
}

- (void)setAccessibilitySelectedRows:(NSArray *)selectedRows {
    if (selectedRows.count == 1) {
        NSArray *accessibilityRows = [self accessibilityRows];
        NSInteger selectedRow = [accessibilityRows indexOfObject:selectedRows.firstObject];
        if (selectedRow != NSNotFound) {
            self.selectedRow = selectedRow;
        }
    }
}

@end
```

[Next](AccessibilityUIExamples-Outline-CustomOutlineView.swift.md)[Previous](AccessibilityUIExamples-SearchField-CustomSearchField.swift.md)

