---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeltaDoc/Introduction.html
archived_at: '2026-07-15T08:04:35.585149Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
What's New in WebObjects

---

[!](What%27s%20New%20in%20WebObjects%204.5.md)

# Introduction

This document describes changes made to WebObjects between
release 4.5 and 4.0. It describes changes made to existing features
and describes new features you may want to start using in your applications

## Compatibility with WebObjects 4.0

WebObjects 4.5 is compile-compatible with WebObjects 4.0.
You should be able to run most WebObjects 4.0 applications by simply
rebuilding them using WebObjects 4.5. Note that Direct To Web and
Java Client applications require some additional effort to convert to
WebObjects 4.5; see the _WebObjects 4.5 Post-Installation
Instructions_ for more information on converting your
existing applications.

## Changes in WebObjects 4.5

This section describes the primary changes to WebObjects for
the 4.5 release, including Enterprise Objects Framework (EOF), which
is considered part of WebObjects 4.5.

### Platform and Language Support

WebObjects makes the following improvements to platform and
language support in release 4.5:

- WebObjects applications written in Java are now
  supported on HP-UX.
- WebObjects now supports JDK 1.1.8 on Windows NT and on Solaris
  (1.1.7 on HP-UX).
- On Solaris and HP-UX, WebObjects no longer needs to be installed
  into
  /opt/Apple.

|  |
| --- |
| __Note:__ HP-UX 10.20 is no longer supported; WebObjects 4.5 requires HP-UX 11.0. |

### Deploying WebObjects Applications

