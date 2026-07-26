---
title: 'CTFontCopyAvailableTables(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopyavailabletables(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopyavailabletables(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopyavailabletables%28_%3A_%3A%29.json'
content_hash: 'sha256:789093b93e05ae9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyAvailableTables(_:_:)

<sub>Function</sub>

Returns an array of font table tags.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyAvailableTables(_ font: CTFont, _ options: CTFontTableOptions) -> CFArray?
```

## Parameters

- `font` — The font reference.

- `options` — The font table options.

## Return Value

An array of [CTFontTableTag](ctfonttabletag.md) values for the given font and the supplied options.

## Discussion

The returned set will contain unboxed values, which can be extracted like so:

```objc
CTFontTableTag tag = (CTFontTableTag)(uintptr_t)CFArrayGetValueAtIndex(tags, index);
```

## See Also

### Getting Font Table Data

- [CTFontCopyTable](<ctfontcopytable(______).md>) — Returns a reference to the font table data.
