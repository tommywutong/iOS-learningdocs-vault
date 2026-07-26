---
title: 'replaceTextStorage(_:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/replacetextstorage(_:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/replacetextstorage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/replacetextstorage%28_%3A%29.json'
content_hash: 'sha256:56fa3b406f649501'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# replaceTextStorage(_:)

<sub>Instance Method</sub>

Replaces the layout manager’s current text storage object with the specified object.

<sub>macOS</sub>

```swift
func replaceTextStorage(_ newTextStorage: NSTextStorage)
```

## Parameters

- `newTextStorage` — The text storage object to set.

## Discussion

Use this method to update the text storage uniformly for a group of related layout manager objects. Unlike changing the value in the textStorage property, this method replaces the text storage for all [NSLayoutManager](../nslayoutmanager.md) objects that share the current layout manager’s [NSTextStorage](../nstextstorage.md) object.

## See Also

### Accessing the text storage

- [textStorage](textstorage.md) — The text storage object that contains the content to lay out.
