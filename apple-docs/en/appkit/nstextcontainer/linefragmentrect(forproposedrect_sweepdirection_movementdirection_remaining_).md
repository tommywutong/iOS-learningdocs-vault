---
title: 'lineFragmentRect(forProposedRect:sweepDirection:movementDirection:remaining:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/appkit/nstextcontainer/linefragmentrect(forproposedrect:sweepdirection:movementdirection:remaining:)'
source_url: 'https://developer.apple.com/documentation/appkit/nstextcontainer/linefragmentrect(forproposedrect:sweepdirection:movementdirection:remaining:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextcontainer/linefragmentrect%28forproposedrect%3Asweepdirection%3Amovementdirection%3Aremaining%3A%29.json'
content_hash: 'sha256:2ceb1deb7ca96381'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextContainer](../nstextcontainer.md)

# lineFragmentRect(forProposedRect:sweepDirection:movementDirection:remaining:)

<sub>Instance Method</sub>

Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.

> [!warning] Deprecated
> Use [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) instead.

<sub>macOS</sub>

```swift
func lineFragmentRect(forProposedRect proposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining remainingRect: NSRectPointer?) -> NSRect
```

## Parameters

- `proposedRect` — The proposed rectangle in which to layout text.

- `sweepDirection` — The line sweep direction.

- `movementDirection` — The line movement direction.

- `remainingRect` — Upon return, the unused, possibly shifted, portion of `proposedRect` that’s available for further text, or `NSZeroRect` if there is no remainder.

## Return Value

The longest rectangle available in the proposed rectangle for displaying text, or `NSZeroRect` if there is none according to the receiver’s region definition.

## Discussion

There is no guarantee as to the width of the proposed rectangle or to its location. For example, the proposed rectangle is likely to be much wider than the width of the receiver. The receiver should examine `proposedRect` to see that it intersects its bounding rectangle and should return a modified rectangle based on `sweepDirection` and `movementDirection`, whose possible values are listed in the class description. If `sweepDirection` is `NSLineSweepRight`, for example, the receiver uses this information to trim the right end of `proposedRect` as needed rather than the left end.

If `proposedRect` doesn’t completely overlap the region along the axis of `movementDirection` and `movementDirection` isn’t `NSLineDoesntMove`, this method can either shift the rectangle in that direction as much as needed so that it does completely overlap, or return `NSZeroRect` to indicate that the proposed rectangle simply doesn’t fit.

## See Also

### Deprecated

- [- initWithContainerSize:](<init(containersize_).md>) — Initializes a text container with a specified bounding rectangle. _(deprecated)_
- [- containsPoint:](<contains(__).md>) — Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle. _(deprecated)_
- [containerSize](containersize.md) — The size of the text container’s bounding rectangle. _(deprecated)_
