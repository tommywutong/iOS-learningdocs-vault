---
title: delegate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skrequest/delegate
source_url: 'https://developer.apple.com/documentation/storekit/skrequest/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skrequest/delegate.json'
content_hash: 'sha256:e4e1144cf5c7f213'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKRequest](../skrequest.md)

# delegate

<sub>Instance Property</sub>

The delegate of the request object.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any SKRequestDelegate)? { get set }
```

## Discussion

The delegate must adopt the [SKRequestDelegate](../skrequestdelegate.md) protocol, although most subclasses of [SKRequest](../skrequest.md) provide a more specific protocol to implement.

## See Also

### Accessing the Delegate

- [SKRequestDelegate](../skrequestdelegate.md) — Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class. _(deprecated)_
