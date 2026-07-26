---
title: 'panel:directoryDidChange:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/panel:directorydidchange:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:directorydidchange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/panel%3Adirectorydidchange%3A.json'
content_hash: 'sha256:7ef4626afcdc36f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# panel:directoryDidChange:

<sub>Instance Method</sub>

Tells the delegate that the user has changed the selected directory in the `NSSavePanel` object specified.

> [!warning] Deprecated
> Use [panel(_:didChangeToDirectoryURL:)](<../../appkit/nsopensavepaneldelegate/panel(__didchangetodirectoryurl_).md>) ([NSOpenSavePanelDelegate](../../appkit/nsopensavepaneldelegate.md)) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) panel:(id) sender directoryDidChange:(NSString *) path;
```

## Parameters

- `sender` — Panel whose directory has changed.

- `path` — String representing the new directory’s path.

## See Also

### Related Documentation

- [panel(_:didChangeToDirectoryURL:)](<../../appkit/nsopensavepaneldelegate/panel(__didchangetodirectoryurl_).md>) — Tells the delegate that the user changed the selected directory to the directory located at the specified URL.
