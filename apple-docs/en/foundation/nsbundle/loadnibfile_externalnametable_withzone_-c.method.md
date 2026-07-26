---
title: 'loadNibFile:externalNameTable:withZone:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsbundle/loadnibfile:externalnametable:withzone:-c.method'
source_url: 'https://developer.apple.com/documentation/foundation/nsbundle/loadnibfile:externalnametable:withzone:-c.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundle/loadnibfile%3Aexternalnametable%3Awithzone%3A-c.method.json'
content_hash: 'sha256:50f480ddd699b0c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# loadNibFile:externalNameTable:withZone:

<sub>Instance Method</sub>

Unarchives the contents of a nib file located in the receiver’s bundle.

> [!warning] Deprecated
> Use the [- loadNibNamed:owner:topLevelObjects:](<../bundle/loadnibnamed(__owner_toplevelobjects_).md>) method instead.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) loadNibFile:(NSString *) fileName externalNameTable:(NSDictionary *) context withZone:(NSZone *) zone;
```

## Parameters

- `fileName` — The name of the nib file, which need not include the `.nib` extension.

- `context` — A name table whose keys identify objects associated with your program or the nib file. The newly unarchived objects from the nib file use this table to connect to objects in your program. For example,  the nib file uses the object associated with the `NSNibOwner` constant as the nib file’s owning object. If you associate an empty `NSMutableArray` object with the `NSNibTopLevelObjects` constant, on output, the array contains the top level objects from the nib file. For descriptions of these constants, see [NSNib](../../appkit/nsnib.md).

- `zone` — The memory zone in which to allocate the nib file objects.

## Return Value

[true](../../swift/true.md) if the nib file was loaded successfully; otherwise, [false](../../swift/false.md).

## Discussion

This method searches the language-specific project (`.lproj`) directories for the specified nib file. If the file is not there, it searches the bundle’s `Resources` directory for a non-localized version of the file.

## See Also

### Loading nib files

- [- loadNibNamed:owner:options:](<../bundle/loadnibnamed(__owner_options_).md>) — Unarchives the contents of a nib file located in the receiver’s bundle.
- [- loadNibNamed:owner:topLevelObjects:](<../bundle/loadnibnamed(__owner_toplevelobjects_).md>) — Loads a nib from the bundle with the specified file name and owner.
- [loadNibNamed:owner:](loadnibnamed_owner_.md) — Unarchives the contents of the nib file and links them to a specific owner object. _(deprecated)_
- [loadNibFile:externalNameTable:withZone:](loadnibfile_externalnametable_withzone_-c.type.method.md) — Unarchives the contents of the nib file and links them to objects in your program. _(deprecated)_
