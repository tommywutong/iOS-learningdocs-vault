---
title: 'adjustedRange(from:forEditingTextSelection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentstorage/adjustedrange(from:foreditingtextselection:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstorage/adjustedrange(from:foreditingtextselection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstorage/adjustedrange%28from%3Aforeditingtextselection%3A%29.json'
content_hash: 'sha256:fc5722bafeaa49e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentStorage](../nstextcontentstorage.md)

# adjustedRange(from:forEditingTextSelection:)

<sub>Instance Method</sub>

Returns the text range, if any, in the backing store that required manual adjustment after editing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func adjustedRange(from textRange: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?
```

## Parameters

- `textRange` — The text range.

- `forEditingTextSelection` — A Boolean value that indicates if `textRange` is for the text selection associated with the edit session.

## Return Value

The  adjusted `TextRange` for the editing session, or `nil` of no adjustment was necessary

## Discussion

When `textRange` is intersecting or following the current edited range, the method returns an adjusted range for the modification in the editing session.

## See Also

### Finding ranges, locations, and offsets

- [- locationFromLocation:withOffset:](<location(__offsetby_).md>) — Returns a new text location object based on an existing location and offset you provide.
- [- offsetFromLocation:toLocation:](<offset(from_to_).md>) — Returns the number of characters between the specified locations.
