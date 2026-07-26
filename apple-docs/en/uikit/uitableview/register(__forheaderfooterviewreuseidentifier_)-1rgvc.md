---
title: 'register(_:forHeaderFooterViewReuseIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitableview/register(_:forheaderfooterviewreuseidentifier:)-1rgvc'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/register(_:forheaderfooterviewreuseidentifier:)-1rgvc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/register%28_%3Aforheaderfooterviewreuseidentifier%3A%29-1rgvc.json'
content_hash: 'sha256:c8c6e5f40590cea2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# register(_:forHeaderFooterViewReuseIdentifier:)

<sub>Instance Method</sub>

Registers a nib object that contains a header or footer with the table view under a specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ nib: UINib?, forHeaderFooterViewReuseIdentifier identifier: String)
```

## Parameters

- `nib` — A nib object that specifies the nib file to use to create the header or footer view. This parameter can’t be `nil`.

- `identifier` — The reuse identifier for the header or footer view. This parameter must not be `nil` and must not be an empty string.

## Discussion

Before dequeueing any header or footer views, call this method or the [- registerClass:forHeaderFooterViewReuseIdentifier:](<register(__forheaderfooterviewreuseidentifier_)-20ybb.md>) method to tell the table view how to create new instances of your views. If a view of the specified type isn’t currently in a reuse queue, the table view uses the provided information to create a new one automatically.

If you previously registered a class or nib file with the same reuse identifier, the nib you specify in the `nib` parameter replaces the old entry. You may specify `nil` for `nib` if you want to unregister the nib from the specified reuse identifier.

## See Also

### Recycling section headers and footers

- [- registerClass:forHeaderFooterViewReuseIdentifier:](<register(__forheaderfooterviewreuseidentifier_)-20ybb.md>) — Registers a class to use in creating new table header or footer views.
- [- dequeueReusableHeaderFooterViewWithIdentifier:](<dequeuereusableheaderfooterview(withidentifier_).md>) — Returns a reusable header or footer view after locating it by its identifier.
