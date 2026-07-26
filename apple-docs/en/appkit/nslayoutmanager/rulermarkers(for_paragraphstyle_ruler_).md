---
title: 'rulerMarkers(for:paragraphStyle:ruler:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/rulermarkers(for:paragraphstyle:ruler:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/rulermarkers(for:paragraphstyle:ruler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/rulermarkers%28for%3Aparagraphstyle%3Aruler%3A%29.json'
content_hash: 'sha256:63d84b5d84e797a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# rulerMarkers(for:paragraphStyle:ruler:)

<sub>Instance Method</sub>

Returns an array of text ruler objects for the current selection.

<sub>macOS</sub>

```swift
func rulerMarkers(for view: NSTextView, paragraphStyle style: NSParagraphStyle, ruler: NSRulerView) -> [NSRulerMarker]
```

## Parameters

- `view` — The text view using the layout manager.

- `style` — Sets the state of the controls in the accessory view; must not be `nil`.

- `ruler` — The ruler view whose ruler markers are returned.

## Return Value

An array of [NSRulerMarker](../nsrulermarker.md) objects representing such things as left and right margins, first-line indent, and tab stops.

## Discussion

If you have turned off automatic ruler updating through the use of [usesRuler](../nstextview/usesruler.md) so that you can do more complex things, but you still want to display the appropriate accessory view, you can use this method.

This method is invoked automatically by the `NSTextView` object using the layout manager. You should rarely need to invoke it, but you can override it to add new kinds of markers or otherwise customize ruler support.

You can set the returned ruler markers with the `NSRulerView` method [markers](../nsrulerview/markers.md).

## See Also

### Handling Rulers

- [- rulerAccessoryViewForTextView:paragraphStyle:ruler:enabled:](<ruleraccessoryview(for_paragraphstyle_ruler_enabled_).md>) — Returns the accessory view that the text system uses for its ruler.
