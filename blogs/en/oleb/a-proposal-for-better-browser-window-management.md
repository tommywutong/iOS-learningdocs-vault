---
title: A Proposal for Better Browser Window Management
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/01/browser-window-management/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3cd7c7380aa5cc2d'
translated: false
---

> 原文：[A Proposal for Better Browser Window Management](https://oleb.net/blog/2015/01/browser-window-management/)　·　Ole Begemann

# A Proposal for Better Browser Window Management

## External Links Never Open in the Right Window

My window management habits are nowhere near [Siracusean levels](http://atp.fm/episodes/96),^[1](#fn:1) but at any given time I do have several browser windows open, with multiple tabs each.

- One window is usually reserved for the task I’m currently working on; it contains relevant documentation, blog posts, Stack Overflow answers, etc. There may be several of these windows, separated by task.
- I have one or more additional windows to collect stuff I found online but haven’t read yet. Most of the tabs in these windows come from links I click in my Twitter or RSS client.
- Depending on the situation, there may be several more windows that acts as reminders for things I want to write about, products I consider buying, etc. These are usually minimized.
- When I do web development, the browser is also used to test the site I work on. This quickly adds four to six additional browser windows to the list (for mobile and desktop layout in multiple browsers), all of which are carefully sized and positioned. When the same app is used for both research and testing, window management becomes even more of a hassle.

Whenever I open a new link (say, from my Twitter client), it creates a tab in the most recently used window of my default browser.^[2](#fn:2) More often than not, this is not what I want. I constantly end up moving tabs between windows.

**A locked browser window would never be used to open links from external sources. The browser would use the most recently used unlocked window to open those links.**

Here’s an idea how to solve this: I’d like to be able to “lock” a browser window.^[3](#fn:3) A locked window would never be used to open links from external sources (Twitter client, Mail app, Alfred, etc.). Instead, the browser would use the most recently used unlocked window to open those links. If no unlocked window exists, it should create a new one.

Aside from that change, locked windows would behave like any other window. You would still be able to manually open a link in a new tab, create new tabs, reorder tabs, or move tabs between windows.

For my work, I would probably keep all windows locked except the one I use to collect stuff I want to read.

I haven’t found a browser extension for Safari or Chrome that does this. I’m not even sure if the extension APIs in current browsers support this functionality. The same idea could also be applied to other apps that work with tabs, such as text editors.

David Owens recently [suggested a somewhat similar idea on Twitter](https://twitter.com/owensd/status/553349421174632450):

> An awesome OS X feature would be to "suspend" an entire Space. Easy to shutdown the work and resume it the next day.
> 
> [@owensd](https://twitter.com/owensd)
> 
> David Owens II
> 
> [June 9, 2015](https://twitter.com/owensd/status/553349421174632450)

1. In [ATP episode 96](http://atp.fm/episodes/96), John Siracusa talked about his approach to window management, to the amazement of his co-hosts:

  > I have 11 windows in Colloquy right now. In BBEdit I frequently have (…) 20 or 30 most of the time. In Terminal I usually have 8 or 9. Each of those windows has tabs in it. (…) I don’t have a lot of browser windows open now. I have 19 Safari windows open right now, tons of tabs in those windows. (…) How many Chrome windows do I have open? 12 Chrome windows.

  The segment starts at 1:30:23, it’s worth a listen. [↩︎](#fnref:1)
2. I configured my browser to open links in new tabs instead of windows. [↩︎](#fnref:2)
3. Is there a better word for this than locking? I can’t think of one. [↩︎](#fnref:3)
