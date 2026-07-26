---
title: Auspicious Continuation
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/05/Auspicious-Continuation/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:05b985fa2d1291ff'
translated: false
---

> 原文：[Auspicious Continuation](https://belkadan.com/blog/2011/05/Auspicious-Continuation/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Scripting Bridge](https://belkadan.com/blog/2009/07/Scripting-Bridge/)

[User-Side Troubleshooting](https://belkadan.com/blog/2011/05/User-Side-Troubleshooting/) »

« [Inauspicious Beginnings](https://belkadan.com/blog/2007/01/Inauspicious-Beginnings/?tag=meta)

[Big News](https://belkadan.com/blog/2012/05/Big-News/?tag=meta) »

## [Auspicious Continuation](#)

Has it really been a year and a half – almost two years – since I’ve used this blog? I’ve certainly had things I’ve wanted to say, neat little programming tidbits or war stories or musings on Apple’s current directions. But somehow I never got around to bringing this back online.more

At the time, I was more focused on the redesign of the site. The old site, if anyone remembers, looked something like this:

[![Grey and with too much text on the main pages](https://belkadan.com/blog/2011/05/Auspicious-Continuation//old-site-sm)](https://belkadan.com/blog/2011/05/Auspicious-Continuation//old-site.jpg)

I much prefer the current “shadowbox” layout, which plays with CSS3 a fair amount. But more importantly, it cuts down on the verbosity of everything, and makes it easier to get to the important stuff.

The trigger for the site redesign was the imminent release of [Keystone](http://belkadan.com/keystone). With all the trouble getting Keystone out, I didn’t want to worry about porting over -dealloc. This blog originally ran on a homebrewed system running on PHP and MySQL, which I dubbed BlogAgain. Amazingly, it worked pretty well. But I had two major problems with it: comment spam, and no notifications when someone posts a comment (meaning _extensive_ comment spam). It was just unprofessional. So when it came time to redesign the site, I exported the data as an Atom feed, archived the SQL database, and more or less forgot about the blog.

Not cool, right?

In the last two years, I’ve participated in Google Summer of Code, working on [Clang](http://clang.llvm.org). I’ve migrated _this_ site, along with my other personal sites, over to [A2 Hosting](http://a2hosting.com) – and off of a home server running Debian. And I’ve completed a B.A. in Computer Science at UC Berkeley, having numerous adventures along the way. So it’s not like I haven’t been doing stuff. But it’s time to bring this back, if only so I can post highly irregularly.

Having been bitten by WordPress hackers on another site a year or two ago, I didn’t want to deal with that this time around. And to be honest, a lot of the dynamic content engines felt too heavy. I didn’t want to have to deal with MySQL, with a site-based editor that fails at WYSIWYG or forces HTML. (I’ve been pretty obsessed with [Markdown](http://daringfireball.net/projects/markdown) for a while now.) So the current trend towards “static site generators” made sense to me.

I ended up picking [Jekyll](https://github.com/mojombo/jekyll), the engine used by GitHub to run their “GitHub Pages” feature. Why? Well, it had a fairly good import path, and it was an active project. Also it would be an excuse to learn/practice Ruby, which I know very little of. With [Disqus](http://disqus.com/) handling the comments this time around, the last piece dropped into place, and I feel _good_ about this.

If you’re a Jekyll user, you can check out my custom theme, [Shadowbox](https://github.com/belkadan/jekyll-shadowbox), on Github. I’m hoping to put more stuff on Github at some point, but I’m still using Xcode 3 for Cocoa programming, which doesn’t have great integration. Git’s begun to pervade anything else that could remotely benefit from versioning, though, thanks to TextMate. The rest of the Belkadan site, for example, is made of true-static HTML living in a Git repo, which I can `git push` to make updates go live. (I don’t feel like it’s necessary to version _blog posts_ though, so they’re just backed up with Time Machine like everything else, and this part of the site is transferred to the live server via `rsync`.)

How’s everything else going? Well, Keystone and Webmailer are both in fairly stable places right now, though I definitely have a couple fixes for Keystone I’d like to work on at some point. As for me personally, we’ll see. (I’ll definitely announce here when I get a job.)

No promises to blog any more than in the past, i.e. once a month or less, but at least the opportunity’s up now.

This entry was posted on [May](https://belkadan.com/blog/2011/05) 30, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Meta](https://belkadan.com/blog/tags/meta)
