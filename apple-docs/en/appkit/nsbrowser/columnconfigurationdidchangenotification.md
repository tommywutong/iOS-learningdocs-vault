---
title: columnConfigurationDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsbrowser/columnconfigurationdidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsbrowser/columnconfigurationdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsbrowser/columnconfigurationdidchangenotification.json'
content_hash: 'sha256:7238b5f8d194677f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSBrowser](../nsbrowser.md)

# columnConfigurationDidChangeNotification

<sub>Type Property</sub>

Notifies the delegate when the width of a browser column has changed.

<sub>macOS</sub>

```swift
class let columnConfigurationDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is the browser whose column sizes need to be made persistent. This notification does not contain a `userInfo` dictionary. If the user resizes more than one column, a single notification is posted when the user is finished resizing.

## See Also

### Related Documentation

- [- browserColumnConfigurationDidChange:](<../nsbrowserdelegate/browsercolumnconfigurationdidchange(__).md>) — Used by clients to implement their own column width persistence.
