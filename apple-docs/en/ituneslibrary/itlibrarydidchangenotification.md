---
title: ITLibraryDidChangeNotification
framework: iTunes Library
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 14.0+, macOS 13.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/ituneslibrary/itlibrarydidchangenotification
source_url: 'https://developer.apple.com/documentation/ituneslibrary/itlibrarydidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/ituneslibrary/itlibrarydidchangenotification.json'
content_hash: 'sha256:23b884f0d12dc50a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [iTunes Library](../ituneslibrary.md)

# ITLibraryDidChangeNotification

<sub>Global Variable</sub>

This notification is sent to NSDistributedNotificationCenter when a change has occurred in the library.

<sub>macOS</sub>

```objc
extern NSNotificationName const ITLibraryDidChangeNotification;
```

## Overview

The client should call [- reloadData](<itlibrary/reloaddata().md>) if it wants a new view of the library contents.

> [!note] Note
> This is not a fine-grained notification.  This API does not support per-object change notifications.
