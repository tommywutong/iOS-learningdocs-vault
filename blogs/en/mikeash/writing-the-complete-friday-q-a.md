---
title: 'Writing the Complete Friday Q&A'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/writing-the-complete-friday-qa.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3aad0ee5e2556588'
translated: false
---

> 原文：[Writing the Complete Friday Q&A](https://www.mikeash.com/pyblog/writing-the-complete-friday-qa.html)　·　mikeash.com Friday Q&A

Posted at 2011-01-28 20:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Complete Friday Q&A Direct-Sell ePub, PDF, and Print on Demand](https://www.mikeash.com/pyblog/complete-friday-qa-direct-sell-epub-pdf-and-print-on-demand.html)  
Previous article: [Complete Friday Q&A Now Available](https://www.mikeash.com/pyblog/complete-friday-qa-now-available.html)  
Tags: [book](https://www.mikeash.com/pyblog/?tag=book) [epub](https://www.mikeash.com/pyblog/?tag=epub)

Writing the Complete Friday Q&A

by [Mike Ash](https://www.mikeash.com/)

**Origins**  
 Quite a few people have suggested to me from time to time that I should publish a book based on Friday Q&A. At the same time, my activities here drew the attention of publishers. I ended up writing portions of two different books in 2009.

Unfortunately, that experience soured me on the entire publishing industry. Without getting into gory details, it was time-consuming and unenjoyable. Additionally, publishers seem to bring little value to the equation while receiving almost all of the money, and sometimes act to _reduce_ value by making content decisions based on marketing reasons.

(The money really is absurd. If I had written one of these books all on my own, without any co-author to split the proceeds, I would have ended up with something like 5% of the cover price for each book purchased. Put it another way: if you buy a $40 tech book, the author will probably see about two of those dollars.)

There are probably publishers out there that are better than the one I worked with. However, the potential upside seemed small, and the potential downside seemed large, so I saw no point in investigating in any detail.

Some people brought up the idea of self-publishing, but it didn't look attractive. Blogging looked like a much better way to go in the end.

The iPad is what finally changed my mind. Here was a device that virtually everyone in my audience was going to own. iBooks ended up being reasonably friendly to independent publishers. After flirting with the idea of selling individual chapters, I finally decided that the best way to go would be to sell a full compilation on iBooks. The money was much more sane (70% of the purchase price goes to the author), I could decide exactly what goes into the book, no deadlines in sight, and all in all it was a much more attractive proposition.

With the overall strategy finally decided, the next step was to massage the text into something iBooks would accept.

**Constructing the ePub File**  
 I had originally considered creating and selling PDFs, but after some thought it appeared that the iBooks store was the way to go, and iBooks meant creating ePubs.

At first I set out to build the ePubs myself. The basic structure of an ePub is XHTML and CSS with XML metadata all stuffed into in a zip file. Since the Friday Q&A posts already existed in HTML form, this seemed like a good approach. However, there are a lot of details needed to produce a valid ePub, and it ended up being impractical, or at least unpleasant, to build them from scratch.

After further investigation, I settled on using [Calibre](http://calibre-ebook.com/) to convert HTML to ePub. Although mainly a GUI application, it includes command-line tools suitable for automating the conversion.

Things were not as straightforward as simply invoking Calibre and submitting the output. The first obstacle was that Calibre takes a single HTML file, with an XPath specified for detecting chapter and page breaks, but Friday Q&A's HTML was spread out across many files, one per post. I wrote code using Python and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) to massage the individual files into a big HTML file in the form that Calibre wanted.

The HTML required a lot of cleaning up to work correctly. Apple requires that iBooks ePubs pass [ePubCheck](http://code.google.com/p/epubcheck/) 1.0.5 validation. Calibre doesn't take care of everything needed to pass validation, and the initial conversion produced several thousand validation errors, so it was clear that some additional work was needed.

Most of the cleanup was fairly straightforward. There were lots of little details that had to be changed, like using `<a id="...">` instead of `<a name="...">`, or needing an `alt` attribute on all `<img>` elements.

One major problem I encountered was getting code blocks to show up in a monospaced font with syntax highlighting. iBooks mostly ignores CSS font attributes, including requests for monospaced fonts. (This was true with 1.1, at least. I have not re-checked it with 1.2.) It would only respect font choices on a very small set of HTML tags, and would even ignore a font specified on one of those tags if it was nested inside a tag it didn't like. I was able to work out some code to clean up the code so iBooks would display it properly, but this caused validation errors. Cleaning up the validation errors broke the monospaced code. I was stuck.

One of my reviewers, [Jeff Schilling](http://manicwave.com/), refused to let me give up, and dove into the problem himself. His solution was to do the initial transformation which produced validation errors, then use the `tidy` command to clean up the HTML so it would validate. It worked! The `tidy` command broke a few things as well, but they were easy to fix up in a final pass with BeautifulSoup.

Aside from validation errors, a lot of other things needed small alterations as well. There were a lot of inter-post links which were broken when squishing everything into a single HTML file. These all had to be found and replaced with anchor links. The closing paragraphs on each post, which all say basically the same thing along the lines of "That's it for this week, come back next time, and send me your ideas for topics in the meantime," were universally decided to be pointless, and so I stripped them. This was all easily accomplished with BeautifulSoup.

Going beyond the bare minimum needed for validation, I decided to take advantage of my blog's tag system to build a richer experience. By lightly transforming the tags into something more human-readable and friendly, and then dumping out all of the tags and a list of articles each tag applied to, I was able to build up a nice index for the book. By seeing which posts had tags in common with other posts, I was able to build a comprehensive list of related articles at the top of each chapter.

The end result was a `git` repository which contained the original Friday Q&A HTML (with a few small fixes), other book resources, and a Python program which could automatically take it all and turn it into an ePub. The one external dependency was for the Calibre command-line tools. In a single command, I am able to create a fresh build of the book, validate it with ePubCheck 1.0.5, and upload it to my web site:

```
    ./make.py build check upload
```

As a programmer, this pleased me a great deal. I had a validating ePub with the features I needed. I just had to make it worthy of release.

**Proofreading**  
 I had initially considered pushing the book out as-is, but after some thought it became clear that it needed additional polishing. Books and blogs simply don't have the same standards of quality or finish. I needed to proofread the book.

Doing it myself was daunting and probably wouldn't have been very useful anyway. A writer tends to easily overlook mistakes in his own work that an external reader will spot in an instant.

Hiring a professional proofreader seemed like a decent possibility, but it didn't look like it would be cost-effective, and I wasn't fond of having somebody who wasn't familiar with my work or with Mac programming doing the proofreading.

Trouble was, who would volunteer for the job of proofreading this book? It ended up being massive, about 920 pages at a reasonable font size on my iPad. This would be a substantial amount of work.

I was talking about this with [Paul Kafasis](http://www.onefoottsunami.com/), and he suggested the idea of recruiting a bunch of people to proofread just a few chapters each. By spreading out the work, nobody would have do too much. We figured I could recruit enough people from my Twitter followers, and I decided to give this a shot.

**Crowdsourced Proofreading**  
 To make everything work smoothly, I needed infrastructure to coordinate and organize the many reviewers I was planning to pull in. I set up a Google Group for basic communication.

Beyond that, we needed a way to avoid duplicating work. I didn't want multiple people all reviewing the same chapter simultaneously without knowing it. Simply declaring work in advance to the mailing list didn't seem like it would work, since people frequently miss mailing list messages. I finally hit upon the idea of using a Google Docs spreadsheet. Each chapter got a row, with columns for chapter claims, and for when it was finished. I made it world-editable and posted the link on the Google Group.

Finally, I needed a way to actually get the book to the reviewers. I posted the ePub file to my web space and posted the URL to the group. I included instructions for getting it onto the iPad, which were fairly involved at the time. (Now you can just load the URL in Safari on the iPad and tell it to open in iBooks, but at the time you had to download it on your computer, put it into iTunes, and sync.)

This setup ended up working extremely well. People claimed chapters through the spreadsheet as desired, then marked them off when done. They sent feedback to the group where I could see it and act upon it, and other reviewers could pitch in if something was unclear.

Since chapter review tracking was all in real time, people who wanted to put in more work were able to grab more chapters as they wished. There were a few problems where people neglected or didn't understand the shared spreadsheet, as is to be expected, but it was nothing major.

In addition to catching all sorts of embarrassing typos, the reviewers provided valuable feedback in other areas. On their advice, I persevered with monospaced code, got rid of the closing paragraphs on each post, and eliminated some other sentences which were pointless when in book form, such as explicit directions to "click" on a link.

I used Twitter as my primary recruiting tool. I'm fortunate to have a lot of followers who are enthusiastic about my blog, and so I got a decent number right away. I augmented the ranks with some judicious recruiting among friends.

The review took much longer than I anticipated. I thought it would take a few weeks, and it ended up taking a few months. This was no surprise to me, being used to software schedules where bumping the estimate up to the next larger unit of time is typical. The review was far more thorough than I anticipated as well, and in the end it was an excellent tradeoff.

**Publishing**  
 With the ePub done, I had to get it out to the world. Although Apple does allow individual authors to sign up and publish through iBooks, they discourage it. They link to distributors during the sign-up process and make it fairly obvious that this is their preferred route. I liked the idea of having as few entities in the middle as possible, but the signup process was intimidating. What finally sealed the deal for me was Apple's requirement that I bring an ISBN, and my inability to find a decent, reasonably-priced way to obtain one on my own.

After looking through Apple's approved distributors, I finally settled on [BookBaby](https://www.bookbaby.com/). I'd heard lots of good things about their sister company CDBaby. They also offered the best terms, with low up-front fees, no per-sale fees, worldwide distribution, and distribution to Amazon, Barnes & Noble, and Sony in addition to iBooks.

The signup process was pretty much painless. I gave them a bunch of information about myself and about the book, and then gave them the ePub.

I made a mistake at this point. I uploaded an ePub that was not quite ready, assuming that I could easily upload a revised one. Turns out that this is not the case. BookBaby requires manual intervention on their side to reset the upload, and so I had to contact them and wait for them to fix things for me. Easy enough to avoid, and I had no good reason to upload the ePub before I was ready.

Once everything was in, I paid my money and the waiting game began.

Turns out that I didn't have long to wait. Only two days after submission, BookBaby showed that the book had been delivered to all four stores, and the book was available for purchase from Amazon and Apple.

**Conclusion**  
 Overall, self-publishing _The Complete Friday Q&A: Volume I_ was a great experience. It was enjoyable in every way that dealing with traditional publishers was not. While I don't have the marketing reach of traditional publishers, initial Twitter buzz suggests that sales should be pretty decent. Since I get about 14 times as much money per sale as I would through a traditional publisher, I can do well with many fewer sales. More than that, I have the satisfaction of knowing that I had total control over what my readers get, I was able to provide useful information without having to worry about what higher-ups would think, and I was able to bypass an industry which more and more gives the appearance of being obsolete and unnecessary.

The ePub conversion had some tough spots but overall was not too bad at all. I'm not sure how someone would fare who is not willing to write code to help with the conversion. BookBaby offers conversion to ePub from other formats for an additional fee, as do many others. I didn't want to try that simply because I wanted full control over the final output, but it should be a good option.

Crowdsourced proofreading ended up working incredibly well. Although slower than I expected, the result was outstanding, and I got a huge amount of valuable input from my reviewers. Many hands truly make light work, and I think this is an excellent way to go. I initially considered foregoing this step, and I'm extremely glad that I didn't.

Finally, distributing through BookBaby was an easy way to get into the iBooks and Kindle stores. The price is right, and the process is simple. Two days after finalizing my submission, I had my book available through two big stores.

The internet tends to eliminate middlemen. It's been harder to do this in the publishing industry than in others because good electronic readers only appeared recently, but now that they have, they're paying off in a big way. I hope that my example may serve to inspire other prospective authors to try a similar route. I would love to see a nice selection of good, self-published technical books available for my iPad, and there's no time like the present to get started with it.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/writing-the-complete-friday-qa.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
