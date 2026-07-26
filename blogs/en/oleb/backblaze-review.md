---
title: Backblaze Review
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/10/backblaze/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c1b75e0f04b15f26'
translated: false
---

> 原文：[Backblaze Review](https://oleb.net/blog/2014/10/backblaze/)　·　Ole Begemann

# Backblaze Review

[Backblaze](https://www.backblaze.com/) is the second online backup service ([after CrashPlan](https://oleb.net/blog/2013/11/crashplan-experience/)) I have tried for a significant amount of time. Now that I have been using Backblaze for the past nine months, I believe I can make a fair evaluation of the service.

# Overview

Like CrashPlan, Backblaze offers unlimited storage for the fantastic price of $5 per month and computer. The Backblaze client allows you to specify your own private passphrase that is used to encrypt all your data before it leaves your computer. Backblaze claims they cannot decrypt the data in their data centers if you do this. (And hopefully [the NSA can’t break the encryption, either](https://www.schneier.com/blog/archives/2012/03/can_the_nsa_bre.html).)

Upload speeds to Backblaze have generally been much better for me than with CrashPlan from my location (Berlin). I’m on a 50/10 Mbit/s connection and I regularly see the Backblaze client utilizing the full upload bandwidth, with an average of about 4–5 Mbit/s in practice (= approximately 2 GB per hour).

# The Client Software

The Backblaze Mac client installs its GUI component as a panel in System Preferences. I’d much rather have a standalone app. The client is very Apple-like, purposely designed to get out of your way and give you as few options as possible.

The backup daemon works very unobtrusively. I never noticed it taxing the system in any way. Everything feels way faster than with CrashPlan’s client app. The four Backblaze processes that are running on my system while I’m writing this consume about 500 MB of memory (as reported by Activity Monitor), and that’s with a backup size of almost 2 TB (comprising 1.2 million files).

[![Activity Monitor screenshot showing the memory consumption of Backblaze processes](https://oleb.net/media/activity-monitor-screenshot-backblaze.png)](https://oleb.net/media/activity-monitor-screenshot-backblaze.png)

<sub>On my computer, all running Backblaze processes consume about 500 MB of memory.</sub>

Backblaze will back up your entire computer except the following by default:

- Some system folders, including directories one would conceivably like to back up, such as `/etc/`, `/usr/`, and `/Applications`. You can add some of your own folders to this list to exclude them from the backup, but there is no way to opt into backing up the system directories.
- Certain file types are excluded based on their file extension. The default list includes disk images (`.dmg`, `.iso`, `.sparseimage`) and virtual machine images among others. Can be customized freely.
- Files larger than 4 GB. This can be customized or turned off entirely.

[![Backblaze’s default list of excluded directories and file extensions](https://oleb.net/media/backblaze-exclusions-screenshot.png)](https://oleb.net/media/backblaze-exclusions-screenshot.png)

<sub>Backblaze’s default list of excluded directories and file extensions.</sub>

I generally like Backblaze’s lack of configurability. The best backup system gets out of your way and just does its job. I do question some of these defaults, though, especially the file size limit. When you find out that some of your home videos have never been backed up in the first place, it might be too late.

What I also would very much like to see from the Backblaze client is more and better _information_ about what’s going on with my backup. Which files are already backed up and which aren’t? Can I be sure the app has noticed and uploaded all changes on an external drive so I can unplug it again?

The app does not answer these questions. The web interface on [backblaze.com](https://www.backblaze.com/) has a little more information, but verifying that a certain file has been backed up is inconvenient and requires you to enter your private encryption passphrase into the browser, something I’d rather not do unless I needed to. Support for the upcoming [Finder Sync extension](https://developer.apple.com/library/prerelease/mac/documentation/General/Conceptual/ExtensibilityPG/Finder.html#//apple_ref/doc/uid/TP40014214-CH15-SW1) in Yosemite would also help with transparency. I hope Backblaze is working on it.

**There is this saying that a backup system that requires manual work is not a reliable backup. That’s Backblaze if you have to deal with external drives.**

# External Drives

One of Backblaze’s biggest downsides for me is its policy towards external hard drives. An unlimited number of external drives is included in your “unlimited” backup allowance, provided that the drive gets attached to your computer at least every 30 days. If Backblaze does not see a drive for more than 30 days, it considers it gone and deletes the data from your backup.

We live in a time where almost nobody owns a computer with multiple internal drive bays anymore. Laptops generally come with smallish and often non-upgradeable SSDs these days, which means that the internal storage capacity of the average computer may actually have gone down in recent years. At the same time, the amount of storage our photo and video collections take up is constantly growing. All this means that many users have more important data than they can fit on their laptop’s internal storage. External drives have become a necessity, not just for local backup purposes.

As an example, the amount of data I have that I consider important enough to back up (about 2 TB) is more than I can fit on any laptop currently sold by Apple. So I have an external hard drive with archived data. I don’t need to access this data regularly, but I still have to remember^[1](#fn:1) to connect it regularly to my computer so that Backblaze won’t forget it. And it’s not enough to attach the drive for just a few seconds. Even if no data on the drive has changed, you have to give the Backblaze app enough time to rescan it. How much time is enough, you ask? I don’t know because the app doesn’t indicate when it’s done, so you better leave it attached for a number of hours at least. [This is from Backblaze’s FAQ](https://help.backblaze.com/entries/20200433-Backing-up-External-Hard-Drives/#unplugged):

> When an external drive is plugged back in, it may take Backblaze a minute or two hours to schedule the files on the external drive to be backed up online.

Also, what happens when you travel for several weeks and you left the external drive at home? Even if you’re lucky to not lose any data, I bet you won’t enjoy having to upload hundreds of gigabytes _again_.

In my opinion, the 30-day limit for external drives is not appropriate for an age of small SSDs. I would happily pay twice the monthly amount to get rid of it.

There is this saying that a backup system that requires manual work is not a reliable backup. That’s Backblaze if you have to deal with external drives.

# Metadata

Please read Michael Tsai’s excellent overview in [What Backblaze Doesn’t Back Up](http://mjtsai.com/blog/2014/05/22/what-backblaze-doesnt-back-up/):

> My other concern is that Backblaze doesn’t actually back up everything. It fails all but one of the Backup Bouncer tests, discarding file permissions, symlinks, Finder flags and locks, creation dates (despite claims), modification date (timezone-shifted), extended attributes (which include Finder tags and the “where from” URL), and Finder comments.

As noted by Michael, Backblaze’s stance on this situation is dismissal, which I find very problematic (emphasis in the original):

> I think it’s misguided and borderline nonsensical. True, Backup Bouncer tests some rather esoteric features, but Backblaze fails the basic tests, too. It would be one thing to say that there’s a _limitation_ whereby dates, tags, comments, etc. aren’t backed up, but they’re actually saying that these _shouldn’t_ be backed up. As if products that _do_ back them up are in error. So presumably Backblaze doesn’t consider this a bug and won’t be fixing it.

# Restores

The Backblaze client has no restore functionality. All restores (be it a single file or your entire archive) start on the website and require you to send your private passphrase to Backblaze’s servers where the data will be decrypted before you can download it. Needless to say, this is not at all ideal from a security perspective.

# Confusing Behavior When Moving Files

Here is something that I tripped over several times, requiring me to reupload several hundred gigabytes that had already been backed up but got deleted from the Backblaze servers.

Say you have a bunch of large files (which have already been backed up to Backblaze) on your internal drive that you want to move to an external drive. The Backblaze daemon does not recognize that the files are being moved. As far as it is concerned, they have been deleted from the internal drive, and it will delete the files from the backup accordingly. Deleted files remain on Backblaze’s servers for 30 days, however, so when the backup daemon picks up the “new” files on the external drives (which can take a few hours) and starts to upload them, the service is smart enough to recognize that the data is already stored on Backblaze’s servers so it does not upload them again. So far, so good.

The process seems to break down when your initial backup is not yet finished. The moved files which the daemon discovers as new seem to get added to the end of the backup queue. Since it can take many weeks to finish your initial backup, chances are that it will take the new old files more than 30 days to reach the front of the queue, by which time the originally uploaded data will be deleted and you have to reupload.

This may sound like an obscure limitation that is largely irrelevant in real life, but it means you won’t be able to move data between drives without risking the loss of your backup state for weeks or potentially months (until the initial backup is complete). I feel that Backblaze could solve this better by monitoring file system changes more directly.

# Conclusion

I’m sticking with Backblaze for now, mainly for its unobtrusiveness and convenience. I still haven’t found the perfect online backup service, however.

1. Backblaze does send reminder emails about missing drives after 14, 21, and 28 days, so technically I don’t have to remember it. It’s still a nuisance. [↩︎](#fnref:1)
