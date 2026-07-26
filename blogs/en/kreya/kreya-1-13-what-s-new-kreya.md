---
title: 'Kreya 1.13 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.13-whats-new/'
original_language: en
published: 2024-01-29
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7cc4b73e6a1597c7'
translated: false
---

> 原文：[Kreya 1.13 - What's New | Kreya](https://kreya.app/blog/kreya-1.13-whats-new/)　·　Kreya Blog

Kreya 1.13 is now available! With a new major feature .. 🥁🥁 .. collections! This allows you to invoke multiple operations with a single click. It's also now possible to import your Postman collections and environments. The protobuf declaration for gRPC operations can be viewed in the new Declaration tab. The CLI has a new 'create project' command and a few bugs have been fixed.

### Collections [Pro / Enterprise](https://kreya.app/pricing/)

Pick your operations, put them all in one collection and run them. All operations will be executed in the defined order. Test scripts are also executed and the results are displayed together. Now it's much easier to test your application with a single click.

![An animation showcasing creating and running a collection](https://kreya.app/whats-new/1.13/collection.gif)

A collection can also be invoked using the CLI.

`kreyac collection invoke -p ./my-directory/my-project.krproj my-collection.krcol`

For more information on the CLI, see the [documentation](https://kreya.app/docs/cli/).

### Postman importer

Want to import your Postman collections or environments? This is now possible in the menu at the `Kreya > Import...` window.

![An animation showcasing importing a Postman collection](https://kreya.app/whats-new/1.13/postman_importer.gif)

### Protobuf declaration

Behind each gRPC endpoint is a protobuf declaration. This can now be viewed in the new Declaration tab.

![An animation showcasing opening the proto declaration](https://kreya.app/whats-new/1.13/proto_declaration.gif)

### CLI create project

A new command has been added to the CLI. It is now possible to create a new project.

`kreyac project create my-project`

### Bug fixes

Many bugs have been fixed. More details can be found on our [release notes](https://kreya.app/docs/release-notes/) page.

If you find a bug, please do not hesitate to [report](https://github.com/riok/Kreya/issues/new/choose) it. You can contact us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#c2aaa7aeaead82a9b0a7bba3eca3b2b2) for any further information or feedback.

Have a nice day and see you soon! ✌
