---
title: AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes/announcementpriorityattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/announcementpriorityattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes/announcementpriorityattribute.json'
content_hash: 'sha256:5f1f54c5335de6aa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [AccessibilityAttributes](../accessibilityattributes.md)

# AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute

<sub>Enumeration</sub>

An attribute to define the urgency of the announcement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum AnnouncementPriorityAttribute
```

## Overview

For example, when `low` is specified, announcements are queued and spoken when other speech utterances have completed. When `default` is specified, announcements will interrupt existing speech, but are interruptible if a new speech utterance is started. When `high` is specified, announcements will interrupt other speech and cannot be interrupted once started.

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [ObjectiveCConvertibleAttributedStringKey](../../objectivecconvertibleattributedstringkey.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enumerations

- [AnnouncementPriority](announcementpriorityattribute/announcementpriority.md) — A priority level used by accessibility clients, such as VoiceOver, to control how announcements are queued and presented.
