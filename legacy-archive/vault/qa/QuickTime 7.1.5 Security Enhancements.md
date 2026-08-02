---
title: QuickTime 7.1.5 Security Enhancements
apple_id: DTS10004261
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2007-04-02'
source_url: https://developer.apple.com/library/archive/qa/qa1520/_index.html
archived_at: '2026-07-18T02:32:05.157767Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1520

# QuickTime 7.1.5 Security Enhancements

## Q:  I'd like to learn more about the security enhancements and other changes contained in the QuickTime 7.1.5 Update. Please help.

A: QuickTime 7.1.5 delivers numerous bug fixes and addresses critical security issues. Here's a brief overview of the security enhancements contained in this release:

The QuickTime 7.1.5 Update places the following new restrictions on all URLs passed to the QuickTime plug-in:

- URLs cannot cross local/remote zone boundaries

Here's how it works:

Prior to asking the user's web browser to access a URL, the QuickTime plug-in compares the requested URL with the "src" URL (the URL for the movie as specified in HTML) and does the following:

- If the "src" movie is http:, https:, data:, rtsp:, or if there is no "src" attribute at all, it allows only http: and https: URLs.
- If the "src" movie is "file:" it allows only file: URLs.

In other words, a local movie can invoke only local URLs, such as another local movie, and remote movies can invoke only remote URLs, such as another remote movie or a web page. Furthermore, remote URLs are restricted to the http:// and https:// protocols. Other protocols, such as javascript://, are prohibited.

Movies played by the QuickTime plug-in in QuickTime 7.1.5 or later will not issue URLs that violate these restrictions, regardless of when the movies were authored.

For additional information about these security enhancements, please see the following documents:

- [HTML Scripting Guide for QuickTime](https://developer.apple.com/documentation/QuickTime/Conceptual/QTScripting_HTML/index.html)
- [QuickTime and JavaScript](https://developer.apple.com/documentation/QuickTime/Conceptual/QTScripting_JavaScript/bQTScripting_JavaScri_Document/chapter_1000_section_1.html)
- [About the security content of QuickTime 7.1.5](http://docs.info.apple.com/article.html?artnum=305149)

QuickTime 7.1.5 also introduces the Apple TV Export Component supporting export specifically for Apple TV. See [Technical Note TN2188: Exporting Movies for iPod and Apple TV](https://developer.apple.com/library/archive/qa/qa1520/TN2188) for all the details.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-04-02 | New document that Discusses the security enhancements and other changes contained in the QuickTime 7.1.5 Update. |

