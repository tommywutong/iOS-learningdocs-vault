---
title: 'setObject:forKeyedSubscript:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiconfigurationstate-1smq1/setobject:forkeyedsubscript:'
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationstate-1smq1/setobject:forkeyedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationstate-1smq1/setobject%3Aforkeyedsubscript%3A.json'
content_hash: 'sha256:f1179f85e1d0746c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationState](../uiconfigurationstate-1smq1.md)

# setObject:forKeyedSubscript:

<sub>Instance Method</sub>

Sets the object for the specified custom state key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) setObject:(id) obj forKeyedSubscript:(UIConfigurationStateCustomKey) key;
```

## See Also

### Managing configuration states

- [traitCollection](traitcollection.md) — The traits that describe the current layout environment of the view, such as the user interface style and layout direction.
- [customStateForKey:](customstateforkey_.md) — Retrieves the custom state for the specified custom state key.
- [setCustomState:forKey:](setcustomstate_forkey_.md) — Sets the custom state for the specified custom state key.
- [objectForKeyedSubscript:](objectforkeyedsubscript_.md) — Retrieves the object for the specified custom state key.
