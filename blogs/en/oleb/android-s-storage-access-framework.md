---
title: 'Android''s Storage Access Framework'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/11/androids-storage-access-framework/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b39516825d8584d9'
translated: false
---

> 原文：[Android's Storage Access Framework](https://oleb.net/blog/2013/11/androids-storage-access-framework/)　·　Ole Begemann

# Android's Storage Access Framework

[![Opening a document with Android's Storage Access Framework](https://oleb.net/media/android-storage-access-framework.jpg)](https://oleb.net/media/android-storage-access-framework.jpg)

<sub>Opening a document in Android's Storage Access Framework. Image: [Google Developer Website](https://developer.android.com/about/versions/kitkat.html#44-storage-access).</sub>

One of the most exciting new features in Android 4.4 is the [Storage Access Framework](https://developer.android.com/about/versions/kitkat.html#44-storage-access). If Apple were to introduce a similar feature in a future iOS version, I believe it has the potential to bring the platform a major step forward. Sadly, given Apple’s current iCloud strategy, I’m not holding my breath for it to happen.

# What Is It?

The Storage Access Framework (SAF) provides Android users with a unified user interface to all kinds of document storage services and locations. All that a cloud service like Dropbox has to do to integrate with the framework, is to deliver a so-called [document provider](https://developer.android.com/guide/topics/providers/document-provider.html) with their existing Android app. The document provider is a component that provides the SAF with the capability to access the files stored with the service from any app that supports it.

Although the API is based on files, it is conceivable that not only traditional cloud storage providers integrate with the SAF. Services like Flickr or Facebook could also expose their photo or video libraries in a way that is compatible with the SAF approach.

And it is not limited to cloud storage, either. The Storage Access Framework also supports local storage on the device’s file system or SD cards.

# User Choice

Apps that integrate with the SAF allow their users to open and store documents regardless of where they are stored. I expect document providers for all kinds of services to be available shortly, giving users complete control over where they want to store their data. Regardless whether you use Dropbox, whether you prefer your own private cloud storage based on [BitTorrent Sync](http://www.bittorrent.com/sync) or if you have set up a private SFTP or WebDAV server to better hide your data from the NSA, you will have access to your documents from all your apps.

Users don’t have to make compromises anymore because their favorite apps don’t support their storage preferences. Contrast this with the current situation on iOS where most apps just offer iCloud or Dropbox storage, if at all.

# A Feature for iOS

The SAF UI is like a cloud edition of Windows Explorer or the OS X Finder, without most of the drawbacks of [traditional file system navigation](https://oleb.net/blog/2012/06/steve-jobs-on-the-file-system/). Apps remain the face of the OS, as is the case on today’s mobile platforms. The file and folder hierarchies the user sees are fairly short, only containing documents the user has created or placed there himself.

If Apple added a feature like the Storage Access Framework to a future iOS version, it would elegantly solve at least two problems:

- The lack of a user-accessible (part of the) file system, making document sharing between apps much harder than it should be.^[1](#fn:1)
- The downsides of iCloud document storage, namely platform dependence and compartmentalization (each app can only access its own documents).

Given Apple’s strategy with iCloud, I don’t believe this will happen in the foreseeable future. The company is definitely not interested in dismantling platform dependencies, and the strict sandboxing of iCloud storage containers seems to be an important privacy and security feature in Apple’s eyes.

I feel that Apple will have to abandon this reasoning at some time, though. Sharing files between apps is too important a feature to disallow it on the grounds of security – especially since versioning and undelete functionality^[2](#fn:2) could mitigate most of the risks. I hope Apple will reevaluate its strategy eventually.

1. The current system using URL schemes or the “Open In…” feature in iOS doesn’t allow true document _sharing_ between apps. Files are always _copied_ from one app’s sandbox to another. [↩︎](#fnref:1)
2. Either built into the operating system or as part of the feature set of the storage providers. For instance, Dropbox already has versioning and undelete features. [↩︎](#fnref:2)
