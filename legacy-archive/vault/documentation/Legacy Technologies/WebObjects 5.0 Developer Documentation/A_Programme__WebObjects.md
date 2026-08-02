---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/WOHTML/A_Programme__WebObjects.html
archived_at: '2026-07-15T08:15:12.265429Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](HTML_Based_Applications.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](WebObjects_Architecture.md)

## A Programmer's View of WebObjects

The following features of WebObjects ease the development
of HTML-based Web applications:

- __The
  HTML and code reside in separate files.__ An object called
  a __component__ represents a Web page and consists
  of separate files for HTML and Java code.
- __WebObjects provides dynamic versions of static
  HTML elements.__ These are called __dynamic elements__.
- __You can reuse HTML and code.__ Components
  can be embedded within other components as if they were dynamic
  elements.
- __WebObjects automatically maintains state information.__ WebObjects
  overcomes the inherent statelessness of HTTP and maintains session
  state (like a shopping cart) and application state (like application
  statistics).
- __Your Web interface code remains separate from your
  business logic.__ Enterprise objects, discussed in Chapter [3](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/EnterpriseObjects/iEnterprise_Objects.html), contain all of your business
  logic. This allows you to reuse your business logic in multiple
  Web pages and even multiple applications.

These advantages are discussed in more detail in the sections
that follow.

### Separating HTML and Code

In WebObjects, a Web page is represented by a __component__,
an object that has both content and behavior. A component can also
represent a portion of a page but usually represents an entire page,
so the word "page" is used interchangeably with the word "component."

Components consist of

- __a
  template in HTML that specifies how the component looks.__ This
  file can be edited by any HTML editor or text editor.
- __code that specifies how the component acts.__ You
  specify this with a standard Java source file.
- __bindings that associate the component's template
  with its code.__ These are stored in a text file.

Separating the template, code, and bindings makes it much
easier to maintain a website. A graphic artist can modify a template,
thus modifying the appearance of the page, without breaking the
code. A programmer can completely rearrange the code without accidentally changing
the layout.

You do not need to edit all three files separately. WebObjects
Builder, a graphical component editing tool provided with WebObjects,
edits the template, bindings, and code files simultaneously, relieving
you of having to manually synchronize them. WebObjects Builder is
described in more detail in ["WebObjects Builder"](Developing__Application.md#apple-krifqusfiyytcmy).

[Figure 4-1](#apple-infeeqsbjjduq) shows the three files in an example component.

__Figure
4-1 The files of a WebObjects component__

![[image: ../Art/GreetingHTML.gif]](../Art/GreetingHTML.gif)

### Dynamic HTML Elements

The template file in [Figure 4-1](#apple-infeeqsbjjduq) looks like any other
HTML file except for the element with the `<WEBOBJECT>` tag.
In this example, this tag represents a __dynamic element__.
Dynamic elements are basic building blocks of a WebObjects application.
They link an application's behavior with the HTML page shown in
the Web browser, and their contents are defined at runtime. A dynamic
element appears in the template as a `<WEBOBJECT>` tag
with a corresponding `</WEBOBJECT>` closing
tag. Some dynamic elements have no HTML counterpart; WORepetition
and WOConditional are examples. [Table 4-1](#apple-krifqusfiyytcoa) lists some of the more
commonly used dynamic elements.

__Table
4-1 Example Dynamic Elements__

__|  |  |
| --- | --- |
| Element Name | Description |__| WOBrowser | A selection list that displays multiple items at a time. |
| WOCheckBox | A checkbox user interface control. |
| WOConditional | Controls whether a portion of the HTML page will be generated. |
| WOForm | A container element that generates a fill-in form. |
| WOHyperlink | Generates a hypertext link. |
| WOImage | Displays an image. |
| WORadioButton | Represents a toggle switch. |
| WORepetition | A container element that repeats its contents (that is, everything between the <WEBOBJECT...> and </WEBOBJECT...> tags in the template file) a given number of times. |
| WOResetButton | A button that clears a form. |
| WOString | A dynamically generated string. |
| WOSubmitButton | A submit button. |
| WOText | A multiline field for text input and display. |
| WOTextField | A single-line field for text input and display. |

### Reusing Components

You can embed a component within another component. For example,
a component might represent only a header or footer of a page; you
can nest it inside of a component that represents the rest of the
page. A component designed to be nested within another component
is called a __reusable component__, shared component,
or subcomponent. Like dynamic elements, reusable components appear
in the template as a `<WEBOBJECT>` tag
with a corresponding `</WEBOBJECT>` closing
tag, allowing you to extend WebObjects' repertoire of dynamically
generated HTML elements.

The WOExtensions Framework provided with WebObjects contains
many useful reusable components like tables, radio button matrices,
tab panels, and collapsible content. In addition, Direct to Web
provides reusable components for editing, listing, selecting, inspecting,
and querying enterprise objects.

### Maintaining State

In addition to the components, each WebObjects application
has a number of __sessions__ and an __application
object__.

A __session__ is a period during which a particular
user is accessing your application. Because users on different clients
may be accessing your application at the same time, a single application
may host more than one session at a time. Session objects encapsulate
the state of a single session. These objects persist beyond the
HTTP request-response cycles, and store (and restore) the pages
of a session, the values of session variables, and any other state
that components need to persist throughout a session. In addition,
each session has its own copy of the components that its user has
requested.

Session variables can be used in shopping cart applications
to represent the items in the shopping cart. Email applications
can use session variables to keep track of whether the user has
logged in or not.

The application object is responsible for interfacing to an
adaptor and forwarding HTTP requests to a dispatcher that, in turn,
passes them to the appropriate session and component. The application
object also passes the HTML response from the active component back
to the adaptor. In addition, the application object manages adaptors, sessions,
application resources, and components.

### Separating Web Interface Code from Business Logic

In HTML-based WebObjects applications (as in all WebObjects
applications), the enterprise objects encapsulate the application's
business logic and provide the connection with the application's
databases. Since enterprise objects are objects, they can appear
as variables in components, sessions, or the application object.
A component's bindings file relates the component's enterprise
objects to the attributes of its dynamic elements. [Figure 4-2](#apple-infeeskbjbaue) shows
how enterprise objects relate to a component in a WebObjects application.

__Figure
4-2 How enterprise objects relate to a
WebObjects component__

![[image: ../Art/HTMLComponent.gif]](../Art/HTMLComponent.gif)

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](HTML_Based_Applications.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](WebObjects_Architecture.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
