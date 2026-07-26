---
title: 'setTextCombine:inRange:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecaption/settextcombine:inrange:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaption/settextcombine:inrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaption/settextcombine%3Ainrange%3A.json'
content_hash: 'sha256:5ae50226a568dfa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCaption](../avmutablecaption.md)

# setTextCombine:inRange:

<sub>Instance Method</sub>

Sets text combine for a range.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (void) setTextCombine:(AVCaptionTextCombine) textCombine inRange:(NSRange) range;
```

## Parameters

- `textCombine` — The text combine.

- `range` — The range to which the text combine applies.

## See Also

### Configuring advanced typography

- [Ruby](../avcaption/ruby.md) — An object that presents ruby characters.
- [setRuby:inRange:](setruby_inrange_.md) — Sets ruby text for a range.
- [removeRubyInRange:](removerubyinrange_.md) — Removes ruby text from a range.
- [TextCombine](../avcaption/textcombine.md) — The caption’s supported rendering policy options.
- [removeTextCombineInRange:](removetextcombineinrange_.md) — Removes text combine from a range of text.
