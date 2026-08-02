---
title: Printing Programming Guide for Mac
apple_id: 10000083i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-12-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_pagination/osxp_pagination.html
archived_at: '2026-07-15T07:17:46.339644Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Printing Programming Guide for Mac](About%20Printing%20on%20the%20Mac.md)


[Next](Managing%20and%20Extending%20the%20Print%20Panel.md)[Previous](Printing%20From%20Your%20App.md)

# Laying Out Page Content

When a view is printed, there are several options for how it is placed on the page. If the view is larger than a single page, the view can be clipped, resized, or tiled across multiple pages. The view’s location on each page can be adjusted. Finally, the view can add adornments to each page. The following sections describe the options available for placing the view onto a page.

When a view is too large to fit onto a single page, the view can be printed in one of several ways. The view can tile itself out onto separate logical pages so that its entire visible region is printed. Alternatively, the view can clip itself and print only the area that fits on the first page. Finally, the view can resize itself to fit onto a single page. These options can be set using the `NSPrintInfo` object’s `setHorizontalPagination:` and `setVerticalPagination:` methods with the constants `NSClipPagination`, `NSFitPagination`, and `NSAutoPagination`. The separate methods for horizontal and vertical pagination allow you to mix these behaviors. For example, you can clip the image in one dimension, but tile it in the other. If these options are not sufficient, the view can also implement its own pagination scheme. The following sections describe each option.

To provide a completely custom pagination scheme that does not use the built-in pagination support of the `NSView` class, a view needs to implement only two simple methods and set

