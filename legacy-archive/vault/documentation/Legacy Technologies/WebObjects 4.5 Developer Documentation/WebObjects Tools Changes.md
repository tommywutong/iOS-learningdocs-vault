---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeltaDoc/WOTools.html
archived_at: '2026-07-15T08:04:35.675621Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
What's New in WebObjects

---

[!](What%27s%20New%20in%20WebObjects%204.5.md)

# WebObjects Tools Changes

This chapter describes changes to the WebObjects tools between
release 4.0.1 and 4.5. It describes changes to existing features
and new features that you might want to start using. The WebObjects
tools include the Project Builder application, the WebObjects Builder application,
and the Direct to Web framework.

## Project Builder Changes

Project Builder has received changes in this release in the
areas of `NSProjectSearchPath` support,
indentation, and the Build, Launch, and Find panels.

Project Builder now includes a Searchpath preferences panel
to specify the project's `NSProjectSearchPath` user
default. If your project uses framework projects that reside in
a directory in the `NSProjectSearchPath`,
you can access the source files for the frameworks through the Frameworks
suitcase. Using the Build Options panel in the Build panel, you can
specify whether to build the frameworks when you build the project.
In the Find panel you can specify whether to search the project
and frameworks or just the project.

Project Builder's automatic indentation has been upgraded.
You can control its behavior with the Indentation preferences panel.

Project Builder's Build, Launch (with debugger) and Find
panels now have an extra pane where you can edit code. You no longer
need to switch between the main Project Builder window and the Build
panel when you are editing compile errors. Likewise, you can search
for text within the project and edit it without leaving the Find
panel.

Project Builder is documented in _WebObjects Tools
and Techniques_.

## WebObjects Builder Changes

WebObjects Builder's user interface has received major changes
for 4.5, specifically in the main window toolbar, the user interface
for binding keys, and the table editing user interface. A path view,
an API editor, and component validation have been added. WebObjects
Builder is documented in _WebObjects Tools and Techniques_.

### Main Window Changes

The editing modes from WebObjects 4.0.1 have been renamed.
Graphical Editing Mode is now called the layout view. Source Editing
Mode is now called the source view. A new view called the preview
view has been added.

#### Layout View Changes

The toolbars have been reorganized. All tools are now available
in a single click. You don't have to choose a toolbar. The WOComponentContent
dynamic element is now available from the toolbar. In addition,
the toolbar also contains an alert icon, which opens a window displaying
the validation errors on the page and a puzzle piece icon, which
opens the API editor. The API editor is described below.

WebObjects Builder now optionally displays HTML tags with
opening and closing tag icons, which makes the HTML structure of
the page more transparent. You can choose which tags are marked
this way with the Layout preferences panel.

In the center of the window is a path view, which replaces
the path view in the inspector and provides extra functionality.
The path view displays the elements in the path as HTML tags rather
than icons.

The object browser has column headings. Each heading displays
the class of the object selected in the previous column. This class
also contains the keys in the column.

Double clicking an element's icon no longer collapses the
element. Use the preview view instead (described below).

#### Preview View

A new preview view, similar to the layout view, displays the
page so it matches what the user sees in the browser as closely
as possible. WebObjects Builder renders elements (for example, WORepetitions)
in their collapsed form and hides comments and HTML tags.

#### Source View

Syntax coloring is new for WebObjects 4.5. By default, WebObjects
Builder displays unmatched tags in red, markers in purple, comments
in grey, and WebObjects in blue. You can change the colors using
the preferences panel.

You can match a tag in the source view by triple-clicking
on it. For example, if you want to select a `<FONT
FACE=...>` tag, the closing `</FONT>` tag,
and everything in between, triple click on `<FONT`, `>`,
or `</FONT>`. You
can also drag the mouse after you have triple-clicked, which expands
the selection by whole containers.

### Changes to the Binding Process

The process of binding is more flexible, streamlined, and
intuitive in this version of WebObjects Builder.

#### Inspector Appearance

The inspector now has a horizontal aspect, which is more convenient
to tile with the main window than before.

