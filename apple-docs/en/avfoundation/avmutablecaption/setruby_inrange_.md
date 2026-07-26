---
title: 'setRuby:inRange:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecaption/setruby:inrange:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaption/setruby:inrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaption/setruby%3Ainrange%3A.json'
content_hash: 'sha256:51b06c6609161c33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCaption](../avmutablecaption.md)

# setRuby:inRange:

<sub>Instance Method</sub>

Sets ruby text for a range.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (void) setRuby:(AVCaptionRuby *) ruby inRange:(NSRange) range;
```

## Parameters

- `ruby` — The ruby text.

- `range` — The range to which the ruby text applies.

## See Also

### Configuring advanced typography

- [Ruby](../avcaption/ruby.md) — An object that presents ruby characters.
- [removeRubyInRange:](removerubyinrange_.md) — Removes ruby text from a range.
- [TextCombine](../avcaption/textcombine.md) — The caption’s supported rendering policy options.
- [setTextCombine:inRange:](settextcombine_inrange_.md) — Sets text combine for a range.
- [removeTextCombineInRange:](removetextcombineinrange_.md) — Removes text combine from a range of text.
