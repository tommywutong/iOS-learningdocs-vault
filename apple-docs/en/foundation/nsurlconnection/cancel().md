---
title: cancel()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlconnection/cancel()
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/cancel%28%29.json'
content_hash: 'sha256:09b4e59ad2fa2b15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# cancel()

<sub>Instance Method</sub>

Cancels an asynchronous load of a request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

After this method is called, the connection makes no further delegate method calls. If you want to reattempt the connection, you should create a new connection object.

## See Also

### Related Documentation

- [- initWithRequest:delegate:](<init(request_delegate_).md>) — Returns an initialized URL connection and begins to load the data for the URL request. _(deprecated)_