1. Set up the pagination mode (`NSPrintingPaginationMode`) using the the appropriate method of `NSPrintInfo` (`setHorizontalPagination:` or `setVerticalPagination:`
2. Override the `knowsPageRange:` method so it returns `YES` to indicate the custom view will collocate the dimension of each page.
3. Implement the `rectForPage:` method so it uses the page page number and the current printing information to calculate an appropriate rectangle in the view’s coordinate system. The printing system sends a `rectForPage:` message to your app before each page is printed, base on the range of pages the user selects in the Print panel. Note that the vertical and horizontal pagination settings in the `NSPrintInfo` object are ignored (unless your implementation takes them into account).

Listing 4-1 shows a simple implementation that splits a view vertically into pages that have the maximum size. The code does not show setting the pagination mode, which you must do.

__Listing 4-1__  Code that splits the view vertically into pages

```objc
// Return the number of pages available for printing
- (BOOL)knowsPageRange:(NSRangePointer)range {
    NSRect bounds = [self bounds];
    float printHeight = [self calculatePrintHeight];

    range->location = 1;
    range->length = NSHeight(bounds) / printHeight + 1;
    return YES;
}

// Return the drawing rectangle for a particular page number
- (NSRect)rectForPage:(int)page {
    NSRect bounds = [self bounds];
    float pageHeight = [self calculatePrintHeight];
    return NSMakeRect( NSMinX(bounds), NSMaxY(bounds) - page * pageHeight,
                        NSWidth(bounds), pageHeight );
}

// Calculate the vertical size of the view that fits on a single page
- (float)calculatePrintHeight {
    // Obtain the print info object for the current operation
    NSPrintInfo *pi = [[NSPrintOperation currentOperation] printInfo];

    // Calculate the page height in points
    NSSize paperSize = [pi paperSize];
    float pageHeight = paperSize.height - [pi topMargin] - [pi bottomMargin];

    // Convert height to the scaled view
    float scale = [[[pi dictionary] objectForKey:NSPrintScalingFactor]
                    floatValue];
    return pageHeight / scale;
}
```


When you perform custom pagination, you can override the `drawPageBorderWithSize:` method to add extra features to the page, such as crop marks, date/time strings, or page numbers. When you override `drawPageBorderWithSize:`:

1. Save the view’s existing body frame—you will need to restore it at the end of the method.
2. Resize the body frame to a rect with origin `(0,0)` and a size equal to the incoming `borderSize` parameter.

   This new frame now encompasses the margins instead of hiding them.
3. Add your custom border elements to all four margin areas (top, bottom, left, and right).

   You typically use the `drawAtPoint:` method for drawing. Any set of drawing calls must be preceded by `lockFocus:` and followed by `unlockFocus:`, otherwise `drawPageBorderWithSize:` will not draw anything to the page for those calls.

   Use the paper and margin dimensions from the print info object to constrain the printable area and prevent `drawPageBorderWithSize:` from printing within the body text frame. If you want to print within the body text frame—to print a watermark, for example—do so by printing directly in the newly enlarged frame and ignoring the margin constraints.
4. Reset the frame to the body text area before exiting the method.

   This assures the next page of content will print only within the paginated portion of the view.

If the view does not supply its own pagination information and one of the print info object’s pagination settings is `NSAutoPagination`, `NSView` tries to fit as much of the view being printed onto a logical page, slicing the view into the largest possible chunks along the given direction (horizontal or vertical). This is sufficient for many views, but if a view’s image must be divided only at certain places—between lines of text or cells in a table, for example—the view can adjust the automatic mechanism to accommodate this by reducing the height or width of each page.

Before printing begins, the view calculates the positions of all the row and column page breaks and gives you an opportunity to adjust them. The `adjustPageHeightNew:top:bottom:limit:` method provides an out parameter for the new bottom coordinate of the page, followed by the proposed top and bottom. An additional parameter limits the height of the page; the bottom can’t be moved above it. The `adjustPageWidthNew:left:right:limit:` method works in the same way to allow the view to adjust the width of a page. The limits are calculated as a percentage of the proposed page’s height or width. Your view subclass can also customize this percentage by overriding the methods `heightAdjustLimit` and `widthAdjustLimit` to return the fraction of the page that can be adjusted; a value of zero indicates that no adjustments are allowed whereas a value of one indicates that the right or bottom edge of the page bounds can be adjusted all the way to the left or top edge.

If one of the print info object’s pagination values is `NSClipPagination`, the view is clipped to a single page along that dimension. If the horizontal pagination is set to clipped, the left most section of the view is printed, clipped to the width of a single page. If the vertical pagination is set to clipped, the top most section of the view is printed, clipped to the height of a single page.

If the print info object’s pagination setting is `NSFitPagination`, the image is resized to fit onto the page. Although vertical and horizontal pagination need not be the same, if either dimension is scaled, the other dimension is scaled by the same amount to avoid distorting the image. If both dimensions are scaled, the scaling factor that produces the smaller image is used, thereby avoiding both distortion and clipping. Note that print info object’s scaling factor (`NSPrintScalingFactor`), which the user sets in the Page Layout panel, is independent of the scaling that’s imposed by pagination and is applied after the pagination scaling.

The `NSView` method `locationOfPrintRect:` places content according to several print info attributes. By default it places the image in the upper left corner of the page, but if the print info object’s `isHorizontallyCentered` or `isVerticallyCentered` methods return `YES`, it centers a single-page image along the appropriate axis. A multiple-page document, however, is always placed at the top left corner of the page so that the divided pieces can be assembled at their edges.

Override this method to position the image yourself. The point returned by `locationOfPrintRect:` is relative to the bottom-left corner of the paper in page coordinates. You need to include the page margins when calculating the position.

After the `NSView` position the rectangle on the page, it invokes `drawPageBorderWithSize:`. If you haven’t implemented this method, nothing happens. If you have implemented `drawPageBorderWithSize:`, any extra marks—crop marks, page numbers, and so on—you draw in this method are added to the page. The `drawPageBorderWithSize:` method is invoked by the printing system once for each page.

See [Custom Pagination](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2tcljrge4tgobs) for more information on using `drawPageBorderWithSize:`.

[Next](Managing%20and%20Extending%20the%20Print%20Panel.md)[Previous](Printing%20From%20Your%20App.md)

