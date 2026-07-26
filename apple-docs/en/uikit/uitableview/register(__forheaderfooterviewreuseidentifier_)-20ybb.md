---
title: 'register(_:forHeaderFooterViewReuseIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/register%28_%3Aforheaderfooterviewreuseidentifier%3A%29-20ybb.json'
content_hash: 'sha256:3f4a9722d774c97c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# register(_:forHeaderFooterViewReuseIdentifier:)

<sub>Instance Method</sub>

Registers a class to use in creating new table header or footer views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ aClass: AnyClass?, forHeaderFooterViewReuseIdentifier identifier: String)
```

## Parameters

- `aClass` — The class of the header or footer view that you want to register. You must specify either [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md) or a subclass of it.

- `identifier` — The reuse identifier for the header or footer view. This parameter must not be `nil` and must not be an empty string.

## Discussion

Before dequeueing any header or footer views, call this method or the [- registerNib:forHeaderFooterViewReuseIdentifier:](<register(__forheaderfooterviewreuseidentifier_)-1rgvc.md>) method to tell the table view how to create new instances of your views. If a view of the specified type isn’t currently in a reuse queue, the table view uses the provided information to create a one automatically.

If you previously registered a class or nib file with the same reuse identifier, the class you specify in the `aClass` parameter replaces the old entry. You may specify `nil` for `aClass` if you want to unregister the class from the specified reuse identifier.

## See Also

### Recycling section headers and footers

- [- registerNib:forHeaderFooterViewReuseIdentifier:](<register(__forheaderfooterviewreuseidentifier_)-1rgvc.md>) — Registers a nib object that contains a header or footer with the table view under a specified identifier.
- [- dequeueReusableHeaderFooterViewWithIdentifier:](<dequeuereusableheaderfooterview(withidentifier_).md>) — Returns a reusable header or footer view after locating it by its identifier.
