---
title: text
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaption/text
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/text.json'
content_hash: 'sha256:b4629852900294e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# text

<sub>Instance Property</sub>

The caption text.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var text: String { get }
```

## Discussion

Apple iTT format text supports the same Unicode code points that an XML document supports. The system converts XML special characters like ‘&’ to corresponding character-reference syntax when it writes the caption to a file. The text may contain the line-breaking character sequences LF, CR, or CF+LF.

CEA608 closed captions support the following Unicode characters. They don’t support the line-breaking character sequences LF, CR, or CF+LF.

| Range | U+0020 - U+005F |
|---|---|
| Range | U+0061 - U+007E |
| Range | U+00A1 - U+00A5 |
| Characters | U+00A9, U+00AB, U+00AE, U+00B0, U+00BB, U+00BD, U+00BF |
| Range | U+00C0-U+00C5 |
| Range | U+00C7-U+00CF |
| Range | U+00D1-U+00D6 |
| Range | U+00D8-U+00DC |
| Range | U+00DF-U+00E5 |
| Range | U+00E7-U+00EF |
| Range | U+00F1-U+00FC |
| Range | U+2018-U+2019 |
| Range | U+2018-U+201D |
| Character | U+2022 |
| Range | U+2120-U+2122 |
| Characters | U+2501, U+2503, U+250F, U+2513, U+2517, U+251B, U+2588, U+266A |

## See Also

### Accessing text and timing

- [timeRange](timerange.md) — The time range over which the system presents the caption.
