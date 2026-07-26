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
doc_path: '/documentation/uikit/nstextelementprovider/adjustedrange(from:foreditingtextselection:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextelementprovider/adjustedrange(from:foreditingtextselection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelementprovider/adjustedrange%28from%3Aforeditingtextselection%3A%29.json'
content_hash: 'sha256:cf075b818af573b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextElementProvider](../nstextelementprovider.md)

# adjustedRange(from:forEditingTextSelection:)

<sub>Instance Method</sub>

A method you implement if the location backing store requires manual adjustment after editing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func adjustedRange(from textRange: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?
```

## Parameters

- `textRange` — An [NSTextRange](../nstextrange.md) that the method adjusts.

- `forEditingTextSelection` — A Boolean value that indicates if `textRange` is for the text selection associated with the edit session.

## Return Value

When `textRange` is intersecting or following the current edited range, the method returns the range adjusted for the modification in the editing session. Returns `nil`, when no adjustment necessary.

## See Also

### Adjusting the range of the text element

- [- offsetFromLocation:toLocation:](<offset(from_to_).md>) — Returns the offset between the two specified locations.