#### Documentation

Documentation for static dynamic elements is now available
from the inspector by clicking the book icon. The documentation
appears in the WOInfoCenter.

#### Binding by Dragging

Binding by dragging from a variable to an element is now different.
Instead of opening the inspector when you release the mouse button,
WebObjects Builder now opens a menu with the element's attributes.
You can click one of these attributes or click "Connect to new binding..."
which adds a new binding.

#### Binding With the Element's Context Menu

You can bind a variable to an element's attribute by selecting
the key in the object browser and Control-clicking (right-click
in Windows NT) an element in the upper pane of the main window.
A menu appears containing a submenu with the element's attributes.
Click one of the attributes to connect it to the selected key. You
can also create a new binding by clicking "Connect to a new binding..."

#### Binding Validation

WebObjects Builder checks for required bindings that are missing
and mutually exclusive bindings that are specified. Invalid bindings
display in red in the inspector. By clicking the alert icon in the
inspector, you can access a description of the missing bindings.

#### Adding and Deleting Bindings with the Inspector

A pull-down list in the top right corner of the inspector
allows you add and delete bindings. You can also add a binding by
selecting the inspector and pressing Enter. You can delete a binding
by selecting the binding and pressing the delete key.

#### Binding Aids in the Inspector

Creating bindings for date formats, number formats, booleans,
image file names, framework names, page names, direct actions, and
direct action classes is now easier. When WebObjects Builder can
determine a set of possible values for an attribute, it displays
a combo box for the attribute that allows you to choose one of these
values. For example, boolean attributes have a combo box which allows
you to choose YES or NO.

#### Binding Name Completion

When you inspect an element, double-click in the binding column,
and start typing a key, WebObjects completes the name for you based
on the keys in the object browser. For example, to bind to "application.allGuests.count,"
you simply type "a.a.c" and the inspector fills in the rest.
The object browser also selects the key as you type it.

### Working with Keys

The keys pull-down list at the bottom left corner of the main
window manipulates keys in the component's script file only. It
does not affect keys in the application or session files. You can
add keys to the application (or session) with the application's
context menu by selecting `application` (or `session`)
and Control-clicking (right-clicking in Windows NT) in the next
column of the object browser.

You can now rename and delete keys in the component's script
file using the keys pull-down list. To delete or rename a application
or session key, Control-click (right-click in Windows NT) on the
key and choose Delete _key_ or Rename _key_ from
the pop-up menu.

### Changes to Keyboard Actions

The tables below show the changes to the keys you need to
press to perform certain WebObjects Builder functions.

__Layout View Keyboard Actions__

|  | __Pre-WebObjects 4.5__ | __WebObjects 4.5__ |
| Insert Paragraph (`<P>`) | Shift-Enter | Enter |
| Insert Line Break (`<BR>`) | Enter | Shift-Enter |
| Delete Text | Backspace, Delete, or Del | unchanged |
| Delete Structures | Backspace, Delete, or Del | Shift-Backspace, Shift-Delete, or Shift-Del |
| Add New List Item | Shift-Enter | Enter |

### Working with Tables

Creating and editing tables is substantially changed and more
intuitive in this version of WebObjects Builder.

#### Creating Tables

To create a table, click the table icon in the toolbar. You
can set the dimensions, size, layout, and other parameters for your
table in the panel that appears. Press OK to insert the table.

#### Making Selections

In previous versions of WebObjects Builder, the inspector
had a path view. In this version, the path view is in the main window.
Thus, selecting the entire table or a single row is done differently
in this version. If you select a table cell, you can inspect the
row (by clicking <TR> in the path view) or the table itself
(by clicking <TABLE> in the path view).

You can select multiple cells by

- clicking in a cell and dragging across the cells
- selecting a cell and shift clicking in another cell
- command (control in NT) clicking each cell.

The first two selection methods ensure that the selected cells
form a contiguous region.

Note: selecting all of the cells in a row or table is not
the same as selecting the row or table!

#### Editing Tables

