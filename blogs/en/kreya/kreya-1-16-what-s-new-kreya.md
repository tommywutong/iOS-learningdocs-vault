---
title: 'Kreya 1.16 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.16-whats-new/'
original_language: en
published: 2025-01-16
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:28061d6a6e8f0447'
translated: false
---

> 原文：[Kreya 1.16 - What's New | Kreya](https://kreya.app/blog/kreya-1.16-whats-new/)　·　Kreya Blog

Kreya 1.16 comes with support for WebSocket calls and an updated look and feel for the project settings. Faker is added to the scripting API, cookie management is added and many more features are implemented.

### WebSocket support

Create a new operation in the operations list, select the type WebSocket and start using WebSockets in Kreya!

![An animation showcasing creating an WebSocket operation and sending it.](https://kreya.app/whats-new/1.16/websocket.gif)

You can find all the details in our [documentation](https://kreya.app/docs/operations/#websocket).

### Auth as custom header or query param

It is now possible to define a custom header for the auth or send it as a query parameter. This can be configured for each auth configuration under advanced options.

![An animation showcasing sending auth as a custom header.](https://kreya.app/whats-new/1.16/auth_custom_header.gif)

### Added faker to scripting API [Pro / Enterprise](https://kreya.app/pricing/)

The [bogus faker](https://github.com/bchavez/Bogus) is now directly accessible in the scripting tab with `kreya.faker`. No additional imports are required.

![An animation showcasing using faker in the scripting tab.](https://kreya.app/whats-new/1.16/faker_scripting_api.gif)

### Updated look and feel of Kreya

Kreya's UI has been reworked. Especially the project settings have been given a fresh new look. They now open as a tab, allowing the user to quickly switch between an operation and the project settings. To open the project settings, go to the application menu and click `Project > Environments or Authentications or ...`.

![An animation showcasing opening project settings.](https://kreya.app/whats-new/1.16/project_settings.gif)

Tip: For even faster access, the project settings can be opened using keyboard shortcuts (e.g. Ctrl+⇧+E for environments on Windows or ⌘+⇧+E on MacOS).

We've also streamlined the workflow for creating operations, so you don't have to select the type every time you create an operation, just choose the right type of operation from the menu at the start.

![An animation showcasing creating operations.](https://kreya.app/whats-new/1.16/create_operation.gif)

### Collection state filter [Pro / Enterprise](https://kreya.app/pricing/)

In the header of a collection it is now possible to filter the operations by their states.

![An animation showcasing filtering states of operations in a collection.](https://kreya.app/whats-new/1.16/collection_state_filter.gif)

### File exclusion list for gRPC proto file importers

In gRPC proto file importers, files can be excluded from import. This is particularly useful if you're importing entire folders of protos and don't want to import certain subfolders.

![An animation showcasing excluding files in a gRPC proto file importer.](https://kreya.app/whats-new/1.16/file_exclusion_list.gif)

### Importer custom headers [Pro / Enterprise](https://kreya.app/pricing/)

To add custom headers to the gRPC server reflection and REST OpenAPI URL importers, open the advanced options in these importers.

![An animation showcasing excluding files in a gRPC proto file importer.](https://kreya.app/whats-new/1.16/importer_custom_headers.gif)

### Cookie management

Cookies can now be managed in Kreya. A response tab is visible when a cookie is set and all cookies can be managed in a separate tab under `Project > Cookies`. It is important to note that all cookies are managed separately per environment.

![An animation showcasing managing cookies.](https://kreya.app/whats-new/1.16/cookie_management.gif)

### AWS Signature v4 authentication

An additional auth type has been added. An AWS Signature v4 auth type can now be created in the auth settings.

![An animation showcasing creating an AWS authentication.](https://kreya.app/whats-new/1.16/aws_auth.gif)

### Bug fixes

Many bugs have been fixed. More details can be found on our [release notes](https://kreya.app/docs/release-notes/) page.

If you find a bug, please do not hesitate to [report](https://github.com/riok/Kreya/issues/new/choose) it. You can contact us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#751d1019191a351e07100c145b140505) for any further information or feedback.

Have a nice day! 👋
