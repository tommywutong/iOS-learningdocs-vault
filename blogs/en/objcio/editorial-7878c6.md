---
title: Editorial
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/19-debugging/editorial'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:eeb6c9c165406e6f'
translated: false
---

> 原文：[Editorial](https://www.objc.io/issues/19-debugging/editorial)　·　objc.io

Welcome to objc.io issue 19: all about debugging.

We're all making mistakes, all the time. As such, debugging is a core part of what we do every day, and we've all developed debugging habits — our own way of approaching the all-too-common situation where something is not working as it should.

But there's always more to learn about debugging. Do you use LLDB to its full potential? Have you disassembled framework code to glance under the covers? Have you ever used the DTrace framework? Do you know about Apple's new activity tracing APIs? We're going to take a look at these topics and more in this issue.

Peter starts off with a [debugging case study](https://www.objc.io/issues/19-debugging/debugging-case-study/): he walks us through the workflow and the tools he used to track down a regression bug in UIKit, from first report to filed radar. Next, Ari shows us the [power of LLDB](https://www.objc.io/issues/19-debugging/lldb-debugging/), and how you can leverage it to make debugging less cumbersome. Chris writes about his [debugging checklist](https://www.objc.io/issues/19-debugging/debugging-checklist/), a list of the many things to consider when diagnosing bugs. Last but not least, Daniel and Florian talk about two powerful but relatively unknown debugging technologies: [DTrace](https://www.objc.io/issues/19-debugging/dtrace/) and [Activity Tracing](https://www.objc.io/issues/19-debugging/activity-tracing/).

We'd love for you to never need all of this — but since that's not going to happen, we at least hope you'll enjoy these articles! :-)

Best from a wintry Berlin,

Chris, Daniel, and Florian.

---
