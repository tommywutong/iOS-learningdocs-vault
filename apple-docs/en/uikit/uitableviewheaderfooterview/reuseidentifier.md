---
title: reuseIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/reuseidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/reuseidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/reuseidentifier.json'
content_hash: 'sha256:62b780deccbc4e7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# reuseIdentifier

<sub>Instance Property</sub>

A string used to identify a reusable header or footer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var reuseIdentifier: String? { get }
```

## Discussion

You assign a reuse identifier to a header or footer view at creation time. Once assigned, the table view uses that reuse identifier to gather your views when they’re scrolled offscreen and queue them for later reuse. You can retrieve header or footer views by passing the same reuse identifier to the [- dequeueReusableHeaderFooterViewWithIdentifier:](<../uitableview/dequeuereusableheaderfooterview(withidentifier_).md>) method of the table view.

## See Also

### Managing view reuse

- [- prepareForReuse](<prepareforreuse().md>) — Prepares a reusable header or footer view for reuse by the table.
