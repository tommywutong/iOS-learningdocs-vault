---
title: NSAppleEventDescriptor.SendOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/sendoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/sendoptions.json'
content_hash: 'sha256:e953b3bb1fcd6776'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# NSAppleEventDescriptor.SendOptions

<sub>Structure</sub>

<sub>macOS</sub>

```swift
struct SendOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSAppleEventSendAlwaysInteract](sendoptions/alwaysinteract.md) — Server should always interact with user where appropriate.
- [NSAppleEventSendCanInteract](sendoptions/caninteract.md) — Server may try to interact with user.
- [NSAppleEventSendCanSwitchLayer](sendoptions/canswitchlayer.md) — Interaction may switch layer.
- [NSAppleEventSendDefaultOptions](sendoptions/defaultoptions.md) — The default options: wait for reply and allow interaction.
- [NSAppleEventSendDontAnnotate](sendoptions/dontannotate.md) — Don’t automatically add any sandbox or other annotations to the event.
- [NSAppleEventSendDontExecute](sendoptions/dontexecute.md) — Don’t execute this event; used for recording.
- [NSAppleEventSendDontRecord](sendoptions/dontrecord.md) — Don’t record this event.
- [NSAppleEventSendNeverInteract](sendoptions/neverinteract.md) — Server should not interact with user.
- [NSAppleEventSendNoReply](sendoptions/noreply.md) — Sender doesn’t want a reply to event.
- [NSAppleEventSendQueueReply](sendoptions/queuereply.md) — Sender wants a reply but won’t wait.
- [NSAppleEventSendWaitForReply](sendoptions/waitforreply.md) — Sender wants a reply and will wait.

### Initializers

- [init(rawValue:)](<sendoptions/init(rawvalue_).md>)
