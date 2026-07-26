---
title: 'Why Kreya isn''t open source | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/why-kreya-isnt-open-source/'
original_language: en
published: 2022-03-01
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5cae67ddd7da0c0c'
translated: false
---

> 原文：[Why Kreya isn't open source | Kreya](https://kreya.app/blog/why-kreya-isnt-open-source/)　·　Kreya Blog

One question we are often asked is why Kreya is not open source. We explain our thoughts and considerations in this blog post.

## We love open source

First off, we are huge fans of open source projects. For example, Kreya uses the open source scripting language [Scriban](https://github.com/scriban/scriban). When we felt that some features (`math.random` and `math.uuid`) were missing, we simply opened a pull request, which was gratefully accepted. This shows the obvious benefits for the repo maintainer.

As another example, we were often glad that the .NET runtime (the "backend" of Kreya is written in C#) is open source. Even though the .NET documentation is pretty good, it is very useful to be able to look up the actual implementation, in case something isn't quite clear.

In addition, with the release of [Mapperly](https://github.com/riok/mapperly), we do have an open source project of our own, with which we try to contribute back to the open source community.

## Desktop apps are a special case

That said, we do have some arguments against open sourcing Kreya. A lot of our competitors are completely closed source or have components (eg. remote server sync) that are closed source too. The same applies to a lot of other desktop apps, such as IDEs or Microsoft Office.

Often, as in our case, the reasoning behind that is money. With the upcoming 1.8 release of Kreya, we plan to include a paid version (don't worry, all existing and most future features remain free). As Kreya doesn't rely on any closed source server components, open sourcing Kreya would allow users to simply build the paid version themselves, removing the license check from the code. Even worse, a fork could do that semi-automatically for each new Kreya version and release the binaries for everyone to download. This is basically what happened to [Franz](https://github.com/meetfranz/franz), which was forked into the completely free [Ferdi](https://github.com/getferdi/ferdi).

As we plan to earn some money from the paid plan to support the development of Kreya (in which we invested way over 1000 hours), having a completely free fork would be unacceptable to us. Of course, we could devise a license that restricts these usages, which brings us to the next point.

## Licensing is hard

Licensing an open source project is really hard. Slamming an MIT license on the Kreya source code would eventually catch up with us at some point. [Look at what happened to Elastic when they used a too permissive license](https://www.elastic.co/blog/why-license-change-aws). Everybody can legally use your software and take advantage of it, even though it may have not been your intent to allow it to such a degree.

And even if we created or found an applicable license, who would enforce it? We are a small team of four software engineers from Switzerland and we have neither the knowledge nor the means to report license violators. Paying lawyers to do that for us would be far more costly and complicated than keeping Kreya closed source.

## Open sourcing is final

Once you open source a project, it is out in the open. Sure, you can delete the project, but from a legal standpoint of view, the released code is still usable under the specified license, should any backups or forks exist. Switching an open source project to closed source or changing it to a much more restrictive license would probably also result in a lot of backlash from the community.

## Forever closed source?

Our decision isn't set in stone. We recognize the benefits of open sourcing Kreya, but currently we favor keeping Kreya closed source.
