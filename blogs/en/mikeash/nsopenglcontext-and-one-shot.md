---
title: NSOpenGLContext and one-shot
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/nsopenglcontext-and-one-shot.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1a8711339b6c9ca0'
translated: false
---

> 原文：[NSOpenGLContext and one-shot](https://www.mikeash.com/pyblog/nsopenglcontext-and-one-shot.html)　·　mikeash.com Friday Q&A

Posted at 2006-02-23 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Fluid Simulation for Dummies](https://www.mikeash.com/pyblog/fluid-simulation-for-dummies.html)  
Previous article: [What Every Programmer Should Know](https://www.mikeash.com/pyblog/what-every-programmer-should-know.html)  
Tags: [advice](https://www.mikeash.com/pyblog/?tag=advice) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [opengl](https://www.mikeash.com/pyblog/?tag=opengl)

NSOpenGLContext and one-shot

by [Mike Ash](https://www.mikeash.com/)

The "secret" is to turn off the "One shot" checkbox for your window in Interface Builder. This setting basically destroys your window while it's hidden, including while it's miniaturized to the Dock. Destroying the window breaks the link between your context and the window, resulting in it blanking out as it flies toward the Dock. Disabling this checkbox makes sure the window always sticking around, so that your OpenGL content looks indistinguishable from the rest.  
  
 I discovered this in this mailing list post: [http://lists.apple.com/archives/mac-opengl/2003/Apr/msg00132.html](http://lists.apple.com/archives/mac-opengl/2003/Apr/msg00132.html)

**No comments:**

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

No comments have been posted.

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
