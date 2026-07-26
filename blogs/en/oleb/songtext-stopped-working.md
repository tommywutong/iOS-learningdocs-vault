---
title: Songtext Stopped Working
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/08/songtext-stopped-working/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fd95934446ee6644'
translated: false
---

> 原文：[Songtext Stopped Working](https://oleb.net/blog/2009/08/songtext-stopped-working/)　·　Ole Begemann

# Songtext Stopped Working

[![Songtext displaying error message](https://oleb.net/media/songtext-stopped-working-screenshot-222x320.png)](https://oleb.net/media/songtext-stopped-working-screenshot-222x320.png)

<sub>Songtext displaying error message.</sub>

As of this morning, Songtext is no longer working. [LyricWiki](http://lyricwiki.org), the site Songtext obtained its lyrics from, was required by music publishers to cripple their [API](https://en.wikipedia.org/wiki/API) in such a way that apps like Songtext [no longer have direct access to the lyrics](https://groups.google.com/group/lyricwiki-api/browse_thread/thread/733ccd919d654040). This effecticely breaks Songtext and many other iPhone lyrics apps that also used LyricWiki as their source.

I am very sorry to all users but at the moment there is nothing I (or LyricWiki) can do about this. I would like to thank the guys at LyricWiki for their efforts in providing an API in the first place. And special thanks for providing users of Songtext and other apps with a clear error message that should minimize support requests for app developers:

> Unfortunately, due to licensing restrictions from some of the major music publishers we can no longer return lyrics through the LyricWiki API (where this application gets some or all of its lyrics). The lyrics for this song can be found at the following URL: … (Please note: this is not the fault of the developer who created this application, but is a restriction imposed by music publishers themselves.)

I sincerely hope that the music publishers are working on a solution that would allow for the existence of lyrics apps in the future. The popularity of some of these apps clearly shows that there is a demand. Instead of only crippling third-party solutions, they should provide their own APIs (with their own licensing model if they feel they need to be compensated).
