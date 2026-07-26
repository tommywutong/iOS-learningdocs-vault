---
title: AppleScript to export open Safari tabs to OmniFocus
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/01/14/apple-script-to-export-open-safari-tabs-to-omnifocus/'
original_language: en
published: 2020-01-14
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fea3ab6c5b170297'
translated: false
---

> 原文：[AppleScript to export open Safari tabs to OmniFocus](https://www.jessesquires.com/blog/2020/01/14/apple-script-to-export-open-safari-tabs-to-omnifocus/)　·　Jesse Squires

I love OmniFocus. It is an indispensable app for me and a _great Mac app_. For managing and organizing to-do lists and personal projects, there is nothing better. Being a great Mac app means adopting behaviors that users expect, conforming to macOS UI/UX paradigms, and for the truly great mac apps it means being scriptable. I want to share two AppleScripts that I wrote for OmniFocus to automate one of my common workflows.

I will eventually write a blog post on my OmniFocus “philosophy”, how I use it, and why it is the best app for to-do’s and projects. But, for now I will be brief.

For me **everything** goes through OmniFocus. Some people email themselves to track things, some people keep 50 tabs open in their browser to “read later” — not me. If there is something I need to do or remember, it goes into OmniFocus to get organized, prioritized, and/or scheduled. If I need to follow-up on an email I will create an item in OmniFocus then move the email out of my inbox. If I have many tabs open in Safari but not enough time to read them, they get sent to OmniFocus — and that is what this post is about.

I am often in a situation where I have a number of tabs open in Safari. I may be reading a collection of blog posts about how to implement a new iOS API, or I may be researching something I need, like new running shoes. I cannot always complete the task in that moment and I want to revisit it another time, or I want to save all the links for later. If they stay in Safari (even as bookmarks) they will be lost forever to me. I need to save them into OmniFocus. So I wrote an AppleScript to do that. Well, two scripts actually.

The first script will collect all of the open tabs in the front-most Safari window and create a new inbox item for each tab. For each item, the title is set to the web page title and the notes field contains the full URL. Suppose we have 5 tabs open: omnigroup.com and four other tabs for Omni’s different apps. Here is the result:

![OmniFocus inbox](https://www.jessesquires.com/img/blog/omnifocus-tabs.png)

<sub>OmniFocus inbox with an item for each Safari tab</sub>

The second script is similar, with a slight variation. It creates a single inbox item instead of one. The item title follows the pattern “`First_Tab_Name` + `N` other tabs”, for example “The Omni Group + 4 other tabs”. The item notes field contains a list of all the tabs, including the title and URL. Here is the result:

![OmniFocus inbox](https://www.jessesquires.com/img/blog/omnifocus-tabs-single-item.png)

<sub>OmniFocus inbox with a single item for all Safari tabs</sub>

Having these two variations is convenient and the one that I choose depends on the context of what I am doing. When the scripts finish, they post a notification.

![AppleScript notification](https://www.jessesquires.com/img/blog/omnifocus-notif.png)

<sub>AppleScript notification</sub>

I have found these to be extremely useful and they save me a ton of time. If you are an OmniFocus user, give them a try. All of [the code is on GitHub](https://github.com/jessesquires/safari-tabs-to-omnifocus). Enjoy!
