---
title: 'Exhibition: An Adaptive OS X App'
apple_id: TP40016178
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/Exhibition/Listings/Exhibition_CenteringClipView_swift.html
archived_at: '2026-07-18T03:08:00.578000Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Exhibition: An Adaptive OS X App](Exhibition-%20An%20Adaptive%20OS%20X%20App.md)


[Next](README.md.md)[Previous](Exhibition-ImageCollectionListController.swift.md)

# Exhibition/CenteringClipView.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Contains the definition for `CenteringClipView` which is a specialized clip view subclass to center its document.
*/

import Cocoa

/**
    `CenteringClipView` is a clip view subclass that centers smaller documents views
    within its inset clip bounds (as described by the set `contentInsets`).
*/
class CenteringClipView: NSClipView {
    override func constrainBoundsRect(_ proposedBounds: NSRect) -> NSRect {
        guard let documentView = documentView else { return super.constrainBoundsRect(proposedBounds) }

        var newClipBoundsRect = super.constrainBoundsRect(proposedBounds)

        // Get the `contentInsets` scaled to the future bounds size.
        let insets = convertedContentInsetsToProposedBoundsSize(newClipBoundsRect.size)

        // Get the insets in terms of the view geometry edges, accounting for flippedness.
        let minYInset = isFlipped ? insets.top : insets.bottom
        let maxYInset = isFlipped ? insets.bottom : insets.top
        let minXInset = insets.left
        let maxXInset = insets.right

        /*
            Get and outset the `documentView`'s frame by the scaled contentInsets.
            The outset frame is used to align and constrain the `newClipBoundsRect`.
        */
        let documentFrame = documentView.frame
        let outsetDocumentFrame = NSRect(x: documentFrame.minX - minXInset,
                                         y: documentFrame.minY - minYInset,
                                     width: (documentFrame.width + (minXInset + maxXInset)),
                                    height: documentFrame.height + (minYInset + maxYInset))

        if newClipBoundsRect.width > outsetDocumentFrame.width {
            /*
                If the clip bounds width is larger than the document, center the
                bounds around the document.
            */
            newClipBoundsRect.origin.x = outsetDocumentFrame.minX - (newClipBoundsRect.width - outsetDocumentFrame.width) / 2.0
        }
        else if newClipBoundsRect.width < outsetDocumentFrame.width {
            /*
                Otherwise, the document is wider than the clip rect. Make sure that 
                the clip rect stays within the document frame.
            */
            if newClipBoundsRect.maxX > outsetDocumentFrame.maxX {
                // The clip rect is outside the maxX edge of the document, bring it in.
                newClipBoundsRect.origin.x = outsetDocumentFrame.maxX - newClipBoundsRect.width
            }
            else if newClipBoundsRect.minX < outsetDocumentFrame.minX {
                // The clip rect is outside the minX edge of the document, bring it in.
                newClipBoundsRect.origin.x = outsetDocumentFrame.minX
            }
        }

        if newClipBoundsRect.height > outsetDocumentFrame.height {
            /*
                If the clip bounds height is larger than the document, center the 
                bounds around the document.
            */
            newClipBoundsRect.origin.y = outsetDocumentFrame.minY - (newClipBoundsRect.height - outsetDocumentFrame.height) / 2.0
        }
        else if newClipBoundsRect.height < outsetDocumentFrame.height {
            /*
                Otherwise, the document is taller than the clip rect. Make sure 
                that the clip rect stays within the document frame.
            */
            if newClipBoundsRect.maxY > outsetDocumentFrame.maxY {
                // The clip rect is outside the maxY edge of the document, bring it in.
                newClipBoundsRect.origin.y = outsetDocumentFrame.maxY - newClipBoundsRect.height
            }
            else if newClipBoundsRect.minY < outsetDocumentFrame.minY {
                // The clip rect is outside the minY edge of the document, bring it in.
                newClipBoundsRect.origin.y = outsetDocumentFrame.minY
            }
        }

        return backingAlignedRect(newClipBoundsRect, options: .alignAllEdgesNearest)
    }

    /**
        The `contentInsets` scaled to the scale factor of a new potential bounds
        rect. Used by `constrainBoundsRect(NSRect)`.
    */
    fileprivate func convertedContentInsetsToProposedBoundsSize(_ proposedBoundsSize: NSSize) -> EdgeInsets {
        // Base the scale factor on the width scale factor to the new proposedBounds.
        let fromBoundsToProposedBoundsFactor = bounds.width > 0 ? (proposedBoundsSize.width / bounds.width) : 1.0

        // Scale the set `contentInsets` by the width scale factor.
        var newContentInsets = contentInsets
        newContentInsets.top *= fromBoundsToProposedBoundsFactor
        newContentInsets.left *= fromBoundsToProposedBoundsFactor
        newContentInsets.bottom *= fromBoundsToProposedBoundsFactor
        newContentInsets.right *= fromBoundsToProposedBoundsFactor

        return newContentInsets
    }
}
```

[Next](README.md.md)[Previous](Exhibition-ImageCollectionListController.swift.md)

