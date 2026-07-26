---
title: 'loadNibNamed:owner:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsbundle/loadnibnamed:owner:'
source_url: 'https://developer.apple.com/documentation/foundation/nsbundle/loadnibnamed:owner:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundle/loadnibnamed%3Aowner%3A.json'
content_hash: 'sha256:af24564a445ac848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# loadNibNamed:owner:

<sub>Type Method</sub>

Unarchives the contents of the nib file and links them to a specific owner object.

> [!warning] Deprecated
> Use the [- loadNibNamed:owner:topLevelObjects:](<../bundle/loadnibnamed(__owner_toplevelobjects_).md>) method instead.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (BOOL) loadNibNamed:(NSString *) nibName owner:(id) owner;
```

## Parameters

- `nibName` — The name of the nib file, which need not include the `.nib` extension. The file name should not include path information. The object in the `owner` parameter determines the location in which to look for the nib file.

- `owner` — The object to assign as the nib File’s Owner. If the class of this object has an associated bundle, that bundle is searched for the specified nib file; otherwise, this method looks in the main bundle.

## Return Value

[true](../../swift/true.md) if the nib file was loaded successfully; otherwise, [false](../../swift/false.md).

## See Also

### Loading nib files

- [- loadNibNamed:owner:options:](<../bundle/loadnibnamed(__owner_options_).md>) — Unarchives the contents of a nib file located in the receiver’s bundle.
- [- loadNibNamed:owner:topLevelObjects:](<../bundle/loadnibnamed(__owner_toplevelobjects_).md>) — Loads a nib from the bundle with the specified file name and owner.
- [loadNibFile:externalNameTable:withZone:](loadnibfile_externalnametable_withzone_-c.type.method.md) — Unarchives the contents of the nib file and links them to objects in your program. _(deprecated)_
- [loadNibFile:externalNameTable:withZone:](loadnibfile_externalnametable_withzone_-c.method.md) — Unarchives the contents of a nib file located in the receiver’s bundle. _(deprecated)_
