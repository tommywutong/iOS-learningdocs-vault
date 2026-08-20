---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/More/EODatabaseContext.html
archived_at: '2026-07-15T08:11:34.816290Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md) 

# EODatabaseContext

## EODatabaseContext's Interaction with Other Classes

The relationship between EODatabaseContext and other classes
in the control and access layers is illustrated in [Figure 0-3](#apple-incumrkfifaus).

__The Role of an
EODatabaseContext__

![[image: ../Art/DbcnTxt.eps]](../Art/DbcnTxt.GIF)

As a subclass of EOCooperatingObjectStore, EODatabaseContext
acts as one of possibly several EOCooperatingObjectStores for an
EOObjectStoreCoordinator, which mediates between EOEditingContexts
and EOCooperatingObjectStores. (EOObjectStore, EOCooperatingObjectStore,
and EOObjectStoreCoordinator are provided by the control layer.)

An EODatabaseContext creates an EOAdaptorContext when initialized,
and uses this object to communicate with the database server.

## Creating and Using an EODatabaseContext

Though you can create an EODatabaseContext explicitly by using
the class method [registeredDatabaseContextForModel:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c64tfm5uxg5dfojswirdborqweyltmvbw63tumv4hirtpojgw6zdfnq5gkzdjoruw4z2dn5xhizlyoq5a),
you should rarely need to do so. If you're using the "higher-level"
objects EOEditingContexts (EOControl) and EODatabaseDataSources,
the database contexts those objects need are created automatically,
on demand. When you create database data source (typically for use
with a display group-the interface layer's EODisplayGroup or
WebObject's WODisplayGroup), it registers a database context that's
capable of fetching objects for the data source's entities. If
objects fetched into an editing context (described more in the following
section) have references to objects from EOModels that are based
on another database, an EODatabaseContext is creates and registered
for each of the additional databases.

EODatabaseContexts are created on demand when an EOObjectStoreCoordinator
(EOControl) posts an `EOCooperatingObjectStoreNeeded` notification.
The EODatabaseContext class registers for the notification, and
it provides the coordinator with a new EODatabaseContext instance
that can handle the request. For more discussion of this topic,
see the chapter "Application Configurations" in the _Enterprise
Objects Framework Developer's Guide_.

For the most part, you don't need to programmatically interact
with an EODatabaseContext. However, some of the reasons you might
want to are as follows:

- To implement your own locking strategy, either
  application-wide, or on a per-fetch basis. This is described in
  the section ["Updating And Locking Strategies"](#apple-inbuuq2hjjauo).
- To do performance tuning, which is described in the section ["Faulting"](#apple-ijduurcjjfdus).
- To intervene when objects are created and fetched to provide
  custom behavior. This is described in the section ["Delegate Methods"](#apple-ijduuq2kinbuk),
  and in the individual delegate method descriptions in the section ["Instance Methods" (page 462)](EODatabaseContext%20Delegate.md#apple-indeeqsciffeo).

## Fetching and Saving Objects

Conceptually, an EODatabaseContext fetches and saves objects
on behalf of an EOEditingContext (EOControl). However, the two objects
don't interact with each other directly-an EOObjectStoreCoordinator
(EOControl) acts as a mediator between them. The relationship between EOEditingContext,
EOObjectStoreCoordinator, and EODatabaseContext is illustrated in [Figure 0-4](#apple-incumrkcjffec). This
configuration includes one EOObjectStoreCoordinator, and can include
one or more EOEditingContexts, and one or more EODatabaseContexts.

__EOEditingContexts,
EOObjectStoreCoordinators, and EODatabaseContexts__

![[image: ../Art/DBBASC2.eps]](../Art/DBBASC2.GIF)

When an editing context fetches objects, the request is passed
through the coordinator, which forwards it to the appropriate database
context based on the fetch specification or global ID. When the
database context receives a request to fetch or write information
to the database, it tries to use one of its EODatabaseChannels.
If all of its channels are busy, it broadcasts an [EODatabaseChannelNeededNotification](EODatabaseContext-2.md#apple-irauorcgirdem) in
the hopes that an observer can provide a new channel or that an
existing channel can be freed up. This observer could be a manager
that decides how many database cursors can be opened by a particular
client.

EODatabaseContext knows how to interact with other EOCooperatingObjectStores
to save changes made to an object graph in more than one database
server. For a more detailed discussion of this subject, see the
class specifications for EOObjectStoreCoordinator and EOCooperatingObjectStore.

## Using a Custom Query

EODatabaseContext defines a hint for use with an EOFetchSpecification
(EOControl) in the [objectsWithFetchSpecification:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2) method.
Named by the key `EOCustomQueryExpressionHintKey`,
the hint's value is a SQL string for performing the fetch. The expression
must query the same attributes in the same order that Enterprise
Objects Framework would if it were generating the SELECT expression
dynamically. If this key is supplied, other characteristics of the
EOFetchSpecification such as __isDeep__, __qualifier__,
and __sortOrderings__ are ignored-in that
sense this key is more of a directive than a hint. For more information
on hint keys, see the method description for __objectsWithFetchSpecification:editingContext:__.

## Faulting

When an EODatabaseContext fetches an object, it examines the
relationships defined in the model and creates objects representing
the destinations of the fetched object's relationships. For example,
if you fetch an employee object, you can ask for its manager and
immediately receive an object; you don't have to get the manager's
employee ID from the object you just fetched and fetch the manager
yourself.

However, EODatabaseContext doesn't immediately fetch data
for the destination objects of relationships since fetching is fairly
expensive. To avoid this waste of time and resources, the destination
objects are created as EOFault objects which act as placeholders.
EOFaults (or faults) come in two varieties: single object faults
for to-one relationships, and array faults for to-many relationships.

When an EOFault is accessed (sent a message), it triggers
its EODatabaseContext to fetch its data and transform it into an
instance of the appropriate object class. This preserves both the
object's __id__ and its EOGlobalID.

You can fine-tune faulting behavior for additional performance
gains by using two different mechanisms: batch faulting, and prefetching
relationships.

## Batch Faulting

When you access a fault, its data is fetched from the database.
However, triggering one fault has no effect on other faults-it
just fetches the object or array of objects for the one fault. You
can take advantage of this expensive round trip to the database
server by batching faults together. EODatabaseContext provides the [batchFetchRelationship:forSourceObjects:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmjqxiy3iizsxiy3ikjswyylunfxw443infyduztpojjw65lsmnsu6ytkmvrxi4z2mvsgs5djnztug33oorsxq5b2) method for
doing this. For example, given an array of Employee objects, this
method can fetch all of their departments with one round trip to
the server, rather than asking the server for each of the employee's departments
individually. You can use the delegate methods [databaseContext:shouldFetchArrayFault:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbaxe4tbpfdgc5lmoq5a) and [databaseContext:shouldFetchObjectFault:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbhwe2tfmn2emylvnr2du) to
fine-tune batch faulting behavior.

You can also set batch faulting in an EOModel. In that approach,
you specify the _number_ of faults
that should be triggered along with the first fault; you don't
actually control which faults are triggered the way you do with __batchFetchRelationship:forSourceObjects:editingContext:__.
For more information on setting batch faulting in an EOModel, see
the book _Enterprise Objects Framework Tools and Techniques_.

## Delegate Methods

An EODatabaseContext shares its delegate with its EODatabaseChannels.
These delegate methods are actually sent from EODatabaseChannel,
but they're defined in EODatabaseContext for ease of access:

You can use the EODatabaseContext delegate methods to intervene
when objects are created and when they're fetched from the database.
This gives you more fine-grained control over such issues as how
an object's primary key is generated ( [databaseContext:newPrimaryKeyForObject:entity:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2nzsxoudsnfwwc4tzjnsxsrtpojhwe2tfmn2duzlooruxi6j2)),
how and if objects are locked ( [databaseContext:shouldLockObjectWithGlobalID:snapshot:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrgg6y3lj5rguzldorlws5dii5wg6ytbnreuiottnzqxa43in52du)),
what fetch specification is used to fetch objects ( [databaseContext:shouldSelectObjectsWithFetchSpecification:databaseChannel:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrjwk3dfmn2e6ytkmvrxi42xnf2gqrtforrwqu3qmvrwsztjmnqxi2lpny5giylumfrgc43finugc3tomvwdu)),
how batch faulting is performed ( [databaseContext:shouldFetchArrayFault:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbaxe4tbpfdgc5lmoq5a) and [databaseContext:shouldFetchObjectFault:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2onug65lmmrdgk5ddnbhwe2tfmn2emylvnr2du)),
and so on. For more information, see the individual delegate method
descriptions in the section ["Instance Methods" (page 462)](EODatabaseContext%20Delegate.md#apple-indeeqsciffeo).

## Snapshots

An EODatabase records snapshots for its EODatabaseContexts.
These snapshots form the application's view of the current state
of the database server. This global view is overridden locally by
database contexts, which form their own snapshots as they make changes
during a transaction. When a database context commits its top-level
transaction, it reconciles all changed snapshots with the global
view of the database object, so that other database contexts (except
those with open transactions) immediately use the new snapshots
as well.

## Updating And Locking Strategies

EODatabaseContext supports three updating strategies defined by
the EOUpdateStrategy type as integer values:

|  |  |
| --- | --- |
| __Type__ | __Description__ |
| `EOUpdateWithOptimisticLocking` | The default update strategy. Under optimistic locking, objects aren't locked immediately on being fetched from the server. Instead, whenever you attempt to save updates to an object in the database, the object's snapshot is used to ensure that the values in the corresponding database row haven't changed since the object was fetched. As long as the snapshot matches the values in the database, the update is allowed to proceed. |
| `EOUpdateWithPessimisticLocking` | Causes objects to be locked in the database when they're selected. This ensures that no one else can modify the objects until the transaction ends. However, this doesn't necessarily mean that either the select or the update operation will succeed. |
| `EOUpdateWithNoLocking` | Objects are never locked. No comparisons are made between the snapshot and the row to ensure that the values in the corresponding database row haven't changed since the object was fetched. |

EODatabaseContext also supports "on-demand" locking, in
which specific optimistic locks can be promoted to database locks
during the course of program execution. You can either use [lockObjectWithGlobalID:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du) to
lock a database row for a particular object, or [objectsWithFetchSpecification:editingContext:](EODatabaseContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2) to
fetch objects with a fetch specification that includes locking.

For more discussion of locking strategies, see the chapter
"Behind the Scenes" in the _Enterprise Objects Framework
Developer's Guide_.

:

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
