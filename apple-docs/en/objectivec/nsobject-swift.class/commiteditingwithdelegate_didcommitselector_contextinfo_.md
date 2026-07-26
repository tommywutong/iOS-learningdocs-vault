---
title: 'commitEditingWithDelegate:didCommitSelector:contextInfo:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/commiteditingwithdelegate:didcommitselector:contextinfo:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commiteditingwithdelegate:didcommitselector:contextinfo:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/commiteditingwithdelegate%3Adidcommitselector%3Acontextinfo%3A.json'
content_hash: 'sha256:cf0a5fc73d47e8e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# commitEditingWithDelegate:didCommitSelector:contextInfo:

<sub>Instance Method</sub>

Attempt to commit any currently edited results of the receiver.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) commitEditingWithDelegate:(id) delegate didCommitSelector:(SEL) didCommitSelector contextInfo:(void *) contextInfo;
```

## Discussion

The receiver must have been registered as the editor of an object using `objectDidBeginEditing:`, and has not yet been unregistered by a subsequent invocation of `objectDidEndEditing:`. When the committing has either succeeded or failed, send the following message to the specified object. The `didCommitSelector` method must have the following method signature:

```objc
- (void)editor:(id)editor didCommit:(BOOL)didCommit contextInfo:(void *)contextInfo
```

If an error occurs while attempting to commit, for example if key-value coding validation fails, an implementation of this method should typically send the NSView in which editing is being done a `presentError:modalForWindow:delegate:didRecoverSelector:contextInfo:` message, specifying the view’s containing window.
