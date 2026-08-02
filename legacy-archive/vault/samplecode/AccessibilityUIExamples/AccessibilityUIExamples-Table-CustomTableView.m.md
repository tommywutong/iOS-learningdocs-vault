---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Table_CustomTableView_m.html
archived_at: '2026-07-18T03:00:38.189664Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Table-CustomTableViewController.swift.md)[Previous](AccessibilityUIExamples-Table-CustomTableView.swift.md)

# AccessibilityUIExamples/Table/CustomTableView.m

```objc
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
Category for adoption on NSAccessibilityTable.
*/

#import "AccessibilityUIExamples-Swift.h"

@interface CustomTableView (Accessibility) <NSAccessibilityTable>
@end

@implementation CustomTableView (Accessibility)

- (void)setAccessibilitySelectedRows:(NSArray *)selectedRows {
    if ([selectedRows count] == 1) {
        NSArray *accessibilityRows = self.accessibilityRows;
        NSInteger index = [accessibilityRows indexOfObject:[selectedRows lastObject]];
        self.selectedRow = index;
    }
}

- (NSArray *)accessibilitySelectedRows {
    NSArray *accessiblityRows = [self accessibilityRows];
    return @[accessiblityRows[self.selectedRow]];
}

- (NSArray *)accessibilityRows {
    NSInteger row, col;
    NSAccessibilityElement *rowElement, *cellElement;
    NSArray *rowData;
    NSString *cellText;
    NSMutableArray *accessibilityRows = [[NSMutableArray alloc] initWithCapacity:CustomTableView.TableRowCount];
    for (row = 0; row < CustomTableView.TableRowCount; row++) {
        rowData = self.tableData[row];
        rowElement = [NSAccessibilityElement new];
        rowElement.accessibilityParent = self;
        rowElement.accessibilityRole = NSAccessibilityRowRole;
        rowElement.accessibilitySubrole = NSAccessibilityTableRowSubrole;
        rowElement.accessibilityFrameInParentSpace = [self rectWithRow:row];
        rowElement.accessibilityIndex = row;

        for (col = 0; col < CustomTableView.TableColumnCount; col++) {
            cellText = rowData[col];
            cellElement = [NSAccessibilityElement new];
            cellElement.accessibilityRole = NSAccessibilityStaticTextRole;
            cellElement.accessibilityLabel = cellText;
            cellElement.accessibilityFrameInParentSpace = [self rectForCellInRowCoordsWithRow:row column:col];
            [rowElement accessibilityAddChildElement:cellElement];
        }

        [accessibilityRows addObject:rowElement];
    }
    self.ourAccessibilityRows = accessibilityRows;
    return self.ourAccessibilityRows;
}

@end
```

[Next](AccessibilityUIExamples-Table-CustomTableViewController.swift.md)[Previous](AccessibilityUIExamples-Table-CustomTableView.swift.md)

