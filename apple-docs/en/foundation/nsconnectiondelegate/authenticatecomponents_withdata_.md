---
title: 'authenticateComponents:withData:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnectiondelegate/authenticatecomponents:withdata:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondelegate/authenticatecomponents:withdata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondelegate/authenticatecomponents%3Awithdata%3A.json'
content_hash: 'sha256:d4c24ac9556a7929'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnectionDelegate](../nsconnectiondelegate.md)

# authenticateComponents:withData:

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether given authentication data is valid for a given set of components.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) authenticateComponents:(NSArray *) components withData:(NSData *) signature;
```

## Parameters

- `components` — An array that contains `NSData` and `NSPort` objects belonging to an `NSPortMessage` object. See the [PortMessage](../portmessage.md) class specification for more information.

- `signature` — Authentication data created by the delegate of the peer `NSConnection` object with [authenticationDataForComponents:](authenticationdataforcomponents_.md).

## Return Value

[true](../../swift/true.md) if the `signature` provided is valid for `components`, otherwise [false](../../swift/false.md).

## Discussion

Use this message for validation of incoming messages. An `NSConnection` object raises an `NSFailedAuthenticationException` on receipt of a remote message the delegate doesn’t authenticate.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)

### Authenticating

- [authenticationDataForComponents:](authenticationdataforcomponents_.md) — Returns an `NSData` object to be used as an authentication stamp for an outgoing message. _(deprecated)_
