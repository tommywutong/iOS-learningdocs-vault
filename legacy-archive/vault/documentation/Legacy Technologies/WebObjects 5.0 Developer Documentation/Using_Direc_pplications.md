---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/Using_Direc_pplications.html
archived_at: '2026-07-15T08:12:23.674074Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Adding_a_Lo_o_Web_Pages.md)[!](Modifying_t_Web_Factory.md)

## Using Direct to Web in Other WebObjects Applications

WebObjects applications that were not generated using the
Direct to Web option in the wizard can use the Direct to Web framework to display
query, list, edit, and other pages in the Direct to Web repertoire. Making use of
Direct to Web can be a convenient shortcut for many applications when all they
need is a standard database-related page. They can use Direct to Web in one of
two ways:

- by embedding Direct to Web components in the
  pages of their application
- by linking to a dynamically created
  Direct to Web page and appropriately implementing the action method invoked when
  the link is clicked

### Embedding Direct to Web Components

Using a Direct To Web component is
not much different than using any other reusable component. The procedure is the
following.

1. Add the Direct to Web and the Direct to Web
   Generation frameworks to your project. The path for these frameworks is
   /System/Library/Frameworks and the file names are
   `JavaDirectToWeb.framework`, `JavaDTWGeneration.framework`,
   and `JavaEOProject.framework`.
2. Decide which Direct to
   Web component you want to use and become familiar with its API.

   See "Direct to
   Web Reusable Components" in the _Direct to Web Reference_ for summaries of
   these components.
3. Put a WebObjects tag for the component in
   the page that is to display it.

   ```
   <WEBOBJECT
   NAME=MyD2WQuery></WEBOBJECT>
   ```

   This is a step you can complete in
   WebObjects Builder. The reusable components are available from the "DirectToWeb"
   palette.
