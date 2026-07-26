---
title: 'setTextCombine(_:in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecaption/settextcombine(_:in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaption/settextcombine(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaption/settextcombine%28_%3Ain%3A%29.json'
content_hash: 'sha256:6880961f7a42b0c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCaption](../avmutablecaption.md)

# setTextCombine(_:in:)

<sub>Instance Method</sub>

Sets text combine for a range.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func setTextCombine(_ textCombine: AVCaption.TextCombine, in range: NSRange)
```

## Parameters

- `textCombine` — The text combine.

- `range` — The range to which the text combine applies.

## See Also

### Configuring advanced typography

- [Ruby](../avcaption/ruby.md) — An object that presents ruby characters.
- [setRuby(_:in:)](<setruby(__in_).md>) — Sets ruby text for a range.
- [removeRuby(in:)](<removeruby(in_).md>) — Removes ruby text from a range.
- [TextCombine](../avcaption/textcombine.md) — The caption’s supported rendering policy options.
- [removeTextCombine(in:)](<removetextcombine(in_).md>) — Removes text combine from a range.
