---
title: 'Kreya 1.9 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.9-whats-new/'
original_language: en
published: 2022-11-04
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:92ad000e74ac5bef'
translated: false
---

> 原文：[Kreya 1.9 - What's New | Kreya](https://kreya.app/blog/kreya-1.9-whats-new/)　·　Kreya Blog

Kreya 1.9 is here :partying_face:. This time with a small release. Just a few new features, but an important macOS bugfix.

### Import operations via curl commands

A new, quick way to create operations is to import curl commands. Just copy a curl command to your clipboard and click inside Kreya. A message appears that allows you to create the operation with the properties of the curl command. This works for REST operations and also for gRPC-web operations. Support for importing gRPCurl commands will be added in a future release.

![An animation showcasing an import operation via curl commands](https://kreya.app/whats-new/1.9/import_operations_via_curl.gif)

### Variable support for scripting and templating [Pro / Enterprise](https://kreya.app/pricing/)

We have implemented a feature that has been requested for a long time: The reuse of data from one request to another via scripting and templating. To achieve this, you can now set multiple variables on the Script tab and access them in another request via a template expression.

As shown in the example below, values from a response can be extracted and then stored in a variable.

```text
kreya.grpc.onCallCompleted(call => {  const name = msg.content.reply.substr('Hello '.length);  kreya.variables.set('name', name);});
```

To access the `name` variable you can use a template expression. For example in a JSON body request.

```text
{  "greeting": "{{ vars.name }}"}
```

For illustration one more gif (maybe you have noticed that we love gifs 😉) or more detailed information in the [docs](https://kreya.app/docs/scripting-and-tests/#user-variables).

![An animation showcasing the variable support for scripting and templating](https://kreya.app/whats-new/1.9/variable_support.gif)

This feature can currently only be used with a Pro or Enterprise plan, if you want to give this a try, there is a [10 day trial period](https://kreya.app/pricing/).

### Bugfixes

In this version, many different bugs have been fixed. Especially the bug in macOS 13.0 that caused Kreya to crash on startup.

### Mapperly

One adjustment that affects our code: we have replaced AutoMapper with [Mapperly](https://mapperly.riok.app/) throughout our codebase. Mapperly is a open source .NET source generator for generating object mappings which is maintained by us. This may be of interest to some .NET developers.

### Feedback

Feel free to open a [bug report or feature request](https://github.com/riok/Kreya/issues/new/choose) if you notice something. You can also write to us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#08606d64646748637a6d716926697878) if you have anything else you would like to tell us.

Currently some nice features are in the works and will be available soon (e.g. a CLI to execute operations and tests).

Stay tuned 🚀
