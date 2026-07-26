---
title: 'authenticationDataForComponents:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnectiondelegate/authenticationdataforcomponents:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondelegate/authenticationdataforcomponents:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondelegate/authenticationdataforcomponents%3A.json'
content_hash: 'sha256:cdcded43e356b91c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnectionDelegate](../nsconnectiondelegate.md)

# authenticationDataForComponents:

<sub>Instance Method</sub>

Returns an `NSData` object to be used as an authentication stamp for an outgoing message.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSData *) authenticationDataForComponents:(NSArray *) components;
```

## Parameters

- `components` — An array containing the elements of a network message, in the form of `NSPort` and `NSData` objects.

## Return Value

An `NSData` object to be used as an authentication stamp for an outgoing message.

## Discussion

The delegate should use only the `NSData` elements to create the authentication stamp. See the [PortMessage](../portmessage.md) class specification for more information on the components.

If [authenticationDataForComponents:](authenticationdataforcomponents_.md) returns `nil`, an `NSGenericException` will be raised. If the delegate determines that the message shouldn’t be authenticated, it should return an empty `NSData` object. The delegate on the other side of the connection must then be prepared to accept an empty `NSData` object as the second parameter to [authenticateComponents:withData:](authenticatecomponents_withdata_.md) and to handle the situation appropriately.

The `components` parameter will be validated on receipt by the delegate of the peer `NSConnection` object with [authenticateComponents:withData:](authenticatecomponents_withdata_.md).

## See Also

### Authenticating

- [authenticateComponents:withData:](authenticatecomponents_withdata_.md) — Returns a Boolean value that indicates whether given authentication data is valid for a given set of components. _(deprecated)_
