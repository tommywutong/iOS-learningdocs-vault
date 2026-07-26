---
title: canInteract
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/sendoptions/caninteract
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendoptions/caninteract'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/sendoptions/caninteract.json'
content_hash: 'sha256:62d02607b0c570d1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAppleEventDescriptor](../../nsappleeventdescriptor.md) · [SendOptions](../sendoptions.md)

# canInteract

<sub>Type Property</sub>

Server may try to interact with user.

<sub>macOS</sub>

```swift
static var canInteract: NSAppleEventDescriptor.SendOptions { get }
```

## See Also

### Constants

- [NSAppleEventSendAlwaysInteract](alwaysinteract.md) — Server should always interact with user where appropriate.
- [NSAppleEventSendCanSwitchLayer](canswitchlayer.md) — Interaction may switch layer.
- [NSAppleEventSendDefaultOptions](defaultoptions.md) — The default options: wait for reply and allow interaction.
- [NSAppleEventSendDontAnnotate](dontannotate.md) — Don’t automatically add any sandbox or other annotations to the event.
- [NSAppleEventSendDontExecute](dontexecute.md) — Don’t execute this event; used for recording.
- [NSAppleEventSendDontRecord](dontrecord.md) — Don’t record this event.
- [NSAppleEventSendNeverInteract](neverinteract.md) — Server should not interact with user.
- [NSAppleEventSendNoReply](noreply.md) — Sender doesn’t want a reply to event.
- [NSAppleEventSendQueueReply](queuereply.md) — Sender wants a reply but won’t wait.
- [NSAppleEventSendWaitForReply](waitforreply.md) — Sender wants a reply and will wait.
