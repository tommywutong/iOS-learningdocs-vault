---
title: SKRequestDelegate
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skrequestdelegate
source_url: 'https://developer.apple.com/documentation/storekit/skrequestdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skrequestdelegate.json'
content_hash: 'sha256:904be891bf2b260b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKRequestDelegate

<sub>Protocol</sub>

Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SKRequestDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [SKProductsRequestDelegate](skproductsrequestdelegate.md)

## Topics

### Completing Requests

- [- requestDidFinish:](<skrequestdelegate/requestdidfinish(__).md>) — Tells the delegate that the request has completed. _(deprecated)_

### Handling Errors

- [- request:didFailWithError:](<skrequestdelegate/request(__didfailwitherror_).md>) — Tells the delegate that the request failed to execute. _(deprecated)_

## See Also

### Accessing the Delegate

- [delegate](skrequest/delegate.md) — The delegate of the request object. _(deprecated)_
