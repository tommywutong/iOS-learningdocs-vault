---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.f.html
archived_at: '2026-07-15T08:14:55.141294Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.e.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.10.md)

#   Generating a Static Site

##  Synopsis

Describes how to use WebObjects to generate a static Web site.

##  Discussion

WebObjects eases the development of dynamic Web-based applications that build HTML pages at run-time. However, there are times you need to generate static Web sites from dynamic WebObjects applications. For example, a publishing company may want to distribute its Web site that features magazines on CDs to its readers. In this case, the company will be looking for a solution that not only allows Internet users to surf the site dynamically, but also put the site onto a CD so that other users can surf it statically.

This example called "Dynamic Publishing" illustrates how to generate a static site from a WebObjects application.

###  Implementing the Dynamic Elements

When writing a WebObjects application that supports static page generation, you must pay attention to those dynamic elements that link to another page (for example, WOHyperlink, WOActiveImage). These elements should refer to the URL of a HTML file in the static site.

In its simplest form, you can use the
href
attributes in WOHyperlink and WOActiveImage to define the location of the HTML file. However, this means that these elements will only behave correctly when surfed statically. To use the same element, the same component, and, hence, the same WebObjects application to work in both dynamically and statically, you must build a dynamic element that changes its identity according to whether the application is static or dynamic. One way to achieve this is to use WOSwitchComponent.

####  VSLINK.WOD

```

SwitchLink: WOSwitchComponent {
          _componentName = linkComponent;
          labelValue = theLabelValue;
          currentDoc = theCurrentDocument;
       }
```

####  VSLINK.WOS

```

id theLabelValue, theCurrentDocument;
- linkComponent {
    if ([[self application] isStaticSite])
        return @"StaticLink";
    else
        return @"DynamicLink";
}
```


Both
StaticLink
and
DynamicLink
are WOHyperlinks.
StaticLink
has a
href
attribute that specifies a static URL and
DynamicLink
has an action that returns a WebObjects response.

####  STATICLINK.WOD

```

AStaticLink: WOHyperlink {
    string = labelValue;
    href = documentStaticPage;
    disabled = isDisable;
};
```

####  DYNAMICLINK.WOD

```

ADynamicLink: WOHyperlink {
    string = labelValue;
    action = gotoDocument;
    disabled = isDisable;
};
```


The template that uses this component has the following declaration:

####  WebScript Code

```

RelatedDocumentLink: VSLink
{
    theLabelValue = aRelatedDocument.name;
    theCurrentDocument = aRelatedDocument;
};
```


###  Directory Structure and Filenames for the Static Site

When generating a static site, it is important to determine

- 

  a strategy for creating unique names for the HTML files that are generated
- 

  the directory structure of your static Web site

in order to specify the correct URL for your images and links. The following are some suggestions of how to handle these two issues:

- 

  Unique file name -- Each HTML file in the static site must be unique. In general, the primary key for the corresponding Enterprise Object is used to ensure uniqueness. In the Dynamic Publishing example, a document-type HTML file generated is named with the primary key of the document (for example,
  23.HTML
  ). If you want to make the name more meaningful, you can prepend the document name (for example,
  iMac-23.HTML
  ).
- 

  Directory Structure -- A static site normally resides somewhere in the document root of your HTTP server. For example, with Microsoft IIS server, the static site should reside in

  /InetPub/wwwroot
  . In the Dynamic Publishing example, the static site has the following directory structure:

```

/InetPub/wwwroot/StaticSite/doc0+/...HTML
/InetPub/wwwroot/StaticSite/doc10+/...HTML
/InetPub/wwwroot/StaticSite/3.HTML
/InetPub/wwwroot/StaticSite/5.HTML
/InetPub/wwwroot/StaticSite/index.HTML
```


StaticSite
is a subdirectory under the document root containing the static site that is generated. Inside the
StaticSite
directory resides
index.html
, which is the home page for the site. Any other HTML files at that level are section home pages. A document is placed in a subdirectory according to its primary key. For example, documents with primary keys from 11 to 20 will be in the subdirectory
doc10+
. This approach is simple, effective, and requires minimum maintenance.

###  How to Send a HTTP Request Programmatically

Typically, two processes are involved in generating a static site:

- 

  A process that knows which HTML pages are required to be generated for the static site and fires the appropriate HTTP request to a WebObjects dynamic application.
- 

  A WebObjects dynamic application that acts as a page broker, taking in a HTTP request and building the response accordingly.

The parameters that are passed to the WebObjects dynamic application are appended as form values at the end of the HTTP request. In the Dynamic Publishing example, the
documentId
is appended as a form value of the HTTP request so that the Dynamic Page Generator receiving the request knows which document to generate.

To fire a HTTP request from a process, you must open a socket programmatically. The simplest way to implement this is to use the Java socket class.

```

Class javaSocketClass = NSClassFromString(@"MyJavaSocket");
Id    javaSocketObj = [javaSocketClass new];

[content setString: [javaSocketObj getContent: URLString]];
```


where URLString is probably something such as:

```

http://python/scripts/WebObjects.exe/DynamicPageGenerator.woa?type=Document&documentId=123
```


getContent in MyJavaSocket uses the Java URL class to fire the HTTP request:

```

public String getContent(String URLPath) {
   String contentString = null;
   try {
        URL aURL = new URL(URLPath);
        URLConnection aURLConnection;
        try {
            byte buffer[] = new byte[20000];
            StringBuffer responseBuff = new StringBuffer();
            int totalBytesRead = 0;
            int bytesRead = -1;
            int i;
            aURLConnection = aURL.openConnection();
            InputStream aInputStream=aURLConnection.getInputStream();
            bytesRead = aInputStream.read(buffer);
            while (bytesRead > 0) {
                totalBytesRead += bytesRead;
                for (i=0; i<bytesRead; i++) {
                    responseBuff.append((char)buffer[i]);
                }
                bytesRead = aInputStream.read(buffer);
            }
            contentString = responseBuff.toString();
        }
    }
    return contentString;
}
```


###  Handling Changes After the Static Site is Generated

Once the site is generated, you must think about how to handle the subsequent changes. How often do you want the changes to propagate to the static site? How do you determine which documents to regenerate when changes are made? The answers depend on the application. Consider a magazine web site, whose contents are updated once a month when a new issue is published. A simple approach, generating a new static site each month, suffices. However, for a Web site that provides 24-hour news to Internet users, the application logic that chooses the documents to regenerate becomes more complex.

###  Limitations of Static Sites

Since the site generated is effectively a static site, the limitations of a manually developed static site applies to a dynamically generated static site as well. For example, there will be no support for direct interaction with the users and, hence, no support for Form elements.

##  See Also

- 

  WOSwitchComponent specification in the _WebObjects Dynamic Element Specifications_

##  Questions

- 

  How do I generate a static site dynamically?
- 

  How do I programmatically fire a HTTP request to a WebObjects application?

##  Keywords

- 

  Static
- 

  Site

##  Revision History

20 July, 1998. Winnie Pun. First Draft.
19 November, 1998. Clif Liu. Second Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.e.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.10.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
