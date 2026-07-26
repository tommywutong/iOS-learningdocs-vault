---
title: 'init(nibName:bundle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uinib/init(nibname:bundle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinib/init(nibname:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinib/init%28nibname%3Abundle%3A%29.json'
content_hash: 'sha256:0e5a0855a79935f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINib](../uinib.md)

# init(nibName:bundle:)

<sub>Initializer</sub>

Returns a nib object from the nib file in the specified bundle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(nibName name: String, bundle bundleOrNil: Bundle?)
```

## Parameters

- `name` — The name of the nib file, without any leading path information.

- `bundleOrNil` — The bundle in which to search for the nib file. If you specify `nil`, this method looks for the nib file in the main bundle.

## Return Value

The initialized [UINib](../uinib.md) object. An exception is thrown if there were errors during initialization or the nib file could not be located.

## Discussion

The [UINib](../uinib.md) object looks for the nib file in the bundle’s language-specific project directories first, followed by the `Resources` directory.

## See Also

### Creating a nib object

- [+ nibWithData:bundle:](<init(data_bundle_).md>) — Creates a nib object from nib data stored in memory.
