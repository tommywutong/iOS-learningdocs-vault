---
title: inputImageMaximumSize()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext/inputimagemaximumsize()
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/inputimagemaximumsize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/inputimagemaximumsize%28%29.json'
content_hash: 'sha256:55585d2cae299c7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# inputImageMaximumSize()

<sub>Instance Method</sub>

Returns the maximum size allowed for any image rendered into the context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func inputImageMaximumSize() -> CGSize
```

## Discussion

Some contexts limit the maximum size of an image that can be rendered into them. For example, the maximum size might reflect a limitation in the underlying graphics hardware.

## See Also

### Determining the Allowed Extents for Images Used by a Context

- [- outputImageMaximumSize](<outputimagemaximumsize().md>) — Returns the maximum size allowed for any image created by the context.
