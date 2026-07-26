---
title: AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes/announcementpriorityattribute/announcementpriority
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/announcementpriorityattribute/announcementpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes/announcementpriorityattribute/announcementpriority.json'
content_hash: 'sha256:5a64b63c44b0a357'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [AttributeScopes](../../../attributescopes.md) · [AccessibilityAttributes](../../accessibilityattributes.md) · [AnnouncementPriorityAttribute](../announcementpriorityattribute.md)

# AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority

<sub>Enumeration</sub>

A priority level used by accessibility clients, such as VoiceOver, to control how announcements are queued and presented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AnnouncementPriority
```

## Relationships

- **Conforms To**: [Copyable](../../../../swift/copyable.md), [Decodable](../../../../swift/decodable.md), [Encodable](../../../../swift/encodable.md), [Equatable](../../../../swift/equatable.md), [Escapable](../../../../swift/escapable.md), [Hashable](../../../../swift/hashable.md), [RawRepresentable](../../../../swift/rawrepresentable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.default](announcementpriority/default.md) — Announcements will interrupt existing speech, but are interruptible if a new speech utterance is started.
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.high](announcementpriority/high.md) — Announcements will interrupt other speech and cannot be interrupted once started.
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute.AnnouncementPriority.low](announcementpriority/low.md) — Announcements are queued and spoken when other speech utterances have completed.
