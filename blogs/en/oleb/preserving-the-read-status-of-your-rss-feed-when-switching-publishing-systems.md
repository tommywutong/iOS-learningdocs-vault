---
title: Preserving the Read Status of Your RSS Feed When Switching Publishing Systems
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/01/preserving-rss-feed-read-status/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:379abb91b30e94e2'
translated: false
---

> 原文：[Preserving the Read Status of Your RSS Feed When Switching Publishing Systems](https://oleb.net/blog/2014/01/preserving-rss-feed-read-status/)　·　Ole Begemann

# Preserving the Read Status of Your RSS Feed When Switching Publishing Systems

Every once in a while, I notice a number of old entries in a particular feed in my RSS reader showing up as unread again, although the posting dates of these entries lie all in the past and I had marked them as read before.

The reason for this phenomenon is usually that the publisher of the feed has migrated their site to a new publishing system and this caused old posts to appear as new items in the RSS feed. While certainly more annoying things exist than having to mark a bunch of old articles as read again, this behavior is a bit unnerving to the readers of a feed.

As a feed publisher, you should take steps to avoid the issue in the first place the next time you move to a new content management system. Here’s how.

# Item IDs

Each entry in your feed should have a unique identifier. The corresponding XML element is called `<id>` in the [Atom standard](http://tools.ietf.org/search/rfc4287) and `<guid>` in the [RSS spec](http://cyber.law.harvard.edu/rss/rss.html). `<guid>` is an optional element in RSS but most popular blogging systems generate it by default.

**Your goal as a feed publisher must be to keep the identifiers for existing feed items constant when switching publishing systems.**

Most feed readers use the unique identifier to determine whether they have already seen a particular item in the feed and to associate their own data (such as read or starred status) with it.[1](#fn:1) So your goal as a feed publisher must be to keep the identifiers for existing feed items constant when switching publishing systems. That’s all you have to do.

# Moving from Wordpress to a Static Site Generator

Most content management systems use an item’s URL as its unique identifier. This isn’t necessarily the “pretty” URL that are exposed to visitors of the site, though. For example, Wordpress always uses its internal URLs of the form `http://example.com/?p=1234` as item IDs, regardless of what permalink format you chose for your site.

When I converted this blog [from Wordpress to nanoc](https://oleb.net/blog/2011/02/new-site-design-now-proudly-serving-static-html/)[2](#fn:2), I solved the problem as follows:

1. For existing posts, include an attribute in the header that contains (a) either the full identifier that has been used in the feed, or (b) enough information to rebuild the item ID later. In the case of Wordpress, the old article ID is sufficient. For example, the post header might look like this (note the `wordpress_id` attribute):

  ```
  title: "The Music Player Framework in iPhone SDK 3.0"
  created_at: 2009-07-13 15:53:00 +02:00
  updated_at: 2009-10-28 12:00:00 +01:00
  wordpress_id: 37
  author: "Ole Begemann"
  kind: "blog_post"
  layout: "article"
  ```
2. In the XML template that generates your feed, include a conditional that outputs old-style item identifiers if the `wordpress_id` attribute is present and new IDs if not. In Ruby/ERB, it might look this:

  ```
  <% posts.each do |post| %>
  <entry>
    <id>
      <%= post[:wordpress_id] ? "http://oleb.net/?p=#{post[:wordpress_id]}"
        : "http://oleb.net#{post.path}" %>
    </id>
    …
  </entry>
  <% end %>
  ```

There is no step 3.

1. I am not certain what other information feed readers use to identify an item if the `<guid>` element is missing. I assume they attempt to use the `<link>` element, which often contains the same content, in such cases. This is just one of the reasons why [writing an RSS reader sucks](http://inessential.com/2013/03/18/brians_stupid_feed_tricks). [↩︎](#fnref:1)
2. I’m using [nanoc](http://nanoc.ws/) as the example here, but the process should work similarly for any static site generator or, in fact, any publishing system that gives you full control over the contents of your feed. [↩︎](#fnref:2)