4. Make the appropriate bindings for the component.

   ```
   MyD2WQuery: D2WQuery { entityName="Movie"; displayKeys="( title, roles,
   studio.budget )"; queryDataSource=movieDisplayGroup.dataSource; }
   ```

   All
   embedded components require an `entityName` binding to specify the
   entity the page works with. Extra bindings could be required, depending on the
   functionality of the page. For example, List pages require a
   `dataSource` binding. If you want to use a named configuration,
   specify it with a `pageConfiguration` binding. See ["Named Configurations"](WebAssistant_Expert_Mode.md#apple-ijaueq2kirbug) for
   more information about named configurations.

   You can also complete this
   step in WebObjects Builder.
5. If necessary, implement the
   action method for the component.
6. You can customize embedded
   Direct to Web components using the Web Assistant. You can launch the Web
   Assistant using the `appletviewer` tool.

   When the Web Assistant
   acts upon an application that was not generated using Direct to Web, it does not
   automatically track which page is displayed. Thus you must set the task and
   entity for the page you want to modify in Expert mode. For example, if you want
   to customize a list page for Movies, click Expert mode and select the list task
   and the Movie entity. You can then customize a component in the same way you
   customize Direct to Web pages. Also, when you click Update to send the new
   settings to the application, the browser does not automatically refresh your
   page. You must either click the Reload button in your browser or (especially when
   you select a new task or entity) you must renavigate to the
   page.

By default, your component appears
in the Neutral look.

### Linking to a Direct to Web Page

The second way to use Direct to Web in you application is
to link directly to a dynamically generated page of the appropriate type. The D2W
class defines methods that create components (inspect, query, list, and so on)
defined for an entity in a session. The returned component objects implement the
appropriate interface:

```
QueryPageInterface queryPageForEntityNamed
(String entity, WOSession session); ListPageInterface listPageForEntityNamed
(String entity, WOSession session); EditPageInterface editPageForEntityNamed
(String entity, WOSession session); InspectPageInterface
inspectPageForEntityNamed (String entity, WOSession session); SelectPageInterface
selectPageForEntityNamed (String entity, WOSession session);
EditRelationshipPageInterface editRelationshipPageForEntityNamed (String entity,
WOSession session); QueryAllPageInterface queryAllPage (WOSession session);
```

To create a named configuration page, you use the
method

```
WOComponent pageForConfigurationNamed (String
namedConfiguration, WOSession session);
```

To link to a
Direct to Web page, you need to implement an action method that returns a Direct
to Web component implementing the appropriate page interface.

#### Implementing the Action Method

To implement the action methods
that link to Direct to Web pages, you must use methods of the D2W class and the
page-specific Direct to Web interfaces. You also need to specify a hyperlink,
active image, or similar HTML control that invokes the action method. The
following example shows such a hyperlink; first, the `WEBOBJECT` tag
in the HTML template file:

```
<WEBOBJECT name=D2WListPage>D2W
list page</WEBOBJECT>
```

Then, in the
`.wod` file, bind the hyperlink to the `d2wList` action
method:

```
D2WListPage: WOHyperlink { action = d2wList; }
```

The action method must return a component (that is, a
WOComponent object) that implements the interface appropriate to the required
type of page. For example, if you want to link to a dynamically generated list
page, the component returned must implement the ListPageInterface interface. The
D2W class provides methods that create such components:

```
public
WOComponent d2wList() { ListPageInterface lpi =
D2W.factory().listPageForEntityNamed("Movie",session());
lpi.setDataSource(movieDisplayGroup.dataSource()); lpi.setNextPage(this); return
(WOComponent)lpi; }
```

Notice that before you return the
component, you must set things such as the data source for the component and the
page to go to when users click Return (`setNextPage`). This example
assumes that the data you want to display is contained in the EODataSource for a
WODisplayGroup called `movieDisplayGroup`.

#### Setting Up a Next-Page Delegate

For some pages, you need to
specify the action method that navigates to the next page. Consider a component
called MyListPage that displays a list of objects and has a hyperlink that adds
objects to the list. To determine which objects to add, the component invokes a
Direct to Web query page.

The query page
behavior differs from the normal Direct to Web query page behavior in two
ways:

- Normally a query page creates a Direct to Web list
  page when the user clicks the Search DB button. In this example, however, the
  query page jumps back to the MyListPage component.
- When the query
  executes, it adds the objects to the list of objects displayed by the MyListPage
  component, an action the normal query component does not perform.

To implement this custom behavior, you need to define and
instantiate a delegate object in addition to creating the query component. The
delegate object must implement the NextPageDelegate interface and include a
method called `nextPage`, which is invoked when the user clicks the
submit button for the query page (Query DB). The query component's next page
delegate must be assigned to this object using the `nextPageDelegate`
method.

[Listing 4-1](#apple-ijaueqsfjbdee)
shows how this can be done.

__Listing 4-1
Sample code that sets up a next-page delegate__

```
public class MyListPage
extends WOComponent {

public WODisplayGroup myDisplayGroup; ...

public WOComponent showD2WQuery() { QueryPageInterface qpi =
D2W.factory().queryPageForEntityNamed("Movie", session());
qpi.setNextPageDelegate (new NextPageDelegate() { // delegate implementation
public WOComponent nextPage(WOComponent sender) { EODataSource ds =
((QueryPageInterface)sender).queryDataSource(); NSArray
objectsToAdd=ds.fetchObjects(); for (Enumeration e =
objectsToAdd.objectEnumerator(); e.hasMoreElements(); ) { EOEnterpriseObject eo =
(EOEnterpriseObject)e.nextElement); MyListPage.this.myDisplayGroup.
insertObjectAtIndex(eo,0); } return MyListPage.this; } }); return (WOComponent)
qpi; } }
```

The `showD2WQuery` method first
creates a query page component. It then creates a delegate object and sets the
query page's next-page delegate to the newly created object. Finally, the method
returns the new query page component, which causes WebObjects to display the
query page.

The next-page delegate object
contains an action method called `nextPage`, which is invoked when the
user clicks Query DB on the query page. This method gets the query data source
containing the query specification. Next, the `nextPage` method
fetches the objects matching the query specification and adds them to the display
group in the MyListPage component. Finally, it returns the MyListPage component,
which causes WebObjects to redisplay the list page.

#### Setting Up the Page Wrapper

Every application that links to a
dynamically created Direct to Web page should have a component called
`PageWrapper.wo`. This component acts as a "wrapper" for the
dynamically generated content and can have customized header and footer material.
If your application does not have a page wrapper, Direct to Web displays your
pages in an empty page wrapper. [Listing 4-2](#apple-ijauerciizceu) and [Listing 4-3](#apple-ijauersdinfeq) show how to set up the
`PageWrapper.wo` component. You can use a text editor, Project
Builder, or (preferably) WebObjects Builder to construct this
component.

__Listing 4-2 PageWrapper.html
example__

```
<HTML> <WEBOBJECT name=Head></WEBOBJECT>
<WEBOBJECT name=BodyContainer> <WEBOBJECT
name=Body></WEBOBJECT> </WEBOBJECT> </HTML>
```

__Listing 4-3 PageWrapper.wod example__

```
BodyContainer:
WOBody { filename = "Images/bkg.jpg"; framework = "DodgeDemo"; bgcolor="#c0c0c0";
TEXT = "#000000"; LINK = "#0000F0"; VLINK = "#0000F0"; ALINK = "#FF0000"; }

Head : D2WHead { _unroll = YES; }

Body: WOComponentContent { _unroll = YES; };
```

The only
required component in `PageWrapper.wo` is the WOComponentContent. The
other components shown in the example are optional, and you can create your own
header, footer, and body-container components for your dynamically generated
pages.

The `_unroll` attribute, when
set to `YES`, enables the Web Assistant to generate a static component
from the dynamically generated one.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Adding_a_Lo_o_Web_Pages.md)[!](Modifying_t_Web_Factory.md)

© 2001 Apple Computer, Inc.

Shop the [Apple Online Store](http://www.apple.com/store/) (1-800-MY-APPLE), visit an [Apple Retail Store](http://www.apple.com/retail/), or find a [reseller](http://www.apple.com/buy/locator/).

- [Mailing Lists](http://lists.apple.com/)
- [RSS Feeds](https://developer.apple.com/rss/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
