---
title: The Case for Selective Restore from iCloud Backups
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/07/the-case-for-selective-restore-from-icloud-backups/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:be8be2517365c408'
translated: false
---

> 原文：[The Case for Selective Restore from iCloud Backups](https://oleb.net/blog/2012/07/the-case-for-selective-restore-from-icloud-backups/)　·　Ole Begemann

# The Case for Selective Restore from iCloud Backups

You probably all know that the App Store delivered corrupt binaries for many recently updated apps to people’s iOS devices last week. (If you don’t, read [Marco Arment’s blog post on the topic](http://www.marco.org/2012/07/04/app-store-corrupt-binaries).) It took Apple three days to fix the problem (which was entirely on their side and no fault of the developers of the affected apps). To their credit, when Apple introduced the fix they did the right thing by (1) ~~deleting all customer reviews~~ for the corrupted version and (2) by [triggering an update for the affected apps](http://www.marco.org/2012/07/06/apple-repushes-corrupt-binaries). That way, users can download the fixed version without having to delete the app first.

**Update July 13, 2012:** [As Marco Arment reported](http://www.marco.org/2012/07/06/apple-repushes-corrupt-binaries) (and I misread), Apple did not delete the reviews. They just got reset and hidden by treating the fixed binary as a new version.

# Deleting an App Deletes its Data

![iOS 5.1.1 showing a warning about app deletion](https://oleb.net/media/ios-springboard-delete-app-warning.png)

In the meantime, however, I am sure many users thought the problem was somehow related to their device or maybe due to a temporary hickup in the installation process that could be fixed by deleting and reinstalling the app. The (many) users who tried this approach would not only discover that it didn’t fix the problem, it also introduced a new one: when an app is deleted, the OS deletes all the app’s data along with it.

Granted, iOS does warn the user of this consequence. That does not make it a good user experience, though. I can imagine many situations where a user might grudgingly accept some data loss (e.g., if the lost data could be recovered by investing time, as would be the case with an app’s settings or cached data) if she hopes that she can fix a different problem that way.

# Apple Could Offer to Restore Data from iCloud Backup

App developers can make this a better experience for their users by storing all their data in iCloud or on their own servers. And we should definitely do so if it is feasible. But for apps that don’t or can’t implement this, Apple could help, too. After all, if users have chosen to backup their device to iCloud, Apple still has a copy of that deleted app’s data on their servers.

Here’s an idea: if a user reinstalls an app she has recently deleted, what if Apple would offer her to restore that app’s data from her most recent iCloud backup? I think this would be a very cool feature. After all, a backup you can’t selectively restore from is significantly less useful. This solution could not only help prevent data loss with issues like the one last week, it would also give users a way to retrieve their data when a bad app update corrupts the existing data.

I doubt Apple is interested in introducing such a feature. Their position is probably that all developers should adopt iCloud – problem solved. Nevertheless, I think it’s a nice idea.
