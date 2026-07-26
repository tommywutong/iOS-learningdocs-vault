---
title: 'enumerateTextElements(from:options:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextelementprovider/enumeratetextelements(from:options:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextelementprovider/enumeratetextelements(from:options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelementprovider/enumeratetextelements%28from%3Aoptions%3Ausing%3A%29.json'
content_hash: 'sha256:fd7acffcad5a2e40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextElementProvider](../nstextelementprovider.md)

# enumerateTextElements(from:options:using:)

<sub>Instance Method</sub>

Enumerates text elements starting at the text location you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func enumerateTextElements(from textLocation: (any NSTextLocation)?, options: NSTextContentManager.EnumerationOptions = [], using block: (NSTextElement) -> Bool) -> (any NSTextLocation)?
```

## Parameters

- `textLocation` — The [NSTextLocation](../nstextlocation.md) at which to start the enumeration.

- `options` — One of the possible `NSTextElementProviderEnumerationOptions` directions.

- `block` — A block you use to evaluate whether to continue the enumeration or tell the method to stop. Return `false` to end the enumeration process.

## Return Value

An `NSTextLocation`.

## Discussion

If `textLocation` is `nil`, the method uses `documentRange.location` for forward enumeration and `documentRange.endLocation` for reverse enumeration. When enumerating backward, the method starts with the element preceding the one containing `textLocation`. If enumerated at least one element, it returns the edge of the enumerated range.

The enumerated range might not match the range of the last element returned. It enumerates the elements in the sequence, but it can skip a range (it can limit the maximum number of text elements enumerated for a single invocation or hide some elements from the layout).

Returning `NO` or `false` from block breaks out of the enumeration.

## See Also

### Accessing and updating the text

- [EnumerationOptions](../nstextlayoutfragment/enumerationoptions.md) — Values that describe options for enumerating text layout fragments.
- [- locationFromLocation:withOffset:](<location(__offsetby_).md>) — Returns a new location from location with offset you provide.
- [- replaceContentsInRange:withTextElements:](<replacecontents(in_with_).md>) — Replaces the characters specified by range with the text elements you provide.
