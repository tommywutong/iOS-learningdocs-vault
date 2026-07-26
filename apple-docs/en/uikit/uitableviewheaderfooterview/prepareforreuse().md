---
title: prepareForReuse()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/prepareforreuse()
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/prepareforreuse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/prepareforreuse%28%29.json'
content_hash: 'sha256:5a1eeafa3a18b4ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# prepareForReuse()

<sub>Instance Method</sub>

Prepares a reusable header or footer view for reuse by the table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepareForReuse()
```

## Discussion

If your header or footer view is reusable — that is, it has a reuse identifier — the table view calls this method just before returning the view from its [- dequeueReusableHeaderFooterViewWithIdentifier:](<../uitableview/dequeuereusableheaderfooterview(withidentifier_).md>) method. Subclasses can override this method and use it to reset attributes of the view to their default values. For performance reasons, you should only reset attributes that aren’t related to content.

If the view doesn’t have a reuse identifier, this method is never called.

## See Also

### Managing view reuse

- [reuseIdentifier](reuseidentifier.md) — A string used to identify a reusable header or footer.