The structure/content table editing modes have been eliminated.
Click in a cell to edit its contents. The table data and table row
inspectors now have buttons to edit the table's structure.

### Working with Fonts

In HTML, the FACE attribute for the FONT tag specifies a comma
separated list of font names in order of preference. The browser
searches for an installed font with a corresponding name in the
list. WebObjects Builder provides a font panel which manipulates
these lists. This font panel is available from the font pull-down
list in the toolbar.

To delete a font list, select it in the font panel and press
the delete key.

### Path View Menu

Control-clicking (right-clicking on Windows NT) an element
in the path view brings up a menu from which you can

- inspect the element
- make the element a static element (if it is a dynamic element)
- make the element a dynamic element (if it is a static element)
- delete the element and its contents
- delete the element's contents only
- delete the element without deleting its contents (unwrapping
  the element)
- isolate the selection (wrap the selected content in the parent
  element separately from the unselected content.)
- make many kinds of selections.

### Context Menus

The path view menu is one example of context menus. These
menus appear when you control-click (right-click on Windows NT)
on elements or keys in the WebObjects Builder window. The following
parts of the user interface have context menus:

- elements in the upper pane of the layout and
  preview views
- elements in the path view
- keys in the object browser
- the empty space in the columns of the object browser
- the empty space in the upper pane of the layout and preview
  views
- the table views, including the Attribute/Binding table in
  the inspector, and the Bindings and Messages tables in the API editor.

### API Editor

A graphical API editor is now accessible by clicking the puzzle
piece icon on the toolbar. It allows you to define the attributes
and binding rules for a reusable component. The editor has three
panels, one for creating bindings and setting attributes on them,
one for creating validation rules, and one for associating an icon
and documentation file with the component.

The Bindings tab allows you set up the attributes of your
reusable component. WebObjects Builder displays these attributes
in the inspector in WebObjects Builder. You can also tell WebObjects
Builder which attributes must be bound, which attributes must be
bound to a key that can be set, and the kind of values each attribute
takes (such as page names, MIME types, or frameworks).

The Validation
tab allows you to set up validation rules for the component. These
rules specify which attributes must be bound together and which
cannot be bound together. The "required" and "will set"
checkboxes on the first tab are really shortcuts for setting up validation
rules; the generated rules appear on the Validation tab when you
check those checkboxes for your attributes. You can also set up
more complex rules on the Validation tab. For example, you can specify
that a set of attributes all control the same basic property of
a component and only one of them may be bound at a time.

The Display
tab allows you to choose an image that WebObjects Builder uses to
display the reusable component in a document. You can also specify
an HTML documentation file for the reusable component with the Display
tab. WebObjects Builder displays this file in the WOInfoCenter when
the user clicks the book icon in the component's inspector.

### Syntactic and Semantic Constraints

WebObjects Builder optionally enforces constraints defined
by the HTML 3.2 specification published by the World Wide Web Consortium
(W3C). The W3C maintains the standards governing the World Wide
Web. Their website is at
http://www.w3.org.

While mainstream browsers tolerate many HTML errors,
WebObjects Builder's Layout view does not allow you to introduce
semantic errors (although the Source view allows you to create and
edit any HTML). If your document already has HTML errors, you can still
edit it with the Layout view depending on the settings in your Validation
preferences panel. This panel allows you to specify what WebObjects
Builder does when it encounters semantic or syntactic errors when
it tries to display the document in the Layout view.

Semantic errors
occur when an HTML tag cannot be a child of another tag. For example, according
to the HTML 3.2 specification, <B> cannot have <H1>
as a child because <B> is a text-level tag, while <H1>
is a block-level tag. Close tags without corresponding open tags
and open tags without corresponding close tags are also semantic
errors.

Syntactic errors occur when your HTML is malformed, for example,
<//B> or <B.

Depending on the settings in the Validation
preferences panel, WebObjects Builder automatically repairs each
error it encounters, ignores it, or asks you what to do with it. Note
that there are some errors for which WebObjects Builder cannot accommodate
the settings you have chosen. For example, a document with two <BODY>
tags can neither be repaired nor ignored.

