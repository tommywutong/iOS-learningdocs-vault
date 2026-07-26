---
title: 'panel:isValidFilename:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/panel:isvalidfilename:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:isvalidfilename:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/panel%3Aisvalidfilename%3A.json'
content_hash: 'sha256:eaf2ce3f5a1bf498'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# panel:isValidFilename:

<sub>Instance Method</sub>

Gives the delegate the opportunity to validate selected items.

> [!warning] Deprecated
> Use [panel(_:validate:)](<../../appkit/nsopensavepaneldelegate/panel(__validate_).md>) ([NSOpenSavePanelDelegate](../../appkit/nsopensavepaneldelegate.md)) instead. If both methods are implemented, the URL version will be called.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) panel:(id) sender isValidFilename:(NSString *) filename;
```

## Parameters

- `sender` — Panel requesting filename validation.

- `filename` — String representing the filename to validate.

## Return Value

[YES](../yes.md) if the filename is valid, or [NO](../no.md) if the save panel should stay in its modal loop and wait for the user to type in or select a different filename or names.

## Discussion

The `NSSavePanel` object `sender` sends this message just before the end of a modal session for each filename displayed or selected (including filenames in multiple selections). If the delegate refuses a filename in a multiple selection, none of the filenames in the selection is accepted.

## See Also

### Related Documentation

- [panel(_:validate:)](<../../appkit/nsopensavepaneldelegate/panel(__validate_).md>) — Asks the delegate to validate the URL for a file that the user selected.
