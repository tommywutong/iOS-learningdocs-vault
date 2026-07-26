---
title: 'objectDidEndEditing:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/objectdidendediting:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/objectdidendediting:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/objectdidendediting%3A.json'
content_hash: 'sha256:7188aaff6b032c37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# objectDidEndEditing:

<sub>Instance Method</sub>

This message should be sent to the receiver when `editor` has finished editing a property belonging to the receiver.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) objectDidEndEditing:(id<NSEditor>) editor;
```

## See Also

### Related Documentation

- [objectDidBeginEditing:](objectdidbeginediting_.md) — This message should be sent to the receiver when `editor` has uncommitted changes that can affect the receiver. _(deprecated)_
