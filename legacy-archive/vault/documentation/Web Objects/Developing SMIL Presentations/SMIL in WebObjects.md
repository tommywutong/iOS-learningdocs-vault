---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Introduction/SMIL_in_WebObjects.html
archived_at: '2026-07-18T02:20:17.708594Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/AboutThisBook/pAbout_This_Book.html) [!](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/index.html)

# SMIL in WebObjects

SMIL (Synchronized Multimedia Integration Language)
is a specification developed by the World Wide Web Consortium to
facilitate the creation and delivery of time-based multimedia content.
With it you can create a presentation made up of several types of media
objects, including text, voice, and video. WebObjects uses version
1.0 of the SMIL specification.

SMIL allows you to place media objects anywhere in a window
and determine when each object is displayed using a timeline. It
also lets you tailor the display of media objects according to the
capabilities of a user's computer, Internet connection speed,
and preferred language, among other criteria. The specification
also provides for linking presentations with each other through
hyperlinks.

An important feature of SMIL documents (which are written
in XML) is that they reference media objects using URLs. This way,
you can set the object that a SMIL element applies to dynamically.
For example, you can use a database containing the names and URLs
of movies to dynamically create a presentation that the user can
use to choose which movie to watch.

SMIL documents can be viewed with multimedia players like
QuickTime Player and RealPlayer. This is an example of a SMIL document:

```
<smil>
    <head>
        <layout>
            <root-layout background-color="#FFFFFF"
                width="100" height="200" id="window" />
            <region id="text_rgn" top="5" />
        </layout>
    </head>
    <body>
        <text region="text_rgn" src="text.html" dur="10s" />
    </body>
</smil>
```

Notice that a SMIL document has two main sections: the layout
section and the body section. The layout section specifies the dimensions
and background color of the presentation's window and the regions
into which the window is divided. Additionally, it can provide metadata
describing the presentation. The body section is where information about
the media objects that make up the presentation is placed. It includes
the physical location of the file as well as display properties,
such as when to show the object and for how long.

WebObjects provides the tools you need to create SMIL presentations
that take advantage of WebObjects technologies such as Enterprise
Objects. For example, you can create an application with a SMIL
component that displays a list of movies from a database and a second
component that shows the movie the user selected in the first one.

To design SMIL presentations in WebObjects, you create standard
WebObjects applications in Project Builder and SMIL components in
WebObjects Builder. You don't create SMIL documents directly.
Rather, you use WebObjects Builder to graphically lay out SMIL elements.
To provide data for SMIL attributes you enter values for the bindings
of each SMIL element.

After designing a SMIL component, or presentation, you build
and run the application like you normally would. However, instead
of using a Web browser to view the application's output, you use
a multimedia player. When the player connects to a WebObjects application
that serves a SMIL presentation, it receives a standard SMIL document.
See [Chapter 4, "SMIL Elements",](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/iSMIL_Elemen_BCHIBCI.html) for
details on the SMIL elements used in WebObjects.

You can use the `curl` command-line
tool to view the SMIL source code that WebObjects generates when
your multimedia viewer connects to a SMIL application. Simply enter
the command in your shell editor followed by the URL used to connect
to the presentation.

[!](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/AboutThisBook/pAbout_This_Book.html) [!](https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/CreatingPresentations/index.html)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
