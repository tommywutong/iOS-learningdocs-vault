---
title: 'load(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cipluginregistration/load(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cipluginregistration/load(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipluginregistration/load%28_%3A%29.json'
content_hash: 'sha256:ce431b7c2352546a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPlugInRegistration](../cipluginregistration.md)

# load(_:)

<sub>Instance Method</sub>

Loads and initializes an image unit, performing custom tasks as needed.

<sub>macOS</sub>

```swift
func load(_ host: UnsafeMutableRawPointer!) -> Bool
```

## Parameters

- `host` — Reserved for future use.

## Return Value

Returns `true` if the image unit is successfully initialized

## Discussion

The `load` method is called once by the host to initialize the image unit when the first filter in the image unit is instantiated. The method provides the image unit with an opportunity to perform custom initialization, such as a registration check.

## See Also

### Related Documentation

- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [Image Unit Tutorial](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004531)
