---
title: Matrix Programming Guide
apple_id: 10000022i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Matrix/Tasks/SettingMatrixAppearance.html
archived_at: '2026-07-15T07:16:40.172627Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Matrix Programming Guide](Introduction%20to%20Matrices.md)


[Next](Document%20Revision%20History.md)[Previous](Managing%20the%20Matrix%E2%80%99s%20Cells.md)

# Setting a Matrix’s Appearance

These methods control the sizes of the matrix’s cells:

- To set the height and width of each cell, use `setCellSize:`.
- To set the amount of space that surrounds each cell, use `setIntercellSpacing:`.

These methods control whether the matrix displays its background. If the matrix’s background isn’t displayed, what’s behind it shows through. If the matrix shows its background but the cells don’t, the matrix’s background shows through the cells.

- To set whether the matrix draws its background, use `setDrawsBackground:`.
- To set whether the matrix’s cells draw their backgrounds, use `setDrawsCellBackground:`.

These methods control the color of the matrix and its cells:

- To set the background color of each cell, use `setCellBackgroundColor:`.
- To set the background color of the space between each cell, use `setBackgroundColor:`.

[Next](Document%20Revision%20History.md)[Previous](Managing%20the%20Matrix%E2%80%99s%20Cells.md)

