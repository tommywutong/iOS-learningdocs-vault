---
title: 'init(reuseIdentifier:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewheaderfooterview/init(reuseidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/init(reuseidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/init%28reuseidentifier%3A%29.json'
content_hash: 'sha256:b54aa0c69e5b15ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# init(reuseIdentifier:)

<sub>Initializer</sub>

Initializes a header-footer view with the specified reuse identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(reuseIdentifier: String?)
```

## Parameters

- `reuseIdentifier` — A string used to identify the header or footer view if it’s to be reused by multiple sections. Pass `nil` if the view isn’t to be reused. You should use the same reuse identifier for all header or footer views of the same form.

## Return Value

An initialized [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md) object or `nil` if the object could not be created.

## Discussion

Once set, you can’t change the reuse identifier for the returned view object.

## See Also

### Creating the view

- [- initWithCoder:](<init(coder_).md>) — Creates a header-footer view from data in an unarchiver.
