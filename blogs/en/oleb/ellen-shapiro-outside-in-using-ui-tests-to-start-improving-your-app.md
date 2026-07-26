---
title: 'Ellen Shapiro: Outside In – Using UI Tests to Start Improving Your App'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/06/ellen-shapiro-ui-testing/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:90fe50f40da4510a'
translated: false
---

> 原文：[Ellen Shapiro: Outside In – Using UI Tests to Start Improving Your App](https://oleb.net/blog/2016/06/ellen-shapiro-ui-testing/)　·　Ole Begemann

# Ellen Shapiro: Outside In – Using UI Tests to Start Improving Your App

[![Preview of YouTube video: Ellen Shapiro, Outside In – Using UI Tests to Start Improving Your App](https://oleb.net/media/ellen-shapiro-ui-testing-video-preview-2292px.jpg)](https://www.youtube.com/watch?v=hYCUy-9yq_M&list=PLdr22uU_wISqm9QbnczWxXs9qyuWpSU4k&index=7)

<sub>[Watch on YouTube](https://www.youtube.com/watch?v=hYCUy-9yq_M&list=PLdr22uU_wISqm9QbnczWxXs9qyuWpSU4k&index=7) (26 minutes).  
 [The slides](https://speakerdeck.com/designatednerd/outside-in-using-ui-tests-to-start-improving-your-app-uikonf-berlin-2016).  
 [Ellen Shapiro on Twitter](https://twitter.com/designatednerd).</sub>

[Ellen Shapiro](https://www.youtube.com/watch?v=hYCUy-9yq_M&list=PLdr22uU_wISqm9QbnczWxXs9qyuWpSU4k&index=7) at [UIKonf](http://www.uikonf.com/) 2016:

> When you start to look at how you can make your [existing] code more stable, rather than [writing unit tests by] starting from the inside out and making sure each individual piece of code is very well tested and then moving out to the rest of your application, it often makes much more sense to start testing from the outside of your app and then moving inward.
> 
> And this is because ultimately the most important question in app development is, “Does this work for the user? Can the person who is using my app actually accomplish what they are trying to do?” Users _do not care_ about how well-architected your application is, how beautifully you separated your concerns, how closely you followed whatever architecture you selected. […]
> 
> So my argument is that you can do this by adding a scaffolding of UI tests around your app. […] UI tests can give you a really good way to hold up the front end of your app to make sure that it keeps working for the user, even when you start taking a sledgehammer to everything under the hood.

In [Working Effectively with Legacy Code](https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052/) (great book by the way), Michael Feathers starts with the same premise as Ellen. Legacy code is code without tests. Since most code is not designed to be easily testable, you need to refactor it before you can start writing unit tests. But to refactor it safely, the unit tests must already be in place. [This is the catch-22 of legacy code.](http://programmers.stackexchange.com/a/122024) The book teaches you how to break out of this catch by making the absolute minimal, safest changes to the code just to enable the first unit tests.

Application : Its user interface ::  
 Framework or library : Its public API

Ellen suggests to approach the problem from the UI side because that’s what ultimately matters in an app. In fact, you could argue that the user interface is the app’s equivalent to the public API of a web service or the public interface of a software library. I like it.
