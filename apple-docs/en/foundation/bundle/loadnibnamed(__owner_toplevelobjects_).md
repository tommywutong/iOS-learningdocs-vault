---
title: 'loadNibNamed(_:owner:topLevelObjects:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/loadnibnamed(_:owner:toplevelobjects:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/loadnibnamed(_:owner:toplevelobjects:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/loadnibnamed%28_%3Aowner%3Atoplevelobjects%3A%29.json'
content_hash: 'sha256:e9f9eea47a7ff072'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# loadNibNamed(_:owner:topLevelObjects:)

<sub>Instance Method</sub>

Loads a nib from the bundle with the specified file name and owner.

<sub>macOS</sub>

```swift
func loadNibNamed(_ nibName: NSNib.Name, owner: Any?, topLevelObjects: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool
```

## Parameters

- `nibName` — The name of the nib.

- `owner` — The object that will be the nib’s owner.

- `topLevelObjects` — This by-reference parameter is populated with the top level objects of the nib.

## Return Value

[true](../../swift/true.md) if the nib file was loaded successfully; otherwise, [false](../../swift/false.md).

## Discussion

Unlike legacy methods, the objects adhere to the standard cocoa memory management rules; it is necessary to keep a strong reference to them by using IBOutlets or holding a reference to the array to prevent the nib contents from being deallocated.

Outlets to top-level objects should be strong references to demonstrate ownership and prevent deallocation.

For more information on Nibs, see [NSNib](../../appkit/nsnib.md).

## See Also

### Loading nib files

- [- loadNibNamed:owner:options:](<loadnibnamed(__owner_options_).md>) — Unarchives the contents of a nib file located in the receiver’s bundle.