In addition to the changes listed under [Platform and Language Support](#apple-ijauqqsgifcue) (above),
the following changes have been made to ease the deployment of WebObjects
applications:

- Web server adaptors can now get their configuration
  information from a file on the local machine, a file on another
  machine running a web server, from `wotaskd` (the replacement
  for MonitorProxy), or from other machines on the subnet running WebObjects
  via a new multicast mechanism.
- Many of the responsibilities formerly assumed by Monitor are
  now handled by `wotaskd` (each
  host involved in a WebObjects deployment now runs `wotaskd`).
  Monitor now simply changes settings in your deployment environment.

### Profiling and Tuning Applications

WebObjects 4.5 provides many new features to help you profile
applications, decrease their memory usage, and increase their speed.
This section provides an overview of the features and tells you
where to go for more information.

#### Profiling

WebObjects 4.5 introduces a new feature to help you profile
your applications. event logging. A new event logging system records
and displays how long certain operations in an application take.
The measurements allow you to profile an application and optimize its
execution time. For this, the EOF and WebObjects frameworks instrument
key portions of their code to measure the elapsed time of functions
and methods. You can instrument key portions of your code as well.
To learn how to use this feature, see ["Event Logging"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoq2gi5cuk) in the chapter [What's New in Enterprise Objects Framework](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscjjbeue).

#### Tuning

There are many new features to help tune your application.
They are:

- Object sharing

   EOF 4.5 introduces a new
  technique for sharing read-only enterprise objects. The new subclass
  of EOEditingContext, EOSharedEditingContext, defines a mechanism
  that allows editing contexts to share enterprise objects for reading.
  This mechanism can reduce both the number of fetches an application
  makes and the amount of redundant data it requires. See the section ["Object Sharing"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoq2iifeuc) in the chapter [What's New in Enterprise Objects Framework](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscjjbeue).
- Subclassing EOGenericRecord

   EOF 4.5 adds a new option
  for creating custom enterprise objects: rather than creating a subclass
  of EOCustomObject (Java) or NSObject (Objective-C), you can now
  subclass EOGenericRecord.

   This feature is most significant
  in applications that use the Java bridge. By default, a subclass
  of EOGenericRecord stores its properties in a dictionary on the
  Objective-C side of the bridge instead of in individual instance
  variables on the Java side. This allows EOF to access enterprise
  object properties with many fewer trips across the bridge, which
  reduces memory usage and improves performance.

   See the
  section ["Subclassing EOGenericRecord"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeorckjbbui) in
  the chapter [What's New in Enterprise Objects Framework](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscjjbeue).
- Deferred faulting

   EOF uses faults as stand-ins for objects
  whose data has not yet been fetched. Although fault creation is
  much faster than fetching, fault instantiation still takes time.
  To improve performance, EOF 4.5 has the ability to use __deferred
  faults__ (which are more efficient) for enterprise object
  classes that enable the feature. See the section ["Deferred Faulting"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoqsgijfee) in
  the chapter [What's New in Enterprise Objects Framework](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscjjbeue).
- Snapshot reference counting

   This is a new feature that
  removes snapshots from an EODatabase when they are no longer used
  by any enterprise objects in an application. This feature reduces
  the memory footprint of WebObjects applications. See the section ["Snapshot Reference Counting"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeorcbijeus) in the chapter [What's New in Enterprise Objects Framework](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscjjbeue).

### Tools Improvements

- WebObjects Builder's user interface has been
  significantly enhanced and should now be even easier to use. See
  the chapter ["WebObjects Tools Changes"](WebObjects%20Tools%20Changes.md#apple-ijbeqrsbivauo).
- EOModeler supports synchronization of a database schema with
  the current state of a model. See the section ["Schema Synchronization"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoqsjivbuk) in chapter [What's New in Enterprise Objects Framework](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscjjbeue).

### Object Modeling Improvements

EOF 4.5 adds the following features that improve object modeling:

- Better handling of missing faults

   When a
  fault fires but doesn't have a corresponding row in the database,
  an exception isn't automatically thrown. An exception is thrown
  only if the application attempts to make changes to the missing
  fault. See ["Handling Missing Faults"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoq2hivfeo).
- Handling of ambiguous to-one relationships in Java

   If
  you enable deferred faulting-a new feature in EOF 4.5-you can
  have to-one relationships to non-leaf entities in an inheritance
  hierarchy. This arrangement was impossible without workarounds in
  earlier versions. See ["Deferred Faulting"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoqsgijfee).
- Enterprise object classes are more flexible and easier to
  maintain

   You can now subclass EOGenericRecord, which can benefit
  the design of your enterprise objects. See ["Subclassing EOGenericRecord"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeorckjbbui).

### Managing Stale Data

EOF 4.5 adds a snapshot timestamping feature to help you keep
your application's data fresh. It updates snapshots when fetching
and allows an editing context to request that the snapshots used
to build enterprise objects are no older than a particular timestamp.
This has the effect of refreshing snapshots periodically, keeping
the application's view more up-to-date with the database. See ["Snapshot Timestamping"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoqscivcum).

### Automatic Database Reconnection

In EOF 4.5, a concrete adaptor can now implement methods that
cause EOF to automatically attempt to reconnect to a database server
when a connection is unexpectedly dropped. This behavior handles
the problem of transient communication failures. By default reconnection
is attempted by all of the adaptors that ship with EOF 4.5. See
the section ["Automatic Database Reconnection"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoq2hjfeuo) in
the chapter [What's New in Enterprise Objects Framework](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscjjbeue).

### Direct to Web

Direct to Web now allows you to create your own visual style
and exposes a great deal of new API. For more information, see the
section ["Direct to Web Changes"](WebObjects%20Tools%20Changes.md#apple-ijbeqq2eirceu) in
the chapter [WebObjects Tools Changes](WebObjects%20Tools%20Changes.md#apple-ijbeqrsbivauo).

### Java Client

Java Client has been extended considerably, including the
following:

- The foundation layer (com.apple.client.foundation)
  contains a new number formatter based on NSNumberFormatter and adds
  an NSUndoManager class, which is analogous to the server side class.
- The control layer (com.apple.client.eocontrol) is more complete.
- The distribution layer (com.apple.client.eodistribution on
  the client side and com.apple.yellow.eodistribution on the server
  side) now provides support for encrypted client/server communication
  and for managing user defaults.
- The interface layer (com.apple.client.eointerface) adds support
  for table cell editing and for displaying images and QuickTime media.

Additionally, Java Client now has a new user interface generation
layer, Direct to Java Client, which is comparable to WebObjects'
Direct to Web.

For more information on changes to Java Client, see the chapter ["What's New in Java Client"](What%27s%20New%20in%20Java%20Client.md#apple-ijdeuskjiffem).

### LDAP Adaptor

EOF 4.5 comes with a new sample adaptor: the LDAP adaptor.
The adaptor provides a simple way to verify a user's password
on the Web with an LDAP server. For more information, see the section ["LDAP Adaptor Example"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoqsjijeem) in the chapter [What's New in Enterprise Objects Framework](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscjjbeue).

[!](What%27s%20New%20in%20WebObjects%204.5.md)
