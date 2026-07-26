---
title: 'objectDidBeginEditing:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/objectdidbeginediting:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/objectdidbeginediting:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/objectdidbeginediting%3A.json'
content_hash: 'sha256:98e7bf0d999cc173'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# objectDidBeginEditing:

<sub>Instance Method</sub>

This message should be sent to the receiver when `editor` has uncommitted changes that can affect the receiver.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) objectDidBeginEditing:(id<NSEditor>) editor;
```

## See Also

### Related Documentation

- [Cocoa Bindings Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)
- [objectDidEndEditing:](objectdidendediting_.md) — This message should be sent to the receiver when `editor` has finished editing a property belonging to the receiver. _(deprecated)_
