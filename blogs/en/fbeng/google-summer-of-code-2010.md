---
title: Google Summer of Code 2010
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2010/10/21/ios/google-summer-of-code-2010/'
original_language: en
published: 2010-10-21
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5309c513c821f734'
translated: false
---

> 原文：[Google Summer of Code 2010](https://engineering.fb.com/2010/10/21/ios/google-summer-of-code-2010/)　·　Meta Engineering — iOS

This summer we participated in [Google Summer of Code](http://code.google.com/soc/) (GSoC) for the first time and wanted to share an update on the progress our students made. GSoC is in its sixth year and exists to encourage university students to spend their summer coding for an open source / free software project. The students in turn are awarded a stipend which definitely makes this a cool summer job.

Unlike most organisations participating in the program, we have a number of [open source projects](http://developers.facebook.com/opensource/) rather than just a single project. This meant that we accepted a few students to work across open source projects which we actively contribute to in addition to projects that we’ve released.

We received many applications from students all over the world who were excited to spend their summer working on adding new features to [HBase](http://hbase.apache.org), [HipHop for PHP](http://github.com/facebook/hiphop-php), [Scribe](http://github.com/facebook/scribe), [Three20](http://github.com/facebook/three20) and [XHP](http://github.com/facebook/xhp). While some projects are still working on merging their changes, by the end of the summer:

- [Chongxin Li](http://github.com/lichongxin) designed and coded some initial support for snapshotting in Apache HBase that will allow for easier recovery from data loss.
- [Hui Chen](http://github.com/huichen) ported HipHop for PHP to 32-bit operating systems, implemented some missing extensions, and helped improve the stability of the project. All of these changes are already in the core and some are running on the very web servers you’re using right now.
- [Souvik Roy](http://github.com/crozzfire) added regular expression support to Scribe for category names and implemented some unit tests into the existing system which makes future development easier.
- [Chih-Wei Lee](http://github.com/dlackty) spent his time working on adding iPad support to Three20, the UI library we released which is used by many iPhone applications. Some of this support has been merged into trunk and the rest is being reviewed.
- [Avgoustinos Kadis](http://github.com/phidias) added support for new HTML5 elements to XHP. This allows PHP developers to write their HTML once and have XHP handle gracefully degradation from native HTML5 elements to JavaScript implementations in older browsers. (We wrote about how [we’re using HTML5](http://www.facebook.com/note.php?note_id=438532093919) last week.)

This weekend we’ll be heading to Google’s campus along with over two-hundred other mentors from participating projects for a BarCamp style event to share our experiences and talk about open source in general.

We really enjoyed having the opportunity to take part in Summer of Code and want to thank these five students for their awesome work!

_Scott, an engineer on our open source team, likes anything related to summer and code!_

(As part of Summer of Code, Google gives both the student and mentoring project a stipend. We’ve asked that what would be given to us as the mentoring organization be donated to the Apache Software Foundation instead.)
