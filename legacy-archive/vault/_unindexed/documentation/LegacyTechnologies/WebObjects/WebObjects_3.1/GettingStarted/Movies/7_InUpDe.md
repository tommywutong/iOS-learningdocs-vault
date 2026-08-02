---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Movies/7_InUpDe.html
archived_at: '2026-07-15T07:49:15.670789Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Movies.book.md) [!Previous Section](6_MasDet.md)

# Add the ability to modify the database

In this final section, you'll add the ability to insert, update, and delete movie roles:!
Most of the set up is done already, but you have to make one more modification to the model file, and you have to add a few more methods. In this section, you'll add methods to the MovieDetails component that:

- Select a movie role when a user clicks a link.
- Manage the selected actor for the page's browser element.
- Return the full name of an actor for display in the browser.
- Save changes to movie roles to the database.

First, you'll set up the model file so that the movie role changes propagate properly and make changes to the interface.

## Update the movieRoles relationship

The modification you need to make in the model file are to the relationship between a movie and its movie roles.

- In EOModeler, double-click the open entity icon for the Movie entity.
!- Select the movieRoles relationship in the bottom view.
- Choose Tools ! Inspector to open the Relationship Inspector.
- In the inspector, click the middle icon to display the Advanced Relationship Inspector.
!- Select the Cascade Delete Rule.
- Enable the Owns Destination and Propagate Primary Key check boxes.
- Save the model file.

Because your application can make changes to both Movie and MovieRoles and because these two entities are related, you need to make sure that the right thing happens to the Movie entity when you modify a MovieRole and vice versa.
A role in a movie cannot exist if the movie itself does not exist, so if a movie is deleted, all of its related movie roles should be deleted as well. This is what the Cascade delete option does. Owns Destination means that if you delete a movie role from the selected movie, it is removed from the database as well. (Recall that in this movieRoles releationship, Movie is called the _source entity_ and MovieRoles is the _destination entity_. Owns Destination means that Movie owns its MovieRoles.)
Next, because Movie and MovieRole share the __movieId__ primary key, you select Propagate Primary Key. Now when you insert a new movie role, that new object will automatically be assigned the __movieID__ of the selected movie.

## Add a hyperlink around the role name string

Now you need to make the role name a hyperlink so that users can select it. When the user clicks one of the movie role hyperlinks, the application should select the corresponding MovieRole object in the __movieroles__ display group.

- Select the string element that displays role names.
- Choose Format ! Abstract Element ! Hyperlink.
!

The Hyperlink command adds a hyperlink element as the selected element's parent. Now the string element is nested inside the hyperlink.

- Add the following method to MovieDetails' script:

```
    - selectObject {
        [movieroles selectObject:movieRole];
    }
```


The __movieRole__ variable is bound to the repetition element's __item__ attribute. In the __selectObject__ method above, __movieRole__ represents the role a user clicked on.

- Bind the __selectObject__ method to the hyperlink __action__ attribute.

## Add a form to the MovieDetails page

- Drag a form element from the Form Elements palette into the MovieDetails page.
- Replace the form's first label and text field with a browser element.
!- Type __Role Name__ as the label for the remaining text field.
- Bind __movieroles__ ! __roleName__ to the Role Name text field.

## Add a Talent display group

The browser you just created is going to display a list of actors, or talent. You need a new WODisplayGroup to manage objects associated with the Talent entity.

- Drag the Talent entity from EOModeler into the MovieDetails page.
- Select the __talents__ display group in the object browser, and then click the check mark button to open the DisplayGroupEditor panel.
- Configure the newly created __talents__ display group to sort its objects alphabetically (ascending) by __lastName__.
- Configure it to fetch on load.
- Set its Entries per batch to 0.

When the MovieDetails page is loaded, the __talents__ display group will fetch all Talent records from the database and display them in the browser.

## Create list and item bindings for the browser element

Like a repetition element, a browser has __list__ and __item__ attributes. As the browser moves through its __list__, it sets __item__ to the object at the current index.

- Bind __talents__ ! __displayedObjects__ to the browser element's __list__ attribute.

__talent__'s __displayedObjects__ method returns an array of all of the talent objects in the database.

- In the browser inspector, select the __item__ attribute.
- Type __talent__ in the text field.
- Click Connect.

WebObjects Builder creates a new variable named __talent__ in the MovieDetails component and binds it to the browser's __item__ attribute.

- Set the class of the __talent__ variable to be the Talent class.
!

Strictly speaking, this step is unnecessary, but it makes it easier to see what's going on. Now when you select __talent__ variable in the object browser, you can see that it has __lastName__ and __firstName__ attributes.

## Create the value binding for the browser element

The __value__ attribute tells the browser what string to display. For each item in its __list__, the browser evaluates its __value__. Typically you bind an attribute of the __item__ variable to the __value__ attribute. For example, you could bind __talent__ ! __lastName__ to the __value__ attribute. However, the browser in the MovieDetails page should display the full name for each of the actors. Since the Talent class doesn't provide an attribute for a full name, you need to write a method to create and return a string containing the full name for the current actor.

- Add the following method to the MovieDetails script.

```
    - fullName {
        id lastName = [talent valueForKey:@"lastName"];

        if (![lastName length]) {
            /* some actors don't have two names */
            return [talent valueForKey:@"firstName"];
        else
            return [NSString stringWithFormat:@"%@ %@",
                [talent valueForKey:@"firstName"],
                lastName];
    }
```

