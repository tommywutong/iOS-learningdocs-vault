---
title: connection
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.7 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsportcoder/connection
source_url: 'https://developer.apple.com/documentation/foundation/nsportcoder/connection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportcoder/connection.json'
content_hash: 'sha256:225df95f8fc99e70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortCoder](../nsportcoder.md)

# connection

<sub>Instance Method</sub>

Returns the `NSConnection` object that uses the receiver.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSConnection *) connection;
```

## Return Value

The `NSConnection` object that uses the receiver. In an object’s [- encodeWithCoder:](<../nscoding/encode(with_).md>) method, this is the sending (server) connection. In [- initWithCoder:](<../nscoding/init(coder_).md>) this is the receiving (client) connection.
