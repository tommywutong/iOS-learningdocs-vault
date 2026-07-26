---
title: 'setRuby(_:in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecaption/setruby(_:in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaption/setruby(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaption/setruby%28_%3Ain%3A%29.json'
content_hash: 'sha256:92ee9e418cfe1344'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCaption](../avmutablecaption.md)

# setRuby(_:in:)

<sub>Instance Method</sub>

Sets ruby text for a range.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func setRuby(_ rubyText: AVCaption.Ruby, in range: NSRange)
```

## Parameters

- `rubyText` — The ruby text.

- `range` — The range to which the ruby text applies.

## See Also

### Configuring advanced typography

- [Ruby](../avcaption/ruby.md) — An object that presents ruby characters.
- [removeRuby(in:)](<removeruby(in_).md>) — Removes ruby text from a range.
- [TextCombine](../avcaption/textcombine.md) — The caption’s supported rendering policy options.
- [setTextCombine(_:in:)](<settextcombine(__in_).md>) — Sets text combine for a range.
- [removeTextCombine(in:)](<removetextcombine(in_).md>) — Removes text combine from a range.
