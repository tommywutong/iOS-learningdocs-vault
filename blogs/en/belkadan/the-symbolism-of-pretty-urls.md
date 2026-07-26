---
title: The Symbolism of Pretty URLS
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2007/04/Symbolism-of-Pretty-URLs/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8038c5216452219e'
translated: false
---

> 原文：[The Symbolism of Pretty URLS](https://belkadan.com/blog/2007/04/Symbolism-of-Pretty-URLs/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Flexible PHP](https://belkadan.com/blog/2007/03/Flexible-PHP/)

[GenericToolbar Icon](https://belkadan.com/blog/2007/06/GenericToolbar-Icon/) »

## [The Symbolism of Pretty URLS](#)

Most people have heard of pretty URLs by now, sometimes under the name “Permalinks”. (Actually, the two are pretty different things, just linked; see below.) It’s not trendy anymore to have a blog that doesn’t support them anymore, or indeed any sort of CMS-based site. BlogAgain, being, in a way, both of these, really needed something nicer than “blog.php?id=2”.

Why? Well, first of all, “good URLs should be hackable.” (This is from a 1999 article called [“URLs as UI”](http://www.useit.com/alertbox/990321.html) that still applies in the overhyped world of Web 2.0). This means, in my mind, that moving up a directory should give you something useful. Ideally the user should understand everything in the URL. The opposite issue of link permanency is pretty good with an ID-based scheme, but the tradeoff in readability seems to help. Also, [ID-based schemes have import-export problems](http://mar.anomy.net/entry/2003/06/09/13.28.59/), since a blog may already have a set of IDs in use. So that was out.

So, what is a “pretty URL”, and how is it different from a “permalink”? Well, basically you hear them used nearly interchangeably because most blog software uses them together as well. A permalink is an unchanging link to a post, a pretty URL is one that avoids any sort of internal ID and gives the viewer a nice way to see what they’re looking at. They don’t really share any characteristics in their definition, but they’re certainly not mutually exclusive and really are even compatible.

So I then had two choices: hierarchical (“/Blog/Symbolism-of-Pretty-URLs”) or chronological (“2007/03/Symbolism-of-Pretty-URLs”). But I’m not just running a blog, I’m writing software! That means the user is paramount. So each post has a flag saying which form it prefers, “parent/[slug](http://en.wikipedia.org/wiki/Slug_%28disambiguation%29#Other_uses)” or “YYYY/MM/slug”. And that even allows hybrid forms, like “2007/03/Symbolism-of-Pretty-URLS/I-Agree”. The interesting thing is that, at least for now, you can still access a post either way (parent or month). Bug or feature?

But I used the word “symbolism”, and so far there hasn’t been anything symbolic. Let’s take three pages used for a post, blog.php (normal display), atom.php (atom feed), and postresponse.php (for commenting). Before we had URLs like blog.php?id=2, and similar ones for the other two pages. Now, we move to something like Blog/, Blog/atom, and Blog/post. The focus has shifted from the action to the post.

_The focus has shifted from the action to the post._

Sound familiar? This struck a chord with me as a programmer: this is very much the transition from functional/imperative languages to object orientation. Amazing! Completely unintentionally, I’ve emulated the evolution of programming languages in a single piece of software. Need more explanation?

`atom.php?id=2` _is_ `atomForPost(post2)`

`Blog/atom` _is_ `blogPost.atom()`

(Separately, we get the benefit of meaningful variable names or symbolic constants over raw integers, depending on how you look at it.)

So, it makes sense to evolve the whole blog this way, right? Eventually, with PATH_INFO and mod_rewrite (although the first can stand alone), I should be able to move nouns from the query string to the base of the URL, and relegate verbs to a lower part of the URL.

Thoughts?

This entry was posted on [April](https://belkadan.com/blog/2007/04) 13, [2007](https://belkadan.com/blog/2007) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Musings](https://belkadan.com/blog/tags/musings)
