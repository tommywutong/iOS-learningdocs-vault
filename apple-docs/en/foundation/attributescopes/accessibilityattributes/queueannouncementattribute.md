---
title: AttributeScopes.AccessibilityAttributes.QueueAnnouncementAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes/queueannouncementattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/queueannouncementattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes/queueannouncementattribute.json'
content_hash: 'sha256:863a741eba7ced84'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [AccessibilityAttributes](../accessibilityattributes.md)

# AttributeScopes.AccessibilityAttributes.QueueAnnouncementAttribute

<sub>Enumeration</sub>

An attribute to define if speech announcements spoken by VoiceOver should be queued behind existing speech rather than interrupting speech in progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum QueueAnnouncementAttribute
```

## Overview

When `true`, the announcement will be queued behind existing speech. When `false`, it will interrupt existing speech. By default, announcements interrupt existing speech.

> [!note] Note
> This attribute is not used on macOS

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)
