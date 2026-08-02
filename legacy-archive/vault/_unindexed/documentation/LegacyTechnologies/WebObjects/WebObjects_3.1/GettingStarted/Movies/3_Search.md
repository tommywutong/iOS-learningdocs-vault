---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Movies/3_Search.html
archived_at: '2026-07-15T07:49:01.429854Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Movies.book.md) [!Previous Section](2_Main.md)

# Add a search page

The Database Wizard can also set up pages for searching the database. In this section, you'll create a page that allows you to search for movies that match criteria you specify.!
You can insert, update, and delete movies with this page the same way you do in Main. Not surprisingly, the steps for creating the search page are very similar to those for creating Main.

## Create a component

- Bring the Movies application window to the front.
- Click the Component tab.
- Click the plus button.
- Type __MovieSearch__ as the name of the component.
!

## Run the Database Wizard

Activate the wizard from the MovieSearch component window. You'll perform the same steps you did for the Main component, except this time you'll:

- Use the model you created for the Main component instead of creating a new model.
- Choose the Matching Records layout option instead of Paginated 10 per page.
- Choose attributes on which to match in a window that only opens when you choose the Matching Records layout.

- In the Database Wizard's Specify a model file panel, click Browse to locate the model file.

When you created the Main page, you created a new model file with the Database Wizard. The wizard saved the model in the Movies application directory. When you run the Database Wizard this time, you can specify that model file.

- In the Open panel, navigate to the __Movies.woa__ directory.

A model file is actually a directory, or _file package_, that contains a collection of files that shouldn't be separated. A model's file package has the extension __.eomodeld__ (for eomodel _directory_).

- Select the directory with the extension __.eomodeld__.

__For Mach Users Only:__ WebObjects application directories such as __Movies.woa__ are also file packages. Ordinarily you can't see the contents of a __.woa__ directory in the Workspace File Viewer, in Open panels, or in Save panels. To select the model file in the Database Wizard's open panel, bring the Workspace File Viewer to the front. Navigate to your __Movies.woa__ application directory, and choose File ! Open as Folder. The Workspace opens a new viewer window that's focused on the contents of the __Movie.woa__ directory. Select the model file package, and drag it into the Database Wizard's Open panel.

!- In the Choose an entity panel, select the Movie entity.

Model files store database login and primary key information, so when you run the Database Wizard this time, it doesn't prompt you with a Choose Adaptor panel, a login panel, or a Choose a Primary Key panel.

- Choose the Selected Record and Matching Records layout options.

As you can see in the Choose a layout panel's page preview, the Matching Records option generates a database search form in which users can specify record-matching criteria.

- Choose the same attributes to display: __title__, __category__, __rating__, __dateReleased__, and __revenue__.
- Choose the __title__ attribute to display on the hyperlink.

When you choose the Matching Records layout option, you must tell the Database Wizard what attributes to put in the query form.

- Select __title__, __category__, and __rating__ as the attributes on which to match.

As before, the Database Wizard designs a functional page, but this one allows you to search the database for a movie that matches criteria you specify. It again uses a WODisplayGroup to not only fetch objects from the database, but also to build the query.

## Add date and number formats

- Add the date format __"%d %b %Y"__ to the dateReleased text field.
- Add the number format __"$ #,##0.00"__ to the revenue text field.

## Change the display group options

- Open the DisplayGroupEditor for the MovieSearch component's __movies__ variable.
- Deselect the Fetches on load option.
- Set the sort order as you did for the Main component.
!

Notice that you're configuring this __movies__ display group differently than you did the Main page's display group. The Main page had Fetches on load selected and its Entries per batch was set to 10. MovieSearch has Fetches on load deselected, and its batch size is 0.
When Fetches on load is selected, the display group fetches records from the database when the component is loaded into the application. You want this feature in the Main page so that your users are immediately presented with a list of movies when they start the application. In contrast, the MovieSearch page should not present a list of movies until the user has entered search criteria and clicked Match. Thus, you deselect Fetches on load so that the movie list is not displayed until the query is performed.
Entries per batch specifies the number of records the display group displays at a time. When this number is 0, as it is in the MovieSearch page, the display group won't display search results in batches. Instead, all the movies that match a user's search criteria are displayed at once. In Main, the batch size is 10 and you use the Next Page and Previous Page buttons to page through the results. The Database Wizard set the batch size to 10 for the Main page because you specified the Paginated 10 per page option when you created it. The Database Wizard sets the batch size to 0 for all other page layout options.

## Specify page transitions

Now your application needs a way for users to get to the MovieSearch page from the application's Main page. To provide it, add a hyperlink to the Main component that opens the MovieSearch page.

- In the Main component window, place the cursor at the bottom of the page below the horizontal line.
- Drag a Hyperlink from the Abstract Elements palette into the component window.
!- Select the word "Hyperlink" and type __Movie Search__ in its place.
- In the hyperlink bindings inspector, set the __pagename__ attribute to __"MovieSearch"__.

The __pagename__ binding is a mechanism for navigating to another page. By setting the attribute to __"MovieSearch"__, you're telling the application to open the MovieSearch page when the hyperlink is clicked.

A user should also be able to get back to the Main page from the MovieSearch page.

- Create a hyperlink labeled "Browse Movies" in the MovieSearch page that opens the Main page.

## Save and run your application

Reload the Main page in your web browser to get the Movies application to load the new Movie Search link. In the Movie Search page, try searching for movies that match the word "The." Notice that the Movies application locates only movies that _begin_ with the string "The" as oppoed to _containing_ the string "The".

- Using the DisplayGroupEditor, change the qualification mode for the __movies__ display group.

How does the qualification mode affect searching in the Movies application?

[!Table of Contents](Movies.book.md) [!Next Section](4_Detail.md)
