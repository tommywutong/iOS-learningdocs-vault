---
title: Text System User Interface Layer Programming Guide
apple_id: 10000090i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/Tasks/MultipleViews.html
archived_at: '2026-07-15T07:20:37.245741Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System User Interface Layer Programming Guide](Introduction%20to%20Text%20System%20User%20Interface%20Layer.md)


[Next](Plain%20and%20Rich%20Text%20Objects.md)[Previous](Putting%20an%20NSTextView%20Object%20in%20an%20NSScrollView.md)

# Using Multiple NSTextViews

A single NSLayoutManager can be assigned any number of NSTextContainers, in whose NSTextViews it lays out text sequentially. In such a configuration, many of the attributes accessed through the NSTextView interface are actually shared by all of these text views. Among these attributes are:

- The selection
- The delegate
- Selectability
- Editability
- Whether they act as a field editor
- Whether they display plain or rich text
- Whether they import graphics
- Whether they use the ruler
- Whether the ruler is visible
- Whether they use the Font panel (Fonts window)

Setting any of these attributes causes all associated NSTextView objects to share the new value.

With multiple NSTextViews, only one is the first responder at any time. NSLayoutManager defines these methods for determining and appropriately setting the first responder:

- `layoutManagerOwnsFirstResponderInWindow:`
- `firstTextView`
- `textViewForBeginningOfSelection`

See their descriptions in the NSLayoutManager class specification for more information.

[Next](Plain%20and%20Rich%20Text%20Objects.md)[Previous](Putting%20an%20NSTextView%20Object%20in%20an%20NSScrollView.md)

