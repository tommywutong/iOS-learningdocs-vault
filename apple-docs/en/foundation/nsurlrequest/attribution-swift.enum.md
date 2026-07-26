---
title: NSURLRequest.Attribution
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/attribution-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/attribution-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/attribution-swift.enum.json'
content_hash: 'sha256:01e6e469f94ff198'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# NSURLRequest.Attribution

<sub>Enumeration</sub>

The entities that can make a network request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Attribution
```

## Overview

Use one of these values when setting the [attribution](../urlrequest/attribution-swift.property.md) parameter of a [URLRequest](../urlrequest.md). If you don’t set a value, the system assumes [NSURLRequestAttributionDeveloper](attribution-swift.enum/developer.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Request sources

- [NSURLRequestAttributionDeveloper](attribution-swift.enum/developer.md) — A developer-initiated network request.
- [NSURLRequestAttributionUser](attribution-swift.enum/user.md) — The user explicitly directs the app to make a network request.

### Initializers

- [init(rawValue:)](<attribution-swift.enum/init(rawvalue_).md>)

## See Also

### Indicating the source of the request

- [attribution](../nsmutableurlrequest/attribution.md) — The entity that initiates the network request.
