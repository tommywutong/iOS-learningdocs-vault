---
title: CFStreamError
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreamerror
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamerror.json'
content_hash: 'sha256:d3f1fb7007ea35c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamError

<sub>Structure</sub>

The structure returned by [CFReadStreamGetError](<cfreadstreamgeterror(__).md>) and [CFWriteStreamGetError](<cfwritestreamgeterror(__).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFStreamError
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfstreamerror/init().md>)
- [init(domain:error:)](<cfstreamerror/init(domain_error_).md>)

### Instance Properties

- [domain](cfstreamerror/domain.md) — The error domain that should be used to interpret the error. See [CFStreamErrorDomain](cfstreamerrordomain.md) for possible values. _(deprecated)_
- [error](cfstreamerror/error.md) — The error code.

## See Also

### Data Types

- [CFStreamClientContext](cfstreamclientcontext.md) — A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.
