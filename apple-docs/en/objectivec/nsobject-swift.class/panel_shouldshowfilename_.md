---
title: 'panel:shouldShowFilename:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/panel:shouldshowfilename:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:shouldshowfilename:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/panel%3Ashouldshowfilename%3A.json'
content_hash: 'sha256:0cd1caeef68558f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# panel:shouldShowFilename:

<sub>Instance Method</sub>

Gives the delegate the opportunity to filter items that it doesn’t want the user to choose.

> [!warning] Deprecated
> Use [panel(_:shouldEnable:)](<../../appkit/nsopensavepaneldelegate/panel(__shouldenable_).md>) ([NSOpenSavePanelDelegate](../../appkit/nsopensavepaneldelegate.md)).

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) panel:(id) sender shouldShowFilename:(NSString *) filename;
```

## Parameters

- `sender` — Panel that is querying whether it should show a certain file.

- `filename` — String representing the name of the file to be loaded in the browser.

## Return Value

[YES](../yes.md) if `filename` should be selectable, and [NO](../no.md) if the save panel should disable the file or directory.

## Discussion

The `NSSavePanel` object `sender` sends this message to the panel’s delegate for each file or directory (filename) it is about to load in the browser.

## See Also

### Related Documentation

- [panel(_:shouldEnable:)](<../../appkit/nsopensavepaneldelegate/panel(__shouldenable_).md>) — Asks the delegate whether the specified URL should be enabled in the Open panel.
