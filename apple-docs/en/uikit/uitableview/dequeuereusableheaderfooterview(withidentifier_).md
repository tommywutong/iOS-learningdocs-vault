---
title: 'dequeueReusableHeaderFooterView(withIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/dequeuereusableheaderfooterview(withidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/dequeuereusableheaderfooterview(withidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/dequeuereusableheaderfooterview%28withidentifier%3A%29.json'
content_hash: 'sha256:c32aeab2f6be1afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# dequeueReusableHeaderFooterView(withIdentifier:)

<sub>Instance Method</sub>

Returns a reusable header or footer view after locating it by its identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dequeueReusableHeaderFooterView(withIdentifier identifier: String) -> UITableViewHeaderFooterView?
```

## Parameters

- `identifier` — A string identifying the header or footer view to be reused. This parameter must not be `nil`.

## Return Value

A [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md) object with the associated identifier or `nil` if no such object exists in the reusable view queue.

## Discussion

For performance reasons, a table view’s delegate should generally reuse [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md) objects when it’s asked to provide them. A table view maintains a queue or list of [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md) objects that the table view’s delegate has marked for reuse. It marks a view for reuse by assigning it a reuse identifier when it creates it (in the [- initWithReuseIdentifier:](<../uitableviewheaderfooterview/init(reuseidentifier_).md>) method of [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)).

You can use this method to access specific template header and footer views that you previously created. You can access a view’s reuse identifier through its [reuseIdentifier](../uitableviewheaderfooterview/reuseidentifier.md) property.

## See Also

### Recycling section headers and footers

- [- registerNib:forHeaderFooterViewReuseIdentifier:](<register(__forheaderfooterviewreuseidentifier_)-1rgvc.md>) — Registers a nib object that contains a header or footer with the table view under a specified identifier.
- [- registerClass:forHeaderFooterViewReuseIdentifier:](<register(__forheaderfooterviewreuseidentifier_)-20ybb.md>) — Registers a class to use in creating new table header or footer views.
