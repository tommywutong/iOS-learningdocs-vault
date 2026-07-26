---
title: commitEditing
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/commitediting
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commitediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/commitediting.json'
content_hash: 'sha256:40b84cb366d056cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# commitEditing

<sub>Instance Method</sub>

Returns whether the receiver was able to commit any pending edits.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) commitEditing;
```

## Return Value

[YES](../yes.md) if the changes were successfully applied to the model, [NO](../no.md) otherwise.

## Discussion

A commit is denied if the receiver fails to apply the changes to the model object, perhaps due to a validation error.

## See Also

### Related Documentation

- [discardEditing](discardediting.md) — Causes the receiver to discard any changes, restoring the previous values. _(deprecated)_
