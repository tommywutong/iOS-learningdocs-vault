---
title: 'Kreya 1.10 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.10-whats-new/'
original_language: en
published: 2023-02-21
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6f4eb40e58a7f327'
translated: false
---

> 原文：[Kreya 1.10 - What's New | Kreya](https://kreya.app/blog/kreya-1.10-whats-new/)　·　Kreya Blog

Kreya 1.10 is out with some important changes, including a CLI and operation tabs. Many other features like a history of operations and path variables for REST operations were also implemented. And of course various bugs have been fixed in this version.

### Tabs

This version introduced tabs for operations and directory settings. They are opened in their own tab, this allows easy and fast switching between them.

![An animation showcasing the tab behaviour](https://kreya.app/whats-new/1.10/tabs.gif)

#### Invoke operations simultaneously [Pro / Enterprise](https://kreya.app/pricing/)

Another advantage of the tabs is the simultaneous invocation of operations.

![An animation showcasing the simultaneous invocation of operations](https://kreya.app/whats-new/1.10/operations_simultaneously.gif)

This feature can only be used with a Pro or Enterprise plan, if you want to give this a try, there is a [10 day trial period](https://kreya.app/pricing/).

### Path variables for REST operations

For REST operations the path variables have been implemented. This allows to define the values for a variable within the path. Path variables can be defined in the URL like `{path-variable}` and then be edited in the Params tab.

![An animation showcasing the REST path params](https://kreya.app/whats-new/1.10/rest_path_params.gif)

### CLI

A new way to use Kreya is the CLI. The CLI can be downloaded from the [download](https://kreya.app/downloads/) page or via the provided [Docker image](https://hub.docker.com/r/riok/kreyac).

Invoking an operation is easy:

`kreyac operation invoke -v -p {path-to-project} ./grpc/greeter/say-hello`

For example, it can be used to execute [tests](https://kreya.app/docs/scripting-and-tests/) in a CI pipeline.

For more details on all the possible commands of the CLI, check out the [docs](https://kreya.app/docs/cli/).

### History of operations [Pro / Enterprise](https://kreya.app/pricing/)

The history of operations have also been implemented with this version. For each invoked operation all details (request, metadata, headers, response, etc.) are stored in a history entry. This history entry can be opened from the context menu of the operation, selecting such a history entry leads to a read-only tab.

![An animation showcasing the history of operations](https://kreya.app/whats-new/1.10/history.gif)

This feature can only be used with a Pro or Enterprise plan, if you want to give this a try, there is a [10 day trial period](https://kreya.app/pricing/).

### Bugfixes

This version also contains many bug fixes.

- Default settings now correctly apply for environments.
- Blank screens on Linux and macOS are fixed.
- Import streams behaviour on failure
- and many more...

### Feedback

Feel free to open a [bug report or feature request](https://github.com/riok/Kreya/issues/new/choose) if you notice something. You can also write to us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#1e767b7272715e756c7b677f307f6e6e) if you have anything else you would like to tell us.

See you soon! 👋
