---
title: noReply
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/sendoptions/noreply
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendoptions/noreply'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/sendoptions/noreply.json'
content_hash: 'sha256:fb4ec60e31911f2c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAppleEventDescriptor](../../nsappleeventdescriptor.md) · [SendOptions](../sendoptions.md)

# noReply

<sub>Type Property</sub>

Sender doesn’t want a reply to event.

<sub>macOS</sub>

```swift
static var noReply: NSAppleEventDescriptor.SendOptions { get }
```

## See Also

### Constants

- [NSAppleEventSendAlwaysInteract](alwaysinteract.md) — Server should always interact with user where appropriate.
- [NSAppleEventSendCanInteract](caninteract.md) — Server may try to interact with user.
- [NSAppleEventSendCanSwitchLayer](canswitchlayer.md) — Interaction may switch layer.
- [NSAppleEventSendDefaultOptions](defaultoptions.md) — The default options: wait for reply and allow interaction.
- [NSAppleEventSendDontAnnotate](dontannotate.md) — Don’t automatically add any sandbox or other annotations to the event.
- [NSAppleEventSendDontExecute](dontexecute.md) — Don’t execute this event; used for recording.
- [NSAppleEventSendDontRecord](dontrecord.md) — Don’t record this event.
- [NSAppleEventSendNeverInteract](neverinteract.md) — Server should not interact with user.
- [NSAppleEventSendQueueReply](queuereply.md) — Sender wants a reply but won’t wait.
- [NSAppleEventSendWaitForReply](waitforreply.md) — Sender wants a reply and will wait.
