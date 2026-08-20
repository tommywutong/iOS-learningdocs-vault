---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeltaDoc/EOF.html
archived_at: '2026-07-15T08:04:35.534606Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
What's New in WebObjects

---

[!](What%27s%20New%20in%20WebObjects%204.5.md)

# What's New in Enterprise Objects Framework

This chapter describes changes made to the Enterprise Objects
Framework (EOF) between release 3.0 and 4.5. It describes changes
made to existing features and describes new features you may want
to start using in your applications.

|  |
| --- |
| __Note:__ To synchronize the version numbers of WebObjects and EOF, the version number of EOF was increased from 3.0 in the last release to 4.5 in this release. |

## Schema Synchronization

In EOF 4.5, EOModeler supports synchronization of a database
schema with the current state of a model.

|  |
| --- |
| __Note:__ The Informix and ODBC adaptors do not provide schema synchronization support. |

To initiate the process of synchronizing a model and schema,
select "Synchronize Schema" from the Model menu. Note that before
synchronizing, you need to save your model. Because the operation
cannot be undone, the "Synchronize Schema" menu item is only enabled
when the model has no unsaved changes.

After starting the synchroniztion process, EOModeler reverse
engineers the database's schema and assembles the adaptor operations
necessary to synchronize it with the model. These operations are
presented to the user for confirmation before execution.

For example, if you add simple attributes (attributes representing
database columns) to an entity, schema synchronization adds the
columns to the underlying table. Similarly new columns or tables
created in the database can be selected for incorporation into the
model. External type changes for attributes and the renaming of
columns and tables are also supported.

### Related API Changes

EOModeler makes use of the schema synchronization API to synchronize
your database with your model. You don't need to use the API yourself
unless you're implementing the API for a custom adaptor.

If you do need to use or implement this API (very unlikely),
see the related documentation in the following class and interface/protocol
specifications:

- EOAdaptor
- EOAdaptorChannel
- EOAdaptorChannel Delegate
- EOSQLExpression

## Event Logging

WebObjects 4.5 introduces event logging. The goal for this
feature is to allow the measurement of how long certain operations
in EOF and WebObjects take. Measurements allow you to profile an
application and optimize its execution time. For this, the EOF and WebObjects
frameworks instrument key portions of their code to measure the
elapsed time of functions and methods.

|  |
| --- |
| __Note:__ The event logging feature, related classes, and related API are not available in the com.apple.client packages. Therefore, you can't time the client side of a Java Client application. |

To support this feature, EOF adds two new classes: EOEvent
and EOEventCenter. An EOEvent keeps information (such as duration)
about a logged event, and EOEventCenter manages the events. EOEvent
is an abstract class whose subclasses are responsible for defining
the events they track. For example, there are (private) subclasses
for Sybase adaptor events, editing context events, WOApplication
events, and so on.