If you choose to repair
errors, WebObjects Builder adds missing close tags, and removes extra
or malformed tags. When one tag is not allowed as a child of another,
WebObjects Builder introduces an intermediate element between the
two incompatible elements or adds a close tag for the parent element
depending on the context. These repairs can be complicated and intrusive,
so you should not routinely allow WebObjects Builder to repair all
errors.

If you choose to ignore errors, WebObjects Builder does not
modify your document. To see the errors in your document from the
Layout view, bring up the validation panel.

If you choose to have
the Builder ask about errors, it stops at every error it encounters
as it tries to display your document in the Layout view and asks
you whether you want to repair the error, ignore it, or stop and
display the document in the source view. Note that if you repair
some errors and then stop on one, the errors that you repaired revert
to their original (incorrect) state; WebObjects Builder does not
modify the document unless every error is either repaired or ignored.

One common semantic violation seen in WebObjects HTML templates
is improperly nesting tags within a WOConditional. For example:

> ```
> <WEBOBJECT NAME=Conditional1>
>     <B>
> </WEBOBJECT>
> This text is conditionally displayed in boldface.
> <WEBOBJECT NAME=Conditional1>
>     </B>
> </WEBOBJECT>
> ```

The corresponding entry in the bindings file is:

> ```
> Conditional1: WOConditional {
>     condition = myCondition;
> }
> ```

Not only is this a semantic violation, it is also bad coding
practice. It is much better to use a WOGenericContainer in such
cases:

> ```
> <WEBOBJECT NAME=Generic1>
>     This text is conditionally displayed in boldface.
> </WEBOBJECT>
> ```

The corresponding entry in the bindings file is:

> ```
> Generic1 : WOGenericContainer {
>     elementName = "B";
>     omitTags = myNegatedCondition;
> }
> ```

Note that you have to negate the original condition.

### How WebObjects Builder Handles Bindings Files

WebObjects Builder now respects bindings (`.wod`)
files that have been edited by hand. Specifically, if you edit the
bindings file of your component with a text editor, open the component
in WebObjects Builder, and save it, WebObjects Builder

- preserves the whitespace and comments around
  entries in the bindings file
- retains the order of the entries (depending on the settings
  in the `.wod` preferences
  panel)
- allows a single entry to be used multiple times in the HTML
  template file

This behavior of WebObjects Builder eases the transition from
hand-editing components with a text editor to using WebObjects Builder.

## Direct to Web Changes

