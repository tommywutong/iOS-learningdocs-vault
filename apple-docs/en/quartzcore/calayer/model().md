---
title: model()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/model()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/model()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/model%28%29.json'
content_hash: 'sha256:ff4a7f194a50d969'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# model()

<sub>Instance Method</sub>

Returns the model layer object associated with the receiver, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func model() -> Self
```

## Return Value

A layer instance representing the underlying model layer.

## Discussion

Calling this method on a layer in the presentation tree returns the corresponding layer object in the model tree. This method returns a value only when a transaction involving changes to the presentation layer is in progress. If no transaction is in progress, the results of calling this method are undefined.

## See Also

### Accessing related layer objects

- [- presentationLayer](<presentation().md>) — Returns a copy of the presentation layer object that represents the state of the layer as it currently appears onscreen.
