---
title: makeRenderCommandEncoder()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlparallelrendercommandencoder/makerendercommandencoder()
source_url: 'https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/makerendercommandencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlparallelrendercommandencoder/makerendercommandencoder%28%29.json'
content_hash: 'sha256:26e7e21e1a3ce244'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLParallelRenderCommandEncoder](../mtlparallelrendercommandencoder.md)

# makeRenderCommandEncoder()

<sub>Instance Method</sub>

Create an object that encodes commands that perform graphics rendering operations and may be assigned to a different thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderCommandEncoder() -> (any MTLRenderCommandEncoder)?
```

## Return Value

A graphics rendering command encoder object

## Discussion

The rendering commands encoded by [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) objects are executed in the order in which the [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) objects are created, not in the order they are ended.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
