---
title: Sharing Browser Cookies With Java Applets
apple_id: DTS10002295
resource_type: QA
platform: Java
topic: Cross Platform
technology: null
published: '2004-10-13'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1265.html
archived_at: '2026-07-18T02:38:21.850540Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



|  |  |
| --- | --- |
|  |  |
| [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Internet & Web](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxInternetWeb-date.html) > | [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Internet & Web](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxInternetWeb-date.html) > |
|  |  |

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Internet & Web > Java](https://developer.apple.com/referencelibrary/InternetWeb/idxJava-date.html)

|  |
| --- |
| Technical Q&A QA1265Sharing Browser Cookies With Java Applets |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Q: Each time my Java Applet opens URLConnections to a server process, a new session with the server is generated. Why doesn't the Applet just use the cookie from its host browser?  A: Prior to Java 1.4.1 Update 1 for Mac OS X 10.2, the Java Plugin did not share cookies with the web browser they are embedded in. This results in separate sessions for the applet's HTTP connections and those of the browser, which can be problematic for some web applications. The problem can be solved, however, by forcing the browser's cookie upon the Applet. This does require code changes, but is reliable across browsers and versions of Mac OS X Java (1.3.1 and 1.4.1).  __Note:__ This problem does not exist in Safari as of Java 1.4.1 Update 1 for Mac OS X 10.2, including all Java 1.4 releases on Mac OS X 10.3 and above. This Q&A is only applicable to developers wishing to support browsers other than Safari which continue to use Java 1.3. Developers requiring Java 1.4 on Mac OS X 10.2 can simply request that users download Java 1.4.1 Update 1 for free via Software Update.  Listing 1 demonstrates the HTML code required to start the process. The entire APPLET tag is written out using JavaScript, and the browser's cookie is written as a PARAM to the Applet via the Document.cookie JavaScript property. This simple HTML and JavaScript can easily be inserted into a JSP or Servlet, or any other dynamic mechanism.  __Listing 1:__ Sending the browser cookie to an Applet.   ``` <HTML>     <BODY>      <SCRIPT LANGUAGE="JavaScript"><!--       // If cutting and pasting, remove line breaks from this writeln code       document.writeln("<APPLET codebase=\".\"          code=\"CookieCommune.class\"          name=\"CookieCommune\" >");         document.writeln("<PARAM name=\"browserCookie\"          value=\"" + document.cookie + "\">");       document.writeln("</APPLET>");     --></SCRIPT>    </BODY> </HTML> ```   The second part of the process is within the Applet itself, where the cookie parameter is fetched and used in all subsequent HTTP connections that the Applet needs to make by setting the "Cookie" request property. Listing 2 shows what this code might look like.  __Listing 2:__ Using the browser cookie inside an Applet.   ``` import java.net.*;   public class CookieCommune extends java.applet.Applet {      private URL serverURL;     public void init() {        try {        serverURL = new URL("http://mystatefulserver.com/talk.cgi");       } catch (MalformedURLException e) {}       super.init();     }     public void start() {        try {         // COOKIE SHARING: take browser cookie from Applet params          URLConnection conn = serverURL.openConnection();         // Attach browser cookie to URLConnection         conn.setRequestProperty)"Cookie", getParameter("browserCookie"));       } catch (java.io.IOException e) {}       // .... use our new cookie-friendly Applet connections!     }   } ```   The result is an Applet that uses the same cookie information as its host browser every time, even through browser refreshes (where the original problem typically manifests). The demonstrated solution should be pluggable across various server applications, as well as any browser that uses Java 1.3.1 or Java 1.4.1 to run Applets on Mac OS X 10.2. Document Revision History  | Date | Notes | | --- | --- | | 2004-10-13 | Cited problem resolution in 1.4.1 Update 1 (for Jaguar) and later. | | 2003-09-11 | New document that creating a persistent browser session (cookie) inside Java 1.3 Applets | |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
