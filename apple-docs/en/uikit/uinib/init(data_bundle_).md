---
title: 'init(data:bundle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uinib/init(data:bundle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinib/init(data:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinib/init%28data%3Abundle%3A%29.json'
content_hash: 'sha256:6db5cf65180c8e14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINib](../uinib.md)

# init(data:bundle:)

<sub>Initializer</sub>

Creates a nib object from nib data stored in memory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(data: Data, bundle bundleOrNil: Bundle?)
```

## Parameters

- `data` — A block of memory that contains nib data.

- `bundleOrNil` — The bundle in which to search for resources referenced by the nib. If you specify `nil`, this method looks for the nib file in the main bundle.

## Return Value

The initialized [UINib](../uinib.md) object. An exception is thrown if there were errors during initialization or the nib data could not be located.

## Discussion

The [UINib](../uinib.md) object looks for the nib file in the bundle’s language-specific project directories first, followed by the `Resources` directory.

The preferred mechanism for instantiating [UINib](../uinib.md) objects is with [+ nibWithNibName:bundle:](<init(nibname_bundle_).md>). A [UINib](../uinib.md) object instantiated using [+ nibWithData:bundle:](<init(data_bundle_).md>) can’t release the cached data under low memory conditions. Your app should prepare to release the [UINib](../uinib.md) object and the data under low memory conditions, recreating both the next time the app needs to instantiate the nib.

## See Also

### Creating a nib object

- [+ nibWithNibName:bundle:](<init(nibname_bundle_).md>) — Returns a nib object from the nib file in the specified bundle.
