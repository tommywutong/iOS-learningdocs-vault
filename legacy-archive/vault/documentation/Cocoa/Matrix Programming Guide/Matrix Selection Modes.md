---
title: Matrix Programming Guide
apple_id: 10000022i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Matrix/Concepts/MatrixSelectionModes.html
archived_at: '2026-07-15T07:16:38.671192Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Matrix Programming Guide](Introduction%20to%20Matrices.md)


[Next](Managing%20the%20Matrix%E2%80%99s%20Cells.md)[Previous](About%20Matrices.md)

# Matrix Selection Modes

Since users frequently press the mouse button while the cursor is within the NSMatrix and then drag the mouse around, NSMatrix offers several methods that determine how it tracks the mouse. `setMode:` lets you choose among four “selection modes” that broadly determine how the matrix tracks the mouse. The `setAllowsEmptySelection:` and `setSelectionByRect:` methods let you refine how those modes work.

The `setMode:` method lets you choose one of these four modes:

- `NSTrackModeMatrix` is the most basic mode of operation. In this mode the NSCells are asked to track the mouse with `trackMouse` whenever the mouse is inside their bounds. No highlighting is performed. An example of this mode might be a “graphic equalizer” NSMatrix of sliders, where moving the mouse around causes the sliders to move under the mouse.
- `NSHighlightModeMatrix` is a modification of `NSTrackModeMatrix`. In this mode, an NSCell is highlighted before it’s asked to track the mouse, then unhighlighted when it’s done tracking. This is useful for multiple unconnected NSCells that use highlighting to inform the user that they are being tracked (like push-buttons and switches).
- `NSRadioModeMatrix` is used when you want no more than one NSCell to be selected at a time. It can be used to create a set of buttons of which one and only one is selected. (There’s also the option of allowing no button to be selected.) Any time an NSCell is selected, the previously selected NSCell is unselected. This is most commonly used with groups of radio buttons. You might also use it with a group of push buttons that you want to behave like radio buttons.
- `NSListModeMatrix` is the opposite of `NSTrackModeMatrix`. NSCells are highlighted, but don’t track the mouse. This mode can be used to select a range of text values, for example. NSMatrix supports the standard multiple-selection paradigms of dragging to select, using the Shift key to make continuous selections, and using the Command key to make discontinuous selections. Browsers (as used, for instance, by NSOpenPanel objects) use this mode.

`setAllowsEmptySelection:` has an effect only if the selection mode is `NSRadioModeMatrix`. It lets you choose whether, in a group of radio buttons, it’s allowed for none of them to be on. For example, say the user clicks on the one radio button in a matrix that’s on. If `allowsEmptySelection` is `YES`, that button turns off and none of the radio buttons is on. If `allowsEmptySelection` is `NO`, the button remains on, and the only way to turn it off is to click another button.

`setSelectionByRect:` sets whether the user can select a range of cells by dragging the mouse. If `isSelectionByRect` is `NO`, dragging over a range selects only the last cell only. If `isSelectionByRect` is `YES`, dragging over a range selects all the cells the user drags over.

[Next](Managing%20the%20Matrix%E2%80%99s%20Cells.md)[Previous](About%20Matrices.md)

