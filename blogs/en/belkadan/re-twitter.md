---
title: 'Re: Twitter'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2022/12/Re-Twitter/'
original_language: en
published: 2022-12-03
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ab9f4ba537ce29cb'
translated: false
---

> 原文：[Re: Twitter](https://belkadan.com/blog/2022/12/Re-Twitter/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Keyboard Pants](https://belkadan.com/blog/2021/07/Keyboard-Pants/)

[Multiplayer Slipways](https://belkadan.com/blog/2023/08/Multiplayer-Slipways/) »

« [#TalkPay](https://belkadan.com/blog/2022/03/TalkPay/?tag=tech-industry)

« [Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/?tag=running-a-website)

[Setting up GoToSocial](https://belkadan.com/blog/2023/02/Setting-up-GoToSocial/?tag=running-a-website) »

## [Re: Twitter](#)

Twitter was

- a place where my shitposts started conversations (or at least joke threads), and where I could participate in conversations (or at least joke threads) on other people’s shitposts
- a comments section for my blog that wasn’t on my blog, and a comments section for others’ blogs even if they don’t have one on their blog
- a place to learn about other cool people and projects through the people I already know, and a place for other people to learn about me and my projects through the people they already know

---

I want a place for shitposts and other ephemera, so maybe I’ll start a microblog. I don’t want to check all over the place for other peoples’ shitposts, but maybe enough of them will be ActivityPub or newsfeeded that I can keep track of them.

This blog had comments once, but they weren’t ever that satisfying. The world has just moved on from comments, I think, or at least my world; the sites that have them don’t feel like good conversation. Maybe replies on the microblog (ActivityPub again) will be enough.

I’m not sure yet _what_ microblog to run. This blog (at the time of this writing) uses a forked old version of [Jekyll](https://jekyllrb.com/), but the “conversation” part of ActivityPub means a static generator won’t cut it. Similarly, my brain wants to turn to a web module like [WordPress](https://en.wikipedia.org/wiki/WordPress) that I can just put on my existing website, like I [did with gitweb](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/)…but ActivityPub is a “push” model, like email[1](#fn:listserv), and that doesn’t scale well if I eventually get as many followers as I did on Twitter. So now I’m looking at various minimal installations that just need a database and a place to run.[2](#fn:takahe) I am, however, sure I want to run it myself this time. (Feel free to let me know your recommendations via…oh. Via email, I guess. jrose, at this domain.)

There was originally going to be more to this post, about leaving Facebook first, about my unrelated temporary Twitter hiatus becoming permanent. Maybe it would have rung true with you too. But it really comes down to the three bullet points above. There were other things I enjoyed about Twitter, but they’re not as important.

1. A friend made a very apt comparison between a follower list and an email listserv: either way you have a single message, or a batch of messages, that needs to be delivered to N individuals on up to N different servers. This was on the heels of another friend pointing out that email had to grapple with this “fanout” problem decades ago, and that the ActivityPub spec authors did not learn their history and were thus doomed to repeat it. [↩︎](#fnref:listserv)
2. I did find Andrew Godwin’s [Takahē](https://jointakahe.org/about/), which originally had a goal to run “serverless”—just schedule a cron job to process pending work! But it sounds like that mode’s got some serious responsiveness drawbacks. Personally I have the sense it could still be done as long as you are careful about _what_ operations need asynchronous processing. [↩︎](#fnref:takahe)

This entry was posted on [December](https://belkadan.com/blog/2022/12) 03, [2022](https://belkadan.com/blog/2022) and is filed under [Personal](https://belkadan.com/blog/personal). Tags: [Tech industry](https://belkadan.com/blog/tags/tech-industry), [Running a website](https://belkadan.com/blog/tags/running-a-website)
