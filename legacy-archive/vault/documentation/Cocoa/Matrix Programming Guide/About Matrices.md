---
title: Matrix Programming Guide
apple_id: 10000022i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Matrix/Concepts/AboutMatrices.html
archived_at: '2026-07-15T07:16:38.165953Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Matrix Programming Guide](Introduction%20to%20Matrices.md)


[Next](Matrix%20Selection%20Modes.md)[Previous](Introduction%20to%20Matrices.md)

# About Matrices

[NSMatrix](https://developer.apple.com/documentation/appkit/nsmatrix) is a class used for creating groups of [NSCell](https://developer.apple.com/documentation/appkit/nscell) objects (or simply, cells or cell objects) that work together in various ways. It includes methods for arranging cells in rows and columns, either with or without space between them. Cell objects in an NSMatrix are numbered by row and column, each starting with 0; for example, the top left cell would be at (0, 0), and the cell that’s second down and third across would be at (1, 2).

The cell objects that an `NSMatrix` contains are usually of a single subclass of `NSCell`, but they can be of multiple subclasses of `NSCell`. The only restriction is that all cell objects must be the same size. An `NSMatrix` object can be set up to create new cell objects by copying a prototype object, or by allocating and initializing instances of a specific `NSCell` class. Cells created by or added to an `NSMatrix` are retained by the matrix.

An `NSMatrix` object (or, simply, matrix) adds to the target-action paradigm implemented by cell objects (specifically, cells that inherit from [NSActionCell](https://developer.apple.com/documentation/appkit/nsactioncell)) by maintaining its own target and action in addition to the targets and actions of its cell objects. A matrix's target and action are used if one of its cells doesn't have a target or action set. This design allows for common usage patterns, including the following:

- If none of the cells of the `NSMatrix` object has either target or action set, the target and action of the `NSMatrix` object is always used.
- If only the actions of each of the cells is set, they share the target specified by their `NSMatrix` object, but send different messages to it.
- If only the targets of each of the cells is set, they all send the action message specified by the `NSMatrix` object, but to different targets.

When the user double-clicks an `NSMatrix` object, it can dispatch a separate action message (the selector for which is set via [setDoubleAction:](https://developer.apple.com/documentation/appkit/nsmatrix/1436469-doubleaction)); this double-click action message is in addition to any cell's single-click action message. The double-click action of an `NSMatrix` object is always sent to its target.

[Next](Matrix%20Selection%20Modes.md)[Previous](Introduction%20to%20Matrices.md)

