---
title: 'Kreya 1.12 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.12-whats-new/'
original_language: en
published: 2023-11-06
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:725b9e72852ebffd'
translated: false
---

> 原文：[Kreya 1.12 - What's New | Kreya](https://kreya.app/blog/kreya-1.12-whats-new/)　·　Kreya Blog

Kreya 1.12 has been released! This new version comes with a lot of new features and some bug fixes. Starting with a new dialog for unimported operations that is visible after an import run. If you ever wanted to see how long a request takes on the wire and server side, this is now possible with the new Timing tab. And for REST, we now support server-sent events.

### Unimported operations dialog

Sometimes an operation is no longer imported (e.g. a method was removed from the gRPC API) and can be deleted. After the importers are run a warning is shown if unimported operations exist in the project. With the dialog you can delete the operations or ignore the warning.

Proto definition before change:

```text
service Greeter {  rpc SayHello (HelloRequest) returns (HelloReply);  rpc SayBye (ByeRequest) returns (ByeReply);}
```

Proto definition after change:

```text
service Greeter {  rpc SayHello (HelloRequest) returns (HelloReply);}
```

![An animation showcasing opening the unimported dialog](https://kreya.app/whats-new/1.12/unimported_dialog.gif)

### Operation and server timing [Pro / Enterprise](https://kreya.app/pricing/)

You may be familiar with some timing diagrams from your browser's development tools. Timing details from requests are now also visible in Kreya, just select the Timing tab to view these details.

The tab is divided into two parts. In the first part you can see the general timing with DNS resolution and so on. And below you will see the details of the server timing, if you had configured it on your server.

### Server-sent events

Kreya now supports server-sent events, allowing a server to stream events to Kreya. Server-sent events work almost like websockets on the client side, but you can't send events from the client to the server. More information about [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

![An animation showcasing streaming REST events](https://kreya.app/whats-new/1.12/rest_streamed_events.gif)

### Operation list improvements

The operations list now allows you to copy and paste operations and directories directly using keyboard shortcuts. The following keyboard shortcuts are now supported:

| Shortcut | Windows / Linux | MacOS |
|---|---|---|
| Copy | Ctrl + C | ⌘ + C |
| Paste | Ctrl + V | ⌘ + V |
| Cut | Ctrl + X | ⌘ + X |
| Delete | Delete | ⌦ (Delete right) |
| Delete without confirmation | ⇧ + Delete | ⌘ + ⌫ (Delete left) |
| Create new directory | Ctrl + ⇧ + N | ⌘ + ⇧ + N |
| Navigate | ← → ↑ ↓ | ← → ↑ ↓ |
| Open | ⏎ | ⏎ |

![An animation showcasing the shortcuts in the operation list](https://kreya.app/whats-new/1.12/operation_list_shortcuts.gif)

### Ignore inherited properties

Inherited metadata, headers and query parameters can now be ignored and overwritten.

![An animation showcasing overwriting inherited entries](https://kreya.app/whats-new/1.12/overwrite_inherited_entries.gif)

### Specify the HTTP version for REST operations

In Kreya it's possible to specify the HTTP version for a REST operation. This can be done in the Settings tab. Kreya has support for HTTP/1.1, HTTP/2 and HTTP/3.

![An animation showcasing specifing the http version](https://kreya.app/whats-new/1.12/specify_http_version.gif)

### Bug fixes

Many bugs have been fixed. Most of them are UI bugs such as aligment of icons and buttons. All details on this release can be found on our [release notes](https://kreya.app/docs/release-notes/) page.

If you find a bug, please do not hesitate to [report](https://github.com/riok/Kreya/issues/new/choose) it. You can contact us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#4b232e2727240b20392e322a652a3b3b) for any further information or feedback.

See you soon 👋
