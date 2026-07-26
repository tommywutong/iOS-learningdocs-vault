---
title: dontAnnotate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/sendoptions/dontannotate
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendoptions/dontannotate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/sendoptions/dontannotate.json'
content_hash: 'sha256:1dd01c6fef2a9d98'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAppleEventDescriptor](../../nsappleeventdescriptor.md) · [SendOptions](../sendoptions.md)

# dontAnnotate

<sub>Type Property</sub>

Don’t automatically add any sandbox or other annotations to the event.

<sub>macOS</sub>

```swift
static var dontAnnotate: NSAppleEventDescriptor.SendOptions { get }
```

## See Also

### Constants

- [NSAppleEventSendAlwaysInteract](alwaysinteract.md) — Server should always interact with user where appropriate.
- [NSAppleEventSendCanInteract](caninteract.md) — Server may try to interact with user.
- [NSAppleEventSendCanSwitchLayer](canswitchlayer.md) — Interaction may switch layer.
- [NSAppleEventSendDefaultOptions](defaultoptions.md) — The default options: wait for reply and allow interaction.
- [NSAppleEventSendDontExecute](dontexecute.md) — Don’t execute this event; used for recording.
- [NSAppleEventSendDontRecord](dontrecord.md) — Don’t record this event.
- [NSAppleEventSendNeverInteract](neverinteract.md) — Server should not interact with user.
- [NSAppleEventSendNoReply](noreply.md) — Sender doesn’t want a reply to event.
- [NSAppleEventSendQueueReply](queuereply.md) — Sender wants a reply but won’t wait.
- [NSAppleEventSendWaitForReply](waitforreply.md) — Sender wants a reply and will wait.
