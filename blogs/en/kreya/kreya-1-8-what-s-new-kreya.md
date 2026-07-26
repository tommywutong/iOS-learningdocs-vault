---
title: 'Kreya 1.8 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.8-whats-new/'
original_language: en
published: 2022-07-11
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b5f19655ba7162d1'
translated: false
---

> 原文：[Kreya 1.8 - What's New | Kreya](https://kreya.app/blog/kreya-1.8-whats-new/)　·　Kreya Blog

It has been more than half a year since Kreya released a new version. Now Kreya 1.8 is here with many new features. Kreya now supports REST APIs, scripting and tests 🚀. We also introduced a Pro and Enterprise plan. Don't worry, almost all features are still available in the free version of Kreya.

First of all, we would like to thank everyone who uses Kreya regularly and gives us feedback so that we can constantly expand and improve Kreya. The fact that the Kreya community continues to grow can also be seen in the numbers. A big milestone was reached at the end of April, when **1 million** operations were invoked :partying_face:.

### REST support

Feedback has repeatedly reached us that they find it a pity to switch between two different APIs tools (Kreya for gRPC and another one for REST). That's why we added REST support to Kreya. Try it out right now: create a new operation, select the REST type and off you go!

![An animation showcasing a rest call](https://kreya.app/whats-new/1.8/rest-call.gif)

*_A great [endpoint](https://github.com/chubin/wttr.in) with weather data to test this out._

Of course, the REST operations have all the advantages that you already know from the gRPC operations: directory settings, environments & templating, support for authentication and much more.

### Scripting and tests [Pro / Enterprise](https://kreya.app/pricing/)

We would like to introduce you to our first paid feature: scripting and tests. With this feature you can define JavaScript code that runs when an operation is invoked. Among other things, it allows you to create tests and view the results of them.

For example, you can check if the response content contains the expected value.

```text
import { expect } from 'chai';kreya.grpc.onResponse(msg => {  kreya.test('response test', () => expect(msg.content.reply).to.be.equal('hello fooBar'))})
```

The script can be defined in the new Script tab and the test results show up in the Tests tab. For more information and examples, see the [documentation](https://kreya.app/docs/scripting-and-tests/).

![An animation showcasing the scripting feature](https://kreya.app/whats-new/1.8/scripting.gif)

Of course, this feature is far from being fully developed, so if you have any suggestions for additional functions, [open an issue](https://github.com/riok/Kreya/issues/new/choose).

### Pro and enterprise plan

There is now the possibility to buy a Pro or Enterprise plan for Kreya which unlocks additional advanced features. The prices and which features are included can be found [here](https://kreya.app/pricing/).

By buying these plans you can support the development of Kreya. With the earnings we can then buy enough coffee ☕ to have even more energy to develop new features.

### More features and fixed bugs

In the last six months we have added many more small features.

- System credentials auth provider (Windows authentication) [Pro / Enterprise](https://kreya.app/pricing/)
- macOS ARM (M1) build
- gRPC deadline support

In addition, various bugs have been fixed. You can find more information at the [release notes](https://kreya.app/docs/release-notes/).

### Feedback

Feel free to open a [bug report or feature request](https://github.com/riok/Kreya/issues/new/choose) if you notice something. You can also write to us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#95fdf0f9f9fad5fee7f0ecf4bbf4e5e5) if you have anything else you would like to tell us. Stay tuned for more new features and releases!

**P.S.** Do you like Kreya? Consider supporting us by buying the Pro plan. Or better, if Kreya is used in your company, suggest buying the Kreya Enterprise plan for your team.
