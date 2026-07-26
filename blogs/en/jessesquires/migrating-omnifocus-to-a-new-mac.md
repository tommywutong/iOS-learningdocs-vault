---
title: Migrating OmniFocus to a new Mac
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2021/03/31/migrating-omnifocus-to-a-new-mac/'
original_language: en
published: 2021-03-31
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:58ab418c3420f73a'
translated: false
---

> 原文：[Migrating OmniFocus to a new Mac](https://www.jessesquires.com/blog/2021/03/31/migrating-omnifocus-to-a-new-mac/)　·　Jesse Squires

One aspect of using OmniFocus involves maintaining an archive of your data (if you choose). Over time — think _years_ of using OmniFocus as your main task management tool — your local database of projects and tasks will grow very large, because OmniFocus keeps a record of everything you have completed or dropped. You can think of it as archiving your emails instead of putting them in the trash.

As you can guess, a very large database results in a very slow OmniFocus. Periodically, the app will remind you to [reduce the size of your database](https://support.omnigroup.com/reduce-size-omnifocus-database/) by moving completed or dropped items to your archive, which does not sync across devices (which also speeds up syncing). You probably do not need to actively sync Todo items that you completed over a year ago. However, if you are like me, it is nice to know this old data is kept somewhere, just in case you need it later. You can access it via `File > Open Archive`.

Setting up OmniFocus on a new Mac is as simple as installing the app and syncing for the first time. However, if you want to preserve your years-old archive, there are a few extra steps.

**On your old Mac:**

1. Go to `File > Show backups in Finder`
2. This will open a Finder window at `~/Library/.../Application Support/OmniFocus/Backups`
3. At the same level as `Backups/` you will find your archive bundle, `Archive.ofocus-archive`
4. Copy the archive to a thumb drive, or some other temporary location that you can access from your new Mac
5. If you want, you can also copy all of your backups (the entire `Backups/` directory)

**On your new Mac:**

1. Go to `File > Show backups in Finder`
2. Place the archive and backups in the same location as your old Mac, `~/Library/.../Application Support/OmniFocus/`

You can verify that moving the archive was successful by trying to open it via `File > Open Archive`.

Strangely, I could not find any “official” instructions on [Omni’s support site](https://support.omnigroup.com) for this. All I could find was the guide on [reducing the size of your database](https://support.omnigroup.com/reduce-size-omnifocus-database/). However, I have confirmed that these steps are correct with the Omni Support team.
