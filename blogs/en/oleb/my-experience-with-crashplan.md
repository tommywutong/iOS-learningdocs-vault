---
title: My Experience With CrashPlan
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/11/crashplan-experience/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:43281dafaa55c19b'
translated: false
---

> 原文：[My Experience With CrashPlan](https://oleb.net/blog/2013/11/crashplan-experience/)　·　Ole Begemann

# My Experience With CrashPlan

I signed up for [CrashPlan](http://www.crashplan.com), the online backup service, almost a year ago, in November 2012.[1](#fn:1) Now that the time has come for renewal, I have evaluated my experience with CrashPlan and decided to cancel my subscription. I’ve simply had too many problems with the service.

This is a sad realization for me because the (non-monetary) investment I have made in CrashPlan is considerable: the initial upload of my full backup set (\> 1 TB) took months and I hate to lose this investment.

# The CrashPlan App Sucks

The problem I have with CrashPlan are mostly related to the CrashPlan client app.

## Java

First of all, it’s Java. I realize this is already a deal-breaker for many and it probably should be. Requiring Java for an essential app that is running in the background all the time is not just an inconvenience, it is also another thing that can break.[2](#fn:2)

The CrashPlan folks have been saying on Twitter for more than year that [a native Mac client is in the works](https://twitter.com/crashplan/status/243065781888364545), but they (wisely) decline to give a release date.

## Synchronizing

The biggest problem of the CrashPlan client is that it seems really slow.[3](#fn:3) The app regularly[4](#fn:4) re-scans the directories in your backup set in order to to check for files that have to be backed up (in case the on-the-fly monitoring misses a file that has changed) and to identify files that can be de-duplicated (if you backup multiple identical files, they will only be stored once).

On my machine with my admittedly large backup set (1.3 TB across almost 2 million files[5](#fn:5)), this “Synchronizing” process takes forever: anywhere from 12 to 24 hours is common. When I contacted support about this, they acknowledged that this behavior was not expected, but the recommendation to increase the memory allocation for the app (apparently you have to do this manually for a Java app) to up to 2 GB did not have any effect.

The re-scanning also occurs whenever you modify your backup set. Even a simple action such as removing a folder from your existing set of directories to back up causes the CrashPlan app to re-scan everything. I have no idea why. The app’s UI is not really clear what happens while the synchronization is in progress.

If backups occur during this phase, the app does not say so. Overall, the app too often gave me the feeling that I was not in control of the backup process.

## Example

Let’s take a fairly common scenario: say I want to download and backup the WWDC 2013 videos.

1. Since there is not enough free space on my internal drive, I need to free some up first. So let’s connect an external hard drive and move some stuff to it from my internal disk.
2. If I would just move files that are currently included in the CrashPlan backup to the external drive, CrashPlan would delete them from the backup. Since I don’t want to lose any of my existing backup, I first have to add the external hard drive to my CrashPlan backup set.
3. As mentioned earlier, the CrashPlan client now starts to rescan all files in my entire backup set! In my case, this will take 12+ hours. It is not clear whether I can begin moving stuff to the external drive during this time or not. So I wait, just to be safe.
4. Meanwhile, let’s start the download. Downloading 300 gigs of videos takes some time, too, after all.
5. hundreds of gigabytes to my backup because it does not recognize immediately that the files are being moved. I start to wonder, did I do anything wrong? Will I have to re-upload these files?
6. Since the app backs up the newest files first (which is generally a good idea), it starts backing up the videos I just downloaded. Only when that process is finished after a week or two, it will start to recognize that the files I moved to the external drive have already been backed up. Can I safely eject the external drive during that time and re-attach it later or would this cause the backup info to get lost? I don’t know, and the app doesn’t tell me.

Nowhere does the CrashPlan app show you which files are already backed up and which are still missing. Compare this to the Dropbox app, which makes it quite clear what it is currently working on.

# Upload Speed

Upload speeds to the CrashPlan data center were quite slow for me. I’m on a 10 Mbit/s upstream but uploads to CrashPlan were rarely faster than 1 Mbit/s and often much slower, even though I regularly see upload speeds that fully utilize my bandwidth to other sites in the US. [Marco Arment had a similar experience](https://twitter.com/marcoarment/status/227591023101108225). There are others whose upload speeds to CrashPlan are great, though, so I don’t want to generalize this experience.

Since I did not evaluate the upload speed I would get with other online backup services, this was not a factor in my decision to abandon CrashPlan.

# Conclusion

I would love to be able to continue using CrashPlan, if only because it would save me the pain of uploading my stuff to another provider in the future. Before I do that, I will make sure to better evaluate their service.

Signing up for CrashPlan was a quick decision because I could essentially get a year for free and I thought it wouldn’t hurt to try it out. Had I considered the considerable non-monetary investment I had to make in order to evaluate whether CrashPlan was the right service for me, I would have taken more time to decide.

If CrashPlan manages to improve their client app and resolves the problems I noted above, I’d happily recommend the service. I especially like their policy for backing up external drives with no strings attached (most other services require you to connect an external drive at least once a month or so to keep it backed up). If I could freeze my subscription until the Mac client is ready, I would definitely re-evaluate the service when the native client is ready. Since that is not possible and I’d have to re-upload all my stuff, I probably won’t be coming back.

**Update December 18, 2013:** A reader pointed me to an article titled [Speeding up CrashPlan Backups](http://networkrockstar.ca/2013/09/speeding-up-crashplan-backups/) from September 2013. In it, the author describes how to disable CrashPlan’s file deduplication feature by editing a configuration file. This single change caused a tremendous increase in the author’s average upload speed by removing a processor usage bottleneck.

Although I had not tried this fix on my machine and I would have loved to see higher upload speeds during my usage of CrashPlan, I doubt it would have made a difference to my fundamental problem: the frustrating endless directory re-scanning I outlined above. In fact, a comment on the article mentions that analyzing files seems to take about twice as long as it did before disabling dedupe.

I think what we are seeing are simply multiple serious issues with the CrashPlan software.

**Update October 15, 2014:** Also check out [my Backblaze review](https://oleb.net/blog/2014/10/backblaze/).

1. At the time, CrashPlan had a special offer that allowed me to pay just $3 for 12 months, so signing up was a no-brainer. As it turns out, I should have taken more time to evaluate the service and the competition, even if that meant not getting the special offer. [↩︎](#fnref:1)
2. After upgrading to Mavericks, the CrashPlan GUI client regularly freezes on launch on my machine even after I reinstalled Java and the CrashPlan app according to the support documents. [↩︎](#fnref:2)
3. And no, I don’t attribute that to the fact that it’s written in Java. You can write fast and slow apps on any technology stack. [↩︎](#fnref:3)
4. By default, this re-scan occurs every 24 hours, but that time can be adjusted. [↩︎](#fnref:4)
5. I could not identify a clear pattern what variable was more to blame for the long scanning phases: the amount of data or the sheer number of files. [↩︎](#fnref:5)