Direct to Web has received two major changes: exposed API
and support for creating your own visual style. There are many additional
changes as well. This version of Direct to Web is not completely
compatible with the 4.0 release. You need to run conversion scripts
on your project's source files, `Main.wod` file,
and rule (`.d2wmodel`)
files. See ["Converting Projects From Earlier Releases"](#apple-ijcusrceizeuc).

### API and Components Exposed

One of the major goals of the 4.5 release is to make more
of Direct to Web available to developers. The API and components
have been reviewed and streamlined and are now ready for public
use. In addition, two books have been added to the documentation
about Direct to Web.

_Developing WebObjects Applications With Direct to
Web_ discusses the Direct to Web architecture and how
to customize your Direct to Web application.

The _Direct to Web Reference_ covers the
classes and reusable components in the Direct to Web Framework.

You can access these documents from the WOInfoCenter.

### Modifying the Visual Style

It is now possible to create your own Direct to Web-style
dynamic template. When generating a 'task' page (for example, the
List Page for _all_ entities) Direct To Web generates a
page that is not specific to a particular entity (unlike freezing
a page). Instead, the page retains its dynamic capabilities and
reacts to the entities it encounters at runtime. You can also access
and modify its template, binding, and Java source files. By creating
a set of these for all the common tasks (query, list, edit, etc.)
you can create your own look.

Note that you can still freeze a Direct to Web page for a
particular task and entity as you could in previous releases.

### Modifying the D2W Menu

The Navigation tool of Direct to Web is now part of your project
when you create it. This allows you to tailor its look and functionality.

### Neutral Look

A new look, called the Neutral look, is now available when
you create a Direct to Web project. It is ideal for adding your
own logo because it contains no Apple or WebObjects logos.

### Custom Components

It is now possible to embed regular WebObjects components
in a Direct to Web page. Two components, D2WCustomComponent and
D2WQueryCustomComponent, have been added for this purpose.

From the Web Assistant, you can configure Direct to Web to
use your component for a particular task and property. See _Developing
WebObjects Applications with Direct to Web_ for more information.

### Named Configurations

Once you have configured a given page (for example, List page
for Movies) you can save those settings under a name (for example,
ListRentedMovies) and use this configuration from your code (either
by API or as an embedded component). This lets you have several pages
for the same task/entity pair which display different sets of properties.
For example, the Rental Store example uses different List Pages
for Movies depending whether you are a customer or a clerk, and
whether you are renting a movie or just browsing.

### Tab Panel Page

A tab panel inspect and edit page has been introduced in the
WebObjects and Neutral looks, which lets you group property keys
in different tabs. This page is not available in the Basic look.

### Better Support for Key Paths in the Web Assistant

The Web Assistant now sports a key-path browser which lets
you add a property based on a key path to any D2W page.

### Web Assistant Support for EOProject Parser

The Web Assistant now uses EOProject to parse your source
code (much like WebObjects builder does) and display custom keys
available on your Enterprise Objects in its key-path browser.

### Confirmation Page

A new confirmation page has been introduced. The list page
uses it before deleting an object. It can be frozen like any other
D2W page.

### Deployment Performance

The caching mechanism for D2W dynamic components has been
rewritten resulting in a twofold to fivefold deployment performance
improvement.

### Converting Projects From Earlier Releases

Since the D2W components are now public, the Java source files,
the `Main.wod` file, and
the rule files have changed in this release. Two scripts are provided
to ease the conversion process.

The first script, located in `$(NEXT_ROOT)/Developer/Java/Conversion/WebObjects/D2W4_5codechanges.tops`,
modifies the code to conform to Direct to Web's API changes (see [API Changes](#apple-incuorcdjfbuq)). You need
to execute it on

- all code generated by releases of Direct to Web
  earlier than 4.5
- the project's `Main.wod` file

A ReadMe file in the script's directory explains how to
execute the script.

The second script, located in `$(NEXT_ROOT)/Developer/Java/Conversion/WebObjects/D2W4_5modelchanges.tops`,
modifies the rule files to use renamed property-level components.
You need to execute it on all files in your project ending in `.d2wmodel`.
See the ReadMe file in the script's directory to see how to execute
the script.

### API Changes

The NextPageCallback interface has been renamed to NextPageDelegate.
This change affects any code that uses this interface including
code generated when you freeze a component with WebObjects 4.0.
The following methods are changed.

__ConfirmPageInterface__

| __Removed API__ | __Replacement API__ |
| setConfirmCallback | setConfirmDelegate |
| setCancelCallback | setCancelDelegate |

__EditPageInterface, EditRelationshipPageInterface, InspecPageInteface, ListPageInterface, and QueryPageInterface__

| __Removed API__ | __Replacement API__ |
| setNextPageCallback | setNextPageDelegate |

__SelectPageInterface__

| __Removed API__ | __Replacement API__ |
| nextPageCallback | nextPageDelegate |
| setNextPageCallback | setNextPageDelegate |

References to the Live Assistant have been changed to Web
Assistant. Consequently, the following methods are deprecated.

__D2W__

| __Deprecated API__ | __New API or Workaround__ |
| isLiveAssistantEnabled | `isWebAssistantEnabled` |
| setLiveAssistantEnabled | `setWebAssistantEnabled` |

__D2WComponent__

| __Deprecated API__ | __New API or Workaround__ |
| isLiveAssistantEnabled | `isWebAssistantEnabled` |

[!](What%27s%20New%20in%20WebObjects%204.5.md)
