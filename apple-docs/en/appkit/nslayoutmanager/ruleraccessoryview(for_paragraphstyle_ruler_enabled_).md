---
title: 'rulerAccessoryView(for:paragraphStyle:ruler:enabled:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/ruleraccessoryview(for:paragraphstyle:ruler:enabled:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/ruleraccessoryview(for:paragraphstyle:ruler:enabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/ruleraccessoryview%28for%3Aparagraphstyle%3Aruler%3Aenabled%3A%29.json'
content_hash: 'sha256:3f27eeab6e3dea29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# rulerAccessoryView(for:paragraphStyle:ruler:enabled:)

<sub>Instance Method</sub>

Returns the accessory view that the text system uses for its ruler.

<sub>macOS</sub>

```swift
func rulerAccessoryView(for view: NSTextView, paragraphStyle style: NSParagraphStyle, ruler: NSRulerView, enabled isEnabled: Bool) -> NSView?
```

## Parameters

- `view` — The text view using the layout manager.

- `style` — Sets the state of the controls in the accessory view; must not be `nil`.

- `ruler` — The ruler view whose accessory view is returned.

- `isEnabled` — If [true](../../swift/true.md), the accessory view is enabled and accepts mouse and keyboard events; if [false](../../swift/false.md) it’s disabled.

## Return Value

The accessory view containing tab wells, text alignment buttons, and so on.

## Discussion

If you have turned off automatic ruler updating through the use of [usesRuler](../nstextview/usesruler.md) so that you can do more complex things, but you still want to display the appropriate accessory view, you can use this method.

This method is invoked automatically by the [NSTextView](../nstextview.md) object using the layout manager. You should rarely need to invoke it, but you can override it to customize ruler support. If you do use this method directly, note that it neither installs the ruler accessory view nor sets the markers for the [NSRulerView](../nsrulerview.md) object. You must install the accessory view into the ruler using the [NSRulerView](../nsrulerview.md) method [accessoryView](../nsrulerview/accessoryview.md). To set the markers, use [- rulerMarkersForTextView:paragraphStyle:ruler:](<rulermarkers(for_paragraphstyle_ruler_).md>) to get the markers needed, and then send [markers](../nsrulerview/markers.md) to the ruler.

## See Also

### Handling Rulers

- [- rulerMarkersForTextView:paragraphStyle:ruler:](<rulermarkers(for_paragraphstyle_ruler_).md>) — Returns an array of text ruler objects for the current selection.