To enable event logging in an application, simply open the
WOEventSetup page as described in ["WOEventSetup page"](#apple-inbeoq2bifbuq) and enable
logging for the event classes you want to see.

In addition to the framework support, the WOExtensions framework
provides components for using the feature. WOEventSetup is a page
you use to configure event logging, and WOEventDisplay is a page
the displays event information. Both pages can be accessed in any
WebObjects 4.5 application with a direct action, as described in
the following sections.

### WOEventSetup page

The page used to set up the logging properties is accessed
through a direct action named "WOEventSetup". So for example,
you can access the WOEventSetup page for an application named "MyApp"
with a URL such as the following:

> ```
> http://myhost:aPort/cgi-bin/WebObjects/MyApp.woa/wa/WOEventSetup
> ```

On the WOEventSetup page, you can see all families of events
that are registered for the application. Since the event classes
are registered dynamically as the program executes, it is a good
idea to "warm up" an application before accessing WOEventSetup.

The page lists the registered event classes, their subcategories,
and a description of the kinds of events that can be logged. For
instance, the EOEditingContext event class logs events for the `saveChanges` and `objectsWithFetchSpecification:` methods.
Logging for each class can be enabled and disabled with the corresponding
check box; it isn't possible to disable individual subcategories
of an event class.

### WOEventDisplay page

The page that displays collected events, WOEventDisplay, is
also accessed through a direct action. For example, you can access
the WOEventSetup page for an application named "MyApp" with
a URL such as the following:

> ```
> http://myhost:aPort/cgi-bin/WebObjects/MyApp.woa/wa/WOEventDisplay
> ```

On this page, you can view events in four different ways:

- __Raw root events__. This view,
  the most verbose, displays all events at the root level (events
  without an encompassing event). WOEventDisplay shows each event individually,
  which means that its possible for an event to appear multiple times
  if the thread of execution crosses its point more than once.
- __Aggregated root events__. This view is similar
  to the raw root event view, except that multiple identical events
  are __aggregated__ or grouped in a single entry,
  and their combined time is displayed. In addition, the "Calls"
  column shows how many times an event was executed (in other words,
  how many events contributed to the displayed aggregate event).
- __Events grouped by page and component__. In
  this view, the first level of display shows only page names. By
  expanding a page, you get a list of components in that page. Expanding
  a component shows all the events within that component. This means
  that even events which were collected "deep" within a component
  are shown immediately below the component name. All identical events
  are aggregated as in the aggregated root event view for easier reading.
  It's possible to traverse the component event hierarchy by expanding
  the hyperlinks within a component.

   Note that since a page is
  also a component, a page with no dynamic subcomponents seems as
  if it's nested one level too deep. This is the correct behavior.
- __Events grouped by page only__. This display
  is similar to the grouped by page and component view, except the
  events do not have a by-component subgrouping.

In any of these displays, if an event or event group has subevents,
it can be expanded by clicking the hyperlink or triangle image.

Each view orders events by duration (in milliseconds) from
the longest to the shortest. Aggregation reduces rounding errors,
which are a maximum of 1ms per event. In other words, an aggregate
event consisting of ten events has at most 1ms deviation from the actual
run time; however, manually adding ten individual events as displayed
in the table might have up to a 10ms deviation. Therefore, any displayed
sum is always more accurate than adding up the durations of individual
events. Also note that the sub-events of an event branch doesn't
necessarily add up to the duration of the branch event-the branch event's
duration might be larger. This because the parent event generally
consists of more than just calling the methods causing the sub-events.

### Event System User Defaults

The event system provides three defaults for configuring its
behavior:

**EOEventLoggingEnabled**
: A boolean value that determines whether event logging
is enabled. The default is NO, logging isn't enabled.
 You
can enable logging with EOEventLoggingEnabled, but the WOEventSetup page
gives you more flexibility. The EOEventLoggingEnabled default enables logging
for every class, whereas with WOEventSetup you can enable logging on
a class by class basis.

**EOEventLoggingLimit**
: An integer value that sets the maximum number of events
the event system logs. The default logging limit is 200,000 per
thread.
 When the logging limit is reached, the event system
attempts to purge old events before logging new ones. If the system
is unable to purge old events, event logging is aborted.

**EOEventLoggingOverflowDisplay**
: A boolean value that determines whether the event system
logs a message when the event logging limit is reached. If enabled,
the system logs messages when the event center truncates the log
and also when event logging is aborted due to overflow.

### Event Logging Questions and Answers

**Question**
: What happens to an EOEvent if an exception is raised
before the event is completed?

**Answer**
: As soon as you close another event, the system detects
that a previous event was not closed properly and closes it for
you. All events logged between an unclosed event (due to an exception
or improper coding) and the closing of another event are logged
at the wrong place in the event hierarchy, but they are logged.
 An
improperly closed event can have another negative side effect: the improperly
closed event can't be pruned with the automatic memory manager. This
is virtually the only thing that can completely abort event logging.
 If
you have reason to believe that you might raise while an event is
in progress, you should cancel the event in an exception handler.

**Question**
: What's the overhead of enabling event logging?

**Answer**
: The logging mechanism is extremely fast and memory efficient.
A standard 300 MHz G3 system can log more than 300,000 events per
second. Thus, the creation and logging of events is negligible compared
to the time required to generate dynamic web pages. The only expensive
operations are tree pruning when memory overflows (which takes about
as long as logging ten events), and handling exceptions (which is
linear to the depth of the tree-rarely more than 5 levels deep
under normal circumstances). Therefore, the overhead is not really
measurable.

**Question**
: Can I enable event logging for a single-user application
in production?

**Answer**
: You shouldn't, because it would use a lot of memory:
about 4 MB per thread for the default event log limit (200,000 events).
Also, throughout the lifetime of an application, the system must
continuously prune the event tree to keep the log size under the
limit. As stated above, pruning the tree is a relatively expensive
operation.

**Question**
: Is performance impacted by the size of the event log?
Does performance degrade if logging isn't reset periodically?

**Answer**
: No. As stated above, the size of the event log is limited.
Once you warm up the application and the logging framework, event
logging overhead is constant-not per event, but over an average
of a series of events.

### Custom Event Logging

To define and log custom events, you create an event class, define
the event's categories and subcategories, register the event class
with the WOEvent center, and instrument the portions of code you
want to log. This section describes these steps.

To create a custom event:

1. Create a subclass of EOEvent or an appropriate
   subclass.

    For example, to log events for a custom adaptor
   you've written, say MyAdaptor, create an EOEvent subclass named
   MyAdaptorEvent.

    Your subclass doesn't usually have
   to override any of the inherited methods, but you can customize
   the default behavior.

2. Create a description file for your event and add it to your
   project's Resources folder.

    An event's description file
   defines the event categories and subcategories used in the WOEventDisplay
   page. The file's contents is a dictionary in plist format. For
   the MyAdaptorEvent class, the file's name is MyAdaptorEvent.description,
   and it might look like the following:
   > ```
   > {
   >     EOEventGroupName = "MyAdaptor Event";
   >     connect = "Connect";
   >     openChannel = "Open Channel";
   >     evaluateExpression = "Evaluate Expression";
   >     fetchRow = "Fetch Row";
   >     commitTransaction = "Commit Transaction";
   > }
   > ```

    The EOEventGroupName
   entry is mandatory. It describes the family of events logged by
   the event class. Any other keys are self defined by the event class.
   In this example, the other keys (`connect`, `openChannel`,
   and so on) are the names of the events MyAdaptorEvent logs.

3. Register the event class with the EOEventCenter.

    Typically
   you register the event class in the `initialize` method
   of the class whose code you're instrumenting-MyAdaptor in this
   example.
   > ```
   > static Class MyAdaptorEventLoggingClass = Nil;
   > static NSString *connectEvent = @"connect";
   > static NSString *openChannelEvent = @"openChannel";
   > static NSString *evaluateExpressionEvent = @"evaluateExpression";
   > static NSString *fetchRowEvent = @"fetchRow";
   > static NSString *commitTransactionEvent = @"commitTransaction";
   >
   > + (void)initialize {
   >     [EOEventCenter registerEventClass:[MyAdaptorEvent class]
   >             classPointer:&MyAdaptorEventLoggingClass];
   > }
   > ```

    As in this example,
   you might want to define string constants for the keys in your event's
   description dictionary.

4. Instrument the methods.

    In any method you want to instrument,
   add the following code, substituting the appropriate event key.
   This code instruments the "connect" event of MyAdaptorEvent.
   > ```
   > MyAdaptorEvent *event=nil;
   >
   > // Setup and start logging
   > if(MyAdaptorEventLoggingClass) {
   >     event = EONewEventOfClass(MyAdaptorEventLoggingClass, connectEvent);
   >     EOMarkStartOfEvent(event, nil);
   > }
   >
   > // Code to be timed goes here.
   >
   > // Finish logging.
   > if(event) {
   >     EOMarkEndOfEvent(event);
   > ```

    The
   second argument to EONewEventOfClass is
   an event key corresponding with an entry in the .description file.
   The corresponding value is used in the Title column of the WOEventDisplay
   page. If the argument isn't a key in the description dictionary, EONewEventOfClass uses
   the argument instead.

   For more information on the methods
   used in this example, see the class descriptions for EOEvent and
   EOEventCenter. To see a complete example of timing events, refer
   to the ODBC Adaptor source code that's distributed with WebObjects.

### Related API Changes

Three new classes and one interface have been added to support
event logging. They are:

- EOEventCenter (EOControl/EOEventCenter.h)
- EOEvent (EOControl/EOEvent.h)
- EOAggregateEvent (EOControl/EOAggregateEvent.h)
- EOEventCenter.EventRecordingHandler (Java) or EOEventRecordingHandler (Objective-C; EOControl/EOEventCenter.h)

For more information, see the corresponding class or interface
specifications.

|  |
| --- |
| __Note:__ These classes and interfaces aren't available in the com.apple.client.eocontrol package. |

## Object Sharing

EOF 4.5 introduces a new technique for sharing
read-only enterprise objects. The new subclass of EOEditingContext,
EOSharedEditingContext, defines a mechanism that allows editing
contexts to share enterprise objects for reading. This mechanism
can reduce both the number of fetches an application makes and the
amount of redundant data it requires.

As an example, consider the FeeType entity in the samle Rentals
model that ships with EOF 4.5. A FeeType enterprise objects describes
a type of fee that a video store can charge its customers-"Rental"
and "Late", are the two FeeTypes in the sample database. It
is very uncommon to add or remove FeeTypes, and it's perhaps even
more uncommon to modify an existing FeeType (to rename it, for example).
For the most part, FeeTypes are read-only.

With 4.5, you can fetch read-only objects such as FeeTypes
into a shared editing context once, when an application starts,
and all the application's sessions can share those objects. For
example, objects in any session can create relationships to the
shared FeeType objects even though the FeeTypes are in a different
editing context from the source objects. Using previous releases,
you would have to make local copies of the read-only FeeTypes in
each of the editing contexts that use them.

|  |
| --- |
| __Note:__ Support for shared editing contexts is not implemented in the com.apple.client packages. Therefore, shared editing contexts are not available in the client side of a Java Client application. |

### How It Works

The idea behind shared editing contexts is to load read-only
(or read-mostly) objects into a central context that all sessions
have transparent access to. It works like this.

1. A model file identifies any objects to be shared.

    Models
   identify shared objects by defining __shared object fetch
   specifications__, which define criteria for fetching objects
   that are to be shared. For information on creating shared object
   fetch specifications, see ["Setting Up Object Sharing"](#apple-inbeorkeiveeq).

    The first time your
   application accesses a model's entities, it checks the model for shared
   object fetch specifications. If any are found, they are evaluated
   and the corresponding fetched objects are loaded into the default
   shared editing context. Any existing editing contexts that don't
   have any registered objects begin using the default shared editing
   context. Similarly, any editing contexts subsequently created use
   the default shared editing context.

    Note that if you
   don't specify any shared fetch specifications, a shared editing
   context is never created and no object sharing occurs. Conversely,
   if you do specify shared object fetch specifications, a shared editing
   context is automatically created and object sharing is enabled for
   all standard editing contexts.
2. The application's shared editing context is created and
   populated the first time a model containing shared object fetch
   specifications is accessed.

    Generally an application's shared
   editing context is initialized when the first editing context attempts
   to access the database. At this time, all the application's models
   are loaded, and any shared object fetch specifications are detected.
   If any of the application's models have shared object fetch specifications,
   a shared editing context is created and populated and is set as
   the shared editing context for all empty editing contexts.

    You
   can disable object sharing on individual editing contexts as described
   in ["Inserting, Updating, and Deleting Shared Objects"](#apple-inbeorkiizbek) or you can disable object
   sharing altogether as described in ["Disabling Sharing During Development"](#apple-inbeoqsdiveeo).
3. Standard editing contexts use objects in the shared editing
   context as if they were local.

    When a standard editing context
   fetches, any relationships to shared objects are automatically resolved
   to the shared editing context's objects. Similarly, an object
   in any standard editing context can create a relationship to a shared
   editing context's object.

    This all works transparently.
   EOEditingContext's implementations of `objectForGlobalID` and `faultForGlobalID` look
   for an object in the shared editing context when a standard editing
   context doesn't find the object locally. If the methods finds
   the object in the shared editing context, they return the shared
   object as they would if the object were local.

To allow object sharing to work, EOF makes the following assumptions:

- Shared objects are read-only (or read-mostly).
- Objects must be unique in their editing contexts and their
  editing context's shared editing context.

The following sections describe why these assumptions are
necessary and how they are enforced.

#### Shared Objects Are Read-Only

If you could update a shared object, all of an application's
users would see the changes immediately since all sessions share
the exact same object. This behavior is undesirable. You only want
users to see _committed_ changes to objects.
For example, suppose you make a change to a shared object in a web
application, but you haven't yet saved it to the database. The
changes are written to the object as soon as the request-response
loop begins, and every other web user sees the change you made,
even if you undo them later or make further changes before saving.

For this reason EOF enforces the read-only quality of shared
objects. Shared objects can't be inserted, updated, or deleted
in a shared editing context the same way that normal enterprise
objects can be inserted, updated, or deleted when they're in a
standard editing context. EOSharedEditingContext overrides EOEditingContext
methods that mutate data (`takeValueForKey`, `saveChanges`, `deleteObject`,
and `insertObject` for example) to raise exceptions.
Correspondingly, methods that report on changes in a shared editing
context return either `null`/`nil` or
an empty array.

It would also be undesirable if you could delete a shared
object. In Objective-C, it would be bad if a shared object were
released while objects in standard editing contexts had relationships
to it. Objects in a shared editing context are always retained.
You are guaranteed that no object in a shared editing context will
be destroyed while the application is running (a shared object can
become invalid, but it won't go away).

#### Shared Objects Are Uniqued

EOF uses object uniquing to ensure that a single editing context
never has more than one object with the same global ID. Because
every standard editing context has access to the objects in a shared
editing context as if the objects were local, none of a shared editing context's
objects can have the same global ID as any object in any standard
editing context.

EOF does most of the work for you. A shared editing context
sends out notifications when it initializes new objects. Standard
editing contexts listen for these notifications and raise exceptions
if they have local objects with the same global ID as the new shared
object. However, you have to take some precautions not to fetch
into a shared editing context objects that have already been fetched
into a standard editing context:

- Don't explicitly fetch into a standard editing
  context an object that is already shared _unless_ you
  disable sharing, as described in ["Inserting, Updating, and Deleting Shared Objects"](#apple-inbeorkiizbek).
- If a shared object has relationships to entities that aren't
  shared, remove the relationships from the model. Otherwise, when
  the faults fire, the destination objects are fetched into the shared
  editing context.

### Setting Up Object Sharing

EOModeler has a new entity inspector for specifying the objects
you want to fetch into a shared editing context when an application
starts. To use it, select the entity whose objects you want to share,
and open the Shared Objects Inspector.

To share all the entity's objects, select "Share all objects."
If the entity has an unqualified fetch specification, that fetch
specification is selected. Otherwise, EOModeler creates an unqualified
fetch specification and selects it.

To share only some objects, define fetch specifications that
select the objects you want to share. In the Shared Objects Inspector,
select "Share objects fetched with" and select your fetch specifications.

You can also prefetch relationships into the shared editing
context. For example, suppose that Product has a relationship to
ProductPlatforms and that both entities should be shared. You can
create a Product fetch specification that has a hint to prefetch
the Product's ProductPlatforms relationship. Using this fetch
specification to fetch Products into the shared editing context
also causes ProductPlatforms to be loaded into the shared editing context.

### Accessing Shared Objects

Shared editing contexts maintain dictionaries of all the objects
they have fetched, both by entity name and by the fetch specification
name they were retrieved with. This makes it easy to use shared
objects for populating user interface controls. The two methods
for accessing these dictionaries are:

> ```
> objectsByEntityName
> objectsByEntityNameAndFetchSpecificationName
> ```

These two methods make it easy to use key-value coding and
key paths to bind data to WebObjects elements directly in a WebObjects .wod file.

For example: Say you have a model with the entity "Products"
and an attribute called "isDiscontinued", which indicates whether
an item is unavailable. You could set up a fetch specification in
EOModeler named "regularProducts" that fetches only objects
that are available (the qualifier would specify that "isDiscontinued
= 0"). To use the returned set of "regular products" in
a WebObjects page, create a user interface control (such as a WOPopup
or WOBrowser), and set its `list` attribute
like this:

> ```
> list =
> session.defaultSharedEditingContext.objectsByEntityNameAndFetchSpecificationName.Products.regularProducts
> ```

The user interface control's list is automatically filled
with data from shared objects.

### Inserting, Updating, and Deleting Shared Objects

Generally shared objects are _read-mostly_.
For example, an application could provide an administration mode
that allows administrative users to insert, update, and delete otherwise
read-only shared objects. You can still use a shared editing context
in such an application, but you have to write special code. Since
insertions, updates, and deletions of shared objects are typically
very infrequent, the performance benefit of sharing objects can still
be significant.

To insert new objects, create and insert a new object in a
standard editing context. Once you do this, you need to fetch the
new object into the shared editing context as described in ["Refreshing the Shared Editing Context"](#apple-inbeorcjirbek).

Updating and deleting them is a little trickier. To modify
shared objects, you need to disable object sharing for a particular
editing context, as follows:

> ```
> mySession.defaultEditingContext().setSharedEditingContext(null); // Java
> [[mySession defaultEditingContext] setSharedEditingContext:nil]; // ObjC
> ```

A session that does this doesn't have access to shared objects
and can explicitly fetch objects that would otherwise be shared.
After fetching the objects, they are local, and you can update or
delete them. When you save the changes, the shared editing context
receives ObjectsChangedInStoreNotifications. In response to the
notifications, the shared editing context refaults updated objects
and removes deleted objects from its `objectsByEntityName` and `objectsByEntityNameAndFetchSpecificationName` dictionaries.

|  |
| --- |
| __Note:__ Deleted objects remain in the shared editing context so that Objective-C objects having relationships to them won't be left with dangling pointers. |

### Refreshing the Shared Editing Context

You might want to refresh the shared editing context after
an administrative user inserts a new shared object or to periodically
synchronize with a database. To refresh a shared editing context,
use the method `bindObjectsWithFetchSpecification` (Java)
or `bindObjectsWithFetchSpecification:toName:` (Objective-C).
For example:

> ```
> EOModelGroup modelGroup = EOModelGroup.defaultGroup();
> EOSharedEditingContext sharedEC =
>     EOSharedEditingContext.defaultSharedEditingContext();
>
> EOFetchSpecification fs =
>     modelGroup.fetchSpecificationNamed("regularProducts", "Product");
>
> if (fs == null) {
>     System.out.println("Couldn't get regularProducts fetch specification.");
> } else {
>     sharedEC.bindObjectsWithFetchSpecification(fs, "regularProducts");
> }
> ```

This has the effect of refetching all the shared objects and
binding them to the `objectsByEntityName` and `objectsByEntityNameAndFetchSpecificationName` dictionaries.

### Disabling Sharing During Development

Initializing a shared editing context does increase the amount
of time it takes for an application to start up. During development
when you starting your application frequently, the additional start
up time can become a nuisance. To make debugging passes quicker,
you can essentially disable object sharing using the static method `setSharedObjectLoadingEnabled` (or
the equivalent class method in Objective-C).

This method specifies whether EOF looks for shared fetch specifications
when it loads models. While a shared editing context can still be
created and referenced, it won't contain any objects unless you
programmatically fetch them into it. The advantage of disabling shared
object loading is that the application starts up more quickly.

### Performance

Using shared editing contexts can have the following positive
performance impact on your application:

- Standard editing contexts don't have their
  own copies of shared objects, so the memory footprint is smaller.
- Fetching read-only data into an application is a lot simpler,
  so fewer database trips may be needed.

However, there are potentially negative performance effects
as well. They are:

- Every editing context has to hash twice: once
  to look up objects in their own tables, and again to look up objects
  in the shared tables. Hashing is _very_ fast,
  but with nested contexts it can add up.
- On Windows NT, locking a thread is significantly slower than
  it is on other platforms with similar hardware. Because shared editing
  contexts generate a lot of locking activity, sharing objects can
  actually degrade the performance of an application on NT. If you
  plan to deploy on NT, test your server's performance carefully.
- Fetching or firing faults in a shared editing context causes
  all other threads to block when they try to get shared data. To
  avoid this problem, try to fetch everything when the application
  starts up.

### Multithreaded Access and Locking

WebObjects applications take care of most multithreading issues
for you. This is also the case with applications that use shared
editing contexts. Here are the basics of how EOF locks shared editing
contexts:

- Shared editing contexts use a new lock, EOMultiReaderLock,
  which allows multiple contexts to read data from the shared editing
  context concurrently. When the shared editing context needs to update
  objects (because of fetching or firing faults), the context waits
  for all reader locks to be surrendered and then issues a writer
  lock. There can only be one writer at a time.
- Whenever an EOEditingContext `lock` method
  is called, it also obtains a reader lock for its shared editing
  context.
- When an EOEditingContext is about to call its parent object
  store, it surrenders its shared reader lock until the call is complete
  (this prevents deadlocks with the object store lock).

From a WebObjects perspective, everything works automatically
as long as you interact with a shared editing context from within
the context of a session. This is because when a web session awakes,
it locks its editing context, which reader-locks the shared editing context.
If you need to interact with the shared editing context outside
the context of a session, you should access it through a locked
EOEditingContext.

If you invoke methods on a shared editing context directly,
you must obey a strict lock ordering protocol to avoid deadlocks
and unsafe multithreaded access. If you directly invoke any method
besides `objectsWithFetchSpecification`, `objectForGlobalID`,
or `faultForGlobalID` on a shared editing
context, you need to take the a reader or writer lock yourself before
calling the method.

### Related API Changes

A new subclass of EOEditingContext, EOSharedEditingContext,
has been added to support object sharing. For more information on
this class, see the corresponding class specification.

|  |
| --- |
| __Note:__ With this release of EOF, there is a subclass of EOEditingContext for the first time. You might have to adjust your code if you ever assume than an editing context is always an instance of EOEditingContext. |

|  |
| --- |
| __Note:__ Support for shared editing contexts is not implemented in the com.apple.client packages. |

Additionally, new API has been added to existing classes as
summarized in the following tables.

__EODatabaseContext (EOAccess/EODatabaseContext.h)__

| __New or Changed API__ | __Description__ |
| `setSharedObjectLoadingEnabled` (Java)  `setSharedObjectLoadingEnabled:` (Objective-C) | A static/class method that sets according to the specified flag whether or not to automatically load enterprise objects into the default shared editing context when a database context loads a model. The default is `true`/`YES` (the database automatically loads shared objects). |
| `isSharedObjectLoadingEnabled` | A static/class method that returns `true`/`YES` if database contexts automatically load enterprise objects into the default shared editing context when database contexts load models, `false`/`NO` otherwise. |

__EOEntity (EOAccess/EOEntity.h)__

| __New or Changed API__ | __Description__ |
| `setSharedObjectFetchSpecificationsByName` (Java)  `setSharedObjectFetchSpecificationsByName:` (Objective-C) | Sets the fetch specifications used to load objects into a shared editing context to the fetch specifications identified by name in the specified array. |
| `sharedObjectFetchSpecificationNames` | Returns an array of strings, which are the names of the fetch specifications used to load objects into a shared editing context. |
| `addSharedObjectFetchSpecificationByName` (Java)  `addSharedObjectFetchSpecificationByName:` (Objective-C) | Adds the fetch specification identified by the specified name to the set of fetch specifications used to load objects into a shared editing context. |
| `removeSharedObjectFetchSpecificationByName` (Java)  `removeSharedObjectFetchSpecificationByName:` (Objective-C) | Removes the fetch specification identified by the specified name from the set of fetch specifications used to load objects into a shared editing context. |

__EOModel (EOAccess/EOModel.h)__

| __New or Changed API__ | __Description__ |
| `entitiesWithSharedObjects` | Returns an array of entities that have objects to load into a shared editing context. |

__EOModelGroup (EOAccess/EOModelGroup.h)__

| __New or Changed API__ | __Description__ |
| `entitiesWithSharedObjects` | Returns an array of entities that have objects to load into a shared editing context. |

__EOEditingContext (EOControl/EOEditingContext.h)__

| __New or Changed API__ | __Description__ |
| `setSharedEditingContext` (Java)  `setSharedEditingContext:` (Objective-C) | Sets the receiver's shared editing context. If the receiver is listening for (`EO)DefaultSharedEditingContextWasInitializedNotification`, it removes itself as an observer.   By default, the shared editing context is `null`/`nil` but is set when an `(EO)DefaultSharedEditingContextWasInitializedNotification` is posted.  Changing the shared editing context to `null`/`nil` allows the receiver to obtain private, editable copies of objects that would otherwise be shared. If both the receiver and the specified shared editing context have registered objects, the objects of both contexts are compared to verify that the objects are unique. If the objects are not unique, an exception is raised by the editing context. |
| `sharedEditingContext` | Returns the shared editing context used by the receiver. |

## Subclassing EOGenericRecord

EOF 4.5 adds a new option for creating custom enterprise objects:
rather than creating a subclass of EOCustomObject (Java) or NSObject
(Objective-C), you can now subclass EOGenericRecord.

This feature is most significant in applications that use
the Java bridge. By default, a subclass of EOGenericRecord stores
its properties in a dictionary on the Objective-C side of the
bridge instead of in individual instance variables on the Java side.
This allows EOF to access enterprise object properties with many
fewer trips across the bridge, which reduces memory usage and improves
performance.

More specifically, subclassing EOGenericRecord provides the
following advantages over subclassing EOCustomObject (Java):

- Java enterprise objects don't incur a performance
  penalty relative to Objective-C. Previously, each call to an EOKeyValueCoding
  method (such as `valueForKey`) resulted in
  a bridged method invocation and possibly the creation of a new object.
  Because EOGenericRecord provides the storage for an enterprise object's
  values, the values don't need to cross the bridge during a fetch.
  This results in a dramatic performance improvement in EOKeyValueCoding-bound
  operations such as fetching, snapshotting, and validation.
- Java enterprise objects don't use more memory than Objective-C
  enterprise objects. Since an enterprise object's values were previously
  stored in its instance variables, each value object had to be morphed
  between Java and ObjC when interacting with the EOF frameworks.
  This meant that the values couldn't be shared between an enterprise object
  and its snapshots in the EOEditingContext and EODatabase. Consequently, many
  more objects were resident in memory than would be the case in the
  non-bridged case.
- Enterprise object classes are more flexible and easier to
  maintain. As you edit your model by adding or removing keys, you
  only have to update your enterprise object class if you want to
  add or remove custom accessors or validation methods. You don't have
  to maintain instance variables since property values are stored
  in a dictionary.
   Also, you can use a specific subclass of
  EOGenericRecord for multiple entities as you can when you use EOGenericRecord.
  In previous releases, a single enterprise object class (other than
  EOGenericRecord) could correspond to only one entity. Subclasses
  of EOGenericRecord can now correspond to multiple entities the same
  way EOGenericRecord can. This might be useful for providing common
  behavior such as validation logic. Note that a "generic" subclass
  of EOGenericRecord (that is, a subclass which is shared among entities) _must_ be
  instantiated using EOClassDescription's `createInstanceWithEditingContext` method
  in the same way that EOGenericRecord must. If it isn't, the resulting
  instance won't be properly initialized.
- Subclasses of EOGenericRecord automatically use deferred faulting,
  which increases performance and decreases memory usage even further.
  For more information on deferred faulting, see ["Deferred Faulting"](#apple-inbeoqsgijfee).

Given all the advantages of subclassing EOGenericRecord, you
might wonder if there's ever a reason to subclass EOCustomObject.
Subclassing EOGenericRecord usually yields better performance. Even
if it doesn't yield _better_ performance, you
can design it to be at least as fast and to have the same level
of functionality as a subclass of EOCustomObject by storing properties
in instance variables. Therefore, you really don't ever need to subclass
EOCustomObject.

### Property Storage: Dictionary or Instance Variables

A subclass of EOGenericRecord can take three approaches to
storing property values:

1. Store them in the EOGenericRecord dictionary.
2. Store them in instance variables.
3. Store them in a combination of the above.

Generally the first approach is the best because it reduces
the number of trips across the Java bridge, improving performance
and reducing memory usage. Enterprise objects are accessed from
Objective-C much more frequently than from Java. A typical enterprise object
is populated from Objective-C when it's fetched from the database,
snapshotted from Objective-C each time the object is changed,
and accessed from Objective-C to provide values for bindings in
WebObjects components.

On the other hand, access from Java is typically limited to
custom validation (implemented in the enterprise object class) and
to accesses by other enterprise objects to obtain property values
explicitly (for example, to check the department budget before validating
a new salary).

The second approach might be appropriate if your application
accesses and manipulates enterprise objects from Java quite frequently,
however this case is probably rare.

|  |
| --- |
| __Note:__ When you create an instance variable for an EOGenericRecord subclass, ensure that the accessor methods read and write the instance variable instead of invoking `valueForKey` and `takeValueForKey`, which is what the implementations do if the code is generated by EOModeler. |

The third approach is to create instance variables for some
of your enterprise object's properties and leave the rest in the
EOGenericRecord dictionary. This approach is the most difficult
to maintain, because the implementation of accessor methods depends
on the way the property is stored.

### Creating a Subclass

EOModeler has been updated with templates that take advantage
of this feature, so new enterprise object classes are automatically
subclasses of EOGenericRecord. To re-parent existing business objects,
perform the following steps in your source files:

1. Set the enterprise object class's superclass
   to EOGenericRecord.
2. Delete all EOKeyValueCoding-related instance variables (that
   is, instance variables that store values for attribute and relationship
   keys).
3. (Optional) For maximum performance, delete the three-argument
   constructor if you don't use the arguments. If you need custom
   logic in your constructor but don't need the three arguments,
   implement a custom default constructor. If you don't need a custom
   constructor, don't implement one at all; the compiler inserts
   the default constructor for you. If the three-argument constructor
   is present, EOF uses it; otherwise the default constructor is invoked.
4. (Optional) For maximum performance, delete all accessors that
   don't contain custom logic. If you want strong typing to simplify
   business logic, implement accessors using `storedValueForKey`,
   such as:
   > ```
   > public NSGregorianDate dateReleased() {
   >     return (NSGregorianDate)storedValueForKey("dateReleased");
   > }
   > ```

In lieu of (or in addition to) adding custom accessors, it
might be convenient to add and use String constants for an enterprise
object class's keys, as shown in the following:

> ```
> public class Movie extends EOGenericRecord {
>     public static final String Title = "title";
>     public static final String DateReleased = "dateReleased";
>     public static final String Studio = "studio";
>
>     public NSGregorianDate dateReleased() {
>         return (NSGregorianDate)storedValueForKey(DateReleased);
>     }
> }
> ```

## Deferred Faulting

EOF uses faults as stand-ins for objects whose data has not
yet been fetched. Although fault creation is much faster than fetching,
fault instantiation still takes time. To improve performance, EOF
4.5 has the ability to use __deferred faults__ (which
are more efficient) for enterprise object classes that enable the
feature.

In an object whose class enables deferred faulting, the object's
relationships are initially set to deferred faults. For a particular
relationship, a single deferred fault is shared between all instances
of an enterprise object class. This sharing of deferred faults can
significantly reduce the number of faults that need to be created,
and usually reduces the overhead of fault creation during a fetch.

For example, consider a Movie class with a `studio` relationship.
Assuming the worst case in which each movie has a different studio,
without deferred faulting, during a fetch of twenty Movie objects,
twenty faults are created for the `studio` relationship-one
fault for each movie. With deferred faulting, only one fault is
created-a deferred fault that is shared by all the movies.

Deferred faults have a special fault handler, which knows
how to replace the deferred fault with a standard fault. Once the
deferred fault is replaced with a normal fault, the normal faulting
behavior applies.

In 4.5, EOGenericRecord enables deferred faulting; you get
the behavior without making any changes to existing code. Non-EOGenericRecord
enterprise object classes don't enable deferred faulting by default.
To enable it on a custom class, implement the class method `useDeferredFaultCreation` to
return `true`/`YES` (the
default is `false`/`NO`).
Additionally, invoke the method `willReadRelationship` before
accessing a relationship that might be a deferred fault. The `willReadRelationship` method
allows the special fault handler to instantiate a normal fault before
it is accessed.

### Deferred Faulting and Inheritance

In Java programming, there's an additional benefit of deferred
faulting: Deferred faulting allows you to have to-one relationships
into an inheritance hierarchy. Without deferred faulting, a to-one
relationship to a non-leaf entity is impossible without implementing workarounds
(because of strong typing in the Java language). The workarounds
are not necessary if you use deferred faulting. For more information
on the inheritance limitation in Java and the workarounds, refer
to the _Enterprise Objects Framework Developer's Guide_.

### Related API Changes

New API added to support the deferred faulting feature is
summarized in this section.

__EODeferredFaulting interface/informal
protocol (EOControl/EOFault.h)__

| __New or Changed API__ | __Description__ |
| `useDeferredFaultCreation` | A static/class method that defaults to `false`/`NO`. Override to return `true`/`YES` on your enterprise object class to use deferred fault creation.  EOGenericRecord's implementation returns `true`/`YES`, indicating that it uses the more efficient deferred fault technique.  Note that in Java, this static method is not a formal part of the EODeferredFaulting interface because the Java language doesn't support the inclusion of static methods in an interface. It is, however, an informal part of the interface. A static method implemented in a custom enterprise object class will be invoked automatically to determine whether or not to use deferred fault creation. |
| `willReadRelationship` (Java)  `willReadRelationship:` (Objective-C) | Invoke this before using any relationship in an enterprise object that uses deferred fault creation. This method sets the corresponding instance variable of the receiver using `takeStoredValueForKey`/`takeStoredValue:forKey:`. Returns a newly instantiated fault if the object is a fault and has a deferred fault handler. Returns the object otherwise. |

__EOFaultHandler (EOControl/EOFaultHandler.h)__

| __New or Changed API__ | __Description__ |
| `createFaultForDeferredFault` (Java)   `createFaultForDeferredFault:sourceObject:` (Objective-C) | Invoked by `willReadRelationship` to ensure that a fault is valid. EOFaultHandler's implementation simply returns its fault. |

## Snapshot Reference Counting

Snapshot reference counting is a new feature that removes
snapshots from an EODatabase when they are no longer used by any
enterprise objects in an application. This feature reduces the memory
footprint of WebObjects applications.

|  |
| --- |
| __Note:__ Snapshot reference counting is not available in the client side of Java Client applications. The corresponding API is in the Java Client packages, but the snapshots are not released. |

The reference count on a snapshot is implicitly incremented
when you create an enterprise object, either by fetching it in a
batch or by faulting it in. An EOEditingContext decrements the reference
count automatically when it forgets or refaults an enterprise object.

To support this feature, the method `editingContextDidForgetObjectWithGlobalID`/ `editingContext:didForgetObjectWithGlobalID:` has
been added to EOObjectStore. This method is not intended to be called
directly by your application.

As a developer you should not worry about this feature; it
should just work without any additional code on your part. There
are only a few cases where it could be incompatible with pre-EOF
4.5 applications:

- When the snapshots are removed because their
  reference counts fall to zero, the globalID associated with these
  snapshots are also released. If your application is written in Objective-C
  and you cache globalIDs in your application, make sure you retain
  them. If you don't, your application will crash with "Message
  sent to freed object" errors when you try to access globalIDs
  that have been freed. Previously GlobalIDs were never released;
  they were kept with the snapshots. This is not a problem if you
  use Java as your development language, since Java automatically retains
  all referenced objects.
- If your application assumes that snapshots for fetched objects
  are always present, you could have a problem. This is no longer
  the case, and asking for a snapshot might now return `null`/`nil`.

Sometimes you want a snapshot to stay around for the lifetime
of your application. If you need this functionality there are three
ways to force selected snapshots to stay around:

- Use the method `incrementSnapshotCountForGlobalID` on
  EODatabase to force the snapshot to stay around. If you use this
  approach, make sure to call `decrementSnapshotCountForGlobalID` when
  you don't need the snapshot anymore.
- Fetch the objects whose snapshots you need. (Note that if
  your application is written in pure Objective-C and it's not
  multithreaded, the EOEditingContext doesn't retain its enterprise
  objects-you have to retain them yourself.)
- Turn on entity caching for the entity. This automatically
  increments the reference count for all the snapshots your entity
  caches.

You can turn the whole feature off and revert to the previous
behavior of retaining snapshots forever by invoking the class method `disableSnapshotRefCounting` on EODatabase.
Make sure to call this method early in your application initialization
code, before the creation of any EODatabase instances.

### Related API Changes

The following tables summarize new or changed API to support
the snapshot reference counting feature.

__EODatabase (EOAccess/EODatabase.h)__

| __New or Changed API__ | __Description__ |
| `incrementSnapshotCountForGlobalID` (Java)  `incrementSnapshotCountForGlobalID:` (Objective-C) | If the receiver releases unreferenced snapshots, increments the reference count for the shared snapshot associated with the specified globalID. |
| `decrementSnapshotCountForGlobalID` (Java)  `decrementSnapshotCountForGlobalID:` (Objective-C) | If the receiver releases unreferenced snapshots, decrements the reference count for shared snapshot associated with the specified globalID; if no more objects refer to the snapshot, removes it from the snapshot table. |
| `disableSnapshotRefCounting` | A static/class method that disables the snapshot reference counting feature so that instances don't release snapshots. |

__EOObjectStore (EOControl/EOObjectStore.h)__

| __New or Changed API__ | __Description__ |
| `editingContextDidForgetObjectWithGlobalID` (Java)  `editingContext:didForgetObjectWithGlobalID:` (Objective-C) | Invoked to inform the object store that it can stop keeping data about an object it passed to a child. Don't invoke this method; it is invoked automatically by the Framework. |

## Snapshot Timestamping

EOF caches database snapshots and uses the cached values to
initialize objects. This significantly improves performance, since
using the cached values is much faster than making round-trips to
the database for fetches. However, this behavior can lead to staleness
of the cached data; and it sometimes produces confusing results,
especially when new values available from a fetch are ignored in
favor of the stale snapshots.

A new snapshot timestamping feature updates snapshots appropriately
when fetching and allows an editing context to request that the
snapshots used to build enterprise objects are no older than the
editing context's `fetchTimestamp`. The
default value for the `fetchTimestamp` of
a new editing context is one hour earlier than the creation time
of the editing context. So any snapshots that are less than an hour
old are acceptable to the editing context; older cached values are
ignored. The default "lag" can be adjusted using the static method `setDefaultFetchTimestampLag` (or
the corresponding Objective-C class method), and the `fetchTimestamp` for
a specific editing context can be set directly with `setFetchTimestamp`.

Note that the `fetchTimestamp` is significant
only when fetching data (typically by sending `objectsWithFetchSpecification`).
An existing enterprise object is unaffected by changes to the editing
context's `fetchTimestamp`.

When an EODatabase records a snapshot, it now also records
a timestamp for that snapshot. The timestamp is an NSTimeInterval
(relative to the reference date as documented for the NSDate class).
Methods that return a snapshot from EODatabase or EODatabaseContext
now have variants that take an extra argument to specify a minimal timestamp
for the snapshot. If the recorded snapshot's timestamp is earlier
than the requested time, `null`/`nil` is
returned. If the snapshot is recent enough for the request, the snapshot
is returned as usual.

### Related API Changes

The following tables summarize new API added to support the
snapshot timestamp feature.

|  |
| --- |
| __Note:__ Support for snapshot timestamping is not available in the com.apple.client packages. However, since snapshots are maintained only on the server, no timestamping takes place on the client side of a Java Client application. In other words, this feature can be used to its fullest potential in a Java Client application. |

__EODatabase (EOAccess/EODatabase.h)__

| __New or Changed API__ | __Description__ |
| `DistantPastTimeInterval`(Java)  `EODistantPastTimeInterval` (Objective-C)  (constant) | The NSTimeInterval used as a lower bound on timestamps. |
| `setTimestampToNow` | Sets the internal timestamp to value returned by NSDate's `timeIntervalSinceReferenceDate` method. Used for recording subsequent snapshots. |
| `snapshotForGlobalID(EOGlobalID)` `snapshotForGlobalID(EOGlobalID, double)`  (Java) | The new, overloaded version of this method takes a double argument to use as a timestamp. It returns the snapshot associated with the specified globalID. Returns `null` if there isn't a snapshot or if its timestamp is less than the specified timestamp.  The old version that only takes a globalID has been reimplemented to invoke the new version using `DistantPastTimeInterval` as the timestamp. |
| `snapshotForSourceGlobalID(EOGlobalID, String)` `snapshotForSourceGlobalID(     EOGlobalID,      String,      double)`  (Java) | The new, overloaded version of this method takes a double argument to use as a timestamp. It returns the to-many snapshot for the specified globalID and relationship name. Returns `null` if there isn't a to-many snapshot or if the timestamp is less than the specified timestamp.  The old version that only takes a globalID and a String has been reimplemented to invoke the new version using `DistantPastTimeInterval` as the timestamp. |
| `snapshotForGlobalID:after:` (Objective-C) | Returns the snapshot associated with the specified globalID. Returns `nil` if there isn't a snapshot or if its timestamp is less than the specified timestamp.   Note that `snapshotForGlobalID:` has been reimplemented to invoke `snapshotForGlobalID:after:` with `EODistantPastTimeInterval` as the timestamp. |
| `snapshotForSourceGlobalID:relationshipName:after:` (Objective-C) | Returns the to-many snapshot for the specified globalID and relationship name. Returns `nil` if there isn't a to-many snapshot or if the timestamp is less than the specified timestamp.   Note that `snapshotForSourceGlobalID:relationshipName:` has been reimplemented to invoke `snapshotForSourceGlobalID:relationshipName:after:` with `EODistantPastTimeInterval` as the timestamp. |
| `timestampForGlobalID` (Java)  `timestampForGlobalID:` (Objective-C) | Returns the timestamp of the snapshot for the specified globalID. Returns `(EO)DistantPastTimeInterval` if there isn't a snapshot. |
| `timestampForSourceGlobalID` (Java)  `timestampForSourceGlobalID:relationshipName:` (Objective-C) | Returns the timestamp of the to-many snapshot for the specified globalID. Returns `(EO)DistantPastTimeInterval` if there isn't a snapshot. |

__EODatabaseContext (EOAccess/EODatabaseContext.h)__

| __New or Changed API__ | __Description__ |
| `snapshotForGlobalID(EOGlobalID)` `snapshotForGlobalID(EOGlobalID, double)`  (Java) | The new, overloaded version of this method takes a double argument to use as a timestamp. It returns the snapshot associated with the specified globalID. Returns `null` if there isn't a snapshot or if its timestamp is less than the specified timestamp. Searches first locally (in the transaction scope) and then in the receiver's EODatabase.  The old version that only takes a globalID has been reimplemented to invoke the new version using `DistantPastTimeInterval` as the timestamp. |
| `snapshotForSourceGlobalID(EOGlobalID, String)`  `snapshotForSourceGlobalID(     EOGlobalID,     String,     double)`  (Java) | The new, overloaded version of this method takes a double argument to use as a timestamp. It returns the to-many snapshot for the specified globalID and relationship name. Returns `null` if there isn't a to-many snapshot or if the timestamp is less than the specified timestamp.  The old version that only takes a globalID and a String has been reimplemented to invoke the new version using `DistantPastTimeInterval` as the timestamp. |
| `snapshotForGlobalID:after:` (Objective-C) | Returns the snapshot associated with the specified globalID. Returns `nil` if there isn't a snapshot or if its timestamp is less than the specified timestamp. Searches first locally (in the transaction scope) and then in the receiver's EODatabase.  Note that `snapshotForGlobalID:` has been reimplemented to invoke `snapshotForGlobalID:after:` with `EODistantPastTimeInterval` as the timestamp. |
| `snapshotForSourceGlobalID:relationshipName:after:` (Objective-C) | Returns the to-many snapshot for the specified globalID and relationship name. Returns `nil` if there isn't a to-many snapshot or if the timestamp is less than the specified timestamp.  Note that `snapshotForSourceGlobalID:relationshipName:` has been reimplemented to invoke `snapshotForSourceGlobalID:relationshipName:after:` with `EODistantPastTimeInterval` as the timestamp. |

__EOEditingContext (EOControl/EOEditingContext.h)__

| __New or Changed API__ | __Description__ |
| `setDefaultFetchTimestampLag` (Java)  `setDefaultFetchTimestampLag:` (Objective-C) | A static/class method that assigns the default timestamp lag for new editing contexts. The default value is 3600.0 seconds (one hour).  When a new editing context is initialized, it is assigned a fetch timestamp equal to the current time less the default timestamp lag. Setting the lag too high might cause every new editing context to accept very old cached data. Setting the lag too low might degrade performance due to excessive fetching. A negative lag value is treated as 0.0. |
| `defaultFetchTimestampLag` (Java)  `defaultFetchTimestampLag` (Objective-C) | A static/class method that returns the default timestamp lag. |
| `setFetchTimestamp` (Java)  `setFetchTimestamp:` (Objective-C) | Sets the receiver's fetch timestamp. When an editing context fetches objects from its parent object store, the parent object store can use the timestamp to determine whether to use cached data or to refetch the most current values. An editing context prefers that fetched values are at least as recent as its fetch timestamp. Note that the parent object store is free to ignore the timestamp; so this value should be considered a hint or request and not a guarantee.  Changing the fetch timestamp has no effect on existing objects in the editing context; it can affect only subsequent fetches. To refresh existing objects, invoke `refaultObjects` before you invoke `setFetchTimestamp`.The initial value for the fetch timestamp of a new non-nested editing context is the current time less the `defaultFetchTimestampLag`. A nested editing context always uses its parent's fetch timestamp. `setFetchTimestamp` raises if it's invoked on a nested editing context. |
| `fetchTimestamp` | Returns the receiver's fetch timestamp. |

## Handling Missing Faults

In previous versions of EOF, if a fault fired but no corresponding
database row could be found (for example because of a referential
integrity problem or because the row was deleted without EOF's
knowledge), the delegate method `databaseContextFailedToFetchObject`/`databaseContext:failedToFetchObject:globalID:` was
called. If the delegate didn't fix the problem, an exception was
raised immediately. In 4.5, The delegate is invoked, but the exception
is delayed or avoided, and an empty enterprise object is returned.
If the application later tries to save an object graph that requires
the missing fault, the exception is raised during `saveChanges`.
If the object is never needed, no exception is raised.

### Related API Changes

The following tables summarize new API added to support the
better handling of missing faults.

__EODatabaseContext (EOAccess/EODatabaseContext.h)__

| __New or Changed API__ | __Description__ |
| `missingObjectGlobalIDs` | Returns the globalIDs of any "missing" enterprise objects. Returns an empty array if no missing objects are known to the receiver. An object is "missing" when a fault fires and the corresponding row for the fault isn't found in the database.  To be notified when a missing object is discovered, implement the delegate method `databaseContextFailedToFetchObject`/`databaseContext:failedToFetchObject:globalID:`.  If an application tries to save a missing object, an exception is raised. |

__EODatabaseContext Delegate
(EOAccess/EODatabaseContext.h)__

| __New or Changed API__ | __Description__ |
| `databaseContextFailedToFetchObject` (Java)  `databaseContext:failedToFetchObject:globalID:` (Objective-C)  (changed behavior) | Invoked when a to-one fault can't find its data in the database. Now if the method returns `false`/`NO`, the specified database context doesn't immediately raise as before. Instead, it simply tracks the globalID of the offending object. If the tracked globalID is in the list of updated objects when `prepareForSaveWithCoordinator`/`prepareForSaveWithCoordinator:editingContext:` is invoked (`saveChanges` invokes this method), an exception is raised.   To get a list of the objects that failed to fetch, see the method `missingObjectGlobalIDs`. |

## Automatic Database Reconnection

In EOF 4.5, a concrete adaptor can now implement methods that
cause EOF to automatically attempt to reconnect to a database server
when a connection is unexpectedly dropped. This behavior handles
the problem of transient communication failures. By default reconnection
is attempted by all of the adaptors that ship with EOF 4.5.

EOF now sends `isDroppedConnectionException` to
the adaptor if an exception is raised during fetching or saving.
If the adaptor returns `true`/`YES`,
then it attempts to reconnect to the database and retry the operation.
(The adaptor context must also implement `handleDroppedConnetion` to
clean up the state of the context and its channels before the reconnection
is attempted.) If the reconnection attempt fails, the exception
from the failure is raised as usual.

The delegate method `reconnectionDictionaryForAdaptor` can
be used to provide a new connection dictionary for the reconnection
attempt. If the delegate is not implemented, the adaptor uses its
existing connection dictionary when reconnecting to the server.

You can completely override the database reconnection behavior
with the delegate method `databaseContextShouldHandleDatabaseException` (Java)
or `databaseContext: shouldHandleDatabaseException` (Objective-C).
For more information, see [Table 5-20](#apple-inbeorkiivdui).

### Related API Changes

The following tables summarize new API added to support the
database reconnection feature.

__EOAdaptor (EOAccess/EOAdaptor.h)__

| __New or Changed API__ | __Description__ |
| `handleDroppedConnection` | The adaptor cleans up after a dropped connection by sending `handleDroppedConnection` to all of its adaptor contexts and then clearing its array of contexts.  If the receiver's delegate implements `reconnectionDictionaryForAdaptor`, that method is invoked and the result is used as the new connection dictionary for the adaptor. Otherwise, the adaptor attempts new connections using the original connection dictionary.  You should never invoke this method; it is invoked automatically by the Framework. Subclasses don't normally need to override the superclass implementation. |
| `isDroppedConnectionException` (Java)  `isDroppedConnectionException:` (Objective-C) | Returns `true`/`YES` if the exception is one that the adaptor can attempt to recover from by reconnecting to the database, `false`/`NO` otherwise. The default implementation returns `false`/`NO`. Subclasses should implement it to allow for automatic database reconnection. |

__EOAdaptor Delegate (EOAccess/EOAdaptor.h)__

| __New or Changed API__ | __Description__ |
| `reconnectionDictionaryForAdaptor` (Java)  `reconnectionDictionaryForAdaptor:`(Objective-C) | Invoked from `handleDroppedConnection`. If this method returns a non-`null`/`nil` value, the value is used as the adaptor's new connection dictionary.   The delegate is responsible for guaranteeing that the new connection dictionary is compatible with any EODatabase that is using the adaptor. If reconnection succeeds, the EODatabase continues to use its database snapshots as if nothing had happened. Therefore, the new database server should have the same data as the original. |

__EOAdaptorContext (EOAccess/EOAdaptorContext.h)__

| __New or Changed API__ | __Description__ |
| `handleDroppedConnection` | Implemented by subclasses to provide automatic database reconnection support. If database reconnection is not supported, subclasses don't have to implement it.  Subclass implementations should clean up the state of the adaptor context and its associated adaptor channels so that they can be safely released and deallocated without any errors.  Don't invoke this method; it's invoked automatically by the Framework. |

__EODatabase (EOAccess/EODatabase.h)__

| `handleDroppedConnection` | Received when a dropped connection is detected to initiate cleanup. It cleans up by sending `handleDroppedConnection` to its adaptor, and then sending `handleDroppedConnection` to all of its registered database contexts. When the cleanup procedure is complete, the Framework can automatically reconnect to the database.  Don't invoke this method; it's invoked automatically by the Framework. |

__EODatabaseContext (EOAccess/EODatabaseContext.h)__

| `handleDroppedConnection` | Cleans up after a dropped connection by effectively releasing adaptor context and database channels, and then creating a new adaptor context.  Don't invoke this method; it's invoked automatically by the Framework. |

__EODatabaseContext Delegate
(EOAccess/EODatabaseContext.h)__

| `databaseContextShouldHandleDatabaseException` (Java)  `databaseContext:shouldHandleDatabaseException:` (Objective-C) | Invoked when an exception is thrown in response to a lost database connection. Implement this method only if you want to override the default reconnection behavior. If the delegate method is not implemented, the reconnection decision is made according to the adaptor's response to `isDroppedConnectionException` (`isDroppedConnectionException:` in Objective-C).  The implementation of this method should inspect the exception to determine if the exception is a response to a dropped connection. If not, the delegate should simply raise the specified exception. If the exception is in response to a dropped connection, the method can return `true`/`YES` to allow the database context to handle the exception by automatically reconnecting to the database or can return `false`/`NO` to customize connection behavior.  If the delegate returns `false`/`NO`, then the delegate is responsible for handling the exception and implementing an appropriate reconnection strategy. The database context retries the operation that generated the original exception without doing any additional clean up and without attempting to reconnect to the database. |

## Setting Access Layer Delegates

EOAdaptor, EOAdaptorContext, and EODatabaseContext now implement
the static method `setDefaultDelegate` to
simplify the setting of delegates for new instances of those classes
(there are corresponding class methods in Objective-C). By default,
the default delegate for those classes is `null`/`nil`.
However, `setDefaultDelegate` can be used
to establish a default delegate for a particular class that will
be assigned to any new instance of that class when the instance
is initialized.

### Related API Changes

The following tables summarize new API added to support the
database reconnection feature.

__EOAdaptor (EOAccess/EOAdaptor.h)__

| __New or Changed API__ | __Description__ |
| `setDefaultDelegate` (Java)  `setDefaultDelegate:` (Objective-C) | A static/class method that sets the default delegate for all newly created EOAdaptor instances. That is, specifies the object that is assigned as delegate to new adaptor objects. |
| `defaultDelegate` | A static/class method that returns the default delegate. |

__EOAdaptorContext (EOAccess/EOAdaptorContext.h)__

| __New or Changed API__ | __Description__ |
| `setDefaultDelegate` (Java)  `setDefaultDelegate:` (Objective-C) | A static/class method that sets the default delegate for all newly created EOAdaptorContext instances (and their EOAdaptorChannels). That is, specifies the object that is assigned as delegate to new adaptor context objects and their channels. |
| `defaultDelegate` | A static/class method that returns the default delegate. |

__EODatabaseContext (EOAccess/EODatabaseContext.h)__

| __New or Changed API__ | __Description__ |
| `setDefaultDelegate` (Java)  `setDefaultDelegate:` (Objective-C) | A static/class method that sets the default delegate for all newly created EODatabaseContext instances. That is, specifies the object that is assigned as delegate to new database context objects. |
| `defaultDelegate` | A static/class method that returns the default delegate. |

## Key Value Coding Changes

EOF 4.5 introduces two improvements to key-value coding: The
addition of key binding objects and the enforcement of lowercase
key names. The follow sections describe each.

### Key Bindings

New key-value coding primitives have been introduced. The
new primitives are based on __bindings__, which associate
a class/key pair to a mechanism for accessing the key. There are two
types of bindings, __get bindings__ and __set
bindings__. They are represented by the new class EOKeyBinding.

To access an object's data with key-value coding, clients
typically use the EOKeyValueCoding and EOKeyValueCodingAdditions
methods `valueForKey`, `takeValueForKey`,
and so on. However, in EOF 4.5, clients can optimize access by obtaining and
caching bindings for particular class/key combinations and applying
those bindings directly. Classes can override the EOKeyValueCoding
methods (such as `valueForKey)` directly,
but overriding `keyValueBindingForKey` to
return an appropriately initialized binder object provides the maximum
performance benefit.

|  |
| --- |
| __Note:__ The need to override the default key-value coding methods, particularly the new binding primitives, is extremely rare. The default behavior is very efficient and should be well suited to almost any application. |

Clients caching bindings are responsible for checking that
the class of the object to which a binding is applied matches the
target class of the binding. Using a binding obtained from one class
on an object of another results in undefined behavior.

### Enforcing Lowercase Key Names

EOF expects keys to begin with a lowercase letter. It now
logs a warning if that restriction is violated. For backwards compatibility
with previous releases which did not strictly check capitalization,
you can use the EOKeyValueCoding.KeyBinding static method `suppressCapitalizedKeyWarning` to
suppress the warning for capitalized keys (EOKeyBinding class method
in Objective-C). However, note that this method is deprecated
and will be removed in a future release.

### Related API Changes

The following new classes have been added to support key value
bindings:

- EOKeyValueCoding.KeyBinding (Java) and EOKeyBinding
  (Objective-C)
- EOKeyValueCoding.KeyGetBinding (Java) and EOKeyGetBinding
  (Objective-C)
- EOKeyValueCoding.KeySetBinding (Java) and EOKeySetBinding
  (Objective-C)

For more information, see the class specification for EOKeyValueCoding.KeyBinding/EOKeyBinding.

In addition, the EOKeyValueCoding interface/informal protocol
has been enhanced to create and return key bindings. In Java, the
new methods are defined in a new interface called EOKeyValueCoding.KeyBindingCreation.
In Objective-C, the new methods are defined in EOKeyValueCoding.h.
For more information, see the EOKeyValueCoding.KeyBindingCreation
interface specification (Java) or the EOKeyBindingCreation informal
protocol specification (Objective-C).

## Recursive Reader and Writer Locks

A new class, EOMultiReaderLock, provides EOF with recursive
reader and writer locks. The locks are recursive; a single thread
can request a lock many times, but a lock is actually taken only
on the first request. Likewise, when a thread indicates it's finished
with a lock, it takes an equal number of unlock calls to return
the lock.

There is no limit on the number of reader locks that can be
taken by a process. However, there can only be one writer lock at
a time, and a writer lock is not issued until all reader locks are
returned. (Reader locks aren't issued to new threads when there
is a thread waiting for a writer lock, but threads that already
have a reader lock can increment their lock count.)

Thread safety is maintained by using mutex locks (binary semaphores),
which ensures that no more than one critical section of the class
can be processed at a time. The queueing order of requests for writer
locks is not managed by the class; the underlying implementation
of mutex signaling manages the queue order.

EOMultiReaderLock correctly handles promotion of a read lock
to a write lock, and the extension of a reader lock to the current
writer. This prevents a thread from deadlocking on itself when requesting
a combination of lock types.

EOMultiReaderLocks are slightly more time-expensive than NSRecursiveLocks
because the recursion count has to be stored per-thread, causing
each request for a reader lock to incur a hash. Writer locks are
even more expensive because EOMultiReaderLock must poll the hashtable
until all reader locks have been returned before the writer lock
can be taken.

### Related API Changes

A new class, EOMultiReaderLock, has been added to the Framework
to support the new multi reader and writer lock feature. For more
information, see the corresponding class specification.

|  |
| --- |
| __Note:__ This class doesn't exist in com.apple.client.eocontrol. Multithreaded clients aren't yet supported in Java Client applications. All the client-side locks in Java Client application's are no-ops. |

## LDAP Adaptor Example

EOF 4.5 comes with a new sample adaptor: the LDAP adaptor.
It provides read, modify, and delete access and limited support
for inserting. Additionally it provides a simple way to verify a
user's password on the Web with an LDAP server without requiring
a model.

### LDAP Client Libraries

The LDAP adaptor is ready to use when you install WebObjects.
The source code is provided so that you can use a different client
library or enhance the adaptor yourself.

The LDAP adaptor consists of two pieces: The adaptor framework
and an LDAP client library. Apple ships a client library based on
the public University of Michigan LDAP Client. You can build and
install this library as a framework, or you can substitute your own
client library, such as the Netscape LDAP library. (The latter has
not been tested, but both libraries conform to RFC 1823, the LDAP
client API).

### Creating Models

You create a model for an LDAP server with EOModeler the way
you create models for other adaptors. Simply choose New from the
Model menu, and choose LDAP as the adaptor for the new model.

|  |
| --- |
| __Note:__ If all you are trying to do is authenticate users using an LDAP server's usernames and encrypted passwords, you don't need to create a model. See ["Performing Authentication"](#apple-infecrcbivauo). |

#### Logging In

The LDAP adaptor defines the following connection keys, which
are represented in the login panel:

**Server Name**
: The server's address. Either an IP address (e.g. 17.205.15.205)
or a name (e.g. ldap.bigfoot.com). If you are inside a corporate
firewall, it might not allow LDAP traffic to pass through. Check
with your administrator if you have trouble accessing LDAP servers
on the open internet.

**User Name**
: If your LDAP server requires you to login, enter a username.
This version of the LDAP adaptor supports simple authentication
only.

**Password**
: If your LDAP server requires a password, enter it here.

**Search Base**
: Entries on an LDAP server (roughly equivalent to rows
in a database) are organized in trees. The search base indicates
what branch of the tree to begin searching in. Common designs are
to have the top level of the tree have country or organization branches,
so good search bases have the form "c=US" or "o=Apple Computer".
An approximate database equivalent is to say the search base is
ANDed with any qualifiers you pass in.

**Schema Base**
: This value is used only during reverse engineering the
LDAP server. The Adaptor looks at this location for the subschema
entry. Note that during reverse engineering, the scope is temporarily
overridden to Base because the subschema does not have any children.

**Value Separator**
: The character used to separate multiple values for a
property.

**Port**
: LDAP servers are almost always on port 389, but secure
servers might use a different port.

**Timeout**
: Maximum time to wait during LDAP operations before raising
an exception. Timeouts come from the client library and are raised
as EOGeneralAdaptorExceptions.

**Scope**
: LDAP entries belong to an object class. The Adaptor
maps each class to an entity. Like classes in object-oriented programming,
LDAP classes have an inheritance hierarchy. Depending on the scope
you set, results include results from the that object class only
(Base), its immediate children (One Level), or the entire subtree
(Subtree). The more you include, the larger the result set is for
a given search. Object class hierarchies and entry hierarchies work
together to give order to the LDAP server's data, and the Adaptor
provides control over how ordered or chaotic the data appears.

#### If Reverse Engineering Fails

The LDAP specification does not require LDAP servers to provide
a means of learning the server's layout; providing a schema to
clients is optional. For this reason, the LDAP adaptor might not
be able to reverse-engineer your LDAP server to generate an EOModel automatically.
If this is the case, you might need to create your model by hand.

Generally speaking, Netscape Directory Servers automatically
create and provide schemas to clients. So, if you have a Netscape
Directory server, you should be fine.

However, if the adaptor can't find subschema information,
it creates a default model with two entities: Person and NoSchemaDataAvailable.
If the server is ldap.bigfoot.com (a well known
server) and the scope is set to Subtree, this model works for finding
names. The NoSchemaDataAvailable entity is designed to be an error
message and should be deleted from the model. (EOAdaptors aren't
allowed to return `null`/`nil` when
reverse engineering a database, so the best alternative is to return
a minimal model.)

### Adding Entries to the Server

The LDAP adaptor provides limited support for adding entries
to the server. If you plan to use the adaptor to insert entries,
keep the following points in mind:

- The LDAP adaptor doesn't provide automatic
  primary key generation. so set the primary key (the distinguished
  name, or "dn") as a class property and set an appropriate value
  yourself before saving a new entry.
- Consider adding an objectclass attribute to the entity so
  your can add the entry to multiple classes at once.
- You must enforce object rules in custom code. The adaptor
  detects object class violations once you attempt to save changes,
  but the violations cause the adaptor to raise an exception.

### Performing Authentication

One of the common applications for LDAP is to verify a user's
password on the Web. The authentication is generally done by the
LDAP server, not by retrieving the user's password from an LDAP
entry. So, in essence, all that is needed is a mutable connection
dictionary from a model and a request to validate the connection.
The LDAP Adaptor provides a simple way to do this without a model:

> ```
> java.lang.Throwable athenticateUser()
> ```

or in Objective-C,

> ```
> + (NSException *)authenticateUserString:(NSString *)userString
>     password:(NSString *)password
>     withServer:(NSString *)server
>     matchOnAttribute:(NSString *)searchAtt
>     searchBase:(NSString *)base
>     searchScope:(NSString *)scope;
> ```

The method is pretty easy to use and the header file contains
specifics on its use. Here is a sample code fragment from a WebObjects
application that has one page, "Main" with three instance variables: `userName1`, `password1`,
and `isLoggedIn`. This
method is tied to the web page's Submit button.

> ```
> - authenticateUser {
>     NSException *exception;
>     exception = [LDAPAdaptor authenticateUserString:userName1
>             password:password1
>             withServer:@"bigbird.apple.com"
>             matchOnAttribute:@"cn"
>             searchBase:@"o=apple computer" searchScope:@"Subtree"];\x93
>     if (exception) {
>         NSLog(@"Auth failed.");
>         isLoggedIn = NO;
>     } else {
>         NSLog(@"Auth successful.");
>         isLoggedIn = YES;
>     }
>     return self;
> }
> ```

Or, in Java (`isLoggedIn` is
a string instead of a BOOL in this example):

> ```
> public WOComponent authenticateUser() {
>     java.lang.Throwable ex = null;
>     ex = LDAPAdaptor.authenticateUser (
>         userName,
>         pswField,
>         "bigbird.apple.com",
>         "cn",
>         "o=Apple Computer",
>         "Subtree");
>     if (ex == null) {
>           isLoggedIn = "You are now logged in.";
>     } else {
>         isLoggedIn = ex.getMessage();
>     }
>     return this;
> }
> ```

## Miscellaneous API Enhancements

This section summarizes other miscellaneous methods added
in EOF 4.5 not covered in the other sections.

__EOAdaptorContext (EOAccess/EOAdaptorContext.h)__

| __New or Changed API__ | __Description__ |
| `hasOpenTransaction` | Returns `true`/`YES` if a transaction is open (begun but not yet committed or rolled back). For more information on this addition, see the section ["Deprecated API"](#apple-inbeoqsginfem). |

__EODatabaseContext Delegate
(EOAccess/EODatabaseContext.h)__

| __New or Changed API__ | __Description__ |
| `databaseContextWillFireObjectFaultForGlobalID` (Java)  `databaseContext:     willFireObjectFaultForGlobalID:     withFetchSpecification:     editingContext:` (Objective-C) | Invoked just before the Framework-generated fetch specification (provided as an argument) is used to clear the fault for the specified globalID.  Note that it is very dangerous to modify the fetch specification. |
| `databaseContextWillFireArrayFaultForGlobalID` (Java)  `databaseContext:     willFireArrayFaultForGlobalID:     relationship:     withFetchSpecification:     editingContext:` (Objective-C) | Invoked just before the Framework-generated fetch specification (provided as an argument) is used to clear the fault for the specified globalID and relationship.  Note that it is very dangerous to modify the fetch specification. |

__EOEditingContext Additions (Objective-C only; EOAccess/EOUtilities.h)__

| __New or Changed API__ | __Description__ |
| `createAndInsertInstanceOfEntityNamed:` | Creates a new enterprise object of the specified entity, inserts it into the receiving editing context, and returns the new object. |

__EOUtilities (Java)__

| __New or Changed API__ | __Description__ |
| `createAndInsertInstance` | Creates a new enterprise object of the specified entity, inserts it into the specified editing context, and returns the new object. |

__EOClassDescription (EOControl/EOClassDescription.h)__

| __New or Changed API__ | __Description__ |
| `fetchSpecificationNamed` (Java)  `fetchSpecificationNamed:`(Objective-C) | The receiver returns the fetch specification it associates with the specified name. EOClassDescription's implementation returns `null`/`nil`; subclasses can override it to return a fetch specification. |

__EOFetchSpecification (EOControl/EOFetchSpecification.h)__

| __New or Changed API__ | __Description__ |
| `fetchSpecificationNamed` (Java)   `fetchSpecificationNamed:entityNamed:` (Objective-C) | A static/class method that returns the fetch specification that the specified entity associates with the specified fetch specification name. |

__EOQualifier (EOControl/EOQualifier.h)__

| __New or Changed API__ | __Description__ |
| `evaluateWithObject` (Java)  `evaluateWithObject:` (Objective-C) | Implemented by subclasses to return `true`/`YES` if the provided object matches the criteria specified in the receiver, `false`/`NO` otherwise. The argument should be an enterprise object, a snapshot dictionary, or something that implements key-value coding. |
| `allQualifierKeys` | Returns an NSSet of strings, which are the left-hand sides of all the qualifiers in the receiver. For example, if you have a qualifier  salary > 10000 AND manager.lastName = 'smith'  `allQualifierKeys` returns an array containing the strings "salary" and "manager.lastName".  Subclasses should not override this method, instead they should override `addQualifierKeysToSet`. |
| `addQualifierKeysToSet` (Java)  `addQualifierKeysToSet:` (Objective-C) | Adds the receiver's qualifier keys to the specified NSMutableSet. The subclasses in the EOControl framework do this by traversing the tree of qualifiers. Node qualifiers (such as EOAndQualifier) recursively invoke this method until they reach a leaf qualifier (such as EOKeyValueQualifier) which adds its key to the set.   Subclasses of EOQualifier must implement this method. |

__EOTemporaryGlobalID__

| __New or Changed API__ | __Description__ |
| `assignGloballyUniqueBytes` (Java only) | This method, which was not wrapped in 4.0, is the equivalent of the Objective-C method, `assignGloballyUniqueBytes:`, which assigns a network-wide unique ID |

__EOAssociation (EOInterface/EOAssociation.h)__

| __New or Changed API__ | __Description__ |
| `isExplicitlyDisabled` (Java Client only)  `setExplicitlyDisabled` (Java Client only) | Returns or sets whether or not the association is explicitly disabled. These methods are used by the new user interface generation layer, which is described in ["Direct To Java Client"](What%27s%20New%20in%20Java%20Client.md#apple-ijdeussfjjfee). An association is "explicitly disabled" when the display object shouldn't be editable, such as in the case where the display object simply displays the results of a search. |

__EODisplayGroup (EOInterface/EODisplayGroup.h)__

| __New or Changed API__ | __Description__ |
| `globalDefaultStringMatchOperator` | A static/class method that returns the default operator used for matching strings, one of `caseInsensitiveLike` or `like` |
| `setGlobalDefaultStringMatchOperator` (Java)  `setGlobalDefaultStringMatchOperator:` (Objective-C) | A static/class method that sets the default operator for instances to use for string matching. |
| `globalDefaultStringMatchFormat` | A static/class method that returns the default format used for matching strings ("`%@*`", for example). |
| `setGlobalDefaultStringMatchFormat` (Java)  `setGlobalDefaultStringMatchFormat:` (Objective-C) | A static/class method that sets the default format for instances to use for string matching. |
| `globalDefaultForValidatesChangesImmediately` | A static/class method that returns `true`/`YES` if instances validate immediately by default. |
| `setGlobalDefaultForValidatesChangesImmediately` (Java)  `setGlobalDefaultForValidatesChangesImmediately:` (Objective-C) | A static/class method that sets the default validation behavior for instances. |

## Deprecated API

Nested transactions are no longer supported. EOF never actually
used nested transactions. Furthermore, the concrete adaptors were
not guaranteed to support them, especially since the SQL/92 standard
doesn't allow nested transactions. New features in EOF 4.5 make nested
transactions impossible to support.

Consequently, the following methods are deprecated.

__EOAdaptorContext (EOAccess/EODeprecated.h)__

| __Deprecated API__ | __New API or Workaround__ |
| `canNestTransactions:` | None.   No adaptor can nest transactions. |
| `transactionNestingLevel` | `hasOpenTransaction`  Returns `true`/`YES` if a transaction is open (begun but not yet committed or rolled back). |

For backwards compatibility, the Sybase Adaptor still allows
you to attempt to begin a nested transaction, but the implementation
ignores the nesting.

[!](What%27s%20New%20in%20WebObjects%204.5.md)
