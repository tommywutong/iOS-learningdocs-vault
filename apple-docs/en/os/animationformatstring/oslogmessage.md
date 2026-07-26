---
title: AnimationFormatString.OSLogMessage
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/animationformatstring/oslogmessage
source_url: 'https://developer.apple.com/documentation/os/animationformatstring/oslogmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/animationformatstring/oslogmessage.json'
content_hash: 'sha256:85ea5ebd9836cbe6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [AnimationFormatString](../animationformatstring.md)

# AnimationFormatString.OSLogMessage

<sub>Structure</sub>

A log message that includes an animation tag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogMessage
```

## Overview

An [OSLogMessage](oslogmessage.md) structure contains a message that you construct from a string interpolation or string literal. This message includes an additional animation tag. Don’t create this structure directly. The system creates one automatically when you log a message using the [os_signpost(_:dso:log:name:signpostID:_:_:)](<../os_signpost(__dso_log_name_signpostid_____)-nez5.md>) function

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md)

## Topics

### Creating a Format String

- [init(stringLiteral:)](<oslogmessage/init(stringliteral_).md>) — Creates a log message using a string literal.
