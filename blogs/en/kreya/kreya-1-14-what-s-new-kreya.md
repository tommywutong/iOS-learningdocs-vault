---
title: 'Kreya 1.14 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.14-whats-new/'
original_language: en
published: 2024-04-18
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:763d6071eb23bf44'
translated: false
---

> 原文：[Kreya 1.14 - What's New | Kreya](https://kreya.app/blog/kreya-1.14-whats-new/)　·　Kreya Blog

Kreya 1.14 brings you a lot of new features. Starting with running a directory as a collection, an Insomnia importer, automatic import of system environment variables and opening items in the file manager. The CLI now has the ability to invoke multiple collections with a single call and generate a JUnit test report. Scripting has been improved and trace messages can be filtered.

### Run directory as collection [Pro / Enterprise](https://kreya.app/pricing/)

In Kreya 1.13 we introduced [collections](https://kreya.app/docs/collections/), which allow you to invoke certain operations together. With Kreya 1.14 it's now also possible to run a whole directory as a collection, so you don't have to add all operations to a collection manually. Just open a directory and hit run in the "Run as collection" tab to run all operations in that directory.

![An animation showcasing running a directory as collection](https://kreya.app/whats-new/1.14/run_directory_as_collection.gif)

### Insomnia importer

Next to the Postman importer, we also added an Insomnia importer. You can import your Insomnia collection in the menu at the `Kreya > Import...` window.

![An animation showcasing importing a Insomnia collection](https://kreya.app/whats-new/1.14/insomnia_importer.gif)

### System environment variables for CI/CD systems or secrets

Kreya automatically imports system environment variables prefixed with `KREYA_ENV_` into the active Kreya environment. The prefix is removed and the variable can be used normally with `{{ env.VARIABLE }}`. System environment variables are especially useful in CI/CD systems or for secrets.

![An animation showcasing using a environment variable](https://kreya.app/whats-new/1.14/environment_variables.gif)

### Open items in file manager

Directories, operations and collections can now be opened in your system's file manager. This gives you easy access to your Kreya project files.

Kreya stores everything in files which allows you to easily sync with a version control system. A detailed description can be found in our blog post [Bring your own storage](https://kreya.app/blog/bring-your-own-storage/).

![An animation showcasing opening a directory in the file manager](https://kreya.app/whats-new/1.14/open_in_file_manager.gif)

### Invoke multiple collections in CLI [Pro / Enterprise](https://kreya.app/pricing/)

Collections can be invoked with the CLI, and with Kreya 1.14 it's possible to invoke multiple collections with a single call.

`kreyac collection invoke -p {path-to-project} {path-to-collections}`

### Junit reporter

Invoking operations and collections in the CLI now has an option to generate a JUnit report. Simply add the `--test-report-junit` flag with a file name to your CLI call.

`kreyac collection invoke -p {path-to-project} {path-to-collections} --test-report-junit junit-report.xml`

### Trace messages filter

Trace messages can now be filtered, allowing you to quickly view certain types of trace messages, such as your script trace messages.

![An animation showcasing filtering trace messages](https://kreya.app/whats-new/1.14/trace_message_filter.gif)

### Improve scripting [Pro / Enterprise](https://kreya.app/pricing/)

Scripting now has environment access, allowing you to read all the properties of the active environment, and a sleep function was added.

```javascript
kreya.trace('Active environment: ' + kreya.environment.active.name);// sleep for 1skreya.sleep(1000);kreya.trace('Some secrets: ' + kreya.environment.active.content.PROD_KEY);
```

### Bug fixes

Many bugs have been fixed. More details can be found on our [release notes](https://kreya.app/docs/release-notes/) page.

If you find a bug, please do not hesitate to [report](https://github.com/riok/Kreya/issues/new/choose) it. You can contact us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#deb6bbb2b2b19eb5acbba7bff0bfaeae) for any further information or feedback.

See you and keep on rockin'... 🎸
