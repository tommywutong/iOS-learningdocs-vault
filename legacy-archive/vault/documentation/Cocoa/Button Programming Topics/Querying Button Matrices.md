---
title: Button Programming Topics
apple_id: 10000019i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Articles/QueryMatrixButtons.html
archived_at: '2026-07-15T07:11:31.387870Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Button Programming Topics](Introduction%20to%20Buttons.md)


[Next](Setting%20the%20Appearance%20of%20a%20Button%E2%80%99s%20Border.md)[Previous](Using%20Radio%20Buttons.md)

# Querying Button Matrices

A group of radio buttons or checkboxes is programmatically an [NSMatrix](https://developer.apple.com/documentation/appkit/nsmatrix) object whose constituent objects are [NSButtonCell](https://developer.apple.com/documentation/appkit/nsbuttoncell) objects. Matrix objects are a special kind of control. Each of its cells can have its own target object and action selector specified. Additionally, an `NSMatrix` may have its own target and action selector. (For more on target-action in relation to matrix objects, see _[Matrix Programming Guide](../Matrix%20Programming%20Guide/Introduction%20to%20Matrices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazde2i)_.)

To find out which radio button or checkbox a user selected—at the moment he or she clicks it—you could specify a target and a different action selector for each cell in the matrix, and then implement the corresponding action method. However, a more efficient way to query the current selection in matrices of radio buttons or checkboxes is to implement target-action for the `NSMatrix` object itself, and in the action method determine which cell (or cells) are now selected. The `NSMatrix` methods for this are [selectedCell](https://developer.apple.com/documentation/appkit/nsmatrix/1436472-selectedcell) and [selectedCells](https://developer.apple.com/documentation/appkit/nsmatrix/1436434-selectedcells).

Listing 1 shows an implementation of an action method that responds to a selection in a matrix of radio buttons.

__Listing 1__  Querying a matrix object for the selected radio-button cell

```objc
- (IBAction)findSelectedButton:(id)sender { // sender is NSMatrix object
    NSButtonCell *selCell = [sender selectedCell];
    NSLog(@"Selected cell is %d", [selCell tag]);
}
```

This code snippet illustrates another technique you can apply when handling selection of cells in matrices. You can assign numeric tags to each cell in a matrix to identify it, and then query for those tag values when handling selections.

[Next](Setting%20the%20Appearance%20of%20a%20Button%E2%80%99s%20Border.md)[Previous](Using%20Radio%20Buttons.md)