- Bind the __fullName__ method to the browser's __value__ attribute.

As the browser iterates through its list, it sets its __item__ (in this case, __talent__) to the current Talent object and then invokes the __fullName__ method. When __fullName__ is invoked, it returns a string containing the full name of the current actor.

## Create the selections binding for the browser element

Browser elements have a __selections__ attribute that should be set to an array of objects. A browser's selection can be zero, one, or many objects; but in this talent browser element, the selection should refer to a single object. Consequently, you need to add two methods to manage the browser's selection: one to return an array containing the selected actor and one to set the selected actor from an array object.

- Add the following method to the MovieDetails script:

```
    - talentSelection {
        id selectedTalent = [[movieroles selectedObject]
            valueForKey:@"talent"];
        if (selectedTalent)
            return [NSArray arrayWithObject:selectedTalent];
        else
            return nil;
    }
```


Because the browser expects an array for its __selections__ attribute, this method packages the __talent__ object for the selected MovieRole in an array. If the selected MovieRole object is __nil__, __talentSelection__ simply returns __nil__ to indicate that the browser shouldn't set a selection.

- Add the following method:

```
    - setTalentSelection:array {
        if ([array count])
            [[movieroles selectedObject]
                takeValue:[array objectAtIndex:0]
                forKey:@"talent"];
    }
```


Again because the browser uses an array for its __selections__ attribute, the __setTalentSelection:__ method must take an array as its argument. If __array__'s count is non-zero, then this method sets the selected MovieRole's __talent__ object to the first object in the array. (Note that a user can select more than one actor. A production-quality application would probably alert the user that a MovieRole can only be played by one actor, but this simple tutorial application won't take that extra step.)

- Bind the __talentSelection__ method to the browser's __selections__ attribute.

Given this binding, the browser invokes __talentSelection__ to determine what the selection is. It invokes __setTalentSelection:__ when a user changes the selection. As a result, the __talent__ instance variable of the selected MovieRole object is set to the newly selected actor.

- Configure the browser's appearance.
- Open the browser inspector.
- Set the number of rows shown to 10.
!

## Add Insert, Update, and Delete buttons

- Delete the Submit and Reset buttons.
- In the MovieDetails script, delete the __submit__ method associated with the Submit button.

__Note:__ If you save your application after deleting the buttons, WebObjects Builder automatically deletes the __submit__ method.

- Drag three active image elements from the Form Elements palette into the form element.

## Assign images to the active image elements

- Select the first active image element.
- Open the active image inspector.
- Click Browse.
!- In the Open panel navigate to the __Main.wo__ directory in the __Movies.woa__ application directory.
- Select the __DBWizardInsert.gif__ file.
- Click Open.
- Follow the same procedure to set the second image's source to __DBWizardUpdate.gif__.
- Set the last image's source to __DBWizardDelete.gif__.

## Create bindings for the active image elements

The WODisplayGroup class defines the methods __insert__ and __delete__ that you'll bind to the insert and delete active image elements, respectively. It doesn't, however, provide a save method. You'll have to provide that.

- In the MovieDetails script, delete the three __submit...__ methods that are bound to the active images.

When you use the Database Wizard and choose the Selected Record layout, the wizard sets up three active image elements just as you're doing on this page. As a part of that set up, it adds a method called __saveChanges__ to the component script. You can copy the __saveChanges__ method generated by the Database Wizard for the Main component and paste it into the MovieDetails component script.

- Copy the __saveChanges__ method from the Main script and paste it into the MovieDetails script.

```
    - saveChanges {
        id exception;

        exception = self.session.defaultEditingContext.tryToSaveChanges();
        if (exception != nil) {
            [exception raise];
        }
    }
```


__self.session__ (the same as __[self session]__) refers to a WOSession object that represents a connection to the application by a single user. WOSession objects provides access to an EOEditingContext object. The expression

```
    self.session.defaultEditingContext.tryToSaveChanges()
```


which is the same as the expression:

```
    [[[self session] defaultEditingContext] tryToSaveChanges]
```


sends a __tryToSaveChanges__ message to the WOSession's __defaultEditingContext__. This default EOEditingContext object manages graphs of objects fetched from the database, and all changes to the database are saved through it. For more information, see the EOEditingContext class specification in the _Enterprise Objects Framework Reference_.

EOEditingContext's __tryToSaveChanges__ method uses other Enterprise Objects Framework objects to analyze its graph of enterprise objects (Movie, MovieRole, and Talent objects referenced by the application) for changes and then to perform a set of corresponding operations in the database. If an error occurs during this process, __tryToSaveChanges__ returns an NSException object. (See the NSException class specification in the _Foundation Reference_ for more information on exceptions.) By default, the __saveChanges__ method simply raises the exception, having the effect of returning a diagnostic page. You could return an error page that explains the reason for the save failure instead, but the application in this tutorial uses the default behavior.

- Bind the __saveChanges__ method to the update image's __action__ attribute.
- Bind __movieroles__ ! __insert__ to the insert image's __action__ attribute.
- Bind __movieroles__ ! __delete__ to the delete image's __action__ attribute.

## Save and run your application

You've now completed the entire application. You can use the Browse Movies and Movie Search pages to insert, update, and delete movies, and you can use the MovieDetails page to inspect the list of roles in a movie and insert, update, and delete movie roles as well.

[!Table of Contents](Movies.book.md) [!Next Section](8_Conclusion.md)
