---
title: New Site Design, Now Proudly Serving Static HTML
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/02/new-site-design-now-proudly-serving-static-html/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3a130dbb867ace73'
translated: false
---

> 原文：[New Site Design, Now Proudly Serving Static HTML](https://oleb.net/blog/2011/02/new-site-design-now-proudly-serving-static-html/)　·　Ole Begemann

# New Site Design, Now Proudly Serving Static HTML

When I started this blog in 2009, I chose [Wordpress](http://wordpress.org/) because it seemed to be the default option for blogs. It worked reasonably well, but I have never been completely happy with my setup. Writing posts in the browser is a pain, and so is copying and pasting them from my editor. Working with images in Wordpress is still cumbersome (although it became a lot easier in recent versions). The source code of a typical Wordpress theme feels so complicated that I never became comfortable with editing or styling it. So I ended up with one of the countless free themes from the [Wordpress Theme Directory](http://wordpress.org/extend/themes/) that was in some way “good enough” but not really (not least because it wasn’t “mine”).

# Static pages for the win!

So Wordpress had to go and something simper had to take its place. As of now, this site consists of nothing but static HTML pages and a hand-made stylesheet. It makes pages load much faster. It’s easier to maintain and extend. It lets me use my favorite editor. It gives me some hope that my site, should it ever get [fireballed](http://fireballed.org/), might actually survive. It makes putting the blog under version control trivial. It’s more secure. It’s the way hackers should build their site anyway. It’s more fun!

The drawbacks of a static site are obvious: dynamic server-side features like comments and trackbacks do not work anymore, unless you want to build your own server-side commenting engine or use a Javascript replacement such as [Disqus](http://disqus.com/). I decided that for my site, this tradeoff was worth it. While comments can be helpful and really add value to a post, the signal-to-noise ratio is usually rather poor and it is extremely rare that an entire comment thread is worth reading just for the discussion itself.

My solution is this: I still welcome your feedback very much, only you cannot post it as a comment anymore. You can still contact me via email or Twitter, however, and if your input is interesting to the rest of the community, I will post it manually as an update to the original post, thereby making it much more prominent than if it were hidden in a comment thread.

# Nanoc + Textmate + Git

If you decide to go forward with a static website, you should use a [static site generator](https://www.google.com/search?q=static+site+generator) to help with templating and the creation of archive pages. There are many open-source solutions available, and each one has different strengths. My suggestion is to choose one that is written in your favorite scripting language so you can easily extend it. I chose [nanoc](http://nanoc.stoneship.org/) because it is written in Ruby and supports very flexible site structures (and even non-file-based data sources, which I do not use at the moment but expect to do in the future). So far, I am really happy with this choice.

My workflow for creating a new blog post now looks like this:

- Open my site’s `content` folder in Textmate and create a new file.
- Write the post in Markdown (or rather [kramdown](http://kramdown.rubyforge.org/), an extended Markdown syntax). Add some metadata, such as the post’s title and creation date, at the top of the file in [YAML](http://www.yaml.org/).
- Run `nanoc compile` on the command line. nanoc runs the new file through the filters I specified in the config file (in my case, [erubis](http://www.kuwata-lab.com/erubis/), kramdown, and [Pygments](http://pygments.org/) for syntax highlighting) and updates the web site in the `output` directory.
- Run `nanoc view` to start a local web server to check my changes before they go online.
- Commit the changes to my local Git repository.
- Run `rake rsync:deploy` to deploy the changes on my server using rsync. The rake task comes with nanoc.

[![Screenshot of my Textmate + nanoc + GitX workflow](https://oleb.net/media/textmate-nanoc-gitx-workflow.png)](https://oleb.net/media/textmate-nanoc-gitx-workflow.png)

# The markup

I wanted a really clean site design, with plenty of whitespace, a large-enough font size for easy reading and no distracting stuff like dozens of share buttons. I started with a blank slate, designing the single-article view first and then moving outward to the sidebar and main navigation bar. I quite like the result I came up with, especially on the article pages like this one. The [home page](https://oleb.net/) still needs some work, though, and so do other sections I am planning.

The markup is HTML5 all the way. I used the new semantic elements such as `<section>`, `<article>`, `<header>`, and `<nav>` everywhere, and I feel that this really helped me achieve a clean markup and accompanying CSS. The biggest advantage I got from the new semantics is the fact that I can now use `<h1>` headings in my articles without interference with other headings in the templates. I highly recommend going the HTML5 way if you have to design a new site. [Modernizr](http://www.modernizr.com/) makes this work in IE (without Modernizr, IE 7 and 8 would display my site as a blank slate).

I use [Sass](http://sass-lang.com/) to help manage my CSS file and also highly recommend it.

The fonts I use, [Museo Sans](http://typekit.com/fonts/museo-sans) for paragraph text and [Museo Slab](http://typekit.com/fonts/museo-slab) for headings, are served by [Typekit](http://typekit.com/). I am currently using a 30-day trial account with Typekit and haven’t yet decided whether I’ll use it in the long term. It is a great service and I’d be happy to pay for it, but the thing that bugs me is that Typekit does not work for users who have blocked HTTP referrers. There are many good privacy reasons to not send referrers with every request, and I’d rather not provide users who do block referrers with a second-rate experience.
