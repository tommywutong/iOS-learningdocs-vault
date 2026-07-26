---
title: usesStandardTextScaling
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/usesstandardtextscaling
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/usesstandardtextscaling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/usesstandardtextscaling.json'
content_hash: 'sha256:5fdb1b1b311b3756'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# usesStandardTextScaling

<sub>Instance Property</sub>

A Boolean value that determines the rendering scale of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var usesStandardTextScaling: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), UIKit automatically adjusts the rendering of the text in the text view to match the standard text scaling.

When using the standard text scaling, font sizes in the text view appear visually similar to how they would render in macOS and non-Apple platforms, and copying the contents of the text view to the pasteboard preserves the original font point sizes. This effectively changes the display size of the text without changing the actual font point size. For example, text using a 13-point font in iOS looks like text using a 13-point font in macOS.

If your app is built with Mac Catalyst, or if your text view’s contents save to a document that a user can view in macOS or other platforms, set this property to [true](../../swift/true.md).

The default value of this property is [false](../../swift/false.md).

## See Also

### Related Documentation

- [NSTextScalingType](../nstextscalingtype.md) — Constants that specify the text scaling.
- [textScaling](../../foundation/nsattributedstring/documentattributekey/textscaling.md) — The text-scaling mode to use when displaying the text.
- [sourceTextScaling](../../foundation/nsattributedstring/documentattributekey/sourcetextscaling.md) — The text-scaling mode you used when creating the text.
- [targetTextScaling](../../foundation/nsattributedstring/documentreadingoptionkey/targettextscaling.md) — The text scaling mode to use after reading the text from disk.
- [sourceTextScaling](../../foundation/nsattributedstring/documentreadingoptionkey/sourcetextscaling.md) — The text-scaling mode to associate with the document’s content.

### Configuring layout attributes

- [textContainerInset](textcontainerinset.md) — The inset of the text container’s layout area within the text view’s content area.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
