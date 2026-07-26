---
title: 'connect(_:withKey:to:withKey:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/connect(_:withkey:to:withkey:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/connect(_:withkey:to:withkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/connect%28_%3Awithkey%3Ato%3Awithkey%3A%29.json'
content_hash: 'sha256:be70e0501065bca5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# connect(_:withKey:to:withKey:)

<sub>Instance Method</sub>

Adds an object to the filter chain.

<sub>macOS</sub>

```swift
func connect(_ sourceObject: Any, withKey sourceKey: String?, to targetObject: Any, withKey targetKey: String)
```

## Parameters

- `sourceObject` — A [CIFilter](../cifilter-swift.class.md) object, a  [CIImage](../ciimage.md) object, or the path (an [NSString](../../foundation/nsstring.md) or [NSURL](../../foundation/nsurl.md) object) to an image.

- `sourceKey` — The key that specifies the source object. For example, if the source is the output image of a filter, pass the `outputImage` key. Pass `nil` if the source object is used directly.

- `targetObject` — The object to which the source object links.

- `targetKey` — The key that specifies the target for the source. For example, if you are connecting the source to the input image of a [CIFilter](../cifilter-swift.class.md) object, you would pass the `inputImage` key.

## See Also

### Connecting and Disconnecting Objects

- [- disconnectObject:withKey:toObject:withKey:](<disconnectobject(__withkey_to_withkey_).md>) — Removes the connection between two objects in the filter chain.
