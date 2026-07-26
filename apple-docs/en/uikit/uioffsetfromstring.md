---
title: UIOffsetFromString
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uioffsetfromstring
source_url: 'https://developer.apple.com/documentation/uikit/uioffsetfromstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uioffsetfromstring.json'
content_hash: 'sha256:46d7091442cc690d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIOffsetFromString

<sub>Function</sub>

Returns a UIKit offset structure corresponding to the data in a given string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern UIOffset UIOffsetFromString(NSString *string);
```

## Parameters

- `string` — A string containing a representation of an offset.

## Return Value

An edge insets data structure. If the string is not well-formed, the function returns [UIOffsetZero](uioffset/zero.md).

## Discussion

In general, you should use this function only to convert strings that were previously created using the [NSStringFromUIOffset](nsstringfromuioffset.md) function.

## See Also

### Converting to and from strings

- [NSStringFromUIOffset](nsstringfromuioffset.md) — Returns a string formatted to contain the data from an offset structure.
