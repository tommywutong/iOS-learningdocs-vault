---
title: 'Kreya 1.19 and 1.19.1 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.19-whats-new/'
original_language: en
published: 2026-02-25
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:be814e993fdd2b22'
translated: false
---

> 原文：[Kreya 1.19 and 1.19.1 - What's New | Kreya](https://kreya.app/blog/kreya-1.19-whats-new/)　·　Kreya Blog

Kreya 1.19 is here, and in the meantime we have already released 1.19.1. Together they bring GraphQL, OAuth 2.0 Device Flow, and a set of polish improvements across the CLI and UI.

## GraphQL support

GraphQL operations allow you to execute queries, mutations, and subscriptions against a GraphQL API. Add a new operation by clicking the  icon. Next, choose a descriptive name for your operation and hit enter.

![An animation showcasing creating a GraphQL operation](https://kreya.app/whats-new/1.19/create_graphql_operation.gif)

You can also enter variables for your query in the "Variables" tab in JSON format. These variables can be used in your query with the `$` prefix (e.g. `$bookId`).

If you don't have a GraphQL API yet, you can experiment with some GraphQL operations in our example project, which you can pull from [GitHub](https://github.com/riok/Kreya).

## OAuth 2.0 Device Flow

We have added support for the [OAuth 2.0 Device Authorization Grant](https://oauth.net/2/device-flow/) (formerly known as the Device Flow) that enables devices with no browser or limited input capability to obtain an access token. To use this, create a new authentication in `Project > Authentication` and select the Grant type `Device code`.

You can then choose this new authentication for an operation. Pressing the `Update` button will start the Device Flow.

![An animation showcasing using the new device flow auth](https://kreya.app/whats-new/1.19/device_flow.gif)

## UI improvements

### Recent projects are searchable

You can now search for recent projects in the launch window. Start typing the name of the project you are looking for, and a list of matching projects will appear.

![An animation showcasing searching for recent projects](https://kreya.app/whats-new/1.19/recent_projects_searchable.gif)

### Create a new project

You can now create a new project directly from the application menu. Select `Kreya > New project...` and enter the necessary project information.

![An animation showcasing creating a new project](https://kreya.app/whats-new/1.19/create_new_project.gif)

### Importer type selection

The process of selecting an importer type has been simplified. Choose your type at the top of the page and enter the required importer information.

![An animation showcasing selecting the importer type](https://kreya.app/whats-new/1.19/importer_type_selection.gif)

### Operation actions

We have moved all operation-related actions into the operation header. Actions such as 'Change gRPC method', 'Reset operation' and 'History' can now be found there.

![An animation showcasing using the new operation actions](https://kreya.app/whats-new/1.19/operation_actions.gif)

### Inline create operation

We have optimized the process of creating an operation in Kreya. First, you enter the name, and then you can select the gRPC method in the operation header.

![An animation showcasing creating an gRPC operation inline](https://kreya.app/whats-new/1.19/inline_create_operation_grpc.gif)

The same applies to REST operations if you have imported API definitions. You can also select a template in the operation header.

![An animation showcasing creating an REST operation inline](https://kreya.app/whats-new/1.19/inline_create_operation_rest.gif)

## Insomnia collection v5 import support

We have added support for importing Insomnia collection v5 files. In the application menu, select `Kreya > Import`, then select `Insomnia collection (v5)` and your file.

![An animation showcasing importing an Insomnia collection v5](https://kreya.app/whats-new/1.19/insomnia_collection_v5_import.gif)

## And more

There are other notable improvements:

- gRPC v1 reflection support in addition to v1alpha
- Session cookies support
- Simplified test scripting

## Kreya 1.19.1

Version 1.19.1 focuses on polish and quality-of-life improvements across the CLI, UI, and platform integrations.

### CLI

- Added the `--relative-to` option for CLI path resolution relative to the project or current working directory. See [relative path resolution](https://kreya.app/docs/cli/path-globs/#relative-path-resolution).
- Added the filename to the JUnit reporter output
- Automatically detect Kreya projects in parent directories
- Show correct default values in the CLI help output

### Kreya UI

- gRPC: Improved fallback to the v1alpha server reflection importer
- Added a `Copy as kreyac` option to the operation context menu to copy the operation as a kreyac command.
- Added quick actions to open settings tabs, clear all cookies and clear all user variables
- Added a word wrap option to all editors with horizontal scrolling

## Release notes and feedback

For a full list of new features and bugfixes, see the [release notes](https://kreya.app/docs/release-notes/).

If you have feedback or questions, please [contact us](https://kreya.app/cdn-cgi/l/email-protection#254d4049494a654e57405c440b445555) or [report an issue](https://github.com/riok/Kreya/issues/new/choose).

Stay tuned! 🚀
