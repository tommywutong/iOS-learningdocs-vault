---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/EODefaults.html
archived_at: '2026-07-15T08:14:39.360412Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

# Enterprise Objects Framework User Defaults

This document lists the user defaults that Enterprise Objects
Framework uses to customize its behavior. For information on how
to set these defaults, see the NSUserDefaults class specification
in the _Foundation Reference._

- [Defaults for Enterprise Objects Framework](#apple-ivhum)
- [Defaults for EOModeler](#apple-ivhu2t2eivgekuq)

## Defaults for Enterprise Objects Framework

The following table lists the defaults used to customize the
behavior of the classes in the Framework.

|  |  |
| --- | --- |
| __Default Name__ | __Description__ |
| EOAdaptorDebugEnabled | A boolean value that determines whether the access layer logs database server interactions, including connection attempts, transaction activity (begin, rollback, commit), and SQL statements (SELECT, UPDATE, and so on). The default is NO, not to log. For more information, see the EOAdaptorContext methods: __setDebugEnabledDefault__, __debugEnabledDefault__. |
| EOAdaptorQuotesExternalNames | A boolean value that determines whether EOSQLExpressions quote external names when they are referenced in SQL statements. The default behavior is NO, not to quote. For more information, see the EOSQLExpression methods __setUseQuotedExternalNames__ and __useQuotedExternalNames__ |
| EOAdaptorUseBindVariables | A boolean value that determines whether the access layer's SQL generation process uses bind variables (for Oracle and Informix). The default is YES, to use bind variables. For more information, see the EOSQLExpression methods __setUseBindVariables__ and __useBindVariables__. |
| EODeferredFaultDebugLevel | An integer value that the determines the level of logging the access layer performs as it creates and fires deferred faults. A value of 0 (the default) disables logging, a value of 1 logs messages when deferred faults are created, and a value of 2 or greater logs messages when deferred faults are created or fired. It can be helpful to enable logging when you're debugging a custom enterprise object class that uses deferred fault creation. |
| EOEventLoggingEnabled | A boolean value that determines whether event logging is enabled for event classes as they are registered. For more information, see the EOEventCenter method __registerEventClass__ (in Objective-C, __registerEventClass:classPointer:__ and __registerEventClass:handler:__). The default is NO, logging isn't enabled. |
| EOEventLoggingLimit | An integer value that sets the maximum number of events the event logging system logs. When the logging limit is reached, the logging system attempts to purge old events before logging new ones. If the system is unable to purge old events, event logging is aborted. The default logging limit is 200,000. For more information, see the EOEventCenter method __markStartOfEvent__. |
| EOEventLoggingOverflowDisplay | A boolean value that determines whether the event logging system logs a message when the event logging limit is reached. If YES, it logs messages when the event center truncates the log and also when event logging is aborted due to overflow. |
| EOFDebugEditingContext | A boolean value that determines whether the control layer logs a message when an object is changed. The logging occurs as the result of registering an undo operation with an undo manager, and the message has the form "Record Undo for object...". The default is NO, not to log messages. |
| EOLockingDebugEnabled | A boolean value that determines whether Enterprise Objects Framework logs messages when code that needs to be protected by a lock:  - Is accessed when no lock is in place - Is accessed by a thread that isn't the lock holder |
| NSProjectSearchPath | An array of paths in which EOAccess searches for framework project directories that contain models. The default is "../..", so during development, your application uses changes made to your project's model without rebuilding. |

## Defaults for EOModeler

The following table lists the defaults used to customize the
behavior of EOModeler.

|  |  |
| --- | --- |
| __Default Name__ | __Description__ |
| BundlesToLoad | An array that lists the paths in which EOModeler looks for extensions. Remember to include parentheses when you set it. For example:     defaults write EOModeler BundlesToLoad "(/System/Developer/Applications/   EOModeler.app/Resources/DiagramEditor.bundle, $HOME/eoexamples/ModelerBundle/ModelerBundle.bundle) " |
| DisableAdvancedOptions | A boolean value that determines whether EOModeler runs in simplified mode. If set to YES, the advanced inspectors don't appear, the choices of table view columns is limited, and so on. The default is NO. |
| DisableAttributeDetails | A boolean value that determines whether the consistency checker verifies attribute definitions. It verifies that:  - Attributes with NSNumber as a value class have   a value type defined. - That attributes with a custom value class have a value factory   method and a adaptor value conversion method set. - The source attributes of a relationship that propagate primary   keys contain the source entity's primary key attributes; that   the destination attributes contain the primary key attributes of   the destination entity, and that the inverse relationship doesn't   also propagate primary key.  The default value is NO, the consistency check is not disabled (the check is performed). You can set this default in EOModeler's preferences panel. |
| DisableConsistencyCheckOnSave | A boolean value that determines whether EOModeler runs the consistency checker when a model is saved. The default value is NO, the consistency check is not disabled (the check is performed). You can set this default in EOModeler's preferences panel. |
| DisableEntityStoredProcedure | A boolean value that determines whether the consistency checker verifies that an entity's stored procedures (for performing a particular operation) match the entity's attributes. The default value is NO, the consistency check is not disabled (the check is performed). You can set this default in EOModeler's preferences panel. |
| DisableExternalNameCheck | A boolean value that determines whether the consistency checker verifies the existence of external names in entities and attributes (and the existence of a value class for attributes). The default value is NO, the consistency check is not disabled (the check is performed). You can set this default in EOModeler's preferences panel. |
| DisableInheritanceCheck | A boolean value that determines whether the consistency checker verifies entity inheritance relationships. It verifies that:  - All the attributes in the parent entity exist   in the child. - The relationships in the parent exist in the child, and their   relationship definitions match. - The primary key definition in the parent matches the primary   key definition in the child. - The parent and child have restricting qualifiers if their   columns reside in the same table.  The default value is NO, the consistency check is not disabled (the check is performed). You can set this default in EOModeler's preferences panel. |
| DisablePrimaryKeyCheck | A boolean value that determines whether the consistency checker verifies the existence of primary key definitions. The default value is NO, the consistency check is not disabled (the check is performed). You can set this default in EOModeler's preferences panel. |
| DisableRelationshipCheck | A boolean value that determines whether the consistency checker verifies relationship definitions. It verifies that:  - All relationships have at least one join defined. - The destination attributes of to one relationships are the   primary keys of the destination entities. - The source attributes of a relationship that propagate primary   keys contain the source entity's primary key attributes; that   the destination attributes contain the primary key attributes of   the destination entity, and that the inverse relationship doesn't   also propagate primary key.  The default value is NO, the consistency check is not disabled (the check is performed). You can set this default in EOModeler's preferences panel. |
| DisableStoredProcedureCheck | A boolean value that determines whether the consistency checker verifies the existence of external names for stored procedures and their attributes. The default value is NO, the consistency check is not disabled (the check is performed). You can set this default in EOModeler's preferences panel. |
| RecordFetchLimit | An integer that specifies how many rows the Data Browser fetches before asking users if they want to fetch all, fetch another _n_ rows, or stop fetching. The default is 100. |
| SkipBeautifyNamesOnModelCreation | A boolean value that determines the naming scheme used for entity and attribute names in new models. If YES, EOModeler uses the database table and column names as the entity and attribute names (including case). If NO, EOModeler _beautifies_ the names as described in the EOEntity and EOAttribute methods __beautifyName__. The default is NO. |

[Top](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/EODefaults.html#top)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
