---
title: WebObjects J2EE Programming Guide
apple_id: TP30001013
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/JSP_and_Servlets/About/About.html
archived_at: '2026-07-18T02:20:56.542188Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/WebObjects/JSP_and_Servlets/Servlets/Servlets.html)

# Introduction to WebObjects J2EE Programming Guide

JavaServer Pages (JSP) and servlets are important parts of Sun’s J2EE (Java 2 Platform, Enterprise Edition) architecture. JSP is a specification that defines interfaces that servlet-container vendors can implement to provide developers the ability to create dynamic Web pages, which are files with the extension `.jsp`. Servlet containers interpret these files and create servlets (also know as workhorse servlets) to process HTTP requests and produce responses. Servlets are server plug-ins that extend the capabilities of your Web server. They provide a straightforward deployment mechanism for your applications. Servlets are deployed inside servlet containers, which are plug-ins to your Web server.

You should read this document if you want to deploy your WebObjects applications inside a servlet container or want to take advantage of WebObjects components (both standard and custom) in your JSP pages.

Deploying WebObjects applications as servlets allows you to take advantage of the features that your servlet container provides. Keep in mind that deployment tools such as Monitor and wotaskd do not work with servlets. WebObjects uses version 2.2 of the Servlet API, and version 1.1 of the JSP specification.

The document addresses two major points, each contained in its own chapter:

- [Servlets](https://developer.apple.com/library/archive/documentation/WebObjects/JSP_and_Servlets/Servlets/Servlets.html#//apple_ref/doc/uid/TP30000040-TPXREF101) explains how you develop WebObjects applications to be deployed as servlets and how to add servlet capability to existing applications.
- [JavaServer Pages](https://developer.apple.com/library/archive/documentation/WebObjects/JSP_and_Servlets/JavaServer_Pages/JavaServer_Pages.html#//apple_ref/doc/uid/TP30000041-TPXREF101) tells you how to write JSP-based applications, which can be thought of as JSP applications that use WebObjects technology or hybrids—applications that use JSP pages to accomplish some tasks and WebObjects components or direct actions to perform others.
- [Special Issues](https://developer.apple.com/library/archive/documentation/WebObjects/JSP_and_Servlets/SpecialIssues/SpecialIssues.html#//apple_ref/doc/uid/TP30000042-TPXREF101) addresses special issues to consider when you deploy WebObjects applications as servlets or when you develop JSP-based applications.
- [Document Revision History](https://developer.apple.com/library/archive/documentation/WebObjects/JSP_and_Servlets/RevisionHistory/RevisionHistory.html#//apple_ref/doc/uid/TP30000043-BAJJHJBG) lists the revisions made to this document.

To get the most out of this document, you must be familiar with WebObjects application development. In particular, you need to know how to create applications using Project Builder and how to layout WebObjects components using WebObjects Builder.

For additional WebObjects documentation and links to other resources, visit [http://developer.apple.com/webobjects](https://developer.apple.com/webobjects).

In addition to WebObjects development experience, you also need to be acquainted with the syntax used in JSP pages and with the layout of WAR (Web Application Archive) files. You can find information about JSP and J2EE in the following documents:

- _Java Servlet Programming_, 2nd edition (O’Reilly) provides an in-depth treatise on servlets. You can find more information at [http://java.oreilly.com](http://java.oreilly.com/).
- _J2EE Technology in Practice_ (Sun) provides an overview of J2EE technology.
- _JavaServer Pages Technology Syntax_ (Sun) is a short document that describes the syntax used in JSP pages. You can download it from [http://java.sun.com/products/jsp/technical.html](http://java.sun.com/products/jsp/technical.html). For more information on JSP and servlets, see [http://java.sun.com/products/jsp](http://java.sun.com/products/jsp).
- _Java Servlet Technology_ contains the latest information on Sun’s Java Servlet technology. You can view it at [http://java.sun.com/products/servlet/](http://java.sun.com/products/servlet/).

WebObjects Developer also includes a commented application project that shows you how JSP pages can take advantage of WebObjects components and direct actions. The example—using the client/server approach—includes two WebObjects application projects named SchoolToolsClient and SchoolToolsServer. The projects are located at `/Developer/Examples/JavaWebObjects`.

The three servlet containers supported in WebObjects are listed in Table I-1.

__Table I-1__  Servlet containers supported in WebObjects

| Platform | Container | Version |
| Mac OS X Server | Tomcat | 3.2.4 |
| Solaris | WebLogic | 7.0 |
| Windows 2000 | WebSphere | 4.0.4 |

[Next](https://developer.apple.com/library/archive/documentation/WebObjects/JSP_and_Servlets/Servlets/Servlets.html)

