---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Movies/5_Actors.html
archived_at: '2026-07-15T07:49:08.591269Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Movies.book.md) [!Previous Section](4_Detail.md)

# Add more entities to the detail page

So far your Movies application fetches, inserts, updates, and deletes only Movie objects. Considered alone, a Movie object isn't as interesting as it is when it's related to actors and roles. In this section, you'll add MovieRole and Talent objects to the Movies application.!
Before you can use MovieRole and Talent objects in your application, you first need to go back to EOModeler and add relationships to the model's entities.
Relational databases model not just individual entities, but entities' relationships to one another. For example, a movie has zero, one, or more roles. This is modeled in the database by both the MOVIE table and MOVIE_ROLE table having a MOVIE_ID column. In the MOVIE_ROLE table, MOVIE_ID is a foreign key, while in MOVIE it's a primary key. A foreign key correlates with the primary key of another table to model a relationship a source table (MOVIE) has to a destination table (MOVIE_ROLE). In the following diagram, notice that the value in the MOVIE_ID column for both MOVIE_ROLE rows is 501. This matches the value in the MOVIE_ID column of the "Alien" MOVIE row. In other words, "Ripley" and "Ash" are both roles in the movie "Alien."!
Suppose you fetch a Movie object. Enterprise Objects Framework takes the value for the movie's MOVIE_ID attribute and looks up movie roles with the corresponding MOVIE_ID foreign key. The framework then assembles an object graph that connects the Movie object with its MovieRoles. As shown below, a Movie object has an array of its MovieRoles, and the MovieRoles each have a Movie.!
After you add relationships to your model, you can access MovieRole and Talent objects through the Movie objects fetched by the __movies__ display group. Using WebObjects Builder, you'll bind attributes of MovieRole and Talent objects to elements in the Movie Details page.

## Add relationships to your model

The Movies application uses two pairs of inverse relationships. The first pair defines the relationship between the Movie and MovieRole entities, while the second pair defines the relationship between the MovieRole and Talent entities. An Enterprise Objects Framework relationship is _directed_; that is, a relationship has a source and a destination. Generally you'll define a relationship for each direction.

- In EOModeler, double-click the open entity icon for the Movie entity.
!- Choose Property ! Add Relationship.
!

A new relationship named "Relationship" is added in the table view at the bottom of the model file window.

- Choose Tools !Inspector.

The Relationship Inspector opens.

- Select the To Many option.
- Select MoveRole as the destination entity.
- Select __movieId__ in the Source Attributes list.
- Select __movieId__ in the Destination Attributes list.
- Click Connect.
!

EOModeler automatically renames the relationship based on the name of the destination entity. For example, after connecting a to-many relationship from Movie to MovieRole, EOModeler names the relationship "movieRoles." To-one relationships are named with the singular form of the destination entity's name. For example, EOModeler names the inverse to-one relationship (from MovieRole to Movie) "movie."

- Repeat the steps above to create the following relationships:

A to-one relationship in the MovieRole entity where:

- The destination entity is Movie.
- The source attribute is __movieId__.
- The destination attribute is __movieId__.

A to-one relationship in the MovieRole entity where:

- The destination entity is Talent.
- The source attribute is __talentId__.
- The destination attribute is __talentId__.

A to-many relationship in the Talent entity where:

- The destination entity is MovieRole.
- The source attribute is __talentId__.
- The destination attribute is __talentId__.

## Save the model file

- Choose Model ! Save.

A Consistency Check panel runs alerting you that several of the model's entities don't have primary keys.

!- Click OK to save your model anyway.

You'll add primary key values in the next step.

## Assign primary key attributes

The Database Wizard assigned a primary key attribute to the Movie entity when it created the model. You need to assign primary keys to the rest of the entities using EOModeler.
The Movies application only uses the Movie, MovieRole, and Talent entities, but you should assign primary keys to all the entities in case you extend the application later.

- Click the model icon in the icon path to display the model's entities.
- Select the Director entity icon.
- Open the inspector.
- Click in the primary key column next to the __movieId__ and __talentId__ attributes to make them primary keys.
!- Repeat the steps above to specify the following primary keys for the remaining entities:

- MovieRole's primary keys are __movieId__ and __roleName__.
- PlotSummary's primary key is __movieId__.
- Studio's primary key is __studioId__.
- Talent's primary key is __talentId__.
- TalentPhoto's primary key is __talentId__.

Note that some of the entities have _compound primary keys_; that is, a primary key that is composed of more than one attribute.

Now when you save, EOModeler should not display the Consistency Check panel.

## Add interface elements for the new information

Now you'll extend the user interface of the MovieDetails component to display the actors in the selected movie. Because different movies have different numbers of roles, you need the dynamism of a repetition element.

- In the MovieDetails component window, add the bolded text __Starring:__ beneath the Revenue line.
- Place the cursor below the Starring label.
- Drag a repetition element into the component window from the Abstract Elements palette.
- Delete the "Repetition" text inside the element and the carriage return before it.
- Add three string elements inside the repetition.

The strings should all be on the same line, so don't type carriage returns between them.

- Type the word "as" between the last two string elements.
!

## Create bindings

- Select the first field of the repetition element.
- Navigate to __movies__ ! __movieRoles__ in the object browser.
- Double-click __movieRoles__.

Remember that a Movie object has a __movieRoles__ instance variable that's an array of MovieRole objects. The steps above bind the __movieRoles__ array of the selected Movie object to the repetition's __list__ attribute. WebObjects Builder automatically adds a new variable to the MovieDetails component named __movieRole__ and binds it to the repetition's __item__ attribute.

!

The __movieRole__ variable, a MovieRole object, has an instance variable-__talent__-that's a Talent object. (The __talent__ instance variable is the result of the to-one relationship from the MovieRole entity to the Talent entity.) Through the __movieRole__ instance variable, you can access the name of the actor playing a particular role.

- Select the first string element in the repetition.
- Navigate to __movieRole__ ! __talent__ ! __firstName__ in the object browser.
- Double-click __firstName__.
- Similarly, bind __movieRole__ ! __talent__ ! __lastName__ to the second string element.
- Bind __movieRole__ ! __roleName__ to the last string element.

## Save and run your application

A WebObjects application only reads its model file once-when it loads the corresponding WODisplayGroup. As a result, you'll need to restart your the Movies application so it can see the relationships you added.
You may need the assistance of your system administrator to end the running Movies process, but generally you use the Windows NT Task Manager to end processes.

- Right-click on the toolbar.
- Choose Task Manager.

The Task Manager window opens.

- Select the WODefaultApp process that corresponds to your Movies application.
- Click End Process.

__For Unix Users Only:__ On Unix systems you can use the __kill__ command to end the WODefaultApp process.

[!Table of Contents](Movies.book.md) [!Next Section](6_MasDet.md)
