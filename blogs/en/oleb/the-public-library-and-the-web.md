---
title: The Public Library and the Web
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/06/public-library-web/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e641242eb83ba88c'
translated: false
---

> 原文：[The Public Library and the Web](https://oleb.net/blog/2015/06/public-library-web/)　·　Ole Begemann

# The Public Library and the Web

Bret Victor in a [follow-up](http://worrydream.com/TheWebOfAlexandria/2.html) to his article titled [The Web of Alexandria](http://worrydream.com/TheWebOfAlexandria/):

> In [The Web of Alexandria](http://worrydream.com/TheWebOfAlexandria/), I suggested that some very stable and reliable media, DNA and print, owe their stability and reliability to replication and retention — every reader gets a copy, and every reader keeps their copy. The web, on the other hand, follows the strategy used for books before the printing press — put a single copy in an institution, allow readers to come visit, hope it doesn’t go up in smoke.

I’ve already linked to these articles in my [previous post](https://oleb.net/blog/2015/05/thoughts-on-google/), but I’d like to revisit Bret’s main theme: how can we make the web better as a permanent archive of knowledge? Currently, content disappears and URLs go out of date at an alarming rate. Again, it’s important to make the distinction between the web as a publication medium and the web as a communication medium or social network. I think we can all agree that the output of the former must be preserved, while there are good arguments for not keeping a permanent record of the latter.

The idea of preserving the web through replication (where everybody has a local copy) is intriguing, but seems infeasible considering the bandwidth and storage requirements. I’d like to propose something different.

The preservation of our collective knowledge is a public responsibility. It is too important to leave it to the whims of private corporations. I’d like to see governments get involved. As we transition from printed to digital media, public libraries should make the collection of digitally published knowledge their primary task. Every country should have its own [Internet Archive](https://archive.org/).

I’m not at all sure what form this should take. A traditional web crawler/search engine (including a cache in case content gets deleted) is one possibility. For books and other traditional media, many countries have [mandatory deposit](https://en.wikipedia.org/wiki/Legal_deposit) laws that require publishers to submit copies of every publication to a public institution. Why not establish something similar for digital publications? Content creators could be required to submit new content to the national library via an API for preservation.

Part of the appeal of the web as a publishing medium is the low entry barrier, so we have to be careful not to overregulate things. But I think such a requirement can be relatively painless. A standardized API would be implemented by every publishing system, from professional CMS to small blogging engines. It might even be enough to publish a full-text RSS feed to fulfill your obligations.

The question of what should be preserved is much harder to answer. Content from established media organizations and scientific articles is easy, but what about personal blogs? What about corporate web pages like the [product page for the newest Macbook](http://www.apple.com/macbook/)? Most tweets are surely part of the “conversational record”, but every so often [a tweet](https://twitpic.com/135xa) gains prolonged significance for the public and should be archived. The same is true for personal photos and videos.

I propose to start small with the uncontroversial sources and then expand from there. Alternatively, I can imagine a library that attempts to collect everything but has strict “forgettability” rules for content that does not get referenced by others, so that e.g. a tweet that nobody links to gets deleted after a few days or weeks.

URLs as a permanent identifier for a piece of content are clearly not reliable. An “official” Internet archive could remedy that by assigning its own URL to each piece and guaranteeing its permanence. But that may not even be necessary. For centuries, people have cited books and other publications by title and author name. That system would also work for a lot of web content. Ignore the URL and rely on search engines to find things.

Our imaginary public web archive has some of the same problems as the ancient library of Alexandria that Bret used as an example in his article. By introducing a single point of failure, we risk losing everything. But unlike the handwritten scrolls in Alexandria, a digital archive can be copied effortlessly. Official copies in multiple locations protect against technical and natural disasters. Ideally, copies should also be kept by non-governmental institutions (like universities) to protect against rogue governments.
