---
title: NSStringFromUIOffset
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringfromuioffset
source_url: 'https://developer.apple.com/documentation/uikit/nsstringfromuioffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringfromuioffset.json'
content_hash: 'sha256:4bb0e5d443e70968'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSStringFromUIOffset

<sub>Function</sub>

Returns a string formatted to contain the data from an offset structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString *NSStringFromUIOffset(UIOffset offset);
```

## Parameters

- `offset` — A UIKit offset data structure.

## Return Value

A string that corresponds to `offset`.

## See Also

### Converting to and from strings

- [UIOffsetFromString](uioffsetfromstring.md) — Returns a UIKit offset structure corresponding to the data in a given string.
