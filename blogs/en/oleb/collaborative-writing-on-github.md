---
title: Collaborative Writing on GitHub
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/02/collaborative-writing-on-github/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:556813c6e0bc2bef'
translated: false
---

> 原文：[Collaborative Writing on GitHub](https://oleb.net/blog/2016/02/collaborative-writing-on-github/)　·　Ole Begemann

# Collaborative Writing on GitHub

I was involved as an editor in several collaborative writing projects in the past year: I edited two [objc.io issues](https://www.objc.io/issues/), and I was the technical reviewer for the [Core Data](https://www.objc.io/books/core-data/) and [Advanced Swift](https://www.objc.io/books/advanced-swift/) books. I’d like to tell you a bit about my experiences.

# The process

The editing process for the books worked like this: The authors would write chapters in [Markdown](http://daringfireball.net/projects/markdown/) and push directly to a private repository on [GitHub](https://github.com). I would then submit a pull request with my edits and additional comments or questions. For subsequent changes to chapters after the first review, the authors would open additional pull requests and give me the chance to push additional edits or post comments before merging.

Overall, this setup worked well for us. The actual collaborative editing process may have been easier with tools like [Google Docs](https://www.google.com/docs/about/) or [Quip](https://quip.com),^[1](#fn:1) but the benefits of having all the content in plain text files in a directory^[2](#fn:2) in the file system are huge for automating the build process. Chris and Florian wrote scripts to check the sample code for compile errors, find broken links, and build the final book PDF, for example.

# GitHub

Once you’ve settled on plain text files in a directory, using GitHub for issues and pull requests is the next logical choice because almost everybody in our community already uses it. This worked mostly well for us, but there were certainly some things that could have been improved.

## The diff viewer

GitHub’s diff viewer is line-based. This is good enough for code but problematic for prose where lines (that is, paragraphs) are often very long. The diff viewer doesn’t always highlight small changes (e.g. when someone added a comma or changed a single typo), making it difficult to see what changed. I mostly used [Kaleidoscope](http://www.kaleidoscopeapp.com) to diff changes locally because it is much better at highlighting those small edits. Kaleidoscope has been an essential tool for me for that reason alone.

## Give everybody push access

Collaborating on a pull request works best if everyone has push access to the repository. For the objc.io articles, we made the mistake not to grant the external authors push access – they had to fork the repository to submit a pull request. In turn, editors would not have push access to the forked repository, so even small changes like fixing a typo or changing the formatting could only be made by the author before the pull request was merged. This was not a problem for the books where everyone involved had write access to the main repository.

Unfortunately, you cannot easily add a comment on GitHub to a particular line in the current version of a particular file. Instead, you would first have to find the commit where this line was last changed (using Blame), and then add your comment to that commit. Of course, this only made sense if your comment actually referred to the change in that commit, which often was not the case when a “line” is really a paragraph of several sentences.

I understand why GitHub works the way it does (for example, who should be notified of a new comment when there is no commit author GitHub can refer to?), but if I could add one feature to GitHub, it would be this one.

The obvious workaround is to open an issue and copy-paste the paragraph you want to comment on, but this is tedious and loses the surrounding context.

Another technique that actually worked quite well for us was to type our comments – prefixed with `TODO [Name]` – directly into the file below the paragraphs they referred to. This way, open items would be attached to their context and not get lost in long discussion threads. You could then run a script to list all remaining TODOs. Another script would filter them out before building the latest version of the book.

# Other tools

As far as I know, the decision to use GitHub for the objc.io articles and the books fell very early on – not because it emerged as the winner from a thorough evaluation of all options, but simply because it did the job and everyone involved was familiar with it.

There are lots of specialized collaborative writing services, though, and many of them are probably more beginner-friendly, especially if your co-authors and editors are not developers. Here are the ones I looked at (albeit briefly):

- [Penflip](https://www.penflip.com) (I like that it also uses Git under the covers.)
- [Draft](https://draftin.com/)
- [Typewrite](https://typewrite.io/)
- [Poetica](https://poetica.com/)
- [Authorea](https://www.authorea.com/)

It may very well be that one of these services provides a much better workflow than GitHub. Unfortunately, evaluating them is really hard unless you dive in completely, invite your collaborators, and start working on a real project for at least a couple of weeks. I have not done that.

1. In fact, the objc.io articles would sometimes start out on Google Docs if the authors preferred that. We would then copy and paste everything into a Markdown file when the first draft was done, which would become the master copy for subsequent changes. [↩︎](#fnref:1)
2. And, if you use [Git](https://git-scm.com) or any other distributed version control system, that directory also includes the entire change history. [↩︎](#fnref:2)
