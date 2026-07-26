---
title: endEncoding()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandencoder/endencoding()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandencoder/endencoding()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandencoder/endencoding%28%29.json'
content_hash: 'sha256:3ebefb6f8cfe424f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandEncoder](../mtlcommandencoder.md)

# endEncoding()

<sub>Instance Method</sub>

Declares that all command generation from the encoder is completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func endEncoding()
```

## Discussion

After `endEncoding` is called, the command encoder has no further use. You cannot encode any other commands with this encoder.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
