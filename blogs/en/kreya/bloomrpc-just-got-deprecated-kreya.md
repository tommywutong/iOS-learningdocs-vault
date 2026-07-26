---
title: 'BloomRPC just got deprecated | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/bloomrpc-deprecated/'
original_language: en
published: 2023-01-06
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a77cd6449820cc8a'
translated: false
---

> 原文：[BloomRPC just got deprecated | Kreya](https://kreya.app/blog/bloomrpc-deprecated/)　·　Kreya Blog

The [BloomRPC](https://github.com/bloomrpc/bloomrpc) GitHub repo just got archived. BloomRPC was one of the earliest gRPC GUI clients, but has not received any updates in nearly two years.

## BloomRPC, the first gRPC GUI client

BloomRPC was one of, if not the first gRPC GUI client to emerge. The workflow for calling gRPC APIs was simple: first you import the protobuf definitions, then you set the endpoint and you're ready to send requests. Thanks to this approach, it quickly gained wide acceptance. After its first release, BloomRPC received over a thousand GitHub stars and continued to steadily acquire more.

For a long time, BloomRPC was the best gRPC GUI client out there. It supported most of the gRPC features. Even though it got some rough edges, it was perhaps its simplicity that conviced users to use BloomRPC.

## Missing features and stalled development

After some time, features requested by the community remained missing. Even pull requests implementing these features were either not merged or never included in a release. Heavily requested functionality, such as [being able to view response metadata](https://github.com/bloomrpc/bloomrpc/issues/37) or [gRPC server reflection](https://github.com/bloomrpc/bloomrpc/issues/1), was never released. What had happened?

BloomRPC was created and maintained by a single person, with the occassional pull request contributed by the community. After this person left his company, [no maintainer could be found to continue working on BloomRPC](https://github.com/bloomrpc/bloomrpc/issues/398). At this point, development of BloomRPC came to a halt and a new version was never released.

## Why you should consider switching

As BloomRPC was created with Electron and not updated in long time, it includes a now very outdated Chromium browser. This can pose a security risk, although it is probably very difficult to exploit.

As described above, BloomRPC also lacks many features that other similar tools support.

## Kreya is the best BloomRPC alternative

As the developers, we naturally recommend [Kreya](https://kreya.app) as the best BloomRPC alternative. The missing features of BloomRPC were [one of the reasons](https://kreya.app/blog/how-we-built-kreya/) why we created Kreya. In the [Kreya vs BloomRPC comparison](https://kreya.app/comparisons/bloomrpc/), we also try to highlight how Kreya supports all of the features that BloomRPC implements.

Other popular GUI clients like Postman or Insomnia are of course also good alternatives, but they may not support the full feature set of BloomRPC.
