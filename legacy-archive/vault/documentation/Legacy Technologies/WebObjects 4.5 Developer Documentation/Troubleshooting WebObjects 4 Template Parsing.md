---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.40.html
archived_at: '2026-07-15T08:09:41.906654Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Converting%20Projects%20From%20Earlier%20Releases.md) [!](Converting%20Java%20Code%20From%20WebObjects%203.5.md) [!](Troubleshooting%20WebObjects%204%20Request%20Handling.md)

---

#   Troubleshooting WebObjects 4 Template Parsing

The WebObjects template parser parses the HTML that is to be included in a response. In WebObjects 4, the template parser preserves all of the static HTML that you provide in a component's template. Previously, the parser recognized many HTML tags and performed special processing based on the type of tag. The WebObjects 4 template parser ignores all tags besides
<WEBOBJECT>
and HTML comment tags.

The new parser has several advantages:

- 

  It solves the problem many have encountered where WebObjects attempts to "fix" your HTML. For example, it previously was difficult to split a container element, such as a form, across two components because WebObjects would insert a closing tag for you.
- 

  It improves your application's performance because it tends to treat larger parts of a file as a single chunk than the previous parser did.
- 

  It allows you to suppress the copying of comments to the outgoing response. This speeds up response generation and shortens download times.

A WebObjects application may unknowingly depend upon the previous behavior of the template parser. For this reason, a compatibility flag is available on WOApplication to revert to the previous behavior.

Usually when WebObjects 4 template parsing produces an error, it is because you have included a WebObjects dynamic form element inside of a static HTML
FORM
element. Change the
FORM
element to a WOForm, and your component should operate normally again. An error may also arise if your HTML pages contain
BODY
or
IMG
tags with
src
parameters containing relative pathnames (absolute pathnames aren't a problem). Change the affected tags to WOBody and WOImage, respectively.

If you want, you can go back to the previous parser by implementing this method in your application class (shown in Java and WebScript):

public boolean requiresWOF35TemplateParser() {

      return true;

    }

    - requiresWOF35TemplateParser {

      return YES;

    }

If you use the WebObjects 4 template parser, you might want to suppress the inclusion of HTML comments. Use WOApplication's
setIncludeCommentsInResponses:
method, or use the
WOIncludeCommentsInResponses
option described in "Starting Up Applications From the Command Line" in _Deploying WebObjects Applications_
.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Converting%20Projects%20From%20Earlier%20Releases.md) [!](Converting%20Java%20Code%20From%20WebObjects%203.5.md) [!](Troubleshooting%20WebObjects%204%20Request%20Handling.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
