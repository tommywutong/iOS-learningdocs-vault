---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Movies/4_Detail.html
archived_at: '2026-07-15T07:49:04.593168Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Movies.book.md) [!Previous Section](3_Search.md)

# Add a detail page

The MovieDetails page shows you the detailed information about a movie you select in either the Main or the MovieSearch page. So, for example, you can choose a movie in the Main page and then click a "Movie Details" hyperlink to display the movie's details in a new page. For this to work, the Main and MovieSearch pages have to tell the MovieDetails page which movie the user selected.!
The MovieDetails page uses a WODisplayGroup object to display movie information in the same way that the Main and MovieSearch pages do. In the MovieDetails page, however, the display group manages exactly one record: the selected movie. In the other pages, the display group manages a set of many records.
The Database Wizard doesn't provide a layout option that resembles the user interface of the MovieDetails page, so in this section you'll perform by hand the tasks the Database Wizard performed to create the other two pages. You'll learn how to create a WODisplayGroup variable and how to bind it to dynamic elements. In the sections following this one, you'll extend the MovieDetails page to display movie roles and the starring actors.

## Create a component

- Add a new component to the Movies application, and name it MovieDetails.

## Open your model file

To open the model file, you need to launch EOModeler.

- In the OPENSTEP Enterprise program group, choose the EOModeler entry.

An empty model opens.

__For Mach Users Only:__ On Mach systems, the EOModeler application is in __/NextDeveloper/Apps__.

- In EOModeler, choose Model ! Open.
- In the Open panel, navigate to your __Movies.woa__ application directory.
- Select the model file inside the application directory.
- Click Open.

After your model file opens, you can close the empty model.

__For Mach Users Only:__ To open the model file, bring the Workspace File Viewer to the front. Navigate to your __Movies.woa__ application directory, and choose File ! Open as Folder. The Workspace opens a new viewer window that's focused on the contents of the __Movies.woa__ directory. Double-click the model file package to open it in EOModeler.

## Add a WODisplayGroup to the component

- Select the Movie entity in the EOModeler's Model Editor.
- Drag the Movie entity into the MovieDetails component window.
!

This creates a WODisplayGroup named __movies__. This WODisplayGroup is just like the __movies__ display groups in the other two components; it manages database records associated with the Movie entity.

## Add a setMovie: method

As stated earlier, the MovieDetails display group manages only one object: the movie selected in the previous page. The Main and MovieSearch pages need a way to set this record in the MovieDetails' display group before the MovieDetails page opens. They use the __setMovie:__ method to do this.

- In the MovieDetails component window, click the script button.
!

The script window is empty except for the following line of code, which declares the component's display group:

```
    id movies;
```

- Add the following method to the script:

```
    - setMovie:aMovie {
        if (aMovie)
            [movies setObjectArray:[NSArray arrayWithObject:aMovie]];
        else
            [movies setObjectArray:nil];
        [movies selectObject:aMovie];
    }
```


A WODisplayGroup stores the set of objects fetched from the database in its _object array_. Usually, the display group itself fetches the objects from the database. This is what happens with the display groups in the Main page and the MovieSearch page. The MovieDetails page displays information about only one object, which has already been fetched by the display group from the previous page. So __setMovie:__ sets the object array to an array containing the single object __aMovie__.

Display groups also keep track of a _selection_. Generally, a WODisplayGroup's selection is maintained programmatically. In this case, the __setMovie:__ method sets the __movies__ display group's selection to __aMovie__.

When you created the Main page, the Database Wizard set up the selection management for you. It defined a method __selectObject__ in Main's script that is invoked whenever one of the hyperlinks is clicked. __selectObject__ sets the __movies__ display group's selected object to the movie whose title is displayed by that hyperlink.

## Specify page transitions

To get to the MovieDetails page from the Main page or the MovieSearch page, users use a hyperlink. The hyperlink should invoke MovieDetails' __setMovie:__ method and then open the MovieDetails page.

- Next to the "Movie Search" hyperlink in the Main component, add a hyperlink labeled "Movie Details."
!- Add the following method to the Main component script:

```
    - showDetailsForMovie {
        id detailsPage = [[self application]
            pageWithName:@"MovieDetails"];
        [detailsPage setMovie:[movies selectedObject]];
        return detailsPage;
    }
```


This method creates the MovieDetails page and then invoke's its __setMovie:__ method with the movie that's selected in the Main page. The display group method __selectedObject__ returns its selected object, which, in the Main component, is set when a user clicks a movie title hyperlink.

- Connect the __showDetailsForMovie__ method to the __action__ attribute of the Movie Details hyperlink.
- Repeat the steps above to invoke __setMovie:__ from the MovieSearch component.

## Create the user interface

- Create the heading "Movie Details" as a centered top-level heading.

The MovieDetails page shows the title of the movie in a heading immediately below the main heading. In the next several steps, you'll create that movie title heading.

- Drag a heading element from the Static Elements palette into the MovieDetails component window.
- Double-click the word "Heading" so it's selected.
- Drag a string element from the Abstract Elements palette into the MovieDetails component window.
!

The string element is now inside the heading element. As a result, the string's value is formatted as a heading element. In the next task, you'll bind the selected movie's title to this heading string.

- Place the cursor below the heading string.
- Type __Category:__.
- Drag another string element into the MovieDetails component window.
- Select the "Category: " label.
- Click the bold button.
- Repeat the steps above to add Rating, Date Released, and Revenue labels and strings.
!

## Create bindings

Now you need to bind attributes of the selected movie to the string elements so the selected movie's information will be displayed in the MovieDetails page.

- Click inside the heading string.
- Select __movies__ ! __title__ in the component window's object browser.

The attributes shown in the object browser for the __movies__ display group are actually attributes of Movie objects (the object that the display group manages) rather than attributes of the display group itself. These attributes are provided as a convenience; they correspond to the display group's selected object. Recall that the __setMovie:__ method sets __movies__' selected object to the movie selected on the previous page.

- Double-click __title__.

Double-clicking __movies__ ! __title__ binds the title of __movies__' selected object to the heading string's __value__ attribute. The string displays the text "movies.selectedObject.title" to indicate what it is bound to.

!- Repeat the steps above to create bindings for the Category, Rating, Date Released, and Revenue strings.

## Add date and number formats

String elements have __dateformat__ and __numberformat__ attributes just like text field elements.

- Add the date format __"%d %b %Y"__ to the Date Released string.
- Add the number format __"$ #,##0.00"__ to the Revenue string.

## Add page transition links to the detail page

Now add hyperlink elements to the Movie Details page so a user can navigate to the Main and MovieSearch pages from the MovieDetails page.

- Add two hyperlink elements to the bottom of the page.
- Label one "Browse Movies" and the other one "Movie Search."
- Set the __pagename__ attributes to __"Main"__ and __"MovieSearch"__.

## Save and run your application

Reload the Main page in your web browser to get the Movies application to load the new Movie Details link. In the Main page, select a movie and click the Movie Details link. The Movie Details page should display all the movie's information.

[!Table of Contents](Movies.book.md) [!Next Section](5_Actors.md)
