---
title: discardEditing
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/discardediting
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/discardediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/discardediting.json'
content_hash: 'sha256:3dd5c3aa890798cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# discardEditing

<sub>Instance Method</sub>

Causes the receiver to discard any changes, restoring the previous values.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) discardEditing;
```

## See Also

### Related Documentation

- [Cocoa Bindings Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)
- [commitEditing](commitediting.md) — Returns whether the receiver was able to commit any pending edits. _(deprecated)_
