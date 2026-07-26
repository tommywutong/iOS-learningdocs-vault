---
title: 'CTFontCopyTable(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopytable(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopytable(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopytable%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cc7e48d328943f71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyTable(_:_:_:)

<sub>Function</sub>

Returns a reference to the font table data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyTable(_ font: CTFont, _ table: CTFontTableTag, _ options: CTFontTableOptions) -> CFData?
```

## Parameters

- `font` — The font reference.

- `table` — The font table identifier as a [CTFontTableTag](ctfonttabletag.md) constant. See [CTFontTableTag](ctfonttabletag.md) for possible values.

- `options` — The font table options.

## Return Value

A retained reference to the font table data as a [CFData](../corefoundation/cfdata.md) object. The table data is not actually copied; however, the data reference must be released.

## See Also

### Getting Font Table Data

- [CTFontCopyAvailableTables](<ctfontcopyavailabletables(____).md>) — Returns an array of font table tags.
