---
title: Setting up default community health files on GitHub and crafting a thorough Contributing Guide for any open-source project
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/01/24/github-default-community-health-files/'
original_language: en
published: 2020-01-24
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6800d4d076046abc'
translated: false
---

> 原文：[Setting up default community health files on GitHub and crafting a thorough Contributing Guide for any open-source project](https://www.jessesquires.com/blog/2020/01/24/github-default-community-health-files/)　·　Jesse Squires

Every open-source author, maintainer, and contributor knows the importance of fostering a positive environment for collaboration and providing adequate resources for folks to seek help and contribute in a meaningful way. These resources include providing a Code of Conduct, a Contributing Guide, issue templates, and more. GitHub refers to this collection of documents as community health files, and they have been slowly improving their support for them. I recently spent some time creating defaults for these files, including crafting a completely new Contributing Guide for all of my projects.

Previously, it was necessary to include copies of community health files in every repository individually. You would commit your `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, issue templates, pull request templates, and more to a `.github/` directory at the root of your repository. The problem is that most of these files are usually the same (or very similar) for every project.

Instead, for organizations and user accounts on GitHub, you can create [default community health files](https://help.github.com/en/github/building-a-strong-community/creating-a-default-community-health-file) in a repository called `.github`, and those files will be inherited for _all_ of your projects, unless overridden. For example, I have created [`jessesquires/.github`](https://github.com/jessesquires/.github). By placing a [`CODE_OF_CONDUCT.md` in the root of this repository](https://github.com/jessesquires/.github/blob/master/CODE_OF_CONDUCT.md), _every single public repository_ for my user account now has a Code of Conduct. That is awesome. It saves so much time and removes the tedious task of potentially updating this health file _for every project individually_.

I am not sure how long this feature has existed. I know it has been available for organizations for some time, but I only recently realized it works for user accounts too. I would highly recommend adopting this for your GitHub account or organization. There is only one bug that I have run into. Adding [default issue templates does not work for user accounts](https://github.community/t5/How-to-use-Git-and-GitHub/Default-community-files-ignores-issue-templates/m-p/43809). It does work for organizations, however.

I have put a lot of effort into creating these default community health files — in particular, the [Contributing Guide](https://github.com/jessesquires/.github/blob/master/CONTRIBUTING.md) and [Support Guide](https://github.com/jessesquires/.github/blob/master/SUPPORT.md). They are the result of my entire experience in open-source and what I think is best for projects to succeed. I also borrowed ideas from other prominent open-source projects and communities. My goal was to create these documents in a way that they can be widely applicable — not only for my own projects, but for others as well. I highly encourage you to take a look. You are free to use them wholesale for your own projects, or use them as a starting point and remix them for your own needs. 🖤
