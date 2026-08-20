---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/Adding_a_Ne_Application.html
archived_at: '2026-07-15T08:12:23.580532Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Modifying_a_eb_Template.md)[![Next](attachments/DirectToWeb/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Appendix/index.html)

## Adding a New Direct to Web Task to Your Application

A Direct to Web application can be expanded to handle new
tasks. This section describes how to add an example task called
edit-list. The edit-list task page looks like a regular list page
but renders the data in text fields so the user can edit the data.
To create a task and use it in a Direct to Web application you need
to

- create the
  Direct to Web template that executes the task
- add rules to configure the default behavior of the page and
  make it available to the Web Assistant
- add a hyperlink to an existing Direct to Web template that
  links to the new task page

Once you have added the task, you can use it with any entity
and configure it with the Web Assistant.

### Creating the Direct to Web Template

The easiest way to create a Direct to Web template is to modify
one that the Web Assistant generates. The edit-list page most closely
resembles the list page.

1. For this
   example, begin with the project you created in the last section, ["Modifying a Direct to Web Template"](Modifying_a_eb_Template.md#apple-ijbusqsdjfeuk). You should have a modified NEUListPage2
   Direct to Web template in your project.
2. Create a Direct to Web template called "NEUEditListPage"
   based on the NEUListPage by following steps 2-4 in ["Modifying a Direct to Web Template"](Modifying_a_eb_Template.md#apple-ijbusqsdjfeuk).
3. Open `NEUEditListPage.wo` in
   WebObjects Builder. Follow the directions below to modify the template.
4. Remove the first and last columns of the main table. The left
   column contains an icon that opens the edit page. The right column
   contains an icon that deletes the record. Since the list page provides
   these functions, they are not duplicated on the edit-list page.
5. Now wrap the main table inside a WOForm. The easiest way to
   do this is to use the source view. Find the line

   ```
   <WEBOBJECT NAME=NavBar></WEBOBJECT>
   ```

   Change
   it to

   ```
   <WEBOBJECT NAME=NavBar></WEBOBJECT><WEBOBJECT NAME=Form1>
   ```

   Find
   the first `</CENTER>` tag
   in the file. Add a closing `</WEBOBJECT>` above
   this line.
6. In the next three steps, you change the Return hyperlink into
   a submit button and add a Save submit button that saves the changes
   to the database. Find the line

   ```
   <WEBOBJECT NAME=ShowCancel><WEBOBJECT NAME=BackLink><WEBOBJECT  NAME=ReturnButton></WEBOBJECT></WEBOBJECT></WEBOBJECT>
   ```

   Add

   ```
   <WEBOBJECT NAME=SubmitChanges></WEBOBJECT>
   ```

   between
   the last two `</WEBOBJECT>` tags.
   The line should now look like this:

   ```
   <WEBOBJECT NAME=ShowCancel><WEBOBJECT NAME=BackLink><WEBOBJECT  NAME=ReturnButton></WEBOBJECT></WEBOBJECT><WEBOBJECT NAME=SubmitChanges></ WEBOBJECT></WEBOBJECT>
   ```
7. In the bindings file, find the bindings for the ReturnButton
   WebObjects element. Change it so it reads as follows:

   ```
   ReturnButton: WOImage {
       alt = "Cancels changes";
       border = "0";
       filename = "CancelMetalBtn.gif";
       framework = "JavaDirectToWeb";
       name = "Cancels changes";
   }
   ```
8. Add the following bindings to the bindings file:

   ```
   Form1: WOForm {
       action = backAction;
   }

   SubmitChanges: WOImageButton {
       action = saveChanges;
       alt = "Saves your changes";
       border = "0";
       filename = "SaveMetalBtn.gif";
       framework = "JavaDirectToWeb";
       name = "Saves your changes";
   }
   ```

   The `backAction` method
   is defined by the NEUEditListPage component's superclass, D2WListPage.
9. Switch back to the layout view to check for HTML syntax errors.
10. Save the NEUEditListPage.wo file.
11. Modify `NEUEditListPage.java` by
    adding the saveChanges method defined in [Listing 4-6](#apple-ijauescejbeuq).__Listing 4-6 Implementation
    of the saveChanges method in NEUEditListPage.java__

    ```
    public WOComponent saveChanges() {
        WOComponent nextPage = this.nextPage();
        try {
            session().defaultEditingContext().saveChanges();
        } catch (Exception exception) {
            ErrorPageInterface epi = (ErrorPageInterface)
                D2W.factory().errorPage(session());
            epi.setMessage(exception.toString());
            epi.setNextPage(this);
            nextPage = (WOComponent)epi;
        } finally {
            return nextPage;
        }
    }
    ```

This Java code tries to save changes to the session's editing
context. If it fails, it returns an error page. Otherwise, it returns
to the page that called it.

### Adding Rules to Define the Default Behavior

When a Direct to Web application launches, it looks for rules
in two files in your project, `user.d2wmodel` and `d2w.d2wmodel`,
and merges them with the rules defined in the Direct to Web framework.
The Web Assistant modifies the rules in the `user.d2wmodel` file.
For basic customization tasks you don't need to edit this file
by hand. When you add rules that change the default behavior of
your application, you modify the `d2w.d2wmodel` file.

Defining the default behavior of a new task page also informs
the Web Assistant of the new task. Specifically, the Web Assistant
collects a list of tasks based on the task = "_taskName_" clauses
on the left-hand side of rules.

Direct to Web provides an application called RuleEditor to
edit the rules.

For the edit-list page example, you need to

- revise the
  Web Assistant rules in the `user.d2wmodel` file

  The
  Web Assistant created two rules when you generated the NEUEditListPage
  Direct to Web template. These rules state that the NEUEditListPage
  can and should be used with the list task. Since you are creating
  an edit-list task, which exclusively uses the NEUEditListPage Direct
  to Web template, these rules must be changed.
- create a `d2w.d2wmodel file` and
  put rules that define the edit-list page default behavior in it

#### Modifying the Web Assistant Rules

1. Quit the
   Web Assistant if it is still running. You will modify the `user.d2wmodel` file
   using the Rule Editor instead of the Web Assistant because the Web
   Assistant can't perform the change.
2. From Project Builder, Control-double-click `user.d2wmodel` in
   the Resources group to invoke the Rule Editor.

   The top half
   of the window lists the rules. The bottom half of the window edits
   the selected rule.
3. Select this rule:

   ```
   ((task = "list") and (look = "NeutralLook"))
       => pageAvailable = "NEUEditListPage"
   ```

   by
   clicking on it. Click Delete. The NEUEditListPage is not available
   to perform the list task.
4. Select this rule:

   ```
   (task = "list") => pageName = "NEUEditListPage"
   ```

   In
   the Value text field in the bottom right corner of the screen, enter `"NEUListPage2"` (including
   the quotation marks) and press Return. Direct to Web displays a NEUListPage2
   component as the default list page.
5. Save the rule file.

   Choose File > Save.

#### Adding New Default Rules

1. Create a
   new rule file.

   In RuleEditor, choose File > New.
2. Click New to create a new rule.

   The first rule you add
   is

   ```
   (task = "editList") => displayPropertyKeys =
       "defaultPropertyKeysFromEntityWithoutRelationships"
   ```

   using
   the DefaultAssignment class. The rule's priority is 50, which
   overrides the default Direct to Web framework rules but not the
   Web Assistant rules.

   This rule specifies that the properties
   on the edit-list page include the entity's attributes but not
   its relationships. The `defaultPropertyKeysFromEntityWithoutRelationships` method
   is defined in the DefaultAssignment class in the Direct to Web framework.
3. In the first line of the browser labeled "Left-Hand Side,"
   enter `task`. Click the
   button with the equal sign. Now type `'editList'` (including
   the quotation marks) and press Enter.

   Choose Custom from the
   Class pop-up list and enter `com.webobjects.directtoweb.DefaultAssignment` in
   the Custom text box. The DefaultAssignment class contains methods
   that derive values from the state in the Direct to Web context.

   Enter `displayPropertyKeys` in
   the Key text box.

   Enter `defaultPropertyKeysFromEntityWithoutRelationships` in
   the Value text box.

   Enter `50` in
   the Priority text box.
4. Add the following rules by repeating step 3. All of the rules
   have a priority of 50 and use the Assignment class (not the DefaultAssignment
   class). Assignment is available in the Class pop-up list; do not
   choose Custom.

   This rule specifies that the NEUEditListPage
   Direct to Web template can be used to display an edit-list page:

   ```
   (task = "editList") => pageAvailable = "NEUEditListPage"
   ```

   This
   rule specifies that the default edit-list Direct to Web template
   is NEUEditListPage:

   ```
   (task = "editList") => pageName = "NEUEditListPage"
   ```

   This
   rule specifies the name of the banner for the edit-list page:

   ```
   (task = "editList") => bannerFileName = "EditMetalBan.gif"
   ```

   The
   following rule specifies that the D2WEditString property-level component
   can be used to edit strings on the edit-list page. To enter the
   left-hand side, use the And and Not buttons.

   ```
   ((task = "editList") and (not (attribute = null))
       and (attribute.className = 'java.lang.String'))
       => componentAvailable = "D2WEditString"
   ```

   This
   rule specifies that the default property-level component that edits
   strings on an edit-list page is D2WEditString:

   ```
   ((task = "editList") and (not (attribute = null))
       and (attribute.className = "java.lang.String"))
       => componentName = "D2WEditString"
   ```

   This
   rule specifies that the D2WEditNumber property-level component can
   be used to edit numbers on the edit-list page:

   ```
   ((task = "editList") and (not (attribute = null))
       and ((attribute.className = "java.math.BigDecimal")
           or (attribute.className = "java.lang.Number")))
       => componentAvailable = "D2WEditNumber"
   ```

   This
   rule specifies that the default property-level component that edits
   numbers on an edit-list page is D2WEditNumber:

   ```
   ((task = "editList") and (not (attribute = null))
       and ((attribute.className = "java.math.BigDecimal")
           or (attribute.className = "java.lang.Number")))
       => componentName = "D2WEditNumber"
   ```

   This
   rule specifies that the D2WEditDate property-level component can
   be used to edit dates on the edit-list page:

   ```
   ((task = "editList") and (not (attribute = null))
       and (attribute.className = "com.webobjects.foundation.NSTimestamp"))
       => componentAvailable = "D2WEditDate"
   ```

   This
   rule specifies that the default property-level component that edits
   dates on an edit-list page is D2WEditDate.

   ```
   ((task = "editList") and (not (attribute = null))
       and (attribute.className = "com.webobjects.foundation.NSTimestamp"))
       => componentName = "D2WEditDate"
   ```
5. Save the file as `d2w.d2wmodel` in
   the top-level directory of your project.
6. Add the `d2w.d2wmodel` file
   to your project.

   Choose Project > Add Files.

   Select
   the `d2w.d2wmodel` file
   created in the previous step and click Open.

   Select
   the Application Server target and click Add.

### Adding a Hyperlink to the New Task Page

Now that Direct to Web can display the edit-list task page,
you need to add a hyperlink to the list page to bring up the edit-list
page.

1. Modify the
   editList method in `NEUListPage2.java` so
   it matches the implementation in listing below:
   __Listing 4-7 Implementation
   of the editList method in NEUListPage2.java__

   ```
   public ListPageInterface editList {
       ListPageInterface lpi = (ListPageInterface) D2W.factory().
           pageForTaskAndEntityNamed("editList",entity().name(),
           session());
       lpi.setNextPage(this);
       lpi.setDataSource(displayGroup().dataSource());
       return lpi;
   }
   ```

   The
   edit-list page uses the same interface as the list page (ListPageInterface)
   because the pages are very similar. The action method `editList` creates
   a new page using `pageForTaskAndEntityNamed` because
   the factory has no special method to create an edit-list page. You
   could add such a method if you like. See ["Modifying the Direct to Web Factory"](Modifying_t_Web_Factory.md#apple-ijbusqsdjbces).

   To
   specify the page to display when the user cancels the edits, the
   action method invokes `setNextPage`.
   When the user clicks the Cancel button, this list page will display. Finally,
   the action method sets the data source for the display group so
   it matches the list page's data source. This ensures that the
   edit-list page displays the same objects the list page displays.
2. Build and launch your application. Navigate to a list page.
   Click the Edit button.

   The edit-list page should appear. You
   can type in a field to edit its contents. If you click cancel, the
   edits are discarded. If you click save, the edits are saved to the
   database. You can page through the displayed objects with the navigation
   bar at the top of the screen. When you move from one page to another,
   the edit-list page discards the edits.
3. You can use the Web Assistant to further customize the edit-list
   page.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Modifying_a_eb_Template.md)[![Next](attachments/DirectToWeb/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Appendix/index.html)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
